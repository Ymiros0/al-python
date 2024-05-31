local var_0_0 = import(".DynamicCellView")
local var_0_1 = import(".SpineCellView")
local var_0_2 = class("SubCellView", DecorateClass(var_0_0, var_0_1))

def var_0_2.Ctor(arg_1_0, arg_1_1):
	var_0_0.Ctor(arg_1_0, arg_1_1)
	var_0_1.Ctor(arg_1_0)
	var_0_1.InitCellTransform(arg_1_0)

	arg_1_0.tfAmmo = arg_1_0.tf.Find("ammo")
	arg_1_0.tfAmmoText = arg_1_0.tfAmmo.Find("text")
	arg_1_0.showFlag = True
	arg_1_0.shuihuaLoader = AutoLoader.New()

	arg_1_0.LoadEffectShuihua()

def var_0_2.GetOrder(arg_2_0):
	return ChapterConst.CellPriorityFleet

def var_0_2.OverrideCanvas(arg_3_0):
	var_0_2.super.OverrideCanvas(arg_3_0)

	arg_3_0.markCanvas = GetOrAddComponent(arg_3_0.tf.Find("mark"), typeof(Canvas))
	arg_3_0.markCanvas.overrideSorting = True

def var_0_2.ResetCanvasOrder(arg_4_0):
	var_0_2.super.ResetCanvasOrder(arg_4_0)

	if not arg_4_0.markCanvas:
		return

	local var_4_0 = arg_4_0.line.row * ChapterConst.PriorityPerRow + ChapterConst.CellPriorityTopMark

	pg.ViewUtils.SetSortingOrder(arg_4_0.markCanvas, var_4_0)

def var_0_2.LoadEffectShuihua(arg_5_0):
	local var_5_0 = "qianting_01"

	arg_5_0.shuihuaLoader.GetPrefab("Effect/" .. var_5_0, var_5_0, function(arg_6_0)
		arg_5_0.effect_shuihua = arg_6_0

		tf(arg_6_0).SetParent(arg_5_0.tf)

		tf(arg_6_0).localPosition = Vector3.zero

		setActive(arg_6_0, False), "Shuihua")

def var_0_2.PlayShuiHua(arg_7_0):
	if not arg_7_0.effect_shuihua:
		return

	setActive(arg_7_0.effect_shuihua, False)
	setActive(arg_7_0.effect_shuihua, True)

def var_0_2.SetActive(arg_8_0, arg_8_1):
	arg_8_0.SetActiveModel(arg_8_1)

def var_0_2.SetActiveModel(arg_9_0, arg_9_1):
	setActive(arg_9_0.tfShadow, arg_9_1)
	arg_9_0.SetSpineVisible(arg_9_1)

def var_0_2.Clear(arg_10_0):
	arg_10_0.showFlag = None

	arg_10_0.shuihuaLoader.Clear()
	var_0_1.ClearSpine(arg_10_0)
	var_0_0.Clear(arg_10_0)

return var_0_2
