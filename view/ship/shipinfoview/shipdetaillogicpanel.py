local var_0_0 = class("ShipDetailLogicPanel", import("...base.BasePanel"))
local var_0_1 = {
	durability = AttributeType.Durability,
	armor = AttributeType.Armor,
	reload = AttributeType.Reload,
	cannon = AttributeType.Cannon,
	torpedo = AttributeType.Torpedo,
	motion = AttributeType.Dodge,
	antiaircraft = AttributeType.AntiAircraft,
	air = AttributeType.Air,
	hit = AttributeType.Hit,
	antisub = AttributeType.AntiSub,
	oxy_max = AttributeType.OxyMax,
	ammo = AttributeType.Ammo,
	hunting_range = AttributeType.HuntingRange,
	luck = AttributeType.Luck,
	consume = AttributeType.Expend,
	speed = AttributeType.Speed
}
local var_0_2 = {
	us = {
		prop_ignore = {
			luck = {
				134,
				-260,
				134,
				-260
			},
			consume = {
				417,
				-260,
				431,
				-260
			},
			hunting_range = {
				622,
				-260,
				639,
				-260
			}
		},
		sort_index = {
			"durability",
			"armor",
			"reload",
			"cannon",
			"torpedo",
			"motion",
			"antiaircraft",
			"air",
			"hit",
			"consume",
			"antisub",
			"oxy_max",
			"ammo",
			"speed",
			"hunting_range",
			"luck"
		},
		hide = {}
	},
	jp = {
		prop_ignore = {
			luck = {
				137,
				-260,
				151,
				-260
			},
			consume = {
				417,
				-260,
				431,
				-260
			},
			hunting_range = {
				622,
				-260,
				639,
				-260
			}
		},
		sort_index = {
			"durability",
			"armor",
			"reload",
			"cannon",
			"torpedo",
			"motion",
			"antiaircraft",
			"air",
			"hit",
			"consume",
			"antisub",
			"oxy_max",
			"ammo",
			"speed",
			"hunting_range",
			"luck"
		},
		hide = {}
	},
	kr = {
		prop_ignore = {
			luck = {
				137,
				-260,
				151,
				-260
			},
			consume = {
				417,
				-260,
				431,
				-260
			},
			hunting_range = {
				622,
				-260,
				639,
				-260
			}
		},
		sort_index = {
			"durability",
			"armor",
			"reload",
			"cannon",
			"torpedo",
			"motion",
			"antiaircraft",
			"air",
			"hit",
			"consume",
			"antisub",
			"oxy_max",
			"ammo",
			"speed",
			"hunting_range",
			"luck"
		},
		hide = {}
	},
	defaut = {
		prop_ignore = {
			luck = {
				137,
				-260,
				151,
				-260
			},
			consume = {
				417,
				-260,
				431,
				-260
			},
			hunting_range = {
				622,
				-260,
				639,
				-260
			}
		},
		sort_index = {
			"durability",
			"armor",
			"reload",
			"cannon",
			"torpedo",
			"motion",
			"antiaircraft",
			"air",
			"hit",
			"antisub",
			"oxy_max",
			"ammo",
			"speed",
			"hunting_range",
			"luck",
			"consume"
		},
		hide = {}
	}
}
local var_0_3
local var_0_4 = 0.5
local var_0_5 = Vector3(1, 1, 1)
local var_0_6 = Vector3(1.3, 1.3, 1.3)

