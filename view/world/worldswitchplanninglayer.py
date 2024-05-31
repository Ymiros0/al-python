local var_0_0 = class("WorldSwitchPlanningLayer", import("view.base.BaseUI"))

var_0_0.MODE_DIFFICULT = 0
var_0_0.MODE_SAFE = 1
var_0_0.MODE_TREASURE = 2
var_0_0.modeToggleDic = {
	[0] = {
		base = True,
		wait_2 = True,
		wait = True,
		boss = True,
		consume = True
	},
	{
		safe = True,
		wait_2 = True,
		wait = True,
		boss = True,
		consume = True
	},
	{
		wait = True,
		boss = True,
		treasure = True,
		consume = True
	}
}

def var_0_0.getUIName(arg_1_0):
	return "WorldSwitchPlanningUI"

def var_0_0.init(arg_2_0):
	pg.UIMgr.GetInstance().BlurPanel(arg_2_0._tf)

	arg_2_0.rtBg = arg_2_0._tf.Find("bg")

	onButton(arg_2_0, arg_2_0.rtBg, function()
		arg_2_0.closeView(), SFX_CANCEL)

	arg_2_0.rtWindow = arg_2_0._tf.Find("window")
	arg_2_0.btnBack = arg_2_0.rtWindow.Find("top/btnBack")

	onButton(arg_2_0, arg_2_0.btnBack, function()
		arg_2_0.closeView(), SFX_CANCEL)

	arg_2_0.btnCancel = arg_2_0.rtWindow.Find("button_container/custom_button_2")

	setText(arg_2_0.btnCancel.Find("pic"), i18n("text_cancel"))
	onButton(arg_2_0, arg_2_0.btnCancel, function()
		arg_2_0.closeView(), SFX_CANCEL)

	arg_2_0.btnConfirm = arg_2_0.rtWindow.Find("button_container/custom_button_1")

	setText(arg_2_0.btnConfirm.Find("pic"), i18n("text_confirm"))
	onButton(arg_2_0, arg_2_0.btnConfirm, function()
		arg_2_0.emit(WorldSwitchPlanningMediator.OnConfirm)
		arg_2_0.closeView(), SFX_CONFIRM)

	arg_2_0.btnMove = arg_2_0.rtWindow.Find("button_container/custom_button_3")

	setText(arg_2_0.btnMove.Find("pic"), i18n("text_goto"))
	onButton(arg_2_0, arg_2_0.btnMove, function()
		local var_7_0 = nowWorld()

		if var_7_0.GetInventoryProxy().GetItemCount(WorldConst.SwitchPlainingItemId) > 0:
			arg_2_0.emit(WorldSwitchPlanningMediator.OnMove, {
				inMap = True,
				context = Context.New({
					mediator = WorldInventoryMediator,
					viewComponent = WorldInventoryLayer
				})
			})
		elif not var_7_0.IsSystemOpen(WorldConst.SystemResetShop):
			pg.TipsMgr.GetInstance().ShowTips(i18n("world_automode_treasure_3"))
		else
			arg_2_0.emit(WorldSwitchPlanningMediator.OnMove, {
				inMap = False,
				context = Context.New({
					mediator = WorldShopMediator,
					viewComponent = WorldShopLayer
				})
			})

		arg_2_0.closeView(), SFX_CONFIRM)

	arg_2_0.rtContent = arg_2_0.rtWindow.Find("content")

	onToggle(arg_2_0, arg_2_0.rtContent.Find("toggles/toggle_base"), function(arg_8_0)
		if arg_8_0:
			arg_2_0.updateView(var_0_0.MODE_DIFFICULT)
			scrollTo(arg_2_0.rtView.Find("content"), None, 1), SFX_PANEL)
	onToggle(arg_2_0, arg_2_0.rtContent.Find("toggles/toggle_safe"), function(arg_9_0)
		if arg_9_0:
			arg_2_0.updateView(var_0_0.MODE_SAFE)
			scrollTo(arg_2_0.rtView.Find("content"), None, 1), SFX_PANEL)
	onToggle(arg_2_0, arg_2_0.rtContent.Find("toggles/toggle_treasure"), function(arg_10_0)
		if arg_10_0:
			arg_2_0.updateView(var_0_0.MODE_TREASURE)
			scrollTo(arg_2_0.rtView.Find("content"), None, 1), SFX_PANEL)

	arg_2_0.rtView = arg_2_0.rtContent.Find("view")

	for iter_2_0, iter_2_1 in ipairs({
		"base",
		"treasure"
	}):
		local var_2_0 = arg_2_0.rtView.Find("content/" .. iter_2_1 .. "/toggles")
		local var_2_1 = var_2_0.Find("all")
		local var_2_2 = {}
		local var_2_3 = 0
		local var_2_4 = var_2_0.childCount

		eachChild(var_2_0, function(arg_11_0)
			onToggle(arg_2_0, arg_11_0, function(arg_12_0)
				local var_12_0 = (arg_12_0 and 1 or 0) - defaultValue(var_2_2[arg_11_0.name], 0)

				var_2_2[arg_11_0.name] = arg_12_0 and 1 or 0
				var_2_3 = var_2_3 + var_12_0

				local var_12_1 = True

				if arg_11_0 == var_2_1 and arg_12_0:
					eachChild(var_2_0, function(arg_13_0)
						if arg_13_0 != arg_11_0 and GetComponent(arg_13_0, typeof(Toggle)).isOn == True:
							triggerToggle(arg_13_0, False)

							var_12_1 = False)
				elif var_2_3 == 0 or var_2_3 >= var_2_4 - 1:
					triggerToggle(var_2_1, True)

					var_12_1 = False
				elif var_2_3 > 1 and GetComponent(var_2_1, typeof(Toggle)).isOn == True:
					triggerToggle(var_2_1, False)

					var_12_1 = False

				if var_12_1:
					arg_2_0.saveConfig(iter_2_1), SFX_PANEL))

	local var_2_5 = pg.gameset.joint_boss_ticket.description
	local var_2_6 = var_2_5[1] + var_2_5[2]
	local var_2_7 = var_2_5[1] .. "&" .. var_2_6
	local var_2_8 = {}

	table.insert(var_2_8, "")
	table.insert(var_2_8, var_2_7)
	table.insert(var_2_8, tostring(var_2_6))

	arg_2_0.togglesList = {
		safe = {
			def getFlag:()
				return PlayerPrefs.GetString("auto_switch_difficult_safe", "all"),
			def setFlag:(arg_15_0)
				PlayerPrefs.SetString("auto_switch_difficult_safe", arg_15_0)
				PlayerPrefs.Save(),
			info = {
				all = "all",
				only = "only"
			}
		},
		wait = {
			def getFlag:()
				return PlayerPrefs.GetInt("auto_switch_wait", 0),
			def setFlag:(arg_17_0)
				PlayerPrefs.SetInt("auto_switch_wait", arg_17_0)
				PlayerPrefs.Save(),
			info = {
				yes = 1,
				no = 0
			}
		},
		wait_2 = {
			def getFlag:()
				return PlayerPrefs.GetInt("auto_switch_wait_2", 0),
			def setFlag:(arg_19_0)
				PlayerPrefs.SetInt("auto_switch_wait_2", arg_19_0)
				PlayerPrefs.Save(),
			info = {
				yes = 1,
				no = 0
			}
		},
		boss = {
			def getFlag:()
				return getProxy(SettingsProxy).GetWorldBossProgressTipFlag(),
			def setFlag:(arg_21_0)
				getProxy(SettingsProxy).WorldBossProgressTipFlag(arg_21_0),
			info = {
				no = var_2_8[1],
				["100"] = var_2_8[2],
				["200"] = var_2_8[3]
			}
		},
		consume = {
			def getFlag:()
				return getProxy(SettingsProxy).GetWorldFlag("consume_item"),
			def setFlag:(arg_23_0)
				getProxy(SettingsProxy).SetWorldFlag("consume_item", arg_23_0),
			info = {
				yes = True,
				no = False
			}
		}
	}

	for iter_2_2, iter_2_3 in pairs(arg_2_0.togglesList):
		local var_2_9 = arg_2_0.rtView.Find("content/" .. iter_2_2 .. "/toggles")

		for iter_2_4, iter_2_5 in pairs(iter_2_3.info):
			onToggle(arg_2_0, var_2_9.Find(iter_2_4), function(arg_24_0)
				if arg_24_0:
					iter_2_3.setFlag(iter_2_5), SFX_PANEL)

	local var_2_10 = {
		base = {
			text = "world_automode_setting_1",
			info = {
				["5"] = "world_automode_setting_1_2",
				until_4 = "world_automode_setting_1_1",
				["6"] = "world_automode_setting_1_3",
				all = "world_automode_setting_1_4"
			}
		},
		safe = {
			text = "world_automode_setting_2",
			info = {
				all = "world_automode_setting_2_2",
				only = "world_automode_setting_2_1"
			}
		},
		treasure = {
			text = "world_automode_setting_new_1",
			info = {
				all = "world_automode_setting_new_1_5",
				["6"] = "world_automode_setting_new_1_4",
				["5"] = "world_automode_setting_new_1_3",
				until_3 = "world_automode_setting_new_1_1",
				["4"] = "world_automode_setting_new_1_2"
			}
		},
		wait = {
			text = "world_automode_setting_all_1",
			info = {
				yes = "world_automode_setting_all_1_1",
				no = "world_automode_setting_all_1_2"
			}
		},
		wait_2 = {
			text = "world_automode_setting_all_4",
			info = {
				yes = "world_automode_setting_all_4_1",
				no = "world_automode_setting_all_4_2"
			}
		},
		boss = {
			text = "world_automode_setting_all_2",
			info = {
				["200"] = "world_automode_setting_all_2_3",
				["100"] = "world_automode_setting_all_2_2",
				no = "world_automode_setting_all_2_1"
			}
		},
		consume = {
			text = "world_automode_setting_all_3",
			info = {
				yes = "world_automode_setting_all_3_2",
				no = "world_automode_setting_all_3_1"
			}
		}
	}

	for iter_2_6, iter_2_7 in pairs(var_2_10):
		local var_2_11 = arg_2_0.rtView.Find("content/" .. iter_2_6)

		setText(var_2_11.Find("Text"), i18n(iter_2_7.text))

		for iter_2_8, iter_2_9 in pairs(iter_2_7.info):
			setText(var_2_11.Find("toggles/" .. iter_2_8 .. "/Text"), i18n(iter_2_9))

	setText(arg_2_0.rtWindow.Find("top/bg/title"), i18n("world_automode_title_1"))
	setText(arg_2_0.rtWindow.Find("top/bg/title/title_en"), i18n("world_automode_title_2"))
	setText(arg_2_0.rtContent.Find("toggles/toggle_base/Text"), i18n("area_putong"))
	setText(arg_2_0.rtContent.Find("toggles/toggle_safe/Text"), i18n("area_anquan"))
	setText(arg_2_0.rtContent.Find("toggles/toggle_treasure/Text"), i18n("area_yinmi"))

