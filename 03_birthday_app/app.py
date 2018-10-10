def print_header():
    print('-' * 30)
    print('         Birthday App')
    print('-' * 30)


def get_birthday_from_user():
    year = input('What year were you born [YYYY]: ')
    month = input('What Month were you born [MM]: ')
    day = input('What day were you born [DD]: ')


def compute_days_between_dates():
    pass


def main():
    print_header()
    get_birthday_from_user()
    compute_days_between_dates()


main()
