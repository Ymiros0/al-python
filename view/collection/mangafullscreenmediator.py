local var_0_0 = class("MangaFullScreenMediator", import("..base.ContextMediator"))

def var_0_0.register(arg_1_0):
	return

def var_0_0.listNotificationInterests(arg_2_0):
	return {
		GAME.APPRECIATE_MANGA_READ_DONE,
		GAME.APPRECIATE_MANGA_LIKE_DONE
	}

def var_0_0.handleNotification(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_1.getName()
	local var_3_1 = arg_3_1.getBody()

	if var_3_0 == GAME.APPRECIATE_MANGA_READ_DONE:
		local var_3_2 = var_3_1.mangaID

		if arg_3_0.contextData.mangaContext:
			arg_3_0.contextData.mangaContext.updateLineAfterRead(var_3_2)
	elif var_3_0 == GAME.APPRECIATE_MANGA_LIKE_DONE:
		arg_3_0.viewComponent.updateLikeBtn()

return var_0_0
