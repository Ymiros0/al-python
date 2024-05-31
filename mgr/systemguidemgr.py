pg = pg or {}
pg.SystemGuideMgr = singletonClass("SystemGuideMgr")

local var_0_0 = pg.SystemGuideMgr
local var_0_1

def var_0_0.Init(arg_1_0, arg_1_1):
	var_0_1 = require("GameCfg.guide.newguide.SSG001")

	arg_1_1()

local function var_0_2(arg_2_0)
	if getProxy(PlayerProxy):
		return pg.NewStoryMgr.GetInstance().IsPlayed(arg_2_0)

	return False

local function var_0_3(arg_3_0)
	if arg_3_0:
		arg_3_0()

local function var_0_4(arg_4_0, arg_4_1, arg_4_2)
	if pg.SeriesGuideMgr.GetInstance().isRunning():
		var_0_3(arg_4_2)

		return

	if var_0_2(arg_4_0):
		var_0_3(arg_4_2)

		return

	if not pg.NewGuideMgr.GetInstance().CanPlay():
		var_0_3(arg_4_2)

		return

	if arg_4_0 == "SYG001":
		pg.TrackerMgr.GetInstance().Tracking(TRACKING_TUTORIAL_COMPLETE_2)
	elif arg_4_0 == "SYG003":
		pg.TrackerMgr.GetInstance().Tracking(TRACKING_TUTORIAL_COMPLETE_3)
	elif arg_4_0 == "SYG006":
		pg.TrackerMgr.GetInstance().Tracking(TRACKING_TUTORIAL_COMPLETE_4)

	pg.m02.sendNotification(GAME.STORY_UPDATE, {
		storyId = arg_4_0
	})
	pg.NewGuideMgr.GetInstance().Play(arg_4_0, arg_4_1, arg_4_2)

def var_0_0.Play(arg_5_0, arg_5_1, arg_5_2):
	if IsUnityEditor and not ENABLE_GUIDE:
		if arg_5_2:
			arg_5_2()

		return

	if arg_5_1.exited:
		return

	local var_5_0 = var_0_1[arg_5_1.__cname]

	if not var_5_0:
		var_0_3(arg_5_2)

		return

	local var_5_1 = _.detect(var_5_0, function(arg_6_0)
		local var_6_0 = arg_6_0.id
		local var_6_1 = arg_6_0.condition

		return not var_0_2(var_6_0) and var_6_1(arg_5_1))

	if not var_5_1:
		var_0_3(arg_5_2)

		return

	local var_5_2 = var_5_1.id
	local var_5_3 = var_5_1.args(arg_5_1)

	var_0_4(var_5_2, var_5_3, arg_5_2)

def var_0_0.PlayChapter(arg_7_0, arg_7_1, arg_7_2):
	if arg_7_1.id == 1160002:
		arg_7_0.PlayByGuideId("NG0011", None, arg_7_2)
	elif arg_7_1.isTypeDefence():
		arg_7_0.PlayByGuideId("NG0016", None, arg_7_2)
	else
		existCall(arg_7_2)

def var_0_0.PlayByGuideId(arg_8_0, arg_8_1, arg_8_2, arg_8_3):
	var_0_4(arg_8_1, arg_8_2, arg_8_3)

def var_0_0.FixGuide(arg_9_0, arg_9_1):
	if not var_0_2("FixGuide"):
		var_0_4("FixGuide")
		arg_9_1()

def var_0_0.PlayDailyLevel(arg_10_0, arg_10_1):
	if not var_0_2("NG0015"):
		pg.m02.sendNotification(GAME.STORY_UPDATE, {
			storyId = "NG0015"
		})
		arg_10_1()

def var_0_0.PlayCommander(arg_11_0):
	local var_11_0 = {
		"ZHIHUIMIAO2",
		"NG006",
		"NG007",
		"ZHIHUIMIAO3",
		"NG008",
		"ZHIHUIMIAO4",
		"NG009"
	}

	if not LOCK_CATTERY:
		table.insert(var_11_0, "NG0029")

	local var_11_1 = _.select(var_11_0, function(arg_12_0)
		return not var_0_2(arg_12_0))
	local var_11_2 = {}
	local var_11_3

	for iter_11_0, iter_11_1 in ipairs(var_11_1):
		table.insert(var_11_2, function(arg_13_0)
			if iter_11_1 == "NG006" and table.getCount(getProxy(CommanderProxy).getData()) >= 1 or iter_11_1 == "NG007" and getProxy(BagProxy).getItemCountById(20012) < 1 or iter_11_1 == "NG008" and getProxy(CommanderProxy).getBoxes()[1].getState() != CommanderBox.STATE_FINISHED or iter_11_1 == "NG009" and table.getCount(getProxy(CommanderProxy).getData()) != 1:
				pg.m02.sendNotification(GAME.STORY_UPDATE, {
					storyId = iter_11_1
				})
				arg_13_0()
			elif iter_11_1 == "ZHIHUIMIAO2" or iter_11_1 == "ZHIHUIMIAO3" or iter_11_1 == "ZHIHUIMIAO4":
				pg.NewStoryMgr.GetInstance().Play(iter_11_1, arg_13_0, True)
			elif iter_11_1 == "NG0029":
				if var_11_3 == "NG009":
					var_0_4(iter_11_1, {
						1
					}, arg_13_0)
				else
					var_0_4(iter_11_1, {
						2
					}, arg_13_0)
			else
				var_11_3 = iter_11_1

				var_0_4(iter_11_1, {}, arg_13_0))

	seriesAsync(var_11_2)

def var_0_0.PlayGuildAssaultFleet(arg_14_0, arg_14_1):
	arg_14_0.PlayByGuideId("GNG001", {}, arg_14_1)
