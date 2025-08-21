import pandas as pd
import os

def get_black_list():
    base_route = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(base_route, "data", "weapons.txt")
    with open(path, mode="r", encoding="utf-8") as black_list:
        return black_list.read().split()


class Processor:
    def __init__(self, data):
        self.df = pd.DataFrame(data)

    def find_rarest_word_for_each(self):
        pass

    def express_sentiment(self):
        pass

    def weapons_detected(self):
        pass

    def get_df(self):
        return self.df
