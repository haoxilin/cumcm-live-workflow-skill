# -*- coding: utf-8 -*-
"""
PDF 成品结构程序化测量模板（PyMuPDF）
======================================
用途：论文 PDF 交付前做结构体检：
  - 每页首行/字数 → 判断摘要是否单页、正文页码范围、附录边界
  - bbox 检测表格/内容是否越界（max x ≤ 右边距）
  - PDF 元数据匿名检查（author/title 应为空）
  - compact 去空白匹配关键数字（规避字体间距导致匹配失败）

用法：
  python verify_pdf_metrics.py <论文.pdf> [关键数字1 关键数字2 ...]
"""
import sys
import re
import fitz

RIGHT_MARGIN_CM = 3.17   # 按你的页边距修改
CM = 28.3465             # 1cm ≈ 28.35pt


def verify(path, key_numbers=()):
    doc = fitz.open(path)
    print(f'页数: {len(doc)}')

    # 1) 结构：每页首行 + 字数
    for i, page in enumerate(doc):
        lines = [l for l in page.get_text().split('\n') if l.strip()]
        head = lines[0][:36] if lines else '(空)'
        print(f'  p{i+1}: {head} | {len(page.get_text())}字符')

    # 2) 越界检测
    for i, page in enumerate(doc):
        words = page.get_text('words')
        if not words:
            continue
        maxx = max(w[2] for w in words)
        limit = page.rect.width - RIGHT_MARGIN_CM * CM
        if maxx > limit + 1:
            print(f'  ⚠ p{i+1}: 内容越界 max_x={maxx:.1f} > 右边距 {limit:.1f}')

    # 3) 元数据匿名
    md = doc.metadata
    leak = {k: v for k, v in md.items() if v and k in ('title', 'author', 'subject', 'keywords')}
    print(f'  元数据: {"OK(空)" if not leak else "⚠ 有信息: " + str(leak)}')

    # 4) 关键数字出现次数（compact 去空白）
    full = re.sub(r'\s+', '', '\n'.join(p.get_text() for p in doc))
    for num in key_numbers:
        n = full.count(str(num))
        print(f'  关键数字 {num}: {n} 次')

    # 5) 未定义引用检查
    print(f'  未定义引用(??): {full.count("??")}')

    # 6) 摘要页判断（第1页是否只有摘要内容）
    p1 = re.sub(r'\s+', '', doc[0].get_text())
    print(f'  第1页含"关键词": {"关键词" in p1} | 含"问题重述": {"问题重述" in p1} (应为False=摘要未溢出)')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('用法: python verify_pdf_metrics.py <论文.pdf> [关键数字...]')
        sys.exit(1)
    verify(sys.argv[1], sys.argv[2:])
