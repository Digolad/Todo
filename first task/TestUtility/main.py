import json
import os


class Employee:

    def __init__(
            self, age: int, marital_status: str, specialization: str,
            post: str, experience: int,  name: str):

        """
        initialization of the employee class

        :param age: integer
        :param marital_status: can be Married/Unmarried
        :param specialization: can be Engineer/Manager
        :param post: it is a position which the employee takes
        :param experience: integer
        :param name: I added this field myself. to understand which employee is who,
        if you do not transfer the name, it will be unknown
        :return:
        """

        self.name = name
        self.age = age
        self.marital_status = marital_status
        self.specialization = specialization
        self.post = post
        self.experience = experience

    def get_employee(self) -> dict:
        return {
            'name': self.name,
            'age': self.age,
            'marital_status': self.marital_status,
            'specialization': self.specialization,
            'post': self.post,
            'experience': self.experience
            }

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == '' or value == ' ':
            raise TypeError('The name field gets not be empty and for have only space instead data.')
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if type(value) is not int:
            raise TypeError(f'The age field can get an only whole numbers. The field should not be empty')
        self._age = value

    @property
    def marital_status(self):
        return self._marital_status

    @marital_status.setter
    def marital_status(self, value):
        value = value.lower()
        if value != 'married' and value != 'unmarried':
            raise TypeError(f'The marital status can be married or unmarried.')
        self._marital_status = value

    @property
    def specialization(self):
        return self._specialization

    @specialization.setter
    def specialization(self, value: str):
        value = value.lower()
        if value != 'manager' and value != 'engineer':
            raise ValueError('The specialization can be manager or engineer')
        self._specialization = value

    @property
    def post(self):
        return self._post

    @post.setter
    def post(self, value):
        if value == '' or value == ' ':
            raise TypeError('The name field gets not be empty and for have only space instead data.')
        self._post = value

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        if type(value) is not int:
            raise TypeError('The experience field can get an only whole numbers')
        self._experience = value


class DataManagement:

    def __init__(self, file_name: str = 'data.json'):
        self.file_name = file_name

    def add_employee_list(self, employee_data: list):
        """
        check no space and empty data,
        check the specialization field has manager/engineer data,
        check the age/experience have int data
        if not issue in list the list will add in a file
        :param employee_data: get list of employee
        :return:
        """

        if os.path.exists(self.file_name):
            data = self.get_employee_list()
        else:
            data = []

        data.append(employee_data)
        self.__write_to_file(data=data, mode='w')

    def get_employee_list(self) -> list:
        """
        get data from file, if the file does not exist  or the file has
        len less 98 will return None
        else, 98 chars = minimum structure data entry
        :return: data [{},{},{},..]
        """

        data = self.__reading_file()

        if data is None:
            print('No data in data file')
            return

        if len(data):
            return data
        return

    def show_employee_list(self):
        get_data = self.get_employee_list()
        if get_data is None:
            return
        for line in get_data:
            for key in line:
                print(key, '=', line[key])
            print('\n')

    def delete_employee_from_list(self, name: str):
        """
        check data if no data return False
        check do we have an employee entering a name
        if yes, the detected var will be True and the employee will delete
        if the detected var is  False will print a message end return False
        finally, if we deleted an employee after that next step is saving data in a file
        :param name: get a name what need for find and delete employee
        :return:
        """

        data = self.__reading_file()

        if data is None:
            return False

        detected = False
        for line in data:
            if name == line['name']:
                detected = True
                data.remove(line)

        if detected is not True:
            print(F'No exist data with name: {name}. Nothing to delete')
            return False

        self.__write_to_file(data=data, mode='w')

    def __write_to_file(self, data: list, mode: str):

        with open(self.file_name, mode) as outfile:
            json.dump(data, outfile)

    def __reading_file(self) -> list:
        """
        reading the file
        checking: if file exist and if is not empty
        :return: if file exist and not empty will retrun dict else False
        """

        try:
            with open(self.file_name) as json_file:
                data = json.load(json_file)
                return data

        except BaseException as be:
            print(f'No data to read. {be}')


def main():
    while True:
        data = int(input(
            'Menu of application, choose: \n'
            '1. Add employee \n'
            '2. Get employee list \n'
            '3. Delete employee by Name \n'
            '4. To exit \n', ))
        MF = DataManagement()

        if data == 1:

            name = input('Enter Name ', )
            age = int(input('Enter age ', ))
            marital_status = input('Enter marital status ', )
            specialization = input('Enter specialization ', )
            post = input('Enter post ', )
            experience = int(input('Enter experience ', ))

            EC = Employee(name=name, age=age, marital_status=marital_status,
                          specialization=specialization, post=post, experience=experience)
            data_of_employee = EC.get_employee()
            MF.add_employee_list(data_of_employee)

        elif data == 2:
            MF.show_employee_list()

        elif data == 3:
            consul_data = input('Enter a name of employee to delete ',)
            MF.delete_employee_from_list(consul_data)

        elif data == 4:
            exit()


if __name__ == '__main__':
    main()