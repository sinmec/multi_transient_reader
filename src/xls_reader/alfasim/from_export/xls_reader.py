import os
import re
from pathlib import Path

import pandas as pd


def create_trend_result_dictionary(main_folder):
    """
    This function creates a dictionary with all the necessary information about the probes. In the first level,
    it performs a parametric run; in the second level, it includes the edges and time simulation;
    in the third level, it incorporates the position as a string; in the fourth level, it covers the position
    as a float and the variable names; in the sixth level, it encompasses the variable measurements and
    their respective units.
    """

    results_trend_dictionary = {}

    for xls in os.listdir(main_folder):
        if xls.endswith(".xls"):
            xls_file = Path(main_folder, xls)
            excel_file = pd.ExcelFile(xls_file)
            sheets = excel_file.sheet_names

            if "Global" in xls or "profile" in xls:
                continue

            if "trend" in xls:
                if "Base Run" in xls:
                    trends_name_structure_file = re.match(
                        r"trend-(\w+ \d+) \(([\d,]+) \[(\w+)\]\)-([\w\s]+)-(\d{4}-\d{2}-\d{2})-T(\d{2}-\d{2}-\d{2})",
                        xls,
                    )
                else:
                    trends_name_structure_file = re.match(
                        r"trend-([\w ]+ \d+) \(([\d,]+) \[(\w+)\]\)-#(\d+)-(\d{4}-\d{2}-\d{2})-T(\d{2}-\d{2}-\d{2})",
                        xls,
                    )

                edge = trends_name_structure_file.group(1)
                position = trends_name_structure_file.group(2).replace(",", ".")

                for sheet in sheets:
                    df = pd.read_excel(
                        xls_file, sheet_name=sheet, header=None, decimal=","
                    )
                    unit = df.iloc[2, 1]
                    variable = df.iloc[0, 1].title()
                    time = df.iloc[4:, 0].astype(float).values
                    variable_values = df.iloc[4:, 1].astype(float).values
                    if "Base Run" in xls:
                        parametric_run = "0"
                    else:
                        parametric_run = df.iloc[3, 1].replace("#", "")

                    if f"{parametric_run}" not in results_trend_dictionary:
                        results_trend_dictionary[f"{parametric_run}"] = {}

                    if f"time" not in results_trend_dictionary[f"{parametric_run}"]:
                        results_trend_dictionary[f"{parametric_run}"][f"time"] = time

                    if f"{edge}" not in results_trend_dictionary[f"{parametric_run}"]:
                        results_trend_dictionary[f"{parametric_run}"][f"{edge}"] = {}

                    if (
                        f"{position}"
                        not in results_trend_dictionary[f"{parametric_run}"][f"{edge}"]
                    ):
                        results_trend_dictionary[f"{parametric_run}"][f"{edge}"][
                            f"{position}"
                        ] = {"position": float(position)}

                    if (
                        f"{variable}"
                        not in results_trend_dictionary[f"{parametric_run}"][f"{edge}"][
                            f"{position}"
                        ]
                    ):
                        results_trend_dictionary[f"{parametric_run}"][f"{edge}"][
                            f"{position}"
                        ][f"{variable}"] = {"values": variable_values, "unit": unit}

    return results_trend_dictionary


def get_trend_variables_names(main_folder):
    """
    This function creates a dictionary with the edges and their respective variable measurements in each one.
    Of course, there can be different probes in the same edge that measure different variables,
    but this function presents a comprehensive overview between the variables and edges.
    """
    trends_variable_names = {}

    for xls in os.listdir(main_folder):
        if xls.endswith(".xls"):
            xls_file = Path(main_folder, xls)
            excel_file = pd.ExcelFile(xls_file)
            sheets = excel_file.sheet_names

            if "Global" in xls or "profile" in xls:
                continue

            elif "trend" in xls:
                if "Base Run" in xls:
                    trends_name_structure_file = re.match(
                        r"trend-(\w+ \d+) \(([\d,]+) \[(\w+)\]\)-([\w\s]+)-(\d{4}-\d{2}-\d{2})-T(\d{2}-\d{2}-\d{2})",
                        xls,
                    )
                else:
                    trends_name_structure_file = re.match(
                        r"trend-([\w ]+ \d+) \(([\d,]+) \[(\w+)\]\)-#(\d+)-(\d{4}-\d{2}-\d{2})-T(\d{2}-\d{2}-\d{2})",
                        xls,
                    )

                edge = trends_name_structure_file.group(1)

                for sheet in sheets:
                    df = pd.read_excel(
                        xls_file, sheet_name=sheet, header=None, decimal=","
                    )
                    variable = df.iloc[0, 1].title()

                    if f"{edge}" not in trends_variable_names:
                        trends_variable_names[f"{edge}"] = ["Time"]

                    if variable not in trends_variable_names[f"{edge}"]:
                        trends_variable_names[f"{edge}"].append(variable)

    return {
        key: sorted(set(values))
        for key, values in sorted(trends_variable_names.items())
    }


