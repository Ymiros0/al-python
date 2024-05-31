local var_0_0 = class("WorldMediaCollectionTemplateLayer", import("view.base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	assert(False, "Need Assign UIName " .. arg_1_0.__cname)

def var_0_0.Ctor(arg_2_0, arg_2_1, ...):
	var_0_0.super.Ctor(arg_2_0, ...)

	arg_2_0.viewParent = arg_2_1
	arg_2_0.buffer = setmetatable({}, {
		def __index:(arg_3_0, arg_3_1)
			return function(arg_4_0, ...)
				arg_2_0.ActionInvoke(arg_3_1, ...),
		def __newindex:()
			errorMsg("Cant write Data in ActionInvoke buffer")
	})

def var_0_0.Show(arg_6_0):
	var_0_0.super.Show(arg_6_0)

	if arg_6_0._top:
		arg_6_0.viewParent.Add2TopContainer(arg_6_0._top)

def var_0_0.Hide(arg_7_0):
	if arg_7_0._top:
		setParent(arg_7_0._top, arg_7_0._tf)

	var_0_0.super.Hide(arg_7_0)

def var_0_0.OnSelected(arg_8_0):
	arg_8_0.Show()

def var_0_0.OnReselected(arg_9_0):
	return

def var_0_0.OnDeselected(arg_10_0):
	arg_10_0.Hide()

def var_0_0.OnBackward(arg_11_0):
	return

def var_0_0.Add2LayerContainer(arg_12_0, arg_12_1):
	setParent(arg_12_1, arg_12_0._tf)

def var_0_0.Add2TopContainer(arg_13_0, arg_13_1):
	setParent(arg_13_1, arg_13_0._top)

def var_0_0.SetActive(arg_14_0, arg_14_1):
	if arg_14_1:
		arg_14_0.Show()
	else
		arg_14_0.Hide()

def var_0_0.UpdateView(arg_15_0):
	return

return var_0_0
