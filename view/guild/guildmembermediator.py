local var_0_0 = class("GuildMemberMediator", import("..base.ContextMediator"))

var_0_0.OPEN_DESC_INFO = "GuildMemberMediator.OPEN_DESC_INFO"
var_0_0.FIRE = "GuildMemberMediator.FIRE"
var_0_0.SET_DUTY = "GuildMemberMediator.SET_DUTY"
var_0_0.IMPEACH = "GuildMemberMediator.IMPEACH"
var_0_0.GET_RANK = "GuildMemberMediator.GET_RANK"

def var_0_0.register(arg_1_0):
	local var_1_0 = getProxy(PlayerProxy).getData()

	arg_1_0.viewComponent.setPlayerVO(var_1_0)

	local var_1_1 = getProxy(GuildProxy)

	arg_1_0.viewComponent.setGuildVO(var_1_1.getData())
	arg_1_0.bind(var_0_0.GET_RANK, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.GUILD_GET_RANK, {
			id = arg_2_1
		}))
	arg_1_0.bind(var_0_0.OPEN_DESC_INFO, function(arg_3_0, arg_3_1)
		arg_1_0.sendNotification(GAME.FRIEND_SEARCH, {
			type = SearchFriendCommand.SEARCH_TYPE_RESUME,
			keyword = arg_3_1.id
		}))
	arg_1_0.bind(var_0_0.FIRE, function(arg_4_0, arg_4_1)
		arg_1_0.sendNotification(GAME.GUILD_FIRE, arg_4_1))
	arg_1_0.bind(var_0_0.SET_DUTY, function(arg_5_0, arg_5_1, arg_5_2)
		arg_1_0.sendNotification(GAME.SET_GUILD_DUTY, {
			playerId = arg_5_1,
			dutyId = arg_5_2
		}))
	arg_1_0.bind(var_0_0.IMPEACH, function(arg_6_0, arg_6_1)
		arg_1_0.sendNotification(GAME.GUILD_IMPEACH, arg_6_1))

	local var_1_2 = getProxy(GuildProxy).GetRanks()

	arg_1_0.viewComponent.SetRanks(var_1_2)

def var_0_0.listNotificationInterests(arg_7_0):
	return {
		GuildProxy.GUILD_UPDATED,
		GAME.SET_GUILD_DUTY_DONE,
		GAME.GUILD_FIRE_DONE,
		GAME.FRIEND_SEARCH_DONE,
		GAME.GUILD_GET_RANK_DONE
	}

def var_0_0.handleNotification(arg_8_0, arg_8_1):
	local var_8_0 = arg_8_1.getName()
	local var_8_1 = arg_8_1.getBody()

	if var_8_0 == GuildProxy.GUILD_UPDATED:
		arg_8_0.viewComponent.setGuildVO(var_8_1)
		arg_8_0.viewComponent.RefreshMembers()
	elif var_8_0 == GAME.SET_GUILD_DUTY_DONE:
		arg_8_0.viewComponent.LoadPainting(var_8_1)
	elif var_8_0 == GAME.GUILD_FIRE_DONE:
		arg_8_0.viewComponent.ActiveDefaultMenmber()
	elif var_8_0 == GAME.FRIEND_SEARCH_DONE:
		local var_8_2 = var_8_1.list[1]

		arg_8_0.viewComponent.ShowInfoPanel(var_8_2)
	elif var_8_0 == GAME.GUILD_GET_RANK_DONE:
		local var_8_3 = var_8_1.id
		local var_8_4 = var_8_1.list

		arg_8_0.viewComponent.UpdateRankList(var_8_3, var_8_4)

return var_0_0
