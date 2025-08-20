from dash import Dash, dcc, html, callback, Output, Input
import plotly.express as px
import pandas as pd
from pathlib import Path
app = Dash(__name__)

region_colors = {
    'north': '#8a3800',
    'south': '#005d5d',
    'east': '#6929c4',
    'west': '#198038',
}

styles = {
    'container': {
        'maxWidth': '960px',
        'margin': 'auto',
        'marginTop': '20px',
        'padding': '20px',
        'backgroundColor': 'white',
        'border': '1px solid #ddd',
        'borderRadius': '5px',
        'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'
    },
    'header': {
        'textAlign': 'center',
        'color': '#333'
    },
    'subHeader': {
        'textAlign': 'center',
        'color': '#555',
        'marginBottom': '15px'
    },
    'controlsContainer': {
        'textAlign': 'center',
        'padding': '10px',
        'border': '1px solid #ddd',
        'borderRadius': '5px',
        'marginBottom': '20px'
    }
}
DATA_PATH = Path(__file__).parent / '../data/cleaned/cleaned_data.csv'
df = pd.read_csv(DATA_PATH)
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

app.layout = html.Div(children=[
    html.Div(style=styles['container'], children=[
        html.H1(
            children='Pink Morsel Sales',
            style=styles['header'],
            id='header',
        ),
        html.Div(style=styles['controlsContainer'], children=[
            html.Div('Select a region to view sales:', style=styles['subHeader']),
            dcc.RadioItems(
                options=['north', 'south', 'east', 'west'],
                value='north',
                id='region-control',
                inline=True,
            ),
        ]),
        dcc.Graph(
            id='main-graph',
            figure={}
        )
    ])
])

@callback(
    Output(component_id='main-graph', component_property='figure'),
    Input(component_id='region-control', component_property='value')
)
def update_graph(selected_region):
    filtered_df = df[df['region'] == selected_region]
    monthly_sales_df = filtered_df.resample('ME').sum().reset_index()

    fig = px.line(
        monthly_sales_df,
        x='date',
        y='sales',
        title=f'Monthly Sales for {selected_region.capitalize()} Region'
    )

    fig.update_traces(line_color=region_colors[selected_region])
    # fig.update_layout(transition_duration=500)

    return fig

if __name__ == '__main__':
    app.run(debug=True)