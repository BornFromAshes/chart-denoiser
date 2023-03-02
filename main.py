import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg.linalg as LA


def denoise_data(lamb, in_data):
    lamb_dx = np.sqrt(lamb) * (np.roll(np.eye(n - 1, n), 1) + -np.eye(n - 1, n))
    i_lamb_d = np.vstack((np.eye(n), lamb_dx))
    y_zero = np.vstack((in_data, np.zeros((n - 1, 1))))
    # least square algorithm
    return np.dot(np.dot(LA.inv(np.dot(np.transpose(i_lamb_d), i_lamb_d)), np.transpose(i_lamb_d)), y_zero)


def show_result(lamb, in_data):
    plt.subplots()
    figure, axis = plt.subplots(nrows=2, ncols=1, figsize=(16, 9))

    axis[0].plot(in_data)
    axis[1].plot(in_data, alpha=0.6, label="Noisy")
    axis[1].plot(denoise_data(lamb, in_data), 'g', lw=1.5, label="Denoised")

    axis[0].set_title("Noisy data")
    axis[1].set_title("Denoised data")
    plt.legend()
    plt.show()


data = np.load('./btc_price.npy')
n = data.size
in_data = data.reshape((n, 1))
show_result(9999, in_data)
