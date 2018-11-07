'''
This is an application which sends Slack notification when IMAX ticket sale is available for a movie.
'''
import datetime
import json
import requests
import time
import os
from bs4 import BeautifulSoup

currentSignal = ''

def main():
    webhook_url = 'https://hooks.slack.com/services/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'#os.environ['SLACK_WEBHOOK_URL']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0'}    

    url = 'https://www.turkishbulls.com/SignalPage.aspx?lang=tr&Ticker=TKFEN'#os.environ['URL']
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, "html.parser")
    lastSignal = soup.find('span',{'id':'MainContent_LastSignal'}).text
    global currentSignal
    if lastSignal != currentSignal:
        notification = "{stock} {signal} sinyali verdi.".format(
        stock = 'TKFEN', signal= lastSignal.lower())
        slack_data = {'text': notification, 'username': 'turkishbulls'}
        response = requests.post(webhook_url, data=json.dumps(
            slack_data), headers={'Content-Type': 'application/json'})
        currentSignal = lastSignal

        if response.status_code != 200:
            raise ValueError('Request to slack returned an error %s, the response is:\n%s' % (
                response.status_code, response.text))


if __name__ == "__main__":
    while True:
        print("[INFO] {} requesting web page.".format(datetime.datetime.now()))
        main()
        print("[INFO] {} request completed.".format(datetime.datetime.now()))
        time.sleep(60 * 5)