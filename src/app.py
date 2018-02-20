'''
This is an application which sends Slack notification when IMAX cinema
'''
import json
import requests
import time
import os


def main():
    webhook_url = os.environ['SLACK_WEBHOOK_URL']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0'}
    notification = "{} IMAX biletleri satışta!".format(
        os.environ['MOVIE_NAME'])
    slack_data = {'text': notification, 'username': 'moviebot'}

    url = os.environ['MOVIE_URL']
    html = requests.get(url, headers=headers).text

    if "IMAX" in html:
        response = requests.post(webhook_url, data=json.dumps(
            slack_data), headers={'Content-Type': 'application/json'})

        if response.status_code != 200:
            raise ValueError('Request to slack returned an error %s, the response is:\n%s' % (
                response.status_code, response.text))


if __name__ == "__main__":
    while True:
        print("Started!")
        main()
        print("Finished!")
        time.sleep(60 * 5)
