local var_0_0 = class("TrophyDetailPanel")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._go = arg_1_1
	arg_1_0._tf = arg_1_1.transform
	arg_1_0._parent = arg_1_2
	arg_1_0.UIMgr = pg.UIMgr.GetInstance()

	pg.DelegateInfo.New(arg_1_0)

	arg_1_0._medalIcon = findTF(arg_1_0._tf, "center/medalBG/icon")
	arg_1_0._nameLabel = findTF(arg_1_0._tf, "center/name")
	arg_1_0._timeStamp = findTF(arg_1_0._tf, "center/timeStamp/Text").GetComponent(typeof(Text))
	arg_1_0._desc = findTF(arg_1_0._tf, "center/desc/Text").GetComponent(typeof(Text))
	arg_1_0._progressBar = findTF(arg_1_0._tf, "center/progress_bar/progress")
	arg_1_0._rank = findTF(arg_1_0._tf, "center/rank/Text").GetComponent(typeof(Text))
	arg_1_0._lock = findTF(arg_1_0._tf, "center/medalBG/lock")
	arg_1_0._conditionList = findTF(arg_1_0._tf, "center/conditions/container")
	arg_1_0._conditionTpl = findTF(arg_1_0._tf, "center/conditions/condition_tpl")

	onButton(arg_1_0, arg_1_0._go, function()
		arg_1_0.SetActive(False), SFX_CANCEL)

	arg_1_0._stepper = findTF(arg_1_0._tf, "center/stepper")
	arg_1_0._preTrophyBtn = findTF(arg_1_0._stepper, "pre")
	arg_1_0._postTrophyBtn = findTF(arg_1_0._stepper, "post")
	arg_1_0._pageText = findTF(arg_1_0._stepper, "page")
	arg_1_0._backTipsText = findTF(arg_1_0._tf, "center/backTips/GameObject (1)")

	setText(arg_1_0._backTipsText, i18n("world_collection_back"))
	onButton(arg_1_0, arg_1_0._postTrophyBtn, function()
		local var_3_0 = arg_1_0._trophyGroup.getPostTrophy(arg_1_0._trophy)

		arg_1_0.UpdateTrophy(var_3_0))
	onButton(arg_1_0, arg_1_0._preTrophyBtn, function()
		local var_4_0 = arg_1_0._trophyGroup.getPreTrophy(arg_1_0._trophy)

		arg_1_0.UpdateTrophy(var_4_0))

	arg_1_0._active = False

def var_0_0.SetTrophyGroup(arg_5_0, arg_5_1):
	arg_5_0._trophyGroup = arg_5_1

def var_0_0.UpdateTrophy(arg_6_0, arg_6_1):
	if arg_6_1 == None:
		return

	arg_6_0._trophy = arg_6_1
	arg_6_0._rank.text = arg_6_1.getConfig("rank")
	arg_6_0._desc.text = arg_6_1.getConfig("desc")

	if arg_6_1.isClaimed():
		local var_6_0 = pg.TimeMgr.GetInstance().STimeDescS(arg_6_1.timestamp, "*t")

		arg_6_0._timeStamp.text = var_6_0.year .. "/" .. var_6_0.month .. "/" .. var_6_0.day
	else
		arg_6_0._timeStamp.text = "-"

	removeAllChildren(arg_6_0._conditionList)
	LoadImageSpriteAsync("medal/" .. arg_6_1.getConfig("icon"), arg_6_0._medalIcon, True)
	SetActive(arg_6_0._lock, not arg_6_1.isClaimed())
	LoadImageSpriteAsync("medal/" .. arg_6_1.getConfig("label"), arg_6_0._nameLabel, True)

	local function var_6_1(arg_7_0, arg_7_1)
		setText(findTF(arg_7_0, "desc"), arg_7_1.getConfig("condition"))

		local var_7_0, var_7_1 = arg_7_1.getProgress()

		if arg_7_1.getTargetType() == Trophy.INTAMACT_TYPE:
			setText(findTF(arg_7_0, "progress"), arg_7_1.isDummy() and "" or "[" .. math.modf(var_7_0 / 100) .. "/" .. math.modf(var_7_1 / 100) .. "]")
		else
			setText(findTF(arg_7_0, "progress"), arg_7_1.isDummy() and "" or "[" .. var_7_0 .. "/" .. var_7_1 .. "]")

	if not arg_6_1.isComplexTrophy():
		local var_6_2 = cloneTplTo(arg_6_0._conditionTpl, arg_6_0._conditionList)

		var_6_1(var_6_2, arg_6_1)
	else
		for iter_6_0, iter_6_1 in pairs(arg_6_1.getSubTrophy()):
			local var_6_3 = cloneTplTo(arg_6_0._conditionTpl, arg_6_0._conditionList)

			var_6_1(var_6_3, iter_6_1)

	arg_6_0._progressBar.GetComponent(typeof(Image)).fillAmount = arg_6_1.getProgressRate()

	arg_6_0.updateStepper(arg_6_1)

def var_0_0.updateStepper(arg_8_0, arg_8_1):
	local var_8_0 = arg_8_0._trophyGroup.getTrophyIndex(arg_8_0._trophy)
	local var_8_1 = arg_8_0._trophyGroup.getTrophyCount()

	setText(arg_8_0._pageText, var_8_0 .. "/" .. var_8_1)

def var_0_0.SetActive(arg_9_0, arg_9_1):
	SetActive(arg_9_0._go, arg_9_1)

	arg_9_0._active = arg_9_1

	if arg_9_1:
		pg.UIMgr.GetInstance().BlurPanel(arg_9_0._go, False, {
			weight = LayerWeightConst.SECOND_LAYER
		})
	else
		pg.UIMgr.GetInstance().UnblurPanel(arg_9_0._go, arg_9_0._parent)

def var_0_0.IsActive(arg_10_0):
	return arg_10_0._active

def var_0_0.Dispose(arg_11_0):
	pg.DelegateInfo.Dispose(arg_11_0)

return var_0_0
