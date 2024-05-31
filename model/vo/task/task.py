local var_0_0 = class("Task", import("..BaseVO"))

var_0_0.TYPE_SCENARIO = 1
var_0_0.TYPE_BRANCH = 2
var_0_0.TYPE_ROUTINE = 3
var_0_0.TYPE_WEEKLY = 4
var_0_0.TYPE_HIDDEN = 5
var_0_0.TYPE_ACTIVITY = 6
var_0_0.TYPE_ACTIVITY_ROUTINE = 36
var_0_0.TYPE_ACTIVITY_BRANCH = 26
var_0_0.TYPE_GUILD_WEEKLY = 12
var_0_0.TYPE_NEW_WEEKLY = 13
var_0_0.TYPE_REFLUX = 15
var_0_0.TYPE_ACTIVITY_WEEKLY = 46

local var_0_1 = {
	"scenario",
	"branch",
	"routine",
	"weekly"
}

var_0_0.TASK_PROGRESS_UPDATE = 0
var_0_0.TASK_PROGRESS_APPEND = 1

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1.id
	arg_1_0.configId = arg_1_1.id
	arg_1_0.progress = arg_1_1.progress or 0
	arg_1_0.acceptTime = arg_1_1.accept_time
	arg_1_0.submitTime = arg_1_1.submit_time or 0

def var_0_0.isClientTrigger(arg_2_0):
	return arg_2_0.getConfig("sub_type") > 2000 and arg_2_0.getConfig("sub_type") < 3000

def var_0_0.bindConfigTable(arg_3_0):
	return pg.task_data_template

def var_0_0.isGuildTask(arg_4_0):
	return arg_4_0.getConfig("type") == var_0_0.TYPE_GUILD_WEEKLY

def var_0_0.IsRoutineType(arg_5_0):
	return arg_5_0.getConfig("type") == var_0_0.TYPE_ROUTINE

def var_0_0.IsActRoutineType(arg_6_0):
	return arg_6_0.getConfig("type") == var_0_0.TYPE_ACTIVITY_ROUTINE

def var_0_0.IsActType(arg_7_0):
	return arg_7_0.getConfig("type") == var_0_0.TYPE_ACTIVITY

def var_0_0.IsWeeklyType(arg_8_0):
	return arg_8_0.getConfig("type") == var_0_0.TYPE_WEEKLY or arg_8_0.getConfig("type") == var_0_0.TYPE_NEW_WEEKLY

def var_0_0.IsBackYardInterActionType(arg_9_0):
	return arg_9_0.getConfig("sub_type") == 2010

def var_0_0.IsFlagShipInterActionType(arg_10_0):
	return arg_10_0.getConfig("sub_type") == 2011

def var_0_0.IsGuildAddLivnessType(arg_11_0):
	local var_11_0 = arg_11_0.getConfig("type")

	return var_11_0 == var_0_0.TYPE_ROUTINE or var_11_0 == var_0_0.TYPE_WEEKLY or var_11_0 == var_0_0.TYPE_GUILD_WEEKLY or var_11_0 == var_0_0.TYPE_NEW_WEEKLY

def var_0_0.isLock(arg_12_0):
	return getProxy(PlayerProxy).getRawData().level < arg_12_0.getConfig("level")

def var_0_0.isFinish(arg_13_0):
	return arg_13_0.getProgress() >= arg_13_0.getConfig("target_num")

def var_0_0.getProgress(arg_14_0):
	local var_14_0 = arg_14_0.progress

	if arg_14_0.getConfig("sub_type") == TASK_SUB_TYPE_GIVE_ITEM:
		local var_14_1 = tonumber(arg_14_0.getConfig("target_id"))

		var_14_0 = getProxy(BagProxy).getItemCountById(tonumber(var_14_1))
	elif arg_14_0.getConfig("sub_type") == TASK_SUB_TYPE_PT:
		local var_14_2 = getProxy(ActivityProxy).getActivityById(tonumber(arg_14_0.getConfig("target_id_2")))

		var_14_0 = var_14_2 and var_14_2.data1 or 0
	elif arg_14_0.getConfig("sub_type") == TASK_SUB_TYPE_PLAYER_RES:
		local var_14_3 = tonumber(arg_14_0.getConfig("target_id"))

		var_14_0 = getProxy(PlayerProxy).getData().getResById(var_14_3)
	elif arg_14_0.getConfig("sub_type") == TASK_SUB_TYPE_GIVE_VIRTUAL_ITEM:
		local var_14_4 = tonumber(arg_14_0.getConfig("target_id"))

		var_14_0 = getProxy(ActivityProxy).getVirtualItemNumber(var_14_4)
	elif arg_14_0.getConfig("sub_type") == TASK_SUB_TYPE_BOSS_PT:
		local var_14_5 = tonumber(arg_14_0.getConfig("target_id"))

		var_14_0 = getProxy(PlayerProxy).getData().getResById(var_14_5)
	elif arg_14_0.getConfig("sub_type") == TASK_SUB_STROY:
		local var_14_6 = arg_14_0.getConfig("target_id")
		local var_14_7 = 0

		_.each(var_14_6, function(arg_15_0)
			if pg.NewStoryMgr.GetInstance().GetPlayedFlag(arg_15_0):
				var_14_7 = var_14_7 + 1)

		var_14_0 = var_14_7
	elif arg_14_0.getConfig("sub_type") == TASK_SUB_TYPE_TECHNOLOGY_POINT:
		var_14_0 = getProxy(TechnologyNationProxy).getNationPoint(tonumber(arg_14_0.getConfig("target_id")))
		var_14_0 = math.min(var_14_0, arg_14_0.getConfig("target_num"))

	return var_14_0 or 0

