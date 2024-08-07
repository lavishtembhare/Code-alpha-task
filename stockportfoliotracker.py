import yfinance as yf

portfolio = {}

def get_stock_price(symbol):
    stock = yf.Ticker(symbol)
    stock_info = stock.history(period='1d')
    if not stock_info.empty:
        return stock_info['Close'].iloc[-1]
    else:
        print(f"Error fetching data for {symbol}")
        return None

def add_stock(symbol, shares):
    if symbol in portfolio:
        portfolio[symbol] += shares
    else:
        portfolio[symbol] = shares

def remove_stock(symbol, shares):
    if symbol in portfolio:
        if portfolio[symbol] > shares:
            portfolio[symbol] -= shares
        elif portfolio[symbol] == shares:
            del portfolio[symbol]
        else:
            print(f"Cannot remove {shares} shares. Only {portfolio[symbol]} shares available.")
    else:
        print(f"{symbol} not found in portfolio.")

def display_portfolio():
    print("Your portfolio:")
    for symbol, shares in portfolio.items():
        price = get_stock_price(symbol)
        if price:
            value = price * shares
            print(f"{symbol}: {shares} shares at ${price:.2f} each, total value: ${value:.2f}")

def main():
    while True:
        print("\n1. Add Stock\n2. Remove Stock\n3. Display Portfolio\n4. Quit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            add_stock(symbol, shares)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            remove_stock(symbol, shares)
        elif choice == '3':
            display_portfolio()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
