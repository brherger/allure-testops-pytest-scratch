import allure
import pytest


def pytest_runtest_setup(item):
    """Helper to facilitate test setups."""
    # decorate all test with allure title

    # apply allure title
    _full_string = (item.obj.__doc__ or item.obj.__name__).strip()
    _title = _full_string.split("\n", 1)[0].strip().rstrip(".")
    if isinstance(item.parent, pytest.Module):
        # test is at module level
        item.obj = allure.title(_title)(item.obj)
    else:
        # test is at class level
        item = allure.title(_title)(item)

