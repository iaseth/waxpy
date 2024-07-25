from .utils import bint



def candle_to_bytes(candle):
	t = candle.timestamp
	v = candle.volume
	ohlc = candle.ohlc
	ohlc = [int(x*100) for x in ohlc]
	new_candle = [t, *ohlc, v]
	byte_candle = [bint(x, 4) for x in new_candle]
	candle_bytes = b''.join(byte_candle)
	return candle_bytes

