﻿local var_0_0 = class("FountainBuiding", import(".NavalAcademyBuilding"))

function var_0_0.GetGameObjectName(arg_1_0)
	return "fountain"
end

function var_0_0.GetTitle(arg_2_0)
	return i18n("school_title_shoucang")
end

function var_0_0.OnClick(arg_3_0)
	arg_3_0:emit(NavalAcademyMediator.ON_OPEN_COLLECTION)
end

function var_0_0.IsTip(arg_4_0)
	return getProxy(CollectionProxy):unclaimTrophyCount() > 0
end

return var_0_0
