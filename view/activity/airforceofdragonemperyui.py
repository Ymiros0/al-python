local var_0_0 = class("AirForceOfDragonEmperyUI", import("view.base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "AirForceOfDragonEmperyUI"

local var_0_1 = {
	"J-10",
	"J-15",
	"FC-1",
	"FC-31"
}
local var_0_2 = {
	"fighterplane_J10_tip",
	"fighterplane_J15_tip",
	"fighterplane_FC1_tip",
	"fighterplane_FC31_tip"
}

def var_0_0.init(arg_2_0):
	arg_2_0.itemList = {}

	for iter_2_0 = 0, arg_2_0._tf.Find("List").childCount - 1:
		local var_2_0 = arg_2_0._tf.Find("List").GetChild(iter_2_0)

		setImageAlpha(var_2_0.Find("Button"), 0.5)
		table.insert(arg_2_0.itemList, var_2_0)

	arg_2_0.currentNameImage = arg_2_0._tf.Find("FighterName")
	arg_2_0.currentFighterImage = arg_2_0._tf.Find("FighterImage")
	arg_2_0.currentFighterDesc = arg_2_0._tf.Find("FighterProgress")

	setImageAlpha(arg_2_0.currentNameImage, 0)
	setImageAlpha(arg_2_0.currentFighterImage, 0)

	arg_2_0.BattleTimes = arg_2_0._tf.Find("BattleTimes")

	local var_2_1 = arg_2_0._tf.GetComponent(typeof(ItemList)).prefabItem
	local var_2_2 = tf(Instantiate(var_2_1[0]))

	setParent(var_2_2, arg_2_0._tf)

	arg_2_0.loader = AutoLoader.New()

def var_0_0.SetActivityData(arg_3_0, arg_3_1):
	arg_3_0.activity = arg_3_1

def var_0_0.GetFighterData(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_0.activity.getKVPList(1, arg_4_1) or 0
	local var_4_1 = arg_4_0.activity.getKVPList(2, arg_4_1) == 1

	return var_4_0, var_4_1

def var_0_0.GetActivityProgress(arg_5_0):
	local var_5_0 = 0
	local var_5_1 = arg_5_0.activity.getConfig("config_client")[1]

	for iter_5_0 = 1, var_5_1:
		var_5_0 = var_5_0 + arg_5_0.GetFighterData(iter_5_0)

	local var_5_2 = pg.TimeMgr.GetInstance()
	local var_5_3 = var_5_2.DiffDay(arg_5_0.activity.data1, var_5_2.GetServerTime()) + 1
	local var_5_4 = math.min(var_5_3 * 2, var_5_1 * 3)

	return var_5_0, var_5_4

def var_0_0.didEnter(arg_6_0):
	onButton(arg_6_0, arg_6_0._tf.Find("Back"), function()
		arg_6_0.closeView(), SOUND_BACK)
	onButton(arg_6_0, arg_6_0._tf.Find("Help"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.fighterplane_help.tip,
			weight = LayerWeightConst.SECOND_LAYER
		}), SFX_PANEL)
	onButton(arg_6_0, arg_6_0._tf.Find("Battle"), function()
		local var_9_0 = arg_6_0.contextData.index
		local var_9_1 = arg_6_0.GetFighterData(arg_6_0.contextData.index)

		local function var_9_2()
			local var_10_0 = arg_6_0.activity.getConfig("config_client")[1]
			local var_10_1 = arg_6_0.activity.getConfig("config_client")[2]
			local var_10_2 = math.floor(#var_10_1 / var_10_0)
			local var_10_3 = var_10_2 * (arg_6_0.contextData.index - 1) + 1
			local var_10_4 = math.min(var_10_3 + var_10_2 - 1, #var_10_1)
			local var_10_5 = var_10_1[math.random(var_10_3, var_10_4)]

			arg_6_0.emit(AirForceOfDragonEmperyMediator.ON_BATTLE, var_10_5)

		if var_9_1 >= 3:
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("fighterplane_complete_tip"),
				onYes = var_9_2,
				weight = LayerWeightConst.SECOND_LAYER
			})
		else
			var_9_2(), SFX_FIGHTER_BATTLE)

	for iter_6_0, iter_6_1 in ipairs(arg_6_0.itemList):
		onButton(arg_6_0, iter_6_1, function()
			arg_6_0.SwitchIndex(iter_6_0), SFX_FIGHTER_SWITCH)

	local var_6_0 = getProxy(PlayerProxy).getRawData()
	local var_6_1 = arg_6_0.contextData.index or PlayerPrefs.GetInt("AirFightIndex_" .. var_6_0.id, 1)

	arg_6_0.contextData.index = None

	arg_6_0.SwitchIndex(var_6_1)
	arg_6_0.UpdateView()

def var_0_0.willExit(arg_12_0):
	local var_12_0 = getProxy(PlayerProxy).getRawData()

	PlayerPrefs.SetInt("AirFightIndex_" .. var_12_0.id, arg_12_0.contextData.index)
	PlayerPrefs.Save()
	LeanTween.cancel(go(arg_12_0.currentNameImage))
	LeanTween.cancel(go(arg_12_0.currentFighterImage))
	LeanTween.cancel(go(arg_12_0.currentFighterDesc.Find("Desc/Text")))
	LeanTween.cancel(go(arg_12_0.currentFighterDesc.Find("Progress")))
	arg_12_0.loader.Clear()

def var_0_0.UpdateView(arg_13_0):
	for iter_13_0, iter_13_1 in ipairs(arg_13_0.itemList):
		local var_13_0, var_13_1 = arg_13_0.GetFighterData(iter_13_0)
		local var_13_2 = arg_13_0.itemList[iter_13_0]

		UIItemList.StaticAlign(var_13_2.Find("Progress"), var_13_2.Find("Progress").GetChild(0), var_13_0)

	arg_13_0.UpdateFighter(arg_13_0.contextData.index)

	local var_13_3, var_13_4 = arg_13_0.GetActivityProgress()

	setText(arg_13_0.BattleTimes, var_13_4 - var_13_3)
	arg_13_0.CheckActivityUpdate()

def var_0_0.SwitchIndex(arg_14_0, arg_14_1):
	if arg_14_1 == None or arg_14_1 == arg_14_0.contextData.index:
		return

	if arg_14_0.contextData.index:
		local var_14_0 = arg_14_0.itemList[arg_14_0.contextData.index]

		setActive(var_14_0.Find("Selected"), False)
		setImageAlpha(var_14_0.Find("Button"), 0.5)

	arg_14_0.contextData.index = arg_14_1

	local var_14_1 = arg_14_0.itemList[arg_14_0.contextData.index]

	setActive(var_14_1.Find("Selected"), True)
	setImageAlpha(var_14_1.Find("Button"), 1)
	arg_14_0.UpdateFighter(arg_14_1)
	;(function()
		local var_15_0
		local var_15_1 = arg_14_0.currentFighterImage.GetComponent(typeof(Image))
		local var_15_2 = tf(arg_14_0.currentFighterImage)

		LeanTween.cancel(go(arg_14_0.currentFighterImage))

		local var_15_3
		local var_15_4 = arg_14_0.currentNameImage.GetComponent(typeof(Image))
		local var_15_5 = tf(arg_14_0.currentNameImage)

		LeanTween.cancel(go(arg_14_0.currentNameImage))
		parallelAsync({
			function(arg_16_0)
				local var_16_0 = var_15_1.color.a

				if var_16_0 < 0.05:
					arg_16_0()

					return

				LeanTween.alpha(var_15_2, 0, var_16_0 * 0.2).setOnComplete(System.Action(arg_16_0)),
			function(arg_17_0)
				local var_17_0 = var_15_4.color.a

				if var_17_0 < 0.05:
					arg_17_0()

					return

				LeanTween.alpha(var_15_5, 0, var_17_0 * 0.2).setOnComplete(System.Action(arg_17_0)),
			function(arg_18_0)
				arg_14_0.loader.GetSpriteDirect("ui/AirForceOfDragonEmperyUI_atlas", var_0_1[arg_14_1], function(arg_19_0)
					var_15_0 = arg_19_0

					arg_18_0(), arg_14_0.currentFighterImage),
			function(arg_20_0)
				arg_14_0.loader.GetSpriteDirect("ui/AirForceOfDragonEmperyUI_atlas", var_0_1[arg_14_1] .. "_BG", function(arg_21_0)
					var_15_3 = arg_21_0

					arg_20_0(), arg_14_0.currentNameImage)
		}, function()
			var_15_1.enabled = True
			var_15_1.sprite = var_15_0

			LeanTween.alpha(var_15_2, 1, 0.2)

			var_15_4.enabled = True
			var_15_4.sprite = var_15_3

			LeanTween.alpha(var_15_5, 1, 0.2)))()
	;(function()
		local var_23_0 = arg_14_0.currentFighterDesc.Find("Desc/Text")

		LeanTween.cancel(var_23_0)
		var_23_0.GetComponent("ScrollText").SetText(i18n(var_0_2[arg_14_1]))
		LeanTween.textAlpha(var_23_0, 1, 0.5).setFrom(0))()

	local var_14_2, var_14_3 = arg_14_0.GetFighterData(arg_14_1)
	local var_14_4 = arg_14_0.currentFighterDesc.Find("Progress")

	UIItemList.StaticAlign(var_14_4, var_14_4.GetChild(0), 3, function(arg_24_0, arg_24_1, arg_24_2)
		if not arg_24_0 == UIItemList.EventUpdate:
			return

		setActive(arg_24_2.GetChild(0), arg_24_1 + 1 <= var_14_2)

		arg_24_2.GetChild(0).localScale = Vector3(0, 1, 1))
	LeanTween.cancel(go(var_14_4))
	LeanTween.value(go(var_14_4), 0, 1, 0.6000000000000001).setOnUpdate(System.Action_float(function(arg_25_0)
		for iter_25_0 = 0, 2:
			local var_25_0 = var_14_4.GetChild(iter_25_0)
			local var_25_1 = math.clamp(3 * arg_25_0 - iter_25_0, 0, 1)

			var_25_0.GetChild(0).localScale = Vector3(var_25_1, 1, 1)))
	arg_14_0.loader.GetSprite("ui/AirForceOfDragonEmperyUI_atlas", var_0_1[arg_14_1] .. "_Text", arg_14_0.currentFighterDesc.Find("Name"), True)

def var_0_0.UpdateFighter(arg_26_0, arg_26_1):
	local var_26_0, var_26_1 = arg_26_0.GetFighterData(arg_26_1)
	local var_26_2 = arg_26_0.itemList[arg_26_1]

	UIItemList.StaticAlign(var_26_2.Find("Progress"), var_26_2.Find("Progress").GetChild(0), var_26_0)

	local var_26_3 = arg_26_0.currentFighterDesc
	local var_26_4 = arg_26_0.activity.getConfig("config_client")[3][arg_26_1]
	local var_26_5 = {
		type = var_26_4[1],
		id = var_26_4[2],
		count = var_26_4[3]
	}

	updateDrop(var_26_3.Find("Item"), var_26_5)
	setActive(var_26_3.Find("ItemMask"), var_26_1)
	onButton(arg_26_0, var_26_3.Find("Item"), function()
		arg_26_0.emit(BaseUI.ON_DROP, var_26_5), SFX_PANEL)

def var_0_0.CheckActivityUpdate(arg_28_0):
	local var_28_0 = arg_28_0.activity.getConfig("config_client")[1]

	for iter_28_0 = 1, var_28_0:
		local var_28_1, var_28_2 = arg_28_0.GetFighterData(iter_28_0)

		if var_28_1 >= 3 and not var_28_2:
			arg_28_0.emit(AirForceOfDragonEmperyMediator.ON_ACTIVITY_OPREATION, {
				cmd = 2,
				activity_id = arg_28_0.activity.id,
				arg1 = iter_28_0
			})

			return

return var_0_0
