import matplotlib.pyplot as plt

a = [84.7, 84.22, 85.84, 88.17, 92.0, 98.9, 108.23, 120.42, 135.61, 150.81, 163.9, 174.83, 182.25, 187.92, 193.06,
     197.79, 199.71, 92.1, 97.66, 108.31, 118.99, 129.23, 154.67, 164.83, 175.03, 185.03, 192.61, 143.14, 142.52, 141.9,
     141.09, 127.7, 132.97, 139.67, 145.99, 151.52, 105.08, 112.12, 119.52, 126.43, 119.36, 112.03, 155.42, 162.07,
     168.93, 174.96, 168.35, 161.75, 118.43, 125.8, 132.94, 140.21, 146.94, 152.59, 157.79, 152.32, 145.51, 138.63,
     131.19, 124.38, 131.29, 139.83, 146.7, 146.54, 139.69, 131.15, 96.7, 112.62, 128.49, 144.2, 159.47, 173.81, 186.57,
     196.74, 199.53, 197.54, 189.14, 178.12, 164.58, 150.14, 135.35, 120.65, 105.33, 89.44, 81.05, 80.34, 81.05, 83.99,
     85.83, 84.74, 84.01, 85.4, 91.76, 95.89, 106.46, 116.95, 127.36, 135.13, 139.77, 141.68, 141.22, 138.31, 101.67,
     98.95, 98.88, 101.75, 103.42, 103.48, 103.01, 100.9, 101.86, 105.23, 106.78, 105.3, 157.73, 153.84, 149.57, 152.44,
     151.75, 156.0, 160.68, 164.9, 166.35, 166.56, 165.38, 162.27, 156.87, 158.26, 157.98, 158.18, 158.38, 157.12]

x = []
y = []
z = []
w = []

# Original Arezzo, senza 30
# selected_lndks_idx = [5, 11, 19, 24, 30, 37, 41, 44, 46, 50, 52, 56, 58]

# Occhi+sopracciglia
# selected_lndks_idx = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]

# Naso
# selected_lndks_idx = [27, 28, 29, 30, 31, 32, 33, 34, 35]

# Bocca
# selected_lndks_idx = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65]

# Occhi sopracciglia naso bocca
#selected_lndks_idx = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
#                      41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64,
#                      65]

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

for i in range(0, len(a)):
    if i < 66:
        z.append(a[i])
    else:
        w.append(a[i])

plt.scatter(z, w, s=100, alpha=0.5)
plt.scatter(x, y, s=100, alpha=1)
plt.gca().invert_yaxis()
plt.show()
