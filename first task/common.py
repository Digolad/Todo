import os

file_name = 'test.json'

path = os.path.abspath(file_name)
required_data = [
        {"name": "Niko", "age": 27, "marital_status": "married", "specialization": "Manager",
         "post": "Program Manager", "experience": 3},
        {"name": "Ivan", "age": 33, "marital_status": "unmarried", "specialization": "Engineer",
         "post": "Manual QA", "experience": 10}
    ]

data_empty_in_field = {
        "name": "ad",
        "age": 27,
        "marital_status": "",
        "specialization": "asdasd",
        "post": "Program Manager",
        "experience": 3
    }

data_unsupported_in_specialization = [
        {"name": "Niko", "age": 27, "marital_status": "married", "specialization": "Manag",
         "post": "Program Manager", "experience": 3},
        {"name": "Ivan", "age": 33, "marital_status": "unmarried", "specialization": "QA",
         "post": "Manual QA", "experience": 10}
    ]

data_string_in_int_field = [
        {"name": "Niko", "age": 27, "marital_status": "married", "specialization": "Manager",
         "post": "Program Manager", "experience": "3"},
        {"name": "Ivan", "age": "33", "marital_status": "unmarried", "specialization": "Engineer",
         "post": "Manual QA", "experience": 10}
    ]

required_data_after_deleted_employee = [
            {"name": "Ivan", "age": 33, "marital_status": "unmarried", "specialization": "Engineer",
             "post": "Manual QA", "experience": 10}
        ]






