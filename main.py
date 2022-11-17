import os
import re
from math import sqrt
from PyPDF2 import PdfReader
import numpy as np





class Article_SA:
    def __init__(self, filename):
        self.positive_words = 0
        self.negative_words = 0
        self.filename = filename
        
        reader = PdfReader(f"./Articles/{filename}")  # Extract text from PDF
        text_list_raw = list()
        for page in reader.pages:
            text_list_raw.append(page.extract_text().lower())
        all_words = list()
        for text in text_list_raw:
            all_words += re.split("[\t\n\r \.,()]", text)
        
        # Get positive and negative words to search for
        positive_array = np.char.lower(np.loadtxt("./Word_Lists/LoughranMcDonald_Positive.csv", dtype="str"))
        negative_array = np.char.lower(np.loadtxt("./Word_Lists/LoughranMcDonald_Negative.csv", dtype="str"))

        for i in all_words:
            if i in positive_array: self.positive_words += 1
            if i in negative_array: self.negative_words += 1
        
        self.total_words = self.positive_words + self.negative_words
        self.raw_sentiment = self.positive_words / (self.positive_words + self.negative_words)
    def get_total(self):
        return self.total_words
    def get_sentiment(self):
        return self.raw_sentiment
    def print(self):
        print(f"Positive Words in Article: {self.positive_words}")
        print(f"Negative Words in Article: {self.negative_words}")
        print(f"Total Words in Article: {self.total_words}")

class Sentiment_Analysis:
    def _insertion_sort(self):
        unordered_articles = self.articles
        for k in range(1, len(unordered_articles)):
            cur = unordered_articles[k]
            j = k
            while j > 0 and unordered_articles[j - 1].get_sentiment() > cur.get_sentiment():
                unordered_articles[j] = unordered_articles[j-1]
                j -= 1
            unordered_articles[j] = cur
        self.ordered_articles = unordered_articles
    
    def __init__(self):
        article_filenames = os.listdir("./Articles/")
        
        self.sa_aggregate = 0
        self.sa_mean = 0
        self.sa_standard_deviation = 0
      
        self.articles = list() # Contains individual article SA
        for i in range(len(article_filenames)):
            self.articles.append(Article_SA(article_filenames[i]))
        
        self.population_size = len(self.articles)
        # Get Aggregated Sentiment Score
        for article in self.articles:
            self.sa_aggregate += article.get_sentiment()
        
        self.sa_mean = self.sa_aggregate / self.population_size
        sum_of_squares = 0
        for article in self.articles:
            sum_of_squares += (article.get_sentiment() - self.sa_mean) ** 2
        
        self.sa_variance = sum_of_squares / self.population_size
        self.sa_standard_deviation = sqrt(self.sa_variance)

        self._insertion_sort()
    
    def print(self):
        print()
        print("============================================================================")
        print("             Article Sentiment Analysis Score in Ascending Order            ")
        for article in self.ordered_articles:
            print(f"Filename: {article.filename}")
            print(f"SA Score: {article.get_sentiment()}")
            print()
        print("============================================================================")
        print()

        

        
    

if __name__ == "__main__":
    x = Sentiment_Analysis()
    x.print()
