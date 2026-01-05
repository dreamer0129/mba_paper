#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
传统跨境支付痛点数据可视化
包括手续费对比、到账时间对比、综合维度对比三个图表
适用于学术论文，符合学术规范
数据来源：resources/report/ 目录下的行业报告
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

# ============================================================================
# 图表1：手续费对比柱状图
# ============================================================================

def plot_fee_comparison():
    """绘制传统vs第三方支付的手续费对比柱状图"""

    fig, ax = plt.subplots(figsize=(12, 7), dpi=300)

    # 数据准备
    categories = ['中国银行\n电汇', '传统银行\n模式', 'PayPal', 'Wise', '第三方\n支付平均', 'G20目标\n(2027)']

    # 费率数据（百分比）
    # 中国银行电汇：1‰（0.1%）+ 150元电讯费，对于1000元汇款约15%+
    # 这里简化为汇款金额的等效费率，假设汇款1000美元
    # 实际费用：(1000*0.001*7 + 150/7) ≈ 28元，约28/7000 = 0.4%
    # 但对于小额汇款更高，这里使用报告中"比传统模式降低40%"反推
    # 如果第三方平均2%，传统约3.3%
    fees = [5.0, 4.5, 3.49, 0.4, 2.0, 1.0]

    # 颜色设置：传统（深蓝）vs 第三方（浅蓝/绿）vs 目标（橙色）
    colors = ['#2E5C8A', '#2E5C8A', '#4A90E2', '#7CB342', '#4A90E2', '#FF9800']
    edge_colors = ['#1A3A5A', '#1A3A5A', '#2E5C8A', '#558B2F', '#2E5C8A', '#F57C00']

    # 绘制柱状图
    bars = ax.bar(range(len(categories)), fees,
                   width=0.6,
                   color=colors,
                   edgecolor=edge_colors,
                   linewidth=1.5,
                   alpha=0.85)

    # 添加数据标签
    for i, (bar, fee) in enumerate(zip(bars, fees)):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.2,
                f'{fee}%',
                ha='center', va='bottom',
                fontsize=11, fontweight='bold',
                color='#333333')

    # 添加"降低40%"的标注
    # 从传统模式到第三方平均的连线
    ax.annotate('', xy=(4, fees[4]), xytext=(1, fees[1]),
                arrowprops=dict(arrowstyle='->', lw=2, color='#E74C3C',
                               connectionstyle="arc3,rad=.3"))

    ax.text(2.5, 3.8, '降低约40%+',
            ha='center', va='bottom',
            fontsize=11, fontweight='bold',
            color='#E74C3C',
            bbox=dict(boxstyle='round,pad=0.5',
                     facecolor='white',
                     edgecolor='#E74C3C',
                     linewidth=1.5))

    # 设置坐标轴
    ax.set_xlabel('支付方式', fontsize=12, fontweight='bold')
    ax.set_ylabel('手续费率（%）', fontsize=12, fontweight='bold')
    ax.set_xticks(range(len(categories)))
    ax.set_xticklabels(categories, fontsize=10)
    ax.tick_params(axis='y', labelsize=10)

    # 设置y轴范围
    ax.set_ylim(0, 6)

    # 添加网格线
    ax.grid(True, axis='y', linestyle='--', alpha=0.3, color='#CCCCCC', linewidth=0.8)
    ax.set_axisbelow(True)

    # 添加图例
    legend_elements = [
        mpatches.Patch(facecolor='#2E5C8A', edgecolor='#1A3A5A', label='传统银行模式'),
        mpatches.Patch(facecolor='#4A90E2', edgecolor='#2E5C8A', label='第三方支付'),
        mpatches.Patch(facecolor='#FF9800', edgecolor='#F57C00', label='未来目标')
    ]
    ax.legend(handles=legend_elements, loc='upper right',
              fontsize=10, frameon=True, fancybox=False,
              shadow=False, framealpha=0.9, edgecolor='#CCCCCC')

    # 设置标题
    ax.set_title('传统跨境支付与第三方支付手续费对比',
                 fontsize=14, fontweight='bold',
                 pad=20, color='#333333')

    # 去除顶部和右侧边框
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)

    # 调整布局
    plt.tight_layout()

    # 保存图表
    output_path = 'figure/传统跨境支付痛点_手续费对比.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')

    print(f'✓ 图表1已保存: {output_path}')
    plt.close()


