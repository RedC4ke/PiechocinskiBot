import json
import POSifiedText
import resource


if __name__ == '__main__':
    resource.setrlimit(resource.RLIMIT_AS, (40000, 40960))

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
    print(output_text + "\n")
    input('press enter')
