local var_0_0 = class("CommanderLockFlagSettingPage", import("view.base.BaseSubView"))
local var_0_1 = 1
local var_0_2 = 2
local var_0_3 = 3

def var_0_0.getUIName(arg_1_0):
	return "CommanderLockFlagSettingui"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.closeBtn = arg_2_0.findTF("frame/close_btn")
	arg_2_0.cancelBtn = arg_2_0.findTF("frame/cancel")
	arg_2_0.confirmBtn = arg_2_0.findTF("frame/confirm")
	arg_2_0.allBtn = arg_2_0.findTF("frame/title/all_btn")
	arg_2_0.allSel = arg_2_0.allBtn.Find("Image")
	arg_2_0.ssrToggle = arg_2_0.findTF("frame/toggles/rarity/ssr")
	arg_2_0.srToggle = arg_2_0.findTF("frame/toggles/rarity/sr")
	arg_2_0.rToggle = arg_2_0.findTF("frame/toggles/rarity/r")
	arg_2_0.talentUIlist = UIItemList.New(arg_2_0.findTF("frame/toggles/scrollrect/content/talent"), arg_2_0.findTF("frame/toggles/scrollrect/content/talent/tpl"))
	arg_2_0.descTxt = arg_2_0.findTF("frame/desc/Text").GetComponent(typeof(Text))

	setText(arg_2_0.findTF("frame/title/rarity"), i18n("word_rarity") .. ". ")
	setText(arg_2_0.findTF("frame/title/talent"), i18n("word_talent") .. ". ")
	setText(arg_2_0.findTF("frame/desc/Text"), i18n("commander_lock_setting_title"))

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.closeBtn, function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.cancelBtn, function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.confirmBtn, function()
		if arg_3_0.UnselAnyTalent() or arg_3_0.UnselAnyRarity():
			arg_3_0.contextData.msgBox.ExecuteAction("Show", {
				content = i18n("commander_unsel_lock_flag_tip"),
				def onYes:()
					arg_3_0.Conform()
			})
		else
			arg_3_0.Conform(), SFX_PANEL)

def var_0_0.UnselAnyTalent(arg_9_0):
	for iter_9_0, iter_9_1 in pairs(arg_9_0.talentList):
		if iter_9_1 == True:
			return False

	return True

def var_0_0.UnselAnyRarity(arg_10_0):
	for iter_10_0, iter_10_1 in pairs(arg_10_0.rarityList):
		if iter_10_1 == True:
			return False

	return True

def var_0_0.Conform(arg_11_0):
	arg_11_0.SaveRarityConfig(arg_11_0.rarityList)
	arg_11_0.SaveTalentConfig(arg_11_0.talentList)
	arg_11_0.Hide()

def var_0_0.Show(arg_12_0):
	var_0_0.super.Show(arg_12_0)
	arg_12_0.InitRarity()
	arg_12_0.InitTalent()

def var_0_0.InitRarity(arg_13_0):
	local var_13_0 = arg_13_0.GetRarityConfig()

	arg_13_0.rarityList = {}

	onToggle(arg_13_0, arg_13_0.ssrToggle, function(arg_14_0)
		arg_13_0.rarityList[var_0_1] = arg_14_0, SFX_PANEL)
	onToggle(arg_13_0, arg_13_0.srToggle, function(arg_15_0)
		arg_13_0.rarityList[var_0_2] = arg_15_0, SFX_PANEL)
	onToggle(arg_13_0, arg_13_0.rToggle, function(arg_16_0)
		arg_13_0.rarityList[var_0_3] = arg_16_0, SFX_PANEL)
	triggerToggle(arg_13_0.ssrToggle, var_13_0[var_0_1])
	triggerToggle(arg_13_0.srToggle, var_13_0[var_0_2])
	triggerToggle(arg_13_0.rToggle, var_13_0[var_0_3])

def var_0_0.InitTalent(arg_17_0):
	local var_17_0 = arg_17_0.GetTalentConfig()

	arg_17_0.talentList = {}
	arg_17_0.talentCards = {}

	local var_17_1 = CommanderCatUtil.GetAllTalentNames()

	arg_17_0.talentUIlist.make(function(arg_18_0, arg_18_1, arg_18_2)
		if arg_18_0 == UIItemList.EventUpdate:
			local var_18_0 = var_17_1[arg_18_1 + 1].id
			local var_18_1 = var_17_1[arg_18_1 + 1].name

			onToggle(arg_17_0, arg_18_2, function(arg_19_0)
				arg_17_0.talentList[var_18_0] = arg_19_0

				arg_17_0.UpdateAllBtnStyle(), SFX_PANEL)
			setText(arg_18_2.Find("Text"), var_18_1)

			arg_18_2.gameObject.name = var_18_0
			arg_17_0.talentCards[var_18_0] = arg_18_2)
	arg_17_0.talentUIlist.align(#var_17_1)

	for iter_17_0, iter_17_1 in pairs(var_17_0):
		if arg_17_0.talentCards[iter_17_0]:
			triggerToggle(arg_17_0.talentCards[iter_17_0], iter_17_1)

	onButton(arg_17_0, arg_17_0.allBtn, function()
		if arg_17_0.AnyCardUnSelected():
			arg_17_0.TriggerAllCardTrue()
		else
			arg_17_0.TriggerAllCardFalse()

		arg_17_0.UpdateAllBtnStyle(), SFX_PANEL)
	arg_17_0.UpdateAllBtnStyle()

def var_0_0.UpdateAllBtnStyle(arg_21_0):
	setActive(arg_21_0.allSel, not arg_21_0.AnyCardUnSelected())

def var_0_0.AnyCardUnSelected(arg_22_0):
	for iter_22_0, iter_22_1 in pairs(arg_22_0.talentCards):
		if not iter_22_1.GetComponent(typeof(Toggle)).isOn:
			return True

	return False

def var_0_0.TriggerAllCardTrue(arg_23_0):
	for iter_23_0, iter_23_1 in pairs(arg_23_0.talentCards):
		triggerToggle(iter_23_1, True)

def var_0_0.TriggerAllCardFalse(arg_24_0):
	for iter_24_0, iter_24_1 in pairs(arg_24_0.talentCards):
		triggerToggle(iter_24_1, False)

def var_0_0.GetRarityConfig(arg_25_0):
	return (getProxy(SettingsProxy).GetCommanderLockFlagRarityConfig())

def var_0_0.SaveRarityConfig(arg_26_0, arg_26_1):
	getProxy(SettingsProxy).SaveCommanderLockFlagRarityConfig(arg_26_1)

def var_0_0.GetTalentConfig(arg_27_0):
	return (getProxy(SettingsProxy).GetCommanderLockFlagTalentConfig())

def var_0_0.SaveTalentConfig(arg_28_0, arg_28_1):
	getProxy(SettingsProxy).SaveCommanderLockFlagTalentConfig(arg_28_1)

def var_0_0.OnDestroy(arg_29_0):
	return

return var_0_0
