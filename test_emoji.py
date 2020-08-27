import pytest


def test_pass():
    assert True


def test_fail():
    assert False


@pytest.mark.xfail()
def test_expected_failed():
    assert False


@pytest.mark.xfail()
def test_expected_failed_but_not():
    assert True


@pytest.mark.skip("Not fix issue")
def test_skip_case():
    assert True


@pytest.fixture
def gen_error():
    raise Exception("DevOops")


def test_error_case(gen_error):
    assert gen_error
