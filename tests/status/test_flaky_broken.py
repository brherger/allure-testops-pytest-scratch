import allure
import random
import time
import pytest


@allure.id("2")
def test_flakey():
    time.sleep(random.uniform(0, 2.0))
    assert (random.randint(0, 10) % 2) == 0, "Random failure"


def test_broken():
    time.sleep(random.uniform(0, 2.0))
    if (random.randint(0, 10) % 2) == 0:
        raise Exception("This test is broken")
    else:
        assert True


@pytest.mark.xfail
def test_xfail():
    time.sleep(random.uniform(0, 2.0))
    if (random.randint(0, 10) % 2) == 0:
        assert False, "Expected failure"
    else:
        assert True
