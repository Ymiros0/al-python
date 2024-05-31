local var_0_0 = class("VoteScheduleMediator", import("view.base.ContextMediator"))

var_0_0.GO_RANK = "VoteScheduleMediator.GO_RANK"
var_0_0.FETCH_RANK = "VoteScheduleMediator.FETCH_RANK"
var_0_0.ON_VOTE = "VoteScheduleMediator.ON_VOTE"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.ON_VOTE, function()
		local var_2_0 = getProxy(VoteProxy).GetOpeningNonFunVoteGroup() or getProxy(VoteProxy).GetOpeningFunVoteGroup()

		if not var_2_0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_notStartOrEnd"))

			return

		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.VOTE, {
			voteGroup = var_2_0
		}))
	arg_1_0.bind(var_0_0.FETCH_RANK, function(arg_3_0, arg_3_1, arg_3_2)
		arg_1_0.sendNotification(GAME.FETCH_VOTE_RANK, {
			voteId = arg_3_1,
			callback = arg_3_2
		}))
	arg_1_0.bind(var_0_0.GO_RANK, function(arg_4_0, arg_4_1)
		seriesAsync({
			function(arg_5_0)
				arg_1_0.CheckPaintingRes(arg_4_1, arg_5_0)
		}, function()
			arg_1_0.addSubLayers(Context.New({
				mediator = ContextMediator,
				viewComponent = VoteRankScene,
				data = {
					voteGroup = arg_4_1
				}
			}))))

def var_0_0.CheckPaintingRes(arg_7_0, arg_7_1, arg_7_2):
	if arg_7_1 and arg_7_1.isFinalsRace() or arg_7_1.IsFunRace():
		local var_7_0 = arg_7_1.GetRankList()
		local var_7_1 = var_7_0[1]
		local var_7_2 = var_7_0[2]
		local var_7_3 = var_7_0[3]
		local var_7_4 = var_7_1.getPainting()
		local var_7_5 = var_7_2.getPainting()
		local var_7_6 = var_7_3.getPainting()
		local var_7_7 = {
			var_7_4,
			var_7_5,
			var_7_6
		}
		local var_7_8 = {}

		for iter_7_0, iter_7_1 in ipairs(var_7_7):
			PaintingGroupConst.AddPaintingNameWithFilteMap(var_7_8, iter_7_1)

		PaintingGroupConst.PaintingDownload({
			isShowBox = True,
			paintingNameList = var_7_8,
			finishFunc = arg_7_2
		})
	else
		arg_7_2()

def var_0_0.listNotificationInterests(arg_8_0):
	return {}

def var_0_0.handleNotification(arg_9_0, arg_9_1):
	local var_9_0 = arg_9_1.getName()
	local var_9_1 = arg_9_1.getBody()

return var_0_0
