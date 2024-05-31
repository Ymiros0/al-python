local var_0_0 = class("NavalAcademyProxy", import(".NetProxy"))

var_0_0.COURSE_START = "NavalAcademyProxy.COURSE_START"
var_0_0.COURSE_UPDATED = "NavalAcademyProxy.COURSE_UPDATED"
var_0_0.COURSE_REWARD = "NavalAcademyProxy.COURSE_REWARD"
var_0_0.COURSE_CANCEL = "NavalAcademyProxy.COURSE_CANCEL"
var_0_0.RESOURCE_UPGRADE = "NavalAcademyProxy.RESOURCE_UPGRADE"
var_0_0.RESOURCE_UPGRADE_DONE = "NavalAcademyProxy.RESOURCE_UPGRADE_DONE"
var_0_0.BUILDING_FINISH = "NavalAcademyProxy.BUILDING_FINISH"
var_0_0.START_LEARN_TACTICS = "NavalAcademyProxy.START_LEARN_TACTICS"
var_0_0.CANCEL_LEARN_TACTICS = "NavalAcademyProxy.CANCEL_LEARN_TACTICS"
var_0_0.SKILL_CLASS_POS_UPDATED = "NavalAcademyProxy.SKILL_CLASS_POS_UPDATED"

def var_0_0.register(arg_1_0):
	arg_1_0.timers = {}
	arg_1_0.students = {}
	arg_1_0.course = AcademyCourse.New()
	arg_1_0.recentShips = {}

	arg_1_0.on(22001, function(arg_2_0)
		local var_2_0 = OilResourceField.New()

		var_2_0.SetLevel(arg_2_0.oil_well_level)
		var_2_0.SetUpgradeTimeStamp(arg_2_0.oil_well_lv_up_time)

		arg_1_0._oilVO = var_2_0

		local var_2_1 = GoldResourceField.New()

		var_2_1.SetLevel(arg_2_0.gold_well_level)
		var_2_1.SetUpgradeTimeStamp(arg_2_0.gold_well_lv_up_time)

		arg_1_0._goldVO = var_2_1

		local var_2_2 = ClassResourceField.New()

		var_2_2.SetLevel(arg_2_0.class_lv)
		var_2_2.SetUpgradeTimeStamp(arg_2_0.class_lv_up_time)

		arg_1_0._classVO = var_2_2

		arg_1_0.course.update(arg_2_0.class)

		local var_2_3 = {}

		for iter_2_0, iter_2_1 in ipairs(arg_2_0.skill_class_list):
			local var_2_4 = Student.New(iter_2_1)

			var_2_3[var_2_4.id] = var_2_4

		arg_1_0.skillClassNum = LOCK_CLASSROOM and 2 or arg_2_0.skill_class_num or 2

		arg_1_0.setStudents(var_2_3)
		pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inClass")
		arg_1_0.CheckResFields()

		arg_1_0.dailyFinsihCnt = arg_2_0.daily_finish_buff_cnt or 0)
	arg_1_0.on(22013, function(arg_3_0)
		arg_1_0.course.SetProficiency(arg_3_0.proficiency)

		local var_3_0 = getProxy(PlayerProxy).getData()

		var_3_0.expField = arg_3_0.exp_in_well

		getProxy(PlayerProxy).updatePlayer(var_3_0)
		arg_1_0.sendNotification(var_0_0.COURSE_UPDATED))

