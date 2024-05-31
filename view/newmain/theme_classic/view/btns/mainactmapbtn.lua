local var_0_0 = class("MainActMapBtn", import(".MainBaseActivityBtn"))

function var_0_0.GetEventName(arg_1_0)
	return "event_map"
end

function var_0_0.GetActivity(arg_2_0)
	local var_2_0 = getProxy(ActivityProxy):getActivitiesByType(ActivityConst.ACTIVITY_TYPE_ZPROJECT)

	return (_.detect(var_2_0, function(arg_3_0)
		return not arg_3_0:isEnd()
	end))
end

function var_0_0.GetActivityID(arg_4_0)
	local var_4_0 = arg_4_0:GetActivity()

	return var_4_0 and var_4_0.id
end

function var_0_0.OnInit(arg_5_0)
	local var_5_0 = getProxy(ChapterProxy):IsActivitySPChapterActive() and SettingsProxy.IsShowActivityMapSPTip()

	setActive(arg_5_0.tipTr.gameObject, var_5_0)
end

function var_0_0.CustomOnClick(arg_6_0)
	local var_6_0 = arg_6_0:GetActivity()

	if var_6_0 then
		arg_6_0:emit(NewMainMediator.SKIP_ACTIVITY_MAP, var_6_0.id)
	end
end

return var_0_0
