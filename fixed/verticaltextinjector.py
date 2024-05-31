local var_0_0 = {}

local function var_0_1(arg_1_0)
	return ReflectionHelp.RefGetField(typeof("UnityEngine.UILineInfo"), "startCharIdx", arg_1_0)

local function var_0_2(arg_2_0)
	local var_2_0 = {}

	for iter_2_0 = 0, #arg_2_0 - 1:
		var_2_0[iter_2_0] = 0

	for iter_2_1, iter_2_2 in ipairs({
		" ",
		"\n"
	}):
		local var_2_1 = Clone(arg_2_0)
		local var_2_2 = 0
		local var_2_3 = string.find(var_2_1, iter_2_2)

		while var_2_3:
			for iter_2_3 = 0, #iter_2_2 - 1:
				var_2_0[var_2_2 + var_2_3 + iter_2_3] = 3

			var_2_2 = var_2_2 + var_2_3 + #iter_2_2
			var_2_1 = string.sub(var_2_1, var_2_3 + #iter_2_2)
			var_2_3 = string.find(var_2_1, iter_2_2)

	local var_2_4

	for iter_2_4, iter_2_5 in ipairs({
		"b",
		"i",
		"size",
		"color",
		"material"
	}):
		local var_2_5 = "</" .. iter_2_5 .. ">"
		local var_2_6 = string.match(arg_2_0, "</*" .. iter_2_5 .. "[^>]*>")
		local var_2_7 = {}

		while var_2_6:
			local var_2_8 = string.find(arg_2_0, var_2_6)

			if var_2_6 == var_2_5:
				if #var_2_7 > 0:
					local var_2_9 = table.remove(var_2_7)

					for iter_2_6 = 0, #var_2_9.str - 1:
						var_2_0[var_2_9.start + iter_2_6] = 1

					for iter_2_7 = 0, #var_2_6 - 1:
						var_2_0[var_2_8 + iter_2_7] = 2
			else
				local var_2_10 = {
					str = var_2_6,
					start = var_2_8
				}

				table.insert(var_2_7, var_2_10)

		local var_2_11 = string.match(arg_2_0, "</*" .. iter_2_5 .. "[^>]*>")

	local var_2_12 = {}
	local var_2_13 = 0

	for iter_2_8 = 0, #arg_2_0 - 1:
		if var_2_0[iter_2_8] == 0:
			var_2_12[iter_2_8] = var_2_13
			var_2_13 = var_2_13 + 1
		else
			var_2_12[iter_2_8] = -2

	for iter_2_9 = 0, #arg_2_0 - 1:
		if var_2_12[iter_2_9] != -2 or var_2_0[iter_2_9] == 0:
			-- block empty
		elif var_2_0[iter_2_9] == 1:
			var_2_12[iter_2_9] = findRight(var_2_0, var_2_12, #arg_2_0, iter_2_9 + 1)
		elif var_2_0[iter_2_9] == 2:
			var_2_12[iter_2_9] = var_2_12[iter_2_9 - 1]
		elif var_2_0[iter_2_9] == 3:
			var_2_12[iter_2_9] = -1

	return var_2_12

local function var_0_3(arg_3_0, arg_3_1, arg_3_2, arg_3_3)
	if arg_3_3 < arg_3_2:
		if arg_3_0[arg_3_3] == 0:
			return arg_3_1[arg_3_3]
		elif arg_3_0[arg_3_3] == 1:
			arg_3_1[arg_3_3] = var_0_3(arg_3_0, arg_3_1, arg_3_2, arg_3_3 + 1)

			return arg_3_1[arg_3_3]
		elif arg_3_0[arg_3_3] == 2:
			return -1
		elif arg_3_0[arg_3_3] == 3:
			arg_3_1[arg_3_3] = var_0_3(arg_3_0, arg_3_1, arg_3_2, arg_3_3 + 1)

			return arg_3_1[arg_3_3]

	return -1

def var_0_0.ModifyMesh():
	return function(arg_5_0, arg_5_1)
		if not ReflectionHelp.RefCallMethod(typeof("VerticalText"), "IsActive", arg_5_0):
			return

		local var_5_0 = GetComponent(ReflectionHelp.RefGetProperty(typeof("VerticalText"), "gameObject", arg_5_0), typeof(Text))
		local var_5_1 = var_5_0.cachedTextGenerator

		ReflectionHelp.RefSetField(typeof("VerticalText"), "lineSpacing", arg_5_0, var_5_0.fontSize * var_5_0.lineSpacing)

		local var_5_2 = ReflectionHelp.RefGetField(typeof("VerticalText"), "spacing", arg_5_0)

		ReflectionHelp.RefSetField(typeof("VerticalText"), "textSpacing", arg_5_0, var_5_0.fontSize * var_5_2)
		ReflectionHelp.RefSetField(typeof("VerticalText"), "xOffset", arg_5_0, var_5_0.rectTransform.sizeDelta.x / 2 - var_5_0.fontSize / 2)
		ReflectionHelp.RefSetField(typeof("VerticalText"), "yOffset", arg_5_0, var_5_0.rectTransform.sizeDelta.y / 2 - var_5_0.fontSize / 2)

		local var_5_3 = ReflectionHelp.RefGetProperty(typeof("UnityEngine.TextGenerator"), "lines", var_5_1)
		local var_5_4 = ReflectionHelp.RefCallStaticMethod(typeof("UnityEngine.UI.RichText"), "RichStringProjection", {
			typeof("System.String")
		}, {
			var_5_0.text
		})
		local var_5_5 = var_5_3.Count

		for iter_5_0 = 0, var_5_5 - 1:
			local var_5_6 = var_5_5 > iter_5_0 + 1 and var_0_1(var_5_3[iter_5_0 + 1]) or utf8_len(var_5_0.text)
			local var_5_7 = 0

			for iter_5_1 = var_0_1(var_5_3[iter_5_0]), var_5_6 - 1:
				if var_5_4[iter_5_1] >= 0:
					ReflectionHelp.RefCallMethod(typeof("VerticalText"), "modifyText", arg_5_0, {
						typeof("UnityEngine.UI.VertexHelper"),
						typeof("System.Int32"),
						typeof("System.Int32"),
						typeof("System.Int32")
					}, {
						arg_5_1,
						var_5_4[iter_5_1],
						var_5_7,
						iter_5_0
					})

				var_5_7 = var_5_7 + 1, LuaInterface.InjectType.Replace

InjectByName("VerticalText", var_0_0)
