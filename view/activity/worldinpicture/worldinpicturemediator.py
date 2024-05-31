local var_0_0 = class("WorldInPictureMediator", import("...base.ContextMediator"))

var_0_0.ON_TRAVEL = "WorldInPictureMediator.ON_TRAVEL"
var_0_0.ON_DRAW = "WorldInPictureMediator.ON_DRAW"
var_0_0.ON_AUTO_TRAVEL = "WorldInPictureMediator.ON_AUTO_TRAVEL"
var_0_0.ON_AUTO_DRAW = "WorldInPictureMediator.ON_AUTO_DRAW"
var_0_0.RESULT_ONEKEY_AWARD = "WorldInPictureMediator.RESULT_ONEKEY_AWARD"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.ON_AUTO_TRAVEL, function(arg_2_0, arg_2_1, arg_2_2, arg_2_3)
		arg_1_0.sendNotification(GAME.WORLDIN_PICTURE_OP, {
			auto = True,
			cmd = ActivityConst.WORLDINPICTURE_OP_TURN,
			arg1 = arg_2_1,
			arg2 = arg_2_2,
			index = arg_2_3
		}))
	arg_1_0.bind(var_0_0.ON_AUTO_DRAW, function(arg_3_0, arg_3_1, arg_3_2, arg_3_3)
		arg_1_0.sendNotification(GAME.WORLDIN_PICTURE_OP, {
			auto = True,
			cmd = ActivityConst.WORLDINPICTURE_OP_DRAW,
			arg1 = arg_3_1,
			arg2 = arg_3_2,
			index = arg_3_3
		}))
	arg_1_0.bind(var_0_0.ON_TRAVEL, function(arg_4_0, arg_4_1, arg_4_2, arg_4_3)
		arg_1_0.sendNotification(GAME.WORLDIN_PICTURE_OP, {
			cmd = ActivityConst.WORLDINPICTURE_OP_TURN,
			arg1 = arg_4_1,
			arg2 = arg_4_2,
			index = arg_4_3
		}))
	arg_1_0.bind(var_0_0.ON_DRAW, function(arg_5_0, arg_5_1, arg_5_2, arg_5_3)
		arg_1_0.sendNotification(GAME.WORLDIN_PICTURE_OP, {
			cmd = ActivityConst.WORLDINPICTURE_OP_DRAW,
			arg1 = arg_5_1,
			arg2 = arg_5_2,
			index = arg_5_3
		}))
	arg_1_0.bind(var_0_0.RESULT_ONEKEY_AWARD, function(arg_6_0)
		if #arg_1_0.cacheAwards > 0:
			arg_1_0.viewComponent.emit(BaseUI.ON_ACHIEVE, arg_1_0.cacheAwards, function()
				arg_1_0.cacheAwards = {}))

	arg_1_0.cacheAwards = {}

	local var_1_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_WORLDINPICTURE)
	local var_1_1 = WorldInPictureActiviyData.New(var_1_0)

	arg_1_0.viewComponent.SetData(var_1_1)

def var_0_0.listNotificationInterests(arg_8_0):
	return {
		GAME.WORLDIN_PICTURE_OP_DONE,
		GAME.WORLDIN_PICTURE_OP_ERRO
	}

def var_0_0.handleNotification(arg_9_0, arg_9_1):
	local var_9_0 = arg_9_1.getName()
	local var_9_1 = arg_9_1.getBody()

	if var_9_0 == GAME.WORLDIN_PICTURE_OP_DONE:
		local var_9_2 = WorldInPictureActiviyData.New(var_9_1.activity)

		arg_9_0.viewComponent.SetData(var_9_2)

		if #var_9_1.awards > 0:
			if not var_9_1.auto:
				arg_9_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_9_1.awards)
			else
				for iter_9_0, iter_9_1 in ipairs(var_9_1.awards):
					table.insert(arg_9_0.cacheAwards, iter_9_1)

		if var_9_1.cmd == ActivityConst.WORLDINPICTURE_OP_TURN:
			arg_9_0.viewComponent.OnOpenCell(var_9_1.arg1, var_9_1.arg2, var_9_1.auto)
		elif var_9_1.cmd == ActivityConst.WORLDINPICTURE_OP_DRAW:
			arg_9_0.viewComponent.OnDrawArea(var_9_1.arg1, var_9_1.arg2, var_9_1.auto)
	elif var_9_0 == GAME.WORLDIN_PICTURE_OP_ERRO:
		if var_9_1.cmd == ActivityConst.WORLDINPICTURE_OP_TURN:
			arg_9_0.viewComponent.OnOpenCellErro(var_9_1.auto)
		elif var_9_1.cmd == ActivityConst.WORLDINPICTURE_OP_DRAW:
			arg_9_0.viewComponent.OnDrawAreaErro(var_9_1.auto)

return var_0_0
