local var_0_0 = class("EmojiMediator", import("..base.ContextMediator"))

def var_0_0.register(arg_1_0):
	if not getProxy(EmojiProxy).getInitedTag():
		arg_1_0.sendNotification(GAME.REQUEST_EMOJI_INFO_FROM_SERVER)

def var_0_0.listNotificationInterests(arg_2_0):
	return {
		GAME.REQUEST_EMOJI_INFO_FROM_SERVER_DONE
	}

def var_0_0.handleNotification(arg_3_0, arg_3_1):
	return

return var_0_0
