from dash import html, dcc, Input, Output, State
import plotly.graph_objects as go

def create_layout(stock_manager):
    return html.Div([        
        # Header
        html.Div([
            html.H1("Advanced Stock Market Dashboard", className="text-center mb-4"),
        ], className="container-fluid bg-light p-3"),
        
        # Main content
        html.Div([
            create_filters(stock_manager),  # Input components
            create_stock_info_section(),    # Info cards
            create_charts(),                # Charts
            create_analysis_section(),      # Analysis tools
            create_technical_analysis_section()  # Technical indicators
        ])
    ])

def create_filters(stock_manager):
    return html.Div([
        html.Div([
            # Stock Symbol Selector
            html.Div([
                html.Label("Stock Symbol:"),
                dcc.Dropdown(
                    id='stock-selector',
                    options=[{'label': symbol, 'value': symbol} 
                            for symbol in stock_manager.default_stocks],
                    value='AAPL',
                    className="mb-3"
                )
            ], className="col-md-4"),
            
            # Time Period Selector
            html.Div([
                html.Label("Time Period:"),
                dcc.Dropdown(
                    id='timeframe-selector',
                    options=[
                        {'label': '1 Day', 'value': '1d'},
                        {'label': '5 Days', 'value': '5d'},
                        {'label': '1 Month', 'value': '1mo'},
                        {'label': '3 Months', 'value': '3mo'},
                        {'label': '1 Year', 'value': '1y'},
                        {'label': '5 Years', 'value': '5y'}
                    ],
                    value='1y',
                    className="mb-3"
                )
            ], className="col-md-4"),
            
            # Interval Selector
            html.Div([
                html.Label("Interval:"),
                dcc.Dropdown(
                    id='interval-selector',
                    options=[
                        {'label': '1 Day', 'value': '1d'},
                        {'label': '1 Hour', 'value': '1h'},
                        {'label': '15 Minutes', 'value': '15m'},
                        {'label': '5 Minutes', 'value': '5m'},
                    ],
                    value='1d',
                    className="mb-3"
                )
            ], className="col-md-4")
        ], className="row mb-4")
    ])

def create_stock_info_section():
    return html.Div([
        # Add stock-card class to see the neumorphic effect
        html.Div(id='stock-info-cards', className="stock-card row mb-4")
    ])

def create_charts():
    return html.Div([
        # Main Chart Row
        html.Div([
            html.Div([
                dcc.Graph(id='main-chart')
            ], className="col-12")
        ], className="row mb-4"),
        
        # Volume and Technical Indicators
        html.Div([
            html.Div([
                dcc.Graph(id='volume-chart')
            ], className="col-md-6"),
            
            html.Div([
                dcc.Graph(id='technical-chart')
            ], className="col-md-6")
        ], className="row")
    ])

def create_analysis_section():
    return html.Div([
        html.H3("Stock Analysis Tools", className="mb-3"),
        html.Div([
            # Manual Price Entry Analysis
            html.Div([
                html.Label("Enter Stock Price for Analysis:"),
                dcc.Input(
                    id='price-input',
                    type='number',
                    placeholder='Enter price...',
                    className="form-control mb-2"
                ),
                html.Button(
                    'Analyze Price', 
                    id='analyze-button',
                    className="analysis-button mb-3"
                ),
                html.Div(id='price-analysis-output', className="alert-section")
            ], className="col-md-6"),
            
            # Price Alert Setup
            html.Div([
                html.Label("Set Price Alerts:"),
                dcc.Input(
                    id='alert-price',
                    type='number',
                    placeholder='Target price...',
                    className="form-control mb-2"
                ),
                dcc.RadioItems(
                    id='alert-type',
                    options=[
                        {'label': ' Above ', 'value': 'above'},
                        {'label': ' Below ', 'value': 'below'}
                    ],
                    value='above',
                    className="mb-2"
                ),
                html.Button(
                    'Set Alert', 
                    id='set-alert-button',
                    className="analysis-button"
                ),
                html.Div(id='alert-output', className="alert-section")
            ], className="col-md-6")
        ], className="row input-section")
    ])

def create_technical_analysis_section():
    return html.Div([
        html.H3("Technical Analysis", className="mb-3"),
        html.Div([
            html.Div([
                dcc.Graph(id='rsi-chart')
            ], className="col-md-6"),
            
            html.Div([
                dcc.Graph(id='macd-chart')
            ], className="col-md-6")
        ], className="row mb-4")
    ]) 