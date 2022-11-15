import allure
import random
import time


@allure.id("1")
def test_pass_always():
    time.sleep(random.uniform(0, 2.0))
    assert True
