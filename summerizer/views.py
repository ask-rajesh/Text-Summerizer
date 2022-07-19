from django.shortcuts import render, HttpResponse

#--------------------------Code for Text Summerization----------------------------

import re # relugar expression
import nltk # natural language toolkit
import string
import heapq
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

def preprocess(text):
  formatted_text = text.lower()
  stopwords = nltk.corpus.stopwords.words('english')
  tokens = []
  for token in nltk.word_tokenize(formatted_text):
    tokens.append(token)
  #print(tokens)
  tokens = [word for word in tokens if word not in stopwords and word not in string.punctuation]
  formatted_text = ' '.join(element for element in tokens)

  return formatted_text


def summary(para, n):
    original_text = para
    original_text = re.sub(r'\s+', ' ', original_text)
    
    formatted_text = preprocess(original_text)
    word_frequency = nltk.FreqDist(nltk.word_tokenize(formatted_text))
    word_frequency.keys()
    highest_frequency = max(word_frequency.values())
    for word in word_frequency.keys():
        word_frequency[word] = (word_frequency[word] / highest_frequency)
    sentence_list = nltk.sent_tokenize(original_text)

    score_sentences = {}
    for sentence in sentence_list:
        for word in nltk.word_tokenize(sentence.lower()):
            if sentence not in score_sentences.keys():
                score_sentences[sentence] = word_frequency[word]
            else:
                score_sentences[sentence] += word_frequency[word]

    
    best_sentences = heapq.nlargest(n, score_sentences, key = score_sentences.get)  

    summary_ans = ' '.join(best_sentences)
    return summary_ans

def main(para):
    number_of_sentences = sent_tokenize(para)
    if len(number_of_sentences) < 10:
        return "Input is too short for summary. Input atleast 10 sentance."

    line = len(number_of_sentences)
    summary_line =  line / 2
    summary_ans = summary(para, int(summary_line))
    return summary_ans
#-----------------------------------------------Views---------------------------------

def summerize(request):
    return render(request, 'summerize.html')

def about(request):
    return render(request, 'About.html')

def paragraph(request):
    data = request.GET["para"]
    data2 = main(data)
    return render(request, 'Text_summary.html', {'data2' : data2})