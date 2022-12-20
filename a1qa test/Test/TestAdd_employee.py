from TestUtility.main import Employee, DataManagement
import common

import unittest
import json
import os


class TestAddMethod(unittest.TestCase):

    def setUp(self):

        self.path = common.path

        self.MF = DataManagement(self.path)

        self.required_data = common.required_data

        self.data_empty_in_field = common.data_empty_in_field

        self.data_unsupported_in_specialization = common.data_unsupported_in_specialization

        self.data_string_in_int_field = common.data_string_in_int_field

    def doCleanups(self):
        """
        Call the method if you want to delete generated file
        :return:
        """
        try:
            os.remove(self.path)
        except FileNotFoundError:
            # print(f'The file {self.file_name} does not exist. Got the error {FNF}')
            pass

    def test_add_data(self):
        """
        add data, check the data saved in the file
        delete the file after test
        :return:
        """

        for line in self.required_data:
            self.MF.add_employee_list(line)

        with open(self.path, 'r') as outfile:
            data = json.load(outfile)

        self.assertEqual(data, self.required_data)

    def test_add_empty_data(self):
        """
        check impossible to add empty data,
        :return:
        """
        try:
            emp_class = Employee(
                name=self.data_empty_in_field['name'],
                age=self.data_empty_in_field['age'],
                experience=self.data_empty_in_field['experience'],
                marital_status=self.data_empty_in_field['marital_status'],
                specialization=self.data_empty_in_field['specialization'],
                post=self.data_empty_in_field['post']
            )
            data = emp_class.get_employee()
            self.dm.add_employee_list(data)

        except TypeError:
            print('I caught waiting for an exception.')

        file = os.path.exists(self.path)
        self.assertFalse(file)

    def test_add_unsupported_data(self):
        """
        add unsupported data,
        check the data is not saved in the file,
        :return:
        """
        try:
            emp_class = Employee(
                name=self.data_unsupported_in_specialization['name'],
                age=self.data_unsupported_in_specialization['age'],
                experience=self.data_unsupported_in_specialization['experience'],
                marital_status=self.data_unsupported_in_specialization['marital_status'],
                specialization=self.data_unsupported_in_specialization['specialization'],
                post=self.data_unsupported_in_specialization['post']
            )
            data = emp_class.get_employee()
            self.dm.add_employee_list(data)

        except TypeError:
            print('I caught waiting for an exception.')

        file = os.path.exists(self.path)
        self.assertFalse(file)

    def test_add_string_in_int_field(self):
        """
        add string data in int field ,
        check the data is not saved in the file,
        :return:
        """

        try:
            emp_class = Employee(
                name=self.data_string_in_int_field['name'],
                age=self.data_string_in_int_field['age'],
                experience=self.data_string_in_int_field['experience'],
                marital_status=self.data_string_in_int_field['marital_status'],
                specialization=self.data_string_in_int_field['specialization'],
                post=self.data_string_in_int_field['post']
            )
            data = emp_class.get_employee()
            self.dm.add_employee_list(data)

        except TypeError:
            print('I caught waiting for an exception.')

        file = os.path.exists(self.path)
        self.assertFalse(file)


if __name__ == '__main__':
    unittest.main()

