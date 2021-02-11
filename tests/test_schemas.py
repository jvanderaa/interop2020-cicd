"""Python testing of the schema files

Author: Josh VanDeraa (Github: @jvanderaa, Twitter: @vanderaaj)
Version: 0.1 (2020-09)
Expected execution:
    From the root of the project, `pytest -vv`
"""
import os
import json
import yaml
import jsonschema
import pytest
from jsonschema import draft7_format_checker

DIRECTORIES = ["devices", "regions", "sites", "tags"]
YAML_EXCLUSION_FILES = [".travis.yml", ".yamllint.yml"]
SCHEMA_FOLDER = "./schema/schemas"


def get_json_files():
    """
    Function to get all of the JSON files from the schema directory
    """
    # Define list to be used to load the json files in the schema directory
    json_file_list = []

    # Find all of the json files in the schema directory and add to json_file_list
    for root, dirs, files in os.walk(SCHEMA_FOLDER):  # pylint: disable=W0612
        for lcl_file in files:
            if lcl_file.endswith(".json"):
                json_file_list.append(os.path.join(root, lcl_file))

    return json_file_list


def get_var_files():
    """
    Function to get all of the files from the appropriate directories
    """
    # Define list of files to be loaded to have the schema tested against
    file_list = []

    # Find all of the YAML files in the parent directory of the project
    for root, dirs, files in os.walk("."):  # pylint: disable=W0612
        for lcl_file in files:
            if lcl_file.endswith(".yml"):
                if lcl_file not in YAML_EXCLUSION_FILES:
                    file_list.append(os.path.join(root, lcl_file))

    return file_list


JSON_SCHEMAS = get_json_files()
VAR_FILE_LIST = get_var_files()


@pytest.mark.parametrize("test_file", VAR_FILE_LIST)
@pytest.mark.parametrize("json_path", JSON_SCHEMAS)
def test_config_definitions_against_schema(test_file, json_path):
    """
    Pytest functional test
    """
    with open(test_file, encoding="UTF-8") as yamlfile:
        yaml_data = yaml.safe_load(yamlfile)

    print(yaml_data)

    with open(json_path, encoding="UTF-8") as json_file:
        schema = json.load(json_file)

    print(schema)

    jsonschema.validate(
        instance=yaml_data, schema=schema, format_checker=draft7_format_checker
    )
