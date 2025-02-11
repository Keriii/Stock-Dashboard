# Layouts Directory

Contains the UI layout components and structure for the dashboard. This directory handles all visual elements and their organization.

## Files

### main_layout.py

Main layout file that defines the complete dashboard structure:

#### Components Structure

```
create_layout
├── Header Section
│   └── Dashboard Title
├── Filter Section
│   ├── Stock Symbol Selector
│   ├── Time Period Selector
│   └── Interval Selector
├── Stock Info Section
│   ├── Company Info Cards (Row 1)
│   └── Market Data Cards (Row 2)
├── Chart Section
│   ├── Main Candlestick Chart
│   ├── Volume Chart
│   └── Technical Chart
├── Analysis Section
│   ├── Price Analysis Tool
│   │   ├── Price Input
│   │   └── Analysis Results
│   └── Alert System
│       ├── Target Price Input
│       ├── Alert Type Selection
│       └── Alert Status
└── Technical Analysis Section
    ├── RSI Chart
    └── MACD Chart
```

## Component Details

### 1. Filter Section (`create_filters`)

- Stock symbol dropdown with default options
- Time period selector (1D to 5Y)
- Interval selector (5m to 1d)
- Bootstrap grid layout (col-md-4 for each)

### 2. Stock Info Section (`create_stock_info_section`)

- Responsive card layout
- Three cards per row
- Dynamic data display
- Neumorphic design with hover effects

### 3. Chart Section (`create_charts`)

```python
html.Div([
    # Main Chart (Full Width)
    html.Div([
        dcc.Graph(id='main-chart')
    ], className="col-12"),

    # Secondary Charts (Half Width Each)
    html.Div([
        dcc.Graph(id='volume-chart')
    ], className="col-md-6"),
    html.Div([
        dcc.Graph(id='technical-chart')
    ], className="col-md-6")
])
```

### 4. Analysis Section (`create_analysis_section`)

- Price analysis tool
  - Numeric input for target price
  - Analysis button
  - Results display
- Alert system
  - Price input
  - Above/Below selection
  - Alert status display

### 5. Technical Analysis Section (`create_technical_analysis_section`)

- RSI chart with overbought/oversold levels
- MACD chart with signal line
- Responsive two-column layout

## Styling

- Uses Bootstrap grid system
- Custom CSS classes from assets/style.css
- Responsive design breakpoints
- Consistent spacing and margins

## Class Usage

Common CSS classes used:

```css
.container-fluid  /* Full-width container */
/* Full-width container */
.row             /* Bootstrap row */
.col-md-*        /* Responsive columns */
.mb-4            /* Margin bottom */
.stock-card      /* Custom card styling */
.alert-section   /* Alert messages */
.input-section; /* Input areas */
```

## Best Practices

1. **Component Organization**

   - Modular function structure
   - Clear component hierarchy
   - Logical grouping of elements

2. **Responsive Design**

   - Mobile-first approach
   - Flexible layouts
   - Bootstrap grid utilization

3. **User Experience**

   - Intuitive layout flow
   - Consistent spacing
   - Clear visual hierarchy

4. **Code Structure**
   - Component reusability
   - Clear function naming
   - Comprehensive comments

## Usage Example

```python
from layouts.main_layout import create_layout

def create_app():
    app = Dash(__name__)
    app.layout = create_layout(stock_manager)
    return app
```

## Dependencies

- dash.html (HTML components)
- dash.dcc (Core components)
- Bootstrap (Grid system and basic styling)
- Custom CSS (assets/style.css)