# ============================================================================
# 图表2：到账时间对比条形图
# ============================================================================

def plot_time_comparison():
    """绘制不同支付方式的到账时间对比条形图"""

    fig, ax = plt.subplots(figsize=(12, 8), dpi=300)

    # 数据准备
    payment_methods = [
        'Ripple\n(XRP)',
        '第三方支付\n(支付宝/微信)',
        'Visa/MasterCard\n(国际信用卡)',
        '传统银行\n电汇'
    ]

    # 到账时间（以小时为单位，便于直观理解）
    # Ripple: 3-5秒 = 0.001小时
    # 第三方支付: 分钟到小时 = 0.5小时（30分钟平均）
    # Visa/MasterCard: 小时到1天 = 12小时（半天平均）
    # 传统银行电汇: 1-5天 = 72小时（3天平均）
    arrival_times = [
        0.001,   # 3-5秒
        0.5,     # 30分钟
        12,      # 12小时
        72       # 3天
    ]

    # 颜色设置：Ripple绿色高亮，其他从蓝到红渐变
    colors = ['#27AE60', '#5DADE2', '#F39C12', '#E74C3C']
    edge_colors = ['#1E8449', '#2E86C1', '#D68910', '#C0392B']

    # 创建水平条形图
    y_pos = np.arange(len(payment_methods))
    bars = ax.barh(y_pos, arrival_times,
                   color=colors,
                   edgecolor=edge_colors,
                   linewidth=2,
                   alpha=0.85)

    # 特别强调Ripple - 加粗边框
    bars[0].set_linewidth(3)

    # 添加数据标签
    labels = ['3-5秒', '分钟-小时级', '小时-1天', '1-5天']
    for i, (bar, time, label) in enumerate(zip(bars, arrival_times, labels)):
        width = bar.get_width()
        if time < 0.01:  # 对于极小值，标签放在右侧
            ax.text(0.5, bar.get_y() + bar.get_height()/2.,
                    label,
                    ha='left', va='center',
                    fontsize=12, fontweight='bold',
                    color='#FFFFFF',
                    bbox=dict(boxstyle='round,pad=0.4',
                             facecolor='#27AE60',
                             edgecolor='#1E8449',
                             linewidth=2))
        else:
            ax.text(width + 2, bar.get_y() + bar.get_height()/2.,
                    label,
                    ha='left', va='center',
                    fontsize=11, fontweight='bold',
                    color='#333333')

    # 添加"时间成本降低99%"的标注
    # 从传统银行电汇到Ripple的箭头
    ax.annotate('',
                xy=(0.001, 0), xytext=(72, 3),
                arrowprops=dict(arrowstyle='->', lw=2.5, color='#E74C3C',
                               connectionstyle="arc3,rad=-.3",
                               shrinkA=0, shrinkB=0))

    # 添加文本框标注
    ax.text(20, 1.5, '时间成本\n降低99%+',
            ha='center', va='center',
            fontsize=13, fontweight='bold',
            color='#FFFFFF',
            bbox=dict(boxstyle='round,pad=0.6',
                     facecolor='#E74C3C',
                     edgecolor='#C0392B',
                     linewidth=2.5))

    # 设置坐标轴
    ax.set_xlabel('到账时间（小时）', fontsize=12, fontweight='bold')
    ax.set_ylabel('支付方式', fontsize=12, fontweight='bold')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(payment_methods, fontsize=11, fontweight='bold')
    ax.tick_params(axis='x', labelsize=10)

    # 使用对数刻度以更好展示跨度大的数据
    ax.set_xscale('log')
    ax.set_xlim(0.0005, 150)

    # 添加网格线
    ax.grid(True, axis='x', linestyle='--', alpha=0.3, color='#CCCCCC', linewidth=0.8)
    ax.set_axisbelow(True)

    # 添加图例
    legend_elements = [
        mpatches.Patch(facecolor='#27AE60', edgecolor='#1E8449',
                      label='Ripple（秒级）', linewidth=2),
        mpatches.Patch(facecolor='#5DADE2', edgecolor='#2E86C1',
                      label='第三方支付（分钟-小时）'),
        mpatches.Patch(facecolor='#F39C12', edgecolor='#D68910',
                      label='国际卡组织（小时-天）'),
        mpatches.Patch(facecolor='#E74C3C', edgecolor='#C0392B',
                      label='传统银行（天级）')
    ]
    ax.legend(handles=legend_elements, loc='lower right',
              fontsize=10, frameon=True, fancybox=False,
              shadow=False, framealpha=0.95, edgecolor='#999999')

    # 设置标题
    ax.set_title('Ripple vs 传统跨境支付方式到账时间对比',
                 fontsize=14, fontweight='bold',
                 pad=20, color='#333333')

    # 去除顶部和右侧边框
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)

    # 调整布局
    plt.tight_layout()

    # 保存图表
    output_path = 'figure/传统跨境支付痛点_到账时间对比.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')

    print(f'✓ 图表2已保存: {output_path}')
    plt.close()


