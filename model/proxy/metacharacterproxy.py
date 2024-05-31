local var_0_0 = class("MetaCharacterProxy", import(".NetProxy"))

var_0_0.METAPROGRESS_UPDATED = "MetaCharacterProxy.METAPROGRESS_UPDATED"

local var_0_1 = pg.ship_strengthen_meta

def var_0_0.register(arg_1_0):
	arg_1_0.data = {}
	arg_1_0.metaProgressVOList = {}
	arg_1_0.metaTacticsInfoTable = None
	arg_1_0.metaTacticsInfoTableOnStart = None
	arg_1_0.metaSkillLevelMaxInfoList = None
	arg_1_0.lastMetaSkillExpInfoList = None
	arg_1_0.startRecordTag = False

	for iter_1_0, iter_1_1 in pairs(var_0_1.all):
		local var_1_0 = MetaProgress.New({
			id = iter_1_1
		})

		arg_1_0.data[iter_1_1] = var_1_0

		table.insert(arg_1_0.metaProgressVOList, var_1_0)

	arg_1_0.redTagTable = {}

	for iter_1_2, iter_1_3 in pairs(var_0_1.all):
		arg_1_0.redTagTable[iter_1_3] = {
			False,
			False
		}

	arg_1_0.on(63315, function(arg_2_0)
		print("63315 get red tag info")

		local var_2_0 = {}

		for iter_2_0, iter_2_1 in ipairs(arg_2_0.arg1):
			local var_2_1 = MetaCharacterConst.GetMetaShipGroupIDByConfigID(iter_2_1)

			table.insert(var_2_0, var_2_1)

		if arg_2_0.type == 1:
			for iter_2_2, iter_2_3 in pairs(arg_1_0.redTagTable):
				if table.contains(var_2_0, iter_2_2):
					iter_2_3[1] = True
					iter_2_3[2] = False
				else
					iter_2_3[1] = False
					iter_2_3[2] = False)
	arg_1_0.on(63316, function(arg_3_0)
		print("63316 get meta skill exp info")

		local var_3_0 = {}
		local var_3_1 = {}
		local var_3_2 = arg_1_0.metaSkillLevelMaxInfoList or {}

		for iter_3_0, iter_3_1 in ipairs(arg_3_0.skill_info_list):
			print("shipID", iter_3_1.ship_id)

			local var_3_3 = iter_3_1.ship_id
			local var_3_4 = iter_3_1.skill_id
			local var_3_5 = iter_3_1.skill_level
			local var_3_6 = iter_3_1.skill_exp
			local var_3_7 = iter_3_1.day_exp
			local var_3_8 = iter_3_1.add_exp

			arg_1_0.addExpToMetaTacticsInfo(iter_3_1)
			arg_1_0.setLastMetaSkillExpInfo(var_3_1, iter_3_1)
			arg_1_0.setMetaSkillLevelMaxInfo(var_3_2, iter_3_1)

			local var_3_9 = getProxy(BayProxy).getShipById(var_3_3)
			local var_3_10 = pg.gameset.meta_skill_exp_max.key_value
			local var_3_11 = var_3_9.getMetaSkillLevelBySkillID(var_3_4)
			local var_3_12 = var_3_10 <= var_3_7
			local var_3_13 = var_3_11 < var_3_5

			if var_3_12 or var_3_13:
				pg.ToastMgr.GetInstance().ShowToast(pg.ToastMgr.TYPE_META, {
					metaShipVO = var_3_9,
					newDayExp = var_3_7,
					addDayExp = var_3_8,
					curSkillID = var_3_4,
					newSkillLevel = var_3_5,
					oldSkillLevel = var_3_11
				})

			var_3_9.updateSkill({
				skill_id = var_3_4,
				skill_lv = var_3_5,
				skill_exp = var_3_6
			})
			getProxy(BayProxy).updateShip(var_3_9)

		if #var_3_2 > 0:
			arg_1_0.metaSkillLevelMaxInfoList = var_3_2

		if #var_3_1 > 0:
			arg_1_0.lastMetaSkillExpInfoList = var_3_1)

