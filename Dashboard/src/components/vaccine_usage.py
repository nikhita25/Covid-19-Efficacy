from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from . import ids
import pandas as pd

VACCINE_USAGE_DATA = pd.read_csv('/Users/rahool/Rahul_DS_projects/Data_Visualization/Dashboard_project/data/vaccinetype_country.csv')

def render(app: Dash) -> html.Div:
    # @app.callback(
    #     Output(ids.TREE_MAP, "children"),
    #     Input(ids.VACCINES_DROPDOWN, 'value')
    # )

   
    fig = px.scatter(VACCINE_USAGE_DATA,x='Vaccine_Manufacturer',y = 'Number of Countries', size='Number of Countries',color='Number of Countries',hover_data=['Vaccine_Manufacturer'],
    template='plotly_dark',color_continuous_scale=px.colors.sequential.Tealgrn)
    return html.Div(dcc.Graph(figure=fig), id=ids.VACCINE_USAGE)

    # return html.Div(id= ids.BUBBLE_PLOT)