local var_0_0 = class("BaseEmptyListPage", import("..base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "TaskEmptyListUI"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0._tf.SetSiblingIndex(1)

def var_0_0.OnInit(arg_3_0):
	arg_3_0.isShowUI = False

def var_0_0.SetEmptyText(arg_4_0, arg_4_1):
	local var_4_0 = findTF(arg_4_0._tf, "Text")

	setText(var_4_0, arg_4_1)

def var_0_0.SetPosY(arg_5_0, arg_5_1):
	setAnchoredPosition(arg_5_0._tf, arg_5_1)

def var_0_0.ShowOrHide(arg_6_0, arg_6_1):
	if arg_6_0.isShowUI == arg_6_1:
		return

	if arg_6_1:
		arg_6_0.Show()
	else
		arg_6_0.Hide()

	arg_6_0.isShowUI = arg_6_1

return var_0_0
