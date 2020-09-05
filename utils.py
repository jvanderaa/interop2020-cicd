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
