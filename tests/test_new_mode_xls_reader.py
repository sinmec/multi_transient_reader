import pytest

from src.xls_reader.new_mode_xls_reader import (
    create_trend_result_dictionary,
    get_trend_variables_names,
    get_trend_variables_number,
    get_trend_probes_position,
    get_trend_probes_position_number,
    get_trend_variables_units,
)
from tests.fixtures.new_datasets import alfasim_file_excel_results


def test_create_trend_result_dictionary(alfasim_file_excel_results):
    results = create_trend_result_dictionary(alfasim_file_excel_results["file"])

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


def test_get_trend_variables_names(alfasim_file_excel_results):
    variable_names = get_trend_variables_names(alfasim_file_excel_results["file"])
    assert variable_names == {key: sorted(set(value)) for key, value in sorted((alfasim_file_excel_results["variable_names"]).items())}


def test_get_trend_variables_number(alfasim_file_excel_results):
    variables_number = get_trend_variables_number(
        alfasim_file_excel_results["file"]
    )
    assert variables_number == {
        key: len(value)
        for key, value in (alfasim_file_excel_results["variable_names"]).items()
    }

def test_get_trend_probes_position(alfasim_file_excel_results):
    probes_position = get_trend_probes_position(alfasim_file_excel_results["file"])
    assert probes_position == {key: sorted(set(value)) for key, value in sorted((alfasim_file_excel_results["probe_positions"]).items())}


def test_get_trend_probes_position_number(alfasim_file_excel_results):
    probes_position_number = get_trend_probes_position_number(
        alfasim_file_excel_results["file"]
    )
    assert probes_position_number == {
        key: len(value)
        for key, value in (alfasim_file_excel_results["probe_positions"]).items()
    }


def test_get_trend_variables_units(alfasim_file_excel_results):
    variables_unit = get_trend_variables_units(
        alfasim_file_excel_results["file"]
    )
    assert variables_unit == sorted(
        alfasim_file_excel_results["units"])
