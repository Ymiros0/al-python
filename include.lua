pg = pg or {}
ys = ys or {}
cs = cs or {}

local function var_0_0(arg_1_0)
	return string.gsub(arg_1_0 or "", "<%[(.-)%]>", function(arg_2_0)
		local var_2_0 = pg.equip_data_code[arg_2_0]

		return var_2_0 and var_2_0.text
	end)
end

local function var_0_1(arg_3_0, arg_3_1)
	return function(arg_4_0, arg_4_1)
		local var_4_0 = arg_4_0.__name

		if arg_3_0 == 1 and cs[var_4_0][arg_4_1] then
			LuaHelper.SetConfVal(var_4_0, cs[var_4_0][arg_4_1][1], cs[var_4_0][arg_4_1][2])
		end

		if arg_3_0 == 2 and cs[var_4_0].indexs[arg_4_1] then
			local var_4_1 = cs[var_4_0].subList[cs[var_4_0].indexs[arg_4_1]]

			if pg.base[var_4_1] == nil then
				require("ShareCfg." .. cs[var_4_0].subFolderName .. "." .. var_4_1)
			end

			var_4_0 = var_4_1
		end

		local var_4_2 = pg.base[var_4_0][arg_4_1]

		if not var_4_2 then
			return nil
		end

		local var_4_3 = {}

		for iter_4_0, iter_4_1 in pairs(var_4_2) do
			if type(iter_4_1) == "string" then
				var_4_3[iter_4_0] = var_0_0(iter_4_1)

				if arg_3_1 then
					var_4_3[iter_4_0] = HXSet.hxLan(var_4_3[iter_4_0])
				end
			end
		end

		local var_4_4 = rawget(var_4_2, "base")

		if var_4_4 ~= nil then
			arg_4_0[arg_4_1] = setmetatable(var_4_3, {
				__index = function(arg_5_0, arg_5_1)
					if var_4_2[arg_5_1] == nil then
						return arg_4_0[var_4_4][arg_5_1]
					else
						return var_4_2[arg_5_1]
					end
				end
			})
		else
			arg_4_0[arg_4_1] = setmetatable(var_4_3, {
				__index = var_4_2
			})
		end

		return arg_4_0[arg_4_1]
	end
end

confSP = confSP or {
	__index = var_0_1(2, true)
}
confMT = confMT or {
	__index = var_0_1(1, true)
}
confHX = confHX or {
	__index = var_0_1(0, true)
}

require("localConfig")
require("const")
require("config")
setmetatable(pg, {
	__index = function(arg_6_0, arg_6_1)
		local var_6_0 = "ShareCfg." .. arg_6_1

		if ShareCfg[var_6_0] then
			require(var_6_0)

			return rawget(pg, arg_6_1)
		end
	end
})

ERROR_MESSAGE = setmetatable({}, {
	__index = function(arg_7_0, arg_7_1)
		if pg.error_message[arg_7_1] then
			return pg.error_message[arg_7_1].desc
		else
			return "none"
		end
	end
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
