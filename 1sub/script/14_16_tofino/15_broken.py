from palettable.tableau import Tableau_10
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np
import sys

font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 18,
        }

font1 = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 22,
        }

font2 = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 26,
        }

# 深蓝，橙色，绿色，红色，紫色，棕色，粉色，灰色，黄绿色，蓝色
tableau_10 = Tableau_10.hex_colors
colors = [tableau_10[0], tableau_10[1], tableau_10[2], tableau_10[3], tableau_10[4], tableau_10[5], tableau_10[6], tableau_10[7], tableau_10[8]]


df1 = pd.read_csv('/mnt/D/NS-2/20230227-main/Server/ns2/experiment/08_flow_completetion_time/broken.csv')
output = '/mnt/D/NS-2/20230227-main/Server/ns2/experiment/08_flow_completetion_time/broken.pdf'

fig, ax = plt.subplots(figsize=(6, 4))   # web_search/data_mining -- various schemes

xdata = df1.loc[:, 'Scheme']
y1data = df1.loc[:, 'flb']
y2data = df1.loc[:, 'flb(test)']

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

#  70000, 90000, 110000, 130000,
# plt.xlim((4, 7.1)) "7w", "9w", "11w", "13w",
ax.set_xticks([60000, 80000, 100000, 120000, 140000], ["60K", "80K", "100K", "120K", "140K"], fontproperties=font1)
plt.xlim(58000, 141000)
# my_x_ticks = np.arange(4, 7.1, 1)
# plt.xticks(my_x_ticks, size=12)

y_levels = ['-0.002', '-0.001', '0.000', '0.001', '0.002', '0.003']
plt.ylim((-0.002, 0.003))
my_y_ticks = np.arange(-0.002, 0.0031, 0.001)
plt.yticks(my_y_ticks)
ax.set_yticks(my_y_ticks)
ax.set_yticklabels(y_levels, fontproperties=font1)


formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((0,0))
ax.yaxis.set_major_formatter(formatter)
ax.yaxis.offsetText.set_fontsize(16)

ax.tick_params(direction = 'in', top = False, bottom = True, left = True, right = False)

# 在图表中添加网格线，':'是点虚线的网格线
plt.grid(linestyle=':')

# 设置图表的边距
plt.margins(x=0.5, y=0.5)

plt.plot(xdata, y1data, marker="s", linestyle='-.', markerfacecolor='none', markersize=12, color=tableau_10[0], label='Maat', linewidth=3)
plt.plot(xdata, y2data, marker="d", linestyle='--', markerfacecolor='none', markersize=12, color=tableau_10[5], label='Maat (Tofino)', linewidth=3)

# 固定图例的位置
plt.legend(loc='best', prop=font)

plt.xlabel('Number of connections', fontproperties = font2)

plt.ylabel('Broken connections (%)', fontproperties = font2)

plt.savefig(output, format='pdf', bbox_inches='tight')

plt.show()