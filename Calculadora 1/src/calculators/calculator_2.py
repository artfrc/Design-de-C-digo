from flask import request as FlaskRequest
from typing import Dict, List
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface  

class Calculator_2:
   """
   - N números são enviados
   - Todos os N números são multiplicados por 11 e elevados à potência de 0.95
   - Por fim, é retirado o desvio padrão desses resultados e retornado o inverso desses valores (1/result)
   """
   def __init__(self, driver_handler: DriverHandlerInterface) -> None:
      self.__driver_handler = driver_handler
   
   def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore  
      body = request.json
      input_data = self.__validate_body(body)
      calculated_number = self.__process_data(input_data)
      return self.__format_result(calculated_number)

   def __validate_body(self, body: Dict) -> List[float]:
      if "numbers" not in body:
         raise Exception("Invalid body. 'numbers' key is required.")
      
      input_data = body["numbers"]
      if not isinstance(input_data, list):
         raise Exception("'numbers' must be a list.")
      
      try:
         input_data = [float(num) for num in input_data]
      except ValueError:
         raise Exception("All elements in 'numbers' must be convertible to float.")
      
      return input_data
   
   def __process_data(self, input_data: List[float]) -> float:
      first_process_result = [(num * 11) ** 0.95 for num in input_data]

      result = self.__driver_handler.standard_deviation(first_process_result)

      return float(1 / result)
   
   def __format_result(self, calc_result: float) -> Dict:
      return {
         "data": {
            "Calculator": 2,
            "Result": round(calc_result, 4)
         }
      }
