'''
Created on Oct 24, 2013

@author: Ryan
'''

import sys
import json

# Parse the JSON file
if __name__ == '__main__':
    questions_file = open(sys.argv[1])
    sentiment_file = open(sys.argv[2])
    
    sentiment_scores = {} # initialize an empty dictionary
    
    for line in sentiment_file:
        term, score = line.split("\t") # The file is tab-delimited. "\t" means "tab character"
        sentiment_scores[term] = int(score)  # Convert the score to an integer.
    
    # This holds the sum of all the sentiments of every question in the file
    total_sentiment_sum = 0
    
    for line in questions_file:
        # Convert the line to a JSON object so we can process it
        questions = json.loads(line)
        
        for question in questions['items']:
            
            # Check if the tweet has the "text" key.
            if 'body' in question:
                # This holds the sum of the sentiment for this particular question
                question_sentiment_sum = 0
                
                question_text = question['body'].encode('utf-8')
                
                # Make the tweet text all lower case in case there are some words with capitals, which wouldn't match our dict keys
                question_text_lower = question_text.lower()
                
                terms = question_text_lower.split()
                
                # If any term ends with punctuation such as period, exclamation mark, question mark, then remove the punctuation.
                for i in range(len(terms)):
                    terms[i] = terms[i].rstrip('.!?,:;-')
                    
                for term in terms:
                    if term in sentiment_scores:
                        question_sentiment_sum += sentiment_scores[term]
                    
                #print '====== QUESTION TEXT =======\n' + question_text + '\n=======SENTIMENT VALUE========\n' + str(sentiment_sum)
                #break
            
                total_sentiment_sum += question_sentiment_sum
                #print question_sentiment_sum
        
        print total_sentiment_sum