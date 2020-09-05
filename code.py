from jinja2 import Template
from utils import load_config


def get_rendered_configuration(filename, variables={}):
    """Function to generate configuration from template."""
    with open(f"{filename}") as file_:
        template = Template(file_.read())

    return template.render(**variables)


def main():
    """Main code execution for demo of Pytest at Interop2020."""
    print("Main code execution.")

    variables = load_config("tests/test_routing.yml")
    rendered_output = get_rendered_configuration(
        "templates/routing.j2", variables=variables
    )

    print(rendered_output)


if __name__ == "__main__":
    main()
