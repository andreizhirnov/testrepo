# Import required libraries
import pandas as pd
import numpy as np
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

spacex_df['success'] = spacex_df['class'].apply(lambda x: 'Success' if x==1 else 'Failure')
df_site_success = spacex_df[['Launch Site','success']].value_counts().reset_index()
df_site_success.rename(columns = {0:'count'}, inplace=True)

dd_options = [{'label': 'All Sites', 'value': 'ALL'}]
uni = [{'label': s, 'value':s} for s in df_site_success['Launch Site'].unique()]
dd_options.extend(uni)

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown', 
                                    options=dd_options,
                                    value='ALL',
                                    placeholder="Select a Launch Site Here",
                                    searchable=True
                                    ),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id='payload-slider',
                                    min=0, max=10000, step=1000,
                                    marks={0: '0', 2500:'2500', 5000:'5000', 7500:'7500', 10000: '10000'},
                                    value=[min_payload,max_payload]),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
# Function decorator to specify function input and output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    filtered_df = df_site_success
    if entered_site == 'ALL':
        fig = px.pie(filtered_df[filtered_df['success']=='Success'], values='count', 
        names='Launch Site', 
        title='Total Missions with Successful Landings by Site') 
    else:
        filtered_df = filtered_df[filtered_df['Launch Site']==entered_site]
        fig = px.pie(filtered_df, values='count', 
        names='success',
        color='success',
        color_discrete_map={'Success':'green','Failure':'red'},
        title=f'Landing Outcomes for Missions Launched at {entered_site}') 
    return fig

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'),
              Input(component_id='payload-slider', component_property='value'))
def get_scatter_chart(entered_site, slider_range):
    low, high = slider_range
    filtered_df = spacex_df[np.logical_and(spacex_df['Payload Mass (kg)'] >= low, spacex_df['Payload Mass (kg)'] <= high)]
    if entered_site == 'ALL':
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', color="Booster Version Category", labels={'class':'Landing Success'},
        title='Payload and Landing Outcomes at All Sites') 
    else:
        filtered_df = filtered_df[filtered_df['Launch Site']==entered_site]
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', color="Booster Version Category", labels={'class':'Landing Success'},
        title=f'Payload and Landing Outcomes for Missions Launched at {entered_site}') 
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server()
