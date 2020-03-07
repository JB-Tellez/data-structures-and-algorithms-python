from data_structures_and_algorithms import __version__


def test_version():
    assert __version__ == "0.1.0"

def test_fail_on_purpose_to_test_ci():
    assert False
