from traceback import print_tb
import pandas as pd


class Clean_Tweets:
    """
    This class will clean the twitter data and return a clean data frame
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df
        print('Automation in Action...!!!')

    def drop_unwanted_column(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        remove rows that has column names. This error originated from
        the data collection stage.
        """

        unwanted_rows = df[df['retweet_count']
                           == 'retweet_count'].index
        df.drop(unwanted_rows, inplace=True)
        df = df[df['polarity'] != 'polarity']

        return df

    def drop_duplicate(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        drop duplicate rows
        """
        df = df.drop_duplicates()
        return df

    def convert_to_datetime(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        convert column to datetime
        """
        self.df['created_at'] = pd.to_datetime(
            self.df['created_at'], errors='coerce')

        self.df = self.df[self.df['created_at'] >= '2020-12-31']

        return self.df

    def convert_to_numbers(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        convert columns like polarity, subjectivity, retweet_count
        favorite_count etc to numbers
        """
        self.df['polarity'] = pd.to_numeric(
            self.df['polarity'], errors='coerce')
        self.df['retweet_count'] = pd.to_numeric(
            self.df['retweet_count'], errors='coerce')
        self.df['favorite_count'] = pd.to_numeric(
            self.df['favorite_count'], errors='coerce')

        return self.df

    def remove_non_english_tweets(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        remove non english tweets from lang
        """
        self.df = df[df['lang'] == 'en']

        return self.df


if __name__ == '__main__':
    data_frame = pd.read_csv('./data/processed_tweet_data.csv')
    cleaner = Clean_Tweets(df=data_frame)

    data_frame = cleaner.drop_duplicate(data_frame)
    data_frame = cleaner.remove_non_english_tweets(data_frame)
    data_frame = cleaner.convert_to_datetime(data_frame)
    data_frame = cleaner.convert_to_numbers(data_frame)
    data_frame = cleaner.drop_unwanted_column(data_frame)

    data_frame.to_csv('./data/clean_processed_tweet_data.csv')
    print('Done cleaning and saving!!!')
