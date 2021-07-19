import json
import POSifiedText


if __name__ == '__main__':
    model_file = open("model.json", "r", encoding="utf-8")
    model = POSifiedText.POSifiedNewlineText.from_json(json.load(model_file))

    sentences = []
    output_text = ""
    for i in range(1):
        sentence = model.make_sentence()
        if sentence not in sentences:
            output_text += "\n" + sentence
        sentences.append(sentence)
    output_text = output_text.replace(" .", ".").replace(" ,", ",")\
        .replace(" ;", ";").replace(" …", "").replace(" ?", "?").replace(" !", "!").replace(" ...", "...")
    print(output_text)
