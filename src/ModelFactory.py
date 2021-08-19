import POSifiedText
import json
import re


if __name__ == '__main__':
    with open("bosack.txt", "r", encoding="utf-8") as f:
        pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        text = pattern.sub('', f.read()).replace('.\n', '\n').replace('\n', '. ').replace('?.', '?').replace('!.', '!')\
            .replace(' .', '.').replace(' ,', ',')
        print(text)

    text_model = POSifiedText.POSifiedText(text, state_size=3, well_formed=True)
    output_file = open("model.json", "w", encoding="utf-8")
    json.dump(text_model.to_json(), output_file, ensure_ascii=False, indent=4)