def var_0_0.getMetaProgressVOList(arg_4_0):
	for iter_4_0, iter_4_1 in ipairs(arg_4_0.metaProgressVOList):
		iter_4_1.setDataBeforeGet()

	return arg_4_0.metaProgressVOList

def var_0_0.getMetaProgressVOByID(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_0.data[arg_5_1]

	assert(var_5_0, "progressVO is null." .. arg_5_1)

	if var_5_0:
		var_5_0.setDataBeforeGet()

	return var_5_0

def var_0_0.setAllProgressPTData(arg_6_0, arg_6_1):
	for iter_6_0, iter_6_1 in ipairs(arg_6_1):
		local var_6_0 = iter_6_1.group_id
		local var_6_1 = arg_6_0.data[var_6_0]

		assert(var_6_1, "Null ProgressVO, ID.", var_6_0)
		var_6_1.metaPtData.initFromServerData(iter_6_1)

def var_0_0.updateRedTag(arg_7_0, arg_7_1):
	if arg_7_0.redTagTable[arg_7_1][1] == True:
		arg_7_0.redTagTable[arg_7_1][2] = True

def var_0_0.getRedTag(arg_8_0, arg_8_1):
	local var_8_0 = arg_8_0.redTagTable[arg_8_1]

	return var_8_0[2] == False and var_8_0[1] == True

def var_0_0.isHaveVaildMetaProgressVO(arg_9_0):
	local var_9_0 = arg_9_0.getMetaProgressVOList()

	for iter_9_0, iter_9_1 in ipairs(var_9_0):
		if iter_9_1.isShow():
			return True

	return False

def var_0_0.setMetaTacticsInfo(arg_10_0, arg_10_1):
	arg_10_0.metaTacticsInfoTable = arg_10_0.metaTacticsInfoTable or {}

	local var_10_0 = arg_10_1.ship_id
	local var_10_1 = MetaTacticsInfo.New(arg_10_1)

	if var_10_1:
		arg_10_0.metaTacticsInfoTable[var_10_0] = var_10_1

		var_10_1.printInfo()
	else
		errorMessage("Creat MetaTacticsInfo Fail!")

def var_0_0.addExpToMetaTacticsInfo(arg_11_0, arg_11_1):
	local var_11_0 = arg_11_1.ship_id
	local var_11_1 = arg_11_0.metaTacticsInfoTable[var_11_0]

	if var_11_1:
		var_11_1.updateExp(arg_11_1)
		var_11_1.printInfo()
	else
		errorMsg("MetaTacticsInfo is Null", var_11_0)

def var_0_0.switchMetaTacticsSkill(arg_12_0, arg_12_1, arg_12_2):
	local var_12_0 = arg_12_0.metaTacticsInfoTable[arg_12_1]

	if var_12_0:
		var_12_0.switchSkill(arg_12_2)
		var_12_0.printInfo()
	else
		errorMsg("MetaTacticsInfo is Null", arg_12_1)

def var_0_0.unlockMetaTacticsSkill(arg_13_0, arg_13_1, arg_13_2, arg_13_3):
	arg_13_0.metaTacticsInfoTable = arg_13_0.metaTacticsInfoTable or {}

	local var_13_0 = arg_13_0.metaTacticsInfoTable[arg_13_1]

	if var_13_0:
		var_13_0.unlockSkill(arg_13_2, arg_13_3)
	else
		local var_13_1 = {
			ship_id = arg_13_1,
			exp = arg_13_3 and 0,
			skill_id = arg_13_3 and arg_13_2,
			skill_exp = {
				{
					exp = 0,
					skill_id = arg_13_2
				}
			}
		}

		arg_13_0.metaTacticsInfoTable[arg_13_1] = MetaTacticsInfo.New(var_13_1)

	var_13_0.printInfo()

def var_0_0.requestMetaTacticsInfo(arg_14_0, arg_14_1, arg_14_2):
	local var_14_0 = arg_14_1 or getProxy(BayProxy).getMetaShipIDList()

	if #var_14_0 == 0:
		return

	if arg_14_2:
		arg_14_0.sendNotification(GAME.TACTICS_EXP_META_INFO_REQUEST, {
			idList = var_14_0
		})
	elif not arg_14_0.metaTacticsInfoTable:
		arg_14_0.sendNotification(GAME.TACTICS_EXP_META_INFO_REQUEST, {
			idList = var_14_0
		})

def var_0_0.getMetaTacticsInfoByShipID(arg_15_0, arg_15_1):
	if not arg_15_0.metaTacticsInfoTable:
		return MetaTacticsInfo.New()

	return arg_15_0.metaTacticsInfoTable[arg_15_1] or MetaTacticsInfo.New()

def var_0_0.printAllMetaTacticsInfo(arg_16_0):
	for iter_16_0, iter_16_1 in pairs(arg_16_0.metaTacticsInfoTable):
		iter_16_1.printInfo()

def var_0_0.setMetaTacticsInfoOnStart(arg_17_0):
	if arg_17_0.startRecordTag:
		return

	local var_17_0 = True

	if arg_17_0.metaTacticsInfoTable:
		for iter_17_0, iter_17_1 in pairs(arg_17_0.metaTacticsInfoTable):
			if iter_17_1:
				var_17_0 = False

				break

	if arg_17_0.metaTacticsInfoTable and not var_17_0:
		arg_17_0.metaTacticsInfoTableOnStart = Clone(arg_17_0.metaTacticsInfoTable)
		arg_17_0.startRecordTag = True

def var_0_0.getMetaTacticsInfoOnEnd(arg_18_0):
	if not arg_18_0.metaTacticsInfoTableOnStart:
		return False

	local var_18_0 = {}
	local var_18_1 = arg_18_0.metaTacticsInfoTable
	local var_18_2 = arg_18_0.metaTacticsInfoTableOnStart

	for iter_18_0, iter_18_1 in pairs(var_18_1):
		local var_18_3 = iter_18_1.shipID
		local var_18_4 = var_18_1[var_18_3]
		local var_18_5 = var_18_2[var_18_3] or MetaTacticsInfo.New()
		local var_18_6 = var_18_4.isAnyLearning() and var_18_5.isAnyLearning()
		local var_18_7 = getProxy(BayProxy).getShipById(var_18_3).isAllMetaSkillLevelMax()
		local var_18_8 = var_18_5 and var_18_5.isExpMaxPerDay() or False

		if var_18_6 and not var_18_7 and not var_18_8:
			local var_18_9 = var_18_4.curSkillID
			local var_18_10 = var_18_4.curDayExp - var_18_5.curDayExp
			local var_18_11 = getProxy(BayProxy).getShipById(var_18_3).isSkillLevelMax(var_18_9)
			local var_18_12 = var_18_10 > 0 and var_18_11
			local var_18_13 = var_18_4.isExpMaxPerDay()
			local var_18_14 = var_18_5.curDayExp / pg.gameset.meta_skill_exp_max.key_value
			local var_18_15 = var_18_4.curDayExp / pg.gameset.meta_skill_exp_max.key_value

			if var_18_10 > 0:
				table.insert(var_18_0, {
					shipID = var_18_3,
					addDayExp = var_18_10,
					isUpLevel = var_18_12,
					isMaxLevel = var_18_11,
					isExpMax = var_18_13,
					progressOld = var_18_14,
					progressNew = var_18_15
				})

	arg_18_0.clearMetaTacticsInfoRecord()

	return var_18_0

def var_0_0.clearMetaTacticsInfoRecord(arg_19_0):
	arg_19_0.metaTacticsInfoTableOnStart = None
	arg_19_0.startRecordTag = False

def var_0_0.setMetaSkillLevelMaxInfo(arg_20_0, arg_20_1, arg_20_2):
	local var_20_0 = arg_20_2.ship_id
	local var_20_1 = arg_20_2.skill_id
	local var_20_2 = arg_20_2.skill_level
	local var_20_3 = arg_20_2.skill_exp
	local var_20_4 = arg_20_2.day_exp
	local var_20_5 = arg_20_2.add_exp
	local var_20_6 = getProxy(BayProxy).getShipById(var_20_0)
	local var_20_7 = var_20_6.getMetaSkillLevelBySkillID(var_20_1)
	local var_20_8 = pg.skill_data_template[var_20_1].max_level
	local var_20_9 = var_20_7 < var_20_2
	local var_20_10 = var_20_8 <= var_20_2

	if var_20_9 and var_20_10:
		local var_20_11 = {
			metaShipVO = var_20_6,
			metaSkillID = var_20_1
		}
		local var_20_12 = False

		for iter_20_0, iter_20_1 in pairs(arg_20_1):
			if iter_20_1.metaShipVO.configId == var_20_11.metaShipVO.configId:
				var_20_12 = True

				break

		if not var_20_12:
			table.insert(arg_20_1, var_20_11)

def var_0_0.getMetaSkillLevelMaxInfoList(arg_21_0):
	return arg_21_0.metaSkillLevelMaxInfoList or {}

def var_0_0.clearMetaSkillLevelMaxInfoList(arg_22_0):
	arg_22_0.metaSkillLevelMaxInfoList = None

def var_0_0.tryRemoveMetaSkillLevelMaxInfo(arg_23_0, arg_23_1, arg_23_2):
	if arg_23_0.metaSkillLevelMaxInfoList and #arg_23_0.metaSkillLevelMaxInfoList > 0:
		local var_23_0

		for iter_23_0, iter_23_1 in ipairs(arg_23_0.metaSkillLevelMaxInfoList):
			local var_23_1 = iter_23_1.metaShipVO
			local var_23_2 = var_23_1.id
			local var_23_3 = var_23_1.metaSkillID

			if arg_23_1 == var_23_2 and arg_23_2 != var_23_3:
				var_23_0 = iter_23_0

				break

		if var_23_0:
			table.remove(arg_23_0.metaSkillLevelMaxInfoList, var_23_0)

def var_0_0.setLastMetaSkillExpInfo(arg_24_0, arg_24_1, arg_24_2):
	local var_24_0 = arg_24_2.ship_id
	local var_24_1 = arg_24_2.skill_id
	local var_24_2 = arg_24_2.skill_level
	local var_24_3 = arg_24_2.skill_exp
	local var_24_4 = arg_24_2.day_exp
	local var_24_5 = arg_24_2.add_exp
	local var_24_6 = getProxy(BayProxy).getShipById(var_24_0).getMetaSkillLevelBySkillID(var_24_1)
	local var_24_7 = pg.skill_data_template[var_24_1].max_level
	local var_24_8 = var_24_6 < var_24_2
	local var_24_9 = var_24_7 <= var_24_2
	local var_24_10 = var_24_4 >= pg.gameset.meta_skill_exp_max.key_value

	table.insert(arg_24_1, {
		shipID = var_24_0,
		addDayExp = var_24_5,
		isUpLevel = var_24_8,
		isMaxLevel = var_24_9,
		isExpMax = var_24_10,
		progress = var_24_4 / pg.gameset.meta_skill_exp_max.key_value
	})

def var_0_0.getLastMetaSkillExpInfoList(arg_25_0):
	return arg_25_0.lastMetaSkillExpInfoList or {}

def var_0_0.clearLastMetaSkillExpInfoList(arg_26_0):
	arg_26_0.lastMetaSkillExpInfoList = None

return var_0_0
