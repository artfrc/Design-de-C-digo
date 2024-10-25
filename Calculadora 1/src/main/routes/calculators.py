from flask import Blueprint, jsonify, request
from src.calculators.calculator_1 import Calculator_1
from src.main.factories.calculator_2_factory import Calculator_2_factory

calc_route_bp = Blueprint("calc_routes", __name__)

@calc_route_bp.route('/calculator/1',  methods=['POST'])
def calculator_1():
  calc = Calculator_1()
  response = calc.calculate(request)
  
  return jsonify(response)

@calc_route_bp.route('/calculator/2',  methods=['POST'])
def calculator_2():
  calc = Calculator_2_factory()
  response = calc.calculate(request)
  
  return jsonify(response)