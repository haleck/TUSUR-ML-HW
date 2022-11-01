from unittest import TestCase, main
from Ex4 import reverse_int


class ReverseIntTest(TestCase):
    def test_reverse_int_1(self):
        input_digit = 1234
        output_digit = 4321
        self.assertEqual(reverse_int(input_digit), output_digit)

    def test_reverse_int_2(self):
        input_digit = -9090
        output_digit = -909
        self.assertEqual(reverse_int(input_digit), output_digit)

    def test_reverse_int_3(self):
        input_digit = 0
        output_digit = 0
        self.assertEqual(reverse_int(input_digit), output_digit)

    def test_reverse_int_4(self):
        input_digit = -90009
        output_digit = -90009
        self.assertEqual(reverse_int(input_digit), output_digit)

    def test_reverse_int_5(self):
        input_digit = +23
        output_digit = 32
        self.assertEqual(reverse_int(input_digit), output_digit)

    def test_reverse_int_6(self):
        with self.assertRaises(TypeError) as e:
            reverse_int('Test')
        self.assertEqual('Передано не целое число', e.exception.args[0])

    def test_reverse_int_7(self):
        with self.assertRaises(TypeError) as e:
            reverse_int(-10.2)
        self.assertEqual('Передано не целое число', e.exception.args[0])


if __name__ == "__main__":
    main()
