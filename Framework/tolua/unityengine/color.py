local var_0_0 = rawget
local var_0_1 = setmetatable
local var_0_2 = type
local var_0_3 = Mathf
local var_0_4 = {}
local var_0_5 = tolua.initget(var_0_4)

def var_0_4.__index(arg_1_0, arg_1_1):
	local var_1_0 = var_0_0(var_0_4, arg_1_1)

	if var_1_0 == None:
		var_1_0 = var_0_0(var_0_5, arg_1_1)

		if var_1_0 != None:
			return var_1_0(arg_1_0)

	return var_1_0

def var_0_4.__call(arg_2_0, arg_2_1, arg_2_2, arg_2_3, arg_2_4):
	return var_0_1({
		r = arg_2_1 or 0,
		g = arg_2_2 or 0,
		b = arg_2_3 or 0,
		a = arg_2_4 or 1
	}, var_0_4)

def var_0_4.New(arg_3_0, arg_3_1, arg_3_2, arg_3_3):
	return var_0_1({
		r = arg_3_0 or 0,
		g = arg_3_1 or 0,
		b = arg_3_2 or 0,
		a = arg_3_3 or 1
	}, var_0_4)

def var_0_4.Set(arg_4_0, arg_4_1, arg_4_2, arg_4_3, arg_4_4):
	arg_4_0.r = arg_4_1
	arg_4_0.g = arg_4_2
	arg_4_0.b = arg_4_3
	arg_4_0.a = arg_4_4 or 1

def var_0_4.Get(arg_5_0):
	return arg_5_0.r, arg_5_0.g, arg_5_0.b, arg_5_0.a

def var_0_4.Equals(arg_6_0, arg_6_1):
	return arg_6_0.r == arg_6_1.r and arg_6_0.g == arg_6_1.g and arg_6_0.b == arg_6_1.b and arg_6_0.a == arg_6_1.a

def var_0_4.Lerp(arg_7_0, arg_7_1, arg_7_2):
	arg_7_2 = var_0_3.Clamp01(arg_7_2)

	return var_0_4.New(arg_7_0.r + arg_7_2 * (arg_7_1.r - arg_7_0.r), arg_7_0.g + arg_7_2 * (arg_7_1.g - arg_7_0.g), arg_7_0.b + arg_7_2 * (arg_7_1.b - arg_7_0.b), arg_7_0.a + arg_7_2 * (arg_7_1.a - arg_7_0.a))

def var_0_4.LerpUnclamped(arg_8_0, arg_8_1, arg_8_2):
	return var_0_4.New(arg_8_0.r + arg_8_2 * (arg_8_1.r - arg_8_0.r), arg_8_0.g + arg_8_2 * (arg_8_1.g - arg_8_0.g), arg_8_0.b + arg_8_2 * (arg_8_1.b - arg_8_0.b), arg_8_0.a + arg_8_2 * (arg_8_1.a - arg_8_0.a))

