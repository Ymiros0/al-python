local var_0_0 = class("AnniversaryIslandBuildingUpgrade2023Window", import("view.base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "AnniversaryIslandBuildingUpgrade2023Window"

def var_0_0.GetAtlasPath(arg_2_0):
	return "ui/" .. arg_2_0.getUIName() .. "_atlas"

def var_0_0.init(arg_3_0):
	arg_3_0.window = arg_3_0._tf.Find("Window")
	arg_3_0.upgradeWindow = arg_3_0.window.Find("Upgrade")
	arg_3_0.displayWindow = arg_3_0.window.Find("Display")

	setText(arg_3_0.window.Find("Upgrade/MaterialsTitle"), i18n("workbench_need_materials"))
	setText(arg_3_0.window.Find("Display/MaxTip"), i18n("workbench_tips6"))

	arg_3_0.loader = AutoLoader.New()

def var_0_0.didEnter(arg_4_0):
	local var_4_0 = arg_4_0.contextData.buildingID

	onButton(arg_4_0, arg_4_0._tf.Find("BG"), function()
		arg_4_0.onBackPressed())
	onButton(arg_4_0, arg_4_0.upgradeWindow.Find("Cancel"), function()
		arg_4_0.onBackPressed(), SFX_CANCEL)
	onButton(arg_4_0, arg_4_0.upgradeWindow.Find("Upgrade"), function()
		if arg_4_0.isMaxLevel:
			return
		elif arg_4_0.isOverAvg:
			pg.TipsMgr.GetInstance().ShowTips(i18n("haidaojudian_upgrade_limit"))
		elif arg_4_0.isLackMat:
			pg.TipsMgr.GetInstance().ShowTips(i18n("haidaojudian_building_tip"))
		else
			arg_4_0.emit(BuildingUpgradeMediator.ACTIVITY_OPERATION, {
				cmd = 1,
				activity_id = arg_4_0.activityId,
				arg1 = var_4_0
			}))
	onButton(arg_4_0, arg_4_0.displayWindow.Find("Confirm"), function()
		arg_4_0.onBackPressed(), SFX_PANEL)
	arg_4_0.UpdateView()

def var_0_0.UpdateView(arg_9_0):
	local var_9_0 = arg_9_0.contextData.buildingID
	local var_9_1 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF_2)

	arg_9_0.activityId = var_9_1.id

	local var_9_2 = var_9_1.GetBuildingLevel(var_9_0)
	local var_9_3 = pg.activity_event_building[var_9_0]
	local var_9_4 = #var_9_3.buff

	arg_9_0.isMaxLevel = var_9_4 <= var_9_2
	arg_9_0.isOverAvg = var_9_2 > var_9_1.GetTotalBuildingLevel()

	setActive(arg_9_0.upgradeWindow, not arg_9_0.isMaxLevel)
	setActive(arg_9_0.displayWindow, arg_9_0.isMaxLevel)

	local var_9_5 = arg_9_0.isMaxLevel and arg_9_0.displayWindow or arg_9_0.upgradeWindow
	local var_9_6 = AnniversaryIsland2023Scene.Buildings[var_9_0]

	arg_9_0.loader.GetSpriteQuiet(arg_9_0.GetAtlasPath(), var_9_6, var_9_5.Find("Title/BuildingName"), True)

	local var_9_7 = 0

	;(function()
		arg_9_0.loader.GetSpriteQuiet(arg_9_0.GetAtlasPath(), var_9_2, var_9_5.Find("Title/LevelBefore"), True)

		local var_10_0 = var_9_3.buff[var_9_2]
		local var_10_1 = CommonBuff.New({
			id = var_10_0
		})
		local var_10_2 = string.split(var_10_1.getConfig("desc"), "/")

		assert(var_10_2)

		local var_10_3, var_10_4, var_10_5 = string.find(var_10_2[1], "([^%+]*)%+")
		local var_10_6 = string.sub(var_10_2[1], var_10_4, #var_10_2[1])
		local var_10_7, var_10_8, var_10_9 = string.find(var_10_2[2], "([^%+]*)%+")
		local var_10_10 = string.sub(var_10_2[2], var_10_8, #var_10_2[2])

		setText(var_9_5.Find("Progress1/1/Desc"), var_10_5)
		setText(var_9_5.Find("Progress1/1/Value"), var_10_6)
		setText(var_9_5.Find("Progress2/1/Desc"), var_10_9)
		setText(var_9_5.Find("Progress2/1/Value"), var_10_10)

		var_9_7 = tonumber(var_10_1.getConfig("benefit_effect")))()
	;(function()
		if var_9_2 >= var_9_4:
			return

		local var_11_0 = var_9_2 + 1

		arg_9_0.loader.GetSpriteQuiet(arg_9_0.GetAtlasPath(), var_11_0, var_9_5.Find("Title/LevelAfter"), True)

		local var_11_1 = var_9_3.buff[var_11_0]
		local var_11_2 = CommonBuff.New({
			id = var_11_1
		})
		local var_11_3 = string.split(var_11_2.getConfig("desc"), "/")

		assert(var_11_3)

		local var_11_4, var_11_5, var_11_6 = string.find(var_11_3[1], "([^%+]*)%+")
		local var_11_7 = string.sub(var_11_3[1], var_11_5, #var_11_3[1])
		local var_11_8, var_11_9, var_11_10 = string.find(var_11_3[2], "([^%+]*)%+")
		local var_11_11 = string.sub(var_11_3[2], var_11_9, #var_11_3[2])

		setText(var_9_5.Find("Progress1/2/Desc"), var_11_6)
		setText(var_9_5.Find("Progress1/2/Value"), var_11_7)
		setText(var_9_5.Find("Progress2/2/Desc"), var_11_10)
		setText(var_9_5.Find("Progress2/2/Value"), var_11_11)

		local var_11_12 = tonumber(var_11_2.getConfig("benefit_effect")) > var_9_7

		setActive(var_9_5.Find("Progress2/2/Up"), var_11_12))()
	;(function()
		if var_9_2 >= var_9_4:
			return

		local var_12_0 = var_9_3.material[var_9_2]
		local var_12_1 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_VIRTUAL_BAG)

		arg_9_0.isLackMat = False

		UIItemList.StaticAlign(var_9_5.Find("Materials"), var_9_5.Find("Materials").GetChild(0), #var_12_0, function(arg_13_0, arg_13_1, arg_13_2)
			if arg_13_0 != UIItemList.EventUpdate:
				return

			local var_13_0 = var_12_0[arg_13_1 + 1]
			local var_13_1 = {
				type = var_13_0[1],
				id = var_13_0[2],
				count = var_13_0[3]
			}

			arg_9_0.UpdateActivityDrop(arg_13_2.Find("Icon"), var_13_1)
			onButton(arg_9_0, arg_13_2.Find("Icon"), function()
				if var_13_1.type == DROP_TYPE_WORKBENCH_DROP:
					arg_9_0.emit(WorkBenchItemDetailMediator.SHOW_DETAIL, WorkBenchItem.New({
						configId = var_13_1.id,
						count = var_13_1.count
					}))
				else
					arg_9_0.emit(BaseUI.ON_DROP, var_13_1))

			local var_13_2 = var_13_0[2]
			local var_13_3 = var_13_0[3]
			local var_13_4 = var_12_1.getVitemNumber(var_13_2)
			local var_13_5 = var_13_4 < var_13_3

			setText(arg_13_2.Find("Text"), setColorStr(var_13_4, var_13_5 and "#bb6754" or "#6b5a48") .. "/" .. var_13_3)

			arg_9_0.isLackMat = arg_9_0.isLackMat or var_13_5))()

local var_0_1 = "ui/AtelierCommonUI_atlas"

def var_0_0.UpdateActivityDrop(arg_15_0, arg_15_1, arg_15_2, arg_15_3):
	updateDrop(arg_15_1, arg_15_2)
	SetCompomentEnabled(arg_15_1.Find("icon_bg"), typeof(Image), False)
	setActive(arg_15_1.Find("bg"), False)
	setActive(arg_15_1.Find("icon_bg/frame"), False)
	setActive(arg_15_1.Find("icon_bg/stars"), False)

	local var_15_0 = arg_15_2.getConfig("rarity")

	if arg_15_2.type == DROP_TYPE_EQUIP or arg_15_2.type == DROP_TYPE_EQUIPMENT_SKIN:
		var_15_0 = var_15_0 - 1

	local var_15_1 = "icon_frame_" .. var_15_0

	if arg_15_3:
		var_15_1 = var_15_1 .. "_small"

	arg_15_0.loader.GetSpriteQuiet(var_0_1, var_15_1, arg_15_1)

def var_0_0.willExit(arg_16_0):
	arg_16_0.loader.Clear()

return var_0_0
