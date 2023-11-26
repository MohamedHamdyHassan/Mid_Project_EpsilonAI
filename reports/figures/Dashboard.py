import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
from dash import Dash,html,dcc,callback
from dash.dependencies import Input,Output,State


raw_df=pd.read_csv('../data/processed/EDA & Cleaning.csv')
df=raw_df.copy()
# Create Dash app
app = Dash()

fig1 = ff.create_distplot([df.age.to_list()], ['age'], show_rug=False)
fig1.update_layout(title_text='Distribution of the Age')
fig1.update_xaxes(title_text='Age')
fig1.update_yaxes(title_text='Frequency')

fig2 = px.histogram(df, x='age', facet_col='diagnosis')
fig2.update_layout(title='Highest Age through Glaucoma')

fig4 = px.histogram(df, x='family_history', y='patient_id', color='gender', histfunc='count',
                    color_discrete_sequence=px.colors.qualitative.Set1,
                    title='Count of Patients Grouped by Family History and Gender', text_auto=True,
                    labels={'family_history': 'Family History', 'count': 'Patient Count'})

fig5 = px.histogram(df, x='medical_history', facet_col='gender', text_auto=True, title='Highest Gender in Medical History')
fig5.update_yaxes(title_text='Patients Count')

fig_pie = px.pie(df, names='diagnosis', title='The Weight of Diagnosis',
                 color_discrete_sequence=px.colors.qualitative.Set1)
fig_pie.update_traces(textinfo='value+percent')

gender_options = [{'label': gender, 'value': gender} for gender in df['gender'].unique()]
diagnosis_options = [{'label': diagnosis, 'value': diagnosis} for diagnosis in df['diagnosis'].unique()]

app.layout = html.Div(style={'textAlign': 'center'}, children=[
    html.H1("Interactive Healthcare Dashboard"),

    html.Div([
        # Dropdown for gender
        dcc.Dropdown(
            id='gender-dropdown',
            options=gender_options,
            value=df['gender'].unique()[0], 
            style={'width': '50%'}
        ),

        # Dropdown for diagnosis
        dcc.Dropdown(
            id='diagnosis-dropdown',
            options=diagnosis_options,
            value=df['diagnosis'].unique()[0],
            style={'width': '50%'}
        ),
    ], style={'display': 'flex', 'justifyContent': 'center', 'margin': '20px'}),

    html.Div([
        # Distribution plot
        dcc.Graph(
            id='distplot',
            figure=fig1,
        ),
        # Histogram plot
        dcc.Graph(
            id='histogram',
            figure=fig2,
        ),
    ], style={'display': 'flex', 'justifyContent': 'space-around', 'margin': '20px'}),

    html.Div([
        # Additional Histogram plot (fig4)
        dcc.Graph(
            id='histogram-family-gender',
            figure=fig4,
        ),
        # Histogram plot for medical history by gender (fig5)
        dcc.Graph(
            id='histogram-medical-history',
            figure=fig5,
        ),
    ], style={'display': 'flex', 'justifyContent': 'space-around', 'margin': '20px'}),

    html.Div([
        # Pie chart for diagnosis (fig_pie)
        dcc.Graph(
            id='pie-chart-diagnosis',
            figure=fig_pie,
        ),
    ], style={'margin': '20px'}),

])


# Callbacks
@app.callback(
    Output('histogram-family-gender', 'figure'),
    [Input('gender-dropdown', 'value')]
)
def update_gender_histogram(selected_gender):
    filtered_df = df[(df['gender'] == selected_gender) & (df['diagnosis'] == app.layout['diagnosis-dropdown'].value)]
    updated_fig = px.histogram(filtered_df, x='family_history', y='patient_id', color='gender', histfunc='count',
                               color_discrete_sequence=px.colors.qualitative.Set1,
                               title=f'Count of Patients with Gender: {selected_gender}',
                               text_auto=True, labels={'family_history': 'Family History', 'count': 'Patient Count'})
    return updated_fig


@app.callback(
    Output('histogram-medical-history', 'figure'),
    [Input('gender-dropdown', 'value')]
)
def update_medical_history_histogram(selected_gender):
    filtered_df = df[(df['gender'] == selected_gender) & (df['diagnosis'] == app.layout['diagnosis-dropdown'].value)]
    updated_fig = px.histogram(filtered_df, x='medical_history', facet_col='gender', text_auto=True,
                               title=f'Highest Gender in Medical History for {selected_gender}')
    updated_fig.update_yaxes(title_text='Patients Count')
    return updated_fig


@app.callback(
    Output('distplot', 'figure'),
    [Input('gender-dropdown', 'value'), Input('diagnosis-dropdown', 'value')]
)
def update_distribution_plot(selected_gender, selected_diagnosis):
    filtered_df = df[(df['gender'] == selected_gender) & (df['diagnosis'] == selected_diagnosis)]
    updated_fig = ff.create_distplot([filtered_df.age.to_list()], ['age'], show_rug=False, colors=colors)
    updated_fig.update_layout(title_text='Distribution of the Age')
    updated_fig.update_xaxes(title_text='Age')
    updated_fig.update_yaxes(title_text='Frequency')
    return updated_fig


@app.callback(
    Output('histogram', 'figure'),
    [Input('diagnosis-dropdown', 'value')]
)
def update_diagnosis_histogram(selected_diagnosis):
    filtered_df = df[df['diagnosis'] == selected_diagnosis]
    updated_fig = px.histogram(filtered_df, x='age', facet_col='diagnosis')
    updated_fig.update_layout(title=f'Highest Age through {selected_diagnosis}')
    return updated_fig


@app.callback(
    Output('pie-chart-diagnosis', 'figure'),
    [Input('diagnosis-dropdown', 'value')]
)
def update_pie_chart(selected_diagnosis):
    filtered_df = df[df['diagnosis'] == selected_diagnosis]
    updated_fig = px.pie(filtered_df, names='diagnosis', title=f'The Weight of {selected_diagnosis}',
                         color_discrete_sequence=px.colors.qualitative.Set1)
    updated_fig.update_traces(textinfo='value+percent')
    return updated_fig


app.run(jupyter_mode = 'external',port=1500)