var_0_0.EQUIPMENT_ADDITION = 0
var_0_0.TECHNOLOGY_ADDITION = 1
var_0_0.CORE_ADDITION = 2

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1.gameObject)

	arg_1_0.skillContainer = findTF(arg_1_0._tf, "skills/content")
	arg_1_0.skillContainerHz = arg_1_0.skillContainer.GetComponent(typeof(HorizontalLayoutGroup))
	arg_1_0.skillTpl = findTF(arg_1_0.skillContainer, "skill_tpl")
	arg_1_0.attrs = findTF(arg_1_0._tf, "attrs/property")
	arg_1_0.powerTxt = findTF(arg_1_0.attrs, "power/value")
	arg_1_0.levelTxt = findTF(arg_1_0.attrs, "level_bg/level_label/Text")
	arg_1_0.levelSlider = findTF(arg_1_0.attrs, "level_bg/exp")
	arg_1_0.expInfo = findTF(arg_1_0.attrs, "level_bg/exp_info")
	arg_1_0.outline = findTF(arg_1_0.attrs, "level_bg/outline")
	arg_1_0.levelTip = findTF(arg_1_0.attrs, "level_bg/tip")
	arg_1_0.levelBg = findTF(arg_1_0.attrs, "level_bg")
	arg_1_0.expTip = findTF(arg_1_0.attrs, "level_bg/exp_tip")
	arg_1_0.armorNameTxt = arg_1_0.attrs.Find("icons").GetChild(1).Find("name")

	if PLATFORM_CODE == PLATFORM_JP:
		var_0_3 = var_0_2.jp
	elif PLATFORM_CODE == PLATFORM_KR:
		var_0_3 = var_0_2.kr
	elif PLATFORM_CODE == PLATFORM_US:
		var_0_3 = var_0_2.us
	else
		var_0_3 = var_0_2.defaut

	local var_1_0 = var_0_3.sort_index

	for iter_1_0 = 1, #var_1_0:
		local var_1_1 = var_1_0[iter_1_0]
		local var_1_2 = findTF(arg_1_0.attrs, "props/" .. var_1_1)
		local var_1_3 = findTF(arg_1_0.attrs, "icons/" .. var_1_1)
		local var_1_4 = pg.gametip["attr_" .. var_1_1].tip

		if var_1_4 and string.len(var_1_4) > 0 and var_1_1 != "armor":
			setText(findTF(var_1_3, "name"), var_1_4)

		var_1_2.SetSiblingIndex(iter_1_0 - 1)
		var_1_3.SetSiblingIndex(iter_1_0 - 1)

	local var_1_5 = var_0_3.hide

	for iter_1_1 = 1, #var_1_5:
		local var_1_6 = var_1_5[iter_1_1]
		local var_1_7 = findTF(arg_1_0.attrs, "props/" .. var_1_6)
		local var_1_8 = findTF(arg_1_0.attrs, "icons/" .. var_1_6)

		setActive(var_1_7, False)
		setActive(var_1_8, False)

	local var_1_9 = var_0_3.prop_ignore

	for iter_1_2, iter_1_3 in pairs(var_1_9):
		local var_1_10 = findTF(arg_1_0.attrs, "props/" .. iter_1_2)
		local var_1_11 = findTF(arg_1_0.attrs, "icons/" .. iter_1_2)

		GetOrAddComponent(var_1_10, typeof(LayoutElement)).ignoreLayout = True
		GetOrAddComponent(var_1_11, typeof(LayoutElement)).ignoreLayout = True
		var_1_10.anchorMax = Vector2(0, 1)
		var_1_10.anchorMin = Vector2(0, 1)
		var_1_11.anchorMax = Vector2(0, 1)
		var_1_11.anchorMin = Vector2(0, 1)
		var_1_10.anchoredPosition = Vector2(iter_1_3[3], iter_1_3[4])
		var_1_11.anchoredPosition = Vector2(iter_1_3[1], iter_1_3[2])

def var_0_0.attach(arg_2_0, arg_2_1):
	var_0_0.super.attach(arg_2_0, arg_2_1)

	arg_2_0.evalueToggle = arg_2_0.attrs.Find("evalue_toggle")
	arg_2_0.evalueIndex = var_0_0.EQUIPMENT_ADDITION

	onToggle(arg_2_0.viewComponent, arg_2_0.evalueToggle, function()
		arg_2_0.evalueIndex = 1 - arg_2_0.evalueIndex

		arg_2_0.updateEvalues())

def var_0_0.enableEvent(arg_4_0, arg_4_1):
	arg_4_0.emit(ShipViewConst.SET_CLICK_ENABLE, arg_4_1)

