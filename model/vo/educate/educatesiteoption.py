local var_0_0 = class("EducateSiteOption", import("model.vo.BaseVO"))

var_0_0.TYPE_SHOP = 1
var_0_0.TYPE_EVENT = 2
var_0_0.TYPE_SITE = 3

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.id = arg_1_1
	arg_1_0.configId = arg_1_0.id
	arg_1_0.usedCnt = arg_1_2 or 0
	arg_1_0.remainCnt = arg_1_0.GetOriginalCnt() - arg_1_0.usedCnt
	arg_1_0.curTime = getProxy(EducateProxy).GetCurTime()

	arg_1_0.initTime()
	arg_1_0.initRefreshTime()

def var_0_0.bindConfigTable(arg_2_0):
	return pg.child_site_option

def var_0_0.initTime(arg_3_0):
	if arg_3_0.IsLimitTime():
		local var_3_0 = arg_3_0.getConfig("time_limit")

		arg_3_0.startTime, arg_3_0.endTime = EducateHelper.CfgTime2Time(var_3_0)

def var_0_0.initRefreshTime(arg_4_0):
	if arg_4_0.IsEventType() and arg_4_0.IsCountLimit():
		arg_4_0.refreshWeeks = {}

		local var_4_0 = 9
		local var_4_1 = 60
		local var_4_2 = arg_4_0.getConfig("count_limit")[2]

		table.insert(arg_4_0.refreshWeeks, var_4_0)

		while var_4_0 < var_4_1:
			var_4_0 = var_4_0 + var_4_2

			table.insert(arg_4_0.refreshWeeks, var_4_0)

def var_0_0.IsShowLimit(arg_5_0):
	return arg_5_0.getConfig("is_limit") == 1 and arg_5_0.remainCnt > 0

def var_0_0.IsLimitTime(arg_6_0):
	return #arg_6_0.getConfig("time_limit") != 0

def var_0_0.IsCountLimit(arg_7_0):
	return arg_7_0.getConfig("count_limit") != "" and #arg_7_0.getConfig("count_limit") == 2

def var_0_0.IsShow(arg_8_0):
	if arg_8_0.IsLimitTime():
		return EducateHelper.InTime(arg_8_0.curTime, arg_8_0.startTime, arg_8_0.endTime)
	else
		return True

def var_0_0.GetType(arg_9_0):
	return arg_9_0.getConfig("type")

def var_0_0.IsEventType(arg_10_0):
	return arg_10_0.getConfig("type") == var_0_0.TYPE_EVENT

def var_0_0.IsReplace(arg_11_0):
	return arg_11_0.getConfig("replace") != 0

def var_0_0.GetCost(arg_12_0):
	return arg_12_0.getConfig("cost")

def var_0_0.GetLinkId(arg_13_0):
	return arg_13_0.getConfig("param")[1]

def var_0_0.GetOriginalCnt(arg_14_0):
	return arg_14_0.IsCountLimit() and arg_14_0.getConfig("count_limit")[1] or 999

def var_0_0.GetRemainCnt(arg_15_0):
	return arg_15_0.remainCnt

def var_0_0.GetCntText(arg_16_0):
	if not arg_16_0.IsCountLimit():
		return ""

	return string.format("(%d/%d)", arg_16_0.remainCnt, arg_16_0.getConfig("count_limit")[1])

def var_0_0.CanTrigger(arg_17_0):
	return arg_17_0.remainCnt > 0

def var_0_0.ReduceCnt(arg_18_0):
	arg_18_0.remainCnt = arg_18_0.remainCnt - 1

def var_0_0.IsShowPolaroid(arg_19_0):
	if #arg_19_0.getConfig("polarid_list") == 0:
		return False

	return underscore.any(arg_19_0.getConfig("polarid_list"), function(arg_20_0)
		return not getProxy(EducateProxy).IsExistPolaroidByGroup(arg_20_0) and getProxy(EducateProxy).CanGetPolaroidByGroup(arg_20_0))

def var_0_0.GetResults(arg_21_0):
	if EducateHelper.IsShowNature():
		return arg_21_0.getConfig("result_display")
	else
		return underscore.select(arg_21_0.getConfig("result_display"), function(arg_22_0)
			return arg_22_0[1] != EducateConst.DROP_TYPE_ATTR or not getProxy(EducateProxy).GetCharData().IsPersonalityAttr(arg_22_0[2]))

def var_0_0.IsResetWeek(arg_23_0, arg_23_1):
	return table.contains(arg_23_0.refreshWeeks, arg_23_1)

def var_0_0.OnWeekUpdate(arg_24_0, arg_24_1):
	arg_24_0.curTime = arg_24_1

	arg_24_0.CheckCntReset()

def var_0_0.CheckCntReset(arg_25_0):
	if arg_25_0.IsEventType() and arg_25_0.IsCountLimit():
		local var_25_0 = EducateHelper.GetWeekIdxWithTime(arg_25_0.curTime)

		if arg_25_0.IsResetWeek(var_25_0):
			arg_25_0.remainCnt = arg_25_0.GetOriginalCnt()

return var_0_0
