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
            html.H1(['日本の運転免許所保有データ'], style={'textAlign': 'center'}),
            html.H2(['１．日本の年齢別人口(青)と運転免許証の分布（緑）と保有割合（橙：線） 2018年度'], style={'textAlign': 'center'}),
        html.Div([
        dcc.Graph(id='age-chart',
                figure={
                    'data':[
                        go.Bar(
                            x=df['age'],
                            y=df['total'],
                            name = '人口',
                            showlegend=False,
                            hoverlabel={'font':{'size': 20}},
                            marker = {'color': '#84B1ED'}
                        ),
                        go.Bar(
                            x = df['age'],
                            y = df1['合計'],
                            name='免許保有人口',
                            showlegend=False,
                            hoverlabel={'font':{'size': 20}},
                            marker={'color':'#81e6cd'}
                        ),
                        go.Scatter(
                            x = df['age'],
                            y = df1['合計'] / df['total'],
                            name = '免許保有割合',
                            yaxis = 'y2',
                            showlegend=False,
                            line = {'color': '#f1bbba', 'width': 5},
                            hoverlabel={'font':{'size': 20}}
                        )
                    ],
                    'layout':{
                        'xaxis': {'title':{'text': '年齢', 'font':{'size': 20}}},
                        'yaxis':{'title':{'text': '人口', 'font':{'size': 20}}},
                        'yaxis2':{'title':{'text': '免許保有割合', 'font':{'size': 20}}, 'overlaying': 'y',
                        'side': 'right'},
                        
                    }
                }
            ),
        ]),
        ]),
    html.Div([
        html.H2(['２．免許保有累計人数 2018年度'], style={'textAlign': 'center'}),
        dcc.Graph(id='cumsum-pct',
            figure={
                'data': [
                    go.Scatter(
                        x=df['age'],
                        y=df1['cumsum'],
                        name='免許保有累計割合',
                        showlegend=False,
                        fill='tozeroy',
                        hoverinfo='all',
                        hoverlabel={'font':{'size': 30}},
                        line={'color':'#81e6cd'}
                    )
                ],
                'layout':{
                    'yaxis':{'title':'累計割合', 'font':{'size': 20}},
                    'xaxis':{'title':'年齢', 'font':{'size':20}}
                }
            }
        )
    ]),
    html.Div([
        html.H2(['３．運転免許保有数変化（2001年＝＞2018年）'],style={'textAlign': 'center'}),
        dcc.Graph(id='histgram-2001-2018',
            figure={
                'data': [
                    go.Scatter(
                        x = df2['age'],
                        y = df2['2001'],
                        name = '2001年免許保有者数',
                        fill='tozeroy',
                        hoverlabel={'font':{'size': 30}},
                        line={'color':'#81e6cd'}
                    ),
                    go.Scatter(
                        x=df2['age'],
                        y=df2['2018'],
                        name='2018免許保有者数',
                        fill='tozeroy',
                        hoverlabel={'font':{'size': 30}},
                        line={'color':'#84B1ED'}
                    )
                ],
                'layout':{
                    'xaxis':{'title': '<b>年代</b>', 'font':{'size': 20}},
                    'yaxis':{'title': '<b>免許保有者数</b>', 'font':{'size':20}},
                    'bg_color':'#e8e8e8', 
                }
            }
        )
    ]),
], style={'padding': '5%','backgroundColor':'#e8e8e8'})

if __name__ == '__main__':
    app.run_server(debug=True)