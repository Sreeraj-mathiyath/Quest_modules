import unittest 
from app import add,Calculations

# class TestAddDunction(unittest.TestCase):
#     def test_add_positive_number(self):
#         result = add(5,5)
#         self.assertEqual(result,10)

#     def test_add_negative_number(self):
#         result = add(-1,-5)
#         self.assertEqual(result,-6)
    
#     def test_not_equal(self):
#         result= add(2,2)
#         self.assertNotEqual(result,5)


# class TestCalculations(unittest.TestCase):
#     def test_sum(self):
#         calculation = Calculations(8,2)
#         self.assertEqual(calculation.get_sum(),10,'The sum is wrong!')

#     def test_diff(self):
#         calc=Calculations(8,2)
#         self.assertEqual(calc.get_difference(),6,'The difference is wrong!')

#     def test_product(self):
#         calc=Calculations(8,2)
#         self.assertEqual(calc.get_product(),16,'The product is wrong!')

#     def test_quotient(self):
#         calc=Calculations(8,2)
#         self.assertEqual(calc.get_quotient(),4,'The quotient is wrong!')

#     def not_a_test_sum(self):
#         calc = Calculations
#         self.assertEqual(calc.get_sum(),10,'The sum is Wrong')


# class TestCalculations(unittest.TestCase):
"""This means that the calculations object will be initialized before each test is run."""
#     def setUp(self):
#         self.calc=Calculations(8,2)

#     def test_sum(self):
#         self.assertEqual(self.calc.get_sum(),10,'The sum is wrong')



if __name__=='__main__':
    unittest.main()


"""If we want to run the tests in both files, we can use the following line:

>>>python -m unittest -v"""