def var_0_0.getTargetNumber(arg_16_0):
	return arg_16_0.getConfig("target_num")

def var_0_0.isReceive(arg_17_0):
	return arg_17_0.submitTime > 0

def var_0_0.getTaskStatus(arg_18_0):
	if arg_18_0.isLock():
		return -1

	if arg_18_0.isReceive():
		return 2

	if arg_18_0.isFinish():
		return 1

	return 0

def var_0_0.onAdded(arg_19_0):
	local function var_19_0()
		if arg_19_0.getConfig("sub_type") == 29:
			local var_20_0 = getProxy(SkirmishProxy).getRawData()

			if _.any(var_20_0, function(arg_21_0)
				return arg_21_0.getConfig("task_id") == arg_19_0.id):
				return

			pg.m02.sendNotification(GAME.TASK_GO, {
				taskVO = arg_19_0
			})
		elif arg_19_0.getConfig("added_tip") > 0:
			local var_20_1

			if getProxy(ContextProxy).getCurrentContext().mediator.__cname != TaskMediator.__cname:
				function var_20_1()
					pg.m02.sendNotification(GAME.GO_SCENE, SCENE.TASK, {
						page = var_0_1[arg_19_0.GetRealType()]
					})

			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				noText = "text_iknow",
				yesText = "text_forward",
				content = i18n("tip_add_task", arg_19_0.getConfig("name")),
				onYes = var_20_1,
				weight = LayerWeightConst.TOP_LAYER
			})

	local function var_19_1()
		local var_23_0 = getProxy(ContextProxy).getCurrentContext()

		if not table.contains({
			"LevelScene",
			"BattleScene",
			"EventListScene",
			"MilitaryExerciseScene",
			"DailyLevelScene"
		}, var_23_0.viewComponent.__cname):
			return True

		return False

	local var_19_2 = arg_19_0.getConfig("story_id")

	if var_19_2 and var_19_2 != "" and var_19_1():
		pg.NewStoryMgr.GetInstance().Play(var_19_2, var_19_0, True, True)
	else
		var_19_0()

def var_0_0.updateProgress(arg_24_0, arg_24_1):
	arg_24_0.progress = arg_24_1

def var_0_0.isSelectable(arg_25_0):
	local var_25_0 = arg_25_0.getConfig("award_choice")

	return var_25_0 != None and type(var_25_0) == "table" and #var_25_0 > 0

def var_0_0.judgeOverflow(arg_26_0, arg_26_1, arg_26_2, arg_26_3):
	local var_26_0 = arg_26_0.getTaskStatus() == 1
	local var_26_1 = arg_26_0.ShowOnTaskScene()

	return var_0_0.StaticJudgeOverflow(arg_26_1, arg_26_2, arg_26_3, var_26_0, var_26_1, arg_26_0.getConfig("award_display"))

