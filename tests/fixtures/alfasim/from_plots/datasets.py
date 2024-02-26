import os
import random

import pytest

from src.xls_reader.alfasim.from_plots.xls_reader import merge_tabs


def shuffle_dataframe(dataframe):
    keys = dataframe.keys()

    indexes_time = []
    for i, key in enumerate(keys):
        if "Time" in key:
            indexes_time.append(i)
    N_indexes_time = len(indexes_time)

    N_columns_global = len(dataframe.keys())
    order_global = list(range(N_columns_global))
    shuffled_order_global = []

    for i, index_time in enumerate(indexes_time):
        if i == N_indexes_time - 1:
            index_start = index_time
            index_end = N_columns_global
        else:
            index_start = index_time
            index_end = indexes_time[i + 1]

        original_order = order_global[index_start + 1 : index_end]
        shuffled_order = original_order.copy()
        random.shuffle(shuffled_order)
        shuffled_order_global += [index_start]
        shuffled_order_global += shuffled_order

    original_keys = list(dataframe.keys())
    shuffled_keys = original_keys.copy()
    for i in range(N_columns_global):
        shuffled_keys[i] = original_keys[shuffled_order_global[i]]

    dataframe_copy = dataframe.copy()
    for i in range(N_columns_global):
        dataframe.iloc[:, i] = dataframe_copy.iloc[:, shuffled_order_global[i]]

    dataframe.columns = shuffled_keys
    return dataframe