def var_0_0.GetRecentShips(arg_4_0):
	if #arg_4_0.recentShips > 0:
		for iter_4_0 = #arg_4_0.recentShips, 1, -1:
			local var_4_0 = arg_4_0.recentShips[iter_4_0]
			local var_4_1 = getProxy(BayProxy).RawGetShipById(var_4_0)

			if not var_4_1 or _.all(var_4_1.getSkillList(), function(arg_5_0)
				return ShipSkill.New(var_4_1.skills[arg_5_0]).IsMaxLevel()):
				table.remove(arg_4_0.recentShips, iter_4_0)

		return arg_4_0.recentShips

	local var_4_2 = getProxy(PlayerProxy).getRawData().id
	local var_4_3 = PlayerPrefs.GetString("NavTacticsRecentShipId" .. var_4_2)
	local var_4_4 = string.split(var_4_3, "#")

	for iter_4_1, iter_4_2 in ipairs(var_4_4):
		local var_4_5 = tonumber(iter_4_2) or 0

		if var_4_5 > 0:
			local var_4_6 = getProxy(BayProxy).RawGetShipById(var_4_5)

			if var_4_6 and not table.contains(arg_4_0.recentShips, var_4_5) and _.any(var_4_6.getSkillList(), function(arg_6_0)
				return not ShipSkill.New(var_4_6.skills[arg_6_0]).IsMaxLevel()):
				table.insert(arg_4_0.recentShips, var_4_5)

	return arg_4_0.recentShips

def var_0_0.SaveRecentShip(arg_7_0, arg_7_1):
	if not table.contains(arg_7_0.recentShips, arg_7_1):
		table.insert(arg_7_0.recentShips, arg_7_1)

		for iter_7_0 = 1, #arg_7_0.recentShips - 11:
			table.remove(arg_7_0.recentShips, iter_7_0)

		local var_7_0 = table.concat(arg_7_0.recentShips, "#")
		local var_7_1 = getProxy(PlayerProxy).getRawData().id

		PlayerPrefs.SetString("NavTacticsRecentShipId" .. var_7_1, var_7_0)
		PlayerPrefs.Save()

def var_0_0.getSkillClassNum(arg_8_0):
	return arg_8_0.skillClassNum

var_0_0.MAX_SKILL_CLASS_NUM = 4

def var_0_0.inCreaseKillClassNum(arg_9_0):
	arg_9_0.skillClassNum = math.min(arg_9_0.skillClassNum + 1, var_0_0.MAX_SKILL_CLASS_NUM)

	arg_9_0.sendNotification(var_0_0.SKILL_CLASS_POS_UPDATED, arg_9_0.skillClassNum)

def var_0_0.onRemove(arg_10_0):
	for iter_10_0, iter_10_1 in pairs(arg_10_0.timers):
		iter_10_1.Stop()

	arg_10_0.timers = None

	var_0_0.super.onRemove(arg_10_0)

def var_0_0.ExistStudent(arg_11_0, arg_11_1):
	return arg_11_0.students[arg_11_1] != None

def var_0_0.getStudentById(arg_12_0, arg_12_1):
	if arg_12_0.students[arg_12_1]:
		return arg_12_0.students[arg_12_1].clone()

def var_0_0.getStudentIdByShipId(arg_13_0, arg_13_1):
	for iter_13_0, iter_13_1 in pairs(arg_13_0.students):
		if iter_13_1.shipId == arg_13_1:
			return iter_13_1.id

def var_0_0.getStudentByShipId(arg_14_0, arg_14_1):
	for iter_14_0, iter_14_1 in pairs(arg_14_0.students):
		if iter_14_1.shipId == arg_14_1:
			return iter_14_1

def var_0_0.setStudents(arg_15_0, arg_15_1):
	arg_15_0.students = arg_15_1

	pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inTactics")

def var_0_0.getStudents(arg_16_0):
	return Clone(arg_16_0.students)

def var_0_0.RawGetStudentList(arg_17_0):
	return arg_17_0.students

def var_0_0.addStudent(arg_18_0, arg_18_1):
	arg_18_0.students[arg_18_1.id] = arg_18_1

	pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inTactics")
	arg_18_0.sendNotification(var_0_0.START_LEARN_TACTICS, Clone(arg_18_1))

def var_0_0.updateStudent(arg_19_0, arg_19_1):
	arg_19_0.students[arg_19_1.id] = arg_19_1

	pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inTactics")

