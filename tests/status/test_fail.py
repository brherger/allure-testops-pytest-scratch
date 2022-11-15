import allure
import random
import time


@allure.id("3")
def test_fail_always():
    time.sleep(random.uniform(0, 2.0))
    assert False, "Verified failure"
