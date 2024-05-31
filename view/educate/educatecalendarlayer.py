local var_0_0 = class("EducateCalendarLayer", import(".base.EducateBaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "EducateCalendarUI"

def var_0_0.init(arg_2_0):
	arg_2_0.calendarTF = arg_2_0.findTF("anim_root/calendar")
	arg_2_0.monthTF = arg_2_0.findTF("month", arg_2_0.calendarTF)

	setText(arg_2_0.findTF("Text", arg_2_0.monthTF), i18n("word_month"))

	arg_2_0.weekTF = arg_2_0.findTF("week/week", arg_2_0.calendarTF)
	arg_2_0.curTime = getProxy(EducateProxy).GetCurTime()
	arg_2_0.anim = arg_2_0.findTF("anim_root").GetComponent(typeof(Animation))
	arg_2_0.animEvent = arg_2_0.findTF("anim_root").GetComponent(typeof(DftAniEvent))

	arg_2_0.animEvent.SetEndEvent(function()
		arg_2_0.emit(var_0_0.ON_CLOSE))
	arg_2_0.animEvent.SetTriggerEvent(function()
		local var_4_0 = EducateHelper.GetTimeAfterWeeks(arg_2_0.curTime, 1)
		local var_4_1 = EducateHelper.GetShowMonthNumber(var_4_0.month)
		local var_4_2 = i18n("word_which_week", var_4_0.week)

		setText(arg_2_0.monthTF, var_4_1)
		setText(arg_2_0.weekTF, var_4_2))

def var_0_0.didEnter(arg_5_0):
	pg.UIMgr.GetInstance().OverlayPanel(arg_5_0._tf, {
		groupName = arg_5_0.getGroupNameFromData(),
		weight = arg_5_0.getWeightFromData() + 1
	})

	local var_5_0 = EducateHelper.GetShowMonthNumber(arg_5_0.curTime.month)
	local var_5_1 = i18n("word_which_week", arg_5_0.curTime.week)

	setText(arg_5_0.monthTF, var_5_0)
	setText(arg_5_0.weekTF, var_5_1)

def var_0_0.onBackPressed(arg_6_0):
	return

def var_0_0.willExit(arg_7_0):
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_7_0._tf)

	if arg_7_0.contextData.onExit:
		arg_7_0.contextData.onExit()

return var_0_0
