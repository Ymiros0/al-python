ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleBuffEvent
local var_0_2 = var_0_0.Battle.BattleUnitEvent
local var_0_3 = var_0_0.Battle.BattleResourceManager
local var_0_4 = var_0_0.Battle.BattleDataFunction

var_0_0.Battle.BattleEffectComponent = class("BattleEffectComponent")

local var_0_5 = var_0_0.Battle.BattleEffectComponent

var_0_5.__name = "BattleEffectComponent"

def var_0_5.Ctor(arg_1_0, arg_1_1):
	var_0_0.EventListener.AttachEventListener(arg_1_0)

	arg_1_0._owner = arg_1_1
	arg_1_0._blinkIDList = {}
	arg_1_0._buffLastEffects = {}
	arg_1_0._effectIndex = 0
	arg_1_0._effectList = {}

def var_0_5.SwitchOwner(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0._owner = arg_2_1

	for iter_2_0, iter_2_1 in pairs(arg_2_0._blinkIDList):
		if arg_2_2[iter_2_1]:
			arg_2_0._blinkIDList[iter_2_0] = arg_2_2[iter_2_1]

def var_0_5.ClearEffect(arg_3_0):
	for iter_3_0, iter_3_1 in pairs(arg_3_0._blinkIDList):
		arg_3_0._owner.RemoveBlink(iter_3_1)

	arg_3_0._blinkIDList = {}

def var_0_5.Dispose(arg_4_0):
	for iter_4_0, iter_4_1 in pairs(arg_4_0._blinkIDList):
		arg_4_0._owner.RemoveBlink(iter_4_1)

	arg_4_0._effectList = None
	arg_4_0._buffLastEffects = None

	var_0_0.EventListener.DetachEventListener(arg_4_0)

def var_0_5.GetFXPool(arg_5_0):
	return var_0_0.Battle.BattleFXPool.GetInstance()

def var_0_5.SetUnitDataEvent(arg_6_0, arg_6_1):
	arg_6_1.RegisterEventListener(arg_6_0, var_0_1.BUFF_CAST, arg_6_0.onBuffCast)
	arg_6_1.RegisterEventListener(arg_6_0, var_0_1.BUFF_ATTACH, arg_6_0.onBuffAdd)
	arg_6_1.RegisterEventListener(arg_6_0, var_0_1.BUFF_STACK, arg_6_0.onBuffStack)
	arg_6_1.RegisterEventListener(arg_6_0, var_0_1.BUFF_REMOVE, arg_6_0.onBuffRemove)
	arg_6_1.RegisterEventListener(arg_6_0, var_0_2.ADD_EFFECT, arg_6_0.onAddEffect)
	arg_6_1.RegisterEventListener(arg_6_0, var_0_2.CANCEL_EFFECT, arg_6_0.onCancelEffect)
	arg_6_1.RegisterEventListener(arg_6_0, var_0_2.DEACTIVE_EFFECT, arg_6_0.onDeactiveEffect)

def var_0_5.RemoveUnitEvent(arg_7_0, arg_7_1):
	arg_7_1.UnregisterEventListener(arg_7_0, var_0_1.BUFF_ATTACH)
	arg_7_1.UnregisterEventListener(arg_7_0, var_0_1.BUFF_CAST)
	arg_7_1.UnregisterEventListener(arg_7_0, var_0_1.BUFF_STACK)
	arg_7_1.UnregisterEventListener(arg_7_0, var_0_1.BUFF_REMOVE)
	arg_7_1.UnregisterEventListener(arg_7_0, var_0_2.ADD_EFFECT)
	arg_7_1.UnregisterEventListener(arg_7_0, var_0_2.CANCEL_EFFECT)
	arg_7_1.UnregisterEventListener(arg_7_0, var_0_2.DEACTIVE_EFFECT)

def var_0_5.Update(arg_8_0, arg_8_1):
	arg_8_0._dir = arg_8_0._owner.GetUnitData().GetDirection()

	for iter_8_0, iter_8_1 in pairs(arg_8_0._effectList):
		iter_8_1.currentTime = arg_8_1 - iter_8_1.startTime

		arg_8_0.updateEffect(iter_8_1)

def var_0_5.onAddEffect(arg_9_0, arg_9_1):
	local var_9_0 = arg_9_1.Data

	arg_9_0.addEffect(var_9_0)

def var_0_5.onCancelEffect(arg_10_0, arg_10_1):
	local var_10_0 = arg_10_1.Data

	arg_10_0.cancelEffect(var_10_0)

def var_0_5.onDeactiveEffect(arg_11_0, arg_11_1):
	local var_11_0 = arg_11_1.Data

	arg_11_0.deactiveEffect(var_11_0)

def var_0_5.onBuffAdd(arg_12_0, arg_12_1):
	arg_12_0.DoWhenAddBuff(arg_12_1)

def var_0_5.onBuffCast(arg_13_0, arg_13_1):
	local var_13_0 = arg_13_1.Data.buff_id

	arg_13_0.addBlink(var_13_0)

def var_0_5.DoWhenAddBuff(arg_14_0, arg_14_1):
	local var_14_0 = arg_14_1.Data.buff_id
	local var_14_1 = arg_14_1.Data.buff_level

	arg_14_0.addInitFX(var_14_0)
	arg_14_0.addLastFX(var_14_0)

def var_0_5.onBuffStack(arg_15_0, arg_15_1):
	arg_15_0.DoWhenStackBuff(arg_15_1)

def var_0_5.DoWhenStackBuff(arg_16_0, arg_16_1):
	local var_16_0 = arg_16_1.Data.buff_id

	arg_16_0.addInitFX(var_16_0)

	local var_16_1 = var_0_0.Battle.BattleDataFunction.GetBuffTemplate(var_16_0)

	if var_16_1.last_effect != "" and var_16_1.last_effect_stack:
		local var_16_2 = arg_16_1.Data.stack_count
		local var_16_3 = #arg_16_0._buffLastEffects[var_16_0]

		if var_16_3 < var_16_2:
			arg_16_0.addLastFX(var_16_0)
		elif var_16_2 < var_16_3:
			local var_16_4 = var_16_3 - var_16_2

			while var_16_4 > 0:
				arg_16_0.removeLastFX(var_16_0)

				var_16_4 = var_16_4 - 1

def var_0_5.onBuffRemove(arg_17_0, arg_17_1):
	local var_17_0 = arg_17_1.Data.buff_id

	if arg_17_0._buffLastEffects[var_17_0]:
		local var_17_1 = #arg_17_0._buffLastEffects[var_17_0]

		while var_17_1 > 0:
			arg_17_0.removeLastFX(var_17_0)

			var_17_1 = var_17_1 - 1

	local var_17_2 = arg_17_0._blinkIDList[var_17_0]

	if var_17_2:
		arg_17_0._owner.RemoveBlink(var_17_2)

		arg_17_0._blinkIDList[var_17_0] = None

def var_0_5.addInitFX(arg_18_0, arg_18_1):
	local var_18_0 = var_0_0.Battle.BattleDataFunction.GetBuffTemplate(arg_18_1)

	if var_18_0.init_effect and var_18_0.init_effect != "":
		local var_18_1 = var_18_0.init_effect

		if var_18_0.skin_adapt:
			var_18_1 = var_0_4.SkinAdaptFXID(var_18_1, arg_18_0._owner.GetUnitData().GetSkinID())

		arg_18_0._owner.AddFX(var_18_1)

def var_0_5.removeLastFX(arg_19_0, arg_19_1):
	local var_19_0 = arg_19_0._buffLastEffects[arg_19_1]

	if var_19_0 != None and #var_19_0 > 0:
		local var_19_1 = table.remove(var_19_0)

		arg_19_0._owner.RemoveFX(var_19_1)

def var_0_5.addLastFX(arg_20_0, arg_20_1):
	local var_20_0 = var_0_0.Battle.BattleDataFunction.GetBuffTemplate(arg_20_1)

	if var_20_0.last_effect != None and var_20_0.last_effect != "":
		local var_20_1 = arg_20_0._owner.AddFX(var_20_0.last_effect)
		local var_20_2 = arg_20_0._buffLastEffects[arg_20_1] or {}

		table.insert(var_20_2, var_20_1)

		arg_20_0._buffLastEffects[arg_20_1] = var_20_2

		if var_20_0.last_effect_cld_scale or var_20_0.last_effect_cld_angle:
			local var_20_3
			local var_20_4 = var_20_0[buffLv] or var_20_0.effect_list

			for iter_20_0, iter_20_1 in ipairs(var_20_4):
				if iter_20_1.arg_list.cld_data:
					var_20_3 = iter_20_1

					break

			if var_20_3:
				if var_20_0.last_effect_cld_scale:
					local var_20_5 = var_20_3.arg_list.cld_data.box
					local var_20_6 = var_20_1.transform.localScale

					if var_20_5.range:
						var_20_6.x = var_20_6.x * var_20_5.range
						var_20_6.y = var_20_6.y * var_20_5.range
						var_20_6.z = var_20_6.z * var_20_5.range
					else
						var_20_6.x = var_20_6.x * var_20_5[1]
						var_20_6.y = var_20_6.y * var_20_5[2]
						var_20_6.z = var_20_6.z * var_20_5[3]

					var_20_1.transform.localScale = var_20_6

				if var_20_0.last_effect_cld_angle:
					local var_20_7 = var_20_3.arg_list.cld_data.angle
					local var_20_8 = var_20_1.transform.Find("scale/sector").GetComponent(typeof(Renderer)).material
					local var_20_9 = (360 - var_20_7) * 0.5 - 5

					var_20_8.SetInt("_AngleControl", var_20_9)

				if var_20_0.last_effect_bound_bone:
					local var_20_10 = arg_20_0._owner.GetBoneList()[var_20_0.last_effect_bound_bone]

					if var_20_10:
						var_20_1.transform.localPosition = var_20_10[1]

		var_20_1.SetActive(True)

def var_0_5.addBlink(arg_21_0, arg_21_1):
	local var_21_0 = var_0_0.Battle.BattleDataFunction.GetBuffTemplate(arg_21_1)

	if var_21_0.blink:
		local var_21_1 = var_21_0.blink
		local var_21_2 = arg_21_0._owner.AddBlink(var_21_1[1], var_21_1[2], var_21_1[3], var_21_1[4], var_21_1[5])

		arg_21_0._blinkIDList[arg_21_1] = var_21_2

def var_0_5.addEffect(arg_22_0, arg_22_1):
	local var_22_0 = arg_22_1.index or arg_22_0.getIndex()
	local var_22_1 = arg_22_0._effectList[var_22_0]

	if var_22_1:
		local var_22_2 = var_22_1.effect_tf.localScale

		var_22_1.effect_go.SetActive(True)

		var_22_1.effect_tf.localScale = var_22_2
	else
		local var_22_3 = arg_22_0._owner.AddFX(arg_22_1.effect)
		local var_22_4 = {
			currentTime = 0,
			effect_go = var_22_3,
			effect_tf = var_22_3.transform,
			posFun = arg_22_1.posFun,
			rotationFun = arg_22_1.rotationFun,
			startTime = pg.TimeMgr.GetInstance().GetCombatTime(),
			fillFunc = arg_22_1.fillFunc
		}

		arg_22_0._effectList[var_22_0] = var_22_4

		arg_22_0.updateEffect(var_22_4)
		pg.EffectMgr.GetInstance().PlayBattleEffect(var_22_3, var_22_3.transform.localPosition, False, function(arg_23_0)
			arg_22_0._owner.RemoveFX(var_22_3)

			arg_22_0._effectList[var_22_0] = None)

def var_0_5.cancelEffect(arg_24_0, arg_24_1):
	local var_24_0 = arg_24_1.index
	local var_24_1 = arg_24_0._effectList[var_24_0]

	if var_24_1:
		arg_24_0._owner.RemoveFX(var_24_1.effect_go)

		arg_24_0._effectList[var_24_0] = None

def var_0_5.deactiveEffect(arg_25_0, arg_25_1):
	local var_25_0 = arg_25_1.index
	local var_25_1 = arg_25_0._effectList[var_25_0]

	if var_25_1:
		var_25_1.effect_go.SetActive(False)

def var_0_5.getIndex(arg_26_0):
	arg_26_0._effectIndex = arg_26_0._effectIndex + 1

	return arg_26_0._effectIndex

def var_0_5.updateEffect(arg_27_0, arg_27_1):
	if arg_27_1.posFun:
		local var_27_0 = arg_27_1.posFun(arg_27_1.currentTime)

		arg_27_1.effect_tf.localPosition = var_27_0

	if arg_27_1.rotationFun:
		local var_27_1 = arg_27_1.rotationFun(arg_27_1.currentTime)

		if arg_27_0._dir == var_0_0.Battle.BattleConst.UnitDir.LEFT:
			var_27_1.y = var_27_1.y - 180

		arg_27_1.effect_tf.localEulerAngles = var_27_1

	if arg_27_1.fillFunc:
		arg_27_0._characterScaleX = arg_27_0._characterScaleX or arg_27_0._owner.GetTf().localScale.x
		arg_27_0._characterScaleZ = arg_27_0._characterScaleZ or arg_27_0._owner.GetTf().localScale.z

		local var_27_2, var_27_3, var_27_4 = arg_27_1.fillFunc()

		arg_27_1.effect_tf.position = var_27_2
		arg_27_1.effect_tf.localScale = Vector3(var_27_3 / arg_27_0._characterScaleX, 0, var_27_4 / arg_27_0._characterScaleZ)