def var_0_0.flush(arg_5_0, arg_5_1):
	assert(arg_5_1, "shipVO can not be None")

	arg_5_0.shipDataTemplate = pg.ship_data_template[arg_5_1.configId]
	arg_5_0.shipVO = arg_5_1

	arg_5_0.updateShipAttrs()
	arg_5_0.updateSKills()
	arg_5_0.updateLevelInfo()

	local var_5_0 = arg_5_1.isMaxStar()

	if not var_5_0 and arg_5_0.evalueIndex == var_0_0.TECHNOLOGY_ADDITION:
		triggerToggle(arg_5_0.evalueToggle, False)

	setActive(arg_5_0.evalueToggle, var_5_0)

def var_0_0.updateEvalues(arg_6_0):
	if not arg_6_0.additionValues:
		return

	local var_6_0 = table.contains(TeamType.SubShipType, arg_6_0.shipVO.getShipType())

	for iter_6_0, iter_6_1 in pairs(arg_6_0.additionValues.transforms):
		if iter_6_0 == AttributeType.Armor or iter_6_0 == AttributeType.Expend or iter_6_0 == AttributeType.HuntingRange and var_6_0:
			setText(iter_6_1, "")
			setActive(iter_6_1, False)
		else
			local var_6_1 = arg_6_0.additionValues[arg_6_0.evalueIndex][iter_6_0] or 0
			local var_6_2 = arg_6_0.shipVO.getTechNationMaxAddition(iter_6_0)
			local var_6_3 = arg_6_0.evalueIndex == var_0_0.EQUIPMENT_ADDITION and COLOR_GREEN or COLOR_YELLOW

			if arg_6_0.evalueIndex == var_0_0.TECHNOLOGY_ADDITION and var_6_1 != var_6_2:
				var_6_3 = "#B4BFD5FF"

			setText(iter_6_1, var_6_1 == 0 and "" or setColorStr(" +" .. var_6_1, var_6_3))
			setActive(iter_6_1, var_6_1 != 0)

def var_0_0.updateShipAttrs(arg_7_0):
	arg_7_0.additionValues = {
		[var_0_0.EQUIPMENT_ADDITION] = {},
		[var_0_0.TECHNOLOGY_ADDITION] = {},
		transforms = {}
	}

	local var_7_0 = arg_7_0.shipVO
	local var_7_1 = table.contains(TeamType.SubShipType, var_7_0.getShipType())
	local var_7_2 = intProperties(var_7_0.isBluePrintShip() and var_7_0.getBluePrint().getShipProperties(var_7_0) or var_7_0.getShipProperties())
	local var_7_3, var_7_4 = var_7_0.getEquipmentProperties()
	local var_7_5 = intProperties(var_7_3)
	local var_7_6 = intProperties(var_7_4)
	local var_7_7 = var_7_0.getShipCombatPower()

	FormationUI.tweenNumText(arg_7_0.powerTxt, var_7_7)

	for iter_7_0, iter_7_1 in pairs(var_0_1):
		local var_7_8 = findTF(arg_7_0.attrs, "props/" .. iter_7_0)
		local var_7_9 = findTF(arg_7_0.attrs, "icons/" .. iter_7_0)
		local var_7_10 = findTF(var_7_8, "value")
		local var_7_11 = findTF(var_7_8, "add")
		local var_7_12 = var_7_2[iter_7_1] or 0
		local var_7_13 = var_7_6[iter_7_1] or 1
		local var_7_14 = calcFloor(((var_7_5[iter_7_1] or 0) + var_7_12) * var_7_13) - var_7_12

		setText(var_7_10, var_7_12)

		arg_7_0.additionValues.transforms[iter_7_1] = var_7_11
		arg_7_0.additionValues[0][iter_7_1] = var_7_14
		arg_7_0.additionValues[1][iter_7_1] = var_7_0.getTechNationAddition(iter_7_1)

		if iter_7_1 == AttributeType.Armor:
			setActive(var_7_10, False)
			setActive(var_7_11, False)
			setText(arg_7_0.armorNameTxt, var_7_0.getShipArmorName())
		elif iter_7_1 == AttributeType.Expend:
			setText(findTF(var_7_8, "value"), var_7_0.getBattleTotalExpend())
			setActive(var_7_11, False)
		elif iter_7_1 == AttributeType.HuntingRange:
			setActive(var_7_9, var_7_1)
			setActive(var_7_8, var_7_1)

			if var_7_1:
				setActive(var_7_10, False)
				setActive(var_7_11, False)
		elif iter_7_1 == AttributeType.AntiSub:
			setActive(var_7_9, not var_7_1)
			setActive(var_7_8, not var_7_1)
		elif iter_7_1 == AttributeType.OxyMax or iter_7_1 == AttributeType.Ammo:
			setActive(var_7_9, var_7_1)
			setActive(var_7_8, var_7_1)

			if iter_7_1 == AttributeType.Ammo:
				setText(var_7_10, var_7_0.getShipAmmo())

	arg_7_0.updateEvalues()

