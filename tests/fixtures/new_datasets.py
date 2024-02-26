import os

import pytest


def alfasim_file_three_edges_heterogenous_data_and_parametric_run_excel_results():
    """
    This fixture contains a dataset with three edges, multiple probe positions and parametric run.
    The probe positions are heterogeneous, i.e., each probe point save a different set of variables.
    This is saved by a different type
    """

    # TODO: Find an elegant way using pytest tools to remove this gambiarra

    folder_path = os.path.join("data","data_from_export","three_edges_heterogenous_data_and_parametric_run.excel_results")

    return {
        "file": folder_path ,
        "variable_names": {'Conn 1': ['Holdup', 'Pressure', 'Time'],
 'Conn 2': ['Time','Flow Pattern', 'Pressure'],
 'Conn 3': ['Time','Flow Pattern', 'Holdup', 'Pressure']}
,
        "edge_names": ["Conn 1", "Conn 2","Conn 3"],
        "probe_positions": {'Conn 1': ['18', '7'], 'Conn 2': ['25'], 'Conn 3': ['500']},
        "units": sorted(['-', 'Pa', 's']),
        "parametric_runs": ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"],
        "results": {
            "0": {
                "Conn 1": {
                    "18": {"position": 18.0, "Pressure": {"unit": "Pa"}},
                    "7": {
                        "position": 7.0,
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    },
                },
                "Conn 2": {
                    "25": {
                        "position": 25.0,
                        "Flow Pattern": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
                "Conn 3": {
                    "500": {
                        "position": 500.0,
                        "Flow Pattern": {"unit": "-"},
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
            },
            "1": {
                "Conn 1": {
                    "18": {"position": 18.0, "Pressure": {"unit": "Pa"}},
                    "7": {
                        "position": 7.0,
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    },
                },
                "Conn 2": {
                    "25": {
                        "position": 25.0,
                        "Flow Pattern": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
                "Conn 3": {
                    "500": {
                        "position": 500.0,
                        "Flow Pattern": {"unit": "-"},
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
            },
            "2": {
                "Conn 1": {
                    "18": {"position": 18.0, "Pressure": {"unit": "Pa"}},
                    "7": {
                        "position": 7.0,
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    },
                },
                "Conn 2": {
                    "25": {
                        "position": 25.0,
                        "Flow Pattern": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
                "Conn 3": {
                    "500": {
                        "position": 500.0,
                        "Flow Pattern": {"unit": "-"},
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
            },
            "3": {
                "Conn 1": {
                    "18": {"position": 18.0, "Pressure": {"unit": "Pa"}},
                    "7": {
                        "position": 7.0,
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    },
                },
                "Conn 2": {
                    "25": {
                        "position": 25.0,
                        "Flow Pattern": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
                "Conn 3": {
                    "500": {
                        "position": 500.0,
                        "Flow Pattern": {"unit": "-"},
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
            },
            "4": {
                "Conn 1": {
                    "18": {"position": 18.0, "Pressure": {"unit": "Pa"}},
                    "7": {
                        "position": 7.0,
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    },
                },
                "Conn 2": {
                    "25": {
                        "position": 25.0,
                        "Flow Pattern": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
                "Conn 3": {
                    "500": {
                        "position": 500.0,
                        "Flow Pattern": {"unit": "-"},
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
            },
            "5": {
                "Conn 1": {
                    "18": {"position": 18.0, "Pressure": {"unit": "Pa"}},
                    "7": {
                        "position": 7.0,
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    },
                },
                "Conn 2": {
                    "25": {
                        "position": 25.0,
                        "Flow Pattern": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
                "Conn 3": {
                    "500": {
                        "position": 500.0,
                        "Flow Pattern": {"unit": "-"},
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
            },
            "6": {
                "Conn 1": {
                    "18": {"position": 18.0, "Pressure": {"unit": "Pa"}},
                    "7": {
                        "position": 7.0,
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    },
                },
                "Conn 2": {
                    "25": {
                        "position": 25.0,
                        "Flow Pattern": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
                "Conn 3": {
                    "500": {
                        "position": 500.0,
                        "Flow Pattern": {"unit": "-"},
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
            },
            "7": {
                "Conn 1": {
                    "18": {"position": 18.0, "Pressure": {"unit": "Pa"}},
                    "7": {
                        "position": 7.0,
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    },
                },
                "Conn 2": {
                    "25": {
                        "position": 25.0,
                        "Flow Pattern": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
                "Conn 3": {
                    "500": {
                        "position": 500.0,
                        "Flow Pattern": {"unit": "-"},
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
            },
            "8": {
                "Conn 1": {
                    "18": {"position": 18.0, "Pressure": {"unit": "Pa"}},
                    "7": {
                        "position": 7.0,
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    },
                },
                "Conn 2": {
                    "25": {
                        "position": 25.0,
                        "Flow Pattern": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
                "Conn 3": {
                    "500": {
                        "position": 500.0,
                        "Flow Pattern": {"unit": "-"},
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
            },
            "9": {
                "Conn 1": {
                    "18": {"position": 18.0, "Pressure": {"unit": "Pa"}},
                    "7": {
                        "position": 7.0,
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    },
                },
                "Conn 2": {
                    "25": {
                        "position": 25.0,
                        "Flow Pattern": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
                "Conn 3": {
                    "500": {
                        "position": 500.0,
                        "Flow Pattern": {"unit": "-"},
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
            },
            "10": {
                "Conn 1": {
                    "18": {"position": 18.0, "Pressure": {"unit": "Pa"}},
                    "7": {
                        "position": 7.0,
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    },
                },
                "Conn 2": {
                    "25": {
                        "position": 25.0,
                        "Flow Pattern": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
                "Conn 3": {
                    "500": {
                        "position": 500.0,
                        "Flow Pattern": {"unit": "-"},
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
            },
            "11": {
                "Conn 1": {
                    "18": {"position": 18.0, "Pressure": {"unit": "Pa"}},
                    "7": {
                        "position": 7.0,
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    },
                },
                "Conn 2": {
                    "25": {
                        "position": 25.0,
                        "Flow Pattern": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
                "Conn 3": {
                    "500": {
                        "position": 500.0,
                        "Flow Pattern": {"unit": "-"},
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
            },
            "12": {
                "Conn 1": {
                    "18": {"position": 18.0, "Pressure": {"unit": "Pa"}},
                    "7": {
                        "position": 7.0,
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    },
                },
                "Conn 2": {
                    "25": {
                        "position": 25.0,
                        "Flow Pattern": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
                "Conn 3": {
                    "500": {
                        "position": 500.0,
                        "Flow Pattern": {"unit": "-"},
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
            },
            "13": {
                "Conn 1": {
                    "18": {"position": 18.0, "Pressure": {"unit": "Pa"}},
                    "7": {
                        "position": 7.0,
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    },
                },
                "Conn 2": {
                    "25": {
                        "position": 25.0,
                        "Flow Pattern": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
                "Conn 3": {
                    "500": {
                        "position": 500.0,
                        "Flow Pattern": {
                            "unit": "-",
                        },
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
            },
            "14": {
                "Conn 1": {
                    "18": {"position": 18.0, "Pressure": {"unit": "Pa"}},
                    "7": {
                        "position": 7.0,
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    },
                },
                "Conn 2": {
                    "25": {
                        "position": 25.0,
                        "Flow Pattern": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
                "Conn 3": {
                    "500": {
                        "position": 500.0,
                        "Flow Pattern": {"unit": "-"},
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
            },
            "15": {
                "Conn 1": {
                    "18": {"position": 18.0, "Pressure": {"unit": "Pa"}},
                    "7": {
                        "position": 7.0,
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    },
                },
                "Conn 2": {
                    "25": {
                        "position": 25.0,
                        "Flow Pattern": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
                "Conn 3": {
                    "500": {
                        "position": 500.0,
                        "Flow Pattern": {"unit": "-"},
                        "Holdup": {"unit": "-"},
                        "Pressure": {"unit": "Pa"},
                    }
                },
            },
        },
    }

def alfasim_file_single_edge_homogeneous_data_excel_results():
    """
    This fixture contains a dataset with a single edge, multiple probe positions and no parametric run.
    The probe positions are homogeneous, i.e., have the exact variables at the same points..
    """

    # TODO: Find an elegant way using pytest tools to remove this gambiarra


    folder_path = os.path.join("data","data_from_export","single_edge_homogeneous_data.excel_results")

    return {
        "file": folder_path,
        "variable_names": {'Conn 1': ['Holdup', 'Pressure', 'Time']},
        "edge_names": ["Conn 1"],
        "probe_positions": {"Conn 1":
            ["1", "1.5", "2","2.5", "3","3.5", "4", "4.5", "5", "5.5", "6", "6.5", "7", "7.5", "8", "8.5", "9", "9.5"]
                            },
        "units": sorted(["s", "Pa", "-"]),
        "parametric_run": ["0"],  # TODO: Sort this data struct
        "results": {
            "0": {
                "Conn 1": {
                    "1": {
                        "position": 1.0,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "1.5": {
                        "position": 1.5,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "2": {
                        "position": 2.0,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "2.5": {
                        "position": 2.5,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "3": {
                        "position": 3.0,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "3.5": {
                        "position": 3.5,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "4": {
                        "position": 4.0,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "4.5": {
                        "position": 4.5,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "5": {
                        "position": 5.0,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "5.5": {
                        "position": 5.5,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "6": {
                        "position": 6.0,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "6.5": {
                        "position": 6.5,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "7": {
                        "position": 7.0,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "7.5": {
                        "position": 7.5,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "8": {
                        "position": 8.0,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "8.5": {
                        "position": 8.5,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "9": {
                        "position": 9.0,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "9.5": {
                        "position": 9.5,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                }
            },
        },
    }

def alfasim_file_single_edge_homogeneous_data_and_parametric_run_excel_results():
    """
    This fixture contains a dataset with a single edge, multiple probe positions and parametric run.
    The probe positions are homogeneous, i.e., have the exact variables at the same points..
    """

    # TODO: Find an elegant way using pytest tools to remove this gambiarra


    folder_path = os.path.join("data","data_from_export","single_edge_homogeneous_data_and_parametric_run.excel_results")


    return {
        "file": folder_path,
        "variable_names":{'Conn 1': ['Holdup', 'Pressure', 'Time']},
        "edge_names": ["Conn 1"],
        "probe_positions": {"Conn 1" : ["1", "1.5"]},
        "units": sorted(["s", "Pa", "-"]),  # TODO: Sort this data struct
        "parametric_run": ["0", "1", "2"],
        "results": {
            "0": {
                "Conn 1": {
                    "1": {
                        "position": 1.0,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "1.5": {
                        "position": 1.5,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                },
            },
            "1": {
                "Conn 1": {
                    "1": {
                        "position": 1.0,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "1.5": {
                        "position": 1.5,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                },
            },
            "2": {
                "Conn 1": {
                    "1": {
                        "position": 1.0,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "1.5": {
                        "position": 1.5,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                },
            },
        },
    }

def alfasim_file_two_edges_homogeneous_data_excel_results():
    """
    This fixture contains a dataset with two edges and multiple probe positions.
    The probe positions are homogeneous, i.e., have the exact variables at the same points.
    """

    # TODO: Find an elegant way using pytest tools to remove this gambiarra


    folder_path = os.path.join("data","data_from_export","two_edges_homogeneous_data.excel_results")

    return {
        "file": folder_path,
        "variable_names": {'Conn 1': ['Holdup', 'Pressure', 'Time'],
 'Conn 2': ['Holdup', 'Pressure', 'Time']},
        "edge_names": ["Conn 1", "Conn 2"],
        "probe_positions": {"Conn 1":["22.63",  '7.98'],"Conn 2":["10","5"]},
        "units": sorted(["s", "Pa", "-"]),
        "parametric_run": ["0"],  # TODO: Sort this data struct
        "results": {
            "0": {
                "Conn 1": {
                    "22.63": {
                        "position": 22.63,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "7.98": {
                        "position": 7.98,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                },
                "Conn 2": {
                    "5": {
                        "position": 5.0,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "10": {
                        "position": 10.0,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                },
            },
        },
    }

def alfasim_file_two_edges_homogeneous_data_and_parametric_run_excel_results():
    """
    This fixture contains a dataset with two edges, multiple probe positions and parametric run.
    The probe positions are homogeneous, i.e., have the exact variables at the same points.
    """

    #TODO: Find an elegant way using pytest tools to remove this gambiarra


    folder_path = os.path.join("data","data_from_export","two_edges_homogeneous_data_and_parametric_run.excel_results")

    return {
        "file": folder_path,
        "variable_names": {'Conn 1': ['Holdup', 'Pressure', 'Time'],
 'Conn 2': ['Holdup', 'Pressure', 'Time']},
        "edge_names": ["Conn 1", "Conn 2"],
        "probe_positions":  {'Conn 1': ['22.63', '7.98'], 'Conn 2': ['10', '5']},
        "units": sorted(["s", "Pa", "-"]),  # TODO: Sort this data struct
        "parametric_run": ["0", "1", "2"],
        "results": {
            "0": {
                "Conn 1": {
                    "22.63": {
                        "position": 22.63,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "7.98": {
                        "position": 7.98,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                },
                "Conn 2": {
                    "5": {
                        "position": 5.0,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "10": {
                        "position": 10.0,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                },
            },
            "1": {
                "Conn 1": {
                    "22.63": {
                        "position": 22.63,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "7.98": {
                        "position": 7.98,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                },
                "Conn 2": {
                    "5": {
                        "position": 5.0,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "10": {
                        "position": 10.0,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                },
            },
            "2": {
                "Conn 1": {
                    "22.63": {
                        "position": 22.63,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "7.98": {
                        "position": 7.98,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                },
                "Conn 2": {
                    "5": {
                        "position": 5.0,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                    "10": {
                        "position": 10.0,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                },
            },
        },
    }

def alfasim_file_two_edges_heterogeneous_data_excel_results():
    """
    This fixture contains a dataset with two edges and multiple probe positions.
    The probe positions are heterogeneous, i.e., each probe point save a different set of variables.
    """

    # TODO: Find an elegant way using pytest tools to remove this gambiarra
    folder_path = os.path.join("data","data_from_export","two_edges_heterogeneous_data.excel_results")

    return {
        "file": folder_path,
        "variable_names": {'Conn 1': ['Holdup', 'Pressure', 'Time', 'Total Oil Mass Flow Rate'],
 'Conn 2': ['Holdup', 'Pressure', 'Time', 'Total Oil Mass Flow Rate']},
        "edge_names": ["Conn 1", "Conn 2"],
        "probe_positions": {'Conn 1': ['14.33', '22.63', '7.98'], 'Conn 2': ['10', '5']},
        "units": sorted(["s", "Pa", "-", "kg/s"]),
        "parametric_run": ["0"],
        "results": {
            "0": {
                "Conn 1": {
                    "22.63": {
                        "position": 22.63,
                        "Pressure": {"unit": "Pa"},
                    },
                    "7.98": {
                        "position": 7.98,
                        "Holdup": {"unit": "-"},
                        "Total Oil Mass Flow Rate": {"unit": "kg/s"},
                    },
                    "14.33": {
                        "position": 14.33,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                },
                "Conn 2": {
                    "5": {
                        "position": 5.0,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                        "Total Oil Mass Flow Rate": {"unit": "kg/s"},
                    },
                    "10": {
                        "position": 10.0,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                        "Total Oil Mass Flow Rate": {"unit": "kg/s"},
                    },
                },
            },
        },
    }

def alfasim_file_two_edges_heterogeneous_data_and_parametric_run_excel_results():
    """
    This fixture contains a dataset with two edges, multiple probe positions and parametric run.
    The probe positions are heterogeneous, i.e., each probe point save a different set of variables.
    """

    # TODO: Find an elegant way using pytest tools to remove this gambiarra
    folder_path = os.path.join("data","data_from_export","two_edges_heterogeneous_data_and_parametric_run.excel_results")


    return {
        "file": folder_path,
        "variable_names":{'Conn 1': ['Holdup', 'Pressure', 'Time', 'Total Oil Mass Flow Rate'],
 'Conn 2': ['Holdup', 'Pressure', 'Time', 'Total Oil Mass Flow Rate']},
        "edge_names": ["Conn 1", "Conn 2"],
        "probe_positions": {'Conn 1': ['14.33', '22.63', '7.98'], 'Conn 2': ['10', '5']},
        "units": sorted(["s", "Pa", "-", "kg/s"]),  # TODO: Sort this data struct
        "parametric_runs": ["0", "1"],
        "results": {
            "0": {
                "Conn 1": {
                    "22.63": {
                        "position": 22.63,
                        "Pressure": {"unit": "Pa"},
                    },
                    "7.98": {
                        "position": 7.98,
                        "Holdup": {"unit": "-"},
                        "Total Oil Mass Flow Rate": {"unit": "kg/s"},
                    },
                    "14.33": {
                        "position": 14.33,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                },
                "Conn 2": {
                    "5": {
                        "position": 5.0,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                        "Total Oil Mass Flow Rate": {"unit": "kg/s"},
                    },
                    "10": {
                        "position": 10.0,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                        "Total Oil Mass Flow Rate": {"unit": "kg/s"},
                    },
                },
            },
            "1": {
                "Conn 1": {
                    "22.63": {
                        "position": 22.63,
                        "Pressure": {"unit": "Pa"},
                    },
                    "7.98": {
                        "position": 7.98,
                        "Holdup": {"unit": "-"},
                        "Total Oil Mass Flow Rate": {"unit": "kg/s"},
                    },
                    "14.33": {
                        "position": 14.33,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                    },
                },
                "Conn 2": {
                    "5": {
                        "position": 5.0,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                        "Total Oil Mass Flow Rate": {"unit": "kg/s"},
                    },
                    "10": {
                        "position": 10.0,
                        "Pressure": {"unit": "Pa"},
                        "Holdup": {"unit": "-"},
                        "Total Oil Mass Flow Rate": {"unit": "kg/s"},
                    },
                },
            },
        },
    }
@pytest.fixture(
    params=[
        alfasim_file_single_edge_homogeneous_data_excel_results(),
        alfasim_file_three_edges_heterogenous_data_and_parametric_run_excel_results(),
        alfasim_file_single_edge_homogeneous_data_and_parametric_run_excel_results(),
        alfasim_file_two_edges_homogeneous_data_excel_results(),
        alfasim_file_two_edges_homogeneous_data_and_parametric_run_excel_results(),
        alfasim_file_two_edges_heterogeneous_data_excel_results(),
        alfasim_file_two_edges_heterogeneous_data_and_parametric_run_excel_results(),
    ],
)
def alfasim_file_excel_results(request):
    return request.param


