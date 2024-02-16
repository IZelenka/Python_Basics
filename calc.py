MY_CONST: int = 3
MY_VECTOR: list = [1,2,3,4,5]

def add_numbers(a: int, b: int) -> int:
    return a + b


def test_add_numbers() -> None:
    print("Running tests for add_numbers ...")

    assert add_numbers(1, 2) == 3
    assert add_numbers(1, 3) == 4

    print("All tests passed")


if __name__ == "__main__":
    test_add_numbers()
