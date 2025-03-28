from collections import deque

class OrderBook:
    def __init__(self):
        self.bids = deque()  # List of buy orders (sorted by price descending)
        self.asks = deque()  # List of sell orders (sorted by price ascending)

    def add_order(self, price, quantity, side):
        order = {'price': price, 'quantity': quantity}
        if side == 'buy':
            self.bids.append(order)
            self.bids = deque(sorted(self.bids, key=lambda x: -x['price']))  # Sort high to low
        else:
            self.asks.append(order)
            self.asks = deque(sorted(self.asks, key=lambda x: x['price']))  # Sort low to high

    def match_orders(self):
        while self.bids and self.asks and self.bids[0]['price'] >= self.asks[0]['price']:
            bid = self.bids.popleft()
            ask = self.asks.popleft()
            trade_price = (bid['price'] + ask['price']) / 2
            trade_quantity = min(bid['quantity'], ask['quantity'])
            print(f"Trade executed: {trade_quantity} units at {trade_price}")

    def output(self):
        print("\nCurrent order book:")
        print("Bids (Buy orders):")
        for i, bid in enumerate(self.bids):
            print(f"{i+1}. Price: {bid['price']}, Quantity: {bid['quantity']}")

        print("\nAsks (Sell orders):")
        for i, ask in enumerate(self.asks):
            print(f"{i+1}. Price: {ask['price']}, Quantity: {ask['quantity']}")
