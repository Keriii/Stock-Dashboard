from dash import Input, Output, State
import plotly.graph_objects as go
from dash import html
import plotly.express as px

def register_callbacks(app, stock_manager):
    @app.callback(
        [Output('main-chart', 'figure'),
         Output('volume-chart', 'figure'),
         Output('technical-chart', 'figure'),
         Output('rsi-chart', 'figure'),
         Output('macd-chart', 'figure'),
         Output('stock-info-cards', 'children')],
        [Input('stock-selector', 'value'),
         Input('timeframe-selector', 'value'),
         Input('interval-selector', 'value')]
    )
    def update_charts(symbol, timeframe, interval):
        df = stock_manager.get_stock_data(symbol, timeframe, interval)
        info = stock_manager.get_stock_info(symbol)
        
        return (
            create_candlestick_chart(df, symbol),
            create_volume_chart(df),
            create_technical_chart(df),
            create_rsi_chart(df),
            create_macd_chart(df),
            create_info_cards(info)
        )

    @app.callback(
        Output('price-analysis-output', 'children'),
        [Input('analyze-button', 'n_clicks')],
        [State('price-input', 'value'),
         State('stock-selector', 'value')]
    )
    def analyze_price(n_clicks, input_price, symbol):
        if not n_clicks or not input_price:
            return ""
        
        df = stock_manager.get_stock_data(symbol, period='1mo', interval='1d')
        if df.empty:
            return html.Div("Error fetching data", className="alert-negative")
        
        current_price = df['Close'].iloc[-1]
        price_diff = ((input_price - current_price) / current_price) * 100
        
        if price_diff > 0:
            return html.Div([
                html.P(f"Target price is {abs(price_diff):.2f}% above current price"),
                html.P(f"Current Price: ${current_price:.2f}"),
                html.P(f"Target Price: ${input_price:.2f}")
            ], className="alert-positive")
        else:
            return html.Div([
                html.P(f"Target price is {abs(price_diff):.2f}% below current price"),
                html.P(f"Current Price: ${current_price:.2f}"),
                html.P(f"Target Price: ${input_price:.2f}")
            ], className="alert-negative")

    @app.callback(
        Output('alert-output', 'children'),
        [Input('set-alert-button', 'n_clicks')],
        [State('alert-price', 'value'),
         State('alert-type', 'value'),
         State('stock-selector', 'value')]
    )
    def set_price_alert(n_clicks, target_price, alert_type, symbol):
        if not n_clicks or not target_price:
            return ""
        
        df = stock_manager.get_stock_data(symbol, period='1d', interval='1d')
        if df.empty:
            return html.Div("Error fetching data", className="alert-negative")
        
        current_price = df['Close'].iloc[-1]
        
        return html.Div([
            html.P(f"Alert set for {symbol}"),
            html.P(f"Current Price: ${current_price:.2f}"),
            html.P(f"Alert when price goes {alert_type} ${target_price:.2f}")
        ], className="alert-positive")

def create_candlestick_chart(df, symbol):
    fig = go.Figure(data=[
        go.Candlestick(
            x=df['Date'],
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close'],
            name=symbol
        )
    ])
    
    # Add SMA lines
    fig.add_trace(go.Scatter(
        x=df['Date'],
        y=df['SMA_20'],
        name='SMA 20',
        line=dict(color='orange')
    ))
    
    fig.add_trace(go.Scatter(
        x=df['Date'],
        y=df['SMA_50'],
        name='SMA 50',
        line=dict(color='blue')
    ))
    
    fig.update_layout(
        title=f'{symbol} Stock Price',
        yaxis_title='Price',
        xaxis_title='Date'
    )
    
    return fig

def create_volume_chart(df):
    fig = go.Figure(data=[
        go.Bar(
            x=df['Date'],
            y=df['Volume'],
            name='Volume'
        )
    ])
    
    fig.update_layout(
        title='Trading Volume',
        yaxis_title='Volume',
        xaxis_title='Date'
    )
    
    return fig

def create_technical_chart(df):
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df['Date'],
        y=df['Close'],
        name='Close Price'
    ))
    
    fig.add_trace(go.Scatter(
        x=df['Date'],
        y=df['SMA_20'],
        name='SMA 20'
    ))
    
    fig.add_trace(go.Scatter(
        x=df['Date'],
        y=df['SMA_50'],
        name='SMA 50'
    ))
    
    fig.update_layout(
        title='Technical Indicators',
        yaxis_title='Price',
        xaxis_title='Date'
    )
    
    return fig

def create_rsi_chart(df):
    fig = go.Figure(data=[
        go.Scatter(
            x=df['Date'],
            y=df['RSI'],
            name='RSI'
        )
    ])
    
    # Add overbought/oversold lines
    fig.add_hline(y=70, line_dash="dash", line_color="red")
    fig.add_hline(y=30, line_dash="dash", line_color="green")
    
    fig.update_layout(
        title='Relative Strength Index (RSI)',
        yaxis_title='RSI',
        xaxis_title='Date'
    )
    
    return fig

def create_macd_chart(df):
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df['Date'],
        y=df['MACD'],
        name='MACD'
    ))
    
    fig.add_trace(go.Scatter(
        x=df['Date'],
        y=df['Signal_Line'],
        name='Signal Line'
    ))
    
    fig.update_layout(
        title='MACD',
        yaxis_title='Value',
        xaxis_title='Date'
    )
    
    return fig

def create_info_cards(info):
    # First row of cards
    row1 = html.Div([
        create_metric_card("Company", info.get('name', 'N/A')),
        create_metric_card("Sector", info.get('sector', 'N/A')),
        create_metric_card("Industry", info.get('industry', 'N/A')),
    ], className="row mb-4")  # Added margin bottom for spacing between rows

    # Second row of cards
    row2 = html.Div([
        create_metric_card("Market Cap", f"${info.get('market_cap', 0):,.0f}"),
        create_metric_card("P/E Ratio", f"{info.get('pe_ratio', 0):.2f}"),
        create_metric_card("Dividend Yield", f"{info.get('dividend_yield', 0):.2%}")
    ], className="row")

    return [
        html.Div([row1, row2], className="container-fluid")  # Added container-fluid for full width
    ]

def create_metric_card(title, value):
    return html.Div([
        html.Div([
            html.H6(title, className="card-subtitle text-muted metric-title"),
            html.H4(value, className="card-title metric-value")
        ], className="card-body")
    ], className="col-md-4 card stock-card")