"""hogehoge"""
from utility.mock_std import In, Out


def test_mock_input():
    file_path = "tmp/tests/utility/test.txt"
    stdin = In(file_path)

    res = list()
    first_row = stdin.pop()
    res.append(first_row)
    for _ in range(int(first_row)):
        res.append(stdin.pop())
    assert res == ["4", "1 4", "4 3", "4 10", "8 3"]


def test_mock_out():
    file_path = "tmp/tests/utility/test.txt"

    stdout = Out(file_path)
    stdout.add(["4", "1 4", "4 3", "4 10", "8 3"])
    assert stdout.validation == stdout.outputs
