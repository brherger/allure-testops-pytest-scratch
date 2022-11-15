import allure
import random
import time
import pytest


@pytest.mark.skip
def test_skip():
    time.sleep(random.uniform(0, 2.0))
    raise NotImplementedError
