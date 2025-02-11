from dash import Dash
from layouts.main_layout import create_layout
from callbacks.callbacks import register_callbacks
from data.stock_data import StockDataManager

def create_app():
    # Initialize Dash app with external Bootstrap CSS
    app = Dash(__name__, 
               external_stylesheets=[
                   'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css'
               ])
    
    # Initialize stock data manager
    stock_manager = StockDataManager()
    
    # Set up layout
    app.layout = create_layout(stock_manager)
    
    # Register callbacks
    register_callbacks(app, stock_manager)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run_server(debug=True) 