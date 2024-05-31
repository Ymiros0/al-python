local var_0_0 = class("ValentineQteGameItem")
local var_0_1 = {
	"1",
	"2",
	"3",
	"4",
	"5",
	"6"
}

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	arg_1_0._go = arg_1_1
	arg_1_0._tf = arg_1_1.transform
	arg_1_0.rect = arg_1_0._tf.rect
	arg_1_0.image = arg_1_0._go.GetComponent(typeof(Image))

	arg_1_0.SetTime(arg_1_3)
	arg_1_0.SetPosition(arg_1_2)

	arg_1_0.bound = getBounds(arg_1_0._tf)

	local var_1_0 = math.random(1, #var_0_1)
	local var_1_1 = GetSpriteFromAtlas("ui/valentineqtegame_atlas", var_0_1[var_1_0])

	arg_1_0.image.sprite = var_1_1

	arg_1_0.image.SetNativeSize()

def var_0_0.SetTime(arg_2_0, arg_2_1):
	arg_2_0.genTime = arg_2_1

def var_0_0.SetPosition(arg_3_0, arg_3_1):
	arg_3_0.genPos = arg_3_1
	arg_3_0._tf.localPosition = arg_3_1

def var_0_0.ShouldDisapper(arg_4_0, arg_4_1):
	if arg_4_0.genTime - arg_4_1 >= ValentineQteGameConst.ITEM_DISAPPEAR_TIME:
		return True

	return False

def var_0_0.IsOverlap(arg_5_0, arg_5_1):
	local var_5_0 = getBounds(arg_5_1)

	return arg_5_0.bound.Intersects(var_5_0)

def var_0_0.IsSufficientLength(arg_6_0, arg_6_1, arg_6_2):
	return arg_6_2 < math.abs(arg_6_0._tf.localPosition.x - arg_6_1)

def var_0_0.Destroy(arg_7_0):
	arg_7_0.image.sprite = None

return var_0_0
