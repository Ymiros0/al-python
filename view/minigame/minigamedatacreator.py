local var_0_0 = class("MiniGameDataCreator")

var_0_0.ShrineGameID = 3
var_0_0.FireWorkGameID = 4
var_0_0.TowerClimbingGameID = 13
var_0_0.NewYearShrineGameID = 20

def var_0_0.DataCreateFunc(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	if arg_1_0 == MiniGameOPCommand.CMD_SPECIAL_GAME:
		local var_1_0 = arg_1_1[1]
		local var_1_1 = arg_1_1[2]
		local var_1_2 = getProxy(MiniGameProxy).GetMiniGameData(var_1_0)
		local var_1_3 = {}

		if var_1_2.getConfig("type") == MiniGameConst.MG_TYPE_3:
			if var_1_1 == 1:
				var_1_3.count = arg_1_2[1]
				var_1_3.serverGold = arg_1_2[2]
				var_1_3.isInited = True
			elif var_1_1 == 2:
				var_1_3.count = var_1_2.GetRuntimeData("count") - 1
				var_1_3.serverGold = arg_1_2[1]
			elif var_1_1 == 3:
				var_1_3.serverGold = arg_1_2[1]
		elif var_1_2.getConfig("type") == MiniGameConst.MG_TYPE_5:
			if var_1_1 == 1:
				var_1_3.count = arg_1_2[1]
				var_1_3.isInited = True
			elif var_1_1 == 2:
				var_1_3.count = var_1_2.GetRuntimeData("count") - 1

				local var_1_4 = arg_1_1[4]
				local var_1_5 = arg_1_1[5]
				local var_1_6 = var_1_2.GetRuntimeData("kvpElements")
				local var_1_7 = var_1_6[1]

				table.insert(var_1_7, {
					key = var_1_4,
					value = var_1_5
				})
				var_1_2.SetRuntimeData("kvpElements", var_1_6)
		elif var_1_0 == var_0_0.TowerClimbingGameID and var_1_1 == 1:
			var_1_3.isInited = True

		local var_1_8 = var_1_2.getConfig("type")

		if var_1_8 == MiniGameConst.MG_TYPE_2 and var_1_1 == 1 or var_1_8 == MiniGameConst.MG_TYPE_5 and var_1_1 == 1 or var_1_8 == MiniGameConst.MG_TYPE_4:
			local var_1_9 = {}

			for iter_1_0 = 1, #arg_1_2:
				var_1_9[iter_1_0] = arg_1_2[iter_1_0]

			local var_1_10 = {}

			for iter_1_1, iter_1_2 in ipairs(arg_1_3):
				local var_1_11 = {}

				for iter_1_3, iter_1_4 in ipairs(iter_1_2.value_list):
					table.insert(var_1_11, {
						key = iter_1_4.key,
						value = iter_1_4.value,
						value2 = iter_1_4.value2
					})

				var_1_10[iter_1_2.key] = var_1_11

			var_1_3.elements = var_1_9
			var_1_3.kvpElements = var_1_10

		for iter_1_5, iter_1_6 in pairs(var_1_3):
			var_1_2.SetRuntimeData(iter_1_5, iter_1_6)

return var_0_0
