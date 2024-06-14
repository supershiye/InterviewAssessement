# Interview Assessment - Ye Shi

This repository contains deliverables for an interview assessment of Ye Shi.

## Repository Contents

```plaintext
project/
├── app/
│   ├── __init__.py        # Initialization of the Flask app
│   ├── app.py             # Source code of the Flask app
├── data.json              # Data file
├── run.py                 # Main script to run the Flask app
├── test_app.py            # Unit tests for the project
├── requirements.txt       # Python packages required for the project
├── README.md              # This file
```

## Project Description

The project is a Flask app that serves the data in the data.json file. The project has the following endpoints:

1. `POST /validate`: Accepts a JSON payload and validates the data.
2. `POST /get_factors`: Accepts a JSON payload, maps the factors, and returns the results in JSON format.

The port number is set to 5000 and localhost (127.0.0.1) by default.

## Examples

### Example 1

**Input for /validate and /get_factors:**
```json
{
    "data": [
        {"var_name": "country", "category": "UK"},
        {"var_name": "age_group", "category": "30-50"}
    ]
}
```

**Output for /validate:**
```json
{
    "results": "success",
    "message": "Validation successful"
}
```

**Output for /get_factors:**
```json
{
    "results": [
        {"var_name": "country", "factor": "UK", "factor_value": 0.5},
        {"var_name": "age_group", "factor": "30-50", "factor_value": 0.3}
    ]
}
```

### Example 2

**Input for /validate and /get_factors:**
```json
{
    "data": [
        {"var_name": "country", "category": "UK"},
        {"var_name": "age_group", "category": "Invalid Category"}
    ]
}
```

**Output for /validate:**
```json
{
    "results": "failed",
    "message": "Validation failed. The return errors are invalid data:",
    "errors": [
        {"var_name": "age_group", "category": "Invalid Category"}
    ]
}
```

**Output for /get_factors:**
```json
{
    "results": [
        {"var_name": "country", "factor": "UK", "factor_value": 0.5},
        {"var_name": "age_group", "factor": "Invalid Category", "factor_value": "N/A"}
    ]
}
```

### Example 3

**Input for /validate and /get_factors:**
```json
{
    "data": []
}
```

**Output for /validate:**
```json
{
   "results": "failed",
   "message": "No data provided"
}
```

**Output for /get_factors:**
```json
{
    "results": [],
    "message": "No data provided"
}
```

## Environment

This project was developed in **Python 3.12.3** with the following packages:
- flask == 3.0.3
- pytest == 8.2.2
- pytest-flask == 0.8.1
  
It is recommended to set up a virtual environment to run the project by using the following command:
```sh
python3 -m venv /path/to/new/virtual/environment
```

## How to Set Up the Project

1. Clone the repository to your local machine.
   ```sh
   git clone https://github.com/supershiye/InterviewAssessement001.git
   ```
3. Install the required packages by running:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Flask app by running:
   ```sh
   python run.py
   ```
5. The Flask app will be running on `http://127.0.0.1:5000/` by default.
6. Note: The debug mode is set to `True` in the `run.py` file. Please change it to `False` in production.

## How to Test the Project

1. Repeat steps 1 and 2 from the setup instructions to set up the project if you haven't already.
2. Run the unit tests by running:
   ```sh
   pytest
   ```
3. Tests are written in the `test_app.py` file.

## Usage of Git and Git Commands

This project is developed in Visual Studio Code with Git integrated. The basic Git workflow is to create a branch for each feature or bug fix and merge it back to the main branch after testing. The following Git commands are used to manage the project:

```plaintext
1. `git init` to initialize the repository.
2. `git checkout -b {branch name}` to create a new branch and switch to it.
3. `git add .` to stage all the changes.
4. `git commit -m "{commit message}"` to commit the changes.
5. `git push origin {branch name}` to push the changes to the remote repository.
6. `git checkout main` to switch to the main branch.
7. `git pull origin main` to pull the changes from the remote repository.
8. `git merge {branch name}` to merge the changes from the branch to the main branch.
```
