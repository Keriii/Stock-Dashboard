# Callbacks Directory

Contains callback functions that handle the interactive elements of the dashboard.

## Files

### callbacks.py

Main callback definitions including:

- Chart updates
- Price analysis
- Alert system
- Technical indicator calculations

## Callback Patterns

1. **Chart Updates**

   - Triggered by symbol/timeframe selection
   - Updates multiple charts simultaneously
   - Handles data fetching and processing

2. **Price Analysis**

   - Button-triggered analysis
   - Uses State to prevent unnecessary updates
   - Provides formatted feedback

3. **Alert System**
   - Custom price alerts
   - Above/below price triggers
   - Real-time price comparison

## Best Practices

- Use State for form-like interactions
- Group related callbacks
- Handle errors gracefully
- Optimize for performance
