pg = pg or {}
ys = ys or {}
cs = cs or {}

local function var_0_0(arg_1_0)
	return string.gsub(arg_1_0 or "", "<%[(.-)%]>", function(arg_2_0)
		local var_2_0 = pg.equip_data_code[arg_2_0]

		return var_2_0 and var_2_0.text)

local function var_0_1(arg_3_0, arg_3_1)
	return function(arg_4_0, arg_4_1)
		local var_4_0 = arg_4_0.__name

		if arg_3_0 == 1 and cs[var_4_0][arg_4_1]:
			LuaHelper.SetConfVal(var_4_0, cs[var_4_0][arg_4_1][1], cs[var_4_0][arg_4_1][2])

		if arg_3_0 == 2 and cs[var_4_0].indexs[arg_4_1]:
			local var_4_1 = cs[var_4_0].subList[cs[var_4_0].indexs[arg_4_1]]

			if pg.base[var_4_1] == None:
				require("ShareCfg." .. cs[var_4_0].subFolderName .. "." .. var_4_1)

			var_4_0 = var_4_1

		local var_4_2 = pg.base[var_4_0][arg_4_1]

		if not var_4_2:
			return None

		local var_4_3 = {}

		for iter_4_0, iter_4_1 in pairs(var_4_2):
			if type(iter_4_1) == "string":
				var_4_3[iter_4_0] = var_0_0(iter_4_1)

				if arg_3_1:
					var_4_3[iter_4_0] = HXSet.hxLan(var_4_3[iter_4_0])

		local var_4_4 = rawget(var_4_2, "base")

		if var_4_4 != None:
			arg_4_0[arg_4_1] = setmetatable(var_4_3, {
				def __index:(arg_5_0, arg_5_1)
					if var_4_2[arg_5_1] == None:
						return arg_4_0[var_4_4][arg_5_1]
					else
						return var_4_2[arg_5_1]
			})
		else
			arg_4_0[arg_4_1] = setmetatable(var_4_3, {
				__index = var_4_2
			})

		return arg_4_0[arg_4_1]

confSP = confSP or {
	__index = var_0_1(2, True)
}
confMT = confMT or {
	__index = var_0_1(1, True)
}
confHX = confHX or {
	__index = var_0_1(0, True)
}

require("localConfig")
require("const")
require("config")
setmetatable(pg, {
	def __index:(arg_6_0, arg_6_1)
		local var_6_0 = "ShareCfg." .. arg_6_1

		if ShareCfg[var_6_0]:
			require(var_6_0)

			return rawget(pg, arg_6_1)
})

ERROR_MESSAGE = setmetatable({}, {
	def __index:(arg_7_0, arg_7_1)
		if pg.error_message[arg_7_1]:
			return pg.error_message[arg_7_1].desc
		else
			return "none"
})
BVCurIndex = 1
BVLastIndex = 1

require("Support/Utils/HXSet")
require("Framework/Include")
require("Support/Include")
require("Net/Include")
require("Mgr/Include")
require("GameCfg/Include")
require("Mod/Battle/Include")
require("skillCfg")
require("buffCfg")
require("cardCfg")
require("genVertify")
require("buffFXPreloadList")
