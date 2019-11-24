class Employee:
    def __init__(self, user_name, user_id):
        self.__user_name = user_name
        self.__user_id = user_id

    def set_user_name(self, user_name):
        self.__user_name = user_name

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_user_name(self):
        return self.__user_name

    def get_user_id(self):
        return self.__user_id


class ProductionWorker(Employee):
    def __init__(self, user_name, user_id, shift_number, hourly_pay):
        Employee.__init__(self, user_name, user_id)
        self.__shift_number = shift_number
        self.__hourly_pay = hourly_pay

    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_hourly_pay(self, hourly_pay):
        self.__hourly_pay = hourly_pay

    def get_shift_number(self):
        return self.__shift_number

    def get_hourly_pay(self):
        return self.__hourly_pay
