import numpy as np
import pytest

from statistical_tools.common_functions import (
    compute_temporal_average,
    compute_temporal_std,
)

MIN_POINTS = 5000
MAX_POINTS = 100000
N_TEST_POINTS = 10
MIN_Y_VALUE = 10.0
MAX_Y_VALUE = 100000.0
N_Y_VALUES = 10


def uniform_sine_wave(sine_parameters):
    t_start = 0.0
    t_end = 2.0 * np.pi
    time_values = np.linspace(t_start, t_end, num=sine_parameters["total_points"])
    transient_values = sine_parameters["y_value"] + np.sin(time_values)

    return time_values, transient_values


def non_uniform_sine_wave(sine_parameters):
    t_start = 0.0
    t_end = 2.0 * np.pi
    time_values = np.random.uniform(
        low=t_start, high=t_end, size=sine_parameters["total_points"]
    )
    time_values.sort()
    transient_values = sine_parameters["y_value"] + np.sin(time_values)

    return time_values, transient_values


@pytest.mark.parametrize(
    "total_points",
    np.linspace(MIN_POINTS, MAX_POINTS, num=N_TEST_POINTS, endpoint=True, dtype=int),
)
@pytest.mark.parametrize(
    "y_value",
    np.linspace(MIN_Y_VALUE, MAX_Y_VALUE, num=N_Y_VALUES, endpoint=True, dtype=float),
)
@pytest.mark.parametrize("test_function", [uniform_sine_wave, non_uniform_sine_wave])
def test_compute_temporal_average(total_points, y_value, test_function):
    """
    This test checks if the temporal average values are being computed correctly.
    This is important in cases where the transient values have a variable timestep
    """

    sine_parameters = {"total_points": total_points, "y_value": y_value}
    time_values, transient_values = test_function(sine_parameters)
    average_value = compute_temporal_average(time_values, transient_values)

    assert average_value == pytest.approx(y_value, rel=1.0e-3)


@pytest.mark.parametrize(
    "total_points",
    np.linspace(MIN_POINTS, MAX_POINTS, num=N_TEST_POINTS, endpoint=True, dtype=int),
)
@pytest.mark.parametrize(
    "y_value",
    np.linspace(MIN_Y_VALUE, MAX_Y_VALUE, num=N_Y_VALUES, endpoint=True, dtype=float),
)
@pytest.mark.parametrize("test_function", [uniform_sine_wave, non_uniform_sine_wave])
def test_compute_temporal_std(total_points, y_value, test_function):
    """
    This test checks if the temporal standard deviation values are being computed correctly.
    This is important in cases where the transient values have a variable timestep.
    For a sine wave on the interval [0, 2 pi], the std value should return sqrt(0.5).
    """

    sine_parameters = {"total_points": total_points, "y_value": y_value}
    time_values, transient_values = test_function(sine_parameters)
    average_value = compute_temporal_std(time_values, transient_values)

    expected_value = np.sqrt(0.5)
    assert average_value == pytest.approx(expected_value, rel=1.0e-3)
