from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import os
import nltk
nltk.download('vader_lexicon')

def get_black_list():
    base_route = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(base_route, "data", "weapons.txt")
    with open(path, mode="r", encoding="utf-8") as black_list:
        return black_list.read().split()


class Processor:
    def __init__(self, data):
        self.df = pd.DataFrame(data)

    def find_rarest_word_for_each(self):
        self.df['rarest_word'] = self.df['Text'].map(lambda x: pd.Series(x.split()).value_counts().idxmin())

    def express_sentiment(self):
        self.df['sentiment'] = self.df['Text'].apply(Processor.check_sentiment)
        # print(self.df.head().to_string())

    def weapons_detected(self):
        self.df['weapons_detected'] = self.df['Text'].apply(Processor.check_for_weapons_in_text)

    def get_df_as_dictionary(self):
        return self.df.to_dict(orient="records")

    @staticmethod
    def check_sentiment(txt):
        score = SentimentIntensityAnalyzer().polarity_scores(txt)
        compound = score['compound']
        if compound <= 0.5:
            return "negative"
        elif compound < 1.5:
            return "neutral"
        else:
            return "positive"

    @staticmethod
    def check_for_weapons_in_text(txt):
        black_list = get_black_list()
        weapon = None
        for word in txt.split():
            if word in black_list:
                weapon = word
                break
        return weapon