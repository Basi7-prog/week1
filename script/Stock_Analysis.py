import pandas as pd
import matplotlib.pyplot as plt
import talib as ta
import pynance as py


class Stocks():
    def __init__(self) -> None:
        pass

    def read_sentiment():
        df=pd.read_csv(r'C:\Users\Baslael\Documents\Kifiya\week1\datasets\raw_analyst_ratings\raw_analyst_ratings.csv')
        # df=pd.read_csv(r'C:\Users\Baslael\Documents\Kifiya\week1\datasets\yfinance_data\AAPL_historical_data.csv')
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
        no_published_date=data.index.value_counts()
        sorted_df=no_published_date.sort_index()
        # sorted_df.index=pd.to_datetime(sorted_df.index)

        return sorted_df.resample(dwm).sum().plot(figsize=(40,20), kind='line')
    
    #change date column to datetime type
    def change_to_date(date_data):
        date_data=pd.to_datetime(date_data, errors='coerce', format='%Y-%m-%d %H:%M:%S',utc=True)
        date_data=pd.to_datetime(date_data).dt.strftime("%Y-%m-%d %H:%M:%S")
        return date_data
    
    def index_edit(data, col):
        data[col]=Stocks.change_to_date(data[col])
        data.set_index(col,inplace=True)
        data.index=pd.to_datetime(data.index)
        
        return data
    
    
    #Stock indicators
    def read_Stock_Data(ticker):
        qnt=py.data.get(ticker)
        qnt=qnt.sort_index()
        return qnt
    
    #RSI calculator and add rsi column to dataframe
    def rsi_calc(data):
        data['RSI']=ta.RSI(data['Close'],timeperiod=10)
        
        #add signal column to signal for bu or sell
        data['Signals']='Neutral'
        data.loc[data['RSI']>70, 'Signals']='Buy'
        data.loc[data['RSI']<30, 'Signals']='Sell'
        
        #change null datas to mean
        rsi_mean=data['RSI'].mean()
        data.loc[data['RSI'].isna(),'RSI']=rsi_mean
                
        return data
    
    #MACD calculator and add cols
    def macd_calc(data):
        data['MACD_line'],data['MACD_sginal'],data['MACD_hist']=ta.MACD(data['Close'], signalperiod=10)
        
        #filling null values with the column mean
        macd_mean,MACD_sginal,MACD_hist=data['MACD_line'].mean(),data['MACD_sginal'].mean(),data['MACD_hist'].mean()
        data.loc[data['MACD_line'].isna(),'MACD_line']=macd_mean
        data.loc[data['MACD_sginal'].isna(),'MACD_sginal']=MACD_sginal
        data.loc[data['MACD_hist'].isna(),'MACD_hist']=MACD_hist
        
        return data
    
    def plot_indicators(data,data_size=100):
        fig,ax=plt.subplots(4,1,figsize=(20,20))

        ax[1].plot(data['RSI'].tail(data_size))
        ax[1].set_title('RSI')
        ax[2].plot(data['MACD_line'].tail(data_size), label='MACD_line')
        ax[2].plot(data['MACD_sginal'].tail(data_size), label='MACD_sginal')
        ax[2].set_title('MACD_sginal and MACD_line')
        ax[2].legend(loc='upper left', fontsize=32)
        ax[3].bar(range(len(data['MACD_hist'].tail(data_size))),data['MACD_hist'].tail(data_size),label='Histogram')
        ax[3].set_title('MACD_hist')
        ax[0].plot(data['Close'].tail(data_size))
        ax[0].set_title('Close')
        
        return plt.show()
    
    