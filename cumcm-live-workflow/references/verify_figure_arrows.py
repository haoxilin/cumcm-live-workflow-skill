# -*- coding: utf-8 -*-
"""
流程图中箭头穿框检测模板（间隙条带法）
========================================
用途：检查流程图里的箭头是否错误地穿过方框内部。
背景：向上流动的箭头若写成"下框下缘→上框上缘"，会从下框底部一路贯穿整个框体，
      肉眼和普通像素检测都不可靠（文字抗锯齿像素会混入箭头色）。间隙条带法只在
      "方框之间的纯间隙"里找箭头像素，间隙无文字/边框干扰，结果可靠。

原理：
  1) 用"方框填充色"做连通域，得到每个方框的像素包围盒；
  2) 对相邻两框的间隙（y 条带），统计箭头色像素；
  3) 若间隙内箭头像素 > 阈值，说明箭头正确连接在框间；若为 0，说明箭头可能缺失
     或（更糟）穿进了框内。

用法：
  python verify_figure_arrows.py <流程图.png>
  （可选参数：--arrow '#6B7B8C' --tol 20 --box-fill 四个填充色）

注意：
  - 需要 numpy + scipy + Pillow
  - 本脚本是通用模板：把 BOX_FILL 颜色改成你流程图实际用的填充色即可复用
"""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

# ---- 按实际流程图修改 ----
BOX_FILL = [
    (0xED, 0xF1, 0xF7),   # 输入框填充
    (0xEA, 0xF2, 0xFB),   # 过程框填充
    (0xE8, 0xF6, 0xF3),   # 方法框填充
    (0xFD, 0xF3, 0xE0),   # 结果框填充
]
ARROW = (0x6B, 0x7B, 0x8C)   # 箭头颜色
ARROW_TOL = 20                # 箭头色容差（必须小于边框色与箭头色的通道差）
FILL_TOL = 30
MIN_BOX_PX = 5000             # 小于此面积的连通域视为噪声


def detect(path):
    img = np.array(Image.open(path).convert('RGB'))
    fill = np.zeros(img.shape[:2], dtype=bool)
    for c in BOX_FILL:
        fill |= np.all(np.abs(img.astype(int) - np.array(c)) <= FILL_TOL, axis=2)
    arrow = np.all(np.abs(img.astype(int) - np.array(ARROW)) <= ARROW_TOL, axis=2)

    lab, k = ndimage.label(fill)
    boxes = []
    for i in range(1, k + 1):
        m = lab == i
        if m.sum() < MIN_BOX_PX:
            continue
        ys, xs = np.where(m)
        boxes.append((int(xs.min()), int(xs.max()), int(ys.min()), int(ys.max())))
    boxes.sort(key=lambda b: (b[2], b[0]))  # 按 y 再按 x 排序

    print(f'检测到方框 {len(boxes)} 个')
    bad = 0
    # 垂直相邻的框对：检查间隙条带
    for i in range(len(boxes) - 1):
        b1, b2 = boxes[i], boxes[i + 1]
        if abs(b1[1] - b2[0]) < max(b1[1] - b1[0], b2[1] - b2[0]) * 0.5:  # x 方向有重叠
            gap_y0, gap_y1 = b1[3], b2[2]
            if gap_y1 > gap_y0:  # 有间隙
                x0 = max(b1[0], b2[0]); x1 = min(b1[1], b2[1])
                strip = arrow[gap_y0 + 2:gap_y1 - 2, x0:x1]
                c = int(strip.sum())
                tag = 'OK' if c > 80 else 'MISSING!'
                if c <= 80:
                    bad += 1
                print(f'  框{i}-{i+1} 间隙[{gap_y0},{gap_y1}) 箭头像素={c}  {tag}')
    if bad == 0:
        print('结论: 未发现缺失/穿框箭头')
    else:
        print(f'结论: {bad} 处箭头缺失或异常，请检查箭头坐标（向上流动应画在下框上缘→上框下缘之间）')
    return bad


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('用法: python verify_figure_arrows.py <流程图.png>')
        sys.exit(1)
    sys.exit(1 if detect(sys.argv[1]) else 0)