def var_0_4.HSVToRGB(arg_9_0, arg_9_1, arg_9_2, arg_9_3):
	if arg_9_3:
		-- block empty

	arg_9_3 = True

	local var_9_0 = var_0_4.New(1, 1, 1, 1)

	if arg_9_1 == 0:
		var_9_0.r = arg_9_2
		var_9_0.g = arg_9_2
		var_9_0.b = arg_9_2

		return var_9_0

	if arg_9_2 == 0:
		var_9_0.r = 0
		var_9_0.g = 0
		var_9_0.b = 0

		return var_9_0

	var_9_0.r = 0
	var_9_0.g = 0
	var_9_0.b = 0

	local var_9_1 = arg_9_1
	local var_9_2 = arg_9_2
	local var_9_3 = arg_9_0 * 6
	local var_9_4 = var_0_3.Floor(var_9_3)
	local var_9_5 = var_9_3 - var_9_4
	local var_9_6 = var_9_2 * (1 - var_9_1)
	local var_9_7 = var_9_2 * (1 - var_9_1 * var_9_5)
	local var_9_8 = var_9_2 * (1 - var_9_1 * (1 - var_9_5))
	local var_9_9 = var_9_4 + 1

	if var_9_9 == 0:
		var_9_0.r = var_9_2
		var_9_0.g = var_9_6
		var_9_0.b = var_9_7
	elif var_9_9 == 1:
		var_9_0.r = var_9_2
		var_9_0.g = var_9_8
		var_9_0.b = var_9_6
	elif var_9_9 == 2:
		var_9_0.r = var_9_7
		var_9_0.g = var_9_2
		var_9_0.b = var_9_6
	elif var_9_9 == 3:
		var_9_0.r = var_9_6
		var_9_0.g = var_9_2
		var_9_0.b = var_9_8
	elif var_9_9 == 4:
		var_9_0.r = var_9_6
		var_9_0.g = var_9_7
		var_9_0.b = var_9_2
	elif var_9_9 == 5:
		var_9_0.r = var_9_8
		var_9_0.g = var_9_6
		var_9_0.b = var_9_2
	elif var_9_9 == 6:
		var_9_0.r = var_9_2
		var_9_0.g = var_9_6
		var_9_0.b = var_9_7
	elif var_9_9 == 7:
		var_9_0.r = var_9_2
		var_9_0.g = var_9_8
		var_9_0.b = var_9_6

	if not arg_9_3:
		var_9_0.r = var_0_3.Clamp(var_9_0.r, 0, 1)
		var_9_0.g = var_0_3.Clamp(var_9_0.g, 0, 1)
		var_9_0.b = var_0_3.Clamp(var_9_0.b, 0, 1)

	return var_9_0

local function var_0_6(arg_10_0, arg_10_1, arg_10_2, arg_10_3)
	local var_10_0 = arg_10_1

	if var_10_0 != 0:
		local var_10_1 = 0

		if arg_10_3 < arg_10_2:
			var_10_1 = arg_10_3
		else
			var_10_1 = arg_10_2

		local var_10_2 = var_10_0 - var_10_1
		local var_10_3 = 0
		local var_10_4 = 0

		if var_10_2 != 0:
			var_10_4 = var_10_2 / var_10_0
			var_10_3 = arg_10_0 + (arg_10_2 - arg_10_3) / var_10_2
		else
			var_10_4 = 0
			var_10_3 = arg_10_0 + (arg_10_2 - arg_10_3)

		local var_10_5 = var_10_3 / 6

		if var_10_5 < 0:
			var_10_5 = var_10_5 + 1

		return var_10_5, var_10_4, var_10_0

	return 0, 0, var_10_0

def var_0_4.RGBToHSV(arg_11_0):
	if arg_11_0.b > arg_11_0.g and arg_11_0.b > arg_11_0.r:
		return var_0_6(4, arg_11_0.b, arg_11_0.r, arg_11_0.g)
	elif arg_11_0.g > arg_11_0.r:
		return var_0_6(2, arg_11_0.g, arg_11_0.b, arg_11_0.r)
	else
		return var_0_6(0, arg_11_0.r, arg_11_0.g, arg_11_0.b)

def var_0_4.GrayScale(arg_12_0):
	return 0.299 * arg_12_0.r + 0.587 * arg_12_0.g + 0.114 * arg_12_0.b

def var_0_4.NewHex(arg_13_0):
	if string.sub(arg_13_0, 1, 1) == "#":
		arg_13_0 = string.sub(arg_13_0, 2)

	arg_13_0 = string.upper(arg_13_0)

	local var_13_0 = {}

	for iter_13_0 = 1, 4:
		if iter_13_0 + iter_13_0 > #arg_13_0:
			var_13_0[iter_13_0] = 1
		else
			var_13_0[iter_13_0] = tonumber(string.sub(arg_13_0, iter_13_0 + iter_13_0 - 1, iter_13_0 + iter_13_0), 16) / 255

	return var_0_4.New(unpack(var_13_0))

def var_0_4.ToHex(arg_14_0, arg_14_1):
	return arg_14_1 and string.format("%.2X%.2X%.2X%.2X", arg_14_0.r * 255, arg_14_0.g * 255, arg_14_0.b * 255, arg_14_0.a * 255) or string.format("%.2X%.2X%.2X", arg_14_0.r * 255, arg_14_0.g * 255, arg_14_0.b * 255)

