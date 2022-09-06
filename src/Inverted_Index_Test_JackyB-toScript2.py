import numpy as np
import pandas as pd
from collections import Counter
import os
import re
import nltk
import time
os.path
from collections import defaultdict 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# for cleaning propose - contracting mapping
# from https://gist.github.com/nealrs/96342d8231b75cf4bb82

contraction_mapping = {
  "ain't": "am not",
  "aren't": "are not",
  "can't": "cannot",
  "can't've": "cannot have",
  "'cause": "because",
  "could've": "could have",
  "couldn't": "could not",
  "couldn't've": "could not have",
  "didn't": "did not",
  "doesn't": "does not",
  "don't": "do not",
  "hadn't": "had not",
  "hadn't've": "had not have",
  "hasn't": "has not",
  "haven't": "have not",
  "he'd": "he would",
  "he'd've": "he would have",
  "he'll": "he will",
  "he'll've": "he will have",
  "he's": "he is",
  "how'd": "how did",
  "how'd'y": "how do you",
  "how'll": "how will",
  "how's": "how is",
  "I'd": "I would",
  "I'd've": "I would have",
  "I'll": "I will",
  "I'll've": "I will have",
  "I'm": "I am",
  "I've": "I have",
  "isn't": "is not",
  "it'd": "it had",
  "it'd've": "it would have",
  "it'll": "it will",
  "it'll've": "it will have",
  "it's": "it is",
  "let's": "let us",
  "ma'am": "madam",
  "mayn't": "may not",
  "might've": "might have",
  "mightn't": "might not",
  "mightn't've": "might not have",
  "must've": "must have",
  "mustn't": "must not",
  "mustn't've": "must not have",
  "needn't": "need not",
  "needn't've": "need not have",
  "o'clock": "of the clock",
  "oughtn't": "ought not",
  "oughtn't've": "ought not have",
  "shan't": "shall not",
  "sha'n't": "shall not",
  "shan't've": "shall not have",
  "she'd": "she would",
  "she'd've": "she would have",
  "she'll": "she will",
  "she'll've": "she will have",
  "she's": "she is",
  "should've": "should have",
  "shouldn't": "should not",
  "shouldn't've": "should not have",
  "so've": "so have",
  "so's": "so is",
  "that'd": "that would",
  "that'd've": "that would have",
  "that's": "that is",
  "there'd": "there had",
  "there'd've": "there would have",
  "there's": "there is",
  "they'd": "they would",
  "they'd've": "they would have",
  "they'll": "they will",
  "they'll've": "they will have",
  "they're": "they are",
  "they've": "they have",
  "to've": "to have",
  "wasn't": "was not",
  "we'd": "we had",
  "we'd've": "we would have",
  "we'll": "we will",
  "we'll've": "we will have",
  "we're": "we are",
  "we've": "we have",
  "weren't": "were not",
  "what'll": "what will",
  "what'll've": "what will have",
  "what're": "what are",
  "what's": "what is",
  "what've": "what have",
  "when's": "when is",
  "when've": "when have",
  "where'd": "where did",
  "where's": "where is",
  "where've": "where have",
  "who'll": "who will",
  "who'll've": "who will have",
  "who's": "who is",
  "who've": "who have",
  "why's": "why is",
  "why've": "why have",
  "will've": "will have",
  "won't": "will not",
  "won't've": "will not have",
  "would've": "would have",
  "wouldn't": "would not",
  "wouldn't've": "would not have",
  "y'all": "you all",
  "y'alls": "you alls",
  "y'all'd": "you all would",
  "y'all'd've": "you all would have",
  "y'all're": "you all are",
  "y'all've": "you all have",
  "you'd": "you had",
  "you'd've": "you would have",
  "you'll": "you you will",
  "you'll've": "you you will have",
  "you're": "you are",
  "you've": "you have"
}

def gettingpath():
    '''
    Prepare the script to ask the client the path to be anlyzed
    
    '''

    files_path = input('Write the path where are located the files to scan begining by a /: ')
    return files_path


def gettingquery():
    '''
    Asking the client if want to search any specific words
    
    '''
    listwordsc = input('Write the list of words to be scanned serarated by a space: ')
    querie = list(listwordsc.split(" "))
    return querie


def list_docs(path):
    '''
    
    Getting the name of the documents in a list
    
    '''
    all_docs = [f for f in os.listdir(path) if not f.startswith('.')] 
    all_docs.sort()
    return all_docs


def cleaning_txt(texto): 
    '''
    cleaning up the text to get the tokens
    
    '''
    
    str_txt = []
    ntxt = []
    
    ## converting txt to string
    str_txt = ''.join(texto)
    
    #print("\n")
    #print('============ text in the file as string. =====================')
    #print(str_txt)

    # removing contractions
    ntxt = str_txt.lower()
    ntxt = ' '.join([contraction_mapping[t] if t in contraction_mapping\
           else t for t in ntxt.split(" ")])

    # removing spaecial character
    ntxt = re.sub(r'\([^)]*\)', '', ntxt)
    ntxt = re.sub('"','', ntxt)
    ntxt = re.sub(r"'s\b","",ntxt)
    ntxt = re.sub("[^a-zA-Z]", " ", ntxt)
    
    #print("\n")
    #print('============ clean text not special characters. =====================')
    #print(ntxt)
    
    return ntxt


