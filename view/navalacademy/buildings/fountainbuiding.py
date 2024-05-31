local var_0_0 = class("FountainBuiding", import(".NavalAcademyBuilding"))

def var_0_0.GetGameObjectName(arg_1_0):
	return "fountain"

def var_0_0.GetTitle(arg_2_0):
	return i18n("school_title_shoucang")

def var_0_0.OnClick(arg_3_0):
	arg_3_0.emit(NavalAcademyMediator.ON_OPEN_COLLECTION)

def var_0_0.IsTip(arg_4_0):
	return getProxy(CollectionProxy).unclaimTrophyCount() > 0

return var_0_0
