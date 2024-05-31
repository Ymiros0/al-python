local var_0_0 = class("SupplyShopBuilding", import(".NavalAcademyBuilding"))

def var_0_0.GetGameObjectName(arg_1_0):
	return "supplyShop"

def var_0_0.GetTitle(arg_2_0):
	return i18n("school_title_shangdian")

def var_0_0.OnClick(arg_3_0):
	arg_3_0.emit(NavalAcademyMediator.ON_OPEN_SUPPLYSHOP)

def var_0_0.IsTip(arg_4_0):
	local var_4_0 = getProxy(ShopsProxy).getShopStreet()

	return var_4_0 and var_4_0.isUpdateGoods()

return var_0_0
