import dash
import dash_bootstrap_components as dbc
import components
import funcions

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

server = app.server

@app.callback(
    dash.Output('navbar-collapse', 'is_open'),
    [dash.Input('navbar-toggler', 'n_clicks')],
    [dash.State('navbar-collapse', 'is_open')],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    dash.Output('select-entes', 'options'),
    dash.Input('select-uf', 'value')
)
def update_selector_ente(uf):
    if uf is None:
        raise dash.exceptions.PreventUpdate
    else:
        entes = [dict(label=row['ente'], value=row['cod_ibge']) for _, row in funcions.getEntesPorUF(uf).iterrows()]
        return entes

@app.callback(
    # dash.Output('log-panel', 'children'),
    dash.Output('resumo-titulo', 'children'),
    dash.Output('resumo-populacao', 'children'),
    dash.Input('button-search', 'n_clicks'),
    dash.State('select-entes', 'value'),
)
def button_search_on_click(n_clicks, cod_ibge):
    if n_clicks is None:
        dash.exceptions.PreventUpdate
    else:
        ente = funcions.getEntePorCodigoIbge(cod_ibge)
        nome = ente['ente']
        uf = ente['uf']
        populacao = ente['populacao']
        return f'{nome} / {uf}', 'População: ' + funcions.numero_inteiro(populacao) + ' habitantes'

app.layout = dbc.Container(
    [
        components.navbar,
        components.tabpanel,
        # dash.html.Div(id='log-panel')
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)