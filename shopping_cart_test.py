
from shopping_cart import to_usd

def test_to_usd():
    price = 4.5
    price_usd = to_usd(price)
    assert price_usd == 4.5 #"$4.50"
