import json
import POSifiedText
import requests
import schedule
import time
import logging
import os
from dotenv import load_dotenv
from opencensus.ext.azure.log_exporter import AzureLogHandler

load_dotenv()

instrumentation_key = os.environ['INSIGHTS_INSTRUMENTATION_KEY']
fb_token = os.environ['FACEBOOK_ACCESS_TOKEN']
fb_secret = os.environ['FACEBOOK_APP_SECRET']
fb_page_id = 105803968458128
fb_post_url = 'https://graph.facebook.com/{}/feed'.format(fb_page_id)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(AzureLogHandler(
    connection_string=f'InstrumentationKey={instrumentation_key}'
))


def info(text):
    print(text)
    logger.info(text)


def fb_setup():
    user_token_request = requests.get(f"https://graph.facebook.com/v11.0/oauth/access_token?"
                                      "grant_type=fb_exchange_token&"
                                      "client_id=847748026179563&"
                                      f"client_secret={fb_secret}&"
                                      f"fb_exchange_token={fb_token}")

    if user_token_request.status_code != 200:
        info("FACEBOOK: " + user_token_request.text)
        return None

    user_token = user_token_request.json()['access_token']

    user_request = requests.get(f"https://graph.facebook.com/v2.10/me?access_token={user_token}")

    if user_request.status_code != 200:
        info("FACEBOOK: " + user_request.text)
        return None

    user_id = user_request.json()['id']

    page_token_request = requests.get(f"https://graph.facebook.com/v11.0/{user_id}/accounts?"
                                      f"access_token={user_token}")

    if page_token_request.status_code != 200:
        info("FACEBOOK: " + page_token_request.text)
        return None

    info("FACEBOOK: Received long term page access token!")
    page_token = page_token_request.json()['data'][0]['access_token']

    return page_token


def sentence():
    output_text = None
    while output_text is None:
        output_text = model.make_sentence(tries=10, max_overlap_total=70)
    return output_text.replace(" .", ".").replace(" ,", ",").replace(" ;", ";").replace(" …", "") \
        .replace(" ?", "?").replace(" !", "!").replace(" ...", "...").replace("  ", ": ").strip()


def facebook(fb_sentence):
    fb_payload = {
        'message': fb_sentence,
        'access_token': fb_page_token
    }
    fb_request = requests.post(fb_post_url, data=fb_payload)
    info(f"Facebook response: {fb_request.text}")

    return


def job():
    info("Job started!")

    text = sentence()
    info(f"Sentence: {text}")

    facebook(text)

    return


if __name__ == '__main__':
    info("Bot started!")

    model_file = open(f"model.json", "r", encoding="utf-8")
    model = POSifiedText.POSifiedNewlineText.from_json(json.load(model_file))

    fb_page_token = fb_setup()

    schedule.every(45).to(280).minutes.do(job)
    info("Job scheduled!")

    while True:
        schedule.run_pending()
        time.sleep(60)
