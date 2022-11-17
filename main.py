import os
import re
from PyPDF2 import PdfReader
import numpy as np

articles = os.listdir("./Articles/")

class Article_SA:
    def __init__(self, filename):
        self.positive_words = 0
        self.negative_words = 0
        
        reader = PdfReader(filename)

        text_list_raw = list()
        for page in reader.pages:
            text_list_raw.append(page.extract_text().lower())

        all_words = list()
        for text in text_list_raw:
            all_words += re.split("[\t\n\r \.,()]", text)
        
        positive_array = np.char.lower(np.loadtxt("./Word_Lists/LoughranMcDonald_Positive.csv", dtype="str"))
        negative_array = np.char.lower(np.loadtxt("./Word_Lists/LoughranMcDonald_Negative.csv", dtype="str"))

        for i in all_words:
            if i in positive_array: self.positive_words += 1
            if i in negative_array: self.negative_words += 1
        
        self.total_words = self.positive_words + self.negative_words
    def print(self):
        print(f"Positive Words in Article: {self.positive_words}")
        print(f"Negative Words in Article: {self.negative_words}")
        print(f"Total Words in Article: {self.total_words}")

if __name__ == "__main__":
    sample = Article_SA(f"./Articles/{articles[0]}")
    sample.print()
