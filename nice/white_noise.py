import numpy as np

def get_white_noise_stim_vector(dims, ch, n):
    # We will have as many stimuli as time_bins so there will be
    # overlap
    stim_vector = np.zeros((dims, dims, ch, n))
    for i in range(stim_vector.shape[-1]):
        # Gaussian noise vector of dimension k for the time window    # 200(milliseconds)
        stim_vector[:, :, :, i] = np.random.normal(0.0, 1.0, size=       (dims, dims, ch))
    return stim_vector

print(get_white_noise_stim_vector(10, 10, 10))