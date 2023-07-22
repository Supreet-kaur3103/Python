import spacy

nlp = spacy.load("en_core_web_sm")
text = """Kiran want to know the famous foods in each state of India. So, he opened Google and search for this question. Google showed that
in Delhi it is Chaat, in Gujarat it is Dal Dhokli, in Tamilnadu it is Pongal, in Andhrapradesh it is Biryani, in Assam it is Papaya Khar,
in Bihar it is Litti Chowkha and so on for all other states"""
locations = []
count = 0
doc = nlp(text)
for ent in doc.ents:
    if ent.label_ == "GPE" and ent.text.lower()!= "pongal":
        locations.append(ent.text)
        count +=1

print("Geographical location Names: ",locations)
print("Count: ",count)
        
