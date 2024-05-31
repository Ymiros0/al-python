local var_0_0 = class("AutoSubCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.isActiveSub
	local var_1_2 = var_1_0.toggle
	local var_1_3 = var_1_0.system
	local var_1_4 = var_0_0.GetAutoSubMark(var_1_3)

	PlayerPrefs.SetInt("autoSubIsAcitve" .. var_1_4, not var_1_1 and 1 or 0)
end

function var_0_0.GetAutoSubMark(arg_2_0)
	if arg_2_0 == SYSTEM_WORLD then
		return "_" .. arg_2_0
	elseif arg_2_0 == SYSTEM_GUILD then
		return "_" .. SYSTEM_GUILD
	else
		return ""
	end
end

return var_0_0
