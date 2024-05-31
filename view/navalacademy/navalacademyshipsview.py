local var_0_0 = class("NavalAcademyShipsView")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.parent = arg_1_1
	arg_1_0.academyStudents = {}
	arg_1_0._map = arg_1_1.findTF("academyMap/map")
	arg_1_0._shipTpl = arg_1_0._map.Find("ship")
	arg_1_0._fountain = arg_1_0._map.Find("fountain")
	arg_1_0.academyGraphPath = GraphPath.New(AcademyGraph)

def var_0_0.BindBuildings(arg_2_0, arg_2_1):
	arg_2_0.buildings = _.map(arg_2_1, function(arg_3_0)
		return arg_3_0._tf)

def var_0_0.Refresh(arg_4_0):
	local var_4_0, var_4_1 = arg_4_0.getStudents()

	_.each(_.keys(arg_4_0.academyStudents), function(arg_5_0)
		local var_5_0 = var_4_0[arg_5_0]
		local var_5_1 = var_4_1[arg_5_0]
		local var_5_2 = arg_4_0.academyStudents[arg_5_0]

		if var_5_0:
			var_5_2.updateStudent(var_5_0, var_5_1)
		else
			var_5_2.detach())

	for iter_4_0, iter_4_1 in pairs(var_4_0):
		if not arg_4_0.academyStudents[iter_4_0]:
			local var_4_2 = var_4_1[iter_4_0]
			local var_4_3 = cloneTplTo(arg_4_0._shipTpl, arg_4_0._map)
			local var_4_4 = NavalAcademyStudent.New(var_4_3.gameObject)

			var_4_4.attach()
			var_4_4.setPathFinder(arg_4_0.academyGraphPath)
			var_4_4.setCallBack(function(arg_6_0)
				arg_4_0.onStateChange(iter_4_1, arg_6_0), function(arg_7_0, arg_7_1)
				arg_4_0.onTask(iter_4_1, var_4_2))
			var_4_4.updateStudent(iter_4_1, var_4_2)

			arg_4_0.academyStudents[iter_4_0] = var_4_4

	arg_4_0.sortStudents()

def var_0_0.Init(arg_8_0):
	arg_8_0.Refresh()

def var_0_0.onStateChange(arg_9_0, arg_9_1, arg_9_2):
	if arg_9_0.sortTimer:
		arg_9_0.sortTimer.Stop()

		arg_9_0.sortTimer = None

	if arg_9_2 == NavalAcademyStudent.ShipState.Walk:
		arg_9_0.sortTimer = Timer.New(function()
			arg_9_0.sortStudents(), 0.2, -1)

		arg_9_0.sortTimer.Start()

def var_0_0.sortStudents(arg_11_0):
	local var_11_0 = {}

	table.insertto(var_11_0, arg_11_0.buildings)

	for iter_11_0, iter_11_1 in pairs(arg_11_0.academyStudents):
		table.insert(var_11_0, iter_11_1._tf)

	table.sort(var_11_0, function(arg_12_0, arg_12_1)
		return arg_12_0.anchoredPosition.y > arg_12_1.anchoredPosition.y)

	local var_11_1 = 0

	for iter_11_2, iter_11_3 in ipairs(var_11_0):
		iter_11_3.SetSiblingIndex(var_11_1)

		var_11_1 = var_11_1 + 1

