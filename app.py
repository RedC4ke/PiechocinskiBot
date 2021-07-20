import json
import POSifiedText
import requests
import logging
import os
from opencensus.ext.azure.log_exporter import AzureLogHandler

instrumentation_key = os.environ['INSIGHTS_INSTRUMENTATION_KEY']
fb_token = os.environ['FACEBOOK_ACCESS_TOKEN']
fb_page_id = 105803968458128
fb_post_url = 'https://graph.facebook.com/{}/feed'.format(fb_page_id)

logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(
    connection_string=f'InstrumentationKey=${instrumentation_key}'
))


if __name__ == '__main__':
    logger.info("Bot started!")

    model_file = open("model.json", "r", encoding="utf-8")
    model = POSifiedText.POSifiedNewlineText.from_json(json.load(model_file))

    sentences = []
    output_text = ""
    for i in range(1):
        sentence = model.make_sentence(tries=10, max_overlap_total=70)
        if sentence not in sentences:
            output_text += "\n" + sentence
        sentences.append(sentence)
    output_text = output_text.replace(" .", ".").replace(" ,", ",").replace(" ;", ";").replace(" …", "")\
        .replace(" ?", "?").replace(" !", "!").replace(" ...", "...").replace("  ", ": ")

    logger.warning(output_text)

    fb_payload = {
        'message': output_text,
        'access_token': fb_token
    }
    fb_request = requests.post(fb_post_url, data=fb_payload)
    logger.warning(fb_request.text)
