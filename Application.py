import json
import POSifiedText
import requests
import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler

logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(
    connection_string='InstrumentationKey=c9e3e1b7-19f7-4f8e-a054-0325aee617c7'
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
