from TestUtility.main import DataManagement
import common
import unittest
import os
import json


class TestGetMethod(unittest.TestCase):

    def setUp(self):

        self.file_name = common.file_name

        self.path = common.path

        self.MF = DataManagement(self.path)

        self.required_data = common.required_data

    def doCleanups(self):
        """
        Call the method if you want to delete generated file
        :return:
        """
        try:
            os.remove(self.path)
            pass
        except FileNotFoundError:
            # print(f'The file {self.file_name} does not exist. Got the error {FNF}')
            pass

    def test_get_data(self):
        """
        add data, check  the data saved in the file
        get the data from the file
        check the data from file and user lists the same
        delete the file after test
        :return:
        """

        for line in self.required_data:
            self.MF.add_employee_list(line)

        data = self.MF.get_employee_list()
        self.assertEqual(data, self.required_data)

    def test_get_data_if_no_file(self):
        """
        check how the method work if no file
        should be return None

        :return:
        """

        data = self.MF.get_employee_list()
        self.assertIsNone(data)

    def test_get_data_if_file_empty(self):
        """
        check how the method work if the file is empty
        should be return None

        :return:
        """

        open(self.path, 'x').close()
        data = self.MF.get_employee_list()
        self.assertIsNone(data)

    def test_if_file_has_empty_list(self):
        """
        check how the method work if the file has []
        should be return None

        :return:
        """

        with open(self.path, 'w') as outfile:
            json.dump([], outfile)

        data = self.MF.get_employee_list()
        self.assertIsNone(data)


if __name__ == '__main__':
    unittest.main()

