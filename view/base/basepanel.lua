﻿local var_0_0 = class("BasePanel")

function var_0_0.Ctor(arg_1_0, arg_1_1)
	assert(arg_1_1)

	arg_1_0._go = arg_1_1
	arg_1_0._tf = arg_1_1.transform

	function arg_1_0.emit()
		assert(false, "can not emit event beforce attach to a parent ui.")
	end

	arg_1_0:init()
end

function var_0_0.init(arg_3_0)
	return
end

function var_0_0.attach(arg_4_0, arg_4_1)
	assert(arg_4_1)

	arg_4_0.exited = false
	arg_4_0.parent = arg_4_1
	arg_4_0.contextData = arg_4_1.contextData

	function arg_4_0.emit(arg_5_0, arg_5_1, ...)
		if arg_5_0.parent then
			arg_5_0.parent:emit(arg_5_1, ...)
		end
	end

	setActive(arg_4_0._go, true)
	pg.DelegateInfo.New(arg_4_0)
end

function var_0_0.detach(arg_6_0)
	if not arg_6_0.exited then
		setActive(arg_6_0._go, false)
		pg.DelegateInfo.Dispose(arg_6_0)
		arg_6_0:clear()

		arg_6_0.parent = nil
		arg_6_0.emit = nil
		arg_6_0.exited = true
	end
end

function var_0_0.findTF(arg_7_0, arg_7_1, arg_7_2)
	assert(arg_7_0._tf, "transform should exist")

	return findTF(arg_7_2 or arg_7_0._tf, arg_7_1)
end

function var_0_0.getTpl(arg_8_0, arg_8_1, arg_8_2)
	local var_8_0 = arg_8_0:findTF(arg_8_1, arg_8_2)

	var_8_0:SetParent(arg_8_0._tf, false)
	SetActive(var_8_0, false)

	return var_8_0
end

function var_0_0.clear(arg_9_0)
	return
end

return var_0_0
