import pytest


def plus(x, y):
	return float(x+y)


# @pytest.mark.parametrize("x, y, o", (2.5, 2.5, 5))
def test_plus():
    assert plus(2.5, 2.5) == 5.0


@pytest.mark.parametrize("x, y, z", [(2.5, 2.5, 5.0)])
def test_plus2(x, y, z):
    assert plus(x, y) == z


def test_plus3():
	try:
		assert plus(2.5, 2.5) == 5.1
	except AssertionError:
		pass



s = ['r', 125, None, ['2', 57]]


def testlist():
	# s.insert(i, x)
	s.append(4)
	return s


def test_testlist():
	assert testlist() is not None


def test_set_comparison():
    assert s.append(3) 