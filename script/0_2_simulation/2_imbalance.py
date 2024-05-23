from palettable.tableau import Tableau_10
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np

font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 20,
        }

font2 = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 22,
        }

tableau_10 = Tableau_10.hex_colors
colors = [tableau_10[0], tableau_10[1], tableau_10[2], tableau_10[3], tableau_10[4], tableau_10[5], tableau_10[6], tableau_10[7], tableau_10[8]]


df1 = pd.read_csv('/mnt/D/NS-2/20230227-main/Server/ns2/experiment/01_simulation/f1.csv')

output = '/mnt/D/NS-2/20230227-main/Server/ns2/experiment/01_simulation/f1.pdf'

fig, ax = plt.subplots(figsize=(6, 4))   # web_search/data_mining -- various schemes

xdata = df1.loc[:, 'imbalance(Normalized)']
y1data = df1.loc[:, 'ECMP']
y2data = df1.loc[:, 'Consistent']

x_levels = ['10', '20', '30', '40']
plt.xlim((9, 40))
my_x_ticks = np.arange(10, 45, 10)
plt.xticks(my_x_ticks)
ax.set_xticks(my_x_ticks)
ax.set_xticklabels(x_levels, fontproperties=font2)

y_levels = ['0', '1', '2', '3', '4']
plt.ylim((0, 4))
my_y_ticks = np.arange(0.0, 4.5, 1)
plt.yticks(my_y_ticks)
ax.set_yticks(my_y_ticks)
ax.set_yticklabels(y_levels, fontproperties=font2)

ax.tick_params(direction = 'in', top = False, bottom = True, left = True, right = False)

# 在图表中添加网格线，':'是点虚线的网格线
plt.grid(linestyle='-')

# 设置图表的边距
plt.margins(x=0.5, y=0.5)

plt.plot(xdata, y1data, marker="s", linestyle='--', markerfacecolor='none', markersize=16, color=tableau_10[1], label='ecmp hash', linewidth=3)
plt.plot(xdata, y2data, marker="o", linestyle='-.', markerfacecolor='none', markersize=16, color=tableau_10[4], label='consistent hash', linewidth=3)


# 固定图例的位置
plt.legend(loc='best', prop=font)

plt.xlabel('Imbalance (Normalized)', fontproperties = font2)
plt.ylabel('Broken connections (%)', fontproperties = font2)

plt.savefig(output, format='pdf', bbox_inches='tight')

plt.show()