#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
跨境支付市场交易规模及增长情况图表重绘
适用于学术论文，符合学术规范
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import rcParams
from matplotlib.font_manager import FontProperties
import numpy as np

# 配置中文字体 - 使用字体文件路径
font_path = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
chinese_font = FontProperties(fname=font_path)

# 设置中文字体支持
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei', 'Noto Sans CJK SC', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 数据准备
years = ['2019', '2020', '2021', '2022', '2023', '2024', '2032E']
values = [134.3, 141.1, 148.3, 155.9, 190.1, 194.6, 320.0]

# 区分历史数据和预测数据
historical_years = years[:-1]  # 2019-2024
historical_values = values[:-1]
forecast_year = years[-1]  # 2032E
forecast_value = values[-1]

# 创建图表
fig, ax = plt.subplots(figsize=(12, 7), dpi=300)

# 设置x轴位置
x_pos = np.arange(len(years))

# 绘制柱状图 - 历史数据（缩小宽度）
bars_hist = ax.bar(x_pos[:-1], historical_values,
                   width=0.3,  # 从0.6缩小到0.3
                   color='#4A90E2',  # 学术蓝
                   edgecolor='#2E5C8A',
                   linewidth=1.5,
                   label='历史数据',
                   alpha=0.85)

# 绘制柱状图 - 预测数据（缩小宽度）
bars_forecast = ax.bar(x_pos[-1], forecast_value,
                       width=0.3,  # 从0.6缩小到0.3
                       color='#7CB9E8',  # 浅蓝色表示预测
                       edgecolor='#4A90E2',
                       linewidth=1.5,
                       label='预测数据',
                       alpha=0.7,
                       hatch='//')  # 添加斜线纹理区分预测数据

# 添加数据标签（保持在柱子顶部）
for i, (x, y) in enumerate(zip(x_pos, values)):
    ax.text(x, y + 8, f'{y:.1f}',
            ha='center',
            va='bottom',
            fontsize=10,
            fontweight='bold',
            color='#333333')

# 绘制增长趋势箭头（分为两段斜向箭头）
arrow_offset = 30  # 箭头在数据点上方的偏移量

# 第一段箭头：从2019年134.3指向2024年194.6（CAGR 9.0%）
ax.annotate('',
            xy=(x_pos[5], values[5] + arrow_offset),  # 2024年194.6
            xytext=(x_pos[0], values[0] + arrow_offset),  # 2019年134.3
            arrowprops=dict(arrowstyle='->',
                           lw=2.5,
                           color='#2E5C8A',
                           mutation_scale=20))

# 第一段箭头的CAGR标注
mid_x_1 = (x_pos[0] + x_pos[5]) / 2
mid_y_1 = (values[0] + values[5]) / 2 + arrow_offset + 20
ax.text(mid_x_1, mid_y_1,
        'CAGR 9.0%',
        ha='center',
        va='bottom',
        fontsize=11,
        fontweight='bold',
        color='#2E5C8A',
        bbox=dict(boxstyle='round,pad=0.5',
                 facecolor='white',
                 edgecolor='#2E5C8A',
                 linewidth=1.5,
                 alpha=0.95))

# 第二段箭头：从2024年194.6指向2032E的320.0（CAGR 6.4%）
arrow_offset_2 = 30  # 第二段箭头更高的偏移量，避免重叠

ax.annotate('',
            xy=(x_pos[6], values[6] + arrow_offset_2),  # 2032E的320.0
            xytext=(x_pos[5], values[5] + arrow_offset_2),  # 2024年194.6
            arrowprops=dict(arrowstyle='->',
                           lw=2.5,
                           color='#2E5C8A',
                           mutation_scale=20))

# 第二段箭头的CAGR标注
mid_x_2 = (x_pos[5] + x_pos[6]) / 2
mid_y_2 = (values[5] + values[6]) / 2 + arrow_offset_2 + 20
ax.text(mid_x_2, mid_y_2,
        'CAGR 6.4%',
        ha='center',
        va='bottom',
        fontsize=11,
        fontweight='bold',
        color='#2E5C8A',
        bbox=dict(boxstyle='round,pad=0.5',
                 facecolor='white',
                 edgecolor='#2E5C8A',
                 linewidth=1.5,
                 alpha=0.95))

# 设置坐标轴
ax.set_xlabel('年份', fontsize=12, fontweight='bold')
ax.set_ylabel('交易规模（万亿美元）', fontsize=12, fontweight='bold')
ax.set_xticks(x_pos)
ax.set_xticklabels(years, fontsize=11)
ax.tick_params(axis='y', labelsize=10)

# 设置y轴范围
ax.set_ylim(0, 350)

# 添加网格线
ax.grid(True, axis='y', linestyle='--', alpha=0.3, color='#CCCCCC', linewidth=0.8)
ax.set_axisbelow(True)  # 网格线在柱状图下方

# 添加图例
ax.legend(loc='upper left',
          fontsize=10,
          frameon=True,
          fancybox=False,
          shadow=False,
          framealpha=0.9,
          edgecolor='#CCCCCC')

# 设置标题
ax.set_title('跨境支付市场交易规模及增长情况',
             fontsize=14,
             fontweight='bold',
             pad=20,
             color='#333333')

# # 添加数据来源
# fig.text(0.12, 0.02, '数据来源：亿欧智库',
#          fontsize=9,
#          style='italic',
#          color='#666666')

# 去除顶部和右侧边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

# 调整布局
plt.tight_layout(rect=[0, 0.03, 1, 1])

# 保存图表
output_path = 'figure/01_跨境支付市场交易规模及增长情况_重绘.png'
plt.savefig(output_path,
            dpi=300,
            bbox_inches='tight',
            facecolor='white',
            edgecolor='none')

print(f'图表已成功保存到: {output_path}')
print(f'分辨率: 300 DPI')
print(f'格式: PNG')

# 显示图表（可选）
# plt.show()
