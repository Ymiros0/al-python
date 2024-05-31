local var_0_0 = class("LimitChallengeMediator", import("..base.ContextMediator"))

def var_0_0.register(arg_1_0):
	arg_1_0.bindEvent()
	arg_1_0.tryGetAward()

def var_0_0.listNotificationInterests(arg_2_0):
	return {
		LimitChallengeConst.REQ_CHALLENGE_INFO_DONE,
		LimitChallengeConst.GET_CHALLENGE_AWARD_DONE,
		LimitChallengeConst.UPDATE_PASS_TIME
	}

def var_0_0.handleNotification(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_1.getName()
	local var_3_1 = arg_3_1.getBody()

	if var_3_0 == LimitChallengeConst.REQ_CHALLENGE_INFO_DONE:
		arg_3_0.viewComponent.onReqInfo()
	elif var_3_0 == LimitChallengeConst.GET_CHALLENGE_AWARD_DONE:
		arg_3_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_3_1.awards)
		arg_3_0.viewComponent.updateToggleList()
		arg_3_0.viewComponent.trigeHigestUnlockLevel()
	elif var_3_0 == LimitChallengeConst.UPDATE_PASS_TIME:
		arg_3_0.viewComponent.updatePassTime()

def var_0_0.bindEvent(arg_4_0):
	arg_4_0.bind(LimitChallengeConst.OPEN_PRE_COMBAT_LAYER, function(arg_5_0, arg_5_1)
		local var_5_0 = arg_5_1.stageID
		local var_5_1 = Context.New({
			mediator = LimitChallengePreCombatMediator,
			viewComponent = LimitChallengePreCombatLayer,
			data = {
				stageId = var_5_0,
				system = SYSTEM_LIMIT_CHALLENGE
			}
		})

		arg_4_0.addSubLayers(var_5_1))

def var_0_0.tryGetAward(arg_6_0):
	local var_6_0 = getProxy(LimitChallengeProxy).getMissAwardChallengeIDLIst()

	if #var_6_0 > 0:
		arg_6_0.sendNotification(LimitChallengeConst.GET_CHALLENGE_AWARD, {
			challengeIDList = var_6_0
		})

return var_0_0
