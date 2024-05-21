from palettable.tableau import Tableau_10
import matplotlib.pyplot as plt
import numpy as np

# 深蓝，橙色，绿色，红色，紫色，棕色，粉色，灰色，黄绿色，蓝色
tableau_10 = Tableau_10.hex_colors
colors = [tableau_10[0], tableau_10[1], tableau_10[2], tableau_10[3], tableau_10[4], tableau_10[5], tableau_10[6], tableau_10[7], tableau_10[8], tableau_10[9]]


def get_pctl(a, p):
	i = int(len(a) * p)
	return a[i]


font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 7,
        }

font1 = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 7,
        }

font2 = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 10,
        }

#  'Maat(conn)', 'Maat(coarse)','Silkroad', 'Maglev', 'Concury', 'Cheetah(rr)',
methods = ['Maat(conn)', 'Maat(coarse)', 'Maat']

load_levels = ['16384', '32768', '65536', '131072']
y_levels = ['0', '6', '12', '18']

# web_search -- schemes
# fct_values1 = {
#     '16384': [1.714352320525624,1.680230812715429,1.763193627500410,1.412448266621621,1.223168153573886],
#     '32768': [3.495332484523281,3.212265626331054,3.535987509791171,3.015575883258183,1.746112305137343],
#     '65536': [6.924546101874531,6.961113220084179,7.366211733496347,5.709352295815273,2.638757883403710],
#     '131072': [14.440129128936894,15.143512647348242,14.093548321364218,11.527217956318144,4.172311994833632],
# }
# data_mining -- schemes
# fct_values1 = {
#     '16384': [1.879919863128339,1.919280908262578,1.933783118084238,1.865354936459531,1.247354716614960],
#     '32768': [3.655874562557773,3.552740598552128,3.686183109601855,3.397773282652871,1.716211639309609],
#     '65536': [7.303961753911406,7.421118263416835,7.630559545494531,7.229234027448066,2.655385756088222],
#     '131072': [15.737700932669687,17.152440194455078,15.282780484231874,14.071127345799511,4.386021730009316]
# }
# web_search -- gran
fct_values1 = {
    '16384': [1.589532702229121,1.206970282752246,1.223168153573886],
    '32768': [3.034785334753378,2.058232429577558,1.746112305137343],
    '65536': [5.969788152203906,4.388021265449843,2.638757883403710],
    '131072': [11.917912637500527,9.028673556683496,4.172311994833632]
}
# data_mining -- gran
# fct_values1 = {
#     '16384': [1.786072927861874,1.306187313018027,1.247354716614960],
#     '32768': [3.533130574857539,2.252958164313378,1.716211639309609],
#     '65536': [7.016407636997871,4.577363913625917,2.655385756088222],
#     '131072': [15.015283815854550,9.987550402538613,4.386021730009316]
# }


# 2 5 1 4 0
# tableau_10[2], tableau_10[5], tableau_10[1], tableau_10[4] -- schemes
# , tableau_10[3], tableau_10[9]
# 'oo', '--', '**', '///'
colors = [tableau_10[3], tableau_10[9], tableau_10[0]]
hatchs = ['...','+++', 'XXX']
# red, dimgray, magenta, limegreen, orange, dodgerblue
# 绘制柱状图
bar_width = 0.12
index = np.arange(len(load_levels))

# scheme -- (4, 1.5)
# granitity -- (7, 1.5)
fig, ax1 = plt.subplots(figsize=(5, 1.8))   # web_search/data_mining -- various schemes
# fig, ax2 = plt.subplots(figsize=(4, 1.5))  # web_search -- various flb

for i, method in enumerate(methods):
    ax1.bar(index + i * bar_width, [fct_values1[load][i] for load in load_levels], bar_width, edgecolor='black', color = colors[i], hatch = hatchs[i])
# for i, method in enumerate(methods):
#     ax2.bar(index + i * bar_width, [fct_values2[load][i] for load in load_levels], bar_width, edgecolor='black', color = colors[i])

# 设置图表参数 -- various method
ax1.set_xlabel('Number of connections', fontproperties = font2)
ax1.set_ylabel('Variance (Normalized)', fontproperties = font2)
ax1.set_xticks(index + bar_width * (len(methods) - 1) / 2)
ax1.set_xticklabels(load_levels, fontproperties = font2)
ax1.set_ylim(0, 18)
ax1.set_yticks(np.arange(0, 18.1, 6))
ax1.set_yticklabels(y_levels, fontproperties=font2)
ax1.grid(linestyle='-', axis='y')

# various schemes
# ax2.set_xlabel('Number of connections', fontproperties = font2)
# ax2.set_ylabel('Variance (Normalized)', fontproperties = font2)
# ax2.set_xticks(index + bar_width * (len(methods) - 1) / 2)
# ax2.set_xticklabels(load_levels, fontproperties = font2)
# ax2.set_ylim(0, 18)
# ax2.set_yticks(np.arange(0, 18.1, 6))
# ax2.grid(linestyle='-', axis='y')

# 显示图例在图片的外部上层
# gran 1.15 scheme 1.3
fig.legend(methods,loc='upper center', fancybox=True, ncol=3, prop = font2, frameon = True, bbox_to_anchor=(0.5, 1.1))
plt.subplots_adjust(wspace=0.1)
ax1.tick_params(direction = 'in', top = False, bottom = False, left = True, right = False)
# ax2.tick_params(direction = 'in', top = False, bottom = False, left = True, right = False)
# plt.savefig('/mnt/D/NS-2/20230227-main/Server/ns2/experiment/04_variance/3_maat_variance_scheme_dm.pdf', format = 'pdf' , dpi = 800 ,bbox_inches = 'tight')
plt.savefig('/mnt/D/NS-2/20230227-main/Server/ns2/experiment/04_variance/4_maat_variance_gran_wb.pdf', format = 'pdf' , dpi = 800 ,bbox_inches = 'tight')
# 显示图表
plt.show()