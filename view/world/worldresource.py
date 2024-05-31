local var_0_0 = class("WorldResource", import("..base.BaseUI"))

var_0_0.Listeners = {
	onUpdateInventory = "OnUpdateInventory",
	onUpdateActivate = "OnUpdateActivate",
	onUpdateStamina = "OnUpdateStamina",
	onBossProgressUpdate = "OnBossProgressUpdate"
}

def var_0_0.Ctor(arg_1_0):
	var_0_0.super.Ctor(arg_1_0)
	PoolMgr.GetInstance().GetUI("WorldResPanel", False, function(arg_2_0)
		local var_2_0 = pg.UIMgr.GetInstance().UIMain

		arg_2_0.transform.SetParent(var_2_0.transform, False)
		arg_1_0.onUILoaded(arg_2_0))

def var_0_0.init(arg_3_0):
	for iter_3_0, iter_3_1 in pairs(var_0_0.Listeners):
		arg_3_0[iter_3_0] = function(...)
			var_0_0[iter_3_1](arg_3_0, ...)

	local var_3_0 = nowWorld()

	arg_3_0.stamina = arg_3_0.findTF("res/stamina")

	onButton(arg_3_0, arg_3_0.stamina, function()
		var_3_0.staminaMgr.Show(), SFX_PANEL)

	arg_3_0.oil = arg_3_0.findTF("res/oil")

	onButton(arg_3_0, arg_3_0.oil, function()
		local var_6_0 = ShoppingStreet.getRiseShopId(ShopArgs.BuyOil, arg_3_0.player.buyOilCount)

		if not var_6_0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_today_buy_limit"))

			return

		local var_6_1 = pg.shop_template[var_6_0]
		local var_6_2 = var_6_1.num

		if var_6_1.num == -1 and var_6_1.genre == ShopArgs.BuyOil:
			var_6_2 = ShopArgs.getOilByLevel(arg_3_0.player.level)

		if pg.gameset.buy_oil_limit.key_value > arg_3_0.player.buyOilCount:
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				type = MSGBOX_TYPE_SINGLE_ITEM,
				content = i18n("oil_buy_tip", var_6_1.resource_num, var_6_2, arg_3_0.player.buyOilCount),
				drop = {
					id = 2,
					type = DROP_TYPE_RESOURCE,
					count = var_6_2
				},
				def onYes:()
					pg.m02.sendNotification(GAME.SHOPPING, {
						isQuickShopping = True,
						count = 1,
						id = var_6_0
					})
			})
		else
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				type = MSGBOX_TYPE_HELP,
				helps = i18n("help_oil_buy_limit"),
				custom = {
					{
						text = "text_iknow",
						sound = SFX_CANCEL
					}
				}
			}), SFX_PANEL)

	arg_3_0.Whuobi = arg_3_0.findTF("res/Whuobi")

	onButton(arg_3_0, arg_3_0.Whuobi, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_SINGLE_ITEM,
			drop = Drop.New({
				type = DROP_TYPE_WORLD_ITEM,
				id = WorldItem.MoneyId
			})
		}), SFX_PANEL)

	arg_3_0.bossProgress = arg_3_0.findTF("res/boss_progress")

	onButton(arg_3_0, arg_3_0.bossProgress, function()
		local var_9_0 = WorldBossConst.GetCurrBossItemInfo()
		local var_9_1 = WorldBossConst.CanUnlockCurrBoss()

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			hideNo = True,
			type = MSGBOX_TYPE_DROP_ITEM,
			name = var_9_0.name,
			content = var_9_0.display,
			iconPath = var_9_0.icon,
			frame = var_9_0.rarity,
			yesText = i18n("common_go_to_analyze"),
			yesGray = not var_9_1,
			def onYes:()
				if var_9_1 and var_3_0.GetBossProxy().IsOpen():
					pg.m02.sendNotification(GAME.GO_SCENE, SCENE.WORLDBOSS)
				else
					pg.TipsMgr.GetInstance().ShowTips(i18n("world_boss_progress_no_enough"))
					pg.MsgboxMgr.GetInstance().hide()
		}), SFX_PANEL)

	if var_3_0.GetActiveMap():
		arg_3_0.setStaminaMgr(var_3_0.staminaMgr)
	else
		arg_3_0.atlas = var_3_0.GetAtlas()

		arg_3_0.atlas.AddListener(WorldAtlas.EventUpdateActiveMap, arg_3_0.onUpdateActivate)
		setActive(arg_3_0.stamina, False)

	arg_3_0.setWorldInventory(var_3_0.GetInventoryProxy())
	arg_3_0.SetWorldBossRes(var_3_0.GetBossProxy())

