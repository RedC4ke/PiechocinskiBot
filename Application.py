import POSifiedText
import markovify

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open("sources.txt", "r", encoding="utf-8") as f:
        unparsed_text = f.readlines()
        text = ""
        for line in unparsed_text:
            text += line

    text_model = POSifiedText.POSifiedNewlineText(text, state_size=2, well_formed=True)
    sentences = []
    for i in range(20):
        sentence = text_model.make_sentence(tries=15, max_overlap_total=60).replace(" ,", ",").replace(" .", ".")
        if sentence is not None and sentence not in sentences:
            print(sentence)
        sentences.append(sentence)
