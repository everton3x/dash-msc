import dash
import dash_bootstrap_components as dbc
import funcions
import datetime

select_uf = dbc.Select(
    id='select-uf',
    options=[dict(label=uf, value=uf) for uf in funcions.getUF()],
    value='RS'
)

select_entes = dbc.Select(
    id='select-entes',
    options=[dict(label=row['ente'], value=row['cod_ibge']) for _, row in funcions.getEntesPorUF('RS').iterrows()],
    value=4310405
)

select_exercicio = dbc.Input(
    id='select-exercicio',
    type='number',
    step=1,
    max=datetime.date.today().year,
    min=2013,
    value=datetime.date.today().year
)

button_search = dbc.Button("Pesquisar", id='button-search', color='primary', className='m-2', n_clicks=0)

search_bar = dbc.Row(
    [
        dbc.Col(select_uf, width='auto'),
        dbc.Col(select_entes, width='auto'),
        dbc.Col(select_exercicio, width='auto'),
        dbc.Col(button_search, width='auto')
    ],
    class_name='ms-auto flex-nowrap mt-3 mt-md-0',
    align='center'
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            dash.html.A(
                dbc.Row(
                    [
                        dbc.Col(dash.html.Img(
                            src='https://images.plot.ly/logo/new-branding/plotly-logomark.png',
                            height='30px'
                        )),
                        dbc.Col(dbc.NavbarBrand('Navbar', className='ms-2'), width='auto')
                    ],
                    align='center',
                    class_name='g-0',
                ),
                href='#',
                style={'textDecoration': 'none'},
            ),
            dbc.NavbarToggler(id='navbar-toggler', n_clicks=0),
            dbc.Collapse(
                search_bar,
                id='navbar-collapse',
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    color='dark',
    dark=True,
)

tab_resumo = dbc.Card(
    dbc.CardBody(
        dbc.Card([
            dbc.CardHeader('Município / UF', id='resumo-titulo'),
            dbc.CardBody([
                dbc.ListGroup([
                    dbc.ListGroupItem('População: 0', id='resumo-populacao')
                ])
            ]),
            dbc.CardFooter('Fonte dos dados: SICONFI')
        ]),
        class_name='mt-3'
    )
)

tab_doar = dbc.Card(
    [
        dbc.CardHeader('Demonstração das Origens e Aplicações dos Recursos'),
        dbc.CardBody(
            [
                dbc.Table([
                    dash.html.Thead(dash.html.Tr([
                        dash.html.Th('Origens'),
                        dash.html.Th('Valor', style={'text-align': 'right'}),
                        dash.html.Th('Aplicações'),
                        dash.html.Th('Valor', style={'text-align': 'right'})
                    ])),
                    dash.html.Tbody([
                        dash.html.Tr([
                            dash.html.Td('Tributos'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Legislativa'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                        dash.html.Tr([
                            dash.html.Td('Transferências'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Judiciária'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                        dash.html.Tr([
                            dash.html.Td('da União', style={'padding-left': '3em'}),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Essencial à justiça'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                        dash.html.Tr([
                            dash.html.Td('do Estado', style={'padding-left': '3em'}),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Administração'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                        dash.html.Tr([
                            dash.html.Td('do FUNDEB', style={'padding-left': '3em'}),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Defesa nacional'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                        dash.html.Tr([
                            dash.html.Td('de outras origens', style={'padding-left': '3em'}),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Segurança pública'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                        dash.html.Tr([
                            dash.html.Td('Exploração econômica, patrimonial e financeira'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Relações exteriores'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                        dash.html.Tr([
                            dash.html.Td('Operações de crédito'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Assistência social'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                        dash.html.Tr([
                            dash.html.Td('Alienação de bens'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Previdência social'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                        dash.html.Tr([
                            dash.html.Td('Amortização de empréstimos'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Saúde'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                        dash.html.Tr([
                            dash.html.Td('Outras origens'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Trabalho'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                        dash.html.Tr([
                            dash.html.Td(''),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Educação'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                        dash.html.Tr([
                            dash.html.Td(''),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Cultura'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                        dash.html.Tr([
                            dash.html.Td(''),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Direitos da cidadania'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                        dash.html.Tr([
                            dash.html.Td(''),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Urbanismo'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                        dash.html.Tr([
                            dash.html.Td(''),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Habitação'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                        dash.html.Tr([
                            dash.html.Td(''),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Saneamento'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                        dash.html.Tr([
                            dash.html.Td(''),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Gestão ambiental'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                        dash.html.Tr([
                            dash.html.Td(''),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Ciência e tecnologia'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                        dash.html.Tr([
                            dash.html.Td(''),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Agricultura'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                        dash.html.Tr([
                            dash.html.Td(''),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Organização agrária'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                        dash.html.Tr([
                            dash.html.Td(''),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Indústria'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                        dash.html.Tr([
                            dash.html.Td(''),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Comércio e serviços'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                        dash.html.Tr([
                            dash.html.Td(''),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Comunicações'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                        dash.html.Tr([
                            dash.html.Td(''),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Energia'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                        dash.html.Tr([
                            dash.html.Td(''),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Transporte'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                        dash.html.Tr([
                            dash.html.Td(''),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Desporto e lazer'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                        dash.html.Tr([
                            dash.html.Td(''),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                            dash.html.Td('Encargos especiais'),
                            dash.html.Td(funcions.to_moeda(0), style={'text-align': 'right'}),
                        ]),
                    ]),
                    dash.html.Tfoot(dash.html.Tr([
                        dash.html.Th('Total das Origens'),
                        dash.html.Th(funcions.to_moeda(0), style={'text-align': 'right'}),
                        dash.html.Th('Total das Aplicações'),
                        dash.html.Th(funcions.to_moeda(0), style={'text-align': 'right'}),
                    ]))
                ], bordered=True)
            ],
            # class_name='mt-3'
        )
    ]
)

tab_receita = dbc.Card(
    dbc.CardBody(
        [
            dash.html.P('Receita')
        ],
        class_name='mt-3'
    )
)

tab_despesa = dbc.Card(
    dbc.CardBody(
        [
            dash.html.P('Despesa')
        ],
        class_name='mt-3'
    )
)

tabpanel = dbc.Tabs(
    [
        dbc.Tab(tab_resumo, label='Resumo'),
        dbc.Tab(tab_doar, label='DOAR'),
        dbc.Tab(tab_receita, label='Receitas'),
        dbc.Tab(tab_despesa, label='Despesas'),
    ]
)