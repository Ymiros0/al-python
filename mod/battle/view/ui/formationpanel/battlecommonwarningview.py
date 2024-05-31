ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleDataFunction
local var_0_2 = var_0_0.Battle.BattleSkillEditCustomWarning
local var_0_3 = class("BattleCommonWarningView")

var_0_0.Battle.BattleCommonWarningView = var_0_3
var_0_3.__name = "BattleCommonWarningView"
var_0_3.WARNING_TYPE_SUBMARINE = "submarine"
var_0_3.WARNING_TYPE_ARTILLERY = "artillery"

def var_0_3.Ctor(arg_1_0, arg_1_1):
	arg_1_0._submarineCount = 0
	arg_1_0._go = arg_1_1
	arg_1_0._tf = arg_1_1.transform
	arg_1_0._subIcon = arg_1_0._tf.Find("submarineIcon")
	arg_1_0._tips = arg_1_0._tf.Find("warningTips")
	arg_1_0._subWarn = arg_1_0._tf.Find("submarineWarningTips")
	arg_1_0._warningRequestTable = {
		{
			flag = False,
			type = var_0_3.WARNING_TYPE_ARTILLERY,
			tf = arg_1_0._tips
		},
		{
			flag = False,
			type = var_0_3.WARNING_TYPE_SUBMARINE,
			tf = arg_1_0._subWarn
		}
	}
	arg_1_0._customWarningTpl = arg_1_0._tf.Find("customWarningTpl")
	arg_1_0._customWarningContainer = arg_1_0._tf.Find("customWarningContainer")
	arg_1_0._customWarningList = {}

def var_0_3.UpdateHostileSubmarineCount(arg_2_0, arg_2_1):
	if arg_2_1 > 0 and arg_2_0._submarineCount <= 0:
		arg_2_0.activeSubmarineWarning()
	elif arg_2_0._submarineCount > 0 and arg_2_1 <= 0:
		arg_2_0.deactiveSubmarineWarning()

	arg_2_0._submarineCount = arg_2_1

def var_0_3.GetCount(arg_3_0):
	return arg_3_0._submarineCount

def var_0_3.ActiveWarning(arg_4_0, arg_4_1):
	local var_4_0 = False
	local var_4_1 = #arg_4_0._warningRequestTable

	for iter_4_0, iter_4_1 in ipairs(arg_4_0._warningRequestTable):
		if arg_4_1 == iter_4_1.type:
			iter_4_1.flag = True

			if not var_4_0:
				SetActive(iter_4_1.tf, True)

				var_4_1 = iter_4_0
			else
				break
		else
			var_4_0 = var_4_0 or iter_4_1.flag

			if iter_4_1.flag and var_4_1 < iter_4_0:
				SetActive(iter_4_1.tf, False)

def var_0_3.DeactiveWarning(arg_5_0, arg_5_1):
	for iter_5_0, iter_5_1 in ipairs(arg_5_0._warningRequestTable):
		if arg_5_1 == iter_5_1.type:
			iter_5_1.flag = False

			SetActive(iter_5_1.tf, False)
		elif iter_5_1.flag:
			arg_5_0.ActiveWarning(iter_5_1.type)

			break

def var_0_3.EditCustomWarning(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_1.op
	local var_6_1 = arg_6_1.key

	if var_6_0 == var_0_2.OP_ADD:
		local var_6_2 = cloneTplTo(arg_6_0._customWarningTpl, arg_6_0._customWarningContainer)
		local var_6_3 = var_0_0.Battle.BattleCustomWarningLabel.New(var_6_2)

		var_6_3.ConfigData(arg_6_1)

		arg_6_0._customWarningList[var_6_1] = var_6_3
	elif var_6_0 == var_0_2.OP_REMOVE:
		local var_6_4 = arg_6_0._customWarningList[var_6_1]

		if var_6_4:
			var_6_4.SetExpire()
	elif var_6_0 == var_0_2.OP_REMOVE_PERMANENT:
		for iter_6_0, iter_6_1 in pairs(arg_6_0._customWarningList):
			if iter_6_1.GetDuration() <= 0:
				iter_6_1.SetExpire()
	elif var_6_0 == var_0_2.OP_REMOVE_TEMPLATE:
		for iter_6_2, iter_6_3 in pairs(arg_6_0._customWarningList):
			if iter_6_3.GetDuration() > 0:
				iter_6_3.SetExpire()

def var_0_3.Update(arg_7_0):
	for iter_7_0, iter_7_1 in pairs(arg_7_0._customWarningList):
		iter_7_1.Update()

		if iter_7_1.IsExpire():
			iter_7_1.Dispose()

			arg_7_0._customWarningList[iter_7_0] = None

def var_0_3.activeSubmarineWarning(arg_8_0):
	SetActive(arg_8_0._subIcon, True)
	arg_8_0.ActiveWarning(var_0_3.WARNING_TYPE_SUBMARINE)
	LeanTween.cancel(go(arg_8_0._subIcon))
	LeanTween.alpha(rtf(arg_8_0._subIcon), 1, 2).setFrom(0)

def var_0_3.deactiveSubmarineWarning(arg_9_0):
	LeanTween.cancel(go(arg_9_0._subIcon))
	LeanTween.alpha(rtf(arg_9_0._subIcon), 0, 1).setFrom(1).setOnComplete(System.Action(function()
		SetActive(arg_9_0._subIcon, False)
		arg_9_0.DeactiveWarning(var_0_3.WARNING_TYPE_SUBMARINE)))

def var_0_3.Dispose(arg_11_0):
	for iter_11_0, iter_11_1 in pairs(arg_11_0._customWarningList):
		iter_11_1.Dispose()

		arg_11_0._customWarningList[iter_11_0] = None

	arg_11_0._customWarningList = None
	arg_11_0._go = None
	arg_11_0._tf = None
	arg_11_0._icon = None
	arg_11_0._tips = None
