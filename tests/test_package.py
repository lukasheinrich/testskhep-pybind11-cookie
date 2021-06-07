import testskhep_pybind11_cookie as m
import testskhep_pybind11_cookie._core as cpp


def test_pybind11():
    assert cpp.add(1, 2) == 3
    assert cpp.subtract(1, 2) == -1


def test_version():
    assert m.__version__
