import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

selected_lndks_idx = range(0, 66)
seq_name = "ak064t1aaaff"
vel_frame_threshold = 30


def get_velocities_plot(seq_name, sequence_lndks_idx):
    """
    Extract velocities of selected landmarks of video sequence seq_name.
    Plot a histogram with sum of velocities of the landmarks for each frame
    """
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

    centroid_x = np.array([np.sum(lndks[i, 0:num_lndks]) / num_lndks for i in range(num_frames)])
    centroid_y = np.array([np.sum(lndks[i, num_lndks:]) / num_lndks for i in range(num_frames)])

    offset = np.hstack((np.repeat(centroid_x.reshape(-1, 1), num_lndks, axis=1),
                        np.repeat(centroid_y.reshape(-1, 1), num_lndks, axis=1)))

    lndks_centered = lndks - offset
    lndks_centered[:, 30] = centroid_x
    lndks_centered[:, 30 + num_lndks] = centroid_y
    lndk_vel = np.power(np.power(lndks_centered[0:lndks_centered.shape[0] - 1, 0:num_lndks] -
                                 lndks_centered[1:lndks_centered.shape[0], 0:num_lndks], 2) +
                        np.power(lndks_centered[0:lndks_centered.shape[0] - 1, num_lndks:] -
                                 lndks_centered[1:lndks_centered.shape[0], num_lndks:], 2), 0.5)
    data_velocities = []
    for k in np.arange(1, lndk_vel.shape[0]):
        data_velocities.append(sum(lndk_vel[k, sequence_lndks_idx]))

    data_velocities_filtered = np.convolve(data_velocities, np.ones(3) / 3, mode='valid')
    plt.bar(range(0, len(data_velocities_filtered)), data_velocities_filtered, color="blue")
    plt.title("Sequence: " + seq_name + " VAS: " + str(VAS) + " Frame numbers: " + str(num_frames))
    plt.xlabel("Frame Num")
    plt.ylabel("Sum Vel Selected Lndk")
    plt.show()
    index = []
    for count, vel in enumerate(data_velocities):
        if vel > vel_frame_threshold:
            index.append(count)
    print(index)


get_velocities_plot("['" + seq_name + "']", selected_lndks_idx)
