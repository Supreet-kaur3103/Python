#write in cmd line python -m spacy download en_core_web_md
import spacy
nlp = spacy.load('en_core_web_md')
doc = nlp("I have two cars")
#Accessing vector using toke.vector property
print(doc[3].vector)