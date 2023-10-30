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

def calculate_mode(dataframe):
    if len(vetor) == 0:
        return None
    frequency_dict = {}
    for numero in dataframe:
        if numero in frequency_dict:
            frequency_dict[numero] += 1
        else:
            frequency_dict[numero] = 1

    mode = max(frequency_dict, key=frequency_dict.get)


    mode_frequency = frequency_dict[mode]
    for num, frequency in frequency_dict.items():
        if frequency == mode_frequency and num != mode:
            return "não há moda"

    return mode  # Retorna a moda

