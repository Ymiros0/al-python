import regex

def transform(pattern:str):
	if '%g' in pattern:
		raise ValueError("Non printable characters not implemented")
	pattern = pattern.replace('%z', '\x00').replace('%l', r'\p{Ll}').replace('%c', r'\p{C}').replace('%p', r'\p{P}').replace('%u', r'\p{Lu}').replace('%x', r'[a-fA-F0-9]')
	pattern = pattern.replace('%Z', '[^\x00]').replace('%L', r'[^\p{Ll}]').replace('%C', r'[^\p{C}]').replace('%p', r'[^\p{P}]').replace('%u', r'[^\p{Lu}]').replace('%X', r'[^a-fA-F0-9]')
	return pattern.replace('%', '\\')

def find(a:str, b:str):
	b = transform(b)
	m = regex.search(b,a)
	if m:
		return m.span()

def sub(s,start, end=None):
	return s[start:end]