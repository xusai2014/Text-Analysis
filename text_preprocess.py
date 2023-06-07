import jieba
import os
from pdfminer.high_level import extract_text
import re

pdf_folder = 'pdfs'
cut_folder = 'cuts.txt'
pdf_texts =[]

def cut_text(pdf_text, pdf_filename):
    text = re.sub(r'[^\u4e00-\u9fa5]','', pdf_text)
    text = re.sub(r'[\s+]', '', text)
    text = re.sub(r'[\n+]', '', text)
    txt = ' '.join(jieba.cut(text))
    return txt
    
    

for pdf_filename in os.listdir(pdf_folder):
    pdf_path = os.path.join(pdf_folder, pdf_filename)
    pdf_text = extract_text(pdf_path)
    pdf_texts.append(cut_text(pdf_text, pdf_filename))

data_folder = 'data'
os.makedirs(data_folder, exist_ok=True)
with open(data_folder + '/' +cut_folder, 'w') as f:
    f.write(' '.join(pdf_texts))
    