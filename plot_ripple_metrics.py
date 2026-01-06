#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ripple 网络指标可视化脚本
绘制从2013年到2026年的各项关键指标随时间的变化趋势
"""

import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np

# 设置中文字体支持
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei', 'Noto Sans CJK SC', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 读取数据
with open('resources/ripple_network/raw_data/metrics.json', 'r') as f:
    data = json.load(f)

# 转换为DataFrame
records = []
for item in data:
    date = datetime.fromisoformat(item['date'].replace('Z', '+00:00'))
    metric = item['metric']
    record = {'date': date}
    record.update(metric)
    records.append(record)

df = pd.DataFrame(records)
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# 计算TPS
df['tps'] = df['tx_per_ledger'] / df['ledger_interval']

# 定义指标及其中文名称
metrics = {
    'transaction_count': '每日交易总数',
    'payments_count': '每日支付交易数',
    'transaction_success_count': '每日成功交易数',
    'accounts_created': '每日新增账户数',
    'payments_volume': '每日支付金额（XRP）',
    'fee_total': '每日手续费总额（XRP）',
    'active_accounts': '活跃账户数',
    'active_users': '活跃用户数',
    'ledger_count': '每日账本数量',
    'ledger_interval': '账本间隔时间（秒）',
    'tx_per_ledger': '每账本交易数',
    'tps': '系统TPS（交易/秒）'
}

# 创建输出目录
import os
os.makedirs('figure', exist_ok=True)


def configure_time_axis(df_plot, metric_name):
    """
    根据数据实际时间范围动态配置时间轴

    参数:
        df_plot: DataFrame，包含'date'列和指标数据（已去除NaN）
        metric_name: str，指标中文名称

    返回:
        dict或None: 包含title、major_locator、minor_locator、date_formatter、rotation
                   如果数据为空返回None
    """
    # 边界情况1：空数据
    if len(df_plot) == 0:
        return None

    # 边界情况2：单个数据点
    if len(df_plot) == 1:
        single_date = df_plot['date'].iloc[0]
        year = single_date.year
        return {
            'title': f'Ripple网络{metric_name}变化趋势（{year}年）',
            'major_locator': None,
            'minor_locator': None,
            'date_formatter': mdates.DateFormatter('%Y-%m-%d'),
            'rotation': 0
        }

    # 计算实际时间范围
    min_date = df_plot['date'].min()
    max_date = df_plot['date'].max()
    time_delta = max_date - min_date
    time_span_days = time_delta.days
    time_span_years = time_span_days / 365.25

    start_year = min_date.year
    end_year = max_date.year

    # 生成动态标题
    if start_year == end_year:
        title_suffix = f'（{start_year}年）'
    else:
        title_suffix = f'（{start_year}-{end_year}）'
    title = f'Ripple网络{metric_name}变化趋势{title_suffix}'

    # 根据时间跨度选择刻度策略
    if time_span_days < 7:
        # 少于1周：每天
        return {
            'title': title,
            'major_locator': mdates.DayLocator(interval=1),
            'minor_locator': None,
            'date_formatter': mdates.DateFormatter('%Y-%m-%d'),
            'rotation': 45
        }

    elif time_span_days < 30:
        # 少于1个月：每周
        return {
            'title': title,
            'major_locator': mdates.WeekdayLocator(interval=1),
            'minor_locator': mdates.DayLocator(interval=1),
            'date_formatter': mdates.DateFormatter('%Y-%m-%d'),
            'rotation': 45
        }

    elif time_span_years < 0.5:
        # 少于半年：每月
        return {
            'title': title,
            'major_locator': mdates.MonthLocator(interval=1),
            'minor_locator': mdates.WeekdayLocator(byweekday=mdates.MO, interval=1),
            'date_formatter': mdates.DateFormatter('%Y-%m'),
            'rotation': 45
        }

    elif time_span_years < 1:
        # 半年到1年：每2个月
        return {
            'title': title,
            'major_locator': mdates.MonthLocator(interval=2),
            'minor_locator': mdates.MonthLocator(interval=1),
            'date_formatter': mdates.DateFormatter('%Y-%m'),
            'rotation': 45
        }

    elif time_span_years < 3:
        # 1-3年：每6个月
        return {
            'title': title,
            'major_locator': mdates.MonthLocator(interval=6),
            'minor_locator': mdates.MonthLocator(interval=3),
            'date_formatter': mdates.DateFormatter('%Y-%m'),
            'rotation': 45
        }

    elif time_span_years < 5:
        # 3-5年：每年
        return {
            'title': title,
            'major_locator': mdates.YearLocator(1),
            'minor_locator': mdates.MonthLocator(interval=6),
            'date_formatter': mdates.DateFormatter('%Y'),
            'rotation': 45
        }

    elif time_span_years < 8:
        # 5-8年：每年
        return {
            'title': title,
            'major_locator': mdates.YearLocator(1),
            'minor_locator': mdates.MonthLocator(interval=6),
            'date_formatter': mdates.DateFormatter('%Y'),
            'rotation': 45
        }

    elif time_span_years < 15:
        # 8-15年：每2年
        return {
            'title': title,
            'major_locator': mdates.YearLocator(2),
            'minor_locator': mdates.YearLocator(1),
            'date_formatter': mdates.DateFormatter('%Y'),
            'rotation': 45
        }

    elif time_span_years < 25:
        # 15-25年：每3年
        return {
            'title': title,
            'major_locator': mdates.YearLocator(3),
            'minor_locator': mdates.YearLocator(1),
            'date_formatter': mdates.DateFormatter('%Y'),
            'rotation': 45
        }

    else:
        # ≥25年：每5年
        return {
            'title': title,
            'major_locator': mdates.YearLocator(5),
            'minor_locator': mdates.YearLocator(2),
            'date_formatter': mdates.DateFormatter('%Y'),
            'rotation': 45
        }


# 为每个指标绘制单独的图表
for metric_key, metric_name in metrics.items():
    if metric_key not in df.columns:
        print(f"跳过缺失的指标: {metric_name}")
        continue

    # 过滤掉NaN值
    df_plot = df[['date', metric_key]].dropna()

    if len(df_plot) == 0:
        print(f"指标 {metric_name} 无有效数据")
        continue

    # 动态配置时间轴
    axis_config = configure_time_axis(df_plot, metric_name)
    if axis_config is None:
        print(f"指标 {metric_name} 时间轴配置失败")
        continue

    fig, ax = plt.subplots(figsize=(14, 6))

    ax.plot(df_plot['date'], df_plot[metric_key], linewidth=1.5, color='#2E86AB', alpha=0.8)
    ax.set_xlabel('时间', fontsize=12)
    ax.set_ylabel(metric_name, fontsize=12)
    ax.set_title(axis_config['title'], fontsize=14, fontweight='bold')

    # 设置x轴日期格式（动态配置）
    if axis_config['major_locator']:
        ax.xaxis.set_major_locator(axis_config['major_locator'])
    if axis_config['minor_locator']:
        ax.xaxis.set_minor_locator(axis_config['minor_locator'])
    ax.xaxis.set_major_formatter(axis_config['date_formatter'])

    # 旋转日期标签（动态角度）
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=axis_config['rotation'], ha='right')

    # 添加网格
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)

    # 格式化y轴（大数值使用科学计数法）
    if df_plot[metric_key].max() > 1e6:
        ax.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))

    plt.tight_layout()

    # 保存图表（替换文件名中的特殊字符）
    safe_metric_name = metric_name.replace('/', '-').replace('（', '(').replace('）', ')')
    filename = f'figure/Ripple网络{safe_metric_name}变化趋势.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"已保存: {filename}")
    plt.close()

# 创建综合对比图（选择关键指标）
print("\n正在创建综合对比图...")

# 动态生成综合对比图标题
overall_min = df['date'].min().year
overall_max = df['date'].max().year
title_suffix = f'（{overall_min}-{overall_max}）' if overall_min != overall_max else f'（{overall_min}年）'

# 选择关键指标绘制多子图
fig, axes = plt.subplots(3, 2, figsize=(16, 12))
fig.suptitle(f'Ripple网络关键指标综合对比{title_suffix}', fontsize=16, fontweight='bold')

key_metrics = [
    ('transaction_count', '每日交易总数'),
    ('tps', '系统TPS（交易/秒）'),
    ('active_users', '活跃用户数'),
    ('payments_volume', '每日支付金额（XRP）'),
    ('ledger_interval', '账本间隔时间（秒）'),
    ('accounts_created', '每日新增账户数')
]

for idx, (metric_key, metric_name) in enumerate(key_metrics):
    row = idx // 2
    col = idx % 2
    ax = axes[row, col]

    df_plot = df[['date', metric_key]].dropna()

    if len(df_plot) > 0:
        ax.plot(df_plot['date'], df_plot[metric_key], linewidth=1.2, color='#2E86AB', alpha=0.8)
        ax.set_xlabel('时间', fontsize=10)
        ax.set_ylabel(metric_name, fontsize=10)
        ax.set_title(metric_name, fontsize=11, fontweight='bold')

        # 动态配置时间轴（为子图）
        axis_config = configure_time_axis(df_plot, metric_name)
        if axis_config:
            # 设置x轴日期格式
            if axis_config['major_locator']:
                ax.xaxis.set_major_locator(axis_config['major_locator'])
            if axis_config['minor_locator']:
                ax.xaxis.set_minor_locator(axis_config['minor_locator'])
            ax.xaxis.set_major_formatter(axis_config['date_formatter'])
            plt.setp(ax.xaxis.get_majorticklabels(), rotation=axis_config['rotation'], ha='right')

        # 添加网格
        ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)

        # 格式化y轴
        if df_plot[metric_key].max() > 1e6:
            ax.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))
    else:
        ax.text(0.5, 0.5, '无有效数据', ha='center', va='center', transform=ax.transAxes)
        ax.set_title(metric_name, fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig('figure/Ripple网络关键指标综合对比.png', dpi=300, bbox_inches='tight')
print("已保存: figure/Ripple网络关键指标综合对比.png")
plt.close()

# 创建按年份统计的汇总图
print("\n正在创建年度汇总统计图...")

df['year'] = df['date'].dt.year
yearly_stats = df.groupby('year').agg({
    'transaction_count': 'sum',
    'payments_count': 'sum',
    'accounts_created': 'sum',
    'tps': 'mean',
    'ledger_interval': 'mean'
}).reset_index()

# 动态生成年度统计图标题
yearly_min = yearly_stats['year'].min()
yearly_max = yearly_stats['year'].max()
yearly_title_suffix = f'（{yearly_min}-{yearly_max}）' if yearly_min != yearly_max else f'（{yearly_min}年）'

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(f'Ripple网络年度统计汇总{yearly_title_suffix}', fontsize=16, fontweight='bold')

# 年度交易总数
ax = axes[0, 0]
ax.bar(yearly_stats['year'], yearly_stats['transaction_count'], color='#2E86AB', alpha=0.7)
ax.set_xlabel('年份', fontsize=10)
ax.set_ylabel('交易总数', fontsize=10)
ax.set_title('年度交易总数', fontsize=11, fontweight='bold')
ax.grid(True, alpha=0.3, axis='y')
ax.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))

# 年度支付交易数
ax = axes[0, 1]
ax.bar(yearly_stats['year'], yearly_stats['payments_count'], color='#A23B72', alpha=0.7)
ax.set_xlabel('年份', fontsize=10)
ax.set_ylabel('支付交易数', fontsize=10)
ax.set_title('年度支付交易数', fontsize=11, fontweight='bold')
ax.grid(True, alpha=0.3, axis='y')
ax.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))

# 年度新增账户数
ax = axes[1, 0]
ax.bar(yearly_stats['year'], yearly_stats['accounts_created'], color='#F18F01', alpha=0.7)
ax.set_xlabel('年份', fontsize=10)
ax.set_ylabel('新增账户数', fontsize=10)
ax.set_title('年度新增账户数', fontsize=11, fontweight='bold')
ax.grid(True, alpha=0.3, axis='y')
ax.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))

# 年度平均TPS
ax = axes[1, 1]
ax.bar(yearly_stats['year'], yearly_stats['tps'], color='#06A77D', alpha=0.7)
ax.set_xlabel('年份', fontsize=10)
ax.set_ylabel('平均TPS', fontsize=10)
ax.set_title('年度平均TPS（交易/秒）', fontsize=11, fontweight='bold')
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('figure/Ripple网络年度统计汇总.png', dpi=300, bbox_inches='tight')
print("已保存: figure/Ripple网络年度统计汇总.png")
plt.close()

# 创建4张独立的年度统计图（用于论文各章节）
print("\n正在创建独立的年度统计图...")

# 1. 年度交易总数（独立图）
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(yearly_stats['year'], yearly_stats['transaction_count'],
              color='#2E86AB', alpha=0.75, edgecolor='#1A5270', linewidth=1.2)
ax.set_xlabel('年份', fontsize=12)
ax.set_ylabel('交易总数', fontsize=12)
ax.set_title(f'Ripple网络年度交易总数统计{yearly_title_suffix}', fontsize=14, fontweight='bold', pad=15)
ax.grid(True, alpha=0.3, axis='y', linestyle='--', linewidth=0.8)
ax.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))

# 在柱子顶部添加数值标签
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:.2e}',
            ha='center', va='bottom', fontsize=9, rotation=0)

plt.tight_layout()
plt.savefig('figure/Ripple网络年度交易总数统计.png', dpi=300, bbox_inches='tight')
print("已保存: figure/Ripple网络年度交易总数统计.png")
plt.close()

# 2. 年度支付交易数（独立图）
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(yearly_stats['year'], yearly_stats['payments_count'],
              color='#A23B72', alpha=0.75, edgecolor='#6B2750', linewidth=1.2)
ax.set_xlabel('年份', fontsize=12)
ax.set_ylabel('支付交易数', fontsize=12)
ax.set_title(f'Ripple网络年度支付交易数统计{yearly_title_suffix}', fontsize=14, fontweight='bold', pad=15)
ax.grid(True, alpha=0.3, axis='y', linestyle='--', linewidth=0.8)
ax.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))

# 在柱子顶部添加数值标签
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:.2e}',
            ha='center', va='bottom', fontsize=9, rotation=0)

plt.tight_layout()
plt.savefig('figure/Ripple网络年度支付交易数统计.png', dpi=300, bbox_inches='tight')
print("已保存: figure/Ripple网络年度支付交易数统计.png")
plt.close()

# 3. 年度新增账户数（独立图）
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(yearly_stats['year'], yearly_stats['accounts_created'],
              color='#F18F01', alpha=0.75, edgecolor='#C47301', linewidth=1.2)
ax.set_xlabel('年份', fontsize=12)
ax.set_ylabel('新增账户数', fontsize=12)
ax.set_title(f'Ripple网络年度新增账户数统计{yearly_title_suffix}', fontsize=14, fontweight='bold', pad=15)
ax.grid(True, alpha=0.3, axis='y', linestyle='--', linewidth=0.8)
ax.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))

# 在柱子顶部添加数值标签
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:.2e}',
            ha='center', va='bottom', fontsize=9, rotation=0)

plt.tight_layout()
plt.savefig('figure/Ripple网络年度新增账户数统计.png', dpi=300, bbox_inches='tight')
print("已保存: figure/Ripple网络年度新增账户数统计.png")
plt.close()

# 4. 年度平均TPS（独立图）
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(yearly_stats['year'], yearly_stats['tps'],
              color='#06A77D', alpha=0.75, edgecolor='#047A5D', linewidth=1.2)
ax.set_xlabel('年份', fontsize=12)
ax.set_ylabel('平均TPS（交易/秒）', fontsize=12)
ax.set_title(f'Ripple网络年度平均TPS统计{yearly_title_suffix}', fontsize=14, fontweight='bold', pad=15)
ax.grid(True, alpha=0.3, axis='y', linestyle='--', linewidth=0.8)

# 在柱子顶部添加数值标签
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:.1f}',
            ha='center', va='bottom', fontsize=9, rotation=0)

plt.tight_layout()
plt.savefig('figure/Ripple网络年度平均TPS统计.png', dpi=300, bbox_inches='tight')
print("已保存: figure/Ripple网络年度平均TPS统计.png")
plt.close()

print("\n所有图表绘制完成！")
print(f"\n数据概览：")
print(f"时间范围: {df['date'].min().date()} 至 {df['date'].max().date()}")
print(f"总天数: {len(df)}")
print(f"\n最新数据（{df['date'].max().date()}）：")
latest = df.iloc[-1]
for key, name in list(metrics.items())[:6]:
    if key in latest and pd.notna(latest[key]):
        print(f"  {name}: {latest[key]:,.2f}")
