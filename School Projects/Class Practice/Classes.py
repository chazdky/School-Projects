# Program that uses the Family class


def print_family():
    from family import Family

    fam1 = Family('Chaz Davis', '650 Sherard Circle', 'Lexington', 'Ky', '40517', '35', '859-699-8820')
    fam2 = Family('Charlie Davis', '650 Sherard Circle', 'Lexington', 'Ky', '40517', '66', '859-699-8346')
    fam3 = Family('Chris O\'Callaghan', '1760 Sandhurst Cv', 'Lexington', 'Ky', '40509', '34', '859-619-6238')

    print('Myself: ')
    print(fam1)
    print()
    print('My Father: ')
    print(fam2)
    print()
    print('My Best Friend: ')
    print(fam3)


if __name__ == "__main__":
    print_family()
    print()
