import argparse
import os

import requests
from dotenv import load_dotenv
from urllib.parse import urlparse
from requests.exceptions import HTTPError


API_URL = "https://api-ssl.bitly.com/v4/"


def shorten_url(bitly_token, url):
    bit_url = "{}shorten".format(API_URL)
    params = {"long_url": url}
    headers = {"Authorization": "Bearer {}".format(bitly_token)}
    response = requests.post(bit_url, json=params, headers=headers)
    response.raise_for_status()
    return response.json()["link"]


def count_clicks(bitly_token, link):
    bit_url = "{0}bitlinks/{1}/clicks/summary".format(API_URL, link)
    params = {"unit": "day", "units": "-1"}
    headers = {"Authorization": "Bearer {}".format(bitly_token)}
    response = requests.get(bit_url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(bitly_token, url):
    bit_url = "{0}bitlinks/{1}".format(API_URL, url)
    headers = {"Authorization": "Bearer {}".format(bitly_token)}
    response = requests.get(bit_url, headers=headers)
    return response.ok


def main():
    bitly_token = os.getenv('BITLINK_TOKEN')
    parser = argparse.ArgumentParser(
        description="Программа позволяет сократить ссылку\
                    или получить количество кликов по уже сокращенной\
                    для этого при вызове скрипта нужно передать аргументом\
                    --url ссылку, с которой нужно произвести операцию ")
    parser.add_argument('--url', help='Введите ссылку')
    args = parser.parse_args()
    parsed_url = urlparse(args.url)
    if parsed_url.scheme:
        url_with_protocol = args.url
    else:
        url_with_protocol = f"http://{args.url}"
    url_without_protocol = f"{parsed_url.netloc}{parsed_url.path}"

    if is_bitlink(bitly_token, url_without_protocol):
        try:
            print(count_clicks(url_without_protocol, bitly_token))
        except:
            print("Ошибка при подсчете кликов")
    else:
        try:
            print(shorten_url(bitly_token, url_with_protocol))
        except HTTPError:
            print("Неправильная ссылка: ", args.url)


if __name__ == "__main__":
    load_dotenv()
    main()
