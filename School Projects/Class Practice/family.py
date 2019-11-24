# Define Family class variable


class Family:
    def __init__(self, name, street_address, city, state, zip_code, age, phone_number):
        self.__name = name
        self.__street_address = street_address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__age = age
        self.__phone_number = phone_number
        
    def set_name(self, name):
        self.__name = name
    
    def set_street_address(self, street_address):
        self.__street_address = street_address

    def set_city(self, city):
        self.__city = city

    def set_state(self, state):
        self.__state = state

    def set_zip_code(self, zip_code):
        self.__zip_code = zip_code
    
    def set_age(self, age):
        self.__age = age
    
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
    
    def get_name(self):
        return self.__name

    def get_street_address(self):
        return self.__street_address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip_code(self):
        return self.__zip_code
    
    def get_age(self):
        return self.__age
    
    def get_phone_number(self):
        return self.__phone_number
    
    def __str__(self):
        result = f"\tName: {self.get_name()} \n" \
                 f"\tAddress: {self.get_street_address()} \n" \
                 f"\t{self.get_city()}, {self.get_state()} \n" \
                 f"\t{self.get_zip_code()} \n " \
                 f"\tAge: {self.get_age()} \n " \
                 f"\tPhone Number: {self.get_phone_number()}"
        return result
