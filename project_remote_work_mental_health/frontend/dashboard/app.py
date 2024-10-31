import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

# Load your dataset
df = pd.read_csv('path_to_your_dataset.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Create a simple layout
app.layout = html.Div(children=[
    html.H1(children='Remote Work and Mental Health Dashboard'),

    dcc.Graph(
        id='example-graph',
        figure=px.scatter(df, x='Column1', y='Column2', title='Sample Scatter Plot')
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')