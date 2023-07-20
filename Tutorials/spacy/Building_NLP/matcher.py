import spacy
# import and initialize the matcher object
from spacy.matcher import Matcher
nlp = spacy.load('en_core_web_md')
matcher = Matcher(nlp.vocab)

#describe patterns and ingests into the matcher
pattern = [{"LOWER": "golden"}, {"LOWER": "retriever"}]
matcher.add('DOG', [pattern])

#call catcher on doc object
doc = nlp("I have a Golden Retriever")

#Running for loop over the results of matching
for match_id, starting, ending in matcher(doc):
    span = doc[starting:ending]
    print('Matched Span:', span.text)
    print('Root Token:', span.root.text)
    print('Root Head Token:', span.root.head.text)
    print('Previous Token:', doc[starting-1].text, doc[starting-1].pos_)
