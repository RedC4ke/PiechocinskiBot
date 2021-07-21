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


def sentence():
    output_text = None
    while output_text is None:
        output_text = model.make_sentence(tries=10, max_overlap_total=70)
    return output_text.replace(" .", ".").replace(" ,", ",").replace(" ;", ";").replace(" …", "") \
        .replace(" ?", "?").replace(" !", "!").replace(" ...", "...").replace("  ", ": ").strip()


def facebook(fb_sentence):
    fb_payload = {
       'message': fb_sentence,
       'access_token': fb_token
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

    schedule.every(75).to(180).minutes.do(job, model)
    info("Job scheduled!")

    while True:
        schedule.run_pending()
        time.sleep(60)
