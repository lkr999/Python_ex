import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# 데이터 로드
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

# Dash 앱 인스턴스 생성
app = dash.Dash(__name__)

# 레이아웃 생성
app.layout = html.Div([
    # 그래프 구성 요소
    dcc.Graph(id='graph-with-slider'),

    # 슬라이더 구성 요소
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    )
])



# 그래프 출력 업데이트 함수 (콜백 데코레이터)
@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    # 슬라이더 'value' 값에 따라 DataFrame 업데이트
    filtered_df = df[df.year == selected_year]

    # Scatter 그래프 생성
    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=55)

    # Scatter 그래프 업데이트
    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    # Dash 앱 실행
    app.run_server(debug=True)
