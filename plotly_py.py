import pandas as pd
import os
import plotly
import plotly.offline as pyof
#import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
from exercise.QfileDialog import MyWindow

########################################
class Plotly_PyQt5():
    def __init__(self):
        plotly_dir='plotly_html'
        if not os.path.isdir(plotly_dir):
            os.mkdir(plotly_dir)

        self.path_dir_plotly_html=os.getcwd()+os.sep+plotly_dir

    def get_plotly_path_if_hs300_bais(self,file_name='if_hs300_bais.html'):
        Button = MyWindow()
        a = Button.msg()
        print(a)

        #df=pd.read_excel(a)
        path_plotly=self.path_dir_plotly_html+os.sep+file_name
        df = pd.read_excel(a)
#        df=pd.read_excel(r'if_index_bais.xlsx')


        line_main_price=go.Scatter(
            x=df['t'],
            y=df['sint'],
            name='sin曲线',
#            conncetgaps=True,
        )
        a=np.array(df['t'])
        s=np.array(df['sint'])
        detal_s = (s[2:np.size(s)] - s[1:np.size(s) - 1]) / (a[2:np.size(a)] - a[1:np.size(a) - 1])
        detal_a=a[1:np.size(a)-1]




        line_hs300_close=go.Scatter(
            x=detal_a,
            y=detal_s,
            name='sin导数',
#            connectgaps=True,
        )
        data=[]


        [data1,data2]=[line_hs300_close,line_main_price]






        fig=plotly.subplots.make_subplots(rows=2,cols=1,shared_xaxes=True)

        fig.append_trace(line_main_price,1,1)
        fig.append_trace(line_hs300_close, 2, 1)
        fig.layout = dict(title='if_hs300_bias',
                      xaxis1=dict(title='Data',domain = [0, 1]),
                      yaxis1=dict(title='Price',titlefont= {
                                               'size': 20},
                               domain = [0, 0.5]),
                      xaxis2=dict(domain = [0, 1]),
                      yaxis2=dict(title='导数',titlefont= {
                                               'size': 20},domain = [0.5, 1])

                      )

        #fig.layout.xaxis1.domain = [0, 1]
        #fig.layout.xaxis2.domain = [0, 1]
        #fig.layout.yaxis1.domain = [0, 0.5]
        #fig.layout.yaxis2.domain = [0.5, 1]



        #fig.layout.yaxis1 = dict(title='这是横坐标轴',titlefont= {
         #       'size': 20},
        #    domain = [0, 0.5])






        '''

        fig.layout.yaxis1={
           'title':'这是横坐标轴',
            'titlefont':{
             'size':20
            }
          }
        fig.layout.yaxis2={
           'title':'这是横坐标轴',
            'titlefont':{
             'size':30
            }
          }
        '''

         #   go.Figure(data=data,layout=layout)

        pyof.plot(fig, filename=path_plotly, auto_open=False)
        return path_plotly



    '''


        fig=go.Figure(data=data, layout=layout)
    '''
        #pyof.plot(fig,filename=path_plotly,auto_open=False)


         #return path_plotly
