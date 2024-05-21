from palettable.tableau import Tableau_10
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np

font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 18,
        }

font2 = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 20,
        }

tableau_10 = Tableau_10.hex_colors
colors = [tableau_10[0], tableau_10[1], tableau_10[2], tableau_10[3], tableau_10[4], tableau_10[5], tableau_10[6], tableau_10[7], tableau_10[8]]


df1 = pd.read_csv('/mnt/D/NS-2/20230227-main/Server/ns2/experiment/01_simulation/f2.csv')

output = '/mnt/D/NS-2/20230227-main/Server/ns2/experiment/01_simulation/f2.pdf'

fig, ax = plt.subplots(figsize=(6, 4))   # web_search/data_mining -- various schemes

xdata = df1.loc[:, 'Number of connections']
y1data = df1.loc[:, 'hash']
y2data = df1.loc[:, 'consistent hash']
y3data = df1.loc[:, 'round robin']
y4data = df1.loc[:, 'power of two']

ax.set_xticks([10000, 20000, 30000, 40000, 50000, 60000], ["10K", "20K", "30K", "40K", "50K", "60K"], fontproperties=font2)
plt.xlim(16000, 66000)

# plt.xlim((16000, 66000))
# my_x_ticks = np.arange(16384, 66000, 8192)
# plt.xticks(my_x_ticks, size=12)

y_levels = ['0', '2', '4', '6', '8']
plt.ylim((0.0, 8.0))
my_y_ticks = np.arange(0.0, 8.5, 2)
ax.set_yticks(my_y_ticks)
ax.set_yticklabels(y_levels, fontproperties=font2)


plt.tick_params(direction='out', top=False, bottom=True, left=True, right=False)

# 在图表中添加网格线，':'是点虚线的网格线
plt.grid(linestyle='-')

# 设置图表的边距
plt.margins(x=0.5, y=0.5)

plt.plot(xdata, y1data, marker="s", linestyle='-.', markerfacecolor='none', markersize=16, color=tableau_10[1], label='ecmp hash', linewidth=3)
plt.plot(xdata, y2data, marker="s", linestyle='-.', markerfacecolor='none', markersize=16, color=tableau_10[4], label='consistent hash', linewidth=3)
plt.plot(xdata, y3data, marker="o", linestyle='-', markerfacecolor='none', markersize=16, color=tableau_10[2], label='round robin', linewidth=3)
plt.plot(xdata, y4data, marker="*", linestyle='--', markerfacecolor='none', markersize=16, color=tableau_10[5], label='power of two', linewidth=3)

# 固定图例的位置
plt.legend(loc='best', prop=font)

plt.xlabel('Number of connections', fontproperties = font2)
plt.ylabel('Imbalance (Normalized)', fontproperties = font2)

plt.savefig(output, format='pdf', bbox_inches='tight')

plt.show()