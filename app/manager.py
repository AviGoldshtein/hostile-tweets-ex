from app.fetcher import Fetcher
from app.processor import Processor


class Manager:
    def __init__(self):
        self.fetcher = Fetcher()
        data = self.fetcher.get_collection_data()
        self.processor = Processor(data)
        self.run_prepossessing()

    def run_prepossessing(self):
        print("starting analyzing...")
        self.processor.find_rarest_word_for_each()
        self.processor.express_sentiment()
        self.processor.weapons_detected()
        print("analyzing ended.")

    def get_results(self):
        return self.processor.get_df_as_dictionary()