def var_0_4.__tostring(arg_15_0):
	return string.format("RGBA(%f,%f,%f,%f)", arg_15_0.r, arg_15_0.g, arg_15_0.b, arg_15_0.a)

def var_0_4.__add(arg_16_0, arg_16_1):
	return var_0_4.New(arg_16_0.r + arg_16_1.r, arg_16_0.g + arg_16_1.g, arg_16_0.b + arg_16_1.b, arg_16_0.a + arg_16_1.a)

def var_0_4.__sub(arg_17_0, arg_17_1):
	return var_0_4.New(arg_17_0.r - arg_17_1.r, arg_17_0.g - arg_17_1.g, arg_17_0.b - arg_17_1.b, arg_17_0.a - arg_17_1.a)

def var_0_4.__mul(arg_18_0, arg_18_1):
	if var_0_2(arg_18_1) == "number":
		return var_0_4.New(arg_18_0.r * arg_18_1, arg_18_0.g * arg_18_1, arg_18_0.b * arg_18_1, arg_18_0.a * arg_18_1)
	elif getmetatable(arg_18_1) == var_0_4:
		return var_0_4.New(arg_18_0.r * arg_18_1.r, arg_18_0.g * arg_18_1.g, arg_18_0.b * arg_18_1.b, arg_18_0.a * arg_18_1.a)

def var_0_4.__div(arg_19_0, arg_19_1):
	return var_0_4.New(arg_19_0.r / arg_19_1, arg_19_0.g / arg_19_1, arg_19_0.b / arg_19_1, arg_19_0.a / arg_19_1)

def var_0_4.__eq(arg_20_0, arg_20_1):
	return arg_20_0.r == arg_20_1.r and arg_20_0.g == arg_20_1.g and arg_20_0.b == arg_20_1.b and arg_20_0.a == arg_20_1.a

def var_0_5.red():
	return var_0_4.New(1, 0, 0, 1)

def var_0_5.green():
	return var_0_4.New(0, 1, 0, 1)

def var_0_5.blue():
	return var_0_4.New(0, 0, 1, 1)

def var_0_5.white():
	return var_0_4.New(1, 1, 1, 1)

def var_0_5.black():
	return var_0_4.New(0, 0, 0, 1)

def var_0_5.yellow():
	return var_0_4.New(1, 0.9215686, 0.01568628, 1)

def var_0_5.cyan():
	return var_0_4.New(0, 1, 1, 1)

def var_0_5.magenta():
	return var_0_4.New(1, 0, 1, 1)

def var_0_5.gray():
	return var_0_4.New(0.5, 0.5, 0.5, 1)

def var_0_5.clear():
	return var_0_4.New(0, 0, 0, 0)

def var_0_5.buttonDisabled():
	return var_0_4.New(0.7843137254901961, 0.7843137254901961, 0.7843137254901961, 0.5)

def var_0_5.ReisalinGold():
	return var_0_4.New(1, 0.90196, 0.50196, 1)

def var_0_5.gamma(arg_33_0):
	return var_0_4.New(var_0_3.LinearToGammaSpace(arg_33_0.r), var_0_3.LinearToGammaSpace(arg_33_0.g), var_0_3.LinearToGammaSpace(arg_33_0.b), arg_33_0.a)

def var_0_5.linear(arg_34_0):
	return var_0_4.New(var_0_3.GammaToLinearSpace(arg_34_0.r), var_0_3.GammaToLinearSpace(arg_34_0.g), var_0_3.GammaToLinearSpace(arg_34_0.b), arg_34_0.a)

def var_0_5.maxColorComponent(arg_35_0):
	return var_0_3.Max(var_0_3.Max(arg_35_0.r, arg_35_0.g), arg_35_0.b)

var_0_5.grayscale = var_0_4.GrayScale
UnityEngine.Color = var_0_4

var_0_1(var_0_4, var_0_4)

return var_0_4
