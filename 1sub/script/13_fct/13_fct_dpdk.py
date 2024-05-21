from palettable.tableau import Tableau_10
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

tableau_10 = Tableau_10.hex_colors
colors = [tableau_10[0], tableau_10[1], tableau_10[2], tableau_10[3], tableau_10[4], tableau_10[5], tableau_10[6], tableau_10[7], tableau_10[8]]

font1 = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 22,
        }

font2 = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 26,
        }

df0 = pd.read_csv('/mnt/D/NS-2/20230227-main/Server/ns2/experiment/09_response_time/32_servers/silkroad_load.csv')
df1 = pd.read_csv('/mnt/D/NS-2/20230227-main/Server/ns2/experiment/09_response_time/32_servers/maglev_load.csv')
df2 = pd.read_csv('/mnt/D/NS-2/20230227-main/Server/ns2/experiment/09_response_time/32_servers/concury_load.csv')
df3 = pd.read_csv('/mnt/D/NS-2/20230227-main/Server/ns2/experiment/09_response_time/32_servers/cheetah_rr_load.csv')
df4 = pd.read_csv('/mnt/D/NS-2/20230227-main/Server/ns2/experiment/09_response_time/32_servers/flb_load.csv')

max_response_time_df0 = df0['response_time'].max()
max_response_time_df1 = df1['response_time'].max()
max_response_time_df2 = df2['response_time'].max()
max_response_time_df3 = df3['response_time'].max()
max_response_time_df4 = df4['response_time'].max()



with open('/mnt/D/NS-2/20230227-main/Server/ns2/experiment/09_response_time/32_servers/result.txt', 'w') as f:
    f.write(f'Maximum response time of silkroad: {max_response_time_df0}\n')
    f.write(f'Maximum response time of maglev: {max_response_time_df1}\n')
    f.write(f'Maximum response time of concury: {max_response_time_df2}\n')
    f.write(f'Maximum response time of cheetah: {max_response_time_df3}\n')
    f.write(f'Maximum response time of flb: {max_response_time_df4}\n')


output = '/mnt/D/NS-2/20230227-main/Server/ns2/experiment/09_response_time/32_servers/boxplot.pdf'

fig = plt.figure(figsize=(6,4), dpi=800)

y0data = df0['response_time']
y1data = df1['response_time']
y2data = df2['response_time']
y3data = df3['response_time']
y4data = df4['response_time']

# 创建箱线图
bp = plt.boxplot([y0data, y1data, y2data, y3data, y4data], vert = True, patch_artist=True, labels = ['silkroad', 'maglev', 'concury', 'cheetah(rr)', 'flb'], showfliers=False,
                 boxprops=dict(linewidth=2), widths=0.75)
# 为每个箱体设置不同的颜色
colors = [tableau_10[2], tableau_10[5], tableau_10[1], tableau_10[4], tableau_10[0]]
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

for median in bp['medians']:
    median.set(color='black')

plt.xlabel('Various schemes', fontproperties = font2)
plt.ylabel('FCT (s)', fontproperties = font2)

# rotation = 28, rotation=25
plt.xticks([1, 2, 3, 4, 5], ['Silkroad', 'Maglev', 'Concury', 'Cheetah', 'Maat'], fontproperties = font1, rotation=15)
plt.yticks(np.arange(0.95, 1.21, 0.05), fontproperties = font1)

# 启用网格线
plt.grid(True, linestyle='--', alpha=0.5)

plt.savefig(output, format = 'pdf' , dpi = 800 ,bbox_inches = 'tight')
# 显示箱线图
plt.show()

