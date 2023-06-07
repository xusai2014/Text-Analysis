import requests
import os
from  bs4  import BeautifulSoup

url = "http://101.200.227.21/plan/6103"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

iframes = soup.find_all('iframe')

pdf_urls = []

for iframe in iframes:
    src = iframe.get('src')
    if src and src.find('libs/pdfjs/web/viewer.html?file'):  # 确保URL指向PDF文件
        pdf_urls.append('http://101.200.227.21' + src.replace('/libs/pdfjs/web/viewer.html?file=',''))

print("pdf_urls: ",pdf_urls)

pdf_folder = 'pdfs'
os.makedirs(pdf_folder, exist_ok=True)

for pdf_url in pdf_urls:
    pdf_response = requests.get(pdf_url)
    pdf_filename = os.path.join(pdf_folder, pdf_url.split('/')[-1])
    with open(pdf_filename, 'wb') as f:
        f.write(pdf_response.content)