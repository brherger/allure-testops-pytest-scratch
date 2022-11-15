"""Custom decorators for pytest."""

# ============================================================== #
#  SECTION: Imports                                              #
# ============================================================== #

# third party library
import allure
import pytest

# first party library
# from pytest_testrail_msa.plugin import pytestrail


# ============================================================== #
#  SECTION: Global Definitions                                   #
# ============================================================== #

TESTRAIL_URL = "https://testrail.foo.com/index.php?/cases/view/"

# ============================================================== #
#  SECTION: Helpers Definition                                   #
# ============================================================== #


def compose_decos(decos):
    """Generic combination of decorators."""

    def composition(func):
        for deco in reversed(decos):
            func = deco(func)
        return func

    return composition


# ============================================================== #
#  SECTION: Decorator Definition                                 #
# ============================================================== #

# blocker decorator, will skip remainder of tests in a module after a failure,
#   will add critical severity in allure
blocker = compose_decos(
    (pytest.mark.blocker, allure.severity(allure.severity_level.CRITICAL))
)


def msa_testcase(*args, **kwargs):
    """Combined decorator for pytestrail.case."""

    def inner(func):
        # pytestrail adds all cases at once
        # func = pytestrail.case(*args, **kwargs)(func)

        # allure adds cases one-by-one
        for arg in args:
            func = allure.testcase(
                TESTRAIL_URL + arg.upper().lstrip("C"), name=f"TestRail: {arg}"
            )(func)

        return func

    return inner


def msa_reference(*args, **kwargs):  # pylint: disable=unused-argument
    """Decorator for pytestrail.references."""

    def inner(func):
        # func = pytestrail.reference(*args)(func)

        # allure adds links one-by-one
        for arg in args:
            func = allure.issue(arg)(func)

        return func

    return inner
