from PyPDF2 import PdfReader
# import pandas as pd
import numpy as np

reader = PdfReader("./Articles/american_express_10_articles.PDF")
# number_of_pages = len(reader.pages)
# page = reader.pages[0]
text_list_raw = list()
for page in reader.pages:
    text_list_raw.append(page.extract_text())

text_list_raw = [x.lower() for x in text_list_raw]

all_words = list()
for text in text_list_raw:
    temp_text_list = text.split()
    all_words += temp_text_list

positive_array = np.char.lower(np.loadtxt("./Word_Lists/LoughranMcDonald_Positive.csv", dtype="str"))
negative_array = np.char.lower(np.loadtxt("./Word_Lists/LoughranMcDonald_Negative.csv", dtype="str"))

positive_word_count = 0
negative_word_count = 0

for i in all_words:
    if i in positive_array: 
        positive_word_count = positive_word_count + 1
    if i in negative_array: 
        negative_word_count = negative_word_count + 1

print(positive_array[1])
print("Positive Word Count:", positive_word_count)
print("Negative Word Count:", negative_word_count)