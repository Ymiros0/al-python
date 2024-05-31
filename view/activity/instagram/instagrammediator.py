local var_0_0 = class("InstagramMediator", import("...base.ContextMediator"))

var_0_0.ON_LIKE = "InstagramMediator.ON_LIKE"
var_0_0.ON_SHARE = "InstagramMediator.ON_SHARE"
var_0_0.ON_COMMENT = "InstagramMediator.ON_COMMENT"
var_0_0.ON_REPLY_UPDATE = "InstagramMediator.ON_REPLY_UPDATE"
var_0_0.ON_READED = "InstagramMediator.ON_READED"
var_0_0.ON_COMMENT_LIST_UPDATE = "InstagramMediator.ON_COMMENT_LIST_UPDATE"

def var_0_0.register(arg_1_0):
	getProxy(InstagramProxy).InitLocalConfigs()
	arg_1_0.bind(var_0_0.ON_READED, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.ACT_INSTAGRAM_OP, {
			arg2 = 0,
			cmd = ActivityConst.INSTAGRAM_OP_MARK_READ,
			arg1 = arg_2_1
		}))
	arg_1_0.bind(var_0_0.ON_LIKE, function(arg_3_0, arg_3_1)
		arg_1_0.sendNotification(GAME.ACT_INSTAGRAM_OP, {
			arg2 = 0,
			cmd = ActivityConst.INSTAGRAM_OP_LIKE,
			arg1 = arg_3_1
		}))
	arg_1_0.bind(var_0_0.ON_SHARE, function(arg_4_0, arg_4_1)
		arg_1_0.sendNotification(GAME.ACT_INSTAGRAM_OP, {
			arg2 = 0,
			cmd = ActivityConst.INSTAGRAM_OP_SHARE,
			arg1 = arg_4_1
		}))
	arg_1_0.bind(var_0_0.ON_COMMENT, function(arg_5_0, arg_5_1, arg_5_2, arg_5_3)
		arg_1_0.sendNotification(GAME.ACT_INSTAGRAM_OP, {
			cmd = ActivityConst.INSTAGRAM_OP_COMMENT,
			arg1 = arg_5_1,
			arg2 = arg_5_3,
			arg3 = arg_5_2
		}))
	arg_1_0.bind(var_0_0.ON_REPLY_UPDATE, function(arg_6_0, arg_6_1)
		arg_1_0.sendNotification(GAME.ACT_INSTAGRAM_OP, {
			arg2 = 0,
			cmd = ActivityConst.INSTAGRAM_OP_UPDATE,
			arg1 = arg_6_1,
			def callback:()
				arg_1_0.viewComponent.UpdateCommentList()
		}))
	arg_1_0.bind(var_0_0.ON_COMMENT_LIST_UPDATE, function(arg_8_0, arg_8_1, arg_8_2)
		arg_1_0.viewComponent.UpdateInstagram(arg_8_2, False)

		if arg_1_0.contextData.instagram:
			arg_1_0.viewComponent.emit(var_0_0.ON_REPLY_UPDATE, arg_8_1, arg_8_2))
	arg_1_0.viewComponent.SetProxy(getProxy(InstagramProxy))

def var_0_0.listNotificationInterests(arg_9_0):
	return {
		GAME.ACT_INSTAGRAM_OP_DONE
	}

def var_0_0.handleNotification(arg_10_0, arg_10_1):
	local var_10_0 = arg_10_1.getName()
	local var_10_1 = arg_10_1.getBody()

	local function var_10_2()
		arg_10_0.viewComponent.SetProxy(getProxy(InstagramProxy))
		arg_10_0.viewComponent.UpdateInstagram(var_10_1.id)
		arg_10_0.viewComponent.UpdateSelectedInstagram(var_10_1.id)

	if var_10_0 == GAME.ACT_INSTAGRAM_OP_DONE:
		arg_10_0.viewComponent.SetProxy(getProxy(InstagramProxy))

		if var_10_1.cmd == ActivityConst.INSTAGRAM_OP_SHARE:
			pg.ShareMgr.GetInstance().Share(pg.ShareMgr.TypeInstagram)
		elif var_10_1.cmd == ActivityConst.INSTAGRAM_OP_LIKE:
			var_10_2()
			arg_10_0.viewComponent.UpdateLikeBtn()
			pg.TipsMgr.GetInstance().ShowTips(i18n("ins_click_like_success"))
		elif var_10_1.cmd == ActivityConst.INSTAGRAM_OP_COMMENT:
			pg.TipsMgr.GetInstance().ShowTips(i18n("ins_push_comment_success"))
			var_10_2()
		elif var_10_1.cmd == ActivityConst.INSTAGRAM_OP_ACTIVE or var_10_1.cmd == ActivityConst.INSTAGRAM_OP_UPDATE:
			arg_10_0.viewComponent.InitList()
			var_10_2()
		elif var_10_1.cmd == ActivityConst.INSTAGRAM_OP_MARK_READ:
			var_10_2()

return var_0_0
