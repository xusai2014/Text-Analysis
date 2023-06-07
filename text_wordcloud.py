from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import matplotlib.pyplot as plt

def wordImage():
    infile = open('./data/baidu_stopwords.txt', encoding= 'utf-8')
    stopwords_list = infile.readlines()
    STOPWORDS = [x.strip() for x in stopwords_list]
    stopwords  = set(STOPWORDS)
    
    txt_file = open('./data/cuts.txt', encoding='utf-8')
    texts = ' '.join(txt_file.readlines())
    wc = WordCloud('./rg.ttf', width=800,height=800, background_color='white',stopwords=stopwords).generate(texts)

    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()

wordImage()