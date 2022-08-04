class Person:
    """Person class"""

    def __init__(self, lname, fname, ssn=''):  # Constructor sets all to no value
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        ssn_characters = set("1234567890-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        if ssn and not ssn_characters.issuperset(ssn):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.ssn = ssn  # Social Security Number

        # self._name = name             # should be considered private
        # self.__surname = surname      # considered private, name mangled
        # you can do the underscore with methods too!

    def __str__(self):
        return self.last_name + ", " + self.first_name + ":" + self.ssn

    def __repr__(self):
        return 'Person({},{},{})'.format(self.first_name, self.last_name, self.ssn)

    def display(self):
        return str(self.last_name) + ", " + str(self.first_name) + " SSN: " + str(self.ssn)
