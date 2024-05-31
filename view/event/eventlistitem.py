EventConst = require("view/event/EventConst")

local var_0_0 = class("EventListItem")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.go = arg_1_1
	arg_1_0.tr = arg_1_1.transform
	arg_1_0.dispatch = arg_1_2
	arg_1_0.bgNormal = arg_1_0.findTF("bgNormal$").gameObject
	arg_1_0.bgEmergence = arg_1_0.findTF("bgEmergence$").gameObject
	arg_1_0.timeLimit = arg_1_0.findTF("timeLimit$").gameObject
	arg_1_0.labelLimitTime = arg_1_0.findTF("timeLimit$/labelLimitTime$").GetComponent("Text")
	arg_1_0.iconType = arg_1_0.findTF("iconType$").GetComponent("Image")
	arg_1_0.iconState = arg_1_0.findTF("iconState$")
	arg_1_0.activityLimitBg = arg_1_0.findTF("bgAct")
	arg_1_0.shadow = arg_1_0.findTF("Image").GetComponent(typeof(Image))
	arg_1_0.timerBg = arg_1_0.findTF("labelTime$").GetComponent(typeof(Image))
	arg_1_0.label = arg_1_0.findTF("labelName$/Image").GetComponent(typeof(Text))
	arg_1_0.labelLv = arg_1_0.findTF("level/labelLv$").GetComponent("Text")
	arg_1_0.iconTip = arg_1_0.findTF("iconTip$").gameObject
	arg_1_0.labelName = arg_1_0.findTF("labelName$").GetComponent("Text")
	arg_1_0.labelTime = arg_1_0.findTF("labelTime$/Text").GetComponent("Text")
	arg_1_0.awardsTr = arg_1_0.findTF("awards$")
	arg_1_0.specialAward = arg_1_0.findTF("specialAward/item")
	arg_1_0.awardItem = arg_1_0.findTF("awards$/item").gameObject
	arg_1_0.mark = arg_1_0.findTF("mark")

	SetActive(arg_1_0.mark, False)

	arg_1_0.ptBonus = EventPtBonus.New(arg_1_0.findTF("bonusPt"))

def var_0_0.Update(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0.index = arg_2_1
	arg_2_0.event = arg_2_2

	arg_2_0.Flush()

def var_0_0.UpdateTime(arg_3_0):
	if not arg_3_0.event:
		return

	local var_3_0 = pg.TimeMgr.GetInstance().GetServerTime()

	if arg_3_0.event.state == EventInfo.StateNone:
		arg_3_0.labelTime.gameObject.SetActive(True)

		arg_3_0.labelTime.text = pg.TimeMgr.GetInstance().DescCDTime(arg_3_0.event.template.collect_time)
	elif arg_3_0.event.state == EventInfo.StateActive:
		arg_3_0.labelTime.gameObject.SetActive(True)

		if var_3_0 <= arg_3_0.event.finishTime:
			arg_3_0.labelTime.text = pg.TimeMgr.GetInstance().DescCDTime(arg_3_0.event.finishTime - var_3_0)
		else
			arg_3_0.labelTime.text = "00.00.00"
	elif arg_3_0.event.state == EventInfo.StateFinish:
		arg_3_0.labelTime.gameObject.SetActive(False)

	local var_3_1 = arg_3_0.event.GetCountDownTime()

	if var_3_1 and var_3_1 >= 0:
		arg_3_0.timeLimit.SetActive(True)

		arg_3_0.labelLimitTime.text = pg.TimeMgr.GetInstance().DescCDTime(var_3_1)
	else
		arg_3_0.timeLimit.SetActive(False)

	SetActive(arg_3_0.mark, arg_3_0.event.state == EventInfo.StateFinish)

def var_0_0.Flush(arg_4_0):
	arg_4_0.bgNormal.SetActive(arg_4_0.event.template.type != 2)
	arg_4_0.bgEmergence.SetActive(arg_4_0.event.template.type == 2)

	if arg_4_0.event.state == EventInfo.StateFinish:
		arg_4_0.iconTip.SetActive(True)
	else
		arg_4_0.iconTip.SetActive(False)

	LoadImageSpriteAsync("eventtype/" .. arg_4_0.event.template.icon, arg_4_0.iconType, True)

	local var_4_0 = arg_4_0.event.IsActivityType()

	arg_4_0.iconType.transform.localScale = var_4_0 and Vector3.one or Vector3(1.5, 1.5, 1.5)

	setActive(arg_4_0.activityLimitBg, var_4_0)
	setActive(arg_4_0.shadow.gameObject, not var_4_0)

	arg_4_0.timerBg.color = var_4_0 and Color.New(0, 0, 0, 0) or Color.New(1, 1, 1, 1)
	arg_4_0.label.color = var_4_0 and Color.New(0.9411764705882353, 0.803921568627451, 1, 1) or Color.New(0.6431372549019608, 0.8117647058823529, 0.9725490196078431, 1)

	eachChild(arg_4_0.iconState, function(arg_5_0)
		setActive(arg_5_0, arg_5_0.gameObject.name == tostring(arg_4_0.event.state)))

	arg_4_0.labelLv.text = "" .. arg_4_0.event.template.lv
	arg_4_0.labelName.text = arg_4_0.event.template.title

	local var_4_1 = arg_4_0.event.template.drop_display

	for iter_4_0 = arg_4_0.awardsTr.childCount, #var_4_1 - 1:
		Object.Instantiate(arg_4_0.awardItem).transform.SetParent(arg_4_0.awardsTr, False)

	local var_4_2 = arg_4_0.awardsTr.childCount

	for iter_4_1 = 0, var_4_2 - 1:
		local var_4_3 = arg_4_0.awardsTr.GetChild(iter_4_1)

		if iter_4_1 < #var_4_1:
			var_4_3.gameObject.SetActive(True)

			local var_4_4 = var_4_1[iter_4_1 + 1]

			updateDrop(var_4_3, {
				type = var_4_4.type,
				id = var_4_4.id,
				count = var_4_4.nums
			})
		else
			var_4_3.gameObject.SetActive(False)

	local var_4_5 = table.getCount(arg_4_0.event.template.special_drop) != 0

	SetActive(arg_4_0.specialAward, var_4_5)

	if var_4_5:
		updateDrop(arg_4_0.specialAward, {
			type = arg_4_0.event.template.special_drop.type,
			id = arg_4_0.event.template.special_drop.id
		})

def var_0_0.Clear(arg_6_0):
	return

def var_0_0.findTF(arg_7_0, arg_7_1):
	return findTF(arg_7_0.tr, arg_7_1)

return var_0_0
