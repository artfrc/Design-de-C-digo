from typing import Dict
from flask import request as FlaskRequest

class Calculator1:
   """
   - Um número é dividido em tres partes iguais.
   
   * A primeira parte é dividida por 4 e seu resultado somado a 7.
   
      - Após, o resultado é elevado ao quadrado e multiplicado por 0.257
      
   * A segunda parte é elevada a potencia de 2.121, dividida por 5 e somada a 1
   
   * Terceira parte mantem o mesmo valor
   """
   
   def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
      body = request.json
      inpu_data = self.__validate_body(body)
      splited_number = inpu_data / 3
      
      first_process_result  = self.__first_process(splited_number) 
      
   def __validate_body(self, body: Dict) -> float:
      if "number" not in body:
         raise Exception("Invalid body.")
      
      input_data = body["number"]
      return input_data
   
   def __first_process(self, first_number: float) -> float:
      first_part =  (first_number / 4) + 7
      second_part = (first_part ** 2) * 0.257
      
      return second_part
      
