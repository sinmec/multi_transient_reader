import os
from pathlib import Path
import re

import pandas as pd

from tests.fixtures.new_datasets import alfasim_file_two_edges_heterogeneous_data_and_parametric_run_excel_results
main_folder =Path(r'C:\Users\Gustavo\Documentos\Engenharia Mecânica - UFSC\Iniciação Cientica - SINMEC\multi_transient_reader\tests\data\data_from_export\two_edges_heterogeneous_data_and_parametric_run.excel_results')

def create_result_trend_dictionary(main_folder):
    results_dict_trends = {}

    for xls in os.listdir(main_folder):

        if xls.endswith('.xls'):
            xls_file = Path(main_folder, xls)
            excel_file = pd.ExcelFile(xls_file)
            abas = excel_file.sheet_names

            if "Global" in xls or "profile"in xls:
                continue

            if "trend" in xls:
                if "Base Run" in xls:
                    trends_name_structure_file = re.match(
                        r'trend-(\w+ \d+) \(([\d,]+) \[(\w+)\]\)-([\w\s]+)-(\d{4}-\d{2}-\d{2})-T(\d{2}-\d{2}-\d{2})',
                        xls)
                else:
                    trends_name_structure_file = re.match(
                        r'trend-([\w ]+ \d+) \(([\d,]+) \[(\w+)\]\)-#(\d+)-(\d{4}-\d{2}-\d{2})-T(\d{2}-\d{2}-\d{2})',
                        xls)

                edge = trends_name_structure_file.group(1)
                position = trends_name_structure_file.group(2).replace(',', '.')

                for aba in abas:
                    df = pd.read_excel(xls_file, sheet_name=aba, header=None, decimal=',')
                    unit = df.iloc[2, 1]
                    variable = df.iloc[0, 1].title()
                    time = df.iloc[4:, 0].astype(float).values
                    variable_values = df.iloc[4:, 1].astype(float).values
                    if "Base Run" in xls:
                        parametric_run = "0"
                    else:
                        parametric_run = df.iloc[3, 1].replace('#', '')

                    if f'{parametric_run}' not in results_dict_trends:
                        results_dict_trends[f'{parametric_run}'] = {}

                    if f'time' not in results_dict_trends[f'{parametric_run}']:
                        results_dict_trends[f'{parametric_run}'][f'time'] = time

                    if f'{edge}' not in results_dict_trends[f'{parametric_run}']:
                        results_dict_trends[f'{parametric_run}'][f'{edge}'] = {}

                    if f'{position}' not in results_dict_trends[f'{parametric_run}'][f'{edge}']:
                        results_dict_trends[f'{parametric_run}'][f'{edge}'][f'{position}'] = {
                            "position": float(position)}

                    if f'{variable}' not in results_dict_trends[f'{parametric_run}'][f'{edge}'][f'{position}']:
                        results_dict_trends[f'{parametric_run}'][f'{edge}'][f'{position}'][f'{variable}'] = {
                            "values": variable_values, "unit": unit}

    return results_dict_trends

def create_result_profile_dictionary(main_folder): #TODO Verify with Rafael and take the test
    results_dict_profile = {}

    for xls in os.listdir(main_folder):


        if xls.endswith('.xls'):
            xls_file = Path(main_folder, xls)
            excel_file = pd.ExcelFile(xls_file)
            abas = excel_file.sheet_names

            if "Global" in xls or "trend" in xls:
                continue

            elif "profile" in xls:
                if "Base Run" in xls:
                    profile_name_structure_file = re.match(
                        r"profile-([\w ]+ \d+)-Base Run-(\d{4}-\d{2}-\d{2})-T(\d{2}-\d{2}-\d{2})", xls)
                else:
                    profile_name_structure_file = re.match(
                        r"profile-([\w ]+ \d+)-#(\d+)-(\d{4}-\d{2}-\d{2})-T(\d{2}-\d{2}-\d{2})", xls)

            edge = profile_name_structure_file.group(1)
            parametric_run = profile_name_structure_file.group(2)

            if f'{parametric_run}' not in results_dict_profile:
                results_dict_profile[f'{parametric_run}'] = {}

            if f'{edge}' not in results_dict_profile[f'{parametric_run}']:
                results_dict_profile[f'{parametric_run}'][f'{edge}'] = {}

            for aba in abas:
                df = pd.read_excel(xls_file, sheet_name=aba, header=None, decimal=",")
                unit = df.iloc[2, 1]
                time = df.iloc[3, 1:].astype(float).values
                variable = df.iloc[0, 1].title()

                results_dict_profile[f'{parametric_run}'][f'time'] = time

                for position_row_index in range(4, len(df)):
                    position = df.iloc[position_row_index, 0]
                    variable_values = df.iloc[position_row_index, 1:].astype(float).values

                    if f'{position}' not in results_dict_profile[f'{parametric_run}'][f'{edge}']:
                        results_dict_profile[f'{parametric_run}'][f'{edge}'][f'{position}'] = {
                            "position": float(position)}

                    if f'{variable}' not in results_dict_profile[f'{parametric_run}'][f'{edge}'][f'{position}']:
                        results_dict_profile[f'{parametric_run}'][f'{edge}'][f'{position}'][f'{variable}'] = {}

                        results_dict_profile[f'{parametric_run}'][f'{edge}'][f'{position}'][f'{variable}'][
                            f'values'] = variable_values
                        results_dict_profile[f'{parametric_run}'][f'{edge}'][f'{position}'][f'{variable}'][
                            f'unit'] = unit

    return results_dict_profile

