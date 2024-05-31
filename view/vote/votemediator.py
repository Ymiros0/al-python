local var_0_0 = class("VoteMediator", import("..base.ContextMediator"))

var_0_0.ON_VOTE = "VoteMediator.ON_VOTE"
var_0_0.ON_FILTER = "VoteMediator.ON_FILTER"
var_0_0.ON_SCHEDULE = "VoteMediator.ON_SCHEDULE"
var_0_0.OPEN_EXCHANGE = "VoteMediator.OPEN_EXCHANGE"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.ON_VOTE, function(arg_2_0, arg_2_1, arg_2_2, arg_2_3)
		arg_1_0.sendNotification(GAME.ON_NEW_VOTE, {
			voteId = arg_2_1,
			gid = arg_2_2,
			count = arg_2_3
		}))
	arg_1_0.bind(var_0_0.ON_FILTER, function(arg_3_0, arg_3_1)
		arg_1_0.addSubLayers(Context.New({
			viewComponent = CustomIndexLayer,
			mediator = CustomIndexMediator,
			data = arg_3_1
		})))
	arg_1_0.bind(var_0_0.ON_SCHEDULE, function()
		arg_1_0.addSubLayers(Context.New({
			mediator = VoteScheduleMediator,
			viewComponent = VoteScheduleScene
		})))
	arg_1_0.bind(var_0_0.OPEN_EXCHANGE, function()
		local var_5_0 = getProxy(VoteProxy).GetOpeningNonFunVoteGroup()

		if not var_5_0:
			return

		arg_1_0.addSubLayers(Context.New({
			mediator = VoteExchangeMediator,
			viewComponent = VoteExchangeScene,
			data = {
				voteGroup = var_5_0
			}
		})))

def var_0_0.listNotificationInterests(arg_6_0):
	return {
		GAME.ON_NEW_VOTE_DONE,
		GAME.ACT_NEW_PT_DONE
	}

def var_0_0.handleNotification(arg_7_0, arg_7_1):
	local var_7_0 = arg_7_1.getName()
	local var_7_1 = arg_7_1.getBody()

	if var_7_0 == GAME.ON_NEW_VOTE_DONE:
		arg_7_0.viewComponent.updateMainview(False)
		pg.TipsMgr.GetInstance().ShowTips(i18n("vote_success"))
		arg_7_0.DisplayAwards(var_7_1.awards)
	elif var_7_0 == GAME.ACT_NEW_PT_DONE:
		arg_7_0.DisplayAwards(var_7_1.awards)

def var_0_0.DisplayAwards(arg_8_0, arg_8_1):
	local var_8_0

	local function var_8_1()
		if #arg_8_0.cache <= 0:
			return

		local var_9_0 = arg_8_0.cache[1]

		arg_8_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_9_0, function()
			table.remove(arg_8_0.cache, 1)
			var_8_1())

	if not arg_8_0.cache:
		arg_8_0.cache = {}

	table.insert(arg_8_0.cache, arg_8_1)

	if #arg_8_0.cache == 1:
		var_8_1()

return var_0_0
