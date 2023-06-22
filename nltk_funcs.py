from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag
from nltk.corpus import wordnet,stopwords
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()



def web_question(sentence):
    ques_words = ['meant','who', 'when', 'where', 'why', 'definition of', 'meaning of','what','should','where','which','does']
    adv = ['your','my','you']
    for keyword in ques_words:
        if keyword in sentence.lower():
            for ad in  adv:
                if ad in sentence.lower():
                    return False
            return True
    return False


def is_wordnet_question(word_token):
    if 'meaning' in word_token or 'define' in word_token or 'definition' in word_token or 'meant' in word_token:
        last_word = word_token[-1]
        if pos_tag([last_word])[0][1].startswith('N') or pos_tag([last_word])[0][1].startswith('V'):
            return last_word
    return False


def get_sentiment(chat_message):
    chat_list = sent_tokenize(chat_message)
    sent_list = []
    for chat in chat_list:
        if "User: " in chat:
            index = chat.find("Bot")
            chat = chat[0:index-1]
            chat = chat.replace("User: ","")
            sentiment_scores = sid.polarity_scores(chat)
            sentiment_polarity = sentiment_scores['compound']

            if sentiment_polarity >= 0.05:
                sentiment_label = 'Happy'
            elif sentiment_polarity <= -0.05:
                sentiment_label = 'Sad'
            else:
                sentiment_label = 'Neutral'
            sent_list.append(sentiment_label)
    counter = Counter(sent_list)
    most_common_element = max(counter, key=counter.get)
    return most_common_element

