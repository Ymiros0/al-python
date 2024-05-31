local var_0_0 = class("ShopBuiding", import(".NavalAcademyUpgradableBuilding"))

def var_0_0.GetGameObjectName(arg_1_0):
	return "shop"

def var_0_0.GetTitle(arg_2_0):
	return i18n("school_title_xiaomaibu")

def var_0_0.OnClick(arg_3_0):
	arg_3_0.emit(NavalAcademyMediator.ON_OPEN_GOLDRESFIELD)

def var_0_0.GetResField(arg_4_0):
	return arg_4_0.parent.goldResField

return var_0_0