def var_0_0.didEnter(arg_25_0):
	triggerToggle(arg_25_0.rtContent.Find("toggles").GetChild(PlayerPrefs.GetInt("auto_switch_mode", 0)), True)

def var_0_0.willExit(arg_26_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_26_0._tf)

def var_0_0.initToggle(arg_27_0, arg_27_1):
	local var_27_0 = arg_27_0.togglesList[arg_27_1]
	local var_27_1 = var_27_0.getFlag()

	for iter_27_0, iter_27_1 in pairs(var_27_0.info):
		if iter_27_1 == var_27_1:
			triggerToggle(arg_27_0.rtView.Find("content/" .. arg_27_1 .. "/toggles/" .. iter_27_0), True)

			break

def var_0_0.updateView(arg_28_0, arg_28_1):
	PlayerPrefs.SetInt("auto_switch_mode", arg_28_1)
	PlayerPrefs.Save()

	local var_28_0 = nowWorld()
	local var_28_1 = arg_28_1 == var_0_0.MODE_TREASURE and not var_28_0.GetGobalFlag("treasure_flag")

	setActive(arg_28_0.rtView.Find("content"), not var_28_1)
	setActive(arg_28_0.rtContent.Find("scrollbar"), not var_28_1)
	setActive(arg_28_0.rtView.Find("tip"), var_28_1)
	setActive(arg_28_0.btnConfirm, not var_28_1)
	setActive(arg_28_0.btnMove, var_28_1)

	if var_28_1:
		if var_28_0.GetInventoryProxy().GetItemCount(WorldConst.SwitchPlainingItemId) > 0:
			setText(arg_28_0.rtView.Find("tip/Text"), i18n("world_automode_treasure_2"))
		else
			setText(arg_28_0.rtView.Find("tip/Text"), i18n("world_automode_treasure_1"))

	eachChild(arg_28_0.rtView.Find("content"), function(arg_29_0)
		setActive(arg_29_0, var_0_0.modeToggleDic[arg_28_1][arg_29_0.name])

		if var_0_0.modeToggleDic[arg_28_1]:
			switch(arg_29_0.name, {
				def base:()
					local var_30_0 = {}

					for iter_30_0, iter_30_1 in ipairs(var_0_0.paresingToggleString(PlayerPrefs.GetString("auto_switch_difficult_base", "all"))):
						var_30_0[iter_30_1] = True

					eachChild(arg_28_0.rtView.Find("content/base/toggles"), function(arg_31_0)
						triggerToggle(arg_31_0, var_30_0[arg_31_0.name])),
				def treasure:()
					local var_32_0 = {}

					for iter_32_0, iter_32_1 in ipairs(var_0_0.paresingToggleString(PlayerPrefs.GetString("auto_switch_difficult_treasure", "all"))):
						var_32_0[iter_32_1] = True

					eachChild(arg_28_0.rtView.Find("content/treasure/toggles"), function(arg_33_0)
						triggerToggle(arg_33_0, var_32_0[arg_33_0.name]))
			}, function()
				arg_28_0.initToggle(arg_29_0.name)))

def var_0_0.saveConfig(arg_35_0, arg_35_1):
	local var_35_0 = {}

	eachChild(arg_35_0.rtView.Find("content/" .. arg_35_1 .. "/toggles"), function(arg_36_0)
		if GetComponent(arg_36_0, typeof(Toggle)).isOn:
			table.insert(var_35_0, arg_36_0.name))
	PlayerPrefs.SetString("auto_switch_difficult_" .. arg_35_1, table.concat(var_35_0, "&"))
	PlayerPrefs.Save()

def var_0_0.paresingToggleString(arg_37_0):
	if not arg_37_0 or arg_37_0 == "":
		return {}

	return string.split(arg_37_0, "&")

def var_0_0.checkDifficultValid(arg_38_0, arg_38_1):
	local var_38_0 = var_0_0.paresingToggleString(arg_38_0)

	for iter_38_0, iter_38_1 in ipairs(var_38_0):
		if iter_38_1 == "all":
			return True
		elif string.sub(iter_38_1, 1, 6) == "until_":
			if arg_38_1 <= tonumber(string.sub(iter_38_1, 7)):
				return True
		elif arg_38_1 == tonumber(iter_38_1):
			return True

	return False

return var_0_0
