import os


def print_header(app_name):
    print('-' * 30)
    print('{:^30}'.format(app_name))
    print('-' * 30)


def load_csv_file():
    pass


def search_real_estate_data():
    pass


def get_data_file():
    base_folder = os.path.dirname(__file__)
    print(base_folder)


def main():
    print_header('REAL ESTATE APP')

    get_data_file()

    load_csv_file()

    search_real_estate_data()


if __name__ == "__main__":
    main()
