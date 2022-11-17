from PyPDF2 import PdfReader
import re

reader = PdfReader("./Articles/american_express_10_articles.PDF")
page = reader.pages[0]
words_raw = page.extract_text()
words = re.split("[\t\n\r \.,()]", words_raw)
print(words)
print("Word List Length:", len(words))
