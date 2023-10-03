def get_variables_names(dataframe):
    variables_names = ['Time']
    column_names = dataframe.keys()
    for item in column_names[1:]:
        first_open_parentheses = item.find("(")
        variables_names.append(item[:first_open_parentheses-1].strip())
    variables_single_names = set(variables_names)
    return sorted(variables_single_names)
def get_number_of_variables(dataframe):
    variables_names = ['Time']
    column_names = dataframe.keys()
    for item in column_names[1:]:
        first_open_parentheses = item.find("(")
        variables_names.append(item[:first_open_parentheses-1].strip())
    number_single_variables_names = len(set(variables_names))
    return number_single_variables_names
def get_number_of_probes(dataframe):
    probes_position = []
    column_names = dataframe.keys()
    for item in column_names[1:]:
        first_open_parentheses = item.find("(")
        second_open_parentheses = item. find("(",first_open_parentheses+1)
        first_open_brackets = item.find("[")
        probes_position.append(item[second_open_parentheses:first_open_brackets-1].strip())
    number_of_single_position_probes = len(set(probes_position))
    return number_of_single_position_probes
def get_probe_position(dataframe):
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

def create_variables_dictionaries(dataframe):
    variables_dictionaries = []
    probe_positions = get_probe_position(dataframe)
    variables_names = get_variables_names(dataframe)
    variables_names_1 = variables_names.remove('Time')
    edge_names = get_edge_names(dataframe)
    units = get_variable_units(dataframe)
    for item in probe_positions:
        aux = {"probe position": None, "edge": None, "variables": {}}
        aux["probe position"] = item
        item_ = str(item).replace(".",",")
        if ",0" in item_:
            item_ = item_[0:1]
        else:
            item_ = item_
        for item1 in edge_names:
            aux["edge"] = item1
            for item2 in variables_names:
                aux_2={}
                for item3 in units:
                    if (item2 == "Absolute Pressure" and item3 != 'bar') or (item2 == "Holdup" and item3 != 'm3/m3') or (item2 == "Time" and item3 != 's'):
                        continue
                    else:
                        dado = f"{item2} ({item1} ({item_} [m])) [{item3}]"
                        aux_2[item2] = dataframe[dado].tolist()
                        aux["variables"].update(aux_2)
        variables_dictionaries.append(aux)

    return variables_dictionaries

    #dado = f"{item2} ({item1} ({item_} [m])) [{item3}]"
    #or (aux["variables"] == "Holdup" and aux["unit"] != "m3/m3") or (aux["variables"] == "Time" and aux["unit"] != "s")
    # column_names = dataframe.keys()
    # variables =[]
    # for item in column_names[1:]:
    #     first_open_parentheses = item.find("(")
    #     second_open_parentheses = item.find("(", first_open_parentheses + 1)
    #     first_open_brackets = item.find("[")
    #     second_open_brackets = item.find("[", first_open_brackets + 1)
    #     first_close_brackets = item.find("]")
    #     second_close_brackets = item.find("]", first_close_brackets + 1)
    #     probe_position = float((item[second_open_parentheses+1:first_open_brackets].strip()).replace(',','.'))
    #     edge_name = item[first_open_parentheses + 1:second_open_parentheses - 1].strip()
    #     variable_name = (item[:first_open_parentheses - 1].strip())
    #     unit = item[second_open_brackets + 1:second_close_brackets].strip()
    #     dict = {}
    #     variable = {}
    #     dict['position'] = probe_position
    #     dict['edge'] = edge_name
    #     vector = dataframe[item].tolist()
    #     dict['variables'] = {variable_name : 0}
    #     variable_name = vector
    #     variables.append(dict)


# for item3 in units:
#     aux_2["unit"] = item3
#     aux["variables"] = aux_2
#     if (list(aux["variables"].keys())[0] == "Absolute Pressure" and aux['variables']['unit'] != 'bar') or (
#             list(aux["variables"].keys())[0] == "Holdup" and aux['variables']['unit'] != 'm3/m3') or (
#             list(aux["variables"].keys())[0] == "Time" and aux['variables']['unit'] != 's'):
#         continue
#     else:
#         dict.append(aux)
#     print(aux)

# aux_2 = {}
# vector = '[12,3,4,4]'
# aux_2[item2] = vector
# if item2 == "Absolute Pressure":
#     aux_2['unit'] = 'bar'
# elif item2 == "Holdup":
#     aux_2['unit'] = 'm3/m3'
# elif item2 == "Time":
#     aux_2['unit'] = 's'
# aux['variables'].update(aux_2)
# print(aux)


# for item2 in variables_names:
#     aux_2 = {}
#     vector = '[12,3,4,4]'
#     aux_2[item2] = vector
#     for item3 in units:
#         aux_2["unit"] = item3
#         if (list(aux_2.keys())[0] == "Absolute Pressure" and aux_2['unit'] != 'bar') or (
#                 list(aux_2.keys())[0] == "Holdup" and aux_2['unit'] != 'm3/m3') or (
#                 list(aux_2.keys())[0] == "Time" and aux_2['unit'] != 's'):
#             continue
#         else:
#             aux_3 = aux_2[item2]
#             print(aux_3)
#             aux["variables"].update(aux_2)
#             print(aux)
