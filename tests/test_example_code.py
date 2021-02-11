"""Test of code generation."""
from example_code import get_rendered_configuration
from utils import load_config


def test_load_variables():
    """Test that loading variables works as expected."""
    filename = "tests/test_routing.yml"
    variables = load_config(filename)
    expected_vars = {
        "dns_servers": ["203.0.113.10", "203.0.113.11"],
        "networks": [
            {"area": 0, "inverse_mask": "0.0.0.255", "network": "192.0.2.0"},
            {"area": 0, "inverse_mask": "0.0.0.255", "network": "198.100.51.0"},
        ],
        "router_id": "192.0.2.1",
    }
    assert variables == expected_vars


def test_get_rendered_configuration_for_routing():
    """Test of the template rendering."""
    expected_output = """router ospf 1
 router-id 192.0.2.1
 network 192.0.2.0 0.0.0.255 area 0
 network 198.100.51.0 0.0.0.255 area 0
 """

    vars_filename = "tests/test_routing.yml"
    template_filename = "templates/routing.j2"
    variables = load_config(vars_filename)

    rendered_output = get_rendered_configuration(template_filename, variables=variables)
    assert rendered_output == expected_output
