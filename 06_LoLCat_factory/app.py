import os
import cat_service


def main():
    print_header('LoLCat Factory')
    folder = get_or_create_folder()
    print('Found and Created Folder {}'.format(folder))
    # download cats
    download_cat(folder)
    # show cats


def print_header(app_name):
    print('-' * 30)
    print('{:^30}'.format(app_name))
    print('-' * 30)


def get_or_create_folder():
    # This return the full path of the application
    folder = 'cat_pictures'

    # print('__file__ var: ',__file__)

    base_folder = os.path.dirname(__file__)
    # print('base folder: ', base_folder)

    full_path = os.path.join(base_folder, folder)
    # print(full_path)

    # create the folder if it doesn't exist
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating the Directory.......')
        os.mkdir(full_path)

    return full_path


def download_cat(folder):
    cat_count = 8
    print('Getting Cats...')
    for i in range(1, cat_count+1):
        name = 'lolcat_{}'.format(i)
        print('downloading {}'.format(name))
        cat_service.get_cat(folder, name)

    print('Done.')


if __name__ == '__main__':
    main()