def get_trends_variable_name(main_folder):
    trends_variable_names = {}

    for xls in os.listdir(main_folder):


        if xls.endswith('.xls'):
            xls_file = Path(main_folder, xls)
            excel_file = pd.ExcelFile(xls_file)
            abas = excel_file.sheet_names

            if "Global" in xls or "profile" in xls:
                continue

            elif "trend" in xls:

                if "Base Run" in xls:
                    trends_name_structure_file = re.match(
                        r'trend-(\w+ \d+) \(([\d,]+) \[(\w+)\]\)-([\w\s]+)-(\d{4}-\d{2}-\d{2})-T(\d{2}-\d{2}-\d{2})',
                        xls)
                else:
                    trends_name_structure_file = re.match(
                        r'trend-([\w ]+ \d+) \(([\d,]+) \[(\w+)\]\)-#(\d+)-(\d{4}-\d{2}-\d{2})-T(\d{2}-\d{2}-\d{2})',
                        xls)

                edge = trends_name_structure_file.group(1)

                for aba in abas:
                    df = pd.read_excel(xls_file, sheet_name=aba, header=None, decimal=',')
                    variable = df.iloc[0, 1].title()

                    if f'{edge}' not in trends_variable_names:
                        trends_variable_names[f'{edge}'] = ["Time"]

                    if variable not in trends_variable_names[f'{edge}']:
                        trends_variable_names[f'{edge}'].append(variable)

    return sorted(list(set(item for sublist in trends_variable_names.values() for item in sublist)))

def get_trends_variable_number(main_folder):
    trends_variable_names = {}

    for xls in os.listdir(main_folder):


        if xls.endswith('.xls'):
            xls_file = Path(main_folder, xls)
            excel_file = pd.ExcelFile(xls_file)
            abas = excel_file.sheet_names

            if "Global" in xls or "profile" in xls:
                continue

            elif "trend" in xls:

                if "Base Run" in xls:
                    trends_name_structure_file = re.match(
                        r'trend-(\w+ \d+) \(([\d,]+) \[(\w+)\]\)-([\w\s]+)-(\d{4}-\d{2}-\d{2})-T(\d{2}-\d{2}-\d{2})',
                        xls)
                else:
                    trends_name_structure_file = re.match(
                        r'trend-([\w ]+ \d+) \(([\d,]+) \[(\w+)\]\)-#(\d+)-(\d{4}-\d{2}-\d{2})-T(\d{2}-\d{2}-\d{2})',
                        xls)

                edge = trends_name_structure_file.group(1)

                for aba in abas:
                    df = pd.read_excel(xls_file, sheet_name=aba, header=None, decimal=',')
                    variable = df.iloc[0, 1].title()

                    if f'{edge}' not in trends_variable_names:
                        trends_variable_names[f'{edge}'] = ["Time"]

                    if variable not in trends_variable_names[f'{edge}']:
                        trends_variable_names[f'{edge}'].append(variable)

    return len(sorted(list(set(item for sublist in trends_variable_names.values() for item in sublist))))

