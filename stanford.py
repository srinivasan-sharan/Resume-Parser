from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import nltk
import os
import pandas as pd
from pdfminer.high_level import extract_text

model = 'C:\stanford_modals\stanford-ner-2020-11-17\classifiers/english.all.3class.distsim.crf.ser.gz'

jar = 'C:\stanford_modals\stanford-ner-2020-11-17\stanford-ner.jar'

st = StanfordNERTagger(model, jar,encoding = 'utf-8')

text = extract_text("resumes\Gaurav_Tikku.pdf")

print(text)


# tokenized_text = nltk.word_tokenize(text)
# classified_text = st.tag(tokenized_text)

# classified_text_df = pd.DataFrame(classified_text)

# classified_text_df.drop_duplicates(keep='first', inplace=True)
# classified_text_df.reset_index(drop=True, inplace=True)
# classified_text_df.columns = ["Entities", "Labels"]
# print(classified_text_df)

# tokenized_text = nltk.word_tokenize(text)
# classified_text = st.tag(tokenized_text)

# netagged_words = classified_text

# entities = []
# labels = []

# from itertools import groupby
# for tag, chunk in groupby(classified_text, lambda x:x[1]):
#     if tag != "O":
#         entities.append(' '.join(w for w, t in chunk))
#         labels.append(tag)
        
        
# entities_all = list(zip(entities, labels))
# entities_unique = list(set(zip(entities, labels))) #unique entities   
# entities_df = pd.DataFrame(entities_unique)
# entities_df.columns = ["Entities", "Labels"]
# print(entities_df)