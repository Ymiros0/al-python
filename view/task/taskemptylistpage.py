local var_0_0 = class("TaskEmptyListPage", import("..base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "TaskEmptyListUI"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0._tf.SetSiblingIndex(1)

	local var_2_0 = findTF(arg_2_0._tf, "Text")

	setText(var_2_0, i18n("list_empty_tip_taskscene"))

def var_0_0.OnInit(arg_3_0):
	arg_3_0.isShowUI = False

def var_0_0.ShowOrHide(arg_4_0, arg_4_1):
	if arg_4_0.isShowUI == arg_4_1:
		return

	if arg_4_1:
		arg_4_0.Show()
	else
		arg_4_0.Hide()

	arg_4_0.isShowUI = arg_4_1

return var_0_0
