import spacy

text_1 = 'Linkedin is the best place to expand one’s network.'

# Tokenizing text without using complete NLP pipeline. Thus, printing each token's corresponding text

nlp = spacy.load('en_core_web_sm')

doc = nlp.make_doc(text_1)  # Tokenizing the text

# Printing token texts
print([token.text for token in doc])

text_2 = 'Linkedin is the best place to expand one’s network.'

# Printing the entities from the final doc

# Disable the tagger and parser
with nlp.disable_pipes('tagger', 'parser'):
    doc = nlp(text_2)  # Processing the text

    print(doc.ents)  # Printing the entities
