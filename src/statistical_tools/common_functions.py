import numpy as np


def compute_temporal_average(time_values, transient_values):
    avg_value = np.trapz(transient_values, x=time_values)
    avg_value /= (time_values.max() - time_values.min())

    return avg_value


def compute_temporal_std(time_values, transient_values):
    avg_value = compute_temporal_average(time_values, transient_values)

    std_value = np.trapz(np.power(transient_values - avg_value, 2.0), x=time_values)
    std_value /= (time_values.max() - time_values.min())
    std_value = np.sqrt(std_value)

    return std_value
