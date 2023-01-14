from dash import Dash,html,dcc
from dash.dependencies import Input, Output
import pandas as pd

from . import ids


def render(app:Dash) -> html.Div:
    # all_countries = pd.read_csv('/Users/rahool/Rahul_DS_projects/Data_Visualization/Dashboard_project/data/actual_efficacy_in_each_country.csv')['Vaccine_Manufacturer'].unique()
    all_variants = ['Alpha/Ancestral','Beta/Gamma/Delta','Omicron']
    return html.Div(
        children = [
            html.H6("Variant"),
            dcc.Dropdown(
                id = ids.VARIANT_DROPDOWN,
                options = [{'label':variant,"value":variant} for variant in all_variants ],
                value= all_variants[0],
                multi=False,
                style = {'color':'black'}
            )
        ]
    )

