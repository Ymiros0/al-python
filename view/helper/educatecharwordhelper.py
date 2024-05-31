local var_0_0 = class("EducateCharWordHelper")

var_0_0.WORD_KEY_CHRISTMAS = "shengdan"
var_0_0.WORD_KEY_NEWYEAR = "xinnian"
var_0_0.WORD_KEY_LUNARNEWYEAR = "chuxi"
var_0_0.WORD_KEY_VALENTINE = "qingrenjie"
var_0_0.WORD_KEY_MIDAUTUMNFESTIVAL = "zhongqiu"
var_0_0.WORD_KEY_ALLHALLOWSDAY = "wansheng"
var_0_0.WORD_KEY_TELL_TIME = "chime_"
var_0_0.WORD_KEY_ACT = "huodong"
var_0_0.WORD_KEY_CHANGE_TB = "genghuan"

local var_0_1 = pg.secretary_special_ship
local var_0_2 = pg.character_voice_special
local var_0_3 = pg.secretary_special_ship_expression

local function var_0_4(arg_1_0, arg_1_1)
	local var_1_0 = var_0_2[arg_1_0]

	if not var_1_0:
		return None, None, None

	return "event./educate-cv/" .. arg_1_1 .. "/" .. var_1_0.resource_key, var_1_0.resource_key

def var_0_0.GetWordAndCV(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0
	local var_2_1
	local var_2_2
	local var_2_3
	local var_2_4 = var_0_1[arg_2_0]
	local var_2_5 = arg_2_1

	if string.find(arg_2_1, ShipWordHelper.WORD_TYPE_MAIN):
		local var_2_6 = string.split(arg_2_1, "_")

		arg_2_1 = ShipWordHelper.WORD_TYPE_MAIN

		local var_2_7 = tonumber(var_2_6[2] or "1")
		local var_2_8 = var_2_4[arg_2_1] or ""

		var_2_2 = string.split(var_2_8 or "", "|")[var_2_7] or ""
		var_2_5 = arg_2_1 .. "" .. var_2_7
	else
		var_2_2 = var_2_4[arg_2_1] or ""

	if var_2_4.voice and var_2_4.voice != "":
		var_2_0 = var_2_4.voice
		var_2_1, var_2_3 = var_0_4(var_2_5, var_2_0)

	if var_2_2 and arg_2_2:
		var_2_2 = SwitchSpecialChar(var_2_2, True)

	var_2_2 = var_2_2 and HXSet.hxLan(var_2_2)

	return var_2_0, var_2_1, var_2_2, var_2_3

def var_0_0.ExistWord(arg_3_0, arg_3_1):
	local var_3_0 = var_0_1[arg_3_0]

	if string.find(arg_3_1, ShipWordHelper.WORD_TYPE_MAIN):
		local var_3_1 = string.split(var_3_0.main, "|")
		local var_3_2 = string.split(arg_3_1, "_")

		return tonumber(var_3_2[2]) <= #var_3_1
	else
		return var_3_0[arg_3_1] != None and var_3_0[arg_3_1] != ""

def var_0_0.RawGetCVKey(arg_4_0):
	return var_0_1[arg_4_0].voice

def var_0_0.GetExpression(arg_5_0, arg_5_1):
	local var_5_0 = var_0_3[arg_5_0]
	local var_5_1 = ""

	if string.find(arg_5_1, ShipWordHelper.WORD_TYPE_MAIN):
		local var_5_2 = string.split(arg_5_1, "_")
		local var_5_3 = tonumber(var_5_2[2] or "1")
		local var_5_4 = var_5_0[ShipWordHelper.WORD_TYPE_MAIN] or ""

		var_5_1 = string.split(var_5_4, "|")[var_5_3] or ""

		if var_5_1 == "0" or var_5_1 == "None":
			var_5_1 = ""
	else
		var_5_1 = var_5_0[arg_5_1] or ""

	return var_5_1

return var_0_0
