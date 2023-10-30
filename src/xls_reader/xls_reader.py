def get_variable_names(dataframe):
    variable_names = ["Time"]
    column_names = dataframe.keys()
    for column_name in column_names[1:]:
        first_open_parentheses = column_name.find("(")
        first_colon = column_name.find(":")
        second_colon = column_name.find(":", first_colon + 1)
        if ":" in column_name:
            contador = 0
            posicao = column_name.find(":")
            while posicao != -1:
                contador += 1
                posicao = column_name.find(":", posicao + 1)
            if contador == 1:
                variable_names.append(column_name[first_colon+1: first_open_parentheses - 1].strip())
            elif contador == 2:
                variable_names.append(column_name[first_colon + 1: second_colon].strip())
        else:
            variable_names.append(column_name[: first_open_parentheses - 1].strip())

    return sorted(set(variable_names))


def get_number_of_variables(dataframe):
    variable_names = ["Time"]
    column_names = dataframe.keys()
    for item in column_names[1:]:
        first_open_parentheses = item.find("(")
        variable_names.append(item[: first_open_parentheses - 1].strip())

    return len(set(variable_names))


def get_number_of_probes(dataframe):
    probes_position = []
    column_names = dataframe.keys()
    for item in column_names[1:]:
        first_open_parentheses = item.find("(")
        second_open_parentheses = item.find("(", first_open_parentheses + 1)
        first_open_brackets = item.find("[")
        probes_position.append(
            item[second_open_parentheses : first_open_brackets - 1].strip()
        )

    return len(set(probes_position))


def get_probe_position(dataframe):
    probes_position = []
    column_names = dataframe.keys()
    for item in column_names[1:]:
        pos_first_open_parentheses = item.find("(")
        pos_second_open_parentheses = item.find("(", pos_first_open_parentheses + 1)
        pos_first_open_brackets = item.find("[")
        probes_position.append(
            item[pos_second_open_parentheses + 1 : pos_first_open_brackets - 1].strip()
        )
    probes_position = [comma.replace(",", ".") for comma in probes_position]

    return sorted(([float(item) for item in set(probes_position)]))


def get_number_of_edges(dataframe):
    edges_names = []
    column_names = dataframe.keys()
    for item in column_names[1:]:
        first_open_parentheses = item.find("(")
        second_open_parentheses = item.find("(", first_open_parentheses + 1)
        edges_names.append(
            item[first_open_parentheses + 1 : second_open_parentheses - 1].strip()
        )

    return len(set(edges_names))


def get_edge_names(dataframe):
    edges_names = []
    column_names = dataframe.keys()
    for item in column_names[1:]:
        first_open_parentheses = item.find("(")
        second_open_parentheses = item.find("(", first_open_parentheses + 1)
        edges_names.append(
            item[first_open_parentheses + 1 : second_open_parentheses - 1].strip()
        )

    return sorted(set(edges_names))


def get_variable_units(dataframe):
    units_names = ["s"]
    column_names = dataframe.keys()
    for column_name in column_names[1:]:
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
    assert dataframe.keys()[0] == "Time [s]"


def create_results_dictionary(dataframe):
    column_names = dataframe.keys()
    results_dict = {}
    for column_name in column_names[1:]:
        first_open_parentheses = column_name.find("(")
        second_open_parentheses = column_name.find("(", first_open_parentheses + 1)
        first_open_brackets = column_name.find("[")
        second_open_brackets = column_name.find("[", first_open_brackets + 1)
        first_close_brackets = column_name.find("]")
        second_close_brackets = column_name.find("]", first_close_brackets + 1)
        probe_position = float((column_name[second_open_parentheses + 1 : first_open_brackets].strip()).replace(",", "."))
        edge_name = column_name[first_open_parentheses + 1 : second_open_parentheses - 1].strip()
        variable_name = column_name[: first_open_parentheses - 1].strip()
        unit = column_name[second_open_brackets + 1 : second_close_brackets].strip()

        if edge_name not in results_dict:
            results_dict[edge_name] = {}

        if probe_position not in results_dict[edge_name]:
            probe_position_name = f"{probe_position:g}"
            results_dict[edge_name][probe_position_name] = {"position": probe_position}

        results_dict[edge_name][probe_position_name][variable_name] = {}
        results_dict[edge_name][probe_position_name][variable_name]["unit"] = unit
        results_dict[edge_name][probe_position_name][variable_name][
            "values"
        ] = dataframe[column_name].to_numpy(dtype=float)

    return results_dict
