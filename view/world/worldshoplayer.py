local var_0_0 = class("WorldShopLayer", import("view.base.BaseUI"))

var_0_0.Listeners = {
	onUpdateGoods = "updateGoods"
}
var_0_0.optionsPath = {
	"adapt/top/title/option"
}

def var_0_0.getUIName(arg_1_0):
	return "WorldShopUI"

def var_0_0.getBGM(arg_2_0):
	return "story-richang"

def var_0_0.init(arg_3_0):
	for iter_3_0, iter_3_1 in pairs(var_0_0.Listeners):
		arg_3_0[iter_3_0] = function(...)
			var_0_0[iter_3_1](arg_3_0, ...)

	arg_3_0.btnBack = arg_3_0.findTF("adapt/top/title/back_button")
	arg_3_0.rtRes = arg_3_0.findTF("adapt/middle/content/res")
	arg_3_0.rtResetTime = arg_3_0.findTF("adapt/middle/content/resetTimer")
	arg_3_0.rtResetTip = arg_3_0.findTF("adapt/middle/content/resetTip")
	arg_3_0.rtShop = arg_3_0.findTF("adapt/middle/content/world_shop")
	arg_3_0.goodsItemList = UIItemList.New(arg_3_0.rtShop.Find("content"), arg_3_0.rtShop.Find("content/item_tpl"))
	arg_3_0.singleWindow = OriginShopSingleWindow.New(arg_3_0._tf, arg_3_0.event)
	arg_3_0.multiWindow = OriginShopMultiWindow.New(arg_3_0._tf, arg_3_0.event)

def var_0_0.didEnter(arg_5_0):
	pg.UIMgr.GetInstance().OverlayPanel(arg_5_0._tf, {
		groupName = arg_5_0.getGroupNameFromData()
	})
	onButton(arg_5_0, arg_5_0.btnBack, function()
		arg_5_0.closeView(), SFX_CANCEL)
	onButton(arg_5_0, arg_5_0.rtRes, function()
		arg_5_0.emit(var_0_0.ON_DROP, {
			type = DROP_TYPE_RESOURCE,
			id = WorldConst.ResourceID
		}), SFX_PANEL)
	arg_5_0.goodsItemList.make(function(arg_8_0, arg_8_1, arg_8_2)
		local var_8_0 = arg_8_1 + 1

		if arg_8_0 == UIItemList.EventUpdate:
			local var_8_1 = Goods.Create(arg_5_0.goodsList[var_8_0], Goods.TYPE_WORLD)

			GoodsCard.New(arg_8_2).update(var_8_1)

			local var_8_2 = var_8_1.getLimitCount()

			setText(arg_8_2.Find("item/count_contain/label"), i18n("activity_shop_exchange_count"))
			setText(arg_8_2.Find("item/count_contain/count"), var_8_2 - var_8_1.buyCount .. "/" .. var_8_2)
			setTextColor(arg_8_2.Find("item/count_contain/count"), Color.New(unpack(ActivityGoodsCard.DefaultColor)))
			setTextColor(arg_8_2.Find("item/count_contain/label"), Color.New(unpack(ActivityGoodsCard.DefaultColor)))
			onButton(arg_5_0, arg_8_2, function()
				local var_9_0 = nowWorld()

				if var_8_1.getConfig("genre") == ShopArgs.WorldCollection and var_9_0.GetTaskProxy().hasDoingCollectionTask():
					pg.TipsMgr.GetInstance().ShowTips(i18n("world_collection_task_tip_1"))

					return
				elif var_8_1.id == 100000 and not underscore.any(underscore.values(var_9_0.pressingAwardDic), function(arg_10_0)
					return arg_10_0.flag):
					pg.TipsMgr.GetInstance().ShowTips(i18n("world_complete_item_tip"))

					return

				if not var_8_1.canPurchase():
					pg.TipsMgr.GetInstance().ShowTips(i18n("buy_countLimit"))

					return

				;(var_8_2 > 1 and arg_5_0.multiWindow or arg_5_0.singleWindow).ExecuteAction("Open", var_8_1, function(arg_11_0, arg_11_1)
					arg_5_0.emit(WorldShopMediator.BUY_ITEM, arg_11_0.id, arg_11_1)), SFX_PANEL))
	arg_5_0.AddWorldListener()

	local var_5_0 = nowWorld()

	arg_5_0.updateGoods(None, None, var_5_0.GetWorldShopGoodsDictionary())

	local var_5_1 = var_5_0.IsReseted()

	setActive(arg_5_0.rtResetTime, var_5_1)
	setActive(arg_5_0.rtResetTip, not var_5_1)
	setText(arg_5_0.rtResetTime.Find("number"), math.floor(var_5_0.GetResetWaitingTime() / 86400))
	setText(arg_5_0.rtResetTip.Find("info"), i18n("world_shop_preview_tip"))

	if var_5_1:
		WorldGuider.GetInstance().PlayGuide("WorldG180")

def var_0_0.onBackPressed(arg_12_0):
	if arg_12_0.singleWindow.isShowing():
		arg_12_0.singleWindow.Close()

		return

	if arg_12_0.multiWindow.isShowing():
		arg_12_0.multiWindow.Close()

		return

	pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_CANCEL)
	triggerButton(arg_12_0.btnBack)

def var_0_0.willExit(arg_13_0):
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_13_0._tf)
	arg_13_0.RemoveWorldListener()
	arg_13_0.singleWindow.Destroy()
	arg_13_0.multiWindow.Destroy()

def var_0_0.setPlayer(arg_14_0, arg_14_1):
	arg_14_0.player = arg_14_1

	GetImageSpriteFromAtlasAsync(Drop.New({
		type = DROP_TYPE_RESOURCE,
		id = WorldConst.ResourceID
	}).getIcon(), "", arg_14_0.rtRes.Find("icon"), True)
	setText(arg_14_0.rtRes.Find("number"), arg_14_0.player.getResource(WorldConst.ResourceID))

def var_0_0.AddWorldListener(arg_15_0):
	nowWorld().AddListener(World.EventUpdateShopGoods, arg_15_0.onUpdateGoods)

def var_0_0.RemoveWorldListener(arg_16_0):
	nowWorld().RemoveListener(World.EventUpdateShopGoods, arg_16_0.onUpdateGoods)

def var_0_0.updateGoods(arg_17_0, arg_17_1, arg_17_2, arg_17_3):
	local var_17_0 = pg.TimeMgr.GetInstance()
	local var_17_1 = nowWorld()
	local var_17_2 = var_17_1.expiredTime
	local var_17_3 = var_17_1.GetTaskProxy()
	local var_17_4 = {}

	for iter_17_0, iter_17_1 in pairs(arg_17_3):
		if not var_17_0.inTime(pg.shop_template[iter_17_0].time) or not var_17_0.inTime(pg.shop_template[iter_17_0].time, var_17_2 - 1):
			-- block empty
		elif iter_17_0 == 100000 and not nowWorld().IsReseted():
			-- block empty
		elif pg.shop_template[iter_17_0].genre == ShopArgs.WorldCollection and iter_17_1 == 0 and var_17_3.getRecycleTask(pg.shop_template[iter_17_0].effect_args[2]):
			-- block empty
		else
			table.insert(var_17_4, {
				id = iter_17_0,
				count = iter_17_1
			})

	table.sort(var_17_4, CompareFuncs({
		function(arg_18_0)
			return pg.shop_template[arg_18_0.id].order,
		function(arg_19_0)
			return arg_19_0.id
	}))

	arg_17_0.goodsList = var_17_4

	arg_17_0.goodsItemList.align(#arg_17_0.goodsList)

return var_0_0