def var_0_0.StaticJudgeOverflow(arg_27_0, arg_27_1, arg_27_2, arg_27_3, arg_27_4, arg_27_5):
	if arg_27_3 and arg_27_4:
		local var_27_0 = getProxy(PlayerProxy).getData()
		local var_27_1 = pg.gameset.urpt_chapter_max.description[1]
		local var_27_2 = arg_27_0 or var_27_0.gold
		local var_27_3 = arg_27_1 or var_27_0.oil
		local var_27_4 = arg_27_2 or not LOCK_UR_SHIP and getProxy(BagProxy).GetLimitCntById(var_27_1) or 0
		local var_27_5 = pg.gameset.max_gold.key_value
		local var_27_6 = pg.gameset.max_oil.key_value
		local var_27_7 = not LOCK_UR_SHIP and pg.gameset.urpt_chapter_max.description[2] or 0
		local var_27_8 = False
		local var_27_9 = False
		local var_27_10 = False
		local var_27_11 = False
		local var_27_12 = False
		local var_27_13 = {}
		local var_27_14 = arg_27_5

		for iter_27_0, iter_27_1 in ipairs(var_27_14):
			local var_27_15, var_27_16, var_27_17 = unpack(iter_27_1)

			if var_27_15 == DROP_TYPE_RESOURCE:
				if var_27_16 == PlayerConst.ResGold:
					local var_27_18 = var_27_2 + var_27_17 - var_27_5

					if var_27_18 > 0:
						var_27_8 = True

						local var_27_19 = {
							type = DROP_TYPE_RESOURCE,
							id = PlayerConst.ResGold,
							count = setColorStr(var_27_18, COLOR_RED)
						}

						table.insert(var_27_13, var_27_19)
				elif var_27_16 == PlayerConst.ResOil:
					local var_27_20 = var_27_3 + var_27_17 - var_27_6

					if var_27_20 > 0:
						var_27_9 = True

						local var_27_21 = {
							type = DROP_TYPE_RESOURCE,
							id = PlayerConst.ResOil,
							count = setColorStr(var_27_20, COLOR_RED)
						}

						table.insert(var_27_13, var_27_21)
			elif not LOCK_UR_SHIP and var_27_15 == DROP_TYPE_VITEM:
				if Item.getConfigData(var_27_16).virtual_type == 20:
					local var_27_22 = var_27_4 + var_27_17 - var_27_7

					if var_27_22 > 0:
						var_27_10 = True

						local var_27_23 = {
							type = DROP_TYPE_VITEM,
							id = var_27_1,
							count = setColorStr(var_27_22, COLOR_RED)
						}

						table.insert(var_27_13, var_27_23)
			elif var_27_15 == DROP_TYPE_ITEM and Item.getConfigData(var_27_16).type == Item.EXP_BOOK_TYPE:
				local var_27_24 = getProxy(BagProxy).getItemCountById(var_27_16) + var_27_17
				local var_27_25 = Item.getConfigData(var_27_16).max_num

				if var_27_25 < var_27_24:
					var_27_11 = True

					local var_27_26 = {
						type = DROP_TYPE_ITEM,
						id = var_27_16,
						count = setColorStr(math.min(var_27_17, var_27_24 - var_27_25), COLOR_RED)
					}

					table.insert(var_27_13, var_27_26)

		return var_27_8 or var_27_9 or var_27_10 or var_27_11, var_27_13

def var_0_0.IsUrTask(arg_28_0):
	if not LOCK_UR_SHIP:
		local var_28_0 = pg.gameset.urpt_chapter_max.description[1]

		do return _.any(arg_28_0.getConfig("award_display"), function(arg_29_0)
			return arg_29_0[1] == DROP_TYPE_ITEM and arg_29_0[2] == var_28_0) end
		return

	return False

def var_0_0.GetRealType(arg_30_0):
	local var_30_0 = arg_30_0.getConfig("priority_type")

	if var_30_0 == 0:
		var_30_0 = arg_30_0.getConfig("type")

	return var_30_0

def var_0_0.IsOverflowShipExpItem(arg_31_0):
	local function var_31_0(arg_32_0, arg_32_1)
		return getProxy(BagProxy).getItemCountById(arg_32_0) + arg_32_1 > Item.getConfigData(arg_32_0).max_num

	local var_31_1 = arg_31_0.getConfig("award_display")

	for iter_31_0, iter_31_1 in ipairs(var_31_1):
		local var_31_2 = iter_31_1[1]
		local var_31_3 = iter_31_1[2]
		local var_31_4 = iter_31_1[3]

		if var_31_2 == DROP_TYPE_ITEM and Item.getConfigData(var_31_3).type == Item.EXP_BOOK_TYPE and var_31_0(var_31_3, var_31_4):
			return True

	return False

def var_0_0.ShowOnTaskScene(arg_33_0):
	local var_33_0 = arg_33_0.getConfig("visibility") == 1

	if arg_33_0.id == 17268:
		var_33_0 = False

		local var_33_1 = getProxy(ActivityProxy).getActivityById(ActivityConst.BUILDING_NEWYEAR_2022)

		if var_33_1 and not var_33_1.isEnd():
			local var_33_2 = var_33_1.data1KeyValueList[2][17] or 1
			local var_33_3 = var_33_1.data1KeyValueList[2][18] or 1

			var_33_0 = var_33_2 >= 4 and var_33_3 >= 4

	return var_33_0

def var_0_0.isAvatarTask(arg_34_0):
	return False

return var_0_0
