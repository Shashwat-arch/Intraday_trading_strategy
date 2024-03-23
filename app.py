from flask import Flask, redirect, url_for, render_template, request

from pipeline.cluster_pipeline import CustomData
from components.data_download import DownloadData
from components.data_transformation import FindExtremum
from components.make_clusters import FindClustersCenters
from components.make_plot import MakePlot

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/formclusters', methods=['GET', 'POST'])
def form_clusters():
    if request.method=='GET':
        return render_template('home.html')
    else:
        params = CustomData(
            tickers=request.form.get('tickers'),
            startdate=request.form.get('start_date'),
            enddate=request.form.get('end_date'),
            interval=request.form.get('interval'),
            groupby=request.form.get('group_by'),
            autoadjust=request.form.get('auto_adjust'),
            prepost=request.form.get('pre_post'),
            threads=request.form.get('threads'),
            proxy=request.form.get('proxy'),
            num_clusters=int(request.form.get('num_clusters')),
            algorithm=request.form.get('clustering_algorithm')
        )
        params_dict = params.get_data_as_dict()

        download_data = DownloadData(params_dict=params_dict)

        high, low, avg_values = download_data.download_stock_data()

        extremum = FindExtremum(high=high, low=low).find_extremum()

        num_clusters = params_dict["num_clusters"][0]

        centroids = FindClustersCenters(extremum=extremum, algorithm=params_dict["algorithm"][0], num_clusters=num_clusters).fit_algorithm()

        imgpath = MakePlot(avg_values, centroids).scatter_plot()

        return render_template('home.html', results=imgpath)

if __name__=="__main__":
    app.run(debug=True)