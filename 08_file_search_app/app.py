import os
from pprint import pprint


def print_header(app_name):
    print('-' * 30)
    print('{:^30}'.format(app_name))
    print('-' * 30)


def search_file(full_file_path, text):
    matches = []
    with open(full_file_path, mode='r', encoding='utf-8') as fin:
        # print(full_file_path)
        for line in fin:
            if line.find(text) >= 0:
                matches.append(line)
        return matches


def search_folders(search_directory, text):
    print('Searching {} for {}'.format(search_directory, text))

    all_files = os.listdir(search_directory)

    all_matches = []

    for file in all_files:
        full_file_path = os.path.join(search_directory, file)
        print(full_file_path)
        if '.DS_Store' in full_file_path:
            continue

        if os.path.isdir(full_file_path):
            search_folders(full_file_path, text)

        matches = search_file(full_file_path, text)
        print('Found {} in File {}'.format(len(matches),full_file_path))
        all_matches.extend(matches)

    return all_matches


def get_folder_from_user():
    folder = input('Please Input Search Directory: ')
    if not folder.strip():
        return None
    if not os.path.isdir(folder):
        return 'No Directory with this Name'

    return os.path.abspath(folder)


def get_text_from_user():
    text = input('Please Enter the word to search for: ')

    if not text:
        return None

    return text.strip()


def main():
    print_header('File Search APP')

    # Get Input from User regarding Folder to Search
    search_folder = get_folder_from_user()

    # Get Text to search for all on all the files
    text = get_text_from_user()

    all_matches = search_folders(search_folder, text)

    print()
    print('Total Matches for text {} is {}'.format(text, len(all_matches)))


if __name__ == "__main__":
    main()
