import spacy

nlp = spacy.load('en_core_web_sm')
doc = open("act.txt").read()
doc_file = nlp(doc)

#for num,sentence in enumerate(doc_file.sents):
    #main_doc = f'{num}: {sentence}'

main_doc=[]

for sentence in doc_file.sents:
    main_doc.append(sentence)
    #print(main_doc)


for s in main_doc:
        print(s)

t=[]
for s in main_doc:
    for token in s:
        t.append(token)

print(t)