def get_profile_variable_name(main_folder): #TODO Verigy with Rafael
    profile_variable_names = []

    for xls in os.listdir(main_folder):


        if xls.endswith('.xls'):
            xls_file = Path(main_folder, xls)
            excel_file = pd.ExcelFile(xls_file)
            abas = excel_file.sheet_names

            if "Global" in xls or "trend" in xls:
                continue

            elif "profile" in xls:

                for aba in abas:
                    df = pd.read_excel(xls_file, sheet_name=aba, header=None, decimal=",")
                    variable = df.iloc[0, 1].title()

                    if variable not in profile_variable_names:
                        profile_variable_names.append(variable)
                    else:
                        continue

    return set(profile_variable_names)

def get_profile_variable_number(main_folder):#TODO Verigy with Rafael
    profile_variable_names = []

    for xls in os.listdir(main_folder):


        if xls.endswith('.xls'):
            xls_file = Path(main_folder, xls)
            excel_file = pd.ExcelFile(xls_file)
            abas = excel_file.sheet_names

            if "Global" in xls or "trend" in xls:
                continue

            elif "profile" in xls:

                for aba in abas:
                    df = pd.read_excel(xls_file, sheet_name=aba, header=None, decimal=",")
                    variable = df.iloc[0, 1].title()

                    if variable not in profile_variable_names:
                        profile_variable_names.append(variable)
                    else:
                        continue

    return len(set(profile_variable_names))

def get_position_of_trends_points(main_folder):
    trends_position_points = {}

    for xls in os.listdir(main_folder):

        if xls.endswith('.xls'):

            if "Global" in xls or "profile" in xls:
                continue

            if "trend" in xls:
                if "Base Run" in xls:
                    trends_name_structure_file = re.match(
                        r'trend-(\w+ \d+) \(([\d,]+) \[(\w+)\]\)-([\w\s]+)-(\d{4}-\d{2}-\d{2})-T(\d{2}-\d{2}-\d{2})',
                        xls)
                else:
                    trends_name_structure_file = re.match(
                        r'trend-([\w ]+ \d+) \(([\d,]+) \[(\w+)\]\)-#(\d+)-(\d{4}-\d{2}-\d{2})-T(\d{2}-\d{2}-\d{2})',
                        xls)

                edge = trends_name_structure_file.group(1)
                position = trends_name_structure_file.group(2).replace(',', '.')

                if f'{edge}' not in trends_position_points:
                    trends_position_points[edge] = []
                if position not in trends_position_points[edge]:
                    trends_position_points[edge].append(position)

    for edge, positions in trends_position_points.items():
        trends_position_points[edge] = sorted(positions, key=lambda x: float(x))

    return trends_position_points

def get_number_of_trends_points(main_folder):
    trends_number_position_points = {}

    for xls in os.listdir(main_folder):


        if xls.endswith('.xls'):

            if "Global" in xls or "profile" in xls:
                continue

            if "trend" in xls:
                if "Base Run" in xls:
                    trends_name_structure_file = re.match(
                        r'trend-(\w+ \d+) \(([\d,]+) \[(\w+)\]\)-([\w\s]+)-(\d{4}-\d{2}-\d{2})-T(\d{2}-\d{2}-\d{2})',
                        xls)
                else:
                    trends_name_structure_file = re.match(
                        r'trend-([\w ]+ \d+) \(([\d,]+) \[(\w+)\]\)-#(\d+)-(\d{4}-\d{2}-\d{2})-T(\d{2}-\d{2}-\d{2})',
                        xls)

                edge = trends_name_structure_file.group(1)
                position = trends_name_structure_file.group(2).replace(',', '.')

                if f'{edge}' not in trends_number_position_points:
                    trends_number_position_points[edge] = []
                if position not in trends_number_position_points[edge]:
                    trends_number_position_points[edge].append(position)

    for edge in trends_number_position_points:
        trends_number_position_points[edge] = len(trends_number_position_points[edge])
    return trends_number_position_points

def get_trends_variable_units(main_folder):
    trends_units_names = ["s"]

    for xls in os.listdir(main_folder):


        if xls.endswith('.xls'):
            xls_file = Path(main_folder, xls)
            excel_file = pd.ExcelFile(xls_file)
            abas = excel_file.sheet_names

            if "Global" in xls or "profile" in xls:
                continue

            if "trend" in xls:
                for aba in abas:
                    df = pd.read_excel(xls_file, sheet_name=aba, header=None, decimal=',')
                    unit = df.iloc[2, 1]

                    if unit not in trends_units_names:
                        trends_units_names.append(unit)



    return sorted(set(trends_units_names))

a= get_position_of_trends_points(main_folder)
print(a)

b=3