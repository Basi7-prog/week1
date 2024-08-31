import pandas as pd
import matplotlib.pyplot as plt


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
    
    #Active publishers based on frequency(above 3 percent) 
    def active_publisher(articles):
        percent=pd.DataFrame()
        percent["articles published"]=articles['publisher'].value_counts()
        percent['in_percent']=((articles['publisher'].value_counts()/len(articles))*100)
        percent=percent[percent['in_percent']>=1]
        
        #filter only active publishers from data
        publishers_names=percent.index
        snt2=articles[articles['publisher'].isin(publishers_names)]
        snt2['date']=Stocks.change_to_date(snt2['date'])
        return [percent,snt2]
    
    def plot_news_frequency(data,dwm):
        no_published_date=data.value_counts()
        sorted_df=no_published_date.sort_index()
        sorted_df.index=pd.to_datetime(sorted_df.index)

        return sorted_df.resample(dwm).sum().plot(figsize=(40,20), kind='line')
    
    #change date column to datetime type
    def change_to_date(date_data):
        date_data=pd.to_datetime(date_data, errors='coerce', format='%Y-%m-%d %H:%M:%S',utc=True)
        date_data=pd.to_datetime(date_data).dt.strftime("%Y-%m-%d %H:%M:%S")
        return date_data