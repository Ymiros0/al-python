local var_0_0 = class("AnniversaryIslandSpringTaskSubmitWindow", import("view.base.BaseUI"))

function var_0_0.getUIName(arg_1_0)
	return "AnniversaryIslandSpringTaskSubmitWindow"
end

function var_0_0.init(arg_2_0)
	setText(arg_2_0._tf:Find("Content/Tips"), i18n("sub_item_warning"))
end

function var_0_0.didEnter(arg_3_0)
	onButton(arg_3_0, arg_3_0._tf:Find("BG"), function()
		arg_3_0:onBackPressed()
	end)
	onButton(arg_3_0, arg_3_0._tf:Find("Content/Cancel"), function()
		arg_3_0:onBackPressed()
	end, SFX_CANCEL)
	onButton(arg_3_0, arg_3_0._tf:Find("Content/Submit"), function()
		arg_3_0:emit(AnniversaryIslandSpringTask2023Mediator.SUBMIT_TASK)
	end, SFX_CONFIRM)

	local var_3_0 = arg_3_0.contextData.task
	local var_3_1 = {
		{
			type = tonumber(var_3_0:getConfig("target_id")),
			id = tonumber(var_3_0:getConfig("target_id_2")),
			count = var_3_0:getConfig("target_num")
		}
	}

	UIItemList.StaticAlign(arg_3_0._tf:Find("Content/Icons"), arg_3_0._tf:Find("Content/Icons"):GetChild(0), #var_3_1, function(arg_7_0, arg_7_1, arg_7_2)
		if arg_7_0 ~= UIItemList.EventUpdate then
			return
		end

		local var_7_0 = var_3_1[arg_7_1 + 1]

		updateDrop(arg_7_2:Find("Mask/IconTpl"), var_7_0)
		onButton(arg_3_0, arg_7_2, function()
			if var_7_0.type == DROP_TYPE_WORKBENCH_DROP then
				arg_3_0:emit(WorkBenchItemDetailMediator.SHOW_DETAIL, WorkBenchItem.New({
					configId = var_7_0.id,
					count = var_7_0.count
				}))
			else
				arg_3_0:emit(BaseUI.ON_DROP, var_7_0)
			end
		end)
	end)
end

function var_0_0.willExit(arg_9_0)
	return
end

return var_0_0
