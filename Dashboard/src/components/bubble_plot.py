from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from . import ids
import pandas as pd

ALL_VACCINES_DATA = pd.read_csv('/Users/rahool/Rahul_DS_projects/Data_Visualization/Dashboard_project/data/bubble_plot_data.csv')

def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.BUBBLE_PLOT, "children"),
        Input(ids.VACCINES_DROPDOWN, 'value')
    )

    def update_bubble_plot(vaccines: str) -> html.Div:
        filtered_data = ALL_VACCINES_DATA[ALL_VACCINES_DATA['Vaccine_Manufacturer']==vaccines]

        fig = px.scatter(filtered_data,x='Date',y='Country',size='Total_Vaccinations',color='Total_Vaccinations',
        template='plotly_dark',color_continuous_scale=px.colors.sequential.Tealgrn)
        return html.Div(dcc.Graph(figure=fig), id=ids.BUBBLE_PLOT)

    return html.Div(id= ids.BUBBLE_PLOT)