import bs4 as bs4
import requests
import bs4
import collections

WeatherReport = collections.namedtuple('report', 'loc,cond,temp,scale')


def main():
    print_header('Weather APP')
    zipcode = ask_user_zipcode()

    # here we get the raw text format HTML data
    html = get_weather_data_from_web(zipcode)

    report = parse_html_data(html)
    print(type(report))
    print(report.cond, report.loc, report.temp, report.scale)


def print_header(app_name):
    print('-' * 30)
    print('{:^30}'.format(app_name))
    print('-' * 30)


def ask_user_zipcode():
    zipcode = input('Please enter the Zipcode for the city (01012): ')
    return zipcode.strip()


def get_weather_data_from_web(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    print('status Code is: ', response.status_code)

    return response.text


def cleanup_text(text: str):
    return text.strip()


def parse_html_data(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    # Here we are searching for a CSS Class that is why we use class_
    # After we get this class we search for h1 tag
    # then we extract the text from this tag
    # city == $('.region-content-header h1')

    city = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='conditions-extra').find(class_='condition-icon').get_text()
    temp = soup.find(class_='current-temp').find(class_='wu-value').get_text()
    scale = soup.find(class_='current-temp').find(class_='wu-label').get_text()

    city = cleanup_text(city)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)
    # print('city is: ', city)
    # print(condition, city, temp, scale)
    # return condition, city, temp, scale
    report = WeatherReport(cond=condition, loc=city, temp=temp, scale=scale)
    return report


if __name__ == "__main__":
    main()
