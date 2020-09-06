"""Utilities for use in multiple files in the Interop 2020 project."""
import yaml


def load_config(filename):
    """Load configuration file

    Args:
        filename (str): Name of the string
    """
    # Load Variables
    with open(filename) as file_:
        variables = yaml.safe_load(file_)

    return variables
