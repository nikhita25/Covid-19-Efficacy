from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from . import ids
import pandas as pd

VACCINE_TYPE_DATA = pd.read_csv('/Users/rahool/Rahul_DS_projects/Data_Visualization/Dashboard_project/data/Total_vaccines_in_each_country.csv')

def render(app: Dash) -> html.Div:
    # @app.callback(
    #     Output(ids.TREE_MAP, "children"),
    #     Input(ids.VACCINES_DROPDOWN, 'value')
    # )

   
    fig = px.scatter(VACCINE_TYPE_DATA,x='Date',y='Country' ,size='Total_Vaccinations',color='Vaccine_Manufacturer',template='plotly_dark')
    return html.Div(dcc.Graph(figure=fig), id=ids.COUNTRY_COUNT_VACCINE)

    # return html.Div(id= ids.BUBBLE_PLOT)