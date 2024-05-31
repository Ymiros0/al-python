local var_0_0 = class("SenrankaguraTrainMediator", import("..base.ContextMediator"))

var_0_0.LEVEL_UP = "level up"
var_0_0.GET_REWARD = "get reward"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.LEVEL_UP, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.SENRANKAGURA_TRAIN_ACT_OP, arg_2_1))
	arg_1_0.bind(var_0_0.GET_REWARD, function(arg_3_0, arg_3_1)
		arg_1_0.sendNotification(GAME.SENRANKAGURA_TRAIN_ACT_OP, arg_3_1))

def var_0_0.initNotificationHandleDic(arg_4_0):
	arg_4_0.handleDic = {
		[GAME.SENRANKAGURA_TRAIN_ACT_OP_DONE] = function(arg_5_0, arg_5_1)
			local var_5_0 = arg_5_1.getBody()

			arg_5_0.viewComponent.LevelUp(var_5_0)
	}

return var_0_0
