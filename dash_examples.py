import dash
from dash import dcc, html, Dash
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.DataFrame(
    {
        "Name": ["John", "Peter"]*3,
        "Subject": ['Math']*2 + ['Science']*2 + ['Art']*2,
        "Score": [90, 100, 80, 70, 50, 100],

    }
)
fig = px.bar(df, x="Subject", y="Score", color="Name", barmode="group")

app.layout = html.Div(
    children=[
        html.H1('Plotly Dashboard Example'),
        html.Div('''
        Dash를 이용한 Dashboard 예저 코드를 정리합니다.
        이 문서 영역은 html.Div()로 구현합니다.
        '''
        ),
        dcc.Graph(id='Dash example graph', figure=fig),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
