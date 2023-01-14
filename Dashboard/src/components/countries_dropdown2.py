from dash import Dash,html,dcc
from dash.dependencies import Input, Output
import pandas as pd

from . import ids


def render(app:Dash) -> html.Div:
    all_countries = pd.read_csv('/Users/rahool/Rahul_DS_projects/Data_Visualization/Dashboard_project/data/Covid-19 vaccinations-by-manufacturer-Efficacy included- DSE2700-4.csv')['Country'].unique()

    return html.Div(
        children = [
            html.H6('Country'),
            dcc.Dropdown(
                id = ids.COUNTRIES_DROPDOWN2,
                options = [{'label':country,"value":country} for country in all_countries ],
                value= all_countries[0],
                multi=False,
                style = {'color':'black'}
            )
        ]
    )