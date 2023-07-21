import spacy

nlp = spacy.load("en_core_web_sm")
with open("D:\Job\Python\Github\Python\Tutorials\spacy\Spacy/news_story.txt","r") as f:
    news_text = f.read()
noun = []
number = []
doc = nlp(news_text)
for token in doc:
    if token.pos_ == "NOUN":
        noun.append(token)
print("Nouns = ",noun)
for token in doc:
    if token.pos_ == "NUM":
        number.append(token)
print("Numbers =" ,number)
count = doc.count_by(spacy.attrs.POS)
for k,v in count.items():
    print(doc.vocab[k].text, "|",v)