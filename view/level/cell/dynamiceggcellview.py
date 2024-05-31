local var_0_0 = import(".DynamicCellView")
local var_0_1 = import(".EggCellView")
local var_0_2 = class("DynamicEggCellView", DecorateClass(var_0_0, var_0_1))

def var_0_2.Ctor(arg_1_0, arg_1_1):
	var_0_0.Ctor(arg_1_0, arg_1_1)
	var_0_1.Ctor(arg_1_0)
	var_0_1.InitEggCellTransform(arg_1_0)

def var_0_2.GetOrder(arg_2_0):
	return ChapterConst.CellPriorityEnemy

def var_0_2.SetActive(arg_3_0, arg_3_1):
	setActive(arg_3_0.go, arg_3_1)

def var_0_2.LoadIcon(arg_4_0, arg_4_1, arg_4_2, arg_4_3):
	if arg_4_0.lastPrefab == arg_4_1:
		existCall(arg_4_3)

		return

	arg_4_0.lastPrefab = arg_4_1

	var_0_1.StartEggCellView(arg_4_0, arg_4_2, arg_4_3)

def var_0_2.UpdateChampionCell(arg_5_0, arg_5_1, arg_5_2, arg_5_3):
	var_0_1.UpdateEggCell(arg_5_0, arg_5_1, arg_5_2, arg_5_2.getConfigTable(), arg_5_3)
	arg_5_0.RefreshLinePosition(arg_5_1, arg_5_2)

return var_0_2
