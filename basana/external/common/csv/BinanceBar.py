from basana.core import bar, pair


import datetime
from decimal import Decimal


class BinanceBar (bar.Bar) :
    def __init__(
            self, datetime: datetime.datetime, pair: pair.Pair,
            open: Decimal, high: Decimal, low: Decimal,
            close: Decimal, volume: Decimal
            ,count = None ,
            taker_buy_quote_volume = None
    ):
        super().__init__(datetime, pair, open, high, low, close, volume)
        self.count = count
        self.taker_buy_quote_volume = taker_buy_quote_volume