def var_0_0.updateSKills(arg_8_0):
	local var_8_0 = arg_8_0.shipVO
	local var_8_1 = Clone(arg_8_0.shipDataTemplate.buff_list_display)

	for iter_8_0 = #var_8_1 + 1, 3:
		table.insert(var_8_1, False)

	setActive(arg_8_0.skillTpl, False)

	local var_8_2 = UIItemList.New(arg_8_0.skillContainer, arg_8_0.skillTpl)

	var_8_2.make(function(arg_9_0, arg_9_1, arg_9_2)
		if arg_9_0 == UIItemList.EventUpdate:
			local var_9_0 = var_8_1[arg_9_1 + 1]

			if var_9_0:
				local var_9_1 = var_8_0.fateSkillChange(var_9_0)
				local var_9_2 = getSkillConfig(var_8_0.RemapSkillId(var_9_1))
				local var_9_3 = var_8_0.skills[var_9_1]

				if var_9_3 and var_9_3.id == 11720 and not var_8_0.transforms[3612]:
					var_9_3 = None

				if var_9_3 and var_9_3.id == 14900 and not var_8_0.transforms[16412]:
					var_9_3 = None

				arg_8_0.updateSkillTF(arg_9_2, var_9_2, var_9_3)
				onButton(arg_8_0, arg_9_2, function()
					arg_8_0.emit(ShipMainMediator.ON_SKILL, var_9_2.id, var_9_3, arg_9_1 + 1), SFX_PANEL)
			else
				arg_8_0.updateSkillTF(arg_9_2)
				RemoveComponent(arg_9_2, "Button"))
	var_8_2.align(#var_8_1)

def var_0_0.updateSkillTF(arg_11_0, arg_11_1, arg_11_2, arg_11_3):
	local var_11_0 = findTF(arg_11_1, "skill")
	local var_11_1 = findTF(arg_11_1, "lock")
	local var_11_2 = findTF(arg_11_1, "unknown")

	if arg_11_2:
		setActive(var_11_0, True)
		setActive(var_11_2, False)
		setActive(var_11_1, not arg_11_3)
		LoadImageSpriteAsync("skillicon/" .. arg_11_2.icon, findTF(var_11_0, "icon"))

		findTF(var_11_0, "mask/name").anchoredPosition = Vector2(0, 0)

		setScrollText(findTF(var_11_0, "mask/name"), getSkillName(arg_11_2.id))

		local var_11_3 = findTF(var_11_0, "level")

		setText(var_11_3, "LEVEL. " .. (arg_11_3 and arg_11_3.level or "??"))
	else
		setActive(var_11_0, False)
		setActive(var_11_2, True)
		setActive(var_11_1, False)

def var_0_0.updateLevelInfo(arg_12_0):
	local var_12_0 = arg_12_0.shipVO

	setText(arg_12_0.levelTxt, var_12_0.level)

	local var_12_1 = var_12_0.getLevelExpConfig()

	if var_12_0.level != var_12_0.getMaxLevel():
		setSlider(arg_12_0.levelSlider, 0, var_12_1.exp_interval, var_12_0.exp)
		setText(arg_12_0.expInfo, var_12_0.exp .. "/" .. var_12_1.exp_interval)
	else
		setSlider(arg_12_0.levelSlider, 0, 1, 1)
		setText(arg_12_0.expInfo, var_12_0.exp .. "/Max")

	arg_12_0.updateMaxLevel(var_12_0)
	arg_12_0.UpdateExpTip(var_12_0)

def var_0_0.UpdateExpTip(arg_13_0, arg_13_1):
	local var_13_0 = arg_13_1.isReachNextMaxLevel()
	local var_13_1 = arg_13_1.level >= arg_13_1.maxLevel

	setActive(arg_13_0.expTip, not var_13_0 and not var_13_1)
	onButton(arg_13_0, arg_13_0.expTip, function()
		if arg_13_1.isActivityNpc():
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("coures_exp_npc_tip"),
				def onYes:()
					arg_13_0.emit(ShipViewConst.SHOW_EXP_ITEM_USAGE, arg_13_1)
			})
		else
			arg_13_0.emit(ShipViewConst.SHOW_EXP_ITEM_USAGE, arg_13_1), SFX_PANEL)

