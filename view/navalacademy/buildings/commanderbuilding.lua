local var_0_0 = class("CommanderBuilding", import(".NavalAcademyBuilding"))

function var_0_0.GetGameObjectName(arg_1_0)
	return "commander"
end

function var_0_0.GetTitle(arg_2_0)
	return i18n("school_title_zhihuimiao")
end

function var_0_0.OnClick(arg_3_0)
	arg_3_0:emit(NavalAcademyMediator.ON_OPEN_COMMANDER)
end

function var_0_0.IsTip(arg_4_0)
	if getProxy(PlayerProxy):getRawData().level < 40 then
		return false
	end

	local var_4_0 = getProxy(CommanderProxy):haveFinishedBox()

	if not LOCK_CATTERY then
		return var_4_0 or getProxy(CommanderProxy):AnyCatteryExistOP() or getProxy(CommanderProxy):AnyCatteryCanUse()
	else
		return var_4_0
	end
end

return var_0_0
