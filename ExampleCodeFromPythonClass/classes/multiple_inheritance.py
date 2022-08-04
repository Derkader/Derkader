"""
Created on July 9, 2022

@author: derek nash

Multiple Inheritance Assignment
"""
import datetime


class Person:
    """Person class using class Address, Class Composition"""

    def __init__(self, lname, fname, addy='', phone_number=''):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.address = addy
        self.phone_number = phone_number

    def display(self):
        return str(self.last_name) + ", " + str(self.first_name) + '\n' + str(self.address)


# class for recording and displaying employee objects
class Employee:

    # Constructor
    def __init__(self, lname, fname, address, phone_number, salaried, start_date, salary):
        self.last_name = lname
        self.first_name = fname
        self.address = address
        self.phone_number = phone_number
        self.salaried = salaried
        self.start_date = start_date
        self.salary = salary

    def display(self):
        return 'Employee ' + self.first_name + ' ' + self.last_name + '\nStart date: ' + str(
            self.start_date) + '\nSalary: ' + str(self.salary)

    def give_raise(self, amount):
        self.salary += amount


class Manager(Person, Employee):

    # Constructor
    def __init__(self, lname, fname, address, phone_number, start_date, salary, department, direct_reports):
        Person.__init__(self, lname, fname, address, phone_number)
        Employee.__init__(self, lname, fname, address, phone_number, True, start_date, salary)
        self.department = department
        self.direct_reports = direct_reports

    def display(self):
        return 'Manager ' + self.first_name + ' ' + self.last_name + '\nStart date: ' + str(
            self.start_date) + '\nSalary: ' + str(self.salary)

    def display_direct_reports(self):
        my_string = ''
        for emp in self.direct_reports:
            my_string += emp.display() + '\n' + '\n'
        return my_string


# driver
my_underlings = [
    Employee('Sasha', 'Patel', '123 Main Street Urban, Iowa', '555-555-5555', True, datetime.date(2010, 7, 2), 20000),
    Employee('Mouse', 'Minnie', '66 26th St Johnston, Iowa', '444-444-4444', True, datetime.date(2019, 6, 28), 21000),
    Employee('Duck', 'Donald', '2626 NW 57th St Ames, Iowa', '777-777-7777', True, datetime.date(2015, 1, 8), 15000)]
derek_manager = Manager('Nash', 'Derek', '333 Tower Ave Des Moines, Iowa', '111-111-1111',
                        datetime.date(2022, 7, 9), 40000, 'Engineering', my_underlings)
print(derek_manager.display())
print()
print(derek_manager.display_direct_reports())
derek_manager.give_raise(2000)
print(derek_manager.display())