def tokens_alldocs(texto):
    '''
    getting the main tokens from all the documents and 
    getting the main tokens input for the final dictionary
    
    '''
    
    text_tokens = []
    no_sw_tokens_d = []
    clean_tokens_d = []
    words_d = []

    # ## removing stopwords
    text_tokens = word_tokenize(texto)
    no_sw_tokens_d = [word for word in text_tokens if not word in stopwords.words("english")]
    
    #print("\n")
    #print('============ no_sw_tokens_d =====================')
    #print(no_sw_tokens_d)
    
    # Identify unique terms in the corpus
    for t in no_sw_tokens_d:    
        if t not in clean_tokens_d:
            clean_tokens_d.append(t)
            
    #print("\n")
    #print('============ tokens. =====================')
    #print(clean_tokens_d)

        
    for t in clean_tokens_d:
        if t not in words_d:
            words_d.append(t)
    words_d.sort()
    #print("\n")
    #print('============ main clean tokens. =====================')
    #print(words_d)
    
    return words_d

def all_together(texto):
    '''
    Cleaning text
    
    '''

    words = cleaning_txt(texto)
    words = tokens_alldocs(words)
    return words


def matchlist(List1, List2):
    '''
    matching the list of words in each doc and the main_words
    
    '''

    List3 = []
    for i in range(len(List1)):
        w = List1[i]
        for j in range(len(List2)):
            if List1[i] == List2[j]:
                List3.append(w)
                break             
    return List3


def sortdictkey(diccionario):
    '''
    Sorted the dictionary
    
    '''

    dic_items = diccionario.items()
    inv_dic = sorted(dic_items)
    return inv_dic


def gettingthedictionary(path):
    '''
    Prepare the script to ask the client the path to be anlyzed
    
    '''

        
    global diccionario
    global main_words
    global main_words_bydoc
    global txt
    global dinv_idx

    diccionario = {}
    main_words = []
    txt = []
    textobydoc = []
       
    all_docs = list_docs(path)
    #print("\n")
    #print(all_docs)
    
    for f in all_docs:
        #print(f)
        #print(files_path+'/'+f)
        document = open(path+'/'+f, 'r', encoding='cp1252')
        txt.append(document.read().replace(r'\r', '').replace(r'\n', ''))
        #print("\n")
        #print('============ text in the file. =====================')
        #print(txt)


    ## getting the main words for all the documents in the path
    main_words = all_together(txt)
    #print("\n")
    #print(main_words)

    ## getting a dictionary with enumerted values
    wdict = {key: idx for idx, key in enumerate(main_words)}
    #print("\n")
    #print(wdict) 


    ## creating the dictionary where the key is the word idex and the value the documents where is located
    for d in all_docs:
        document_r = open(path+'/'+d, 'r', encoding='cp1252')
        textobydoc.append(document_r.read().replace(r'\r', '').replace(r'\n', ''))
        words_bydoc = all_together(textobydoc)
        main_words_bydoc = matchlist(main_words, words_bydoc)
        #print("\n")
        #print(main_words_bydoc)
        
        main_words_bydoc.sort()
        #print("\n")
        #print(main_words_bydoc)
        
        for w in main_words_bydoc:
            if w not in diccionario.keys():
                diccionario[w] = [d]
            else:
                diccionario[w]+=[d]
                
    #sorting the dictionary by key:word    
    inv_dict = sortdictkey(diccionario)
        
    
    #remplacing the key:word by key:index in a new dictionary
    dinv_idx = defaultdict(list)   
    for k1, v1 in wdict.items():
        for k2, v2 in diccionario.items():
            if k1 == k2:
                dinv_idx[v1].append(v2)

    #print("\n")
    #print(diccionario)          
    
    return inv_dict
    

def querydocs(scanwrd, diccw):
    '''
    Quering the words provide by the client
    
    '''

    results = {}
    for word in diccw:
        for w in scanwrd:
            if w != word[0]:
                pass
            else:
                results[w] = word[1]

    return results


def salir ():
    exit()

if __name__ == '__main__':

    ##tracking the time at the begining of the process
    time_start = time.localtime()
    
    ## building the inverted index dictionary    
    inverted_dictionary = {}
    queriew = []
    
    files_path = gettingpath()
    inv_dictionary = gettingthedictionary(files_path)
    #print("\n")
    #print(inv_dictionary)
    
    time_end = time.localtime()
    
    print("\n")
    print("======================================= Dictionary ======================================")
    print("\n")
    print('The dictionary from the documents scanned is: ')
    print("\n")
    print( dinv_idx)
    
    print("\n")
    print ('Processing Start Time: %.2d:%.2d' % (time_start.tm_hour, time_start.tm_min))
    print ('Processing End Time: %.2d:%.2d' % (time_end.tm_hour, time_end.tm_min))



