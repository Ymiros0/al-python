local var_0_0 = class("MedalShopPurchasePanel", import(".GuildShopPurchasePanel"))

def var_0_0.getUIName(arg_1_0):
	return "MedalShopPurchaseMsgUI"

def var_0_0.OnConfirm(arg_2_0):
	arg_2_0.emit(NewShopsMediator.ON_MEDAL_SHOPPING, arg_2_0.data.id, arg_2_0.selectedList)

return var_0_0
