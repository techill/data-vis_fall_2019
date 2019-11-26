# -*- coding: utf-8 -*-
import math

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('./employee_data.csv')
print(df.shape)
print(df.columns.values)

def get_barchart_data_cat(col_name):
    x = df[col_name].unique()
    # print(x.shape)
    y = []
    for i in x:
        y.append(df[df[col_name] == i].shape[0])
    return {'x': x, 'y': y, 'type': 'bar', 'name': col_name}


def get_piechart_data_cat(col_name):
    x = df[col_name].unique()
    # print(x.shape)
    y = []
    for i in x:
        y.append(df[df[col_name] == i].shape[0])
    return {'labels': x, 'values': y, 'type': 'pie', 'name': col_name}


def get_barchart_data_real(col_name,span):
    min = df[col_name].min() - 1
    max = df[col_name].max() + 1
    spans = math.ceil((max - min)/span)
    x = []
    interval_left = min
    interval_right = min + span
    y = []
    for i in range(0, spans):
        x.append(str(interval_left) + "~" + str(interval_right))
        y.append(df[ (df[col_name] >= interval_left) & (df[col_name] < interval_right)].shape[0])
        interval_left = interval_left + span
        interval_right = interval_right + span
    return {'x': x, 'y': y, 'type': 'bar', 'name': col_name}


def get_piechart_data_real(col_name,span):
    min = df[col_name].min() - 1
    max = df[col_name].max() + 1
    spans = math.ceil((max - min)/span)
    x = []
    interval_left = min
    interval_right = min + span
    y = []
    for i in range(0, spans):
        x.append(str(interval_left) + "~" + str(interval_right))
        y.append(df[ (df[col_name] >= interval_left) & (df[col_name] < interval_right)].shape[0])
        interval_left = interval_left + span
        interval_right = interval_right + span
    return {'labels': x, 'values': y, 'type': 'pie', 'name': col_name}


app.layout = html.Div(children=[
    html.H1(children='Hello Visionary Guys'),

     dcc.Graph(
        id='barchar-1',
        figure={
            'data': [
                get_barchart_data_cat('groups')
            ],
            'layout': {
                'title': 'Blood Groups Data'
            }
        }
    ),
    dcc.Graph(
        id='piechart-1',
        figure={
            'data': [
                get_piechart_data_cat('groups')
            ],
            'layout': {
                'title': 'Blood Groups Data'
            }
        }
    ),
    dcc.Graph(
        id='barchar-2',
        figure={
            'data': [
                get_barchart_data_cat('healthy_eating')
            ],
            'layout': {
                'title': 'Healthy_eating Data'
            }
        }
    ),
    dcc.Graph(
        id='piechart-2',
        figure={
            'data': [
                get_piechart_data_cat('healthy_eating')
            ],
            'layout': {
                'title': 'Healthy_eating Data'
            }
        }
    ),
    dcc.Graph(
        id='barchar-3',
        figure={
            'data': [
                get_barchart_data_cat('active_lifestyle')
            ],
            'layout': {
                'title': 'Active_lifestyle Data'
            }
        }
    ),
    dcc.Graph(
        id='piechar-3',
        figure={
            'data': [
                get_piechart_data_cat('active_lifestyle')
            ],
            'layout': {
                'title': 'Active_lifestyle Data'
            }
        }
    ),
    dcc.Graph(
        id='barchar-4',
        figure={
            'data': [
                get_barchart_data_real('age', 5)
            ],
            'layout': {
                'title': 'Age Data'
            }
        }
    ),
    dcc.Graph(
        id='piechar-4',
        figure={
            'data': [
                get_piechart_data_real('age', 5)
            ],
            'layout': {
                'title': 'Age Data'
            }
        }
    ),
    dcc.Graph(
        id='barchar-5',
        figure={
            'data': [
                get_barchart_data_real('salary', 200)
            ],
            'layout': {
                'title': 'Salary Data'
            }
        }
    ),
    dcc.Graph(
        id='piechar-5',
        figure={
            'data': [
                get_piechart_data_real('salary', 200)
            ],
            'layout': {
                'title': 'Salary Data'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)