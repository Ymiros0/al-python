local var_0_0 = class("AttachmentSpineAnimationCell", import(".StaticCellView"))

var_0_0.SDPosition = Vector2(0, -15)
var_0_0.SDScale = Vector3(0.4, 0.4, 0.4)

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.name = None
	arg_1_0.model = None
	arg_1_0.anim = None
	arg_1_0.AnimIndex = None
	arg_1_0.group = {}
	arg_1_0.timer = None

def var_0_0.GetOrder(arg_2_0):
	return ChapterConst.CellPriorityAttachment

def var_0_0.Set(arg_3_0, arg_3_1):
	if arg_3_0.name == arg_3_1:
		return

	arg_3_0.ClearLoader()
	table.clear(arg_3_0.group)

	arg_3_0.name = arg_3_1

	if IsNil(arg_3_0.go):
		arg_3_0.PrepareBase("SD")
		arg_3_0.OverrideCanvas()
		arg_3_0.ResetCanvasOrder()

	arg_3_0.GetLoader().GetSpine(arg_3_1, function(arg_4_0)
		arg_3_0.model = arg_4_0
		arg_3_0.anim = arg_4_0.GetComponent("SpineAnimUI")

		setParent(arg_4_0, arg_3_0.go)

		arg_4_0.transform.anchoredPosition = arg_3_0.SDPosition
		arg_4_0.transform.localScale = arg_3_0.SDScale

		arg_3_0.PlayAction(arg_3_0.AnimIndex), "SD")

def var_0_0.SetRoutine(arg_5_0, arg_5_1):
	table.clear(arg_5_0.group)

	arg_5_0.AnimIndex = None

	for iter_5_0, iter_5_1 in ipairs(arg_5_1 or {}):
		arg_5_0.group[iter_5_0] = iter_5_1

	if #arg_5_0.group < 1:
		table.insert(arg_5_0.group, {
			action = "default",
			duration = 9999
		})

	arg_5_0.PlayAction(math.min(#arg_5_0.group, 1))

def var_0_0.PlayAction(arg_6_0, arg_6_1):
	if not arg_6_1 or arg_6_1 <= 0 or arg_6_1 > #arg_6_0.group or arg_6_0.AnimIndexPlaying == arg_6_1:
		return

	arg_6_0.AnimIndex = arg_6_1

	if not arg_6_0.loader or arg_6_0.loader.GetLoadingRP("SD") or not arg_6_0.anim:
		return

	local var_6_0 = arg_6_0.group[arg_6_1]

	arg_6_0.ClearTimer()

	arg_6_0.timer = Timer.New(function()
		arg_6_1 = arg_6_1 + 1

		if arg_6_1 > #arg_6_0.group:
			arg_6_1 = math.min(#arg_6_0.group, 1)

		arg_6_0.PlayAction(arg_6_1), var_6_0.duration)

	arg_6_0.anim.SetAction(var_6_0.action, 0)
	arg_6_0.timer.Start()

	arg_6_0.AnimIndexPlaying = arg_6_1

def var_0_0.ClearTimer(arg_8_0):
	if arg_8_0.timer:
		arg_8_0.timer.Stop()

		arg_8_0.timer = None

def var_0_0.Clear(arg_9_0):
	arg_9_0.ClearTimer()

	arg_9_0.name = None

	var_0_0.super.Clear(arg_9_0)

return var_0_0