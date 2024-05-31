local var_0_0 = class("PublicGuildMainMediator", import("...base.ContextMediator"))

var_0_0.ON_COMMIT = "PublicGuildMainMediator.ON_COMMIT"
var_0_0.UPGRADE_TECH = "PublicGuildMainMediator.UPGRADE_TECH"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.ON_COMMIT, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.PUBLIC_GUILD_COMMIT_DONATE, {
			id = arg_2_1
		}))
	arg_1_0.bind(var_0_0.UPGRADE_TECH, function(arg_3_0, arg_3_1)
		arg_1_0.sendNotification(GAME.PULIC_GUILD_UPGRADE_TECH, {
			id = arg_3_1
		}))

	local var_1_0 = getProxy(GuildProxy).GetPublicGuild()

	arg_1_0.viewComponent.SetPublicGuild(var_1_0)
	arg_1_0.viewComponent.SetPlayer(getProxy(PlayerProxy).getData())

def var_0_0.listNotificationInterests(arg_4_0):
	return {
		GAME.PUBLIC_GUILD_COMMIT_DONATE_DONE,
		GAME.PUBLIC_GUILD_REFRESH_DONATE_LIST_DONE,
		PlayerProxy.UPDATED,
		GAME.PULIC_GUILD_UPGRADE_TECH_DONE,
		GAME.GET_PUBLIC_GUILD_USER_DATA_DONE
	}

def var_0_0.handleNotification(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_1.getName()
	local var_5_1 = arg_5_1.getBody()

	if var_5_0 == GAME.PUBLIC_GUILD_COMMIT_DONATE_DONE:
		arg_5_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_5_1.awards)
		arg_5_0.viewComponent.OnUpdateDonateList()
	elif var_5_0 == GAME.PUBLIC_GUILD_REFRESH_DONATE_LIST_DONE:
		arg_5_0.viewComponent.OnUpdateDonateList()
	elif var_5_0 == PlayerProxy.UPDATED:
		arg_5_0.viewComponent.OnPlayerUpdate(var_5_1)
	elif var_5_0 == GAME.PULIC_GUILD_UPGRADE_TECH_DONE:
		arg_5_0.viewComponent.OnTechGroupUpdate(var_5_1.id)
	elif var_5_0 == GAME.GET_PUBLIC_GUILD_USER_DATA_DONE:
		local var_5_2 = getProxy(GuildProxy).GetPublicGuild()

		arg_5_0.viewComponent.SetPublicGuild(var_5_2)
		arg_5_0.viewComponent.RefreshAll()

return var_0_0
