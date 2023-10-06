import os
from pathlib import Path

import pandas as pd
import pytest
import numpy as np

from src.xls_reader.xls_reader import get_variables_names, get_number_of_variables, get_number_of_probes, \
    get_probe_position, get_number_of_edges, get_edge_names, get_variable_units, create_results_dictionary


@pytest.fixture(scope='session')
def alfasim_file_single_edge_homogeneous_data():
    '''
    This fixture contains a dataset with a single edge and multiple probe positions.
    The probe positions are homogeneous, i.e., have the exact variables at the same points.
    '''
    xls_file = Path(os.getcwd(), "transient_example_short.xlsx")

    return {'dataframe': pd.read_excel(xls_file, decimal=","),
            'variable_names': sorted(['Time', 'Absolute Pressure', 'Holdup']),
            'edge_names': ['Conn 1'],
            'probe_positions': ([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8.0, 8.5, 9, 9.5]),
            'units': sorted(['s', 'bar', 'm3/m3']),  # TODO: Sort this data struut
            'results': {'Conn 1':
                            {'1': {'position': 1.0,
                                   'Absolute Pressure': {'unit': 'bar'},
                                   'Holdup': {'unit': 'm3/m3'}},
                             '1.5': {'position': 1.5,
                                     'Absolute Pressure': {'unit': 'bar'},
                                     'Holdup': {'unit': 'm3/m3'}},
                             '2': {'position': 2.0,
                                   'Absolute Pressure': {'unit': 'bar'},
                                   'Holdup': {'unit': 'm3/m3'}},
                             '2.5': {'position': 2.5,
                                     'Absolute Pressure': {'unit': 'bar'},
                                     'Holdup': {'unit': 'm3/m3'}},
                             '3': {'position': 3.0,
                                   'Absolute Pressure': {'unit': 'bar'},
                                   'Holdup': {'unit': 'm3/m3'}},
                             '3.5': {'position': 3.5,
                                     'Absolute Pressure': {'unit': 'bar'},
                                     'Holdup': {'unit': 'm3/m3'}},
                             '4': {'position': 4.0,
                                   'Absolute Pressure': {'unit': 'bar'},
                                   'Holdup': {'unit': 'm3/m3'}},
                             '4.5': {'position': 4.5,
                                     'Absolute Pressure': {'unit': 'bar'},
                                     'Holdup': {'unit': 'm3/m3'}},
                             '5': {'position': 5.0,
                                   'Absolute Pressure': {'unit': 'bar'},
                                   'Holdup': {'unit': 'm3/m3'}},
                             '5.5': {'position': 5.5,
                                     'Absolute Pressure': {'unit': 'bar'},
                                     'Holdup': {'unit': 'm3/m3'}},
                             '6': {'position': 6.0,
                                   'Absolute Pressure': {'unit': 'bar'},
                                   'Holdup': {'unit': 'm3/m3'}},
                             '6.5': {'position': 6.5,
                                     'Absolute Pressure': {'unit': 'bar'},
                                     'Holdup': {'unit': 'm3/m3'}},
                             '7': {'position': 7.0,
                                   'Absolute Pressure': {'unit': 'bar'},
                                   'Holdup': {'unit': 'm3/m3'}},
                             '7.5': {'position': 7.5,
                                     'Absolute Pressure': {'unit': 'bar'},
                                     'Holdup': {'unit': 'm3/m3'}},
                             '8': {'position': 8.0,
                                   'Absolute Pressure': {'unit': 'bar'},
                                   'Holdup': {'unit': 'm3/m3'}},
                             '8.5': {'position': 8.5,
                                     'Absolute Pressure': {'unit': 'bar'},
                                     'Holdup': {'unit': 'm3/m3'}},
                             '9': {'position': 9.0,
                                   'Absolute Pressure': {'unit': 'bar'},
                                   'Holdup': {'unit': 'm3/m3'}},
                             '9.5': {'position': 9.5,
                                     'Absolute Pressure': {'unit': 'bar'},
                                     'Holdup': {'unit': 'm3/m3'}},
                             }
                        }

            }


def test_get_variables_names(alfasim_file_single_edge_homogeneous_data):
    variable_names = get_variables_names(alfasim_file_single_edge_homogeneous_data['dataframe'])
    assert variable_names == alfasim_file_single_edge_homogeneous_data['variable_names']


def test_get_number_of_variables(alfasim_file_single_edge_homogeneous_data):
    number_single_variables_names = get_number_of_variables(alfasim_file_single_edge_homogeneous_data['dataframe'])
    assert number_single_variables_names == len(alfasim_file_single_edge_homogeneous_data['variable_names'])


def test_get_number_of_probes(alfasim_file_single_edge_homogeneous_data):
    number_of_single_position_probes = get_number_of_probes(alfasim_file_single_edge_homogeneous_data['dataframe'])
    assert number_of_single_position_probes == len(alfasim_file_single_edge_homogeneous_data['probe_positions'])


def test_get_probe_position(alfasim_file_single_edge_homogeneous_data):
    probes_single_position = get_probe_position(alfasim_file_single_edge_homogeneous_data['dataframe'])
    assert probes_single_position == alfasim_file_single_edge_homogeneous_data['probe_positions']


def test_get_number_of_edges(alfasim_file_single_edge_homogeneous_data):
    single_edges_names_number = get_number_of_edges(alfasim_file_single_edge_homogeneous_data['dataframe'])
    assert single_edges_names_number == len(alfasim_file_single_edge_homogeneous_data['edge_names'])


def test_get_edge_names(alfasim_file_single_edge_homogeneous_data):
    single_edges_names = get_edge_names(alfasim_file_single_edge_homogeneous_data['dataframe'])
    assert single_edges_names == alfasim_file_single_edge_homogeneous_data['edge_names']


def test_get_variable_units(alfasim_file_single_edge_homogeneous_data):
    unit_names = get_variable_units(alfasim_file_single_edge_homogeneous_data['dataframe'])
    assert unit_names == alfasim_file_single_edge_homogeneous_data['units']


def test_create_variables_dictionaries(alfasim_file_single_edge_homogeneous_data):
    results = create_results_dictionary(alfasim_file_single_edge_homogeneous_data['dataframe'])

    test_results = alfasim_file_single_edge_homogeneous_data['results']

    for edge_name in results:
        for probe_name in results[edge_name]:
            assert results[edge_name][probe_name]['position'] == pytest.approx(test_results[edge_name][probe_name]['position'], abs=1.0e-3)
            for variable_name in results[edge_name][probe_name]:
                if variable_name is not 'position':
                    assert results[edge_name][probe_name][variable_name]['unit'] == test_results[edge_name][probe_name][variable_name]['unit']