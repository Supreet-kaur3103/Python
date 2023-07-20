# Importing Phrase Matcher & initialise it.
import spacy
from spacy.matcher import PhraseMatcher
nlp = spacy.load('en_core_web_md')
matcher = PhraseMatcher(nlp.vocab)

# Creating pattern doc objects
COUNTRIES = [ "United Kingdom", "India", "United States of America" ]
doc=nlp("I basically belong to India but I like to travel a lot so I have visited United States of America, and I currently I am living in United Kingdom to pursue my masters")

patterns = list(nlp.pipe(COUNTRIES))

matcher.add('COUNTRY', None, *patterns) # Adding to matcher

# Calling the matcher on the doc & printing the result.

matches = matcher(doc)

print([doc[start:end] for match_id, start, end in matches])