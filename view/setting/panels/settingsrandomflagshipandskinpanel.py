local var_0_0 = class("SettingsRandomFlagShipAndSkinPanel", import(".SettingsBasePanel"))

var_0_0.EVT_UPDTAE = "SettingsRandomFlagShipAndSkinPanel.EVT_UPDTAE"
var_0_0.SHIP_FREQUENTLYUSED = 1
var_0_0.SHIP_LOCKED = 2
var_0_0.COUSTOM = 3

def var_0_0.GetUIName(arg_1_0):
	return "RandomFlagShipAndSkin"

def var_0_0.GetTitle(arg_2_0):
	return i18n("random_ship_and_skin_title")

def var_0_0.GetTitleEn(arg_3_0):
	return "                                                                                      / RANDOM RANGE"

def var_0_0.OnInit(arg_4_0):
	arg_4_0.subTitleTxt = arg_4_0._tf.Find("title").GetComponent(typeof(Text))
	arg_4_0.shipToggles = {
		[var_0_0.SHIP_FREQUENTLYUSED] = arg_4_0._tf.Find("1"),
		[var_0_0.SHIP_LOCKED] = arg_4_0._tf.Find("2"),
		[var_0_0.COUSTOM] = arg_4_0._tf.Find("3")
	}
	arg_4_0.shipToggleTxts = {
		[var_0_0.SHIP_FREQUENTLYUSED] = i18n("random_ship_frequse_mode"),
		[var_0_0.SHIP_LOCKED] = i18n("random_ship_locked_mode"),
		[var_0_0.COUSTOM] = i18n("random_ship_custom_mode")
	}
	arg_4_0.editBtn = findTF(arg_4_0._tf, "edit_btn")

	arg_4_0.UpdateSelected()
	arg_4_0.InitToggles()

def var_0_0.InitToggles(arg_5_0):
	for iter_5_0, iter_5_1 in pairs(arg_5_0.shipToggles):
		onToggle(arg_5_0, iter_5_1, function(arg_6_0)
			if arg_6_0:
				arg_5_0.UpdateShipRandomMode(iter_5_0), SFX_PANEL)
		setText(iter_5_1.Find("Text"), arg_5_0.shipToggleTxts[iter_5_0])

	onButton(arg_5_0, arg_5_0.editBtn, function()
		pg.m02.sendNotification(GAME.GO_SCENE, SCENE.RANDOM_DOCKYARD), SFX_PANEL)

def var_0_0.UpdateShipRandomMode(arg_8_0, arg_8_1):
	if arg_8_1 == var_0_0.COUSTOM and not arg_8_0.refreshFlag and #getProxy(PlayerProxy).getRawData().GetCustomRandomShipList() == 0:
		pg.TipsMgr.GetInstance().ShowTips(i18n("random_ship_custom_mode_empty"))

	arg_8_0.refreshFlag = None

	if arg_8_0.randomFlagShipMode != arg_8_1:
		pg.m02.sendNotification(GAME.CHANGE_RANDOM_SHIP_MODE, {
			mode = arg_8_1
		})

def var_0_0.UpdateSelected(arg_9_0):
	local var_9_0 = getProxy(PlayerProxy).getRawData().GetRandomFlagShipMode()

	arg_9_0.randomFlagShipMode = var_9_0

	triggerToggle(arg_9_0.shipToggles[var_9_0], True)

def var_0_0.OnRandomFlagshipFlagUpdate(arg_10_0):
	arg_10_0.refreshFlag = True

	arg_10_0.UpdateSelected()

return var_0_0
