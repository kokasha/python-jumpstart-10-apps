import journal


def main():
    print_header('Journal App')
    run_event_loop()


def print_header(app_name):
    print('-' * 30)
    print('{:^30}'.format(app_name))
    print('-' * 30)


def listing_entries(data):
    """

    :param data: this is the jounral data structure / file
    :return: None
    """
    print('Listing All the Data in the Journal....\n')
    data = reversed(data)
    for idx, line in enumerate(data):
        print('[{}] {}'.format(idx + 1, line))


def adding_entries(data):
    """

    :param data: This is the journal data structure / file
    :return: None
    """
    print('Adding a New Entry....')
    text = input('Please enter a new Entry, <enter> to exit: ')
    journal.add_entry(text, data)
    # data.append(text)


def run_event_loop():
    print('**** Journal App is Starting ***')

    journal_name = 'default'
    # Initialize the Data Structure for the Journal
    journal_data = journal.load(journal_name)

    print('What do you want to do with your journal? ')
    cmd = 'EMPTY'

    while cmd != 'x' and cmd:
        cmd = input('[L]ist Entries, [A]dd new Entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            listing_entries(journal_data)
        elif cmd == 'a':
            adding_entries(journal_data)
        elif cmd != 'x' and cmd:
            print("I don't understand the Input '{}'".format(cmd))

    journal.save(journal_name, journal_data)

    print('Goodbye!!')


main()
