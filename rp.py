import spacy
from spacy.matcher import Matcher
import docx2txt

nlp = spacy.load('en_core_web_sm')

matcher = Matcher(nlp.vocab)

def extract_name(resume_text):
    nlp_text = nlp(resume_text)

    pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]

    matcher.add("NAME",*pattern)

    matches = matcher(nlp_text)

    for match_id, start, end in matches:
        span = nlp_text[start:end]
        return span.text 
    
def extract_text_from_docx(docx_path):
    txt = docx2txt.process(docx_path)
    if txt:
        return txt.replace('/t', ' ')
    return None

if __name__ == '__main__':
    text = extract_text_from_docx('cv.docx')
    names = extract_name(text)
