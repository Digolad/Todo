from unittest import TestLoader, TestSuite, TextTestRunner

from Test.TestAdd_employee import TestAddMethod
from Test.TestGet_employee_list import TestGetMethod
from Test.TestRemove_employee import TestRemoveMethod

if __name__ == '__main__':
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(TestAddMethod),
        loader.loadTestsFromTestCase(TestGetMethod),
        loader.loadTestsFromTestCase(TestRemoveMethod)
    ))
    runner = TextTestRunner(verbosity=1)
    runner.run(suite)