def var_0_0.setParent(arg_11_0, arg_11_1, arg_11_2):
	setParent(arg_11_0._go, arg_11_1, arg_11_2)

def var_0_0.setPlayer(arg_12_0, arg_12_1):
	assert(isa(arg_12_1, Player), "should be an instance of Player")

	arg_12_0.player = arg_12_1

	setText(arg_12_0.oil.Find("max_value"), "MAX." .. pg.user_level[arg_12_1.level].max_oil)
	setText(arg_12_0.oil.Find("value"), arg_12_1.oil)

def var_0_0.OnUpdateActivate(arg_13_0):
	arg_13_0.setStaminaMgr(nowWorld().staminaMgr)
	arg_13_0.atlas.RemoveListener(WorldAtlas.EventUpdateActiveMap, arg_13_0.onUpdateActivate)

def var_0_0.setStaminaMgr(arg_14_0, arg_14_1):
	arg_14_0.staminaMgr = arg_14_1

	setText(arg_14_0.stamina.Find("max_value"), "MAX." .. arg_14_1.GetMaxStamina())
	arg_14_0.staminaMgr.AddListener(WorldStaminaManager.EventUpdateStamina, arg_14_0.onUpdateStamina)
	arg_14_0.OnUpdateStamina()
	setActive(arg_14_0.stamina, True)

def var_0_0.setWorldInventory(arg_15_0, arg_15_1):
	arg_15_0.inventoryProxy = arg_15_1

	arg_15_0.inventoryProxy.AddListener(WorldInventoryProxy.EventUpdateItem, arg_15_0.onUpdateInventory)
	arg_15_0.OnUpdateInventory()

def var_0_0.OnUpdateStamina(arg_16_0):
	setText(arg_16_0.stamina.Find("value"), arg_16_0.staminaMgr.GetDisplayStanima())

def var_0_0.OnUpdateInventory(arg_17_0, arg_17_1, arg_17_2, arg_17_3):
	if not arg_17_1 or arg_17_1 == WorldInventoryProxy.EventUpdateItem and arg_17_3.id == WorldItem.MoneyId:
		setText(arg_17_0.Whuobi.Find("value"), arg_17_0.inventoryProxy.GetItemCount(WorldItem.MoneyId))

def var_0_0.SetWorldBossRes(arg_18_0, arg_18_1):
	arg_18_0.worldBossProxy = arg_18_1

	arg_18_0.worldBossProxy.AddListener(WorldBossProxy.EventUnlockProgressUpdated, arg_18_0.onBossProgressUpdate)
	arg_18_0.OnBossProgressUpdate()

def var_0_0.OnBossProgressUpdate(arg_19_0):
	local var_19_0 = WorldBossConst.GetCurrBossItemProgress()
	local var_19_1, var_19_2, var_19_3 = WorldBossConst.GetCurrBossItemCapacity()
	local var_19_4, var_19_5 = WorldBossConst.GetCurrBossConsume()
	local var_19_6 = arg_19_0.bossProgress.Find("value")
	local var_19_7 = arg_19_0.bossProgress.Find("max_value")
	local var_19_8 = var_19_3 <= var_19_2 and COLOR_GREY or COLOR_WHITE

	setText(var_19_6, "<color=" .. var_19_8 .. ">" .. var_19_0 .. "/" .. var_19_5 .. "</color>")
	setText(var_19_7, "<color=" .. var_19_8 .. ">DAILY." .. var_19_2 .. "/" .. var_19_3 .. "</color>")
	setActive(arg_19_0.bossProgress, nowWorld().IsSystemOpen(WorldConst.SystemWorldBoss))

def var_0_0.willExit(arg_20_0):
	if arg_20_0.staminaMgr:
		arg_20_0.staminaMgr.RemoveListener(WorldStaminaManager.EventUpdateStamina, arg_20_0.onUpdateStamina)
	else
		arg_20_0.atlas.RemoveListener(WorldAtlas.EventUpdateActiveMap, arg_20_0.onUpdateActivate)

	arg_20_0.inventoryProxy.RemoveListener(WorldInventoryProxy.EventUpdateItem, arg_20_0.onUpdateInventory)
	arg_20_0.worldBossProxy.RemoveListener(WorldBossProxy.EventUnlockProgressUpdated, arg_20_0.onBossProgressUpdate)
	PoolMgr.GetInstance().ReturnUI("WorldResPanel", arg_20_0._go)

return var_0_0
