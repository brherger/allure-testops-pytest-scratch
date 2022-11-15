import allure
import pytest


@pytest.fixture(autouse=True)
def setup_fixture_1():
    pass


@pytest.fixture(autouse=True)
def setup_fixture_2(setup_fixture_1):
    with allure.step('Set up fixture 2 sub step'):
        pass


@pytest.fixture(autouse=True)
def teardown_fixture_1():
    yield
    pass


@pytest.fixture(autouse=True)
def teardown_fixture_2(teardown_fixture_1):
    yield
    with allure.step('Tear down fixture 2 sub step'):
        pass


@allure.step
def step1():
    pass


@allure.step
def step_with_nested_steps():
    nested_step()


@allure.step
def nested_step():
    pass


def test_step_usage():
    step1()

    with allure.step('step2'):
        pass

    step_with_nested_steps()


def test_step_usage_w_failure():
    step1()

    with allure.step('step2'):
        assert False, "Intentional Failure"

    step_with_nested_steps()
