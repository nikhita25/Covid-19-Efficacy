from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from . import ids
import pandas as pd
import geopandas as gpd
import folium, pycountry
from plotly.subplots import make_subplots

df3  = pd.read_csv('/Users/rahool/Rahul_DS_projects/Data_Visualization/Dashboard_project/data/map_plot_file.csv')

def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.MAP_PLOT, "children"),
        Input(ids.VACCINES_DROPDOWN_2, 'value')
    )

    def update_map_plot(vaccines: str) -> html.Div:

        maxval=pd.DataFrame(df3[df3['Vaccine_Manufacturer']==vaccines].groupby('Country')['Total_Vaccinations'].max())
        maxval.reset_index(inplace=True)
        list_countries = maxval['Country'].to_list()
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
            maxval.loc[(maxval.Country == k), 'iso_alpha'] = v

        

        fig = make_subplots(rows=3, cols=4, start_cell="bottom-left")


        fig = px.choropleth(data_frame = maxval,
                        locations= "iso_alpha",
                        color= "Total_Vaccinations",
                        # color_continuous_scale= px.colors.sequential.Inferno,
                        # animation_frame = 'Country',
                        hover_name= "Total_Vaccinations",
                        template='plotly_dark')

        # my_map.save('vaccine_locations.html')

        # filtered_data = ALL_VACCINES_DATA[ALL_VACCINES_DATA['Vaccine_Manufacturer']==vaccines]

        # fig = my_map
        return html.Div(dcc.Graph(figure=fig),id=ids.MAP_PLOT)

        # return html.Div([html.Iframe(id = 'MAP',srcDoc=open('vaccine_locations.html','r').read(), width='100%',height='600')],
        #          id=ids.MAP_PLOT)

    return html.Div(id= ids.MAP_PLOT)