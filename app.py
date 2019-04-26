import dash  
import dash_core_components as dcc 
import dash_html_components as html 
import plotly.graph_objs as go 
import pandas as pd 
import os 

df = pd.read_csv('allpop.csv', index_col=0)
df1 = pd.read_csv('driver-license.csv', index_col=0)
df2 = pd.read_csv('drv0118.csv', index_col=0)

app = dash.Dash(__name__)
server = app.server
app.layout = html.Div([
        html.Div([
            html.H1(['日本の年齢別人口(青色)と運転免許証の分布（オレンジ） 2018年度'], style={'textAlign': 'center'}),
        html.Div([
        dcc.Graph(id='age-chart',
                figure={
                    'data':[
                        go.Bar(
                            x=df['age'],
                            y=df['total'],
                            name = '人口',
                            showlegend=False,
                            hoverlabel={'font':{'size': 30}}
                        ),
                        go.Bar(
                            x = df['age'],
                            y = df1['合計'],
                            name='免許保有人口',
                            showlegend=False,
                            hoverlabel={'font':{'size': 30}}
                        ),
                        go.Scatter(
                            x = df['age'],
                            y = df1['合計'] / df['total'],
                            name = '免許保有割合',
                            yaxis = 'y2',
                            showlegend=False,
                            hoverlabel={'font':{'size': 30}}
                        )
                    ],
                    'layout':{
                        'xaxis': {'title':{'text': '<b>年齢</b>', 'font':{'size': 20}}},
                        'yaxis':{'title':{'text': '<b>人口</b>', 'font':{'size': 20}}},
                        'yaxis2':{'title':{'text': '<b>免許保有割合</b>'}, 'overlaying': 'y',
                        'side': 'right'},
                        
                    }
                }
            ),
        ]),
        ]),
    html.Div([
        dcc.Graph(id='cumsum-pct',
            figure={
                'data': [
                    go.Scatter(
                        x=df['age'],
                        y=df1['percent'],
                        showlegend=False,
                        fill='tozeroy',
                        name='免許保有累計割合',
                        hoverlabel={'font':{'size': 30}}
                    )
                ]
            }
        )
    ]),
    html.Div([
        html.H3(['運転免許保有数変化（2001年＝＞2018年）'],style={'textAlign': 'center'}),
        dcc.Graph(id='histgram-2001-2018',
            figure={
                'data': [
                    go.Scatter(
                        x = df2['age'],
                        y = df2['2001'],
                        name = '2001年免許保有者数',
                        fill='tozeroy',
                        hoverlabel={'font':{'size': 30}}
                    ),
                    go.Scatter(
                        x=df2['age'],
                        y=df2['2018'],
                        name='2018免許保有者数',
                        fill='tozeroy',
                        hoverlabel={'font':{'size': 30}}
                    )
                ],
                'layout':{
                    'xaxis':{'title': '<b>年代</b>', 'font':{'size': 20}},
                    'yaxis':{'title': '<b>免許保有者数</b>', 'font':{'size':20}}
                }
            }
        )
    ]),
], style={'marginBottom': '5%'})

if __name__ == '__main__':
    app.run_server(debug=True)