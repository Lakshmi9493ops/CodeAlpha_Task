# Stock Portfolio Tracker
# B.Tech student version - Simple & Clear

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 310,
    "AMZN": 125
}

portfolio = {}
total_investment = 0

print("Welcome to the Stock Portfolio Tracker!\n")
print("Available Stocks:", ', '.join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
    
    if stock == 'DONE':
        break

    if stock not in stock_prices:
        print("Sorry, stock not available in the price list.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity
    investment = quantity * stock_prices[stock]
    total_investment += investment
    print(f"Added {quantity} shares of {stock} worth ${investment}")

# Display Portfolio Summary
print("\n--- Portfolio Summary ---")
for stock, quantity in portfolio.items():
    value = quantity * stock_prices[stock]
    print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment: ${total_investment}")

# Ask user if they want to save the result
save = input("\nDo you want to save this summary to a file? (yes/no): ").lower()

if save == 'yes':
    filename = "portfolio_summary.txt"
    with open(filename, 'w') as file:
        file.write("Portfolio Summary:\n")
        for stock, quantity in portfolio.items():
            value = quantity * stock_prices[stock]
            file.write(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}\n")
        file.write(f"\nTotal Investment: ${total_investment}")
    print(f"Summary saved to {filename}")

print("\nThank you for using the Stock Portfolio Tracker!")
