import os
from pathlib import Path

import pandas as pd
import pytest


@pytest.fixture(scope="session")
def alfasim_file_single_edge_homogeneous_data():
    """
    This fixture contains a dataset with a single edge and multiple probe positions.
    The probe positions are homogeneous, i.e., have the exact variables at the same points.
    """

    # TODO: Find an elegant way using pytest tools to remove this gambiarra
    file_path = os.path.dirname(__file__)
    xls_file = Path(file_path, "../data/transient_example_short.xlsx")

    return {
        "dataframe": pd.read_excel(xls_file, decimal=","),
        "variable_names": sorted(["Time", "Absolute Pressure", "Holdup"]),
        "edge_names": ["Conn 1"],
        "probe_positions": (
            [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8.0, 8.5, 9, 9.5]
        ),
        "units": sorted(["s", "bar", "m3/m3"]),  # TODO: Sort this data struct
        "results": {
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
    }
