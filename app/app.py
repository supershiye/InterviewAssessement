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
            "results": "failed",
            "message": "No data provided"}), 400

    errors = []

    for item in input_data:
        is_valid = validate_a_sample(item)
        if not is_valid: # if the item is not valid, add it to the errors list
            errors.append(item)

    if not errors:
        return jsonify({
            "results": "success",
            "message": "Validation successful"}), 200
    else:
        return jsonify({
            "results": "failed",
            "message": "Validation failed. The return errors are invalid data:",
            "errors": errors}), 400
    
@main.route('/get_factors', methods=['POST'])
def get_factors():
    """
    Factor Mapping:

    Map the factors from the provided data.json file based on the input values.
    
    Retrieves factors based on input data.

    Returns:
        A JSON response containing the results.
    """
    input_data = request.get_json()["data"]

    if not input_data:
        return jsonify({
            "results": "failed",
            "message": "No data provided"}), 400

    results = []

    for item in input_data:
        
        # Initialize the result with NA values
        result = {  "var_name": item["var_name"],
                    "category": item["category"],
                    "factor": "N/A"}
        
        for entry in data:
            if item["var_name"] == entry["var_name"] and item["category"] == entry["category"]:
                result = {
                    "var_name": item["var_name"],
                    "category": item["category"],
                    "factor": entry["factor"]
                }
                break

        results.append(result)
                # edge case 1: if the category or var_name is not found in the data.json file, the loop will break and the result will not be appended
                    # solved by appending the result to the results list after the loop
                # edge case 2: if the category or var_name is found multiple times in the data.json file, the first match will be appended to the results
                    # solved by checking for duplicates in the data.json file

    if len(results) == len(input_data): # if the results list is the same length as the input data, return the results
        return jsonify({"results": results}), 200
    else:
        return jsonify({
            "results": results,
            "message": "Some of the data are unavailable"}), 400