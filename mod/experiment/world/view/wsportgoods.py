local var_0_0 = class("WSPortGoods", import("...BaseEntity"))

var_0_0.Fields = {
	transform = "userdata",
	rtMask = "userdata",
	goods = "table",
	txName = "userdata",
	rtResIcon = "userdata",
	rtItem = "userdata",
	txCount = "userdata",
	rtResCount = "userdata"
}
var_0_0.Listeners = {
	onUpdate = "Update"
}

def var_0_0.Build(arg_1_0, arg_1_1):
	arg_1_0.transform = arg_1_1

def var_0_0.Setup(arg_2_0, arg_2_1):
	arg_2_0.goods = arg_2_1

	arg_2_0.goods.AddListener(WorldGoods.EventUpdateCount, arg_2_0.onUpdate)
	arg_2_0.Init()

def var_0_0.Dispose(arg_3_0):
	arg_3_0.goods.RemoveListener(WorldGoods.EventUpdateCount, arg_3_0.onUpdate)
	arg_3_0.Clear()

def var_0_0.Init(arg_4_0):
	local var_4_0 = arg_4_0.transform

	arg_4_0.rtMask = var_4_0.Find("mask")
	arg_4_0.rtItem = var_4_0.Find("IconTpl")
	arg_4_0.txCount = var_4_0.Find("count_contain/count")
	arg_4_0.txName = var_4_0.Find("name_mask/name")
	arg_4_0.rtResIcon = var_4_0.Find("consume/contain/icon")
	arg_4_0.rtResCount = var_4_0.Find("consume/contain/Text")

	setText(var_4_0.Find("mask/tag/sellout_tag"), i18n("word_sell_out"))
	setText(var_4_0.Find("count_contain/label"), i18n("activity_shop_exchange_count"))

	local var_4_1 = arg_4_0.goods.item

	updateDrop(arg_4_0.rtItem, var_4_1)
	setText(arg_4_0.txName, shortenString(var_4_1.getConfig("name"), 6))

	local var_4_2 = arg_4_0.goods.moneyItem

	GetImageSpriteFromAtlasAsync(var_4_2.getIcon(), "", arg_4_0.rtResIcon, False)
	setText(arg_4_0.rtResCount, var_4_2.count)
	arg_4_0.Update()

def var_0_0.Update(arg_5_0, arg_5_1):
	if arg_5_1 == None or arg_5_1 == WorldGoods.EventUpdateCount:
		setText(arg_5_0.txCount, arg_5_0.goods.count .. "/" .. arg_5_0.goods.config.frequency)
		setActive(arg_5_0.rtMask, arg_5_0.goods.count == 0)

return var_0_0
