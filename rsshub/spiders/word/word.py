import re
import csv
import random 
import requests
import linecache
from os import path
import requests
from rsshub.utils import DEFAULT_HEADERS


file_path = path.dirname(path.realpath(__file__))

def get_csv_line(url):
    response = requests.get(url)
    lines = response.text.splitlines()
    reader = csv.reader(lines)
    data = list(reader)
    data = data[1:]
    random_line = random.choice(data)
    return random_line

def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def ctx(category=''):
    word = ''
    word_original = ''
    if category == 'ja':
        url = 'https://raw.githubusercontent.com/henrylovemiller/img/main/words.csv'
        res = get_csv_line(url)
        word = f"{res[1]} 〔{res[2]} {res[4]}〕 {res[3]} "
        word_original = f"{res[1]}"
    elif category == 'jlpt3':
        url = 'https://raw.githubusercontent.com/henrylovemiller/img/main/hongbaoshu_N3.csv'
        res = get_csv_line(url)
        word = f"{res[0]}〔{res[1]} {res[2]}〕 ➡{res[3]}   ➡{res[4]}   ➡ {res[5]}  ➡ {res[6]} "
        word = remove_html_tags(word)
        word_original = remove_html_tags(res[0])
    elif category == 'jlpt2':
        url = 'https://raw.githubusercontent.com/HenryLoveMiller/ja/main/N2_hongbaoshu.csv'
        res = get_csv_line(url)
        word = f"{res[0]}〔{res[1]} {res[2]}〕 ➡{res[3]}   ➡{res[4]}   ➡ {res[5]}  ➡ {res[6]} "
        word = remove_html_tags(word)  
        word_original = remove_html_tags(res[0])      
    else:
        category = 'toefl'
        file = path.join(file_path,'toeflwords.txt')
        with open(file, encoding='utf-8') as inf:
            f = inf.readlines()
            count = len(f)
            wordnum = random.randrange(0, count, 1)
            word = linecache.getline(file, wordnum)
            word_original = word.split(',')[0] 
    return {"word": word, 
            "word_original": word_original, 
            "category": category
            }
