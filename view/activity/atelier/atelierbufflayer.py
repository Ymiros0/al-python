local var_0_0 = class("AtelierBuffLayer", import("view.base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "AtelierBuffUI"

def var_0_0.SetActivity(arg_2_0, arg_2_1):
	arg_2_0.activity = arg_2_1

	local var_2_0 = arg_2_1.GetItems()

	arg_2_0.buffItems = _.map(_.filter(AtelierMaterial.bindConfigTable().all, function(arg_3_0)
		return AtelierMaterial.bindConfigTable()[arg_3_0].type == AtelierMaterial.TYPE.STRENGTHEN), function(arg_4_0)
		return var_2_0[arg_4_0] or AtelierMaterial.New({
			configId = arg_4_0
		}))

def var_0_0.init(arg_5_0):
	arg_5_0.slotTfs = _.map({
		1,
		2,
		3,
		4,
		5
	}, function(arg_6_0)
		return arg_5_0._tf.Find("Panel").GetChild(arg_6_0))
	arg_5_0.effectList = arg_5_0._tf.Find("Effects/ScrollView/Viewport/Content")

	setText(arg_5_0._tf.Find("Items/List").GetChild(0).Find("Max/Text"), i18n("ryza_tip_control_buff_limit"))
	setText(arg_5_0._tf.Find("Items/List").GetChild(0).Find("Min/Text"), i18n("ryza_tip_control_buff_not_obtain"))

	arg_5_0.buffItemTFs = CustomIndexLayer.Clone2Full(arg_5_0._tf.Find("Items/List"), 8)

	setText(arg_5_0._tf.Find("Top/Tips"), i18n("ryza_tip_control"))
	setText(arg_5_0._tf.Find("Effects/Total"), i18n("ryza_tip_control_buff"))

	arg_5_0.loader = AutoLoader.New()

def var_0_0.didEnter(arg_7_0):
	onButton(arg_7_0, arg_7_0._tf.Find("Top/Back"), function()
		arg_7_0.onBackPressed(), SFX_CANCEL)
	onButton(arg_7_0, arg_7_0._tf.Find("Top/Home"), function()
		arg_7_0.quickExitFunc(), SFX_CANCEL)
	onButton(arg_7_0, arg_7_0._tf.Find("Top/Help"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.ryza_control_help_tip.tip
		}), SFX_PANEL)
	table.Foreach(arg_7_0.slotTfs, function(arg_11_0, arg_11_1)
		onButton(arg_7_0, arg_11_1, function()
			arg_7_0.contextData.selectIndex = arg_11_0

			arg_7_0.UpdateView(), SFX_PANEL))
	table.Foreach(arg_7_0.buffItemTFs, function(arg_13_0, arg_13_1)
		onButton(arg_7_0, arg_13_1, function()
			local var_14_0 = arg_7_0.buffItems[arg_13_0]

			if not arg_7_0.contextData.selectIndex:
				arg_7_0.emit(AtelierMaterialDetailMediator.SHOW_DETAIL, var_14_0)

				return

			local var_14_1 = arg_7_0.activity.GetSlots()
			local var_14_2 = var_14_1[arg_7_0.contextData.selectIndex]

			local function var_14_3(arg_15_0, arg_15_1)
				if arg_15_1 > var_14_0.count:
					pg.TipsMgr.GetInstance().ShowTips(i18n("ryza_tip_control_buff_not_obtain_tip"))

					return

				local var_15_0 = Clone(var_14_1)
				local var_15_1 = var_15_0[arg_7_0.contextData.selectIndex]

				var_15_1[1] = arg_15_0
				var_15_1[2] = arg_15_1

				arg_7_0.emit(GAME.UPDATE_ATELIER_BUFF, var_15_0)

			if var_14_2[1] == var_14_0.GetConfigID():
				if var_14_2[2] < #var_14_0.GetBuffs():
					var_14_3(var_14_2[1], var_14_2[2] + 1)

				return

			if _.detect(var_14_1, function(arg_16_0)
				return arg_16_0[1] == var_14_0.GetConfigID()):
				return

			var_14_3(var_14_0.GetConfigID(), 1), SFX_PANEL))
	arg_7_0.UpdateView()
	pg.UIMgr.GetInstance().OverlayPanel(arg_7_0._tf, {
		weight = LayerWeightConst.SECOND_LAYER
	})

	if PlayerPrefs.GetInt("first_enter_ryza_buff_" .. getProxy(PlayerProxy).getRawData().id, 0) == 0:
		triggerButton(arg_7_0._tf.Find("Top/Help"))
		PlayerPrefs.SetInt("first_enter_ryza_buff_" .. getProxy(PlayerProxy).getRawData().id, 1)

def var_0_0.UpdateView(arg_17_0):
	local var_17_0 = arg_17_0.activity.GetSlots()
	local var_17_1 = _.all(var_17_0, function(arg_18_0)
		return arg_18_0[1] > 0)

	setActive(arg_17_0._tf.Find("Panel/Full"), var_17_1)

	arg_17_0.slotFull = var_17_1

	table.Foreach(arg_17_0.slotTfs, function(arg_19_0, arg_19_1)
		arg_17_0.UpdateSlot(arg_19_1, arg_19_0))

	local var_17_2 = arg_17_0.contextData.selectIndex and var_17_0[arg_17_0.contextData.selectIndex]

	table.Foreach(arg_17_0.buffItems, function(arg_20_0, arg_20_1)
		local var_20_0 = arg_17_0.buffItemTFs[arg_20_0]
		local var_20_1 = arg_20_1.GetBuffs()
		local var_20_2 = _.detect(var_17_0, function(arg_21_0)
			return arg_21_0[1] == arg_20_1.GetConfigID())
		local var_20_3 = #var_20_1
		local var_20_4 = var_20_2 and var_20_3 <= var_20_2[2]
		local var_20_5 = arg_20_1.count == 0 or var_20_2 and var_20_3 > var_20_2[2] and var_20_2[2] == arg_20_1.count
		local var_20_6 = var_20_2 and table.indexof(var_17_0, var_20_2) == arg_17_0.contextData.selectIndex
		local var_20_7 = var_17_2 and not var_20_4 and var_20_2 and not var_20_6
		local var_20_8 = var_17_2 and not var_20_2 and not var_20_5
		local var_20_9 = not var_20_5 and var_17_2 and (var_20_8 and var_17_2[1] == 0 or var_20_6 and var_20_3 > var_20_2[2])
		local var_20_10 = var_20_8 or var_20_9

		setActive(var_20_0.Find("Min"), False)

		if var_20_5:
			setActive(var_20_0.Find("Min"), True)
			setText(var_20_0.Find("Min/Text"), i18n("ryza_tip_control_buff_not_obtain"))
		elif var_20_7:
			setActive(var_20_0.Find("Min"), True)
			setText(var_20_0.Find("Min/Text"), i18n("ryza_tip_control_buff_already_active_tip"))

		setActive(var_20_0.Find("Avaliable"), var_20_10)

		if var_20_9:
			setText(var_20_0.Find("Avaliable/Text"), i18n("ryza_tip_control_buff_upgrade"))
		elif var_20_8:
			setText(var_20_0.Find("Avaliable/Text"), i18n("ryza_tip_control_buff_replace"))

		setActive(var_20_0.Find("Max"), var_20_4)
		setScrollText(var_20_0.Find("Name/Text"), arg_20_1.GetName())

		local var_20_11 = arg_20_1.count

		if var_20_2:
			var_20_11 = var_20_11 - var_20_2[2]

		updateDrop(var_20_0.Find("Icon"), {
			type = DROP_TYPE_RYZA_DROP,
			id = arg_20_1.GetConfigID(),
			count = var_20_11
		}))

	local var_17_3 = _.map(var_17_0, function(arg_22_0)
		if arg_22_0[1] == 0 or arg_22_0[2] == 0:
			return

		local var_22_0 = arg_17_0.activity.GetItems()[arg_22_0[1]]

		assert(var_22_0)

		var_22_0 = var_22_0 or AtelierMaterial.New({
			configId = arg_22_0[1]
		})

		local var_22_1 = var_22_0.GetBuffs()

		if not var_22_1:
			return

		local var_22_2 = var_22_1[math.min(#var_22_1, arg_22_0[2])]
		local var_22_3 = CommonBuff.New({
			id = var_22_2
		})

		return "【" .. var_22_3.getConfig("name") .. "】." .. var_22_3.getConfig("desc"))
	local var_17_4 = CustomIndexLayer.Clone2Full(arg_17_0.effectList, #var_17_3)

	for iter_17_0, iter_17_1 in ipairs(var_17_4):
		setText(iter_17_1, var_17_3[iter_17_0])

def var_0_0.PlayFullEffect(arg_23_0):
	arg_23_0.LoadingOn()

def var_0_0.UpdateSlot(arg_24_0, arg_24_1, arg_24_2):
	local var_24_0 = arg_24_0.activity.GetSlots()[arg_24_2]
	local var_24_1 = var_24_0[1]
	local var_24_2 = var_24_0[2]
	local var_24_3 = arg_24_0.contextData.selectIndex == arg_24_2
	local var_24_4 = var_24_1 > 0 or var_24_3

	setActive(arg_24_1.Find("Avaliable"), var_24_4)
	setActive(arg_24_1.Find("Link"), var_24_4)
	setActive(arg_24_1.Find("LinkActive"), var_24_3)
	setActive(arg_24_1.Find("Diamond"), var_24_1 > 0)

	local var_24_5 = False

	if var_24_4:
		setActive(arg_24_1.Find("Avaliable/Selecting"), var_24_3)
		setActive(arg_24_1.Find("Avaliable/Item"), var_24_1 > 0)
		setActive(arg_24_1.Find("Avaliable/Item").GetChild(2), arg_24_0.slotFull)
		setActive(arg_24_1.Find("Avaliable/Image"), var_24_1 == 0)

		if var_24_1 > 0:
			local var_24_6 = AtelierMaterial.New({
				configId = var_24_1
			})

			var_24_5 = #var_24_6.GetBuffs() == var_24_2

			local var_24_7 = var_24_6.GetBuffs()[math.min(#var_24_6.GetBuffs(), var_24_2)]
			local var_24_8 = CommonBuff.New({
				id = var_24_7
			})

			arg_24_0.loader.GetSpriteQuiet(var_24_8.getConfig("icon"), "", arg_24_1.Find("Avaliable/Item/Image"))
			setText(arg_24_1.Find("Avaliable/Item/Name/Text"), var_24_8.getConfig("name"))

	setActive(arg_24_1.Find("Link/3"), var_24_5)
	setActive(arg_24_1.Find("Link/1"), not var_24_5 and var_24_2 > 0)

def var_0_0.OnUpdateAtelierBuff(arg_25_0):
	arg_25_0.UpdateView()
	arg_25_0.PlayLevelUpAnim()

def var_0_0.PlayLevelUpAnim(arg_26_0):
	arg_26_0.CleanTween()

	local var_26_0 = arg_26_0.slotTfs[arg_26_0.contextData.selectIndex]
	local var_26_1 = var_26_0.Find("Avaliable/LevelUp/Image")

	setActive(var_26_1.parent, True)

	local var_26_2 = var_26_1.anchoredPosition.y

	setImageAlpha(var_26_1, 0)

	arg_26_0.tweenId = LeanTween.value(go(var_26_0), 0, 2, 2).setOnUpdate(System.Action_float(function(arg_27_0)
		arg_27_0 = math.clamp(arg_27_0, 0, 1)

		setImageAlpha(var_26_1, arg_27_0)
		setAnchoredPosition(var_26_1, {
			y = var_26_2 + 20 * (arg_27_0 - 1)
		}))).setOnComplete(System.Action(function()
		setAnchoredPosition(var_26_1, {
			y = var_26_2
		})
		setActive(var_26_1.parent, False))).id

def var_0_0.CleanTween(arg_29_0):
	if not arg_29_0.tweenId:
		return

	LeanTween.cancel(arg_29_0.tweenId, True)

def var_0_0.LoadingOn(arg_30_0):
	if arg_30_0.animating:
		return

	arg_30_0.animating = True

	pg.UIMgr.GetInstance().LoadingOn(False)

def var_0_0.LoadingOff(arg_31_0):
	if not arg_31_0.animating:
		return

	pg.UIMgr.GetInstance().LoadingOff()

	arg_31_0.animating = False

def var_0_0.willExit(arg_32_0):
	arg_32_0.loader.Clear()
	arg_32_0.CleanTween()
	arg_32_0.LoadingOff()
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_32_0._tf)

return var_0_0
