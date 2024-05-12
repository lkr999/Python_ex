from dash import Dash, html, dcc, Input, Output, callback

from datetime import date
import datetime
import qrcode

app = Dash(__name__)
app.layout = html.Div([
    dcc.DatePickerSingle(
        id='dpicker',
        min_date_allowed=date(1995, 8, 5),
        max_date_allowed=date(2050, 9, 19),
        initial_visible_month=date(2023, 11, 25),
        date=date(2023, 11, 25)
    ),
    html.Div(id='output-container-date-picker-single')
])

@callback(
    Output('output-container-date-picker-single', 'children'),
    Input('dpicker', 'date'))
def update_output(dpicker):
    string_prefix = 'You have selected: '
    DD = datetime.date(2023,10,31)
    EE = date(int(dpicker[:4]),int(dpicker[5:7]),int(dpicker[8:10]))

    print(DD,EE, dpicker, EE.today())

    if date is not None:
        date_object = date.fromisoformat(dpicker)
        date_string = date_object.strftime('%B %d, %Y')
        return string_prefix + date_string

if __name__ == '__main__':
    app.run(debug=False, port=8030)