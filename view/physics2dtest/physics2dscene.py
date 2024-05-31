local var_0_0 = class("Physics2dScene", import("..base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "PhysicsTest"

def var_0_0.init(arg_2_0):
	arg_2_0._backBtn = arg_2_0.findTF("back_btn")
	arg_2_0._box = arg_2_0.findTF("box")
	arg_2_0._boxRig = GetComponent(arg_2_0._box, "Rigidbody2D")
	arg_2_0._boxPhyItem = GetComponent(arg_2_0._box, "Physics2DItem")

	Physics2DMgr.Inst.AddSimulateItem(arg_2_0._boxPhyItem)

	arg_2_0._gizmos = arg_2_0.findTF("res/gizmos")

def var_0_0.didEnter(arg_3_0):
	onButton(arg_3_0, arg_3_0._backBtn, function()
		arg_3_0.emit(var_0_0.ON_BACK))

	local var_3_0 = arg_3_0._tf.TransformPoint(Vector3(-578, -390))

	arg_3_0._boxRig.position = var_3_0

	arg_3_0._boxPhyItem.CollisionEnter.AddListener(function(arg_5_0)
		if Physics2D.autoSimulation:
			print("=========================")
			print(arg_5_0.collider.gameObject.name)
			print(arg_5_0.otherCollider.gameObject.name)

			if arg_5_0.collider.gameObject.name != "ground":
				LeanTween.scale(arg_5_0.collider.gameObject, Vector3(0, 0, 0), 1))
	onDelayTick(function()
		arg_3_0.simulateDrawPath(), 1)
	onDelayTick(function()
		arg_3_0.jump(), 3)

def var_0_0.jump(arg_8_0):
	local var_8_0 = arg_8_0._tf.TransformPoint(Vector3(-578, -390))

	arg_8_0._boxRig.position = var_8_0
	arg_8_0._boxRig.velocity = Vector2(10, 10)

def var_0_0.simulateDrawPath(arg_9_0):
	Physics2DMgr.Inst.DoPrediction(0.1, 50, function()
		arg_9_0.jump(), function()
		local var_11_0 = instantiate(arg_9_0._gizmos)

		setParent(tf(var_11_0), arg_9_0._tf, False)
		setAnchoredPosition(var_11_0, arg_9_0._tf.InverseTransformVector(arg_9_0._boxRig.position)))

def var_0_0.willExit(arg_12_0):
	Physics2DMgr.Inst.RemoveSimulateItem(arg_12_0._boxPhyItem)
	arg_12_0._boxPhyItem.CollisionEnter.RemoveAllListeners()

return var_0_0
