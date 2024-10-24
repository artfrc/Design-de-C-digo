from typing import Dict
from flask import request as FlaskRequest

class Calculator1:
   """
   - Um número é dividido em tres partes iguais.
   
   * A primeira parte é dividida por 4 e seu resultado somado a 7.
   
      - Após, o resultado é elevado ao quadrado e multiplicado por 0.257
      
   * A segunda parte é elevada a potencia de 2.121, dividida por 5 e somada a 1
   
   * Terceira parte mantem o mesmo valor
   
   * Por fim, os três valores são somados e entregue o resultado.
   """
   
   def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
      body = request.json
      inpu_data = self.__validate_body(body)
      splited_number = inpu_data / 3
      
      first_process_result  = self.__first_process(splited_number) 
      second_process_result  = self.__second_process(splited_number)
      calc_result = first_process_result + second_process_result + splited_number
      
      return self.__format_result(calc_result)
      
      
   def __validate_body(self, body: Dict) -> float:
      if "number" not in body:
         raise Exception("Invalid body.")
      
      input_data = body["number"]
      return input_data
   
   def __first_process(self, first_number: float) -> float:
      first_part =  (first_number / 4) + 7
      second_part = (first_part ** 2) * 0.257
      
      return second_part
   
   def __second_process(self, second_number: float) -> float:
      first_part = second_number ** 2.121
      second_part = (first_part / 5) + 1
      
      return second_part
   
   def __format_result(self, calc_result: float) -> float:
      return {
         "data": {
            "Calculator": 1,
            "Result": round(calc_result, 4)
         }
      }
      
