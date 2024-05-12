import dash_bootstrap_components as dbc
import dash_bootstrap_components.themes
from dash import html
import dash
from dash import Input, Output, State, html, dcc, dash_table, MATCH, ALL, ctx

app = dash.Dash(external_stylesheets=[dash_bootstrap_components.themes.DARKLY])


row = html.Div(
    [
        dbc.Row(dbc.Col(html.Div("A single column"))),
        dbc.Row(
            [
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
            ]
        ),
    ]
)

row2 = html.Div(
    [
        dbc.Row(dbc.Col(html.Div("A single column"))),
        dbc.Row(
            [
                dbc.Col(html.Div("One of four columns")),
                dbc.Col(html.Div("One of four columns")),
                dbc.Col(html.Div("One of four columns")),
                dbc.Col(html.Div("One of four columns")),
            ]
        ),
    ]
)


badge = dbc.Button(
    [
        "Notifications",
        dbc.Badge("4", color="orange", text_color="primary", className="ms-1"),
    ],
    color="blue",
)

button_group = html.Div(
    [
        dbc.RadioItems(
            id="radios",
            className="btn-group",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "Option 1", "value": 1},
                {"label": "Option 2", "value": 2},
                {"label": "Option 3", "value": 3},
            ],
            value=1,
        ),
        html.Div(id="output"),
    ],
    className="radio-group",
)

app.layout = dbc.Container(button_group)

@app.callback(
    Output("output", "children"),
    Input("radios", "value")
)
def display_value(value):
    return f"Selected value: {value}"

if __name__ == "__main__":
    app.run_server(debug=True)