def var_0_0.deleteStudent(arg_20_0, arg_20_1):
	arg_20_0.students[arg_20_1] = None

	pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inTactics")
	arg_20_0.sendNotification(var_0_0.CANCEL_LEARN_TACTICS, arg_20_1)

def var_0_0.GetOilVO(arg_21_0):
	return arg_21_0._oilVO

def var_0_0.GetGoldVO(arg_22_0):
	return arg_22_0._goldVO

def var_0_0.GetClassVO(arg_23_0):
	return arg_23_0._classVO

def var_0_0.getCourse(arg_24_0):
	return Clone(arg_24_0.course)

def var_0_0.setCourse(arg_25_0, arg_25_1):
	arg_25_0.course = arg_25_1

	pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inClass")

def var_0_0.GetShipIDs(arg_26_0):
	return {}

def var_0_0.CheckResFields(arg_27_0):
	if arg_27_0._oilVO.IsStarting():
		arg_27_0.AddResFieldListener(arg_27_0._oilVO)

	if arg_27_0._goldVO.IsStarting():
		arg_27_0.AddResFieldListener(arg_27_0._goldVO)

	if arg_27_0._classVO.IsStarting():
		arg_27_0.AddResFieldListener(arg_27_0._classVO)

def var_0_0.StartUpGradeSuccess(arg_28_0, arg_28_1):
	local var_28_0 = arg_28_1.bindConfigTable()[arg_28_1.GetLevel()].time

	arg_28_1.SetUpgradeTimeStamp(pg.TimeMgr.GetInstance().GetServerTime() + var_28_0)
	arg_28_0.AddResFieldListener(arg_28_1)
	arg_28_0.facade.sendNotification(var_0_0.RESOURCE_UPGRADE, {
		resVO = arg_28_1
	})

def var_0_0.AddResFieldListener(arg_29_0, arg_29_1):
	local var_29_0 = arg_29_1._upgradeTimeStamp - pg.TimeMgr.GetInstance().GetServerTime()

	if var_29_0 > 0:
		local var_29_1 = arg_29_1.GetUpgradeType()

		if arg_29_0.timers[var_29_1]:
			arg_29_0.timers[var_29_1].Stop()

			arg_29_0.timers[var_29_1] = None

		arg_29_0.timers[var_29_1] = Timer.New(function()
			arg_29_0.UpgradeFinish()
			arg_29_0.timers[var_29_1].Stop()

			arg_29_0.timers[var_29_1] = None, var_29_0, 1)

		arg_29_0.timers[var_29_1].Start()

