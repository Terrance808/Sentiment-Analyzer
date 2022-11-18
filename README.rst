============================================================================
PDF Sentiment Analyzer
============================================================================
This project assesses the positive vs. negative sentiment of each PDF input.
----------------------------------------------------------------------------
Usage
----------------------------------------------------------------------------
* Install requirements, preferably in a virtual environment.
* Store PDFs in the folder, Articles.
* Run main.py in the terminal
----------------------------------------------------------------------------
Sentiment Analysis Score
----------------------------------------------------------------------------
The program counts the number of positive words and negative words in each PDF
using **Loughran-McDonald Sentiment Word Lists**. It then returns scores for each
PDF on a scale from 0 - 1 (completely negative to completely positive) in a 
nondescending order.
----------------------------------------------------------------------------
Sentiment Score Formula
----------------------------------------------------------------------------
Positive Words / Positive Words + Negative Words