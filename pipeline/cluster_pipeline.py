from datetime import datetime

class CustomData:
    def __init__(self,
                 tickers:str,
                 startdate:datetime,
                 enddate:datetime,
                 interval:str,
                 groupby:str,
                 autoadjust:bool,
                 prepost:bool,
                 threads:bool,
                 proxy:bool,
                 num_clusters:int,
                 algorithm:str):
        self.tickers = tickers
        self.startdate = startdate
        self.enddate = enddate
        self.interval = interval
        self.groupby = groupby
        self.autoadjust = autoadjust
        self.prepost = prepost
        self.threads = threads
        self.proxy = proxy
        self.num_clusters = num_clusters
        self.algorithm = algorithm

    def get_data_as_dict(self):
        try:
            custom_data_dict = {
                "tickers" : [self.tickers],
                "start" : [self.startdate],
                "end" : [self.enddate],
                "interval" : [self.interval],
                "group_by" : [self.groupby],
                "auto_adjust" : [self.autoadjust],
                "prepost" : [self.prepost],
                "threads" : [self.threads],
                "proxy" : [self.proxy],
                "num_clusters":[self.num_clusters],
                "algorithm" : [self.algorithm]
            }

            return custom_data_dict
        except:
            pass