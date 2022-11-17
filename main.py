import os
import re
from math import sqrt

import numpy as np
from PyPDF2 import PdfReader


class Article_SA:
    def __init__(self, filename):
        self.positive_words = 0
        self.negative_words = 0
        self.filename = filename
        
        # Extract text from PDF
        reader = PdfReader(f"./Articles/{filename}")
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
            if i in positive_array:
                self.positive_words += 1
            if i in negative_array:
                self.negative_words += 1

        self.total_words = self.positive_words + self.negative_words
        self.sentiment_score = self.positive_words / \
            (self.positive_words + self.negative_words)

    def get_filename(self):
        return self.filename

    def get_positive(self):
        return self.positive_words

    def get_negative(self):
        return self. negative_words

    def get_total(self):
        return self.total_words

    def get_sentiment(self):
        return self.sentiment_score


class Sentiment_Analysis:
    def _insertion_sort(self, articles):
        unordered_articles = articles
        for k in range(1, len(unordered_articles)):
            cur = unordered_articles[k]
            j = k
            # Order by Sentiment Analysis Score
            while j > 0 and unordered_articles[j - 1].get_sentiment() > cur.get_sentiment():
                unordered_articles[j] = unordered_articles[j-1]
                j -= 1
            unordered_articles[j] = cur
        self.ordered_articles = unordered_articles

    def __init__(self):
        article_filenames = os.listdir("./Articles/")
        self.articles = list()  # Contains individual article SA
        for i in range(len(article_filenames)):
            self.articles.append(Article_SA(article_filenames[i]))
        self.number_of_articles = len(self.articles)
        self._insertion_sort(self.articles)

    def report_SA(self):
        print()
        print(
            "============================================================================")
        print(
            "             Article Sentiment Analysis Score in Ascending Order            ")
        for article in self.ordered_articles:
            print(f"Filename: {article.get_filename()}")
            print(f"Positive WC: {article.get_positive()}")
            print(f"Negative WC: {article.get_negative()}")
            print(f"Total WC: {article.get_total()}")
            print(f"SA Score: {article.get_sentiment()}")
            print()
        print(
            "============================================================================")
        print()


if __name__ == "__main__":
    Sentiment_Analysis().report_SA()