def var_0_0.updateMaxLevel(arg_16_0, arg_16_1):
	if arg_16_1.isReachNextMaxLevel():
		SetActive(arg_16_0.outline, True)
		setActive(arg_16_0.levelTip, True)
		blinkAni(arg_16_0.outline, 1.5, -1, 0.1).setFrom(1)
		blinkAni(arg_16_0.levelTip, 1.5, -1, 0.1).setFrom(1)

		local var_16_0 = arg_16_1.getNextMaxLevelConsume()
		local var_16_1 = arg_16_1.getMaxLevel()
		local var_16_2 = arg_16_1.getNextMaxLevel()

		onButton(arg_16_0, arg_16_0.levelBg, function()
			if arg_16_1.isActivityNpc():
				pg.TipsMgr.GetInstance().ShowTips(i18n("npc_upgrade_max_level"))

				return

			arg_16_0.emit(ShipViewConst.SHOW_CUSTOM_MSG, {
				content = i18n("upgrade_to_next_maxlevel_tip"),
				content1 = var_16_1 .. "->" .. var_16_2,
				items = var_16_0,
				def onYes:()
					local var_18_0, var_18_1 = arg_16_1.canUpgradeMaxLevel()

					if var_18_0:
						arg_16_0.emit(ShipViewConst.HIDE_CUSTOM_MSG)
						arg_16_0.emit(ShipMainMediator.ON_UPGRADE_MAX_LEVEL, arg_16_1.id)
					else
						pg.TipsMgr.GetInstance().ShowTips(var_18_1)
			}), SFX_PANEL)
	else
		arg_16_0.removeLevelUpTip()

def var_0_0.removeLevelUpTip(arg_19_0):
	SetActive(arg_19_0.outline, False)
	setActive(arg_19_0.levelTip, False)

	if LeanTween.isTweening(go(arg_19_0.outline)):
		LeanTween.cancel(go(arg_19_0.outline))

	if LeanTween.isTweening(go(arg_19_0.levelTip)):
		LeanTween.cancel(go(arg_19_0.levelTip))

	removeOnButton(arg_19_0.levelBg)

