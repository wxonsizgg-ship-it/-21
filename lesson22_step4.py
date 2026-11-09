import pytest

# Добавляем маркер и параметр strict=True к первому тесту
@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True

@pytest.mark.xfail
def test_not_succeed():
    assert False

@pytest.mark.skip
def test_skipped():
    assert False