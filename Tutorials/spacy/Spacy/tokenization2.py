import spacy

nlp = spacy.blank("en")
nlp.add_pipe('sentencizer')
text = "Tony gave two $ to Peter, Bruce gave 500 € to Steve"
doc = nlp(text)
amount = []
for sentence in doc.sents:
    for token in sentence:
        if token.like_num and doc[token.i+1].is_currency:
            print(token.text, doc[token.i+1].text)  