def var_0_0.doLeveUpAnim(arg_20_0, arg_20_1, arg_20_2, arg_20_3):
	arg_20_0.removeLevelUpTip()
	arg_20_0.enableEvent(False)

	local var_20_0 = {}

	if arg_20_1.level < arg_20_2.level:
		local var_20_1 = arg_20_2.level - arg_20_1.level
		local var_20_2 = arg_20_1.getLevelExpConfig()

		for iter_20_0 = 1, var_20_1:
			table.insert(var_20_0, function(arg_21_0)
				TweenValue(arg_20_0.levelSlider, 0, var_20_2.exp_interval, var_0_4, 0, function(arg_22_0)
					setSlider(arg_20_0.levelSlider, 0, var_20_2.exp_interval, arg_22_0)
					setText(arg_20_0.expInfo, math.floor(arg_22_0) .. "/" .. var_20_2.exp_interval), function()
					local var_23_0 = Clone(arg_20_1)

					arg_20_1.level = arg_20_1.level + 1
					var_20_2 = arg_20_1.getLevelExpConfig()

					arg_20_0.scaleAnim(arg_20_0.levelTxt, var_0_5, var_0_6, var_0_4 / 2, function()
						if arg_20_1.level == arg_20_2.level:
							arg_20_0.doAttrAnim(var_23_0, arg_20_2, function()
								TweenValue(arg_20_0.levelSlider, 0, arg_20_2.exp, var_0_4, 0, function(arg_26_0)
									setSlider(arg_20_0.levelSlider, 0, var_20_2.exp_interval, arg_26_0)
									setText(arg_20_0.expInfo, math.floor(arg_26_0) .. "/" .. var_20_2.exp_interval), arg_21_0))
						else
							arg_20_0.doAttrAnim(var_23_0, arg_20_1, arg_21_0), function()
						setText(arg_20_0.levelTxt, arg_20_1.level))))
	else
		local var_20_3 = arg_20_2.getLevelExpConfig()

		if arg_20_2.exp > arg_20_1.exp:
			table.insert(var_20_0, function(arg_28_0)
				TweenValue(arg_20_0.levelSlider, arg_20_1.exp, arg_20_2.exp, var_0_4, 0, function(arg_29_0)
					setSlider(arg_20_0.levelSlider, 0, var_20_3.exp_interval, arg_29_0)
					setText(arg_20_0.expInfo, math.floor(arg_29_0) .. "/" .. var_20_3.exp_interval), arg_28_0))

	seriesAsync(var_20_0, function()
		if arg_20_3:
			arg_20_3()

		arg_20_0.enableEvent(True))

