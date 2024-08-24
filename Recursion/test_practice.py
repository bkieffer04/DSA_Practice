import pytest
from practice import practice


def test_printOnlyEvens(capsys):
    # Test the recursive method
    result = practice.printOnlyEvens(4)

    # Capture the printed output
    captured = capsys.readouterr()
    output = captured.out.strip().split("\n")

    # Test that the correct even numbers are printed
    expected_output = ['4', 'Odd', '2', 'Odd', '0']
    assert output == expected_output

    # Test the return value when val == 0
    assert result == 0
def test_onlyEvens():
    list = [2, 3, 5, 6, 9, 8, 10]
    result = practice.onlyEvens(list, 0)
    expected = [2, 6, 8, 10]
    assert result == expected
def test_findIndexOfVal():
    list = [3, 17, 23, 19, 4, 10, 12]
    result = practice.findIndexOfVal(list, 0, 33)
    expected = 0
    assert result == expected
def test_twoValsSumInSortedList():
    list = [1, 3, 4, 5, 6, 10, 23, 25, 26, 30, 31, 39, 54]
    result = practice.twoValsSumInSortedList(list, 59)
    expected = True
    assert result == expected
def test_twoValsSumInUnsortedList():
    list = [3, 10, 2, 7, 18, 34, 28, 73, 52, 98, 103, 89]
    result = practice.twoValsSumInUnsortedList(list, 125)
    expected = True
    assert result == expected
def test_binarySearch():
    list = [1, 3, 4, 5, 6, 10, 23, 25, 26, 30, 31, 39, 54]
    result = practice.binarySearch(list, 54)
    expected = True
    assert result == expected
def test_generateParanthese():
    result = practice.generateParanthese(3)
    expected = ["((()))","(()())","(())()","()(())","()()()"]
    assert result == expected