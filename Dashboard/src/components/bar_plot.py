from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from . import ids
import pandas as pd
import plotly.graph_objects as go

#ALL_VACCINES_DATA = pd.read_csv('/Users/rahool/Rahul_DS_projects/Data_Visualization/Dashboard_project/data/bubble_plot_data.csv')
EFFICACY_DATA = pd.read_csv('/Users/rahool/Rahul_DS_projects/Data_Visualization/Dashboard_project/data/actual_efficacy_in_each_country.csv')
EFFICACY_DATA['percent_protected_SD_Al'] = EFFICACY_DATA['percent_protected_SD_Al']*100
EFFICACY_DATA['percent_protected_inf_Al'] = EFFICACY_DATA['percent_protected_inf_Al']*100
EFFICACY_DATA['percent_protected_SD_Dt'] = EFFICACY_DATA['percent_protected_SD_Dt']*100
EFFICACY_DATA['percent_protected_inf_Dt'] = EFFICACY_DATA['percent_protected_inf_Dt']*100
EFFICACY_DATA['percent_protected_SD_Om'] = EFFICACY_DATA['percent_protected_SD_Om']*100
EFFICACY_DATA['percent_protected_inf_Om'] = EFFICACY_DATA['percent_protected_inf_Om']*100


def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.BAR_PLOT, "children"),
        Input(ids.COUNTRIES_DROPDOWN, 'value')
    )

    def update_bar_plot(country: str) -> html.Div:

        # filtered_data = EFFICACY_DATA[EFFICACY_DATA['Vaccine_Manufacturer']==country]
        if country == 'Alpha/Ancestral':
            # fig = go.Figure()
            # fig.add_trace(go.bar(x=EFFICACY_DATA['percent_protected_SD_Al']))
            # fig.add_trace(go.bar(x=EFFICACY_DATA['percent_protected_inf_Al']))
            # EFFICACY_DATA = EFFICACY_DATA.sort_values(by='percent_protected_SD_Al',axis=1)
            fig = px.bar(EFFICACY_DATA.sort_values(by='percent_protected_inf_Al'), x=['percent_protected_SD_Al','percent_protected_inf_Al'],y='Country',labels={'value':'Percentage'},
            template='plotly_dark',color_continuous_scale=px.colors.sequential.Tealgrn, height=1000)
            # fig.update_layout(barmode="relative",xaxis={'categoryorder':'category ascending'})
            # fig.update_traces(textfont_size=4, textangle=50, textposition="outside", cliponaxis=False)
        if country == 'Beta/Gamma/Delta':
            fig = px.bar(EFFICACY_DATA.sort_values(by='percent_protected_inf_Dt'),x=['percent_protected_SD_Dt','percent_protected_inf_Dt'],y='Country',labels={'value':'Percentage'},
            template='plotly_dark',color_continuous_scale=px.colors.sequential.Tealgrn, height=1000)
            # fig.update_layout(barmode="relative",yaxis={'categoryorder':'category ascending'})
            # fig.update_traces(textfont_size=4, textangle=50, textposition="outside", cliponaxis=False)
        if country == 'Omicron':
            fig = px.bar(EFFICACY_DATA.sort_values(by='percent_protected_inf_Om'),x=['percent_protected_SD_Om','percent_protected_inf_Om'],y='Country',labels={'value':'Percentage'},
            template='plotly_dark',color_continuous_scale=px.colors.sequential.Tealgrn, height=1000)
            # fig.update_layout(barmode="relative",yaxis={'categoryorder':'category ascending'})
            # fig.update_traces(textfont_size=4, textangle=50, textposition="outside", cliponaxis=False)
        # x=['percent_protected_inf_Al','percent_protected_inf_Dt','percent_protected_inf_Om']
        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_PLOT)

    return html.Div(id= ids.BAR_PLOT)