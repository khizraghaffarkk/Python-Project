# Natural Language Processing Packages
import spacy 
nlp = spacy.load('en')
# Packages for Normalizing Text
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
# Import Heapq for Finding the Top N Sentences
from heapq import nlargest
#raw_docx="""Terrorism is, in the broadest sense, the use of intentional violence for political or religious purposes. It is used in this regard primarily to refer to violence during peacetime or in the context of war against non-combatants (mostly civilians and neutral military personnel). The terms "terrorist" and "terrorism" originated during the French Revolution of the late 18th century but gained mainstream popularity in the 1970s during the conflicts of Northern Ireland, the Basque Country and Palestine. The increased use of suicide attacks from the 1980s onwards was typified by the September 11 attacks in New York City and Washington, D.C. in 2001.There are various different definitions of terrorism, with no universal agreement about it. Terrorism is a charged term. It is often used with the connotation of something that is "morally wrong". Governments and non-state groups use the term to abuse or denounce opposing groups. Varied political organizations have been accused of using terrorism to achieve their objectives. These include right-wing and left-wing political organizations, nationalist groups, religious groups, revolutionaries and ruling governments. Legislation declaring terrorism a crime has been adopted in many states. When terrorism is perpetrated by nation states, it is not considered terrorism by the state conducting it, making legality a largely grey-area issue. There is no consensus as to whether or not terrorism should be regarded as a war crime. The Global Terrorism Database, maintained by the University of Maryland, College Park, has recorded more than 61,000 incidents of non-state terrorism, resulting in at least 140,000 deaths, between 2000 and 2014"""
def text_summarizer(raw_docx):
    raw_text = raw_docx
    docx = nlp(raw_text)
    #print("Docx: ",docx)
    stopwords = list(STOP_WORDS)
    #print("Stopwords: ",stopwords)
    # Build Word Frequency # word.text 
    word_frequencies = {}  
    for word in docx:  
        if word.text not in stopwords:
            if word.text not in punctuation:
              if word.text not in word_frequencies.keys():
                  word_frequencies[word.text] = 1
              else:
                  word_frequencies[word.text] += 1
    #print("Original Document: \n",raw_docx)
    #print("Punctuation: \n",punctuation)
    #print("Word Frequency: \n",word_frequencies)
    maximum_frequncy = max(word_frequencies.values())
    #print("Max Frequency: \n",maximum_frequncy)
  #text_summarizer(raw_docx)
    for word in word_frequencies.keys():  
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)  
    #print("Word Frequency: \n",word_frequencies)
    # Sentence Tokenization
    sentence_list = [ sentence for sentence in docx.sents ]

    # Sentence Scores
    sentence_scores = {}  
    for sent in sentence_list:  
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
              if word.text not in punctuation:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]

    s_length=int(len(sentence_list)*0.3)
    #print("=============================================")
    #print("\n\nlength: ",s_length)
    #print("Sentence Score:  ",sentence_scores)
    summarized_sentences=nlargest(s_length,sentence_scores,key=sentence_scores.get)
    final_sentences = [ w.text for w in summarized_sentences ]
    summary = ' '.join(final_sentences)
    #print("\nSummary: \n",summary)
    #print("\nOriginal Document Length: ",len(raw_docx))
    #print("Summary Length: ",len(summary))
    return summary
#text_summarizer(raw_docx)