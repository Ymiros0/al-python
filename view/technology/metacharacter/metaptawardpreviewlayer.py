local var_0_0 = class("MetaPTAwardPreviewLayer", import("...base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "MetaPTAwardPreviewUI"

def var_0_0.init(arg_2_0):
	arg_2_0.initUITextTips()
	arg_2_0.initData()
	arg_2_0.findUI()
	arg_2_0.addListener()
	arg_2_0.initScrollList()

def var_0_0.didEnter(arg_3_0):
	pg.UIMgr.GetInstance().BlurPanel(arg_3_0._tf, False, {
		weight = LayerWeightConst.THIRD_LAYER
	})
	arg_3_0.updatePTInfo()
	arg_3_0.updateScrollList()

def var_0_0.willExit(arg_4_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_4_0._tf)

def var_0_0.initUITextTips(arg_5_0):
	local var_5_0 = arg_5_0.findTF("Panel/AwardTpl/PointLight/PointTipText")
	local var_5_1 = arg_5_0.findTF("Panel/AwardTpl/PointGray/PointTipText")
	local var_5_2 = arg_5_0.findTF("Panel/AwardTpl/GetText")
	local var_5_3 = arg_5_0.findTF("Panel/AwardTpl/GotText")

	setText(var_5_0, i18n("meta_pt_point"))
	setText(var_5_1, i18n("meta_pt_point"))
	setText(var_5_2, i18n("meta_award_get"))
	setText(var_5_3, i18n("meta_award_got"))

def var_0_0.initData(arg_6_0):
	arg_6_0.curMetaProgressVO = arg_6_0.contextData.metaProgressVO
	arg_6_0.ptData = arg_6_0.curMetaProgressVO.metaPtData
	arg_6_0.itemNum = #arg_6_0.ptData.dropList

def var_0_0.findUI(arg_7_0):
	arg_7_0.bg = arg_7_0.findTF("BG")

	local var_7_0 = arg_7_0.findTF("Panel")
	local var_7_1 = arg_7_0.findTF("PT", var_7_0)

	arg_7_0.ptNumText = arg_7_0.findTF("NumText", var_7_1)
	arg_7_0.ptIcon = arg_7_0.findTF("PTIcon", var_7_1)
	arg_7_0.scrollViewTF = arg_7_0.findTF("ScrollView", var_7_0)
	arg_7_0.awardContainerTF = arg_7_0.findTF("ScrollView/Viewport/Content", var_7_0)
	arg_7_0.awardTpl = arg_7_0.findTF("AwardTpl", var_7_0)

	local var_7_2 = arg_7_0.findTF("NotchAdapt")

	arg_7_0.nextArrow = arg_7_0.findTF("NextBtn", var_7_2)
	arg_7_0.preArrow = arg_7_0.findTF("PreBtn", var_7_2)
	arg_7_0.sizeW = GetComponent(arg_7_0.awardTpl, "LayoutElement").preferredWidth
	arg_7_0.spaceW = GetComponent(arg_7_0.awardContainerTF, "HorizontalLayoutGroup").spacing
	arg_7_0.leftW = GetComponent(arg_7_0.awardContainerTF, "HorizontalLayoutGroup").padding.left

def var_0_0.addListener(arg_8_0):
	onButton(arg_8_0, arg_8_0.bg, function()
		arg_8_0.closeView(), SFX_PANEL)

def var_0_0.initScrollList(arg_10_0):
	arg_10_0.awardUIItemList = UIItemList.New(arg_10_0.awardContainerTF, arg_10_0.awardTpl)

	arg_10_0.awardUIItemList.make(function(arg_11_0, arg_11_1, arg_11_2)
		if arg_11_0 == UIItemList.EventUpdate:
			arg_10_0.updateAwardTpl(arg_11_2, arg_11_1 + 1))

	arg_10_0.scrollRectSC = arg_10_0.scrollViewTF.GetComponent("ScrollRect")

	arg_10_0.scrollRectSC.onValueChanged.AddListener(function(arg_12_0)
		setActive(arg_10_0.preArrow, arg_12_0.x >= 0.01)
		setActive(arg_10_0.nextArrow, arg_12_0.x <= 0.99))

def var_0_0.updateScrollList(arg_13_0):
	local var_13_0, var_13_1, var_13_2 = arg_13_0.curMetaProgressVO.metaPtData.GetLevelProgress()

	arg_13_0.awardUIItemList.align(var_13_1)

	local var_13_3 = (var_13_0 - 1) * (arg_13_0.sizeW + arg_13_0.spaceW)

	setLocalPosition(arg_13_0.awardContainerTF, {
		x = -var_13_3
	})

	if var_13_0 > 1:
		setActive(arg_13_0.preArrow, True)

def var_0_0.updateAwardTpl(arg_14_0, arg_14_1, arg_14_2):
	local var_14_0 = arg_14_0.findTF("Item", arg_14_1)
	local var_14_1 = arg_14_0.findTF("mask", var_14_0)
	local var_14_2 = arg_14_0.findTF("Got", var_14_1)
	local var_14_3 = arg_14_0.findTF("Lock", var_14_1)
	local var_14_4 = arg_14_0.findTF("PointLight", arg_14_1)
	local var_14_5 = arg_14_0.findTF("NumText", var_14_4)
	local var_14_6 = arg_14_0.findTF("PointGray", arg_14_1)
	local var_14_7 = arg_14_0.findTF("NumText", var_14_6)
	local var_14_8 = arg_14_0.findTF("GetText", arg_14_1)
	local var_14_9 = arg_14_0.findTF("GotText", arg_14_1)
	local var_14_10 = arg_14_0.findTF("LockText", arg_14_1)
	local var_14_11 = arg_14_0.findTF("LineTpl", arg_14_1)
	local var_14_12 = arg_14_0.findTF("LineTpl/Light", arg_14_1)
	local var_14_13 = arg_14_0.findTF("LineTpl/Dark", arg_14_1)
	local var_14_14 = arg_14_0.ptData.dropList[arg_14_2]
	local var_14_15 = arg_14_0.ptData.targets[arg_14_2]
	local var_14_16 = {
		type = var_14_14[1],
		id = var_14_14[2],
		count = var_14_14[3]
	}

	updateDrop(var_14_0, var_14_16, {
		hideName = True
	})
	onButton(arg_14_0, var_14_0, function()
		arg_14_0.emit(BaseUI.ON_DROP, var_14_16), SFX_PANEL)
	setText(var_14_5, var_14_15)
	setText(var_14_7, var_14_15)
	setText(var_14_10, "PHASE " .. math.floor(var_14_15 / arg_14_0.curMetaProgressVO.unlockPTNum * 100) .. "%")

	if arg_14_2 < arg_14_0.ptData.level + 1:
		setActive(var_14_1, True)
		setActive(var_14_2, True)
		setActive(var_14_3, False)
		setActive(var_14_4, False)
		setActive(var_14_6, True)
		setActive(var_14_12, False)
		setActive(var_14_13, True)
		setActive(var_14_8, False)
		setActive(var_14_9, True)
		setActive(var_14_10, False)
	elif var_14_15 > arg_14_0.ptData.count:
		setActive(var_14_1, True)
		setActive(var_14_2, False)
		setActive(var_14_3, True)
		setActive(var_14_4, False)
		setActive(var_14_6, True)
		setActive(var_14_12, False)
		setActive(var_14_13, True)
		setActive(var_14_8, False)
		setActive(var_14_9, False)
		setActive(var_14_10, True)
	else
		setActive(var_14_1, False)
		setActive(var_14_2, False)
		setActive(var_14_3, False)
		setActive(var_14_4, True)
		setActive(var_14_6, False)
		setActive(var_14_12, True)
		setActive(var_14_13, False)
		setActive(var_14_8, True)
		setActive(var_14_9, False)
		setActive(var_14_10, False)

	if arg_14_2 == 1:
		setActive(var_14_11, False)

def var_0_0.updatePTInfo(arg_16_0):
	setImageSprite(arg_16_0.ptIcon, LoadSprite(arg_16_0.curMetaProgressVO.getPtIconPath()))
	setText(arg_16_0.ptNumText, arg_16_0.ptData.count)

return var_0_0