def var_0_0.UpgradeFinish(arg_31_0):
	if arg_31_0._goldVO.GetDuration() and arg_31_0._goldVO.GetDuration() <= 0:
		local var_31_0 = arg_31_0._goldVO.bindConfigTable()[arg_31_0._goldVO.GetLevel()].store

		arg_31_0._goldVO.SetLevel(arg_31_0._goldVO.GetLevel() + 1)
		arg_31_0._goldVO.SetUpgradeTimeStamp(0)

		local var_31_1 = arg_31_0._goldVO.bindConfigTable()[arg_31_0._goldVO.GetLevel()].store

		arg_31_0.sendNotification(var_0_0.RESOURCE_UPGRADE_DONE, {
			field = arg_31_0._goldVO,
			value = var_31_1 - var_31_0
		})

	if arg_31_0._oilVO.GetDuration() and arg_31_0._oilVO.GetDuration() <= 0:
		local var_31_2 = arg_31_0._oilVO.bindConfigTable()[arg_31_0._oilVO.GetLevel()].store

		arg_31_0._oilVO.SetLevel(arg_31_0._oilVO.GetLevel() + 1)
		arg_31_0._oilVO.SetUpgradeTimeStamp(0)

		local var_31_3 = arg_31_0._oilVO.bindConfigTable()[arg_31_0._oilVO.GetLevel()].store

		arg_31_0.sendNotification(var_0_0.RESOURCE_UPGRADE_DONE, {
			field = arg_31_0._oilVO,
			value = var_31_3 - var_31_2
		})

	if arg_31_0._classVO.GetDuration() and arg_31_0._classVO.GetDuration() <= 0:
		local var_31_4 = arg_31_0._classVO.bindConfigTable()[arg_31_0._classVO.GetLevel()].store
		local var_31_5 = arg_31_0._classVO.bindConfigTable()[arg_31_0._classVO.GetLevel()].proficency_get_percent
		local var_31_6 = arg_31_0._classVO.bindConfigTable()[arg_31_0._classVO.GetLevel()].proficency_cost_per_min

		arg_31_0._classVO.SetLevel(arg_31_0._classVO.GetLevel() + 1)
		arg_31_0._classVO.SetUpgradeTimeStamp(0)

		local var_31_7 = arg_31_0._classVO.bindConfigTable()[arg_31_0._classVO.GetLevel()].store
		local var_31_8 = arg_31_0._classVO.bindConfigTable()[arg_31_0._classVO.GetLevel()].proficency_get_percent
		local var_31_9 = arg_31_0._classVO.bindConfigTable()[arg_31_0._classVO.GetLevel()].proficency_cost_per_min

		arg_31_0.sendNotification(var_0_0.RESOURCE_UPGRADE_DONE, {
			field = arg_31_0._classVO,
			value = var_31_7 - var_31_4,
			rate = var_31_8 - var_31_5,
			exp = (var_31_9 - var_31_6) * 60
		})

def var_0_0.isResourceFieldUpgradeConditionSatisfy(arg_32_0):
	local var_32_0 = getProxy(PlayerProxy).getData()

	if arg_32_0.GetOilVO().CanUpgrade(var_32_0.level, var_32_0.gold) or arg_32_0.GetGoldVO().CanUpgrade(var_32_0.level, var_32_0.gold) or arg_32_0.GetClassVO().CanUpgrade(var_32_0.level, var_32_0.gold):
		return True

	return False

def var_0_0.AddCourseProficiency(arg_33_0, arg_33_1):
	local var_33_0 = arg_33_0.getCourse()
	local var_33_1 = arg_33_0.GetClassVO()
	local var_33_2 = var_33_1.GetExp2ProficiencyRatio() * var_33_0.getExtraRate()
	local var_33_3 = var_33_0.GetProficiency() + math.floor(arg_33_1 * var_33_2 * 0.01)
	local var_33_4 = math.min(var_33_3, var_33_1.GetMaxProficiency())

	var_33_0.SetProficiency(var_33_4)
	arg_33_0.setCourse(var_33_0)

