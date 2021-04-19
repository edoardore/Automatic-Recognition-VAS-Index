import pandas as pd
import numpy as np

coords = pd.read_csv('./data/dataset/2d_skeletal_data_unbc_coords.csv')
sequence = pd.read_csv('./data/dataset/2d_skeletal_data_unbc_sequence.csv')
seq = []
for seq_num in np.arange(sequence.shape[0]):
    if sequence['VAS'][seq_num] >= 8:
        seq.append(seq_num)
    else:
        sequence = sequence.drop(seq_num)
for coord in np.arange(coords.shape[0]):
    if coords['0'][coord] not in seq:
        coords = coords.drop([coord])

coords.to_csv('./data/dataset/2d_skeletal_data_unbc_coords.csv', index=False)
sequence.to_csv('./data/dataset/2d_skeletal_data_unbc_sequence.csv', index=False)

coords = pd.read_csv('./data/dataset/2d_skeletal_data_unbc_coords.csv')
sequence = pd.read_csv('./data/dataset/2d_skeletal_data_unbc_sequence.csv')
num = coords['0'][0]
i = 0
for numCoord in np.arange(coords.shape[0]):
    if num == coords['0'][numCoord]:
        coords['0'][numCoord] = i
    else:
        i += 1
        num = coords['0'][numCoord]
        coords['0'][numCoord] = i

coords.to_csv('./data/dataset/2d_skeletal_data_unbc_coords.csv', index=False)
sequence.to_csv('./data/dataset/2d_skeletal_data_unbc_sequence.csv', index=False)
