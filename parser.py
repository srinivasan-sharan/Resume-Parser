from os import name
import docx2txt
import nltk
import re
import subprocess
from pdfminer.high_level import extract_text

PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')
SKILLS_DB = [
    'machine learning',
    'data science',
    'python',
    'word',
    'excel',
    'English',
    'HTML',
    'CSS',
    'mySQL',
    'Python',
    'Java',
    'JavaScript',
    'C',
    'Node',
    'Express',
    'MongoDB'
]


def doc_to_text_catdoc(file_path):
    try:
        process = subprocess.Popen(  
            ['catdoc', '-w', file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )
    except (
        FileNotFoundError,
        ValueError,
        subprocess.TimeoutExpired,
        subprocess.SubprocessError,
    ) as err:
        return (None, str(err))
    else:
        stdout, stderr = process.communicate()

    return (stdout.strip(), stderr.strip())


def extract_text_from_docx(docx_path):
    txt = docx2txt.process(docx_path)
    if txt:
        return txt.replace('/t', ' ')
    return None

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)
    

def extract_names(txt):
    person_names = []

    for sent in nltk.sent_tokenize(txt):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk,'label') and chunk.label() == 'PERSON':
                person_names.append(
                    ' '.join(chunk_leave[0] for chunk_leave in chunk.leaves())
                )
    return person_names

def extract_phone_number(resume_text):
    phone = re.findall(PHONE_REG, resume_text)

    if phone:
        number = ''.join(phone[0])

        if resume_text.find(number) >= 0 and len(number) < 16:
            return number
    return None

def extract_email_id(resume_text):
    return re.findall(EMAIL_REG, resume_text)

def extract_skills(resume_text):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    word_tokens = nltk.tokenize.word_tokenize(resume_text)

    filtered_tokens = [w for w in word_tokens if w not in stop_words] #removing stop words

    filtered_tokens = [w for w in word_tokens if w.isalpha()] #punctuation removal

    bigrams_trigrams = list(map(' '.join, nltk.everygrams(filtered_tokens,2,3))) #making bigrams and trigrams, not entirely sure why or how it works

    found_skills = set() #set for storing the skills found

    for token in filtered_tokens: #searching for each skill/token in skills db
        if token.lower() in SKILLS_DB:
            found_skills.add(token)

    for ngram in bigrams_trigrams: #we search for bigram and trigram in skills db
        if ngram.lower() in SKILLS_DB:
            found_skills.add(ngram)
    
    return found_skills

if __name__ == '__main__':
    text = extract_text_from_docx('cv.docx')
    # text = doc_to_text_catdoc('resumes\MADHUSUDAN KUMAR S (Resume 1).doc')
    # text = extract_text_from_pdf("resumes/ue.pdf")
    names = extract_names(text)
    phone_number = extract_phone_number(text)
    email_id = extract_email_id(text)
    skills = extract_skills(text)

    if names:
        print(names[0])
    
    if phone_number:
        print(phone_number)

    if email_id:
        print(email_id)
    
    if skills:
        print(skills)
