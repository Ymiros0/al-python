local var_0_0 = class("VoteEntranceMediator", import("view.base.ContextMediator"))

var_0_0.ON_VOTE = "VoteEntranceMediator.ON_VOTE"
var_0_0.ON_FUN_VOTE = "VoteEntranceMediator.ON_FUN_VOTE"
var_0_0.ON_EXCHANGE = "VoteEntranceMediator.ON_EXCHANGE"
var_0_0.ON_SCHEDULE = "VoteEntranceMediator.ON_SCHEDULE"
var_0_0.GO_HALL = "VoteEntranceMediator.GO_HALL"
var_0_0.SUBMIT_TASK = "VoteEntranceMediator.SUBMIT_TASK"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.SUBMIT_TASK, function()
		local var_2_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.VOTE_ENTRANCE_ACT_ID)

		if not var_2_0 or var_2_0.isEnd():
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_notStartOrEnd"))

			return

		local var_2_1 = var_2_0.getConfig("config_client")[2]

		arg_1_0.sendNotification(GAME.SUBMIT_TASK, var_2_1))
	arg_1_0.bind(var_0_0.ON_VOTE, function()
		local var_3_0 = getProxy(VoteProxy).GetOpeningNonFunVoteGroup()

		if not var_3_0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("vote_tip_area_closed"))

			return

		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.VOTE, {
			voteGroup = var_3_0
		}))
	arg_1_0.bind(var_0_0.ON_FUN_VOTE, function()
		local var_4_0 = getProxy(VoteProxy).GetOpeningFunVoteGroup()

		if not var_4_0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("vote_tip_area_closed"))

			return

		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.VOTE, {
			voteGroup = var_4_0
		}))
	arg_1_0.bind(var_0_0.ON_EXCHANGE, function()
		local var_5_0 = getProxy(VoteProxy).GetOpeningNonFunVoteGroup()

		if not var_5_0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_notStartOrEnd"))

			return

		arg_1_0.addSubLayers(Context.New({
			mediator = VoteExchangeMediator,
			viewComponent = VoteExchangeScene,
			data = {
				voteGroup = var_5_0
			}
		})))
	arg_1_0.bind(var_0_0.ON_SCHEDULE, function()
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.VOTESCHEDULE))
	arg_1_0.bind(var_0_0.GO_HALL, function()
		arg_1_0.addSubLayers(Context.New({
			mediator = VoteFameHallMediator,
			viewComponent = VoteFameHallLayer
		})))

def var_0_0.listNotificationInterests(arg_8_0):
	return {
		GAME.SUBMIT_TASK_DONE,
		GAME.ON_NEW_VOTE_DONE,
		GAME.STORY_END
	}

def var_0_0.handleNotification(arg_9_0, arg_9_1):
	local var_9_0 = arg_9_1.getName()
	local var_9_1 = arg_9_1.getBody()

	if var_9_0 == GAME.SUBMIT_TASK_DONE:
		arg_9_0.viewComponent.UpdateHonorTip()
		arg_9_0.viewComponent.UpdateMainAward()
		arg_9_0.viewComponent.UpdateMainStageTip()
		arg_9_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_9_1, None)
	elif var_9_0 == GAME.ON_NEW_VOTE_DONE:
		arg_9_0.viewComponent.UpdateVotes()
		arg_9_0.viewComponent.UpdateMainStageTip()
		arg_9_0.viewComponent.UpdateSubStageTip()
	elif var_9_0 == GAME.STORY_END:
		arg_9_0.viewComponent.FlushAll()

return var_0_0
