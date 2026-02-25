import pytest

def test_divide_zero(divide_func):
    with pytest.raises(ZeroDivisionError) as exc_info:
        divide_func(4, 0)

    assert "division by zero" in str(exc_info.value)

def test_divide_custom_zero(divide_custom_func):
    with pytest.raises(ValueError) as exc_info:
        divide_custom_func(4, 0)

    assert "zero divide is forbidden" in str(exc_info.value)
