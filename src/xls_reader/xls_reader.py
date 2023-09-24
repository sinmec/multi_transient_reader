def get_variables_names(dataframe):
    variables_names = ['Time']
    column_names = dataframe.keys()
    for item in column_names[1:]:
        pos_first_open_parentheses = item.find("(")
        variables_names.append(item[:pos_first_open_parentheses-1].strip())
    variables_single_names = set(variables_names)
    return sorted(variables_single_names)
def get_number_of_variables(dataframe):
    variables_names = ['Time']
    column_names = dataframe.keys()
    for item in column_names[1:]:
        pos_first_open_parentheses = item.find("(")
        variables_names.append(item[:pos_first_open_parentheses-1].strip())
    number_single_variables_names = len(set(variables_names))
    return number_single_variables_names
def get_number_of_probes(dataframe):
    probes_position = []
    column_names = dataframe.keys()
    for item in column_names[1:]:
        pos_first_open_parentheses = item.find("(")
        pos_second_open_parentheses = item. find("(", pos_first_open_parentheses+1)
        pos_first_open_brackets = item.find("[")
        probes_position.append(item[pos_second_open_parentheses:pos_first_open_brackets-1].strip())
    number_of_single_position_probes = len(set(probes_position))
    return number_of_single_position_probes
def get_probe_location(dataframe):
    probes_position = []
    column_names = dataframe.keys()
    for item in column_names[1:]:
        pos_first_open_parentheses = item.find("(")
        pos_second_open_parentheses = item.find("(", pos_first_open_parentheses + 1)
        pos_first_open_brackets = item.find("[")
        probes_position.append(item[pos_second_open_parentheses+1:pos_first_open_brackets - 1].strip())
    probes_position = [comma.replace(",", ".") for comma in probes_position]
    probes_single_position = set(probes_position)
    return sorted(([float(item) for item in probes_single_position]))

def get_number_of_edges(dataframe):
    edges_names = []
    column_names = dataframe.keys()
    for item in column_names[1:]:
        first_open_parentheses = item.find("(")
        second_open_parentheses = item.find("(", first_open_parentheses + 1)
        edges_names.append(item[first_open_parentheses+1:second_open_parentheses-1].strip())
    single_edges_names_number = len(set(edges_names))
    return single_edges_names_number
def get_edge_names(dataframe):
    edges_names = []
    column_names = dataframe.keys()
    for item in column_names[1:]:
        first_open_parentheses = item.find("(")
        second_open_parentheses = item.find("(", first_open_parentheses + 1)
        edges_names.append(item[first_open_parentheses + 1:second_open_parentheses - 1].strip())
    single_edges_names = set(edges_names)
    return sorted(single_edges_names)

def get_variable_units(dataframe):
    units_names = ['s']
    column_names = dataframe.keys()
    for item in column_names[1:]:
        first_open_brackets = item.find("[")
        second_open_brackets = item.find("[", first_open_brackets + 1)
        first_close_brackets = item.find("]")
        second_close_brackets = item.find("]", first_close_brackets + 1)
        units_names.append(item[second_open_brackets+1:second_close_brackets].strip())
    single_units_names = set(units_names)
    return sorted(single_units_names)
