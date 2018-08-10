import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')
doc = open("act.txt").read()
doc_file = nlp(doc)

for word in doc_file:
    print(word.text, word.pos_)

ex1 = nlp("Sally likes Sam")
displacy.render(ex1,style='dep', jupyter=True)



