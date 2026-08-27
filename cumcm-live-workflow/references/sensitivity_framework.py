# -*- coding: utf-8 -*-
"""
敏感性实验跑批框架模板
========================
用途：对关键参数做 ±1.5% / ±0.5% 等扰动，量化结论变化百分比，判断模型稳健性。
注意：敏感性数值必须实跑得出，禁止凭空填；响应可能正负不对称，如实呈现并解释。

用法：
  1. 实现 run_metric(params) -> 输出结论数值（如终止时刻 t*）；
  2. 改 PARAMETERS 列表（参数名/基准值/扰动比例）；
  3. python sensitivity_framework.py
"""
import copy


# ---- 按实际模型修改 ----
def run_metric(params):
    """输入参数 dict，返回一个可比较的结论数值。"""
    # 示例：替换为你的模型调用
    W = params['W']
    p = params['p']
    # 示意公式（请换成真实模型！）
    return 412.0 + (0.30 - W) * 5000 + (0.55 - p) * 3000


PARAMETERS = [
    # (名称, 基准值, 扰动比例列表)
    ('W', 0.30, [0.015, -0.015]),     # 板宽 ±1.5%
    ('p', 0.55, [0.005, -0.005]),     # 螺距 ±0.5%
]
BASE = {'W': 0.30, 'p': 0.55}


def main():
    base_val = run_metric(BASE)
    print(f'基准结论 = {base_val:.4f}')
    results = {}
    for name, base, ratios in PARAMETERS:
        for r in ratios:
            p = dict(BASE)
            p[name] = base * (1 + r)
            val = run_metric(p)
            dev = (val - base_val) / base_val * 100
            print(f'  {name} {r:+.3f} → 结论={val:.4f} ({dev:+.2f}%)')
            results[f'{name}{r:+.1%}'] = dev
    # 提示：响应可能不对称（如 +1.5% → -1.45% 而 -1.5% → +0.04%），属正常，如实写入论文并解释
    print('完成。将结果整理为三线表放入论文"敏感性分析"小节；说明中注明由脚本实算得到。')


if __name__ == '__main__':
    main()
