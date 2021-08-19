import app
import POSifiedText
import json

if __name__ == '__main__':
    model_file = open(f"model.json", "r", encoding="utf-8")
    model = POSifiedText.POSifiedText.from_json(json.load(model_file))

    for i in range(20):
        output_text = model.make_sentence(tries=35, max_overlap_total=60)
        if output_text is not None:
            print(output_text.replace(" .", ".").replace(" ,", ",").replace(" ;", ";").replace(" …", "") \
                .replace(" ?", "?").replace(" !", "!").replace(" ...", "...").replace("  ", ": ").strip())
