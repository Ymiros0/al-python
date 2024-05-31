local var_0_0 = class("MetaProgress", import("..BaseVO"))

var_0_0.STATE_LESS_PT = 1
var_0_0.STATE_LESS_STORY = 2
var_0_0.STATE_CAN_AWARD = 3
var_0_0.STATE_CAN_FINISH = 4
var_0_0.STATE_GOT_SHIP = 5

def var_0_0.bindConfigTable(arg_1_0):
	return pg.ship_strengthen_meta

def var_0_0.Ctor(arg_2_0, arg_2_1):
	arg_2_0.id = arg_2_1.id
	arg_2_0.configId = arg_2_0.id
	arg_2_0.metaType = arg_2_0.getConfig("type")
	arg_2_0.actID = arg_2_0.getConfig("activity_id")
	arg_2_0.metaShipVO = None

	if arg_2_0.isPtType():
		arg_2_0.unlockPTNum = arg_2_0.getConfig("synchronize")
		arg_2_0.unlockPTLevel = None
		arg_2_0.metaPtData = MetaPTData.New({
			group_id = arg_2_0.id
		})

		local var_2_0

		for iter_2_0, iter_2_1 in ipairs(pg.world_joint_boss_template.all):
			local var_2_1 = pg.world_joint_boss_template[iter_2_1]

			if var_2_1.meta_id == arg_2_0.id:
				var_2_0 = var_2_1

				break

		if var_2_0:
			arg_2_0.timeConfig = var_2_0.state

def var_0_0.updateMetaPtData(arg_3_0, arg_3_1):
	if arg_3_0.metaPtData:
		arg_3_0.metaPtData.Update(arg_3_1)

def var_0_0.getSynRate(arg_4_0):
	local var_4_0, var_4_1, var_4_2 = arg_4_0.metaPtData.GetResProgress()

	return var_4_0 / arg_4_0.unlockPTNum

def var_0_0.getStoryIndexList(arg_5_0):
	return arg_5_0.getConfig("unlock_story") or {
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0
	}

def var_0_0.getCurLevelStoryIndex(arg_6_0):
	local var_6_0, var_6_1, var_6_2 = arg_6_0.metaPtData.GetLevelProgress()

	return arg_6_0.getStoryIndexList()[var_6_0]

def var_0_0.isFinishCurLevelStory(arg_7_0):
	local var_7_0 = arg_7_0.getCurLevelStoryIndex()
	local var_7_1 = False

	if var_7_0 == 0:
		var_7_1 = True
	else
		local var_7_2 = pg.NewStoryMgr.GetInstance()
		local var_7_3 = var_7_2.StoryName2StoryId(var_7_0)

		if var_7_2.IsPlayed(var_7_3):
			var_7_1 = True

	return var_7_1

def var_0_0.getCurLevelStoryName(arg_8_0):
	local var_8_0 = arg_8_0.getCurLevelStoryIndex()

	return pg.memory_template[var_8_0].title

def var_0_0.isCanGetAward(arg_9_0):
	local var_9_0 = arg_9_0.metaPtData.CanGetAward()
	local var_9_1 = arg_9_0.getCurLevelStoryIndex()
	local var_9_2 = False

	if var_9_1 == 0:
		var_9_2 = True
	else
		local var_9_3 = pg.NewStoryMgr.GetInstance()
		local var_9_4 = var_9_3.GetStoryByName("index")[var_9_1]

		if var_9_3.IsPlayed(var_9_1):
			var_9_2 = True

	return var_9_0 and var_9_2

def var_0_0.getMetaProgressPTState(arg_10_0):
	local var_10_0 = arg_10_0.metaPtData.CanGetAward()
	local var_10_1 = arg_10_0.isFinishCurLevelStory()
	local var_10_2 = arg_10_0.isUnlocked()
	local var_10_3 = arg_10_0.metaPtData.level + 1

	if var_10_3 < arg_10_0.unlockPTLevel:
		if not var_10_0:
			return var_0_0.STATE_LESS_PT
		elif var_10_1 == False:
			return var_0_0.STATE_LESS_STORY
		elif var_10_1 == True:
			return var_0_0.STATE_CAN_AWARD
	elif var_10_3 == arg_10_0.unlockPTLevel:
		if not var_10_0:
			return var_0_0.STATE_LESS_PT
		elif var_10_1 == False:
			return var_0_0.STATE_LESS_STORY
		elif var_10_1 == True:
			return var_0_0.STATE_CAN_FINISH
	elif var_10_3 > arg_10_0.unlockPTLevel:
		return var_0_0.STATE_GOT_SHIP

def var_0_0.IsGotAllAwards(arg_11_0):
	return arg_11_0.isInAct() and arg_11_0.isInArchive() and not arg_11_0.metaPtData.CanGetNextAward()

