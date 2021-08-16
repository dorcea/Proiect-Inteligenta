
from sklearn.base import BaseEstimator, TransformerMixin

class TextNormalizer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
#x este un string
    def transform(self, X, y=None):
        #creem o copie
        X_copy = X.copy()
        for i in range(len(X_copy)):
            X_copy[i] = X_copy[i].lower()
# scoatem new linerulie
            X_copy[i] = X_copy[i].replace('\n', ' ')
            X_copy[i] = X_copy[i].replace('\r', ' ')
# functia strip scoate din stinga si dreapta spatiile
            X_copy[i] = X_copy[i].strip()
        return X_copy


class WordExctractor(BaseEstimator, TransformerMixin):  # gaseste hapaxele si
    def __init__(self, language, tokenize):
        self.language = language
        self.stopwords = stopwords.words(self.language)
        self.tokenize = tokenize

    def fit(self, X, y=None):
        general_freq = FreqDist()
        for txt in X:
            freq_dist = FreqDist(self.tokenize(txt))  # freq_dist calculeaza distributia pe toate textele
            general_freq.update(freq_dist)
        self.hapaxes = general_freq.hapaxes()
        return self

    def transform(self, X, y=None):
        X_copy = X.copy()
        for i in range(len(X_copy)):
            X_copy[i] = ' '.join([token for token in self.tokenize(X_copy[i])
                                  if token not in self.stopwords and token not in self.hapaxes])
        return X_copy


class ApplyStemmer(BaseEstimator, TransformerMixin):
    def __init__(self, stemmer, tokenize):
        self.stemmer = stemmer
        self.tokenize = tokenize

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X_copy = X.copy()
        for i in range(len(X_copy)):
            X_copy[i] = ' '.join([self.stemmer.stem(token)
                                  for token in self.tokenize(X_copy[i])])
        return X_copy