def var_0_0.doAttrAnim(arg_31_0, arg_31_1, arg_31_2, arg_31_3):
	local var_31_0 = intProperties(arg_31_1.getShipProperties())
	local var_31_1, var_31_2 = arg_31_1.getEquipmentProperties()
	local var_31_3 = intProperties(arg_31_2.getShipProperties())
	local var_31_4, var_31_5 = arg_31_2.getEquipmentProperties()
	local var_31_6 = intProperties(var_31_1)
	local var_31_7 = intProperties(var_31_2)
	local var_31_8 = intProperties(var_31_4)
	local var_31_9 = intProperties(var_31_5)
	local var_31_10 = {}
	local var_31_11 = arg_31_2.getShipCombatPower()
	local var_31_12 = arg_31_1.getShipCombatPower()

	if var_31_12 != var_31_11:
		table.insert(var_31_10, function(arg_32_0)
			TweenValue(arg_31_0.powerTxt, var_31_12, var_31_11, var_0_4, 0, function(arg_33_0)
				setText(arg_31_0.powerTxt, math.floor(arg_33_0)), arg_32_0))

	for iter_31_0, iter_31_1 in pairs(var_0_1):
		local var_31_13 = findTF(arg_31_0.attrs, "props/" .. iter_31_0) or findTF(arg_31_0.attrs, "prop_" .. iter_31_0)
		local var_31_14 = findTF(arg_31_0.attrs, "icons/" .. iter_31_0) or findTF(arg_31_0.attrs, "icon_" .. iter_31_0)
		local var_31_15 = findTF(var_31_13, "value")
		local var_31_16 = findTF(var_31_13, "add")
		local var_31_17 = var_31_0[iter_31_1] or 0
		local var_31_18 = var_31_7[iter_31_1] or 1
		local var_31_19 = var_31_3[iter_31_1] or 0
		local var_31_20 = var_31_9[iter_31_1] or 1
		local var_31_21
		local var_31_22

		if arg_31_0.evalueIndex == var_0_0.EQUIPMENT_ADDITION:
			var_31_21 = calcFloor(((var_31_6[iter_31_1] or 0) + var_31_17) * var_31_18) - var_31_17
			var_31_22 = calcFloor(((var_31_8[iter_31_1] or 0) + var_31_19) * var_31_20) - var_31_19
		elif arg_31_0.evalueIndex == var_0_0.TECHNOLOGY_ADDITION:
			var_31_21 = arg_31_1.getTechNationAddition(iter_31_1)
			var_31_22 = arg_31_2.getTechNationAddition(iter_31_1)

		if var_31_17 != 0:
			table.insert(var_31_10, function(arg_34_0)
				TweenValue(var_31_15, var_31_17, var_31_19, var_0_4, 0, function(arg_35_0)
					setText(var_31_15, math.floor(arg_35_0)), arg_34_0)
				arg_31_0.scaleAnim(var_31_15, var_0_5, var_0_6, var_0_4 / 2))

		if var_31_21 < var_31_22:
			local var_31_23 = arg_31_0.evalueIndex == var_0_0.EQUIPMENT_ADDITION and COLOR_GREEN or COLOR_YELLOW

			table.insert(var_31_10, function(arg_36_0)
				TweenValue(var_31_16, var_31_21, var_31_22, var_0_4, 0, function(arg_37_0)
					setText(var_31_16, setColorStr("+" .. math.floor(arg_37_0), var_31_23)), arg_36_0)
				arg_31_0.scaleAnim(var_31_16, var_0_5, var_0_6, var_0_4 / 2))

		setActive(var_31_16, var_31_22 != 0)

		if iter_31_1 == AttributeType.Armor:
			setActive(var_31_15, False)
			setActive(var_31_16, False)
			setText(arg_31_0.armorNameTxt, arg_31_2.getShipArmorName())
		elif iter_31_1 == AttributeType.Expend:
			local var_31_24 = arg_31_2.getBattleTotalExpend()
			local var_31_25 = arg_31_1.getBattleTotalExpend()
			local var_31_26 = findTF(var_31_13, "value")

			if var_31_25 != var_31_24:
				table.insert(var_31_10, function(arg_38_0)
					TweenValue(var_31_26, var_31_25, var_31_24, var_0_4, 0, function(arg_39_0)
						setText(var_31_26, math.floor(arg_39_0)), arg_38_0)
					arg_31_0.scaleAnim(var_31_26, var_0_5, var_0_6, var_0_4 / 2))

			setActive(var_31_16, False)
		elif iter_31_1 == AttributeType.OxyMax or iter_31_1 == AttributeType.Tactics:
			local var_31_27 = table.contains(TeamType.SubShipType, arg_31_2.getShipType())

			setActive(var_31_14, var_31_27)
			setActive(var_31_13, var_31_27)

			if var_31_27 and iter_31_1 == AttributeType.Tactics:
				local var_31_28, var_31_29 = arg_31_2.getTactics()

				setActive(var_31_15, False)
				setActive(var_31_16, True)
				setText(var_31_16, i18n(var_31_29))

	parallelAsync(var_31_10, function()
		if arg_31_3:
			arg_31_3())

def var_0_0.scaleAnim(arg_41_0, arg_41_1, arg_41_2, arg_41_3, arg_41_4, arg_41_5, arg_41_6):
	LeanTween.scale(go(arg_41_1), arg_41_3, arg_41_4).setFrom(arg_41_2).setOnComplete(System.Action(function()
		if arg_41_6:
			arg_41_6()

		LeanTween.scale(go(arg_41_1), arg_41_2, arg_41_4).setFrom(arg_41_3).setOnComplete(System.Action(arg_41_5))))

def var_0_0.clear(arg_43_0):
	triggerToggle(arg_43_0.evalueToggle, False)

	if LeanTween.isTweening(go(arg_43_0.levelSlider)):
		LeanTween.cancel(go(arg_43_0.levelSlider))

	if LeanTween.isTweening(go(arg_43_0.powerTxt)):
		LeanTween.cancel(go(arg_43_0.powerTxt))

	if LeanTween.isTweening(go(arg_43_0.expInfo)):
		LeanTween.cancel(go(arg_43_0.expInfo))

	arg_43_0.removeLevelUpTip()

	arg_43_0.additionValues = None

return var_0_0
