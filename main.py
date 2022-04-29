import argparse
import os

import requests
from dotenv import load_dotenv
from urllib.parse import urlparse

from requests.exceptions import HTTPError


def shorten_url(bitly_token, url):
    bit_url = "https://api-ssl.bitly.com/v4/shorten"
    params = {"long_url": url}
    headers = {"Authorization": "Bearer {}".format(bitly_token)}
    response = requests.post(bit_url, json=params, headers=headers)
    response.raise_for_status()
    return response.json()["link"]


def count_clicks(bitly_token, link):
    bit_url = "https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary" \
                                                        .format(link)
    params = {"unit": "day", "units": "-1"}
    headers = {"Authorization": "Bearer {}".format(bitly_token)}
    response = requests.get(bit_url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(bitly_token, url):
    bit_url = "https://api-ssl.bitly.com/v4/bitlinks/{}".format(url)
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

    if is_bitlink(authorization, netloc_with_path):
        try:
            print(count_clicks(netloc_with_path, authorization))
        except:
            print("Ошибка при подсчете кликов")
    else:
        try:
            print(shorten_link(authorization, user_url))
        except:
            print("Ошибка при сокращении ссылки")


if __name__ == "__main__":
    load_dotenv()
    main()
