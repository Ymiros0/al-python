local var_0_0 = class("EducateSchedulePerformLayer", import(".base.EducateBaseUI"))
local var_0_1 = {
	"FFFFFF",
	"79D3FE",
	"818183"
}
local var_0_2 = {
	"39BFFF",
	"39BFFF",
	"2D2E2F"
}

def var_0_0.getUIName(arg_1_0):
	return "EducateSchedulePerformUI"

def var_0_0.init(arg_2_0):
	arg_2_0.initData()
	arg_2_0.findUI()

def var_0_0.initData(arg_3_0):
	arg_3_0.planCnt = getProxy(EducateProxy).GetCharData().GetNextWeekPlanCnt()
	arg_3_0.curDay = 1
	arg_3_0.curIndex = 1
	arg_3_0.events = arg_3_0.contextData.events
	arg_3_0.drops = {}
	arg_3_0.isSkip = arg_3_0.contextData.skip

	underscore.each(arg_3_0.contextData.plan_results, function(arg_4_0)
		if not arg_3_0.drops[arg_4_0.day]:
			arg_3_0.drops[arg_4_0.day] = {}

		arg_3_0.drops[arg_4_0.day][arg_4_0.index] = {
			plan_drops = arg_4_0.plan_drops,
			event_drops = arg_4_0.event_drops,
			spec_event_drops = arg_4_0.spec_event_drops
		})

	arg_3_0.showGrids = arg_3_0.contextData.gridData
	arg_3_0.showEventIds = {}

	underscore.each(arg_3_0.events, function(arg_5_0)
		if not arg_3_0.showEventIds[arg_5_0.day]:
			arg_3_0.showEventIds[arg_5_0.day] = {}

		arg_3_0.showEventIds[arg_5_0.day][arg_5_0.index] = arg_5_0.value[1].event_id)

def var_0_0.findUI(arg_6_0):
	arg_6_0.windowsTF = arg_6_0.findTF("anim_root/window")
	arg_6_0.leftTF = arg_6_0.findTF("left", arg_6_0.windowsTF)

	setText(arg_6_0.findTF("title/Text", arg_6_0.leftTF), i18n("child_plan_perform_title"))

	arg_6_0.dayUIList = UIItemList.New(arg_6_0.findTF("content", arg_6_0.leftTF), arg_6_0.findTF("content/day_tpl", arg_6_0.leftTF))
	arg_6_0.rightTF = arg_6_0.findTF("right", arg_6_0.windowsTF)
	arg_6_0.planNameTF = arg_6_0.findTF("name", arg_6_0.rightTF)

def var_0_0.didEnter(arg_7_0):
	pg.UIMgr.GetInstance().OverlayPanel(arg_7_0._tf, {
		groupName = arg_7_0.getGroupNameFromData(),
		weight = arg_7_0.getWeightFromData() + 1
	})
	pg.PerformMgr.GetInstance().SetParamForUI(arg_7_0.__cname)
	arg_7_0.initDayList()
	arg_7_0.playWeek(function()
		arg_7_0.emit(var_0_0.ON_CLOSE))

