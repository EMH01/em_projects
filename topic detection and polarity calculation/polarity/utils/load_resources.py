import os

def load_swn():
    swn = {}
    try:
        with open(os.getenv('SWN_PATH'), 'r') as swn_file:
            lines = swn_file.readlines()
            for line in lines:
                word,values = line.split('\t')
                pos,positive,negative = values.split()
                positive, negative = float(positive),float(negative)
                if positive == 0 and negative == 0:
                    continue
                try:
                    swn[word][pos] = [positive,negative]
                except:
                    swn[word] = {pos:[positive,negative]}
    except IOError as fileNotFound:
        raise fileNotFound
    
    return swn

def load_stopwords():
    with open(os.getenv('STOPWORDS_PATH'), 'r') as stopwords_file:
        stopwords = [line.strip() for line in stopwords_file.readlines()]
        return stopwords