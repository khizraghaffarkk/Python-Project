"""
Created on Fri Jul 17 12:21:01 2020
@author: Khizra Ghaffar
"""
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq  
#raw_text="""Terrorism is, in the broadest sense, the use of intentional violence for political or religious purposes. It is used in this regard primarily to refer to violence during peacetime or in the context of war against non-combatants (mostly civilians and neutral military personnel). The terms "terrorist" and "terrorism" originated during the French Revolution of the late 18th century but gained mainstream popularity in the 1970s during the conflicts of Northern Ireland, the Basque Country and Palestine. The increased use of suicide attacks from the 1980s onwards was typified by the September 11 attacks in New York City and Washington, D.C. in 2001.There are various different definitions of terrorism, with no universal agreement about it. Terrorism is a charged term. It is often used with the connotation of something that is "morally wrong". Governments and non-state groups use the term to abuse or denounce opposing groups. Varied political organizations have been accused of using terrorism to achieve their objectives. These include right-wing and left-wing political organizations, nationalist groups, religious groups, revolutionaries and ruling governments. Legislation declaring terrorism a crime has been adopted in many states. When terrorism is perpetrated by nation states, it is not considered terrorism by the state conducting it, making legality a largely grey-area issue. There is no consensus as to whether or not terrorism should be regarded as a war crime. The Global Terrorism Database, maintained by the University of Maryland, College Park, has recorded more than 61,000 incidents of non-state terrorism, resulting in at least 140,000 deaths, between 2000 and 2014"""
def nltk_summarizer(raw_text):
	stopWords = set(stopwords.words("english"))
	word_frequencies = {}  
	for word in nltk.word_tokenize(raw_text):  
	    if word not in stopWords:
	        if word not in word_frequencies.keys():
	            word_frequencies[word] = 1
	        else:
	            word_frequencies[word] += 1

	maximum_frequncy = max(word_frequencies.values())

	for word in word_frequencies.keys():  
	    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
#print(maximum_frequncy)
#text_summarizer(raw_docx)
	sentence_list = nltk.sent_tokenize(raw_text)
	sentence_scores = {}  
	for sent in sentence_list:  
	    for word in nltk.word_tokenize(sent.lower()):
	        if word in word_frequencies.keys():
	            if len(sent.split(' ')) < 30:
	                if sent not in sentence_scores.keys():
	                    sentence_scores[sent] = word_frequencies[word]
	                else:
	                    sentence_scores[sent] += word_frequencies[word]



	summary_sentences=heapq.nlargest(7,sentence_scores,key=sentence_scores.get)

	summary = ' '.join(summary_sentences)
	return summary
#nltk_summarizer(raw_text)