import matplotlib.pyplot as plt
import pandas as pd
import os

seq_name = "ak064t1aiaff"

# Original Arezzo, senza 30
# selected_lndks_idx = [5, 11, 19, 24, 30, 37, 41, 44, 46, 50, 52, 56, 58]

# Occhi+sopracciglia
# selected_lndks_idx = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]

# Naso
# selected_lndks_idx = [27, 28, 29, 30, 31, 32, 33, 34, 35]

# Bocca
# selected_lndks_idx = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65]

# Occhi sopracciglia naso bocca
# selected_lndks_idx = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
#                      41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64,
#                      65]

""""
# sopracciglia
x.append(a[17])
x.append(a[18])
x.append(a[19])
x.append(a[20])
x.append(a[21])
x.append(a[22])
x.append(a[23])
x.append(a[24])
x.append(a[25])
x.append(a[26])

# occhi
x.append(a[36])
x.append(a[37])
x.append(a[38])
x.append(a[39])
x.append(a[40])
x.append(a[41])
x.append(a[42])
x.append(a[43])
x.append(a[44])
x.append(a[45])
x.append(a[46])
x.append(a[47])

# naso
x.append(a[27])
x.append(a[28])
x.append(a[29])
x.append(a[30])
x.append(a[31])
x.append(a[32])
x.append(a[33])
x.append(a[34])
x.append(a[35])

# bocca
x.append(a[48])
x.append(a[49])
x.append(a[50])
x.append(a[51])
x.append(a[52])
x.append(a[53])
x.append(a[54])
x.append(a[55])
x.append(a[56])
x.append(a[57])
x.append(a[58])
x.append(a[59])
x.append(a[60])
x.append(a[61])
x.append(a[62])
x.append(a[63])
x.append(a[64])
x.append(a[65])

# sopracciglia
y.append(a[83])
y.append(a[84])
y.append(a[85])
y.append(a[86])
y.append(a[87])
y.append(a[88])
y.append(a[89])
y.append(a[90])
y.append(a[91])
y.append(a[92])

# occhi
y.append(a[102])
y.append(a[103])
y.append(a[104])
y.append(a[105])
y.append(a[106])
y.append(a[107])
y.append(a[108])
y.append(a[109])
y.append(a[110])
y.append(a[111])
y.append(a[112])
y.append(a[113])

# naso
y.append(a[93])
y.append(a[94])
y.append(a[95])
y.append(a[96])
y.append(a[97])
y.append(a[98])
y.append(a[99])
y.append(a[100])
y.append(a[101])

# bocca
y.append(a[114])
y.append(a[115])
y.append(a[116])
y.append(a[117])
y.append(a[118])
y.append(a[119])
y.append(a[120])
y.append(a[121])
y.append(a[122])
y.append(a[123])
y.append(a[124])
y.append(a[125])
y.append(a[126])
y.append(a[127])
y.append(a[128])
y.append(a[129])
y.append(a[130])
y.append(a[131])
"""

selected_lndks_idx = range(0, 66)
seq_name = "['" + seq_name + "']"
coord_df_path = "./data/dataset/2d_skeletal_data_unbc_coords.csv"
seq_df_path = "./data/dataset/2d_skeletal_data_unbc_sequence.csv"
coord_df = pd.read_csv(coord_df_path)
seq_df = pd.read_csv(seq_df_path)
seq = seq_df.query('sequence_name== @seq_name')
seq_idx = seq.index.values[0]
VAS = seq['VAS'][seq_idx]
num_frames = seq['num_frames'][seq_idx]
print("Sequence: " + seq_name + " VAS: " + str(VAS) + " Frame numbers: " + str(num_frames))
lndks = coord_df.loc[coord_df['0'] == seq_idx].values
num_lndks = 66
lndks = lndks[:, 2:]
lndks_x = lndks[:, :num_lndks]
lndks_y = lndks[:, num_lndks:]
os.makedirs("./"+seq_name)
for j in range(0, num_frames):
    print("Saving frame "+str(j)+"/"+str(num_frames))
    plt.title("Frame" + str(j))
    plt.scatter(lndks_x[j, :], lndks_y[j, :], s=100, alpha=0.5)
    plt.gca().invert_yaxis()
    plt.savefig(seq_name+"/"+'frame' + str(j) + '.png')
    plt.show()
print("Frames saved in folder: "+seq_name)