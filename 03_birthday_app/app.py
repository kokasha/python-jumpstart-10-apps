import datetime


def print_header():
    print('-' * 30)
    print('         Birthday App')
    print('-' * 30)


def get_birthday_from_user():
    print('What is your birthday? ')
    year = int(input('What year were you born [YYYY]: '))
    month = int(input('What Month were you born [MM]: '))
    day = int(input('What day were you born [DD]: '))
    date = datetime.date(year, month, day)
    return date


def compute_days_between_dates(original_date, today_date):
    # Normalize the birthday to be on this year
    # We need only to get the difference between Months and Days
    # without taking into account the Year
    new_original_date = datetime.date(year=today_date.year,
                                      month=original_date.month,
                                      day=original_date.day)

    date_diff = new_original_date - today_date

    print('Date Difference is: {}'.format(date_diff.days))
    return date_diff.days


def print_birthday_info(days):
    if days < 0:
        print('You already have your birthday {} ago'.format(abs(days)))
    elif days > 0:
        print("Your birthday is comming in {}".format(abs(days)))
    else:
        print('Happy Birthday!!!')



def main():
    print_header()
    bday = get_birthday_from_user()
    today = datetime.date.today()
    print('Today Date is : ', today)
    number_of_days = compute_days_between_dates(bday, today)
    print_birthday_info(number_of_days)


main()
