import pytest

from alfasim.from_plots.xls_reader import (
    get_variable_names,
    get_number_of_variables,
    get_number_of_probes,
    get_probe_position,
    get_number_of_edges,
    get_edge_names,
    get_variable_units,
    create_results_dictionary,
)
from tests.multi_transient_reader.fixtures.alfasim.from_plots.datasets import (
    alfasim_file,
    shuffled_alfasim_files,
)


def test_get_variable_names(alfasim_file):
    variable_names = get_variable_names(alfasim_file["dataframe"])
    assert variable_names == alfasim_file["variable_names"]


def test_get_number_of_variables(alfasim_file):
    number_single_variables_names = get_number_of_variables(alfasim_file["dataframe"])
    assert number_single_variables_names == len(alfasim_file["variable_names"])


def test_get_number_of_probes(alfasim_file):
    number_of_single_position_probes = get_number_of_probes(alfasim_file["dataframe"])
    assert number_of_single_position_probes == len(alfasim_file["probe_positions"])


def test_get_probe_position(alfasim_file):
    probes_single_position = get_probe_position(alfasim_file["dataframe"])
    assert probes_single_position == alfasim_file["probe_positions"]


def test_get_number_of_edges(alfasim_file):
    single_edges_names_number = get_number_of_edges(alfasim_file["dataframe"])
    assert single_edges_names_number == len(alfasim_file["edge_names"])


def test_get_edge_names(alfasim_file):
    single_edges_names = get_edge_names(alfasim_file["dataframe"])
    assert single_edges_names == alfasim_file["edge_names"]


def test_get_variable_units(alfasim_file):
    unit_names = get_variable_units(alfasim_file["dataframe"])
    assert unit_names == alfasim_file["units"]


def test_create_variables_dictionaries(alfasim_file):
    results = create_results_dictionary(alfasim_file["dataframe"])

    test_results = alfasim_file["results"]
    for parametric_run in test_results:
        for edge_name in test_results[parametric_run]:
            for probe_name in test_results[parametric_run][edge_name]:
                assert results[parametric_run][edge_name][probe_name][
                    "position"
                ] == pytest.approx(
                    test_results[parametric_run][edge_name][probe_name]["position"],
                    abs=1.0e-3,
                )
                for variable_name in test_results[parametric_run][edge_name][
                    probe_name
                ]:
                    if variable_name is not "position":
                        assert (
                            results[parametric_run][edge_name][probe_name][
                                variable_name
                            ]["unit"]
                            == test_results[parametric_run][edge_name][probe_name][
                                variable_name
                            ]["unit"]
                        )


def test_create_variables_dictionaries_shuffled_columns(shuffled_alfasim_files):
    for alfasim_file in shuffled_alfasim_files:
        test_create_variables_dictionaries(alfasim_file)