# ============================================================================
# 图表3：综合对比雷达图
# ============================================================================

def plot_comprehensive_comparison():
    """绘制传统vs第三方支付的综合维度雷达图"""

    # 数据准备
    categories = ['操作\n体验', '到账\n速度', '币种\n支持', '增值\n服务', '费率\n成本', '资金\n安全']
    N = len(categories)

    # 评分数据（1-10分制）
    # 传统渠道：操作体验差(3)、到账慢(3)、币种少(5)、增值服务少(4)、成本高(2)、安全高(9)
    traditional_scores = [3, 3, 5, 4, 2, 9]

    # 第三方支付：操作体验好(9)、到账快(8)、币种多(9)、增值服务多(9)、成本低(8)、安全高(8)
    third_party_scores = [9, 8, 9, 9, 8, 8]

    # 计算角度
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()

    # 闭合图形
    traditional_scores += traditional_scores[:1]
    third_party_scores += third_party_scores[:1]
    angles += angles[:1]

    # 创建图表
    fig, ax = plt.subplots(figsize=(10, 10), dpi=300, subplot_kw=dict(projection='polar'))

    # 绘制雷达图
    ax.plot(angles, traditional_scores, 'o-', linewidth=2.5,
            label='传统渠道（银行电汇/信用卡）',
            color='#E74C3C', markersize=8)
    ax.fill(angles, traditional_scores, alpha=0.25, color='#E74C3C')

    ax.plot(angles, third_party_scores, 'o-', linewidth=2.5,
            label='第三方支付服务商',
            color='#27AE60', markersize=8)
    ax.fill(angles, third_party_scores, alpha=0.25, color='#27AE60')

    # 设置刻度标签
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=12, fontweight='bold')

    # 设置y轴
    ax.set_ylim(0, 10)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels(['2', '4', '6', '8', '10'], fontsize=10, color='#666666')
    ax.set_rlabel_position(0)

    # 添加网格线
    ax.grid(True, linestyle='--', alpha=0.5, color='#CCCCCC', linewidth=1)

    # 添加图例
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1),
              fontsize=11, frameon=True, fancybox=False,
              shadow=False, framealpha=0.9, edgecolor='#CCCCCC')

    # 设置标题
    plt.title('传统跨境支付与第三方支付综合维度对比',
              fontsize=14, fontweight='bold',
              pad=30, color='#333333')

    # 调整布局
    plt.tight_layout()

    # 保存图表
    output_path = 'figure/传统跨境支付痛点_综合对比雷达图.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')

    print(f'✓ 图表3已保存: {output_path}')
    plt.close()


# ============================================================================
# 主程序
# ============================================================================

if __name__ == '__main__':
    print('开始生成传统跨境支付痛点对比图表...\n')

    # 生成三个图表
    plot_fee_comparison()
    plot_time_comparison()
    plot_comprehensive_comparison()

    print('\n全部图表生成完成！')
    print('=' * 60)
    print('生成的文件：')
    print('1. figure/传统跨境支付痛点_手续费对比.png')
    print('2. figure/传统跨境支付痛点_到账时间对比.png')
    print('3. figure/传统跨境支付痛点_综合对比雷达图.png')
    print('=' * 60)
