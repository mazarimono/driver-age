import dash  
import dash_core_components as dcc 
import dash_html_components as html 
import plotly.graph_objs as go 
import pandas as pd 

df = pd.read_csv('allpop.csv', index_col=0)
df1 = pd.read_csv('driver-license.csv', index_col=0)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H1('日本の年齢別人口(青色)と運転免許証の分布（オレンジ）')
    ], style={'textAlign': 'center'}),
    html.Div([
        dcc.Graph(id='age-chart',
                figure={
                    'data':[
                        go.Bar(
                            x=df['age'],
                            y=df['total'],
                            name = 'population'
                        ),
                        go.Bar(
                            x = df['age'],
                            y = df1['合計'],
                            name='has driver license'
                        )
                    ],
                    'layout':{
                        'xaxis': {'title':{'text': '<b>年齢</b>', 'font':{'size': 20}}},
                        'yaxis':{'title':{'text': '<b>人口</b>', 'font':{'size': 20}}},
                    }
                }
        ),
    html.Div([
        html.H1('年齢別運転免許証保有割合')],
        style={'textAlign': 'center'}),
        dcc.Graph(id='percentage-chart',
                figure={
                    'data':[
                        go.Bar(
                            x = df['age'],
                            y = df1['合計'] / df['total'],
                            name = 'percentage who has driver license'
                        )
                    ],
                    'layout':{
                        'xaxis': {'title':{'text': '<b>年齢</b>', 'font':{'size': 20}}},
                        'yaxis': {'title': {'text': '<b>割合</b>',
                        'font':{'size': 20}}}
                    }
                })
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)