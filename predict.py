import pickle
import nltk
from nltk import word_tokenize          
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords
import contractions
import string
import os
import sys

import warnings
warnings.filterwarnings("ignore")

# uncomment the follow part if need
# nltk.download('omw-1.4')
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('stopwords')

model_path = "./svc.model"
# load model
model = pickle.load(open(model_path, 'rb'))

# load vectorizer
class Tokenizer(object):
    def __init__(self):
        self.wnl = WordNetLemmatizer()
    def __call__(self, articles):
        articles = articles.lower()

        for p in string.punctuation:
          articles = articles.replace(p, ' ')
        
        articles = contractions.fix(articles)
        
        res = []
        _stopwords = set(stopwords.words('english'))
        for t in word_tokenize(articles):
          token = self.wnl.lemmatize(t) 
          if token in _stopwords:
            continue
          res.append(token)
        return res

vectorizer = pickle.load(open('./vectorizer', 'rb'))


def predictText(pred):
    return "Normal question" if pred == 0 else "DEI violation"

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 3 or argv[1] not in ['-t', '-f']:
        print("invalid command")

    if argv[1] == '-t':
        text = " ".join(argv[2:])
        print("Question:", text)
        data = vectorizer.transform([text])
        pred = model.predict(data)[0]
        print(predictText(pred))
    elif argv[1] == '-f':
        file_path = argv[2]

        if not os.path.exists(file_path):
            print("file {} not exists".format(file_path))
        else:
            with open(file_path, 'r') as f:
                all_text = f.readlines()
            data = vectorizer.transform(all_text)
            preds = model.predict(data)
            with open("./results.txt", 'w') as f:
                for pred in preds:
                    f.write(predictText(pred)+'\n')
                print("All results have been saved to results.txt")
        
     