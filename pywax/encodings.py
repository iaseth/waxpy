


class EncodingScheme:
	def __init__(self, widths, multipliers):
		self.count = len(widths)
		self.widths = []
		self.multipliers = []
		self.width = sum(widths)

	def encoder(self):
		pass

	def decoder(self):
		pass



index_2B  = EncodingScheme([4, 2, 2, 2, 2],        [1, 100, 100, 100, 100])
stock_2B  = EncodingScheme([4, 2, 2, 2, 2, 4],     [1, 100, 100, 100, 100, 1])
option_2B = EncodingScheme([4, 2, 2, 2, 2, 4, 4],  [1, 100, 100, 100, 100, 1, 1])

index_3B  = EncodingScheme([4, 3, 3, 3, 3],        [1, 100, 100, 100, 100])
stock_3B  = EncodingScheme([4, 3, 3, 3, 3, 4],     [1, 100, 100, 100, 100, 1])
option_3B = EncodingScheme([4, 3, 3, 3, 3, 4, 4],  [1, 100, 100, 100, 100, 1, 1])

index_4B  = EncodingScheme([4, 4, 4, 4, 4],        [1, 100, 100, 100, 100])
stock_4B  = EncodingScheme([4, 4, 4, 4, 4, 4],     [1, 100, 100, 100, 100, 1])
option_4B = EncodingScheme([4, 4, 4, 4, 4, 4, 4],  [1, 100, 100, 100, 100, 1, 1])

index_5B  = EncodingScheme([4, 5, 5, 5, 5],        [1, 100, 100, 100, 100])
stock_5B  = EncodingScheme([4, 5, 5, 5, 5, 4],     [1, 100, 100, 100, 100, 1])
option_5B = EncodingScheme([4, 5, 5, 5, 5, 4, 4],  [1, 100, 100, 100, 100, 1, 1])



ENCODINGS = {}

ENCODINGS["21"] = index_2B
ENCODINGS["22"] = stock_2B
ENCODINGS["23"] = option_2B

ENCODINGS["31"] = index_3B
ENCODINGS["32"] = stock_3B
ENCODINGS["33"] = option_3B

ENCODINGS["41"] = index_4B
ENCODINGS["42"] = stock_4B
ENCODINGS["43"] = option_4B

ENCODINGS["51"] = index_5B
ENCODINGS["52"] = stock_5B
ENCODINGS["53"] = option_5B


