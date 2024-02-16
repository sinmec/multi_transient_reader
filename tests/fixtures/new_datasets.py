def alfasim_file_trends_export():
    """
    This fixture contains a dataset with three edges, multiple probe positions and parametric run.
    The probe positions are heterogeneous, i.e., each probe point save a different set of variables.
    This is saved by a different type
    """

    # TODO: Find an elegant way using pytest tools to remove this gambiarra
    file_path = os.path.dirname(__file__)
    xls_file = Path(
        file_path,
        "../data/alfasim_file_two_edges_heterogeneous_data_and_parametric_run.xlsx",
    )

    return {
        "dataframe": merge_tabs(xls_file),
        "variable_names": sorted(
            ["Time", "Absolute Pressure", "Holdup", "Total Oil Mass Flow Rate"]
        ),
        "edge_names": ["Conn 1", "Conn 2"],
        "probe_positions": ([5, 7.98, 10, 14.33, 22.63]),
        "units": sorted(["s", "Pa", "m3/m3", "kg/s"]),  # TODO: Sort this data struct
        "parametric_runs": ["0", "1"],
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
                            "values": array([3.0, 3.0, 3.0, 3.0, 3.0]),
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