def var_0_0.onTask(arg_13_0, arg_13_1, arg_13_2):
	local var_13_0 = getProxy(TaskProxy)
	local var_13_1 = getProxy(ActivityProxy)
	local var_13_2 = var_13_1.getActivitiesByType(ActivityConst.ACTIVITY_TYPE_TASK_LIST)
	local var_13_3 = _.detect(var_13_2, function(arg_14_0)
		local var_14_0 = arg_14_0.getTaskShip()

		return var_14_0 and var_14_0.groupId == arg_13_1.groupId)

	if var_13_3 and not var_13_3.isEnd():
		if var_13_3.id == ActivityConst.JYHZ_ACTIVITY_ID and arg_13_2.acceptTaskId:
			local var_13_4 = var_13_0.getAcademyTask(arg_13_1.groupId)
			local var_13_5 = var_13_1.getActivityByType(ActivityConst.ACTIVITY_TYPE_ZPROJECT)

			if var_13_5:
				local var_13_6 = var_13_5.getConfig("config_data")
				local var_13_7 = _.detect(var_13_6, function(arg_15_0)
					local var_15_0 = pg.chapter_template[arg_15_0]

					return _.any(var_15_0.npc_data, function(arg_16_0)
						return pg.npc_squad_template[arg_16_0].task_id == var_13_4))

				if var_13_7 and getProxy(ChapterProxy).getChapterById(var_13_7).active:
					pg.TipsMgr.GetInstance().ShowTips(i18n("task_target_chapter_in_progress"))

					return

		if arg_13_2.type:
			if arg_13_2.type == 1:
				Application.OpenURL(arg_13_2.param)
			elif arg_13_2.type == 2:
				arg_13_0.emit(NavalAcademyMediator.GO_SCENE, arg_13_2.param)
			elif arg_13_2.type == 3:
				arg_13_0.emit(NavalAcademyMediator.OPEN_ACTIVITY_PANEL, tonumber(arg_13_2.param))
			elif arg_13_2.type == 4:
				arg_13_0.emit(NavalAcademyMediator.OPEN_ACTIVITY_SHOP)
			elif arg_13_2.type == 5:
				arg_13_0.emit(NavalAcademyMediator.OPEN_SCROLL, tonumber(arg_13_2.param))
		elif not arg_13_2.currentTask and arg_13_2.acceptTaskId:
			local var_13_8 = getProxy(PlayerProxy).getRawData()
			local var_13_9 = pg.task_data_template[arg_13_2.acceptTaskId]

			if var_13_8.level < var_13_9.level:
				pg.TipsMgr.GetInstance().ShowTips(i18n("task_level_notenough", var_13_9.level))

				return

			arg_13_0.emit(NavalAcademyMediator.ACTIVITY_OP, {
				cmd = 1,
				activity_id = var_13_3.id,
				arg1 = arg_13_2.acceptTaskId
			})
		elif arg_13_2.currentTask:
			if not arg_13_2.currentTask.isFinish() and arg_13_2.currentTask.getConfig("sub_type") == 29:
				arg_13_0.emit(NavalAcademyMediator.TASK_GO, {
					taskVO = arg_13_2.currentTask
				})
			elif not arg_13_2.currentTask.isReceive():
				arg_13_0.emit(NavalAcademyMediator.GO_TASK_SCENE, {
					page = "activity"
				})
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("main_navalAcademyScene_work_done"))

def var_0_0.emit(arg_17_0, ...):
	arg_17_0.parent.emit(...)

def var_0_0.clearStudents(arg_18_0):
	if arg_18_0.sortTimer:
		arg_18_0.sortTimer.Stop()

		arg_18_0.sortTimer = None

	for iter_18_0, iter_18_1 in pairs(arg_18_0.academyStudents):
		iter_18_1.detach()
		Destroy(iter_18_1._go)

	arg_18_0.academyStudents = {}

def var_0_0.Dispose(arg_19_0):
	arg_19_0.clearStudents()

def var_0_0.getStudents(arg_20_0):
	local var_20_0 = {}
	local var_20_1 = {}
	local var_20_2 = getProxy(TaskProxy)
	local var_20_3 = getProxy(ActivityProxy).getActivitiesByType(ActivityConst.ACTIVITY_TYPE_TASK_LIST)

	local function var_20_4(arg_21_0)
		local var_21_0 = arg_21_0.getConfig("config_client")
		local var_21_1 = arg_21_0.getConfig("config_data")
		local var_21_2 = _.flatten(var_21_1)
		local var_21_3
		local var_21_4

		if type(var_21_0) == "table":
			for iter_21_0, iter_21_1 in ipairs(var_21_0):
				var_20_0[iter_21_1.id] = Ship.New(iter_21_1)

				if iter_21_0 == 1:
					var_20_0[iter_21_1.id].withShipFace = True

					local var_21_5 = {}

					if iter_21_1.type:
						var_21_5.type = iter_21_1.type
						var_21_5.param = iter_21_1.param

					local var_21_6, var_21_7 = getActivityTask(arg_21_0, True)

					var_21_5.showTips = var_21_6 and not var_21_7 or var_21_7 and var_21_7.isFinish() and not var_21_7.isReceive()
					var_21_5.acceptTaskId = var_21_6
					var_21_5.currentTask = var_21_7
					var_20_1[iter_21_1.id] = var_21_5
					var_21_3 = var_21_5.acceptTaskId
					var_21_4 = var_21_5.currentTask

				local var_21_8 = iter_21_1.tasks

				if var_21_8:
					var_20_0[iter_21_1.id].hide = True

					local var_21_9 = var_21_4 and table.indexof(var_21_2, var_21_4.id) or table.indexof(var_21_2, var_21_3)

					for iter_21_2, iter_21_3 in ipairs(var_21_8):
						if iter_21_3 == var_21_9:
							var_20_0[iter_21_1.id].hide = False

							break

	_.each(var_20_3, function(arg_22_0)
		if not arg_22_0.isEnd():
			var_20_4(arg_22_0))

	var_20_0 = getProxy(NavalAcademyProxy).fillStudens(var_20_0)

	return var_20_0, var_20_1

return var_0_0
