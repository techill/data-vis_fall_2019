# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('./employee_data.csv')
print(df.shape)
print(df.columns.values)


def get_figure_1():
    filtered_df = df
    traces = []
    for i in filtered_df.groups.unique():
        df_by_groups = filtered_df[filtered_df['groups'] == i]
        traces.append(go.Scatter(
            x=df_by_groups['age'],
            y=df_by_groups['salary'],
            text=df_by_groups['healthy_eating'],
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
            xaxis={'type': 'log', 'title': 'age '},
            yaxis={'title': 'Salary', 'range': [df['salary'].min()*0.5, df['salary'].max()*1.5]},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }


def get_figure_2():
    filtered_df = df
    traces = []
    for i in filtered_df.groups.unique():
        df_by_groups = filtered_df[filtered_df['groups'] == i]
        traces.append(go.Scatter(
            x=df_by_groups['age'],
            y=df_by_groups['healthy_eating'],
            text=df_by_groups['healthy_eating'],
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
            xaxis={'type': 'log', 'title': 'age '},
            yaxis={'title': 'Healthy Eating', 'range': [df['healthy_eating'].min(), df['healthy_eating'].max()]},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }


def get_figure_3():
    filtered_df = df
    traces = []
    df_by_groups = filtered_df
    traces.append(go.Scatter(
        x=df_by_groups['active_lifestyle'],
        y=df_by_groups['healthy_eating'],
        text=df_by_groups['healthy_eating'],
        mode='markers',
        opacity=0.7,
        marker={
            'size': 15,
            'line': {'width': 0.5, 'color': 'white'}
        },
        name='all group'
    ))
    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'type': 'log', 'title': 'active_lifestyle ', },
            yaxis={'title': 'Healthy Eating', 'range': [df['healthy_eating'].min(), df['healthy_eating'].max()]},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }


app.layout = html.Div(children=[
    html.H1(children='Hello Visionary Guys'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    html.Div([
        dcc.Dropdown(
            id='attributes',
            options=[{'label': i, 'value': i} for i in df.columns.values],
            value=df.columns.values[0]
        )
    ], style={'width': '48%', 'display': 'inline-block'}),
    dcc.Graph(
        id='graph-scatter-1',
        figure=get_figure_1()
    ),
    dcc.Graph(
        id='graph-scatter-2',
        figure=get_figure_2()
    ),
    dcc.Graph(
        id='graph-scatter-3',
        figure=get_figure_3()
    )
 ])





if __name__ == '__main__':
    app.run_server(debug=True)