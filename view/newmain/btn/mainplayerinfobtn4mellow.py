local var_0_0 = class("MainPlayerInfoBtn4Mellow", import(".MainPlayerInfoBtn"))

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_0.super.super.Ctor(arg_1_0, arg_1_1, arg_1_2)
	pg.DelegateInfo.New(arg_1_0)

	arg_1_0.playerInfoBtn = findTF(arg_1_0._tf, "name_bg")
	arg_1_0.playerNameTxt = findTF(arg_1_0._tf, "name_bg/Text").GetComponent(typeof(Text))
	arg_1_0.playerLevelTr = findTF(arg_1_0._tf, "name_bg/level/Text")
	arg_1_0.playerLevelTxt = findTF(arg_1_0._tf, "name_bg/level/Text").GetComponent(typeof(Text))
	arg_1_0.expTxt = findTF(arg_1_0._tf, "name_bg/level/mask/Text").GetComponent(typeof(Text))
	arg_1_0.goldMax = findTF(arg_1_0._tf, "res/gold/max").GetComponent(typeof(Text))
	arg_1_0.goldValue = findTF(arg_1_0._tf, "res/gold/Text").GetComponent(typeof(Text))
	arg_1_0.oilMax = findTF(arg_1_0._tf, "res/oil/max").GetComponent(typeof(Text))
	arg_1_0.oilValue = findTF(arg_1_0._tf, "res/oil/Text").GetComponent(typeof(Text))
	arg_1_0.gemValue = findTF(arg_1_0._tf, "res/gem/Text").GetComponent(typeof(Text))
	arg_1_0.expTr = findTF(arg_1_0._tf, "name_bg/level/mask")

	onButton(arg_1_0, findTF(arg_1_0._tf, "res/gold"), function()
		pg.playerResUI.ClickGold(), SFX_PANEL)
	onButton(arg_1_0, findTF(arg_1_0._tf, "res/oil"), function()
		pg.playerResUI.ClickOil(), SFX_PANEL)
	onButton(arg_1_0, findTF(arg_1_0._tf, "res/gem"), function()
		pg.playerResUI.ClickGem(), SFX_PANEL)
	arg_1_0.bind(PlayerProxy.UPDATED, function()
		arg_1_0.Flush())
	arg_1_0.bind(GAME.GUILD_GET_USER_INFO_DONE, function()
		arg_1_0.Flush())
	arg_1_0.bind(GAME.GET_PUBLIC_GUILD_USER_DATA_DONE, function()
		arg_1_0.Flush())

def var_0_0.Flush(arg_8_0, arg_8_1):
	var_0_0.super.Flush(arg_8_0, arg_8_1)
	arg_8_0.UpdateRes()

def var_0_0.UpdateRes(arg_9_0):
	local var_9_0 = getProxy(PlayerProxy).getRawData()

	PlayerResUI.StaticFlush(var_9_0, arg_9_0.goldMax, arg_9_0.goldValue, arg_9_0.oilMax, arg_9_0.oilValue, arg_9_0.gemValue)

def var_0_0.UpdateExp(arg_10_0):
	local var_10_0 = 0
	local var_10_1 = getProxy(PlayerProxy).getRawData()

	arg_10_0.playerLevelTxt.text = var_10_1.level
	arg_10_0.expTxt.text = var_10_1.level

	local var_10_2

	if var_10_1.level == var_10_1.getMaxLevel():
		var_10_2 = 1
	else
		local var_10_3 = getConfigFromLevel1(pg.user_level, var_10_1.level)

		var_10_2 = var_10_1.exp / var_10_3.exp_interval

	local var_10_4 = 34 * var_10_2

	arg_10_0.expTr.sizeDelta = Vector2(70, var_10_4)

def var_0_0.Dispose(arg_11_0):
	var_0_0.super.Dispose(arg_11_0)
	pg.DelegateInfo.Dispose(arg_11_0)

return var_0_0