def var_0_0.getRepairRateFromMetaCharacter(arg_12_0):
	assert(arg_12_0.metaShipVO, "metaShipVO is null")

	local var_12_0 = arg_12_0.metaShipVO.metaCharacter

	assert(var_12_0, "metaCharacterVO is null")

	return (var_12_0.getRepairRate())

def var_0_0.isPtType(arg_13_0):
	return arg_13_0.metaType == MetaCharacterConst.Meta_Type_Act_PT

def var_0_0.isPassType(arg_14_0):
	return arg_14_0.metaType == MetaCharacterConst.Meta_Type_Pass

def var_0_0.isBuildType(arg_15_0):
	return arg_15_0.metaType == MetaCharacterConst.Meta_Type_Build

def var_0_0.isInAct(arg_16_0):
	if arg_16_0.isPtType():
		return WorldBossConst.IsCurrBoss(arg_16_0.id)
	elif arg_16_0.isPassType() or arg_16_0.isBuildType():
		local var_16_0 = arg_16_0.getConfig("activity_id")
		local var_16_1 = getProxy(ActivityProxy).getActivityById(var_16_0)

		return var_16_1 and not var_16_1.isEnd()

def var_0_0.isInArchive(arg_17_0):
	return WorldBossConst.IsAchieveBoss(arg_17_0.id)

def var_0_0.isUnlocked(arg_18_0):
	return arg_18_0.metaShipVO != None

def var_0_0.isShow(arg_19_0):
	local var_19_0 = arg_19_0.isInAct()
	local var_19_1 = arg_19_0.isInArchive()
	local var_19_2 = arg_19_0.isUnlocked()
	local var_19_3 = True

	if var_19_2:
		return True
	elif var_19_1:
		return True
	elif var_19_0:
		if arg_19_0.isPtType() and var_19_3:
			return True
		elif arg_19_0.isPassType() or arg_19_0.isBuildType():
			return True
		else
			return False
	else
		return False

def var_0_0.getMetaShipFromBayProxy(arg_20_0):
	local var_20_0 = getProxy(BayProxy).getMetaShipByGroupId(arg_20_0.configId)

	arg_20_0.metaShipVO = var_20_0

	return var_20_0

def var_0_0.getShip(arg_21_0):
	return arg_21_0.metaShipVO

def var_0_0.updateShip(arg_22_0, arg_22_1):
	assert(arg_22_1, "metaShipVO can not be null!")

	arg_22_0.metaShipVO = arg_22_1

def var_0_0.setDataBeforeGet(arg_23_0):
	arg_23_0.metaShipVO = arg_23_0.getMetaShipFromBayProxy()

	if arg_23_0.isPtType() and arg_23_0.metaPtData and not arg_23_0.unlockPTLevel:
		local var_23_0 = arg_23_0.metaPtData.targets

		for iter_23_0, iter_23_1 in ipairs(var_23_0):
			if iter_23_1 == arg_23_0.unlockPTNum:
				arg_23_0.unlockPTLevel = iter_23_0

				break

	if (arg_23_0.isPassType() or arg_23_0.isBuildType()) and not arg_23_0.timeConfig:
		local var_23_1 = arg_23_0.getConfig("activity_id")
		local var_23_2 = getProxy(ActivityProxy).getActivityById(var_23_1)

		if var_23_2:
			arg_23_0.timeConfig = {
				var_23_2.getConfig("time")[2],
				var_23_2.getConfig("time")[3]
			}

def var_0_0.updateDataAfterAddShip(arg_24_0):
	arg_24_0.metaShipVO = arg_24_0.getMetaShipFromBayProxy()

def var_0_0.addPT(arg_25_0, arg_25_1):
	if arg_25_0.isPtType() and arg_25_0.metaPtData:
		arg_25_0.metaPtData.addPT(arg_25_1)

def var_0_0.updatePTLevel(arg_26_0, arg_26_1):
	if arg_26_0.isPtType() and arg_26_0.metaPtData:
		arg_26_0.metaPtData.updateLevel(arg_26_1)

def var_0_0.getPaintPathAndName(arg_27_0):
	local var_27_0 = arg_27_0.isUnlocked()
	local var_27_1, var_27_2 = MetaCharacterConst.GetMetaCharacterPaintPath(arg_27_0.configId, var_27_0)

	return var_27_1, var_27_2

def var_0_0.getBannerPathAndName(arg_28_0):
	local var_28_0, var_28_1 = MetaCharacterConst.GetMetaCharacterBannerPath(arg_28_0.configId)

	return var_28_0, var_28_1

def var_0_0.getBGNamePathAndName(arg_29_0):
	local var_29_0, var_29_1 = MetaCharacterConst.GetMetaCharacterNamePath(arg_29_0.configId)

	return var_29_0, var_29_1

def var_0_0.getPtIconPath(arg_30_0):
	assert(arg_30_0.isPtType() and arg_30_0.metaPtData)

	return Item.getConfigData(arg_30_0.metaPtData.resId).icon

return var_0_0
