from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from . import ids
import pandas as pd
import geopandas as gpd
import folium, pycountry
from plotly.subplots import make_subplots
import plotly.graph_objects as go

df3 = pd.read_csv('/Users/rahool/Rahul_DS_projects/Data_Visualization/Dashboard_project/data/actual_efficacy_in_each_country.csv')
list_countries = df3['Country'].to_list()
country_code = []
d_country_code = {}
for country in list_countries:
        try:
            country_data = pycountry.countries.search_fuzzy(country)
            country_code = country_data[0].alpha_3
            d_country_code.update({country: country_code})
        except:
            print('could not add ISO 3 code for ->', country)
            d_country_code.update({country: ' '})

for k, v in d_country_code.items():
    df3.loc[(df3.Country == k), 'iso_alpha'] = v

def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.EFFICACY_MAP_PLOT, "children"),
        Input(ids.COUNTRIES_DROPDOWN, 'value')
    )
    

    def update_map_plot(vaccines: str ) -> html.Div:
        if vaccines == 'Alpha/Ancestral':
            fig = make_subplots(rows=3, cols=4, start_cell="bottom-left")
            # fig = go.Figure()
            # fig.add_trace(
            #     go.Choropleth(
            #         data_frame = df3,
            #         locations= "iso_alpha",
            #         z = "percent_protected_SD_Al",
            #         marker_line_color = 'white',
            #         coloraxis = 'coloraxis',
            #         hover_name= "percent_protected_SD_Al"
            #     )
            # )
            # fig.add_trace(
            #     go.Choropleth(
            #         data_frame = df3,
            #         locations= "iso_alpha",
            #         z = "percent_protected_inf_Al",
            #         marker_line_color = 'white',
            #         coloraxis = 'coloraxis',
            #         hover_name= "percent_protected_inf_Al"
            #     )
            # )
            fig = px.choropleth(data_frame = df3,
                        locations= "iso_alpha",
                        # z = "percent_protected_SD_Al",
                        # marker_line_color = 'white',
                        # coloraxis = 'coloraxis',
                        color= "percent_protected_SD_Al",
                        # color_continuous_scale= px.colors.sequential.Inferno,
                        # animation_frame = 'Country',
                        hover_name= "percent_protected_SD_Al",
                        template='plotly_dark')
                        # color_continuous_scale=px.colors.sequential.Tealgrn)
            fig2 = px.choropleth(data_frame = df3,
                        locations= "iso_alpha",
                        # z = "percent_protected_SD_Al",
                        # marker_line_color = 'white',
                        # coloraxis = 'coloraxis',
                        color= "percent_protected_inf_Al",
                        # color_continuous_scale= px.colors.sequential.Inferno,
                        # animation_frame = 'Country',
                        hover_name= "percent_protected_inf_Al",
                        template='plotly_dark')
                        # color_continuous_scale=px.colors.sequential.Tealgrn)
            return html.Div(children=[
                dcc.Graph(figure=fig),
                dcc.Graph(figure = fig2)],id=ids.EFFICACY_MAP_PLOT)
        elif vaccines == 'Beta/Gamma/Delta':
            fig = make_subplots(rows=3, cols=4, start_cell="bottom-left")
            fig = px.choropleth(data_frame = df3,
                        locations= "iso_alpha",
                        color= "percent_protected_SD_Dt",
                        # color_continuous_scale= px.colors.sequential.Inferno,
                        # animation_frame = 'Country',
                        hover_name= "percent_protected_SD_Dt",
                        template='plotly_dark')
                        # color_continuous_scale=px.colors.sequential.Tealgrn)
            fig2 = px.choropleth(data_frame = df3,
                        locations= "iso_alpha",
                        # z = "percent_protected_SD_Al",
                        # marker_line_color = 'white',
                        # coloraxis = 'coloraxis',
                        color= "percent_protected_inf_Dt",
                        # color_continuous_scale= px.colors.sequential.Inferno,
                        # animation_frame = 'Country',
                        hover_name= "percent_protected_inf_Dt",
                        template='plotly_dark')
                        # color_continuous_scale=px.colors.sequential.Tealgrn)
            return html.Div(children=[
                dcc.Graph(figure=fig),
                dcc.Graph(figure = fig2)],id=ids.EFFICACY_MAP_PLOT)
        
        elif vaccines == 'Omicron':
            fig = make_subplots(rows=3, cols=4, start_cell="bottom-left")
            fig = px.choropleth(data_frame = df3,
                        locations= "iso_alpha",
                        color= "percent_protected_SD_Om",
                        # color_continuous_scale= px.colors.sequential.Inferno,
                        # animation_frame = 'Country',
                        hover_name= "percent_protected_SD_Om",
                        template='plotly_dark')
                        # color_continuous_scale=px.colors.sequential.Tealgrn)
            fig2 = px.choropleth(data_frame = df3,
                        locations= "iso_alpha",
                        # z = "percent_protected_SD_Al",
                        # marker_line_color = 'white',
                        # coloraxis = 'coloraxis',
                        color= "percent_protected_inf_Om",
                        # color_continuous_scale= px.colors.sequential.Inferno,
                        # animation_frame = 'Country',
                        hover_name= "percent_protected_inf_Om",
                        template='plotly_dark')
                        # color_continuous_scale=px.colors.sequential.Tealgrn)
            
            return html.Div(children=[
                dcc.Graph(figure=fig),
                dcc.Graph(figure = fig2)],id=ids.EFFICACY_MAP_PLOT)
            


    return html.Div(id = ids.EFFICACY_MAP_PLOT)