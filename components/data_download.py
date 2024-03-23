import yfinance as yf
import datetime
import numpy as np

class DownloadData:
    def __init__(self, params_dict:dict):
        self.params_dict = params_dict

    def download_stock_data(self):
        try:
            params = self.params_dict

            tickers = params['tickers'][0]
            start = datetime.datetime.strptime(params['start'][0], '%Y-%m-%d')
            end = datetime.datetime.strptime(params['end'][0], '%Y-%m-%d')
            interval = params['interval'][0]
            group_by = params['group_by'][0]
            auto_adjust = params['auto_adjust'][0]
            prepost = params['prepost'][0]
            threads = params['threads'][0]
            proxy = params['proxy'][0]

            if proxy == 'None':
                proxy = None
            else:
                proxy = proxy

            nifty50_df = yf.download(
                            tickers = tickers,
                            start = start,
                            end = end,
                            interval = interval,
                            group_by = group_by,
                            auto_adjust = auto_adjust,
                            prepost = prepost,
                            threads = threads,
                            proxy = proxy)

            high = np.asarray(nifty50_df["High"])
            low = np.asarray(nifty50_df["Low"])

            avg_values = np.asarray((nifty50_df["Open"]+nifty50_df["High"]+nifty50_df["Low"]+nifty50_df["Close"])/4)

            return high, low, avg_values

        except:
            pass
    