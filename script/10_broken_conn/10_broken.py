from palettable.tableau import Tableau_10
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np
import sys

# 深蓝，橙色，绿色，红色，紫色，棕色，粉色，灰色，黄绿色，蓝色
tableau_10 = Tableau_10.hex_colors
colors = [tableau_10[0], tableau_10[1], tableau_10[2], tableau_10[3], tableau_10[4], tableau_10[5], tableau_10[6], tableau_10[7], tableau_10[8]]

font1 = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 20,
        }


font2 = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 24,
        }

if sys.argv[1] == '0':
    df1 = pd.read_csv('/mnt/D/NS-2/20230227-main/Server/ns2/experiment/06_broken_countingbf/f8_65536_wb.csv')
    output = '/mnt/D/NS-2/20230227-main/Server/ns2/experiment/06_broken_countingbf/maat_f8_65536_wb.pdf'
elif sys.argv[1] == '1':
    df1 = pd.read_csv('/mnt/D/NS-2/20230227-main/Server/ns2/experiment/06_broken_countingbf/f8_131072_wb.csv')
    output = '/mnt/D/NS-2/20230227-main/Server/ns2/experiment/06_broken_countingbf/maat_f8_131072_wb.pdf'
elif sys.argv[1] == '2':
    df1 = pd.read_csv('/mnt/D/NS-2/20230227-main/Server/ns2/experiment/06_broken_countingbf/f8_65536_dm.csv')
    output = '/mnt/D/NS-2/20230227-main/Server/ns2/experiment/06_broken_countingbf/maat_f8_65536_dm.pdf'
elif sys.argv[1] == '3':
    df1 = pd.read_csv('/mnt/D/NS-2/20230227-main/Server/ns2/experiment/06_broken_countingbf/f8_131072_dm.csv')
    output = '/mnt/D/NS-2/20230227-main/Server/ns2/experiment/06_broken_countingbf/maat_f8_131072_dm.pdf'

fig, ax1 = plt.subplots(figsize=(6, 4))   # web_search/data_mining -- various schemes

xdata = df1.loc[:, 'size of cbf']
y1data = df1.loc[:, '60000']
y2data = df1.loc[:, '80000']
y3data = df1.loc[:, '100000']

x_levels = ['2', '4', '6', '8', '10']
# y_levels = ['-0.0005', '0.0000', '0.0005', '0.0010', '0.0015', '0.0020']
y_levels = ['-0.02', '0.00', '0.02', '0.04', '0.06', '0.08']

def custom_function(xdata, pos):
    if xdata == 10000:
        return '10K'
    elif xdata == 20000:
        return '20K'
    elif xdata == 40000:
        return '40K'
    elif xdata == 60000:
        return '60K'
    elif xdata == 80000:
        return '80K'
    elif xdata == 100000:
        return '100K'
    elif xdata == 1000000:
        return '1M'
    elif xdata == 2000000:
        return '2M'
    elif xdata == 10000000:
        return '10M'
    elif xdata == 1000:
        return '1K'
    elif xdata == 2000:
        return '2K'
    elif xdata == 4000:
        return '4K'
    elif xdata == 8000:
        return '8K'
    else:
        return 0

ax1.set_xlim((2, 9))
# plt.xticks([20000, 30000, 40000, 50000, 60000, 70000], ["2w", "3w", "4w", "5w", "6w", "7w"])
my_x_ticks = np.arange(2, 10.1, 2)
ax1.set_xticks(my_x_ticks)
ax1.set_xticklabels(x_levels, fontproperties = font2)


if sys.argv[1] == '0':
    # f8_65536_wb
    ax1.set_ylim((0, 0.0005))
    my_y_ticks = np.arange(-0.0001, 0.00051, 0.0001)
    ax1.set_yticks(my_y_ticks, fontproperties=font2)
elif sys.argv[1] == '1':
    # f8_131072_wb
    ax1.set_ylim((0, 0.02))
    my_y_ticks = np.arange(-0.005, 0.021, 0.005)
    ax1.set_yticks(my_y_ticks)
    ax1.set_yticklabels(y_levels, fontproperties=font2)
elif sys.argv[1] == '2':
    # f8_65536_dm
    ax1.set_ylim((0, 0.002))
    my_y_ticks = np.arange(-0.001, 0.0021, 0.001)
    ax1.set_yticks(my_y_ticks, fontproperties=font2)
elif sys.argv[1] == '3':
    # f8_131072_dm
    ax1.set_ylim((0, 0.08))
    my_y_ticks = np.arange(-0.02, 0.081, 0.02)
    ax1.set_yticks(my_y_ticks)
    ax1.set_yticklabels(y_levels, fontproperties=font2)

formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((0,0))
ax1.yaxis.set_major_formatter(formatter)
ax1.yaxis.offsetText.set_fontsize(20)

ax1.tick_params(direction = 'in', top = False, bottom = True, left = True, right = False)

# 在图表中添加网格线，':'是点虚线的网格线
plt.grid(linestyle='-')

# 设置图表的边距
plt.margins(x=0.5, y=0.5)

plt.plot(xdata, y1data, marker="<", linestyle='--', markerfacecolor='none', markersize=16, color=tableau_10[5], label='Δ=60K', linewidth=3)
plt.plot(xdata, y2data, marker="o", linestyle='-', markerfacecolor='none', markersize=16, color=tableau_10[2], label='Δ=80K', linewidth=3)
plt.plot(xdata, y3data, marker="*", linestyle='-.', markerfacecolor='none', markersize=16, color=tableau_10[1], label='Δ=100K', linewidth=3)

# 固定图例的位置 bbox_to_anchor=(0.5, 1.15), 
# fig.legend(loc='best', fancybox=True, ncol=3, prop = font2, frameon = False)
plt.legend(loc='best', prop = font1)

ax1.set_xlabel('Size of CBF (KiB)', fontproperties = font2)

ax1.set_ylabel('Broken connections (%)', fontproperties = font2)

plt.savefig(output, format='pdf', dpi = 800, bbox_inches='tight')

plt.show()