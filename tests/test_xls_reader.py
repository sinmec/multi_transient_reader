import pytest

from src.xls_reader.xls_reader import (
    get_variable_names,
    get_number_of_variables,
    get_number_of_probes,
    get_probe_position,
    get_number_of_edges,
    get_edge_names,
    get_variable_units,
    create_results_dictionary,
)
from tests.fixtures.datasets import alfasim_file_single_edge_homogeneous_data


def test_get_variable_names(alfasim_file_single_edge_homogeneous_data):
    variable_names = get_variable_names(
        alfasim_file_single_edge_homogeneous_data["dataframe"]
    )
    assert variable_names == alfasim_file_single_edge_homogeneous_data["variable_names"]


def test_get_number_of_variables(alfasim_file_single_edge_homogeneous_data):
    number_single_variables_names = get_number_of_variables(
        alfasim_file_single_edge_homogeneous_data["dataframe"]
    )
    assert number_single_variables_names == len(
        alfasim_file_single_edge_homogeneous_data["variable_names"]
    )


def test_get_number_of_probes(alfasim_file_single_edge_homogeneous_data):
    number_of_single_position_probes = get_number_of_probes(
        alfasim_file_single_edge_homogeneous_data["dataframe"]
    )
    assert number_of_single_position_probes == len(
        alfasim_file_single_edge_homogeneous_data["probe_positions"]
    )


def test_get_probe_position(alfasim_file_single_edge_homogeneous_data):
    probes_single_position = get_probe_position(
        alfasim_file_single_edge_homogeneous_data["dataframe"]
    )
    assert (
        probes_single_position
        == alfasim_file_single_edge_homogeneous_data["probe_positions"]
    )


def test_get_number_of_edges(alfasim_file_single_edge_homogeneous_data):
    single_edges_names_number = get_number_of_edges(
        alfasim_file_single_edge_homogeneous_data["dataframe"]
    )
    assert single_edges_names_number == len(
        alfasim_file_single_edge_homogeneous_data["edge_names"]
    )


def test_get_edge_names(alfasim_file_single_edge_homogeneous_data):
    single_edges_names = get_edge_names(
        alfasim_file_single_edge_homogeneous_data["dataframe"]
    )
    assert single_edges_names == alfasim_file_single_edge_homogeneous_data["edge_names"]


def test_get_variable_units(alfasim_file_single_edge_homogeneous_data):
    unit_names = get_variable_units(
        alfasim_file_single_edge_homogeneous_data["dataframe"]
    )
    assert unit_names == alfasim_file_single_edge_homogeneous_data["units"]


def test_create_variables_dictionaries(alfasim_file_single_edge_homogeneous_data):
    results = create_results_dictionary(
        alfasim_file_single_edge_homogeneous_data["dataframe"]
    )

    test_results = alfasim_file_single_edge_homogeneous_data["results"]

    for edge_name in results:
        for probe_name in results[edge_name]:
            assert results[edge_name][probe_name]["position"] == pytest.approx(
                test_results[edge_name][probe_name]["position"], abs=1.0e-3
            )
            for variable_name in results[edge_name][probe_name]:
                if variable_name is not "position":
                    assert (
                        results[edge_name][probe_name][variable_name]["unit"]
                        == test_results[edge_name][probe_name][variable_name]["unit"]
                    )
