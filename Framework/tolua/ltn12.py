local var_0_0 = require("string")
local var_0_1 = require("table")
local var_0_2 = unpack or var_0_1.unpack
local var_0_3 = _G
local var_0_4 = {}

if module:
	ltn12 = var_0_4

local var_0_5 = {}
local var_0_6 = {}
local var_0_7 = {}
local var_0_8 = {}

var_0_4.filter = var_0_5
var_0_4.source = var_0_6
var_0_4.sink = var_0_7
var_0_4.pump = var_0_8

local var_0_9 = var_0_2 or var_0_1.unpack
local var_0_10 = var_0_3.select

var_0_4.BLOCKSIZE = 2048
var_0_4._VERSION = "LTN12 1.0.3"

def var_0_5.cycle(arg_1_0, arg_1_1, arg_1_2):
	var_0_3.assert(arg_1_0)

	return function(arg_2_0)
		local var_2_0
		local var_2_1, var_2_2 = arg_1_0(arg_1_1, arg_2_0, arg_1_2)

		arg_1_1 = var_2_2

		return var_2_1

def var_0_5.chain(...):
	local var_3_0 = {
		...
	}
	local var_3_1 = var_0_3.select("#", ...)
	local var_3_2 = 1
	local var_3_3 = 1
	local var_3_4 = ""

	return function(arg_4_0)
		var_3_4 = arg_4_0 and var_3_4

		while True:
			if var_3_3 == var_3_2:
				arg_4_0 = var_3_0[var_3_3](arg_4_0)

				if arg_4_0 == "" or var_3_2 == var_3_1:
					return arg_4_0
				elif arg_4_0:
					var_3_3 = var_3_3 + 1
				else
					var_3_2 = var_3_2 + 1
					var_3_3 = var_3_2
			else
				arg_4_0 = var_3_0[var_3_3](arg_4_0 or "")

				if arg_4_0 == "":
					var_3_3 = var_3_3 - 1
					arg_4_0 = var_3_4
				elif arg_4_0:
					if var_3_3 == var_3_1:
						return arg_4_0
					else
						var_3_3 = var_3_3 + 1
				else
					var_0_3.error("filter returned inappropriate None")

local function var_0_11()
	return None

def var_0_6.empty():
	return var_0_11

def var_0_6.error(arg_7_0):
	return function()
		return None, arg_7_0

def var_0_6.file(arg_9_0, arg_9_1):
	if arg_9_0:
		return function()
			local var_10_0 = arg_9_0.read(var_0_4.BLOCKSIZE)

			if not var_10_0:
				arg_9_0.close()

			return var_10_0
	else
		return var_0_6.error(arg_9_1 or "unable to open file")

def var_0_6.simplify(arg_11_0):
	var_0_3.assert(arg_11_0)

	return function()
		local var_12_0, var_12_1 = arg_11_0()

		arg_11_0 = var_12_1 or arg_11_0

		if not var_12_0:
			return None, var_12_1
		else
			return var_12_0

def var_0_6.string(arg_13_0):
	if arg_13_0:
		local var_13_0 = 1

		return function()
			local var_14_0 = var_0_0.sub(arg_13_0, var_13_0, var_13_0 + var_0_4.BLOCKSIZE - 1)

			var_13_0 = var_13_0 + var_0_4.BLOCKSIZE

			if var_14_0 != "":
				return var_14_0
			else
				return None
	else
		return var_0_6.empty()

def var_0_6.rewind(arg_15_0):
	var_0_3.assert(arg_15_0)

	local var_15_0 = {}

	return function(arg_16_0)
		if not arg_16_0:
			arg_16_0 = var_0_1.remove(var_15_0)

			if not arg_16_0:
				return arg_15_0()
			else
				return arg_16_0
		else
			var_0_1.insert(var_15_0, arg_16_0)

