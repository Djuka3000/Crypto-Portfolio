import matplotlib.pyplot as plt

class Plots :

    def plot_token_value_percentage(token_values):

        # Calculate total value
        total_value = sum(token_values.values())

        # Calculate percentages
        percentages = [value / total_value * 100 for value in token_values.values()]
        tokens = list(token_values.keys())

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.bar(tokens, percentages, color='green')
        plt.xlabel('Token')
        plt.ylabel('Percentage')
        plt.title('Tokennn Value Percentage Distribution')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

    def plot_token_value_percentage_as_pie(token_values):
    
        tokens = list(token_values.keys())
        values = list(token_values.values())

        plt.figure(figsize=(8, 8))
        plt.pie(values, labels=tokens, autopct='%1.1f%%', startangle=140)
        plt.title('Token Value Percentage Distribution')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()

    def plot_token_prices(token_prices):
    
        tokens = list(token_prices.keys())
        prices = list(token_prices.values())

        plt.figure(figsize=(10, 6))
        bars = plt.bar(tokens, prices, color='blue')
        plt.xlabel('Token')
        plt.ylabel('Price')
        plt.title('Token Prices')
        plt.xticks(rotation=45, ha='right')

        # Add prices as text on the bars
        for bar, price in zip(bars, prices):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{price:.2f}', ha='center', va='bottom')

        plt.tight_layout()
        plt.show()



    def plot_token_values(token_values):
    
        tokens = list(token_values.keys())
        values = list(token_values.values())

        plt.figure(figsize=(10, 6))
        plt.bar(tokens, values, color='blue')
        plt.xlabel('Token')
        plt.ylabel('Value')
        plt.title('Token Values')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

    
    def plot_address_portfolio_values(portfolio_values):
    
        addresses = list(portfolio_values.keys())
        values = list(portfolio_values.values())

        plt.figure(figsize=(10, 6))
        plt.bar(addresses, values, color='blue')
        plt.xlabel('Address')
        plt.ylabel('Portfolio Value')
        plt.title('Portfolio Value for Each Address')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()