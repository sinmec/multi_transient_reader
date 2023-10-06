import numpy as np


def get_variable_names(dataframe):
    variable_names = ['Time']
    column_names = dataframe.keys()
    for item in column_names[1:]:
        first_open_parentheses = item.find("(")
        variable_names.append(item[:first_open_parentheses - 1].strip())

    return sorted(set(variable_names))


def get_number_of_variables(dataframe):
    variable_names = ['Time']
    column_names = dataframe.keys()
    for item in column_names[1:]:
        first_open_parentheses = item.find("(")
        variable_names.append(item[:first_open_parentheses - 1].strip())

    return len(set(variable_names))


def get_number_of_probes(dataframe):
    probes_position = []
    column_names = dataframe.keys()
    for item in column_names[1:]:
        first_open_parentheses = item.find("(")
        second_open_parentheses = item.find("(", first_open_parentheses + 1)
        first_open_brackets = item.find("[")
        probes_position.append(item[second_open_parentheses:first_open_brackets - 1].strip())

    return len(set(probes_position))


def get_probe_position(dataframe):
    probes_position = []
    column_names = dataframe.keys()
    for item in column_names[1:]:
        pos_first_open_parentheses = item.find("(")
        pos_second_open_parentheses = item.find("(", pos_first_open_parentheses + 1)
        pos_first_open_brackets = item.find("[")
        probes_position.append(item[pos_second_open_parentheses + 1:pos_first_open_brackets - 1].strip())
    probes_position = [comma.replace(",", ".") for comma in probes_position]

    return sorted(([float(item) for item in set(probes_position)]))


def get_number_of_edges(dataframe):
    edges_names = []
    column_names = dataframe.keys()
    for item in column_names[1:]:
        first_open_parentheses = item.find("(")
        second_open_parentheses = item.find("(", first_open_parentheses + 1)
        edges_names.append(item[first_open_parentheses + 1:second_open_parentheses - 1].strip())

    return len(set(edges_names))


def get_edge_names(dataframe):
    edges_names = []
    column_names = dataframe.keys()
    for item in column_names[1:]:
        first_open_parentheses = item.find("(")
        second_open_parentheses = item.find("(", first_open_parentheses + 1)
        edges_names.append(item[first_open_parentheses + 1:second_open_parentheses - 1].strip())

    return sorted(set(edges_names))


def get_variable_units(dataframe):
    units_names = ['s']
    column_names = dataframe.keys()
    for column_name in column_names[1:]:
        first_open_brackets = column_name.find("[")
        second_open_brackets = column_name.find("[", first_open_brackets + 1)
        first_close_brackets = column_name.find("]")
        second_close_brackets = column_name.find("]", first_close_brackets + 1)
        units_names.append(column_name[second_open_brackets + 1:second_close_brackets].strip())
    return sorted(set(units_names))


# TODO: When we implement a function to read the .xls(x) files
#      , check if the the first column is 'Time[s]'
def check_time_column(dataframe):
    assert dataframe.keys()[0] == 'Time [s]'


def create_results_dictionary(dataframe):
    probe_positions = get_probe_position(dataframe)
    variable_names = get_variable_names(dataframe)
    edge_names = get_edge_names(dataframe)
    units = get_variable_units(dataframe)

    results_dict = {}
    for edge_name in edge_names:
        if edge_name not in results_dict:
            results_dict[edge_name] = {}
        for probe_position in probe_positions:
            if f'{probe_position:g}' not in results_dict[edge_name]:
                results_dict[edge_name][f'{probe_position:g}'] = {'position': probe_position}
            for variable_name in variable_names:
                for unit in units:
                    probe_position_string = f'{probe_position:g}'.replace('.', ',')
                    column_name = f'{variable_name} ({edge_name} ({probe_position_string} [m])) [{unit}]'
                    if column_name in dataframe.keys():
                        results_dict[edge_name][f'{probe_position:g}'][variable_name] = {'unit': unit,
                                                                                         'value': np.array([],
                                                                                                           dtype=float)
                                                                                         }

    return results_dict
