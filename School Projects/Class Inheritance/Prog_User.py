import user_info


def get_prog_user_info():

    prog_user = input("Enter the Employees User Name:  ")
    prog_user_id = input("Enter the Employees User ID:  ")
    prog_user_shift_number = int(input("Enter the Employees shift \n 1 for dayshift or 2 for nightshift:  "))
    prog_user_hourly_pay = float(input("Enter the Employee hourly pay:  "))
    print()
    print()

    worker = user_info.ProductionWorker(prog_user, prog_user_id, prog_user_shift_number, prog_user_hourly_pay)

    print("Production Employees Information:")
    print(f'\tName: {worker.get_user_name()}')
    print(f'\tID Number: {worker.get_user_id()}')
    if worker.get_shift_number() == 1:
        print('\tEmployee works DayShift')
    else:
        print('\tEmployee works Night Shift')
    print(f'\tEmployees Hourly Pay is: {worker.get_hourly_pay():.2f}')


if __name__ == '__main__':
    get_prog_user_info()
    print()
