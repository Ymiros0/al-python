local var_0_0 = import(".DynamicCellView")
local var_0_1 = import(".SpineCellView")
local var_0_2 = class("FleetCellView", DecorateClass(var_0_0, var_0_1))

def var_0_2.Ctor(arg_1_0, arg_1_1):
	var_0_2.super.Ctor(arg_1_0, arg_1_1)
	var_0_1.Ctor(arg_1_0)
	var_0_1.InitCellTransform(arg_1_0)

	arg_1_0.tfArrow = arg_1_0.tf.Find("arrow")
	arg_1_0.tfAmmo = arg_1_0.tf.Find("ammo")
	arg_1_0.tfAmmoText = arg_1_0.tfAmmo.Find("text")
	arg_1_0.tfOp = arg_1_0.tf.Find("op")
	arg_1_0.tfIconRecorded = None
	arg_1_0.RecordedFlag = None

def var_0_2.GetOrder(arg_2_0):
	return ChapterConst.CellPriorityFleet

def var_0_2.showPoisonDamage(arg_3_0, arg_3_1):
	local var_3_0 = "dexiv4_SLG_poison"
	local var_3_1 = arg_3_0.tfShip.localPosition

	arg_3_0.GetLoader().GetPrefab("ui/" .. var_3_0, var_3_0, function(arg_4_0)
		setParent(arg_4_0.transform, arg_3_0.tf, False)
		LeanTween.moveY(arg_3_0.tfShip, var_3_1.y - 10, 0.1).setEase(LeanTweenType.easeInOutSine).setLoopPingPong()

		local var_4_0 = arg_4_0.GetComponent(typeof(ParticleSystemEvent))

		if not IsNil(var_4_0):
			var_4_0.AddEndEvent(function()
				arg_3_0.tfShip.localPosition = var_3_1

				arg_3_0.loader.ClearRequest("PoisonDamage")
				LeanTween.cancel(arg_3_0.tfShip.gameObject)

				if arg_3_1:
					arg_3_1()), "PoisonDamage")

def var_0_2.SetActiveNoPassIcon(arg_6_0, arg_6_1):
	local var_6_0 = "NoPassIcon"

	if not arg_6_1:
		if arg_6_0.loader:
			arg_6_0.loader.ClearRequest(var_6_0)
	else
		if arg_6_0.GetLoader().GetRequestPackage(var_6_0):
			return

		local var_6_1 = "event_task_small"

		arg_6_0.GetLoader().GetPrefabBYStopLoading("boxprefab/" .. var_6_1, var_6_1, function(arg_7_0)
			setParent(arg_7_0.transform, arg_6_0.tf, False)

			local var_7_0 = 150

			setLocalPosition(arg_7_0, Vector3(0, var_7_0, 0))
			LeanTween.moveY(rtf(arg_7_0), var_7_0 - 10, 1).setEase(LeanTweenType.easeInOutSine).setLoopPingPong(), var_6_0)

def var_0_2.UpdateIconRecordedFlag(arg_8_0, arg_8_1):
	arg_8_0.RecordedFlag = arg_8_1

	arg_8_0.UpdateIconRecorded()

def var_0_2.UpdateIconRecorded(arg_9_0):
	if not (arg_9_0.RecordedFlag and arg_9_0.visible):
		if not IsNil(arg_9_0.tfIconRecorded):
			setActive(arg_9_0.tfIconRecorded, False)
	else
		if IsNil(arg_9_0.tfIconRecorded):
			pg.PoolMgr.GetInstance().GetPrefab("effect/fleet_status_recorded", "", False, function(arg_10_0)
				arg_9_0.tfIconRecorded = tf(arg_10_0)

				setParent(arg_10_0, arg_9_0.tf, False))

		setActive(arg_9_0.tfIconRecorded, True)

def var_0_2.TweenShining(arg_11_0):
	local var_11_0 = arg_11_0.GetSpineRole()

	if not var_11_0:
		return

	local var_11_1 = Color.black
	local var_11_2 = Color.gray

	var_11_1.a = 0
	var_11_2.a = 0

	var_11_0.TweenShining(0.2, 2, 0, 1, var_11_1, var_11_2, True, True)

def var_0_2.SetSpineVisible(arg_12_0, arg_12_1):
	arg_12_0.visible = arg_12_1

	var_0_2.super.SetSpineVisible(arg_12_0, arg_12_1)
	setActive(arg_12_0.tfShadow, arg_12_1)
	arg_12_0.UpdateIconRecorded()

def var_0_2.StopTween(arg_13_0):
	local var_13_0 = arg_13_0.GetSpineRole()

	if not var_13_0:
		return

	var_13_0.StopTweenShining()

def var_0_2.unloadSpine(arg_14_0):
	var_0_2.super.UnloadSpine(arg_14_0)

def var_0_2.Clear(arg_15_0):
	var_0_1.ClearSpine(arg_15_0)
	var_0_2.super.Clear(arg_15_0)

return var_0_2