def var_0_0.fillStudens(arg_34_0, arg_34_1):
	local var_34_0 = pg.gameset.academy_random_ship_count.key_value
	local var_34_1 = {}

	for iter_34_0, iter_34_1 in pairs(arg_34_1):
		var_34_1[iter_34_1.groupId] = True
		var_34_0 = var_34_0 - 1

	local var_34_2 = pg.gameset.academy_random_ship_coldtime.key_value

	if not arg_34_0._timeStamp or var_34_2 < os.time() - arg_34_0._timeStamp:
		arg_34_0._studentsFiller = None

	if not arg_34_0._studentsFiller:
		local var_34_3 = math.random(1, var_34_0)

		arg_34_0._timeStamp = os.time()
		arg_34_0._studentsFiller = {}

		local var_34_4 = getProxy(CollectionProxy).getGroups()
		local var_34_5 = getProxy(BayProxy)
		local var_34_6 = getProxy(ShipSkinProxy).getSkinList()
		local var_34_7 = {}

		for iter_34_2, iter_34_3 in pairs(var_34_4):
			if not table.contains(var_34_1, iter_34_2):
				var_34_7[#var_34_7 + 1] = iter_34_2

		local var_34_8 = #var_34_7

		while var_34_3 > 0 and var_34_8 > 0:
			local var_34_9 = math.random(#var_34_7)
			local var_34_10 = var_34_7[var_34_9]
			local var_34_11 = var_34_4[var_34_10]
			local var_34_12 = var_34_10 * 10 + 1
			local var_34_13 = 10000000000 + var_34_12
			local var_34_14 = ShipGroup.getSkinList(var_34_10)
			local var_34_15 = {}
			local var_34_16
			local var_34_17 = {}

			for iter_34_4, iter_34_5 in ipairs(var_34_14):
				local var_34_18 = iter_34_5.skin_type

				if var_34_18 == ShipSkin.SKIN_TYPE_DEFAULT or table.contains(var_34_6, iter_34_5.id) or var_34_18 == ShipSkin.SKIN_TYPE_REMAKE and var_34_11.trans or var_34_18 == ShipSkin.SKIN_TYPE_PROPOSE and var_34_11.married == 1:
					var_34_17[#var_34_17 + 1] = iter_34_5.id

				var_34_16 = var_34_17[math.random(#var_34_17)]

			local var_34_19 = {
				id = var_34_13,
				groupId = var_34_10,
				configId = var_34_12,
				skin_id = var_34_16
			}

			table.remove(var_34_7, var_34_9)

			var_34_8 = var_34_8 - 1
			var_34_3 = var_34_3 - 1
			arg_34_0._studentsFiller[#arg_34_0._studentsFiller + 1] = var_34_19

	for iter_34_6, iter_34_7 in ipairs(arg_34_0._studentsFiller):
		arg_34_1[#arg_34_1 + 1] = Ship.New(iter_34_7)

	return arg_34_1

def var_0_0.IsShowTip(arg_35_0):
	local var_35_0 = getProxy(PlayerProxy)

	if var_35_0 and var_35_0.getData() and arg_35_0.isResourceFieldUpgradeConditionSatisfy():
		return True

	local var_35_1 = getProxy(ShopsProxy)

	if var_35_1:
		local var_35_2 = var_35_1.getShopStreet()

		if var_35_2 and var_35_2.isUpdateGoods():
			return True

	local var_35_3 = pg.TimeMgr.GetInstance().GetServerTime()

	for iter_35_0, iter_35_1 in pairs(arg_35_0.students):
		if var_35_3 >= iter_35_1.getFinishTime():
			return True

	if getProxy(CollectionProxy).unclaimTrophyCount() > 0:
		return True

	local var_35_4 = getProxy(TaskProxy)

	if _.any(getProxy(ActivityProxy).getActivitiesByType(ActivityConst.ACTIVITY_TYPE_TASK_LIST), function(arg_36_0)
		local var_36_0 = arg_36_0.getTaskShip()
		local var_36_1 = var_36_0 and var_35_4.getAcademyTask(var_36_0.groupId) or None
		local var_36_2 = var_35_4.getTaskById(var_36_1)
		local var_36_3 = var_35_4.getFinishTaskById(var_36_1)

		return var_36_0 and (var_36_1 and not var_36_2 and not var_36_3 or var_36_2 and var_36_2.isFinish())):
		return True

	return False

def var_0_0.getDailyFinishCnt(arg_37_0):
	local var_37_0 = _.detect(BuffHelper.GetBuffsByActivityType(ActivityConst.ACTIVITY_TYPE_BUFF), function(arg_38_0)
		return arg_38_0.getConfig("benefit_type") == "skill_learn_time")

	return (var_37_0 and tonumber(var_37_0.getConfig("benefit_effect")) or 0) - arg_37_0.dailyFinsihCnt

def var_0_0.updateUsedDailyFinishCnt(arg_39_0):
	arg_39_0.dailyFinsihCnt = arg_39_0.dailyFinsihCnt + 1

def var_0_0.resetUsedDailyFinishCnt(arg_40_0):
	arg_40_0.dailyFinsihCnt = 0

return var_0_0
