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


#using stemming in nltk
print("Stemming using NLTK")
lst_words = ['running', 'painting', 'walking', 'dressing', 'likely', 'children', 'whom', 'good', 'ate', 'fishing']

for word in lst_words:
    print(word,"|", stemmer.stem(word))
    
    
print("*"*40)

#using lemmatization in spacy
print("Lematization using SpaCy")
doc = nlp("running painting walking dressing likely children whom good ate fishing")
for token in doc:
    print(token.text,"|", token.lemma_,"|",token.lemma)
