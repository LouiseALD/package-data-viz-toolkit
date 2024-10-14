import plotly.graph_objs as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

def create_dashboard(data):
    app = dash.Dash(__name__)
    
    app.layout = html.Div([
        dcc.Graph(id='bar-chart'),
        dcc.Dropdown(
            id='dropdown',
            options=[{'label': key, 'value': key} for key in data.keys()],
            value=list(data.keys())[0]
        )
    ])

    @app.callback(
        Output('bar-chart', 'figure'),
        [Input('dropdown', 'value')]
    )
    def update_graph(selected_value):
        figure = go.Figure([go.Bar(x=[selected_value], y=[data[selected_value]])])
        return figure

    app.run_server(debug=True)
