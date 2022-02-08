import calculator


class TestCalculator:
    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 5 == calculator.subtract(7, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)
