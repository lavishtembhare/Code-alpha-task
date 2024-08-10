import requests

API_KEY = 'your_financial_api_key_here'

portfolio = []

def get_stock_data(stock_symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_symbol}&interval=5min&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    
    if "Time Series (5min)" in data:
        latest_time = sorted(data['Time Series (5min)'].keys())[0]
        latest_price = float(data['Time Series (5min)'][latest_time]['4. close'])
        return {
            'symbol': stock_symbol,
            'latest_price': latest_price
        }
    else:
        return None

def add_stock():
    stock_symbol = input("Enter stock symbol: ").upper()
    quantity = int(input("Enter quantity: "))
    
    stock_data = get_stock_data(stock_symbol)
    
    if stock_data:
        portfolio.append({
            'symbol': stock_symbol,
            'quantity': quantity,
            'initial_price': stock_data['latest_price'],
            'current_price': stock_data['latest_price']
        })
        print(f"Stock {stock_symbol} added successfully!")
    else:
        print("Stock symbol not found!")

def remove_stock():
    stock_symbol = input("Enter stock symbol to remove: ").upper()
    global portfolio
    portfolio = [stock for stock in portfolio if stock['symbol'] != stock_symbol]
    print(f"Stock {stock_symbol} removed successfully!")

def view_portfolio():
    total_value = 0
    for stock in portfolio:
        stock_data = get_stock_data(stock['symbol'])
        if stock_data:
            stock['current_price'] = stock_data['latest_price']
            stock['value'] = stock['quantity'] * stock['current_price']
            stock['performance'] = (stock['current_price'] - stock['initial_price']) * stock['quantity']
            total_value += stock['value']
    
    print("\nCurrent Portfolio:")
    for stock in portfolio:
        print(f"Symbol: {stock['symbol']}, Quantity: {stock['quantity']}, "
              f"Initial Price: {stock['initial_price']}, Current Price: {stock['current_price']}, "
              f"Performance: {stock['performance']:.2f} USD")
    
    print(f"\nTotal Portfolio Value: {total_value:.2f} USD\n")

def menu():
    while True:
        print("\nStock Portfolio Manager")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_stock()
        elif choice == '2':
            remove_stock()
        elif choice == '3':
            view_portfolio()
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    menu()
