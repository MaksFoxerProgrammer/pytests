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

def ftest(x, y):
	if (x == y):
		return 1


def test_testlist():
	assert testlist() is not None


@pytest.mark.parametrize("x, y", [(5,5),
	(8, 8)])
def test_set_comparison(x, y):
    assert ftest(x, y) == 1


def test_testlist():
	try:
		assert testlist() is None
	except AssertionError:
		pass