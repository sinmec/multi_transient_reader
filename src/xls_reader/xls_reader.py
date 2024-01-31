import numpy as np


def get_variable_names(dataframe):
    variable_names = ["Time"]
    column_names = dataframe.keys()
    for column_name in column_names[1:]:
        if "Time [s]" in column_name:
            continue
        first_colon = column_name.find(":")
        if "Base Run" in column_name or "#" in column_name:
            if column_name.count(":") == 2:
                second_colon = column_name.find(":", first_colon + 1)
                variable_names.append(
                    column_name[first_colon + 1 : second_colon].strip()
                )
            else:
                first_open_parentheses = column_name.find("(")
                variable_names.append(
                    column_name[first_colon + 1 : first_open_parentheses].strip()
                )
        else:
            if column_name.count(":") == 1:
                variable_names.append(column_name[:first_colon].strip())
            else:
                first_open_parentheses = column_name.find("(")
                variable_names.append(column_name[:first_open_parentheses].strip())
    return sorted(set(variable_names))


def get_number_of_variables(dataframe):
    variable_names = ["Time"]
    column_names = dataframe.keys()
    for column_name in column_names[1:]:
        if "Time [s]" in column_name:
            continue
        first_colon = column_name.find(":")
        if "Base Run" in column_name or "#" in column_name:
            if column_name.count(":") == 2:
                second_colon = column_name.find(":", first_colon + 1)
                variable_names.append(
                    column_name[first_colon + 1 : second_colon].strip()
                )
            else:
                first_open_parentheses = column_name.find("(")
                variable_names.append(
                    column_name[first_colon + 1 : first_open_parentheses].strip()
                )
        else:
            if column_name.count(":") == 1:
                variable_names.append(column_name[:first_colon].strip())
            else:
                first_open_parentheses = column_name.find("(")
                variable_names.append(column_name[:first_open_parentheses].strip())
    return len(set(variable_names))


def get_number_of_probes(dataframe):
    probes_position = []
    column_names = dataframe.keys()
    for column_name in column_names:
        if "Time [s]" in column_name:
            continue
        first_open_parentheses = column_name.find("(")
        second_open_parentheses = column_name.find("(", first_open_parentheses + 1)
        first_open_brackets = column_name.find("[")
        probes_position.append(
            column_name[second_open_parentheses : first_open_brackets - 1].strip()
        )

    return len(set(probes_position))


def get_probe_position(dataframe):
    probes_position = []
    column_names = dataframe.keys()
    for column_name in column_names[1:]:
        if "Time [s]" in column_name:
            continue
        pos_first_open_parentheses = column_name.find("(")
        pos_second_open_parentheses = column_name.find(
            "(", pos_first_open_parentheses + 1
        )
        pos_first_open_brackets = column_name.find("[")
        probes_position.append(
            column_name[
                pos_second_open_parentheses + 1 : pos_first_open_brackets - 1
            ].strip()
        )
    probes_position = [comma.replace(",", ".") for comma in probes_position]

    return sorted(([float(item) for item in set(probes_position)]))


def get_number_of_edges(dataframe):
    edges_names = []
    column_names = dataframe.keys()
    for column_name in column_names[1:]:
        if "Time [s]" in column_name:
            continue
        first_open_parentheses = column_name.find("(")
        second_open_parentheses = column_name.find("(", first_open_parentheses + 1)
        edges_names.append(
            column_name[
                first_open_parentheses + 1 : second_open_parentheses - 1
            ].strip()
        )

    return len(set(edges_names))


def get_edge_names(dataframe):
    edges_names = []
    column_names = dataframe.keys()
    for column_name in column_names[1:]:
        if "Time [s]" in column_name:
            continue
        first_open_parentheses = column_name.find("(")
        second_open_parentheses = column_name.find("(", first_open_parentheses + 1)
        edges_names.append(
            column_name[
                first_open_parentheses + 1 : second_open_parentheses - 1
            ].strip()
        )

    return sorted(set(edges_names))


def get_variable_units(dataframe):
    units_names = ["s"]
    column_names = dataframe.keys()
    for column_name in column_names[1:]:
        if "Time [s]" in column_name:
            continue
        first_open_brackets = column_name.find("[")
        second_open_brackets = column_name.find("[", first_open_brackets + 1)
        first_close_brackets = column_name.find("]")
        second_close_brackets = column_name.find("]", first_close_brackets + 1)
        units_names.append(
            column_name[second_open_brackets + 1 : second_close_brackets].strip()
        )
    return sorted(set(units_names))


# TODO: When we implement a function to read the .xls(x) files
#      , check if the the first column is 'Time[s]'
def check_time_column(dataframe):
    return dataframe.keys()[0]
    assert dataframe.keys()[0] == "Time [s]"


def create_results_dictionary(dataframe):
    column_names = dataframe.keys()
    results_dict = {}

    for column_name in column_names:
        if "Time [s]" in column_name:
            time = np.array(dataframe[column_name].tolist(), dtype=float)
        else:
            first_colon = column_name.find(":")
            hashtag = column_name.find("#")
            if "Base Run" in column_name or "#" in column_name:
                if "#" in column_name:
                    parametric_run = column_name[hashtag + 1 : first_colon].strip()
                else:
                    parametric_run = "0"
                results_dict.setdefault(str(parametric_run), {})
                if column_name.count(":") == 2:
                    second_colon = column_name.find(":", first_colon + 1)
                    variable_name = column_name[first_colon + 1 : second_colon].strip()
                else:
                    first_open_parentheses = column_name.find("(")
                    variable_name = column_name[
                        first_colon + 1 : first_open_parentheses
                    ].strip()
            else:
                parametric_run = "0"
                results_dict.setdefault(str(parametric_run), {})
                if column_name.count(":") == 1:
                    variable_name = column_name[:first_colon].strip()
                else:
                    first_open_parentheses = column_name.find("(")
                    variable_name = column_name[:first_open_parentheses].strip()

            first_open_parentheses = column_name.find("(")
            second_open_parentheses = column_name.find("(", first_open_parentheses + 1)
            first_open_brackets = column_name.find("[")
            second_open_brackets = column_name.find("[", first_open_brackets + 1)
            first_close_brackets = column_name.find("]")
            second_close_brackets = column_name.find("]", first_close_brackets + 1)

            edge_name = column_name[
                first_open_parentheses + 1 : second_open_parentheses - 1
            ].strip()

            unit_name = column_name[
                second_open_brackets + 1 : second_close_brackets
            ].strip()

            probe_position_str = column_name[
                second_open_parentheses + 1 : first_open_brackets - 1
            ].strip()
            probe_position = probe_position_str.replace(",", ".")

            results_dict[parametric_run].setdefault("time", np.array(time, dtype=float))
            results_dict[parametric_run].setdefault(edge_name, {})
            results_dict[parametric_run][edge_name].setdefault(
                str(probe_position), {"position": float(probe_position)}
            )
            results_dict[parametric_run][edge_name][probe_position].setdefault(
                variable_name,
                {
                    "unit": unit_name,
                    "values": np.array(dataframe[column_name].tolist(), dtype=float),
                },
            )

    return results_dict
