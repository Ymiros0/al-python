local var_0_0 = class("EducateDatePanel", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "EducateDatePanel"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.timeTF = arg_2_0.findTF("content/top/time")
	arg_2_0.weekTF = arg_2_0.findTF("week", arg_2_0.timeTF)
	arg_2_0.dayTF = arg_2_0.findTF("day", arg_2_0.timeTF)
	arg_2_0.homeTF = arg_2_0.findTF("content/top/home")

	setText(arg_2_0.findTF("Text", arg_2_0.homeTF), i18n("child_date_text1"))

	arg_2_0.schoolTF = arg_2_0.findTF("content/top/school")

	setText(arg_2_0.findTF("Text", arg_2_0.schoolTF), i18n("child_date_text2"))

	arg_2_0.upgradeTF = arg_2_0.findTF("content/top/upgrade")

	setText(arg_2_0.findTF("Text", arg_2_0.upgradeTF), i18n("child_date_text3"))

	arg_2_0.dataTF = arg_2_0.findTF("content/top/data")

	setText(arg_2_0.findTF("Text", arg_2_0.dataTF), i18n("child_date_text4"))

	arg_2_0.newsBtn = arg_2_0.findTF("content/bottom")

	onButton(arg_2_0, arg_2_0.newsBtn, function()
		arg_2_0.emit(EducateBaseUI.EDUCATE_GO_SUBLAYER, Context.New({
			mediator = EducateNewsMediator,
			viewComponent = EducateNewsLayer
		})), SFX_PANEL)

	arg_2_0.targetSetDays = getProxy(EducateProxy).GetTaskProxy().GetTargetSetDays()

	arg_2_0.Flush()

def var_0_0.Flush(arg_4_0):
	if not arg_4_0.GetLoaded():
		return

	arg_4_0.curTime = getProxy(EducateProxy).GetCurTime()
	arg_4_0.status = getProxy(EducateProxy).GetGameStatus()

	setActive(arg_4_0.homeTF, arg_4_0.isHomeShow())
	setActive(arg_4_0.schoolTF, arg_4_0.isSchoolShow())
	setActive(arg_4_0.upgradeTF, arg_4_0.isUpgradeShow())
	setActive(arg_4_0.dataTF, arg_4_0.status == EducateConst.STATUES_RESET)

	local var_4_0 = arg_4_0.isTimeShow()

	setActive(arg_4_0.timeTF, var_4_0)

	if var_4_0:
		local var_4_1 = arg_4_0.curTime.month
		local var_4_2 = EducateHelper.GetShowMonthNumber(var_4_1) .. i18n("word_month") .. i18n("word_which_week", arg_4_0.curTime.week)

		setText(arg_4_0.weekTF, var_4_2)
		setText(arg_4_0.dayTF, EducateHelper.GetWeekStrByNumber(arg_4_0.curTime.day))

def var_0_0.UpdateWeekDay(arg_5_0, arg_5_1):
	if not arg_5_0.GetLoaded():
		return

	local var_5_0 = EducateHelper.GetTimeAfterWeeks(getProxy(EducateProxy).GetCurTime(), 1)
	local var_5_1 = EducateHelper.GetShowMonthNumber(var_5_0.month) .. i18n("word_month") .. i18n("word_which_week", var_5_0.week)

	setText(arg_5_0.weekTF, var_5_1)
	setText(arg_5_0.dayTF, EducateHelper.GetWeekStrByNumber(arg_5_1))

def var_0_0.isHomeShow(arg_6_0):
	return EducateHelper.IsSameDay(arg_6_0.curTime, arg_6_0.targetSetDays[1])

def var_0_0.isSchoolShow(arg_7_0):
	return EducateHelper.IsSameDay(arg_7_0.curTime, arg_7_0.targetSetDays[2])

def var_0_0.isUpgradeShow(arg_8_0):
	return EducateHelper.IsSameDay(arg_8_0.curTime, arg_8_0.targetSetDays[3]) or EducateHelper.IsSameDay(arg_8_0.curTime, arg_8_0.targetSetDays[4])

def var_0_0.isTimeShow(arg_9_0):
	return not isActive(arg_9_0.homeTF) and not isActive(arg_9_0.schoolTF) and not isActive(arg_9_0.upgradeTF) and not isActive(arg_9_0.dataTF)

return var_0_0