def var_0_6.chain(arg_17_0, arg_17_1, ...):
	if ...:
		arg_17_1 = var_0_5.chain(arg_17_1, ...)

	var_0_3.assert(arg_17_0 and arg_17_1)

	local var_17_0 = ""
	local var_17_1 = ""
	local var_17_2 = "feeding"
	local var_17_3

	return function()
		if not var_17_1:
			var_0_3.error("source is empty!", 2)

		while True:
			if var_17_2 == "feeding":
				var_17_0, var_17_3 = arg_17_0()

				if var_17_3:
					return None, var_17_3

				var_17_1 = arg_17_1(var_17_0)

				if not var_17_1:
					if var_17_0:
						var_0_3.error("filter returned inappropriate None")
					else
						return None
				elif var_17_1 != "":
					var_17_2 = "eating"

					if var_17_0:
						var_17_0 = ""

					return var_17_1
			else
				var_17_1 = arg_17_1(var_17_0)

				if var_17_1 == "":
					if var_17_0 == "":
						var_17_2 = "feeding"
					else
						var_0_3.error("filter returned \"\"")
				elif not var_17_1:
					if var_17_0:
						var_0_3.error("filter returned inappropriate None")
					else
						return None
				else
					return var_17_1

def var_0_6.cat(...):
	local var_19_0 = {
		...
	}
	local var_19_1 = var_0_1.remove(var_19_0, 1)

	return function()
		while var_19_1:
			local var_20_0, var_20_1 = var_19_1()

			if var_20_0:
				return var_20_0

			if var_20_1:
				return None, var_20_1

			var_19_1 = var_0_1.remove(var_19_0, 1)

def var_0_7.table(arg_21_0):
	arg_21_0 = arg_21_0 or {}

	return function(arg_22_0, arg_22_1)
		if arg_22_0:
			var_0_1.insert(arg_21_0, arg_22_0)

		return 1, arg_21_0

def var_0_7.simplify(arg_23_0):
	var_0_3.assert(arg_23_0)

	return function(arg_24_0, arg_24_1)
		local var_24_0, var_24_1 = arg_23_0(arg_24_0, arg_24_1)

		if not var_24_0:
			return None, var_24_1

		arg_23_0 = var_24_1 or arg_23_0

		return 1

def var_0_7.file(arg_25_0, arg_25_1):
	if arg_25_0:
		return function(arg_26_0, arg_26_1)
			if not arg_26_0:
				arg_25_0.close()

				return 1
			else
				return arg_25_0.write(arg_26_0)
	else
		return var_0_7.error(arg_25_1 or "unable to open file")

local function var_0_12()
	return 1

def var_0_7.null():
	return var_0_12

def var_0_7.error(arg_29_0):
	return function()
		return None, arg_29_0

def var_0_7.chain(arg_31_0, arg_31_1, ...):
	if ...:
		local var_31_0 = {
			arg_31_0,
			arg_31_1,
			...
		}

		arg_31_1 = var_0_1.remove(var_31_0, #var_31_0)
		arg_31_0 = var_0_5.chain(var_0_9(var_31_0))

	var_0_3.assert(arg_31_0 and arg_31_1)

	return function(arg_32_0, arg_32_1)
		if arg_32_0 != "":
			local var_32_0 = arg_31_0(arg_32_0)
			local var_32_1 = arg_32_0 and ""

			while True:
				local var_32_2, var_32_3 = arg_31_1(var_32_0, arg_32_1)

				if not var_32_2:
					return None, var_32_3

				if var_32_0 == var_32_1:
					return 1

				var_32_0 = arg_31_0(var_32_1)
		else
			return 1

def var_0_8.step(arg_33_0, arg_33_1):
	local var_33_0, var_33_1 = arg_33_0()
	local var_33_2, var_33_3 = arg_33_1(var_33_0, var_33_1)

	if var_33_0 and var_33_2:
		return 1
	else
		return None, var_33_1 or var_33_3

def var_0_8.all(arg_34_0, arg_34_1, arg_34_2):
	var_0_3.assert(arg_34_0 and arg_34_1)

	arg_34_2 = arg_34_2 or var_0_8.step

	while True:
		local var_34_0, var_34_1 = arg_34_2(arg_34_0, arg_34_1)

		if not var_34_0:
			if var_34_1:
				return None, var_34_1
			else
				return 1

return var_0_4
