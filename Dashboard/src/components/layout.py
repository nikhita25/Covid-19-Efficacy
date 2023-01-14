from dash import Dash, html,dcc
from src.components import vaccines_dropdown, bubble_plot,tree_map, countries_per_vaccine, vaccine_usage, vaccines_dropdown2, map_plot, countries_dropdown, bar_plot
from src.components import variant_dropdown,efficacy_map_plot,countries_dropdown2,line_chart


text_bubble = 'I am calling this for bubble chart'
objective_text = 'The objective of this project is to find a closer estimation of the true protection percentage of a country considering the number of vaccines, its efficacy, the vaccine type composition of a given country and the percentage of its vaccinated population.'
intro_text = 'Despite different COVID-19 Vaccines being available for over 2 years, hesitancy about vaccines’ ability to protect our immune system against serious disease still lingers.     Due to the lack of understanding of what vaccines are and how they work, it is often misunderstood that vaccines guarantee an 100% protection from any given disease.'
intro_text2 = 'The average conversation of covid vaccine tends to overlook the efficacy of the vaccine and the vaccine type used in each country. Countries with different vaccines, different vaccine efficacy and different vaccine composition will end up having different protection levels against Covid-19 and its different variants.'
assumptions_text1 = '- Vaccine efficacy levels reported are taken at face value.'
assumptions_text2 = '- Vaccine provided replicates the same efficacy despite people’s specific health conditions.'
assumptions_text3 = '- Level of protection based on the number of vaccine doses administrated.'
unknowns_text = '- Number of vaccines given to each person.'
unknowns_text_1 = 'The two graphs above show the number of countries each vaccine type was used it. The graph shows that Pfizer was the most used vaccine, while SKYcovione and Medicago were the least common.'
unknowns_text_2 = 'The map above shows the Total Vaccine doses gives in each country based on the vaccine type. The drop down can be used to select a certain vaccine type and the countries it was used in are colored.'
vaccine_efficacy_definition = 'For this project, we define "Vaccine Efficacy" as the levels of protection assuming the ideal conditions are met.'
formula_1 = '- Vaccine Percentage Distribution = Number of vaccines of a single type / Total number of vaccines administrated'
formula_2 = '- Vaccine True Percentage Contribution = Vaccine Percentage Distribution * Vaccine Efficacy'
formula_3 = '- Country Percentage  Protection Level = Sum of all Vaccine True Percentage Contribution.'
formula_4 = '- Truly Protected Vaccinated People = Country Percentage Protection Level * Number of Vaccinated People'
formula_5 = '- True Country Percentage Protection Level  = Truly Protected Vaccinated People / Country Population'
efficacy_bar = 'The efficacy or percentage of vaccine protection for severe disease and infection are shown in the bar graph. The drop down can be used to select the variant. Portugal has the highest percentage protection at 41.5% and Bulgaria has one of the lowest at 12.8%. '
efficacy_map = 'The maps show the percentage of people protected for each variant. The darker the color the less the percentage of protection.'


def create_layout(app : Dash) -> html.Div:


    return html.Div(
        className = 'row',
        children=[
            html.H1(app.title, style={
                'textAlign':'center',
                'color' : '#808080'
            }),
            html.Hr(),
            html.H2('Objective', style={
                'textAlign' : 'left',
                'color' : 'white'
            }),
            html.Hr(),
            dcc.Markdown(objective_text,style={'color':'#FAF9F6'}),
            # html.Hr(),
            html.H2('Introduction', style={
                'textAlign' : 'left',
                'color' : 'white'
            }),
            html.Hr(),
            dcc.Markdown(intro_text,style={'color':'#FAF9F6'}),
            dcc.Markdown(intro_text2,style={'color':'#FAF9F6'}),
            html.Hr(),
            html.H2('Assumptions', style={
                'textAlign' : 'left',
                'color' : 'white'
            }),
            dcc.Markdown(assumptions_text1,style={'color':'#FAF9F6'}),
            dcc.Markdown(assumptions_text2,style={'color':'#FAF9F6'}),
            dcc.Markdown(assumptions_text3,style={'color':'#FAF9F6'}),
            html.Hr(),
            html.H2('Unknowns', style={
                'textAlign' : 'left',
                'color' : 'white'
            }),
            dcc.Markdown(unknowns_text,style={'color':'#FAF9F6'}),


            html.Div(
                children = [
                    html.H2('Vaccine usage'),
                    html.Hr(),
                    #vaccines_dropdown.render(app)
                ]
            ),
            vaccine_usage.render(app),
            
            # html.Div(
            #     children = [
            #         html.H2('Tree Map'),
            #         html.Hr(),
            #         #vaccines_dropdown.render(app)
            #     ]
            # ),
            tree_map.render(app),
            dcc.Markdown(unknowns_text_1,style={'color':'#FAF9F6'}),
            # html.Div(
            #     children = [
            #         html.H2('Countries per vaccine type'),
            #         html.Hr(),
            #         #vaccines_dropdown.render(app)
            #     ]
            # ),
            # countries_per_vaccine.render(app),
            html.H3('Total vaccinations per country'),
            html.Div(
                className = "dropdown-container",
                children = [
                    vaccines_dropdown.render(app)
                ]
            ),
            bubble_plot.render(app),
            # dcc.Markdown(text_bubble,style={'color':'white'}),
            # html.Hr(),
            # html.H2('Map Plot'),
            html.Div(
                children = [
                    vaccines_dropdown2.render(app)
                ]
            ),
            html.Hr(),
            map_plot.render(app),
            dcc.Markdown(unknowns_text_2,style={'color':'#FAF9F6'}),
            html.Hr(),
            # html.H2('Vaccine distribution in each country'),
            # html.Div(
            #     children = [
            #         countries_dropdown2.render(app)
            #     ]
            # ),
            # line_chart.render(app),
            html.H2('Vaccine Efficacy'),
            html.Hr(),
            dcc.Markdown(vaccine_efficacy_definition,style={'color':'#FAF9F6'}),
            html.H3('Formulas'),
            dcc.Markdown(formula_1,style={'color':'#FAF9F6'}),
            dcc.Markdown(formula_2,style={'color':'#FAF9F6'}),
            dcc.Markdown(formula_3,style={'color':'#FAF9F6'}),
            dcc.Markdown(formula_4,style={'color':'#FAF9F6'}),
            dcc.Markdown(formula_5,style={'color':'#FAF9F6'}),
            html.Hr(),
            html.Div(
                children = [
                    countries_dropdown.render(app)
                ]
            ),
            bar_plot.render(app),
            dcc.Markdown(efficacy_bar,style={'color':'#FAF9F6'}),
            efficacy_map_plot.render(app),
            dcc.Markdown(efficacy_map,style={'color':'#FAF9F6'}),
            # html.text(text_bubble, style = {'color': 'white'}),

            # html.Hr(),
            # html.H2("Vaccine Efficacy Map plot"),
            # html.Hr(),
            # html.Div(
            #     children = [
            #         variant_dropdown.render(app)
            #     ]
            # ),
            # efficacy_map_plot.render(app)
        ]
    )