def var_0_0.initDayList(arg_9_0):
	arg_9_0.dayUIList.make(function(arg_10_0, arg_10_1, arg_10_2)
		if arg_10_0 == UIItemList.EventInit:
			local var_10_0 = arg_10_1 + 1

			arg_10_2.name = var_10_0

			setText(arg_9_0.findTF("Text", arg_10_2), EducateHelper.GetWeekStrByNumber(var_10_0))

			for iter_10_0 = 1, 3:
				local var_10_1 = arg_9_0.findTF("phase" .. iter_10_0, arg_10_2)

				setActive(var_10_1, iter_10_0 == arg_9_0.planCnt)
		elif arg_10_0 == UIItemList.EventUpdate:
			local var_10_2 = arg_10_1 + 1

			setActive(arg_9_0.findTF("selected", arg_10_2), arg_9_0.curDay == var_10_2)

			local var_10_3 = arg_9_0.findTF("Text", arg_10_2)
			local var_10_4 = "FFFFFF"
			local var_10_5 = "FFFFFF"

			if var_10_2 < arg_9_0.curDay:
				var_10_4 = var_0_1[1]
				var_10_5 = var_0_2[1]
			elif arg_9_0.curDay == var_10_2:
				var_10_4 = var_0_1[2]
				var_10_5 = var_0_2[3]
			else
				var_10_4 = var_0_1[3]
				var_10_5 = var_0_2[3]

			setTextColor(var_10_3, Color.NewHex(var_10_4))

			local var_10_6 = arg_9_0.findTF("phase" .. arg_9_0.planCnt, arg_10_2)

			for iter_10_1 = 1, var_10_6.childCount:
				local var_10_7 = var_10_5

				if arg_9_0.curDay == var_10_2 and iter_10_1 <= arg_9_0.curIndex:
					var_10_7 = var_0_2[2]

				setImageColor(var_10_6.GetChild(iter_10_1 - 1), Color.NewHex(var_10_7)))
	arg_9_0.updateLeft()

def var_0_0.updateLeft(arg_11_0):
	arg_11_0.dayUIList.align(6)

def var_0_0.playWeek(arg_12_0, arg_12_1):
	arg_12_0.curDay = 1
	arg_12_0.curIndex = 1

	arg_12_0.emit(EducateSchedulePerformMediator.WEEKDAY_UPDATE, arg_12_0.curDay)

	local var_12_0 = {}

	for iter_12_0 = 1, 6:
		for iter_12_1 = 1, 3:
			local var_12_1 = arg_12_0.drops[iter_12_0][iter_12_1] or {}
			local var_12_2 = arg_12_0.showEventIds[iter_12_0] and arg_12_0.showEventIds[iter_12_0][iter_12_1] and arg_12_0.showEventIds[iter_12_0][iter_12_1] != 0

			if arg_12_0.showGrids[iter_12_0] and arg_12_0.showGrids[iter_12_0][iter_12_1]:
				local var_12_3 = arg_12_0.showGrids[iter_12_0][iter_12_1]

				table.insert(var_12_0, function(arg_13_0)
					arg_12_0.curDay = iter_12_0
					arg_12_0.curIndex = iter_12_1

					arg_12_0.emit(EducateSchedulePerformMediator.WEEKDAY_UPDATE, arg_12_0.curDay)
					arg_12_0.updateLeft()
					setText(arg_12_0.planNameTF, var_12_3.GetName())

					local var_13_0 = var_12_3.IsPlan() and var_12_1.plan_drops or var_12_1.spec_event_drops

					if arg_12_0.isSkip:
						if not var_12_3.IsPlan() or var_12_2:
							pg.PerformMgr.GetInstance().PlayGroupNoHide(var_12_3.GetPerformance(), arg_13_0, var_13_0 or {})
						else
							arg_13_0()
					else
						pg.PerformMgr.GetInstance().PlayGroupNoHide(var_12_3.GetPerformance(), arg_13_0, var_13_0 or {}))

			if var_12_2:
				local var_12_4 = arg_12_0.showEventIds[iter_12_0][iter_12_1]

				table.insert(var_12_0, function(arg_14_0)
					pg.PerformMgr.GetInstance().PlayGroupNoHide(pg.child_event[var_12_4].performance, arg_14_0, var_12_1.event_drops or {}))

	pg.PerformMgr.GetInstance().Show()
	seriesAsync(var_12_0, function()
		pg.PerformMgr.GetInstance().Hide()
		onNextTick(function()
			if arg_12_1:
				arg_12_1()))

def var_0_0.onBackPressed(arg_17_0):
	return

def var_0_0.willExit(arg_18_0):
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_18_0._tf)
	pg.PerformMgr.GetInstance().SetParamForUI("Default")

	if arg_18_0.contextData.onExit:
		arg_18_0.contextData.onExit()

return var_0_0
