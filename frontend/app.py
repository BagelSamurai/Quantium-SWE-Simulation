from dash import Dash, dcc, html, callback, Output, Input
import plotly.express as px
import pandas as pd

app = Dash(__name__)



df = pd.read_csv('../data/cleaned/cleaned_data.csv')
# Plot dates across months
df['date'] = pd.to_datetime(df['date'])

df.set_index('date', inplace=True)




app.layout = html.Div(children=[
    html.H1(
        children='Pink Morsel Sales',
        style={
            'textAlign': 'center',
        }
    ),
    html.Div('Select a region:'),


    dcc.RadioItems(options=['north', 'south', 'east', 'west'], value='north',  id='region-control', inline=True),

    dcc.Graph(
        id='main-graph',
        figure={}
    )
])
@callback(
    Output(component_id='main-graph', component_property='figure'),
    Input(component_id='region-control', component_property='value')
)
def update_graph(selected_region):
    filtered_df = df[df['region'] == selected_region]
    monthly_sales_df = filtered_df.resample('ME').sum().reset_index()
    fig = fig = px.line(monthly_sales_df, x='date', y='sales',  title=f'Monthly Sales of Pink Morsels by {selected_region} region')
    return fig
if __name__ == '__main__':
    app.run(debug=True)