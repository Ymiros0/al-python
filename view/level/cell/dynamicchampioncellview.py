local var_0_0 = import(".DynamicCellView")
local var_0_1 = import(".ChampionCellView")
local var_0_2 = class("DynamicChampionCellView", DecorateClass(var_0_0, var_0_1))

def var_0_2.Ctor(arg_1_0, arg_1_1):
	var_0_0.Ctor(arg_1_0, arg_1_1)
	var_0_1.Ctor(arg_1_0)
	var_0_1.InitChampionCellTransform(arg_1_0)

def var_0_2.GetOrder(arg_2_0):
	return ChapterConst.CellPriorityEnemy

def var_0_2.SetActive(arg_3_0, arg_3_1):
	arg_3_0.SetActiveModel(arg_3_1)

def var_0_2.SetActiveModel(arg_4_0, arg_4_1):
	arg_4_0.SetSpineVisible(arg_4_1)
	setActive(arg_4_0.tfShadow, arg_4_1)

	for iter_4_0, iter_4_1 in pairs(arg_4_0._extraEffectList):
		if not IsNil(iter_4_1):
			setActive(iter_4_1, arg_4_1)

def var_0_2.PlayShuiHua():
	return

def var_0_2.UpdateChampionCell(arg_6_0, arg_6_1, arg_6_2, arg_6_3):
	var_0_1.UpdateChampionCell(arg_6_0, arg_6_1, arg_6_2, arg_6_3)
	arg_6_0.RefreshLinePosition(arg_6_1, arg_6_2)

def var_0_2.TweenShining(arg_7_0, arg_7_1):
	arg_7_0.StopTween()

	local var_7_0 = arg_7_0.GetSpineRole()

	if not var_7_0:
		return

	var_7_0.TweenShining(0.5, arg_7_1, 0, 1, Color.New(0, 0, 0, 0), Color.New(1, 1, 1, 1), True, True)

def var_0_2.StopTween(arg_8_0):
	if not arg_8_0.tweenId:
		return

	LeanTween.cancel(arg_8_0.tweenId, True)

	arg_8_0.tweenId = None

def var_0_2.Clear(arg_9_0):
	arg_9_0.StopTween()

	if arg_9_0.go:
		LeanTween.cancel(arg_9_0.go)

	var_0_1.Clear(arg_9_0)

return var_0_2
