local var_0_0 = class("MetaExpView", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "MetaExpUI"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.initUITip()
	arg_2_0.initData()
	arg_2_0.initUI()
	arg_2_0.addListener()
	arg_2_0.updateIconList()

def var_0_0.OnDestroy(arg_3_0):
	if arg_3_0.closeCB:
		arg_3_0.closeCB()

def var_0_0.setData(arg_4_0, arg_4_1, arg_4_2):
	arg_4_0.expInfoList = arg_4_1
	arg_4_0.closeCB = arg_4_2

def var_0_0.initUITip(arg_5_0):
	local var_5_0 = arg_5_0.findTF("Panel/Title/Text")

	setText(var_5_0, i18n("battle_end_subtitle2"))

def var_0_0.initData(arg_6_0):
	arg_6_0.metaProxy = getProxy(MetaCharacterProxy)

def var_0_0.initUI(arg_7_0):
	arg_7_0.bg = arg_7_0.findTF("BG")
	arg_7_0.iconTpl = arg_7_0.findTF("IconTpl")
	arg_7_0.panelTF = arg_7_0.findTF("Panel")
	arg_7_0.iconContainer = arg_7_0.findTF("ScrollView/Content", arg_7_0.panelTF)
	arg_7_0.gridLayoutGroupSC = GetComponent(arg_7_0.iconContainer, typeof(GridLayoutGroup))
	arg_7_0.iconUIItemList = UIItemList.New(arg_7_0.iconContainer, arg_7_0.iconTpl)

def var_0_0.addListener(arg_8_0):
	return

def var_0_0.updateIconList(arg_9_0):
	local var_9_0 = arg_9_0.expInfoList or arg_9_0.metaProxy.getMetaTacticsInfoOnEnd()
	local var_9_1 = arg_9_0.sortDataList(var_9_0)
	local var_9_2 = #var_9_1

	arg_9_0.gridLayoutGroupSC.constraintCount = var_9_2 > 4 and 2 or 1

	arg_9_0.iconUIItemList.make(function(arg_10_0, arg_10_1, arg_10_2)
		arg_10_1 = arg_10_1 + 1

		if arg_10_0 == UIItemList.EventUpdate:
			local var_10_0 = arg_9_0.findTF("Icon", arg_10_2)
			local var_10_1 = arg_9_0.findTF("AddExpText", arg_10_2)
			local var_10_2 = arg_9_0.findTF("LevelMaxText", arg_10_2)
			local var_10_3 = arg_9_0.findTF("ExpMaxText", arg_10_2)
			local var_10_4 = arg_9_0.findTF("Slider", arg_10_2)
			local var_10_5 = arg_9_0.findTF("Light", arg_10_2)
			local var_10_6 = var_9_1[arg_10_1]
			local var_10_7 = var_10_6.shipID
			local var_10_8 = var_10_6.addDayExp
			local var_10_9 = var_10_6.isUpLevel
			local var_10_10 = var_10_6.isMaxLevel
			local var_10_11 = var_10_6.isExpMax
			local var_10_12 = var_10_6.progressOld
			local var_10_13 = var_10_6.progressNew
			local var_10_14 = getProxy(BayProxy).getShipById(var_10_7)
			local var_10_15 = var_10_14.getPainting()
			local var_10_16 = "SquareIcon/" .. var_10_15

			setImageSprite(var_10_0, LoadSprite(var_10_16, var_10_15))
			setText(var_10_1, "EXP + " .. var_10_8)
			setActive(var_10_5, var_10_9 and var_10_10)

			if var_10_9 and var_10_10:
				setActive(var_10_1, False)
				setActive(var_10_2, True)
				setActive(var_10_3, False)
			elif var_10_11:
				setActive(var_10_1, False)
				setActive(var_10_2, False)
				setActive(var_10_3, True)
			else
				setActive(var_10_1, True)
				setActive(var_10_2, False)
				setActive(var_10_3, False)

			setSlider(var_10_4, 0, 1, var_10_13)
			onButton(arg_9_0, arg_10_2, function()
				LoadContextCommand.LoadLayerOnTopContext(Context.New({
					viewComponent = MetaSkillDetailBoxLayer,
					mediator = MetaSkillDetailBoxMediator,
					data = {
						metaShipID = var_10_14.id,
						expInfoList = arg_9_0.lastMetaExpInfoList
					},
					def onRemoved:()
						arg_9_0.updateIconList()
				})), SFX_PANEL))
	arg_9_0.iconUIItemList.align(#var_9_1)

def var_0_0.openPanel(arg_13_0):
	if arg_13_0.isAni == True:
		return

	arg_13_0.isAni = True

	Canvas.ForceUpdateCanvases()

	local var_13_0 = arg_13_0.panelTF.sizeDelta.x

	LeanTween.value(go(arg_13_0.panelTF), 0, var_13_0, 0.5).setOnUpdate(System.Action_float(function(arg_14_0)
		setAnchoredPosition(arg_13_0.panelTF, {
			x = -arg_14_0
		}))).setOnComplete(System.Action(function()
		arg_13_0.isAni = False))

def var_0_0.closePanel(arg_16_0):
	if arg_16_0.isAni == True:
		return

	arg_16_0.isAni = True

	local var_16_0 = arg_16_0.panelTF.sizeDelta.x

	LeanTween.value(go(arg_16_0.panelTF), -var_16_0, 0, 0.5).setOnUpdate(System.Action_float(function(arg_17_0)
		setAnchoredPosition(arg_16_0.panelTF, {
			x = arg_17_0
		}))).setOnComplete(System.Action(function()
		arg_16_0.isAni = False

		arg_16_0.Destroy()))

def var_0_0.sortDataList(arg_19_0, arg_19_1):
	table.sort(arg_19_1, function(arg_20_0, arg_20_1)
		local var_20_0 = arg_20_0.isUpLevel and arg_20_0.isMaxLevel and 9999 or 0
		local var_20_1 = arg_20_1.isUpLevel and arg_20_1.isMaxLevel and 9999 or 0
		local var_20_2 = arg_20_0.progressNew
		local var_20_3 = arg_20_1.progressNew
		local var_20_4 = var_20_0 + var_20_2
		local var_20_5 = var_20_1 + var_20_3

		if var_20_5 < var_20_4:
			return True
		elif var_20_4 == var_20_5:
			return arg_20_0.shipID < arg_20_1.shipID
		elif var_20_4 < var_20_5:
			return False)

	return arg_19_1

return var_0_0
