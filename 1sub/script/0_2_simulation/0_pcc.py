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
        'size': 22,
        }

tableau_10 = Tableau_10.hex_colors
colors = [tableau_10[0], tableau_10[1], tableau_10[2], tableau_10[3], tableau_10[4], tableau_10[5], tableau_10[6], tableau_10[7], tableau_10[8]]

# 从CSV文件读取数据
df = pd.read_csv('/mnt/D/NS-2/20230227-main/Server/ns2/experiment/01_simulation/pcc_fct/flowsize.csv')

output = '/mnt/D/NS-2/20230227-main/Server/ns2/experiment/01_simulation/pcc_fct/flowsize.pdf'

fig, ax = plt.subplots(figsize=(6, 4))   # web_search/data_mining -- various schemes

# 将数据转换为列表
flowsize = df['flowsize(normailized)'].tolist()
fct_no_broken = df['fct(no broken)'].tolist()
fct_broken = df['fct(broken)'].tolist()

x_levels = ['0', '10', '20', '30']
plt.xlim((0, 31))
my_x_ticks = np.arange(0, 31, 10)
ax.set_xticks(my_x_ticks)
ax.set_xticklabels(x_levels, fontproperties=font2)

y_levels = ['0.0', '0.5', '1.0', '1.5', '2.0']
plt.ylim((0, 2))
my_y_ticks = np.arange(0, 2.1, 0.5)
ax.set_yticks(my_y_ticks)
ax.set_yticklabels(y_levels, fontproperties=font2)

plt.tick_params(direction='out', top=False, bottom=True, left=True, right=False)

# 在图表中添加网格线，':'是点虚线的网格线
plt.grid(linestyle='-')

# 设置图表的边距
plt.margins(x=0.5, y=0.5)

# 绘制折线图
plt.plot(flowsize, fct_broken, linestyle='-', marker='o', markerfacecolor='none', markersize=16, color=tableau_10[2], label='with pcc violation', linewidth=3)
plt.plot(flowsize, fct_no_broken, linestyle='-.', marker='s', markerfacecolor='none', markersize=16, color=tableau_10[1], label='without pcc violation', linewidth=3)


# 固定图例的位置
plt.legend(loc='best', prop=font1)

# 添加标题和标签
# plt.title('Flowsize vs. FCT')
plt.xlabel('Flowsize (Normalized)', fontproperties = font2)
plt.ylabel('Flow Completion Time (s)', fontproperties = font2)

plt.savefig(output, format='pdf', bbox_inches='tight')

plt.show()