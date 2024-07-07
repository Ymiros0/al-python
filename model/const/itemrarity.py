from packages.alsupport import math

Gray = 1
Blue = 2
Purple = 3
Gold = 4
SSR = 5

def Rarity2Print(arg_1_0):
	if math.clamp(arg_1_0, 1, 9) == arg_1_0:
		return str(arg_1_0)
	else:
		return Gray

colors = {
	"FFFFFFFF",
	"41D7FFFF",
	"CC7BFFFF",
	"FDC637FF",
	"FF5E39FF",
	"FFFFFFFF",
	"FDC637FF",
	"FFFFFFFF",
	"FDC637FF"
}

def Rarity2HexColor(arg_2_0):
	return colors[arg_2_0]

frameColors = {
	"BDBDBDFF",
	"65C7FFFF",
	"BFA3FFFF",
	"FFE743FF",
	"FFFFFFFF",
	"FFFFFFFF",
	"FFE743FF",
	"FFFFFFFF",
	"FFE743FF"
}

def Rarity2FrameHexColor(arg_3_0):
	return frameColors[arg_3_0]
