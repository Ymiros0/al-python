ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = require("Mgr/Pool/PoolUtil")

var_0_0.Battle.BattlePopNum = class("BattlePopNum")
var_0_0.Battle.BattlePopNum.__name = "BattlePopNum"

local var_0_3 = var_0_0.Battle.BattlePopNum

var_0_3.NUM_INIT_OFFSET = Vector3(0, 1.6, 0)

local var_0_4 = Vector3(10000, 10000)
local var_0_5 = Vector2(1, 1)

def var_0_3.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.bundle = arg_1_2.bundle
	arg_1_0.pool = arg_1_1

	local var_1_0 = Object.Instantiate(arg_1_2.template)

	arg_1_0._go = var_1_0
	arg_1_0._tf = var_1_0.transform

	arg_1_0.SetParent(arg_1_2.parentTF)

	arg_1_0._animator = var_1_0.GetComponent(typeof(Animator))

	local var_1_1 = arg_1_0._tf.Find("text")

	if var_1_1:
		arg_1_0.textCom = var_1_1.GetComponent(typeof(Text))

	var_1_0.GetComponent(typeof(DftAniEvent)).SetEndEvent(function(arg_2_0)
		arg_1_1.Recycle(arg_1_0))

	arg_1_0._offsetVector = Vector3.zero

def var_0_3.SetParent(arg_3_0, arg_3_1):
	arg_3_0._tf.SetParent(arg_3_1, False)

def var_0_3.SetText(arg_4_0, arg_4_1):
	arg_4_0.textCom.text = tostring(arg_4_1)

def var_0_3.SetReferenceCharacter(arg_5_0, arg_5_1, arg_5_2):
	arg_5_0._offsetVector.x = arg_5_2.x

	local var_5_0 = arg_5_1.GetReferenceVector(arg_5_0._offsetVector)

	var_5_0.Add(var_0_3.NUM_INIT_OFFSET)

	arg_5_0._tf.position = var_5_0

def var_0_3.Play(arg_6_0):
	arg_6_0._animator.enabled = True

def var_0_3.SetScale(arg_7_0, arg_7_1):
	arg_7_0._tf.localScale = Vector2(arg_7_1, arg_7_1)

def var_0_3.Init(arg_8_0):
	arg_8_0._go.SetActive(True)

def var_0_3.Recycle(arg_9_0):
	arg_9_0._animator.enabled = False
	arg_9_0._tf.position = var_0_4
	arg_9_0._tf.localScale = var_0_5

def var_0_3.Dispose(arg_10_0):
	arg_10_0._go.SetActive(False)

	arg_10_0._go = None
	arg_10_0._tf = None
