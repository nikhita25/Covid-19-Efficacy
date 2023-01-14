from dash import Dash,html,dcc
from dash.dependencies import Input, Output
import pandas as pd

from . import ids

def render(app:Dash) -> html.Div:
    all_vaccines = pd.read_csv('/Users/rahool/Rahul_DS_projects/Data_Visualization/Dashboard_project/data/bubble_plot_data.csv')['Vaccine_Manufacturer'].unique()

    return html.Div(
        children = [
            html.H6("Vaccine Manufacturer"),
            dcc.Dropdown(
                id = ids.VACCINES_DROPDOWN_2,
                options = [{'label':vaccine,"value":vaccine} for vaccine in all_vaccines ],
                value= all_vaccines[0],
                multi=False,
                style = {'color':'black'}
            )
        ]
    )

