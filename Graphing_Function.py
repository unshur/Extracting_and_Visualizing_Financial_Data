def make_graph(stock_data, revenue_data, stock):
    
    """
    Create a two-subplot graph displaying historical share price and revenue data.

    This function takes historical stock price and revenue data, along with a stock name, and creates a two-subplot
    graph to visualize the historical share price and revenue over time. The two subplots share the same x-axis and
    are arranged vertically. The historical data is filtered to include only records up to specific dates for both
    stock price and revenue.

    Parameters:
    - stock_data (DataFrame): A DataFrame containing historical stock price data, including 'Date' and 'Close' columns.
    - revenue_data (DataFrame): A DataFrame containing historical revenue data, including 'Date' and 'Revenue' columns.
    - stock (str): The name of the stock, which will be used as the graph's title.

    Returns:
    - None: The function displays the graph but does not return any value.

    Example Usage:
    >>> make_graph(stock_price_df, revenue_df, "Company XYZ")
    """
    
    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        subplot_titles=("Historical Share Price", "Historical Revenue"),
        vertical_spacing=.3
    )
    
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    
    fig.add_trace(
        go.Scatter(
            x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True),
            y=stock_data_specific.Close.astype("float"),
            name="Share Price"
        ), 
        row=1,
        col=1
    )
    
    fig.add_trace(
        go.Scatter(
            x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True),
            y=revenue_data_specific.Revenue.astype("float"),
            name="Revenue"
        ),
        row=2,
        col=1
    )
    
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    
    fig.update_layout(
        showlegend=False,
        height=900,
        title=stock,
        xaxis_rangeslider_visible=True
    )
    
    fig.show()