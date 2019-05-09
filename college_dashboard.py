import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import os

app = dash.Dash()

df_degrees_that_pay_back = pd.read_csv(os.path.join(os.getcwd(), "dataset", "college-salaries",
                                                    "degrees-that-pay-back.csv"))
df_salaries_by_college_type = pd.read_csv(os.path.join(os.getcwd(), "dataset", "college-salaries",
                                                       "salaries-by-college-type.csv"))
df_salaries_by_region = pd.read_csv(os.path.join(os.getcwd(), "dataset", "college-salaries",
                                                 "salaries-by-region.csv"))


degree_drop_down_list = df_degrees_that_pay_back.keys()[1:]

school_type_drop_down_list = df_salaries_by_college_type.keys()[2:]

school_types = df_salaries_by_college_type['School Type'].unique()

school_regions_drop_down_list_regions = df_salaries_by_region['Region'].unique()

school_regions_drop_down_list_salary_types = df_salaries_by_region.keys()[2:]

colors = {
    'background': '#111111',
    'text': '#000000',
    'bar-text': '#FFFFFF'
}

app.layout = html.Div([

    html.Div([
        html.H2(
            'Comparision Between Major',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),

        html.Div([
            html.Span(["y axis"]),
            dcc.Dropdown(
                id='degrees-drop-down-y',
                options=[{'label': i, 'value': i} for i in degree_drop_down_list],
                value='Starting Median Salary'
            )
        ],
        style={'width': '49%', 'display': 'inline-block'}),

        html.Div([
            html.Span(["x axis"]),
            dcc.Dropdown(
                id='degrees-drop-down-x',
                options=[{'label': i, 'value': i} for i in degree_drop_down_list],
                value='Mid-Career Median Salary'
            )
        ],
        style={'width': '49%', 'display': 'inline-block'})
        ],

        style={
        'borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)',
        'padding': '10px 5px'
    }),

    html.Div([
        dcc.Graph(
            id='degrees-scatter'
        )
    ], style={'width': '100%', 'display': 'inline-block', 'padding': '0 20'}),

    html.Br([]),
    html.Br([]),
    html.Br([]),

    html.Div([
        html.H2(
            'Comparision in each School Type',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),

        html.Div([
            html.Span(["y axis"]),
            dcc.Dropdown(
                id='school-types-drop-down-y',
                options=[{'label': i, 'value': i} for i in school_type_drop_down_list],
                value='Starting Median Salary'
            )
        ],
        style={'width': '32%', 'display': 'inline-block'}),

        html.Div([
            html.Span(["x axis"]),
            dcc.Dropdown(
                id='school-types-drop-down-x',
                options=[{'label': i, 'value': i} for i in school_type_drop_down_list],
                value='Mid-Career Median Salary'
            )
        ],
        style={'width': '32%', 'display': 'inline-block'}),

        html.Div([
            html.Span(["school type"]),
            dcc.Dropdown(
                id='school-types-drop-down-type',
                options=[{'label': i, 'value': i} for i in school_types],
                value='Engineering'
            )
        ],
        style={'width': '32%', 'display': 'inline-block'})
        ],
        style={
        'borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)',
        'padding': '10px 5px'
    }),

    html.Div([
        dcc.Graph(
            id='school-types-scatter'
        )
    ], style={'width': '100%', 'display': 'inline-block', 'padding': '0 20'}),

    html.Br([]),
    html.Br([]),
    html.Br([]),

    html.Div([
        html.H2(
            'Comparision in each School Region',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),

        html.Div([
            html.Span(["region"]),
            dcc.Dropdown(
                id='school-regions-drop-down-region',
                options=[{'label': i, 'value': i} for i in school_regions_drop_down_list_regions],
                value='California'
            )
        ],
        style={'width': '49%', 'display': 'inline-block'}),

        html.Div([
            html.Span(["salary type"]),
            dcc.Dropdown(
                id='school-regions-drop-down-region-salary-type',
                options=[{'label': i, 'value': i} for i in school_regions_drop_down_list_salary_types],
                value='Mid-Career Median Salary'
            )
        ],
        style={'width': '49%', 'display': 'inline-block'})
        ],
        style={
        'borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)',
        'padding': '10px 5px'
    }),

    html.Div([
        dcc.Graph(
            id='school-region-graph'
        )
    ], style={'width': '100%','height':'100%', 'display': 'inline-block', 'padding': '0 20'}),

    html.Br([]),
    html.Br([]),
    html.Br([]),
    html.Br([]),
    html.Br([]),
    html.Br([]),
])


app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})


@app.callback(
    dash.dependencies.Output('degrees-scatter', 'figure'),
    [dash.dependencies.Input('degrees-drop-down-x', 'value'),
     dash.dependencies.Input('degrees-drop-down-y', 'value')])
def update_degrees_graph(x_type, y_type):
    print(x_type, y_type)

    dff = df_degrees_that_pay_back

    traces = []
    for i in dff['Undergraduate Major'].unique():
        df_by_major = dff[dff['Undergraduate Major'] == i]
        traces.append(go.Scatter(
            x=df_by_major[x_type],
            y=df_by_major[y_type],
            text=df_by_major['Undergraduate Major'],
            mode='markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
        ))

    return {
        'data': traces,
        'layout': {
            "xaxis": {
                'title': x_type,
                'type': 'linear'
            },
            "yaxis": {
                'title': y_type,
                'type': 'linear'
            },
            "margin": {'l': 40, 'b': 30, 't': 10, 'r': 0},
            "height": 450,
            "hovermode": 'closest'
        }
    }


@app.callback(
    dash.dependencies.Output('school-types-scatter', 'figure'),
    [dash.dependencies.Input('school-types-drop-down-x', 'value'),
     dash.dependencies.Input('school-types-drop-down-y', 'value'),
     dash.dependencies.Input('school-types-drop-down-type', 'value')])
def update_school_types_graph(x_type, y_type, school_type):
    print(x_type, y_type, school_type)

    dff = df_salaries_by_college_type
    dff = dff[dff['School Type'] == school_type]
    traces = []
    for i in dff['School Name'].unique():
        df_by_school_name = dff[dff['School Name'] == i]
        traces.append(go.Scatter(
            x=df_by_school_name[x_type],
            y=df_by_school_name[y_type],
            text=df_by_school_name['School Name'],
            mode='markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
        ))

    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={
                'title': x_type,
                'type': 'linear'
            },
            yaxis={
                'title': y_type,
                'type': 'linear'
            },
            margin={'l': 40, 'b': 30, 't': 10, 'r': 0},
            height=450,
            hovermode='closest'
        )
    }


@app.callback(
    dash.dependencies.Output('school-region-graph', 'figure'),
    [dash.dependencies.Input('school-regions-drop-down-region', 'value'),
     dash.dependencies.Input('school-regions-drop-down-region-salary-type', 'value')])
def update_school_regions_graph(region, salary_type):
    dff = df_salaries_by_region[df_salaries_by_region['Region'] == region]
    print("regions")
    print(region, salary_type)
    y_data = dff[salary_type]
    x_data = dff['School Name'].unique()
    result = [
        {'x': x_data,
        'y': y_data,
        'type': 'bar',
        'name': 'regions'}
    ]
    print(result)
    return {
        'data': result,
        'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['bar-text']
                }
            }
    }

if __name__ == '__main__':
    app.run_server()