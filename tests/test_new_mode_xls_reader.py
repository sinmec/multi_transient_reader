import pytest

from tests.fixtures.new_datasets import alfasim_file_excel_results
from src.xls_reader.new_mode_xls_reader import (
    create_result_trend_dictionary,
    get_trends_variable_name,
    get_trends_variable_number,
    get_position_of_trends_points,
)


def test_create_result_trend_dictionary(alfasim_file_excel_results):
    results = create_result_trend_dictionary(alfasim_file_excel_results["file"])

    test_results = alfasim_file_excel_results["results"]

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


def test_get_trends_variable_name(alfasim_file_excel_results):
    variable_names = get_trends_variable_name(alfasim_file_excel_results["file"])
    assert variable_names == alfasim_file_excel_results["variable_names"]


def test_get_trends_variable_number(alfasim_file_excel_results):
    number_single_variable_names = get_trends_variable_number(alfasim_file_excel_results["file"])
    assert number_single_variable_names == len(alfasim_file_excel_results["variable_names"])


def test_get_position_of_trends_points(alfasim_file_excel_results):
    probes_single_position = get_position_of_trends_points(alfasim_file_excel_results["file"])
    assert probes_single_position == alfasim_file_excel_results["probe_positions"]
