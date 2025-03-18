from basana.core import bar
from basana.external.common.csv.BinanceBar import BinanceBar
from basana.external.common.csv.bars import RowParser


import datetime
from decimal import Decimal


class BinanceRowParser (RowParser) :
    def __init__(self, pair, tzinfo, timedelta):
        super().__init__(pair, tzinfo, timedelta)

    def parse_row(self, row_dict):
        # File format:
        #
        # datetime,open,high,low,close,volume
        # 2015-01-01 00:00:00,321,321,321,321,1.73697242

        volume = Decimal(row_dict["volume"])
        count = Decimal (row_dict["count"])
        taker_buy_quote_volume = Decimal (row_dict["taker_buy_quote_volume"])
        # Skip bars with no volume.
        if volume == 0 :
            return []
        dt = datetime.datetime.fromtimestamp(int(row_dict["open_time"]) /1000.0, tz=self.tzinfo)
        # dt = datetime.datetime.strptime(row_dict["open_time"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=self.tzinfo)
        return [
            bar.BarEvent(
                dt + self.timedelta,
                BinanceBar(
                    dt, self.pair, Decimal(row_dict["open"]), Decimal(row_dict["high"]), Decimal(row_dict["low"]),
                    Decimal(row_dict["close"]), volume,count,taker_buy_quote_volume
                )
            )
        ]