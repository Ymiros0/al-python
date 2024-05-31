local var_0_0 = class("JoinGuildMediator", import("..base.ContextMediator"))

var_0_0.APPLY = "JoinGuildMediator.APPLY"
var_0_0.REFRESH = "JoinGuildMediator.REFRESH"
var_0_0.SEARCH = "JoinGuildMediator.SEARCH"

def var_0_0.register(arg_1_0):
	arg_1_0.sendNotification(GAME.GUILD_LIST_REFRESH)

	local var_1_0 = getProxy(PlayerProxy).getData()

	arg_1_0.viewComponent.setPlayerVO(var_1_0)
	arg_1_0.bind(var_0_0.APPLY, function(arg_2_0, arg_2_1, arg_2_2)
		arg_1_0.sendNotification(GAME.GUILD_APPLY, {
			id = arg_2_1,
			content = arg_2_2
		}))
	arg_1_0.bind(var_0_0.REFRESH, function(arg_3_0)
		arg_1_0.sendNotification(GAME.GUILD_LIST_REFRESH))
	arg_1_0.bind(var_0_0.SEARCH, function(arg_4_0, arg_4_1)
		arg_1_0.sendNotification(GAME.GUILD_SEARCH, arg_4_1))

def var_0_0.listNotificationInterests(arg_5_0):
	return {
		GAME.GUILD_LIST_REFRESH_DONE,
		GAME.GUILD_SEARCH_DONE,
		GAME.GUILD_APPLY_DONE,
		GAME.REMOVE_LAYERS
	}

def var_0_0.handleNotification(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_1.getName()
	local var_6_1 = arg_6_1.getBody()

	if var_6_0 == GAME.GUILD_LIST_REFRESH_DONE or var_6_0 == GAME.GUILD_SEARCH_DONE:
		arg_6_0.viewComponent.setGuildVOs(var_6_1)

		if arg_6_0.contextData.filterData:
			arg_6_0.viewComponent.filter()
		else
			arg_6_0.viewComponent.sortGuilds()
	elif var_6_0 == GAME.GUILD_APPLY_DONE:
		arg_6_0.viewComponent.CloseApply()

return var_0_0
