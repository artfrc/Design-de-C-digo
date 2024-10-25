from src.calculators.calculator_2 import Calculator_2
from src.drivers.numpy_handler import NumpyHandler

def Calculator_2_factory():
   numpy_handler = NumpyHandler()
   calc = Calculator_2(numpy_handler)
   return calc