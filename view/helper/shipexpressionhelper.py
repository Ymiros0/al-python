local var_0_0 = class("ShipExpressionHelper")
local var_0_1 = pg.ship_skin_expression
local var_0_2 = pg.ship_skin_expression_ex
local var_0_3 = False

local function var_0_4(...)
	if var_0_3 and IsUnityEditor:
		print(...)

local function var_0_5(arg_2_0, arg_2_1, arg_2_2, arg_2_3)
	local var_2_0 = var_0_2[arg_2_0]

	local function var_2_1()
		local var_3_0 = var_2_0[arg_2_1]
		local var_3_1

		if var_3_0 and var_3_0 != "":
			for iter_3_0, iter_3_1 in ipairs(var_3_0):
				if arg_2_2 >= iter_3_1[1]:
					var_3_1 = iter_3_1[2]

		return var_3_1

	local function var_2_2(arg_4_0)
		local var_4_0 = var_2_0.main_ex

		if var_4_0 and var_4_0 != "":
			local var_4_1

			for iter_4_0, iter_4_1 in ipairs(var_4_0):
				if arg_2_2 >= iter_4_1[1]:
					var_4_1 = iter_4_1[2]

			if var_4_1:
				return string.split(var_4_1, "|")[arg_4_0]

		return None

	local function var_2_3()
		local var_5_0 = string.split(arg_2_1, "_")[2]

		if not var_5_0:
			return None

		local var_5_1 = tonumber(var_5_0) - ShipWordHelper.GetMainSceneWordCnt(arg_2_3)

		if var_5_1 > 0:
			return var_2_2(var_5_1)
		else
			return var_2_1()

	local var_2_4

	if var_2_0:
		if arg_2_3 and string.find(arg_2_1, "main"):
			var_2_4 = var_2_3()
		else
			var_2_4 = var_2_1()

	return var_2_4

def var_0_0.GetExpression(arg_6_0, arg_6_1, arg_6_2, arg_6_3):
	var_0_4("name.", arg_6_0, " - kind.", arg_6_1, " - favor.", arg_6_2)

	local var_6_0 = var_0_1[arg_6_0]

	if not var_6_0:
		return None

	local var_6_1 = var_6_0[arg_6_1]

	if arg_6_2:
		local var_6_2 = var_0_5(arg_6_0, arg_6_1, arg_6_2, arg_6_3)

		if var_6_2:
			var_0_4("get expression form ex.", var_6_2)

			var_6_1 = var_6_2

	if not var_6_1 or var_6_1 == "":
		var_6_1 = var_6_0.default

		var_0_4("get expression form default.", var_6_1)

	var_0_4("get express .", var_6_1)

	return var_6_1

def var_0_0.SetExpression(arg_7_0, arg_7_1, arg_7_2, arg_7_3, arg_7_4):
	local var_7_0 = var_0_0.GetExpression(arg_7_1, arg_7_2, arg_7_3, arg_7_4)

	return var_0_0.UpdateExpression(arg_7_0, arg_7_1, var_7_0)

def var_0_0.UpdateExpression(arg_8_0, arg_8_1, arg_8_2):
	local var_8_0 = tf(arg_8_0).Find("face")

	if not var_8_0:
		return False, None

	local var_8_1 = arg_8_1

	if not arg_8_2 or arg_8_2 == "":
		var_8_1 = string.gsub(arg_8_1, "_n", "")

		if var_0_0.DefaultFaceless(var_8_1):
			arg_8_2 = var_0_0.GetDefaultFace(var_8_1)

	if not arg_8_2 or arg_8_2 == "":
		setActive(var_8_0, False)

		return False, None

	var_0_0._UpdateExpression(var_8_0, var_8_1, arg_8_2)

	return True, arg_8_2

def var_0_0._UpdateExpression(arg_9_0, arg_9_1, arg_9_2):
	local var_9_0 = GetSpriteFromAtlas("paintingface/" .. arg_9_1, arg_9_2)

	setImageSprite(arg_9_0, var_9_0)
	setActive(arg_9_0, True)

	local var_9_1 = findTF(arg_9_0, "face_sub")

	if var_9_1:
		local var_9_2 = GetSpriteFromAtlas("paintingface/" .. arg_9_1, arg_9_2 .. "_sub")

		setActive(var_9_1, var_9_2)

		if var_9_2:
			setImageSprite(var_9_1, var_9_2)

def var_0_0.DefaultFaceless(arg_10_0):
	local var_10_0 = var_0_1[arg_10_0]

	return var_10_0 and var_10_0.default != ""

def var_0_0.GetDefaultFace(arg_11_0):
	return var_0_1[arg_11_0].default

return var_0_0
