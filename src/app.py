'''
This is an application which sends Slack notification when IMAX ticket sale is available for a movie.
'''
import datetime
import json
import requests
import time
import os

notificationSent = False

def main():
    webhook_url = os.environ['SLACK_WEBHOOK_URL']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0'}
    notification = "{} biletleri satışta!".format(
        os.environ['MOVIE_NAME'])
    slack_data = {'text': notification, 'username': 'moviebot'}

    url = os.environ['MOVIE_URL']
    searchKeyword = "IMAX"

    if("biletix" in url):
        searchKeyword = "Bilet Ara"

    html = requests.get(url, headers=headers).text
    global notificationSent
    if searchKeyword in html and notificationSent == False:
        response = requests.post(webhook_url, data=json.dumps(
            slack_data), headers={'Content-Type': 'application/json'})

        if response.status_code != 200:
            raise ValueError('Request to slack returned an error %s, the response is:\n%s' % (
                response.status_code, response.text))
        else:
            notificationSent = True


if __name__ == "__main__":
    while True:
        print("[INFO] {} requesting web page.".format(datetime.datetime.now()))
        main()
        print("[INFO] {} request completed.".format(datetime.datetime.now()))
        time.sleep(60 * 5)
