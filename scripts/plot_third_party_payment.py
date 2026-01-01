#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第三方跨境电商支付市场规模及同比增速图表绘制
适用于学术论文，符合学术规范
双Y轴组合图：柱状图（市场规模）+ 折线图（同比增速）
"""

import matplotlib.pyplot as plt
import numpy as np

# 配置中文字体支持
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei', 'Noto Sans CJK SC', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 数据准备
years = ['2018', '2019', '2020', '2021', '2022', '2023', '2024']
scale_values = [3478.71, 4113.83, 5485.35, 6748.16, 7772.05, 10125.43, 12165.70]  # 市场规模（亿元）
growth_rates = [None, 18.26, 33.34, 23.02, 15.17, 30.28, 20.15]  # 同比增速（%），2018年无同比数据

# 创建图表 - 双Y轴
fig, ax1 = plt.subplots(figsize=(12, 7), dpi=300)

# 设置x轴位置
x_pos = np.arange(len(years))

# ============ 绘制柱状图（左侧Y轴 - 市场规模） ============
bars = ax1.bar(x_pos, scale_values,
               width=0.5,
               color='#4A90E2',  # 学术蓝
               edgecolor='#2E5C8A',
               linewidth=1.5,
               alpha=0.85,
               label='市场规模',
               zorder=2)

# 添加柱状图数值标签
for i, (x, y) in enumerate(zip(x_pos, scale_values)):
    ax1.text(x, y + 100, f'{y:,.2f}',  # 增加偏移量从200到400，避免与折线图重叠
             ha='center',
             va='bottom',
             fontsize=9,
             fontweight='bold',
             color='#333333')

# 配置左侧Y轴（市场规模）
ax1.set_xlabel('年份', fontsize=12, fontweight='bold', color='#333333')
ax1.set_ylabel('市场交易规模（亿元人民币）', fontsize=12, fontweight='bold', color='#2E5C8A')
ax1.set_xticks(x_pos)
ax1.set_xticklabels(years, fontsize=11)
ax1.tick_params(axis='y', labelsize=10, labelcolor='#2E5C8A')
ax1.set_ylim(0, 16000)

# ============ 绘制折线图（右侧Y轴 - 同比增速） ============
ax2 = ax1.twinx()  # 创建共享X轴的第二个Y轴

# 过滤掉None值（2018年无同比数据）
valid_indices = [i for i, rate in enumerate(growth_rates) if rate is not None]
valid_x_pos = [x_pos[i] for i in valid_indices]
valid_rates = [growth_rates[i] for i in valid_indices]

# 绘制折线图
line = ax2.plot(valid_x_pos, valid_rates,
                color='#FF8C00',  # 橙色
                linewidth=2.5,
                marker='o',
                markersize=8,
                markerfacecolor='white',
                markeredgecolor='#FF8C00',
                markeredgewidth=2,
                label='同比增速',
                zorder=3)

# 添加折线图百分比标签
for x, y in zip(valid_x_pos, valid_rates):
    ax2.text(x, y + 2, f'{y:.2f}%',
             ha='center',
             va='bottom',
             fontsize=9,
             fontweight='bold',
             color='#FF8C00')

# 配置右侧Y轴（同比增速）
ax2.set_ylabel('同比增速（%）', fontsize=12, fontweight='bold', color='#333333')
ax2.tick_params(axis='y', labelsize=10, labelcolor='#333333')
ax2.set_ylim(0, 40)

# ============ 视觉美化与配置 ============

# 添加网格线（仅Y轴方向，在柱状图下方）
ax1.grid(True, axis='y', linestyle='--', alpha=0.3, color='#CCCCCC', linewidth=0.8, zorder=1)
ax1.set_axisbelow(True)

# 隐藏顶部边框
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)

# 设置边框线宽
ax1.spines['left'].set_linewidth(1.5)
ax1.spines['left'].set_color('#2E5C8A')
ax1.spines['bottom'].set_linewidth(1.5)
ax1.spines['bottom'].set_color('#333333')
ax2.spines['right'].set_linewidth(1.5)
ax2.spines['right'].set_color('#333333')

# 合并图例（双Y轴的图例）
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2,
           loc='upper left',
           fontsize=10,
           frameon=True,
           fancybox=False,
           shadow=False,
           framealpha=0.9,
           edgecolor='#CCCCCC')

# 设置标题
ax1.set_title('2018-2024年我国第三方跨境电商支付市场规模及同比增速',
              fontsize=14,
              fontweight='bold',
              pad=20,
              color='#333333')

# 调整布局
plt.tight_layout()

# 保存图表
output_path = 'figure/02_第三方跨境电商支付市场规模及增速.png'
plt.savefig(output_path,
            dpi=300,
            bbox_inches='tight',
            facecolor='white',
            edgecolor='none')

print(f'✓ 图表已成功保存到: {output_path}')
print(f'✓ 分辨率: 300 DPI')
print(f'✓ 格式: PNG')
print(f'✓ 数据范围: {years[0]}-{years[-1]}年（共{len(years)}年）')
print(f'✓ 市场规模范围: {scale_values[0]:,.2f} - {scale_values[-1]:,.2f} 亿元')

# 显示图表（可选）
# plt.show()
