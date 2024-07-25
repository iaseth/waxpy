from .utils import intb



def bytes_to_candle(candle_bytes):
	candle = [0, 0, 0, 0, 0, 0]
	for x in range(6):
		start = x * 4
		end = start + 4
		candle[x] = intb(candle_bytes[start:end])

	for x in range(1, 5):
		candle[x] = candle[x] / 100

	return candle

