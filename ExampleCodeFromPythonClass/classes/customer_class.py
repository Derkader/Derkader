class Customer:
    """Customer class"""

    def __init__(self, cid, lname, fname, pnumber, addy):  # Constructor sets all to no value
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        phone_number_characters = set("1234567890-()")
        customer_id_characters = set("1234567890")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        if not phone_number_characters.issuperset(pnumber):
            raise ValueError
        if not customer_id_characters.issuperset(cid):
            raise ValueError
        self.customer_id = cid
        self.last_name = lname
        self.first_name = fname
        self.phone_number = pnumber
        self.address = addy

    def __str__(self):
        return self.customer_id + ": " + self.last_name + ", " + self.first_name + " Phone: " + self.phone_number + " Address: " + self.address

    def __repr__(self):
        return 'Customer({},{},{},{},{})'.format(self.customer_id, self.last_name, self.first_name, self.phone_number,
                                                 self.address)

    def change_last_name(self, name):
        self.last_name = name

    def change_first_name(self, name):
        self.first_name = name

    def change_phone_number(self, number):
        self.phone_number = number

    def change_address(self, addy):
        self.address = addy

    def display(self):
        return self.customer_id + ": " + self.last_name + ", " + self.first_name + " Phone: " + self.phone_number + " Address: " + self.address


# Driver code
# Valid customer
customer_one = Customer('123', 'Duck', 'Donald', '(555)555-5555', '123 main street')  # all required
print(str(customer_one))

# Invalid phone
# Wait! try/except needed!
try:
    customer_two = Customer('123', 'Duck', 'Donald', '(555)555-5555P', '123 main street')  # all required
except ValueError:
    print("Error found, customer not created")

# Invalid customer_id
# try/except needed
try:
    customer_two = Customer('ABC', 'Duck', 'Donald', '(555)555-5555', '123 main street')  # all required
except ValueError:
    print("Error found, customer not created")

# Invalid first_name
# try/except needed!
try:
    customer_two = Customer('123', 'Duck', '2', '(555)555-5555', '123 main street')  # all required
except ValueError:
    print("Error found, customer not created")
