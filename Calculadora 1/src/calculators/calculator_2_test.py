from typing import Dict, List
from src.calculators.calculator_2 import Calculator_2
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
   def __init__(self, body: Dict) -> None:
      self.json = body

class MockDriverHandler(DriverHandlerInterface):
   def standard_deviation(self, numbers: List[float]) -> float:
      return 3

def test_calculate_integration():
   mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})
   driver = NumpyHandler()
   calc2 = Calculator_2(driver)
   response = calc2.calculate(mock_request)
   
   assert isinstance(response, dict)
   assert response == {'data': {'Calculator': 2, 'Result': 0.081}}
   
def test_calculate():
   mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})
   driver = MockDriverHandler()
   calc2 = Calculator_2(driver)
   response = calc2.calculate(mock_request)
   
   assert isinstance(response, dict)
   assert response == {'data': {'Calculator': 2, 'Result': 0.3333}}