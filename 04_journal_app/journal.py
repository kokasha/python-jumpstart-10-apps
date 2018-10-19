import os


def load(name):
    # load the data structure which will hold our journal data
    data = []

    filename = get_fullpathname(name)
    print(filename)
    print(os.path.exists(filename))

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                #print('would load entry: {}'.format(entry.rstrip()))
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    """

    :param name: Name of the journal
    :param journal_data: the data structure / file for storing the data
    :return:
    """
    filename = get_fullpathname(name)
    # filename = './journals/' + name + '.jrl'
    print('.... Saving to file {}:'.format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_fullpathname(name):
    return os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))


def add_entry(text, journal_data):
    journal_data.append(text)