def get_trend_variables_number(main_folder):
    """
    The same structure as get_trend_variables_names, but functions as a counter, i.e.,
    it returns the number of measured variables in each edge
    """
    trends_variable_names_number = {}

    for xls in os.listdir(main_folder):
        if xls.endswith(".xls"):
            xls_file = Path(main_folder, xls)
            excel_file = pd.ExcelFile(xls_file)
            abas = excel_file.sheet_names

            if "Global" in xls or "profile" in xls:
                continue

            elif "trend" in xls:
                if "Base Run" in xls:
                    trends_name_structure_file = re.match(
                        r"trend-(\w+ \d+) \(([\d,]+) \[(\w+)\]\)-([\w\s]+)-(\d{4}-\d{2}-\d{2})-T(\d{2}-\d{2}-\d{2})",
                        xls,
                    )
                else:
                    trends_name_structure_file = re.match(
                        r"trend-([\w ]+ \d+) \(([\d,]+) \[(\w+)\]\)-#(\d+)-(\d{4}-\d{2}-\d{2})-T(\d{2}-\d{2}-\d{2})",
                        xls,
                    )

                edge = trends_name_structure_file.group(1)

                for aba in abas:
                    df = pd.read_excel(
                        xls_file, sheet_name=aba, header=None, decimal=","
                    )
                    variable = df.iloc[0, 1].title()

                    if f"{edge}" not in trends_variable_names_number:
                        trends_variable_names_number[f"{edge}"] = ["Time"]

                    if variable not in trends_variable_names_number[f"{edge}"]:
                        trends_variable_names_number[f"{edge}"].append(variable)

    return {key: len(value) for key, value in trends_variable_names_number.items()}


def get_trend_probes_position(main_folder):
    """
    This function associates the position where the variables are being measured in each edge.
    As we can have more than one edge with different configurations
    """
    trend_probes_position = {}

    for xls in os.listdir(main_folder):
        if xls.endswith(".xls"):
            if "Global" in xls or "profile" in xls:
                continue

            if "trend" in xls:
                if "Base Run" in xls:
                    trends_name_structure_file = re.match(
                        r"trend-(\w+ \d+) \(([\d,]+) \[(\w+)\]\)-([\w\s]+)-(\d{4}-\d{2}-\d{2})-T(\d{2}-\d{2}-\d{2})",
                        xls,
                    )
                else:
                    trends_name_structure_file = re.match(
                        r"trend-([\w ]+ \d+) \(([\d,]+) \[(\w+)\]\)-#(\d+)-(\d{4}-\d{2}-\d{2})-T(\d{2}-\d{2}-\d{2})",
                        xls,
                    )

                edge = trends_name_structure_file.group(1)
                position = trends_name_structure_file.group(2).replace(",", ".")

                if f"{edge}" not in trend_probes_position:
                    trend_probes_position[edge] = []
                if position not in trend_probes_position[edge]:
                    trend_probes_position[edge].append(position)

    return {
        key: sorted(set(value)) for key, value in sorted(trend_probes_position.items())
    }


def get_trend_probes_position_number(main_folder):
    """
    This function returns the edge and a number that represents the count of probes in that edge
    """
    trend_probes_position_number = {}

    for xls in os.listdir(main_folder):
        if xls.endswith(".xls"):
            if "Global" in xls or "profile" in xls:
                continue

            if "trend" in xls:
                if "Base Run" in xls:
                    trends_name_structure_file = re.match(
                        r"trend-(\w+ \d+) \(([\d,]+) \[(\w+)\]\)-([\w\s]+)-(\d{4}-\d{2}-\d{2})-T(\d{2}-\d{2}-\d{2})",
                        xls,
                    )
                else:
                    trends_name_structure_file = re.match(
                        r"trend-([\w ]+ \d+) \(([\d,]+) \[(\w+)\]\)-#(\d+)-(\d{4}-\d{2}-\d{2})-T(\d{2}-\d{2}-\d{2})",
                        xls,
                    )

                edge = trends_name_structure_file.group(1)
                position = trends_name_structure_file.group(2).replace(",", ".")

                if f"{edge}" not in trend_probes_position_number:
                    trend_probes_position_number[edge] = []
                if position not in trend_probes_position_number[edge]:
                    trend_probes_position_number[edge].append(position)

    return {key: len(value) for key, value in trend_probes_position_number.items()}


def get_trend_variables_units(main_folder):
    """
    This function returns only the units that were chosen in the variables measurement.
    """
    trends_units_names = ["s"]

    for xls in os.listdir(main_folder):
        if xls.endswith(".xls"):
            xls_file = Path(main_folder, xls)
            excel_file = pd.ExcelFile(xls_file)
            sheets = excel_file.sheet_names

            if "Global" in xls or "profile" in xls:
                continue

            if "trend" in xls:
                for sheet in sheets:
                    df = pd.read_excel(
                        xls_file, sheet_name=sheet, header=None, decimal=","
                    )
                    unit = df.iloc[2, 1]

                    if unit not in trends_units_names:
                        trends_units_names.append(unit)

    return sorted(set(trends_units_names))
