from palettable.tableau import Tableau_10
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np

font1 = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 20,
        }

font2 = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 26,
        }

# 深蓝，橙色，绿色，红色，紫色，棕色，粉色，灰色，黄绿色，蓝色
tableau_10 = Tableau_10.hex_colors
colors = [tableau_10[0], tableau_10[1], tableau_10[2], tableau_10[3], tableau_10[4], tableau_10[5], tableau_10[6], tableau_10[7], tableau_10[8]]

df1 = pd.read_csv('/mnt/D/NS-2/20230227-main/Server/ns2/experiment/03_process/f4.csv')

output = '/mnt/D/NS-2/20230227-main/Server/ns2/experiment/03_process/maat_f4_1VIP.pdf'

fig, ax = plt.subplots(figsize=(6, 4))   # web_search/data_mining -- various schemes

xdata = df1.loc[:, 'Number of connections']
y1data = df1.loc[:, 'hash']
y2data = df1.loc[:, 'consistent hash']
y3data = df1.loc[:, 'othello hash']
y4data = df1.loc[:, 'cheetah(rr)']
y5data = df1.loc[:, 'flb']

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
    elif xdata == 520000:
        return '520K'
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


x_levels = ['131072', '262144', '524288', '1048576', '2097152']
ax.set_xlim(-0.2, 4.1)
# ax.set_xscale('log')
# ax.xaxis.set_major_locator(ticker.LogLocator(base=10, numticks=10))
# ax.xaxis.set_major_formatter(ticker.FuncFormatter(custom_function))
# ax.set_xticklabels(x_levels, fontproperties=font2)
ax.set_xticks(np.arange(5), ('131K', '262K', '524K', '1M', '2M'), fontproperties = font2)

y_levels = ['0', '15', '30', '45', '60']
ax.set_ylim((0, 60))
my_y_ticks = np.arange(0, 61, 15)
ax.set_yticks(my_y_ticks)
ax.set_yticklabels(y_levels, fontproperties=font2)


ax.tick_params(direction = 'in', top = False, bottom = True, left = True, right = False)

# 在图表中添加网格线，':'是点虚线的网格线
plt.grid(linestyle='-')

# 设置图表的边距
plt.margins(x=0.5, y=0.5)

plt.plot(xdata, y1data, marker="s", linestyle='-.', markerfacecolor='none', markersize=16, color=tableau_10[5], label='Silkroad', linewidth=3)
plt.plot(xdata, y2data, marker="o", linestyle='-', markerfacecolor='none', markersize=16, color=tableau_10[4], label='Maglev', linewidth=3)
plt.plot(xdata, y3data, marker=">", linestyle='-', markerfacecolor='none', markersize=16, color=tableau_10[1], label='Concury', linewidth=3)
plt.plot(xdata, y4data, marker="d", linestyle='-', markerfacecolor='none', markersize=16, color=tableau_10[2], label='Cheetah (rr)', linewidth=3)
plt.plot(xdata, y5data, marker="*", linestyle='--', markerfacecolor='none', markersize=16, color=tableau_10[0], label='Maat', linewidth=3)

# 固定图例的位置
fig.legend(loc='upper center', fancybox=True, ncol=2, prop = font1, frameon = True, bbox_to_anchor=(0.5, 1.25))

ax.set_xlabel('Number of connections', fontproperties = font2)

ax.set_ylabel('Throughput (Mpps)', fontproperties = font2)

plt.savefig(output, format='pdf', bbox_inches='tight')

plt.show()