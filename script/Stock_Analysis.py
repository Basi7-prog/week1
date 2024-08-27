import pandas as pd


class Stocks():
    def __init__(self) -> None:
        pass

    def read_sentiment():
        df=pd.read_csv(r'C:\Users\Baslael\Documents\Kifiya\week1\datasets\raw_analyst_ratings\raw_analyst_ratings.csv')
        # df=pd.read_csv(r'C:\Users\Baslael\Documents\Kifiya\week1\datasets\yfinance_data\AAPL_historical_data.csv')
        return df
    
    def read_Stock_Data():
        df=pd.read_csv(r'C:\Users\Baslael\Documents\Kifiya\week1\datasets\yfinance_data\AAPL_historical_data.csv')
        return df
    def active_publisher(articles):
        #Active publishers based on frequency(above 3 percent) 
        percent=pd.DataFrame()
        percent["articles published"]=articles['publisher'].value_counts()
        percent['in_percent']=((articles['publisher'].value_counts()/len(articles))*100)
        percent=percent[percent['in_percent']>=1]
        return percent