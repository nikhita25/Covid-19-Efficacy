from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from . import ids
import pandas as pd


DATA = pd.read_csv('/Users/rahool/Rahul_DS_projects/Data_Visualization/Dashboard_project/data/Covid-19 vaccinations-by-manufacturer-Efficacy included- DSE2700-4.csv')

def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.LINE_CHART, "children"),
        Input(ids.COUNTRIES_DROPDOWN2, 'value')
    )
    def update_line_chart(country : str) -> html.Div:
        filtered_data = DATA[DATA['Country']==country]
        max_cnt = filtered_data.groupby('Vaccine_Manufacturer')['Total_Vaccinations'].max()
        # print(max_cnt)
        # filtered_data = filtered_data.sort_values('Date')
        # fig = px.scatter(filtered_data,x='Date' ,y=['Total_Vaccinations'],color='Vaccine_Manufacturer',line_shape='linear')
        fig = px.bar(filtered_data,x='Vaccine_Manufacturer' ,y='Total_Vaccinations',
        template='plotly_dark',color_continuous_scale=px.colors.sequential.Tealgrn)

        return html.Div(dcc.Graph(figure=fig), id=ids.LINE_CHART)

    return html.Div(id=ids.LINE_CHART)