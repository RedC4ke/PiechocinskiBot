import POSifiedText
import json


if __name__ == '__main__':
    with open("sources.txt", "r", encoding="utf-8") as f:
        text = f.readlines()

    text_model = POSifiedText.POSifiedNewlineText(text, state_size=2, well_formed=True)
    output_file = open("model.json", "w", encoding="utf-8")
    json.dump(text_model.to_json(), output_file, ensure_ascii=False, indent=4)
