#!/usr/bin/env python3
"""
Ripple网络节点全球分布与URL配置分析可视化脚本

生成双子图：
1. 左图：Top 15国家的节点分布（水平条形图）
2. 右图：Validator URL配置占比（饼图）
"""

import re
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 设置中文字体支持
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei', 'Noto Sans CJK SC', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

def parse_node_data(file_path):
    """解析ripple_node.md文件，提取节点分布数据"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    data = []

    # 正则表达式：匹配 "排名 国家 数字 百分比%" 模式
    # 示例: "1 🇺🇸 United States of America 196 24.02%"
    pattern = r'^\s*\d+\s+(.+?)\s+(\d+)\s+([\d.]+)%\s*$'

    for line in lines:
        match = re.match(pattern, line)
        if match:
            country_part = match.group(1).strip()
            count = int(match.group(2))
            percentage = float(match.group(3))

            # 移除emoji（保留文字国家名）
            # emoji通常是2-4字节的Unicode字符
            country = ''
            for char in country_part:
                # 保留ASCII字母、数字、空格和常见标点
                if ord(char) < 0x1F000:  # 排除emoji范围
                    country += char

            country = country.strip()

            if country:
                data.append({
                    'country': country,
                    'count': count,
                    'percentage': percentage
                })

    return pd.DataFrame(data)

def create_visualization(df, validator_total=115, url_count=34):
    """创建双子图可视化"""

    # 创建画布，双子图布局
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))
    fig.suptitle('Ripple网络节点全球分布与Validator分析',
                 fontsize=16, fontweight='bold', y=0.98)

    # ===== 左图：Top 15国家节点分布 =====
    top15 = df.head(15).copy()

    # 为Top 3设置特殊颜色
    colors = []
    for i in range(len(top15)):
        if i == 0:
            colors.append('#1f77b4')  # 深蓝
        elif i == 1:
            colors.append('#ff7f0e')  # 橙色
        elif i == 2:
            colors.append('#2ca02c')  # 绿色
        elif top15.iloc[i]['country'] == 'Unknown':
            colors.append('#d62728')  # 红色突出Unknown
        else:
            colors.append('#7f7f7f')  # 灰色

    # 绘制水平条形图（倒序显示，最高的在上面）
    bars = ax1.barh(range(len(top15)), top15['count'], color=colors, alpha=0.8)

    # 设置y轴标签（国家名称）
    ax1.set_yticks(range(len(top15)))
    ax1.set_yticklabels(top15['country'])

    # 设置x轴
    ax1.set_xlabel('节点数量', fontsize=11)
    ax1.set_xlim(0, 250)  # 设置X轴最大值为250
    ax1.set_title('节点国家分布 (Top 15)', fontsize=13, fontweight='bold', pad=10)

    # 在条形图上添加数值标签
    for i, (bar, row) in enumerate(zip(bars, top15.itertuples())):
        width = bar.get_width()
        ax1.text(width + 3, bar.get_y() + bar.get_height()/2,
                f'{int(row.count)} ({row.percentage:.1f}%)',
                ha='left', va='center', fontsize=9)

    # 反转y轴，让最大值在顶部
    ax1.invert_yaxis()

    # 添加网格线
    ax1.grid(axis='x', alpha=0.3, linestyle='--')
    ax1.set_axisbelow(True)

    # ===== 右图：URL占比饼图 =====
    url_data = [url_count, validator_total - url_count]
    labels = [f'URL\n{url_count}个', f'非URL\n{validator_total - url_count}个']
    colors_pie = ['#2ca02c', '#d62728']
    explode = (0.05, 0)  # 突出有URL的部分

    wedges, texts, autotexts = ax2.pie(url_data,
                                        labels=labels,
                                        colors=colors_pie,
                                        autopct='%1.1f%%',
                                        startangle=90,
                                        explode=explode,
                                        textprops={'fontsize': 11})

    # 设置百分比文本样式
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(12)

    ax2.set_title(f'验证节点分布\n(总计{validator_total}个)',
                 fontsize=13, fontweight='bold', pad=10)

    # 调整布局
    plt.tight_layout()

    return fig

def main():
    """主函数"""
    # 设置路径
    base_dir = Path(__file__).parent.parent.parent
    data_file = base_dir / 'resources/ripple_network/raw_data/ripple_node.md'
    output_file = base_dir / 'figure/Ripple节点全球分布与URL占比分析.png'

    # 确保输出目录存在
    output_file.parent.mkdir(parents=True, exist_ok=True)

    print("正在读取数据...")
    df = parse_node_data(data_file)

    print(f"成功解析 {len(df)} 个国家/地区的数据")
    print(f"节点总数: {df['count'].sum()}")
    print(f"\nTop 5 国家:")
    print(df.head(5)[['country', 'count', 'percentage']])

    print("\n正在生成图表...")
    fig = create_visualization(df, validator_total=115, url_count=34)

    # 保存图表
    print(f"\n保存图表到: {output_file}")
    fig.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='white')

    print("✓ 图表生成完成！")
    print(f"\n输出文件: {output_file}")
    print(f"图片尺寸: 14x6 英寸")
    print(f"分辨率: 300 DPI")

if __name__ == '__main__':
    main()
