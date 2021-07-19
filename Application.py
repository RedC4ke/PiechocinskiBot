import POSifiedText

if __name__ == '__main__':
    with open("piecho1.txt", "r", encoding="utf-8") as f:
        text = f.readlines()

    text_model = POSifiedText.POSifiedNewlineText(text, state_size=2, well_formed=True)
    sentences = []
    output_text = ""
    for i in range(50):
        sentence = text_model.make_sentence(tries=15, max_overlap_total=70)
        if sentence not in sentences:
            output_text += "\n" + sentence
        sentences.append(sentence)
    output_text = output_text.replace(" .", ".").replace(" ,", ",")\
        .replace(" ;", ";").replace(" …", "").replace(" ?", "?").replace(" !", "!").replace(" ...", "...")
    print(output_text)
