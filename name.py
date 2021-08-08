import nltk
import pandas as pd
from pdfminer.high_level import extract_text



text = extract_text("resumes\RUPALI'S RESUME .pdf")

words  = nltk.sent_tokenize(text)

pos_tags = nltk.pos_tag(words)

chunks = nltk.ne_chunk(pos_tags, binary = False)

entities = []
labels = []

# for chunk in chunks:
#     if hasattr(chunk, 'label'):
#         entities.append(' '.join(c[0] for c in chunk))
#         labels.append(chunk.label())


sentence = nltk.sent_tokenize(text)
for sent in sentence:
    for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent)), binary=False):
        if hasattr(chunk, 'label'):
            entities.append(' '.join(c[0] for c in chunk))
            labels.append(chunk.label())

entities_labels = list(set(zip(entities,labels)))
entities_df = pd.DataFrame(entities_labels)
entities_df.columns = ["Entities","Labels"]

print(entities_df)