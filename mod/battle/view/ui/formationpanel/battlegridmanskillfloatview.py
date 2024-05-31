ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig

var_0_0.Battle.BattleGridmanSkillFloatView = class("BattleGridmanSkillFloatView")
var_0_0.Battle.BattleGridmanSkillFloatView.__name = "BattleGridmanSkillFloatView"

local var_0_2 = var_0_0.Battle.BattleGridmanSkillFloatView

def var_0_2.Ctor(arg_1_0, arg_1_1):
	arg_1_0._go = arg_1_1
	arg_1_0._tf = tf(arg_1_1)

	arg_1_0.init()

def var_0_2.init(arg_2_0):
	arg_2_0._fusion = {}
	arg_2_0._fusion[var_0_1.FRIENDLY_CODE] = arg_2_0._tf.Find("fusion_1")
	arg_2_0._fusion[var_0_1.FOE_CODE] = arg_2_0._tf.Find("fusion_-1")
	arg_2_0._skillList = {}

	local function var_2_0(arg_3_0)
		arg_2_0._skillList[arg_3_0] = {}

		for iter_3_0 = 1, 3:
			local var_3_0 = iter_3_0 * arg_3_0
			local var_3_1 = arg_2_0._tf.Find("skill_" .. var_3_0)

			table.insert(arg_2_0._skillList[arg_3_0], {
				idle = True,
				tf = var_3_1
			})

	var_2_0(var_0_1.FRIENDLY_CODE)
	var_2_0(var_0_1.FOE_CODE)

	arg_2_0._resource = arg_2_0._tf.Find("res")

def var_0_2.DoSkillFloat(arg_4_0, arg_4_1, arg_4_2):
	local var_4_0
	local var_4_1 = arg_4_0._skillList[arg_4_2]

	for iter_4_0 = 1, 3:
		if var_4_1[iter_4_0].idle:
			var_4_0 = var_4_1[iter_4_0]

			break

	if not var_4_0:
		return

	var_4_0.idle = False

	local var_4_2 = var_4_0.tf
	local var_4_3 = var_4_2.Find("anima")
	local var_4_4 = arg_4_0._resource.Find(arg_4_1).GetComponent(typeof(Image)).sprite

	setImageSprite(var_4_3, var_4_4, True)
	setActive(var_4_2, True)
	var_4_3.GetComponent(typeof(DftAniEvent)).SetEndEvent(function(arg_5_0)
		var_4_0.idle = True

		setActive(var_4_2, False))

def var_0_2.DoFusionFloat(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_0._fusion[arg_6_1]

	setActive(var_6_0, True)
	var_6_0.Find("anima").GetComponent(typeof(DftAniEvent)).SetEndEvent(function(arg_7_0)
		setActive(var_6_0, False))

def var_0_2.Dispose(arg_8_0):
	return
