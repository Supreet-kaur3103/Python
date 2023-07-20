#let import necessary libraries and create the object

#for nltk
import nltk
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

#downloading all neccessary packages related to nltk
#nltk.download('all')


#for spacy
import spacy
nlp = spacy.load("en_core_web_sm")

text = """Latha is very multi talented girl.She is good at many skills like dancing, running, singing, playing.She also likes eating Pav Bhagi. she has a 
habit of fishing and swimming too.Besides all this, she is a wonderful at cooking too.
"""

#using stemming in nltk
print("Using stemming in NLTK")


#step1: Word tokenizing

from nltk.tokenize import word_tokenize
nltk_tokens = word_tokenize(text)

all_stemmed_text = []
#step2: getting the base form for each token using stemmer

for word in nltk_tokens:
    stemmed_text =stemmer.stem(word)
    all_stemmed_text.append(stemmed_text)


#step3: joining all words in a list into string using 'join()'#
final_stemmed_text =" ".join(all_stemmed_text)
print(final_stemmed_text)


#using lemmatisation in spacy
print("Using lemmatisation in Spacy")

#step1: Creating the object for the given text
doc = nlp(text)

all_lemma_text = []
#step2: getting the base form for each token using spacy 'lemma_'

for token in doc:
    lemma_text = token.lemma_
    all_lemma_text.append(lemma_text)

#step3: joining all words in a list into string using 'join()'
final_lemma=" ".join(all_lemma_text)
print(final_lemma)