local var_0_0 = class("CanteenBuiding", import(".NavalAcademyUpgradableBuilding"))

def var_0_0.GetGameObjectName(arg_1_0):
	return "canteen"

def var_0_0.GetTitle(arg_2_0):
	return i18n("school_title_shitang")

def var_0_0.OnClick(arg_3_0):
	arg_3_0.emit(NavalAcademyMediator.ON_OPEN_OILRESFIELD)

def var_0_0.GetResField(arg_4_0):
	return arg_4_0.parent.oilResField

return var_0_0
