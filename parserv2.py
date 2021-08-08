import spacy
import sys, fitz

fname = "resumes\Dasmanisha.pdf"
doc = fitz.open(fname)
text = ""

for page in doc:
    text = text + str(page.getText())

tx = " ".join(text.split('\n'))

nlp_model = spacy.load('nlp_model')

doc = nlp_model(tx)
for ent in doc.ents:
    print(f'{ent.label_.upper():{30}}- {ent.text}')