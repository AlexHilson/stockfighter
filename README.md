# stockfighter
Tools for working with stockfighter.io - may include spoilers

## Example usage
First, add your API key to stockfighter/config.py, then:

### Start a new level
```python
from stockfighter.level import Level
my_level = Level.new_level("first_steps")
print(my_level.instructions)
print(my_level.account)
print(my_level.venues)
```

### Request venue details
```python
...
from stockfighter.venue import Venue
my_venue = Venue("TESTEX")
print(my_venue.stocks)
```

### Order a stock
```python
...
my_stock = my_venue.stocks[0]
print(my_stock.orderbook())
my_stock.order(
    my_level.account, price=1000, qty=10, direction="buy", order_type="limit")