def alfasim_file_single_edge_homogeneous_data():
    """
    This fixture contains a dataset with a single edge, multiple probe positions and no parametric run.
    The probe positions are homogeneous, i.e., have the exact variables at the same points..
    """

    xls_file = os.path.join(
        "..",
        "..",
        "..",
        "data",
        "alfasim",
        "from_plots",
        "alfasim_file_single_edge_homogeneous_data.xlsx",
    )

    return {
        "dataframe": merge_tabs(xls_file),
        "variable_names": sorted(["Time", "Absolute Pressure", "Holdup"]),
        "edge_names": ["Conn 1"],
        "probe_positions": (
            [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8.0, 8.5, 9, 9.5]
        ),
        "units": sorted(["s", "bar", "m3/m3"]),
        "parametric_run": ["0"],
        "results": {
            "0": {
                "Conn 1": {
                    "1": {
                        "position": 1.0,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "1.5": {
                        "position": 1.5,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "2": {
                        "position": 2.0,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "2.5": {
                        "position": 2.5,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "3": {
                        "position": 3.0,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "3.5": {
                        "position": 3.5,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "4": {
                        "position": 4.0,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "4.5": {
                        "position": 4.5,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "5": {
                        "position": 5.0,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "5.5": {
                        "position": 5.5,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "6": {
                        "position": 6.0,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "6.5": {
                        "position": 6.5,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "7": {
                        "position": 7.0,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "7.5": {
                        "position": 7.5,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "8": {
                        "position": 8.0,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "8.5": {
                        "position": 8.5,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "9": {
                        "position": 9.0,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "9.5": {
                        "position": 9.5,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                }
            },
        },
    }


def alfasim_file_single_edge_homogeneous_data_and_parametric_run():
    """
    This fixture contains a dataset with a single edge, multiple probe positions and parametric run.
    The probe positions are homogeneous, i.e., have the exact variables at the same points..
    """

    xls_file = os.path.join(
        "..",
        "..",
        "..",
        "data",
        "alfasim",
        "from_plots",
        "alfasim_file_single_edge_homogeneous_data_and_parametric_run.xlsx",
    )

    return {
        "dataframe": merge_tabs(xls_file),
        "variable_names": sorted(["Time", "Absolute Pressure", "Holdup"]),
        "edge_names": ["Conn 1"],
        "probe_positions": ([1, 1.5]),
        "units": sorted(["s", "bar", "m3/m3"]),
        "parametric_run": ["0", "1", "2"],
        "results": {
            "0": {
                "Conn 1": {
                    "1": {
                        "position": 1.0,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "1.5": {
                        "position": 1.5,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                },
            },
            "1": {
                "Conn 1": {
                    "1": {
                        "position": 1.0,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "1.5": {
                        "position": 1.5,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                },
            },
            "2": {
                "Conn 1": {
                    "1": {
                        "position": 1.0,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "1.5": {
                        "position": 1.5,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                },
            },
        },
    }


def alfasim_file_two_edges_homogeneous_data():
    """
    This fixture contains a dataset with two edges and multiple probe positions.
    The probe positions are homogeneous, i.e., have the exact variables at the same points.
    """

    xls_file = os.path.join(
        "..",
        "..",
        "..",
        "data",
        "alfasim",
        "from_plots",
        "alfasim_file_two_edges_homogeneous_data.xlsx",
    )

    return {
        "dataframe": merge_tabs(xls_file),
        "variable_names": sorted(["Time", "Absolute Pressure", "Holdup"]),
        "edge_names": ["Conn 1", "Conn 2"],
        "probe_positions": ([5, 7.98, 10, 22.63]),
        "units": sorted(["s", "bar", "m3/m3"]),
        "parametric_run": ["0"],
        "results": {
            "0": {
                "Conn 1": {
                    "22.63": {
                        "position": 22.63,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "7.98": {
                        "position": 7.98,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                },
                "Conn 2": {
                    "5": {
                        "position": 5.0,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "10": {
                        "position": 10.0,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                },
            },
        },
    }


def alfasim_file_two_edges_homogeneous_data_and_parametric_run():
    """
    This fixture contains a dataset with two edges, multiple probe positions and parametric run.
    The probe positions are homogeneous, i.e., have the exact variables at the same points.
    """

    xls_file = os.path.join(
        "..",
        "..",
        "..",
        "data",
        "alfasim",
        "from_plots",
        "alfasim_file_two_edges_homogeneous_data_and_parametric_run.xlsx",
    )

    return {
        "dataframe": merge_tabs(xls_file),
        "variable_names": sorted(["Time", "Absolute Pressure", "Holdup"]),
        "edge_names": ["Conn 1", "Conn 2"],
        "probe_positions": ([5, 7.98, 10, 22.63]),
        "units": sorted(["s", "bar", "m3/m3"]),
        "parametric_run": ["0", "1", "2"],
        "results": {
            "0": {
                "Conn 1": {
                    "22.63": {
                        "position": 22.63,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "7.98": {
                        "position": 7.98,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                },
                "Conn 2": {
                    "5": {
                        "position": 5.0,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "10": {
                        "position": 10.0,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                },
            },
            "1": {
                "Conn 1": {
                    "22.63": {
                        "position": 22.63,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "7.98": {
                        "position": 7.98,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                },
                "Conn 2": {
                    "5": {
                        "position": 5.0,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "10": {
                        "position": 10.0,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                },
            },
            "2": {
                "Conn 1": {
                    "22.63": {
                        "position": 22.63,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "7.98": {
                        "position": 7.98,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                },
                "Conn 2": {
                    "5": {
                        "position": 5.0,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                    "10": {
                        "position": 10.0,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                },
            },
        },
    }


def alfasim_file_two_edges_heterogeneous_data():
    """
    This fixture contains a dataset with two edges and multiple probe positions.
    The probe positions are heterogeneous, i.e., each probe point save a different set of variables.
    """

    xls_file = os.path.join(
        "..",
        "..",
        "..",
        "data",
        "alfasim",
        "from_plots",
        "alfasim_file_two_edges_heterogeneous_data.xlsx",
    )

    return {
        "dataframe": merge_tabs(xls_file),
        "variable_names": sorted(
            ["Time", "Absolute Pressure", "Holdup", "Total Oil Mass Flow Rate"]
        ),
        "edge_names": ["Conn 1", "Conn 2"],
        "probe_positions": ([5, 7.98, 10, 14.33, 22.63]),
        "units": sorted(["s", "bar", "m3/m3", "kg/s"]),
        "parametric_run": ["0"],
        "results": {
            "0": {
                "Conn 1": {
                    "22.63": {
                        "position": 22.63,
                        "Absolute Pressure": {"unit": "bar"},
                    },
                    "7.98": {
                        "position": 7.98,
                        "Holdup": {"unit": "m3/m3"},
                        "Total Oil Mass Flow Rate": {"unit": "kg/s"},
                    },
                    "14.33": {
                        "position": 14.33,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                },
                "Conn 2": {
                    "5": {
                        "position": 5.0,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                        "Total Oil Mass Flow Rate": {"unit": "kg/s"},
                    },
                    "10": {
                        "position": 10.0,
                        "Absolute Pressure": {"unit": "bar"},
                        "Holdup": {"unit": "m3/m3"},
                        "Total Oil Mass Flow Rate": {"unit": "kg/s"},
                    },
                },
            },
        },
    }


def alfasim_file_two_edges_heterogeneous_data_and_parametric_run():
    """
    This fixture contains a dataset with two edges, multiple probe positions and parametric run.
    The probe positions are heterogeneous, i.e., each probe point save a different set of variables.
    """

    xls_file = os.path.join(
        "..",
        "..",
        "..",
        "data",
        "alfasim",
        "from_plots",
        "alfasim_file_two_edges_heterogeneous_data_and_parametric_run.xlsx",
    )

    return {
        "dataframe": merge_tabs(xls_file),
        "variable_names": sorted(
            ["Time", "Absolute Pressure", "Holdup", "Total Oil Mass Flow Rate"]
        ),
        "edge_names": ["Conn 1", "Conn 2"],
        "probe_positions": ([5, 7.98, 10, 14.33, 22.63]),
        "units": sorted(["s", "Pa", "m3/m3", "kg/s"]),
        "parametric_runs": ["0", "1"],
        "results": {
            "0": {
                "Conn 1": {
                    "22.63": {
                        "position": 22.63,
                        "Absolute Pressure": {"unit": "Pa"},
                    },
                    "7.98": {
                        "position": 7.98,
                        "Holdup": {"unit": "m3/m3"},
                        "Total Oil Mass Flow Rate": {"unit": "kg/s"},
                    },
                    "14.33": {
                        "position": 14.33,
                        "Absolute Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                },
                "Conn 2": {
                    "5": {
                        "position": 5.0,
                        "Absolute Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "m3/m3"},
                        "Total Oil Mass Flow Rate": {"unit": "kg/s"},
                    },
                    "10": {
                        "position": 10.0,
                        "Absolute Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "m3/m3"},
                        "Total Oil Mass Flow Rate": {"unit": "kg/s"},
                    },
                },
            },
            "1": {
                "Conn 1": {
                    "22.63": {
                        "position": 22.63,
                        "Absolute Pressure": {"unit": "Pa"},
                    },
                    "7.98": {
                        "position": 7.98,
                        "Holdup": {"unit": "m3/m3"},
                        "Total Oil Mass Flow Rate": {"unit": "kg/s"},
                    },
                    "14.33": {
                        "position": 14.33,
                        "Absolute Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "m3/m3"},
                    },
                },
                "Conn 2": {
                    "5": {
                        "position": 5.0,
                        "Absolute Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "m3/m3"},
                        "Total Oil Mass Flow Rate": {"unit": "kg/s"},
                    },
                    "10": {
                        "position": 10.0,
                        "Absolute Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "m3/m3"},
                        "Total Oil Mass Flow Rate": {"unit": "kg/s"},
                    },
                },
            },
        },
    }


@pytest.fixture(
    scope="session",
    params=[
        alfasim_file_single_edge_homogeneous_data(),
        alfasim_file_single_edge_homogeneous_data_and_parametric_run(),
        alfasim_file_two_edges_homogeneous_data(),
        alfasim_file_two_edges_homogeneous_data_and_parametric_run(),
        alfasim_file_two_edges_heterogeneous_data(),
        alfasim_file_two_edges_heterogeneous_data_and_parametric_run(),
    ],
)
def alfasim_file(request):
    return request.param


@pytest.fixture()
def shuffled_alfasim_files(alfasim_file):
    _shuffled_alfasim_files = []
    """
    Shuffling column order to mimic different edge, variable and position possible order.
    From a single dataframe, 100 new random dataframes are generated
    """
    N_SHUFFLE_TESTS = 100
    for _ in range(N_SHUFFLE_TESTS):
        alfasim_file_copy = alfasim_file.copy()
        df_shuffle = alfasim_file_copy["dataframe"].copy()
        alfasim_file_copy["dataframe"] = shuffle_dataframe(df_shuffle)
        _shuffled_alfasim_files.append(alfasim_file_copy)
    return _shuffled_alfasim_files
