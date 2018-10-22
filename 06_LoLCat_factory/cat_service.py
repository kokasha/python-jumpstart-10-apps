import requests
import os

import shutil


def get_cat_from_url(url):
    data = requests.get(url, stream=True)
    # print(data.status_code)
    return data.raw


def save_image(folder, name, data):
    filename = os.path.join(folder, name + '.jpg')
    with open(filename, 'wb') as fout:
        shutil.copyfileobj(data, fout)


def get_cat(folder, name):
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data = get_cat_from_url(url)
    save_image(folder, name, data)
