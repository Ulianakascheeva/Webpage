import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets_link = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets_link)

colors = {
    'background': '#FFFFFF',
    'text': '#000000',
    'answers': '#FF0000'
}

app.layout = html.Div(children=[
    html.Img(src='https://sun9-25.userapi.com/c851324/v851324328/12d06/KaOgrdRhRAA.jpg', style={
        'height': '94vh',
        'maxWidth': '100%',
        'margin': 0,
        'textAlign': 'center'
    }),
    
    html.H4('Кащеева Ульяна'),
    html.P('Художник, дизайнер'),
    html.P('Разрабатываю иллюстрации для книг'),
    html.P('Биоинформатик, анализирую геном Covid-19 (SARS COV2)'),
    html.H6('Образование'),
    html.P('НИУ ВШЭ, Факультет Биологии и Биотехнологии'),
    html.P('Лицей «Вторая школа»'),
    html.P('СУНЦ МГУ'),
    
    html.Div([
        html.H6('Какое у тебя любимое число?'),
        dcc.Input(id='input-number-id', value="", type='text'),
        html.Div(id='output-number-id', style={
            'color': colors['answers']
        })
    ])
], style={'columnCount':2})

@app.callback(
    Output(component_id='output-number-id', component_property='children'),
    [Input(component_id='input-number-id', component_property='value')]
)

def update_output_div(input_value):
    if input_value=='':
        return ''
    else:
        return 'Как здорово, {} - и моё любимое число!'.format(input_value)

if __name__ == '__main__':
    app.run_server(debug=False)