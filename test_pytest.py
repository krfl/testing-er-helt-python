import pytest
import time

import sys


def example(x):
    return x + 1


def raise_exception():
    raise Exception("Whoopsie")


def setup_module():
    pass


def setup_function():
    pass


def teardown_module():
    pass


def teardown_function():
    pass


@pytest.mark.fast
def test_example():
    assert example(1) == 2


@pytest.mark.slow
def test_exception():
    time.sleep(3)
    with pytest.raises(Exception):
        raise_exception()


# @pytest.mark.skipif(sys.platform == 'darwin', reason="does not run on mac")
@pytest.mark.skip
def test_skipped():
    assert False


@pytest.mark.parametrize(
    "a, b",
    [
        (1, 1),
        ((1, 1, "a"), (1, 1, "b"))
    ]
)
def test_equals(a, b):
    assert a == b
