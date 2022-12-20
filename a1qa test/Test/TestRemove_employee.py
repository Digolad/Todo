from TestUtility.main import DataManagement

import common
import unittest
import json
import os


class TestRemoveMethod(unittest.TestCase):

    def setUp(self):

        self.path = common.path
        self.dm = DataManagement(self.path)
        self.list_without_deleted_data = common.required_data_after_deleted_employee
        self.required_data = common.required_data

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

    def test_delete_data_by_name(self):
        """
        add data in a file.
        delete the list with data by entering name
        check if the data by name does not exist
        :return:
        """

        for line in self.required_data:
            self.dm.add_employee_list(line)

        self.dm.delete_employee_from_list("Niko")

        with open(self.path, 'r') as outfile:
            data = json.load(outfile)

        self.assertEqual(data, self.list_without_deleted_data)

    def test_not_delete_data(self):
        """
        add data in a file.
        entering a name what not exist in data
        check the delete method returned False (nothing to delete)
        :return:
        """

        for line in self.required_data:
            self.dm.add_employee_list(line)

        self.assertFalse(self.dm.delete_employee_from_list("Vova"), False)

    def test_no_delete_data_by_other_field(self):
        """
        add data in a file.
        entering a name what not exist in data
        check the delete method returned False (nothing to delete)
        :return:
        """

        for line in self.required_data:
            self.dm.add_employee_list(line)

        for line in self.required_data:
            for key in line:
                if key != 'name':
                    self.assertFalse(self.dm.delete_employee_from_list(line[key]), False)

    def test_no_deleted_file(self):
        """
        delete an employee by name
        check the file is not deleting
        :return:
        """

        for line in self.required_data:
            self.dm.add_employee_list(line)

        self.dm.delete_employee_from_list("Niko")
        self.assertTrue(os.path.exists(path=self.path), 'File not found')


if __name__ == '__main__':
    unittest.main()

