local var_0_0 = class("WSPortTaskDetail", import("...BaseEntity"))

var_0_0.Fields = {
	task = "table",
	onCancel = "function",
	transform = "userdata"
}

function var_0_0.Setup(arg_1_0)
	pg.DelegateInfo.New(arg_1_0)
	arg_1_0:Init()
end

function var_0_0.Dispose(arg_2_0)
	pg.DelegateInfo.Dispose(arg_2_0)
	arg_2_0:Clear()
end

function var_0_0.Init(arg_3_0)
	local var_3_0 = arg_3_0.transform

	onButton(arg_3_0, var_3_0, function()
		arg_3_0.onCancel()
	end, SFX_CANCEL)
	onButton(arg_3_0, var_3_0:Find("top/btnBack"), function()
		arg_3_0.onCancel()
	end, SFX_CANCEL)
end

function var_0_0.UpdateTask(arg_6_0, arg_6_1)
	arg_6_0.task = arg_6_1

	local var_6_0 = arg_6_0.transform

	setText(var_6_0:Find("window/desc"), arg_6_1.config.description)

	local var_6_1 = arg_6_1:GetDisplayDrops()
	local var_6_2 = var_6_0:Find("window/scrollview/list")
	local var_6_3 = var_6_0:Find("window/scrollview/item")
	local var_6_4 = UIItemList.New(var_6_2, var_6_3)

	var_6_4:make(function(arg_7_0, arg_7_1, arg_7_2)
		if arg_7_0 == UIItemList.EventUpdate then
			local var_7_0 = var_6_1[arg_7_1 + 1]

			updateDrop(arg_7_2, var_7_0)
			setScrollText(arg_7_2:Find("name_mask/name"), var_7_0:getConfig("name"))
		end
	end)
	var_6_4:align(#var_6_1)
end

return var_0_0
