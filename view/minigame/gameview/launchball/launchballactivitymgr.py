local var_0_0 = class("LaunchBallActivityMgr")

def var_0_0.GetRoundCount(arg_1_0):
	local var_1_0 = LaunchBallActivityMgr.GetActivityById(arg_1_0)

	if not var_1_0:
		return 0

	if var_1_0.data1 and var_1_0.data1 > 0:
		return var_1_0.data1

	return 0

def var_0_0.GetRoundCountMax(arg_2_0):
	local var_2_0 = LaunchBallActivityMgr.GetActivityById(arg_2_0)

	if not var_2_0:
		return 0

	return #var_2_0.getConfig("config_data")[1]

def var_0_0.GotInvitationFlag(arg_3_0):
	return LaunchBallActivityMgr.GetActivityById(arg_3_0).data3 == 1

def var_0_0.GetActivityDay(arg_4_0):
	local var_4_0 = LaunchBallActivityMgr.GetActivityById(arg_4_0)

	if var_4_0:
		return var_4_0.getDayIndex()

	return 0

def var_0_0.GetRemainCount(arg_5_0):
	return LaunchBallActivityMgr.GetActivityDay(arg_5_0) - LaunchBallActivityMgr.GetRoundCount(arg_5_0)

def var_0_0.IsTip(arg_6_0):
	return LaunchBallActivityMgr.GetRemainCount(arg_6_0) > 0

def var_0_0.GetInvitationAble(arg_7_0):
	if LaunchBallActivityMgr.GotInvitationFlag(arg_7_0):
		return False

	return LaunchBallActivityMgr.GetRoundCount(arg_7_0) >= LaunchBallActivityMgr.GetRoundCountMax(arg_7_0)

def var_0_0.GetInvitation(arg_8_0):
	if LaunchBallActivityMgr.GetInvitationAble(arg_8_0):
		pg.m02.sendNotification(GAME.ACTIVITY_OPERATION, {
			cmd = 2,
			activity_id = arg_8_0
		})

def var_0_0.GetInvitationDropId(arg_9_0):
	return LaunchBallActivityMgr.GetActivityById(arg_9_0).getConfig("config_data")[6]

def var_0_0.GetActivityById(arg_10_0):
	return getProxy(ActivityProxy).getActivityById(arg_10_0)

def var_0_0.GetZhuanShuCount(arg_11_0):
	local var_11_0 = LaunchBallActivityMgr.GetActivityById(arg_11_0)

	if not var_11_0:
		return 0

	return var_11_0.data1_list or {}

def var_0_0.GetZhuanShuItems(arg_12_0, arg_12_1):
	local var_12_0 = LaunchBallActivityMgr.GetActivityById(arg_12_0)

	if not var_12_0:
		return 0

	return var_12_0.getConfig("config_data")[4][1][arg_12_1]

def var_0_0.IsFinishZhuanShu(arg_13_0, arg_13_1):
	if not LaunchBallActivityMgr.GetActivityById(arg_13_0):
		return 0

	local var_13_0 = LaunchBallActivityMgr.GetZhuanShuCount(arg_13_0)

	return var_13_0 and table.contains(var_13_0, arg_13_1)

def var_0_0.CheckZhuanShuAble(arg_14_0, arg_14_1):
	local var_14_0 = LaunchBallActivityMgr.GetZhuanShuItems(arg_14_0, arg_14_1)
	local var_14_1

	if var_14_0:
		var_14_1 = getProxy(BagProxy).getItemById(var_14_0)

	return var_14_1 != None

def var_0_0.GetPlayerZhuanshuIndex(arg_15_0):
	if arg_15_0 > 1:
		return arg_15_0 - 1

	return None

def var_0_0.GetGameScore(arg_16_0, arg_16_1):
	local var_16_0 = LaunchBallActivityMgr.GetActivityById(arg_16_0)

	if not var_16_0:
		return 0

	return var_16_0.data2 or 0

def var_0_0.OpenGame(arg_17_0, arg_17_1):
	LaunchBallGameVo.initRoundData(arg_17_0, arg_17_1)
	pg.m02.sendNotification(GAME.GO_MINI_GAME, 57)

def var_0_0.GetGameAward(arg_18_0, arg_18_1, arg_18_2, arg_18_3):
	local var_18_0 = LaunchBallActivityMgr.GetActivityById(arg_18_0)

	if not var_18_0:
		return

	local var_18_1 = LaunchBallActivityMgr.GetRoundCount(arg_18_0)
	local var_18_2 = LaunchBallActivityMgr.GetActivityDay(arg_18_0)
	local var_18_3 = LaunchBallActivityMgr.GetRoundCountMax(arg_18_0)
	local var_18_4 = var_18_0.data2
	local var_18_5 = LaunchBallActivityMgr.GetGameScores(arg_18_0)

	if arg_18_1 == LaunchBallGameConst.round_type_juqing:
		if var_18_2 <= var_18_1:
			print("活动天数不足")

			return

		if var_18_1 < var_18_3 and arg_18_2 <= var_18_1:
			print("已经领过剧情关奖励")

			return

		if arg_18_2 > var_18_1 + 1:
			print("上一关还未解锁")

			return

		pg.m02.sendNotification(GAME.ACTIVITY_OPERATION, {
			cmd = 1,
			activity_id = arg_18_0,
			arg1 = arg_18_1,
			arg2 = arg_18_2,
			arg3 = math.floor(LaunchBallGameVo.gameStepTime)
		})
	elif arg_18_1 == LaunchBallGameConst.round_type_wuxian:
		if var_18_1 < var_18_3:
			print("还没有完全通关剧情关卡")

			return

		if arg_18_3 <= var_18_4:
			print("没有超过往期的最大分数")

			return

		local var_18_6 = False

		for iter_18_0 = 1, #var_18_5:
			if not var_18_6 and arg_18_3 >= var_18_5[iter_18_0][1] and var_18_4 < var_18_5[iter_18_0][1]:
				var_18_6 = True

		if var_18_6:
			pg.m02.sendNotification(GAME.ACTIVITY_OPERATION, {
				cmd = 1,
				activity_id = arg_18_0,
				arg1 = arg_18_1,
				arg2 = arg_18_3,
				arg3 = math.floor(LaunchBallGameVo.gameStepTime)
			})
	else
		if not LaunchBallActivityMgr.CheckZhuanShuAble(arg_18_0, arg_18_2):
			print("专属关卡没有解锁")

			return

		pg.m02.sendNotification(GAME.ACTIVITY_OPERATION, {
			cmd = 1,
			activity_id = arg_18_0,
			arg1 = arg_18_1,
			arg2 = arg_18_2,
			arg3 = math.floor(LaunchBallGameVo.gameStepTime)
		})

def var_0_0.GetGameScores(arg_19_0):
	local var_19_0 = LaunchBallActivityMgr.GetActivityById(arg_19_0)

	if not var_19_0:
		return 0

	return var_19_0.getConfig("config_data")[5]

def var_0_0.GetGamePtId(arg_20_0):
	local var_20_0 = LaunchBallActivityMgr.GetActivityById(arg_20_0)

	if not var_20_0:
		return 0

	return var_20_0.getConfig("config_data")[2]

return var_0_0
