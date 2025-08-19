from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__)



df = pd.read_csv('../data/cleaned/cleaned_data.csv')
# Plot dates across months
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
# Resample
monthly_sales_df = df.resample('M').sum().reset_index()

fig = px.line(monthly_sales_df, x='date', y='sales',  title='Monthly Sales of Pink Morsels')

app.layout = html.Div(children=[
    html.H1(
        children='Pink Morsel Sales',
        style={
            'textAlign': 'center',
        }
    ),


    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)