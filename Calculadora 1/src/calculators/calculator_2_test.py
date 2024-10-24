from typing import Dict
from src.calculators.calculator_2 import Calculator_2

class MockRequest:
   def __init__(self, body: Dict) -> None:
      self.json = body

def test_calculate():
   mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})
   calc2 = Calculator_2()
   response = calc2.calculate(mock_request)
   
   assert isinstance(response, dict)
   assert response == {'data': {'Calculator': 2, 'Result': 0.081}}