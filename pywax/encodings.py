from .encoding_scheme import EncodingScheme



ENCODINGS = [
	EncodingScheme(21, "Index B2",  [4, 2, 2, 2, 2],        [1, 100, 100, 100, 100]),
	EncodingScheme(22, "Stock B2",  [4, 2, 2, 2, 2, 4],     [1, 100, 100, 100, 100, 1]),
	EncodingScheme(23, "Option B2", [4, 2, 2, 2, 2, 4, 4],  [1, 100, 100, 100, 100, 1, 1]),

	EncodingScheme(31, "Index B3",  [4, 3, 3, 3, 3],        [1, 100, 100, 100, 100]),
	EncodingScheme(32, "Stock B3",  [4, 3, 3, 3, 3, 4],     [1, 100, 100, 100, 100, 1]),
	EncodingScheme(33, "Option B3", [4, 3, 3, 3, 3, 4, 4],  [1, 100, 100, 100, 100, 1, 1]),

	EncodingScheme(41, "Index B4",  [4, 4, 4, 4, 4],        [1, 100, 100, 100, 100]),
	EncodingScheme(42, "Stock B4",  [4, 4, 4, 4, 4, 4],     [1, 100, 100, 100, 100, 1]),
	EncodingScheme(43, "Option B4", [4, 4, 4, 4, 4, 4, 4],  [1, 100, 100, 100, 100, 1, 1]),

	EncodingScheme(51, "Index B5",  [4, 5, 5, 5, 5],        [1, 100, 100, 100, 100]),
	EncodingScheme(52, "Stock B5",  [4, 5, 5, 5, 5, 4],     [1, 100, 100, 100, 100, 1]),
	EncodingScheme(53, "Option B5", [4, 5, 5, 5, 5, 4, 4],  [1, 100, 100, 100, 100, 1, 1]),
]


def get_encoding_from_code(code):
	for encoding in ENCODINGS:
		if encoding.code == code:
			return encoding
	return None


def get_encoding_from_codename(codeName):
	for encoding in ENCODINGS:
		if encoding.codeName == codeName:
			return encoding
	return None


