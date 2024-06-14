"""
POST /validate: Accepts a JSON payload and validates the data.
POST /get_factors: Accepts a JSON payload, maps the factors, and returns the results in JSON format.

"""

import os
from flask import Blueprint, request, jsonify
import json

main = Blueprint('main', __name__)

# Determine the path to the data.json file
current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, '../data.json')

# Load data from JSON file
with open(data_path) as f:
    data = json.load(f)["data"]

# If the data.json file is empty or does not exist, raise an error
if not data:
    raise ValueError("Data is empty")

# If the data.json file contains duplicate entries, raise an error
unique_entries = {entry["var_name"] + entry["category"] for entry in data}
if len(unique_entries) != len(data):
    raise ValueError("Data contains duplicate entries")

def validate_a_sample(sample):
    """
    Validates a sample against the data.

    Args:
        sample (dict): A dictionary containing the sample data.

    Returns:
        A dictionary containing the sample data and the validation status.
    """
    is_valid = False
    for entry in data:
        if sample["var_name"] == entry["var_name"] and sample["category"] == entry["category"]:
            is_valid = True
    return is_valid

@main.route('/validate', methods=['POST'])
def validate():
    """
    Validates the input data and returns a JSON response.

    Returns:
        A JSON response with a success message if the validation is successful,
        otherwise returns a JSON response with an error message.
    """
    input_data = request.get_json()["data"]
    if not input_data:
        return jsonify({
            "status": "error",
            "message": "No data provided"}), 400

    errors = []

    for item in input_data:
        is_valid = validate_a_sample(item)
        if not is_valid: # if the item is not valid, add it to the errors list
            errors.append(item)

    if not errors:
        return jsonify({
            "status": "success",
            "message": "Validation successful"}), 200
    else:
        return jsonify({
            "status": "error",
            "message": "Validation failed. The return data are invalid:",
            "data": errors}), 400