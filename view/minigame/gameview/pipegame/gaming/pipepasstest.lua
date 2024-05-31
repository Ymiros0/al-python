local var_0_0 = class("PipePassTest")
local var_0_1

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3)
	var_0_1 = PipeGameVo
	arg_1_0._tf = arg_1_1
	arg_1_0._leftId = 1
	arg_1_0._rightId = 1
	arg_1_0._leftIndex = 1
	arg_1_0._rightIndex = 2
	arg_1_0._leftDirect = {
		0,
		0
	}
	arg_1_0._rightDirect = {
		0,
		0
	}
	arg_1_0._leftTrigger = GetOrAddComponent(findTF(arg_1_0._tf, "left/ok"), typeof(EventTriggerListener))

	arg_1_0._leftTrigger:AddPointClickFunc(function()
		arg_1_0._leftId = tonumber(GetComponent(findTF(arg_1_0._tf, "left/inputId"), typeof(Text)).text)
		arg_1_0._leftIndex = tonumber(GetComponent(findTF(arg_1_0._tf, "left/inputIndex"), typeof(Text)).text)

		local var_2_0 = PipeGameConst.map_item_data[arg_1_0._leftId]

		arg_1_0._leftDirect = var_2_0.direct

		setImageSprite(findTF(arg_1_0._tf, "left/icon"), var_0_1.GetSprite(var_2_0.img), false)
	end)

	arg_1_0._rightTrigger = GetOrAddComponent(findTF(arg_1_0._tf, "right/ok"), typeof(EventTriggerListener))

	arg_1_0._rightTrigger:AddPointClickFunc(function()
		arg_1_0._rightId = tonumber(GetComponent(findTF(arg_1_0._tf, "right/inputId"), typeof(Text)).text)
		arg_1_0._rightIndex = tonumber(GetComponent(findTF(arg_1_0._tf, "right/inputIndex"), typeof(Text)).text)

		local var_3_0 = PipeGameConst.map_item_data[arg_1_0._rightId]

		arg_1_0._rightDirect = var_3_0.direct

		setImageSprite(findTF(arg_1_0._tf, "right/icon"), var_0_1.GetSprite(PipeGameConst.map_item_data[arg_1_0._rightId].img), false)
	end)

	arg_1_0._passTrigger = GetOrAddComponent(findTF(arg_1_0._tf, "btnPass"), typeof(EventTriggerListener))

	arg_1_0._passTrigger:AddPointClickFunc(function()
		if callback then
			callback(arg_1_0._leftIndex, arg_1_0._rightIndex, arg_1_0._leftDirect, arg_1_0._rightDirect)
		end
	end)
end

function var_0_0.setPassDesc(arg_5_0, arg_5_1)
	if arg_5_1 then
		setText(findTF(arg_5_0._tf, "passDesc"), "检测通过")
	else
		setText(findTF(arg_5_0._tf, "passDesc"), "检测失败")
	end
end

function var_0_0.setVisible(arg_6_0, arg_6_1)
	setActive(arg_6_0._tf, arg_6_1)
end

function var_0_0.dispose(arg_7_0)
	ClearEventTrigger(arg_7_0._leftTrigger)
	ClearEventTrigger(arg_7_0._rightTrigger)
end

return var_0_0
