local var_0_0 = class("GuildAssaultShip", import(".CheckCustomNameShip"))

def var_0_0.IsOwner(arg_1_0):
	return tonumber(GuildAssaultFleet.GetUserId(arg_1_0.id)) == getProxy(PlayerProxy).getRawData().id

def var_0_0.GetUniqueId(arg_2_0):
	return GuildAssaultFleet.GetRealId(arg_2_0.id)

def var_0_0.ConverteFromShip(arg_3_0):
	return setmetatable({}, {
		def __index:(arg_4_0, arg_4_1)
			return var_0_0[arg_4_1] and var_0_0[arg_4_1] or arg_3_0[arg_4_1]
	})

return var_0_0
