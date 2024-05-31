ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleUnitEvent

var_0_0.Battle.BattleAircraftCharacter = class("BattleAircraftCharacter", var_0_0.Battle.BattleCharacter)
var_0_0.Battle.BattleAircraftCharacter.__name = "BattleAircraftCharacter"

local var_0_2 = var_0_0.Battle.BattleAircraftCharacter

def var_0_2.Ctor(arg_1_0):
	var_0_2.super.Ctor(arg_1_0)

	arg_1_0._hpBarOffset = Vector3(0, 1.6, 0)

	arg_1_0.SetYShakeMin()
	arg_1_0.SetYShakeMax()

	arg_1_0.shadowScale = Vector3.one
	arg_1_0.shadowPos = Vector3.zero

def var_0_2.SetUnitData(arg_2_0, arg_2_1):
	arg_2_0._unitData = arg_2_1

	arg_2_0.AddUnitEvent()

def var_0_2.InitWeapon(arg_3_0):
	arg_3_0._weapon = arg_3_0._unitData.GetWeapon()

	for iter_3_0, iter_3_1 in ipairs(arg_3_0._weapon):
		iter_3_1.RegisterEventListener(arg_3_0, var_0_1.CREATE_BULLET, arg_3_0.onCreateBullet)

def var_0_2.GetModleID(arg_4_0):
	return arg_4_0._unitData.GetSkinID()

def var_0_2.GetInitScale(arg_5_0):
	return 1

def var_0_2.AddUnitEvent(arg_6_0):
	return

def var_0_2.RemoveUnitEvent(arg_7_0):
	for iter_7_0, iter_7_1 in ipairs(arg_7_0._weapon):
		iter_7_1.UnregisterEventListener(arg_7_0, var_0_1.CREATE_BULLET)

	if arg_7_0._unitData.GetIFF() == var_0_0.Battle.BattleConfig.FOE_CODE:
		arg_7_0._unitData.UnregisterEventListener(arg_7_0, var_0_1.UPDATE_AIR_CRAFT_HP)

def var_0_2.PlayAction(arg_8_0):
	return

def var_0_2.Update(arg_9_0):
	arg_9_0.UpdateMatrix()
	arg_9_0.UpdateDirection()
	arg_9_0.UpdateUIComponentPosition()
	arg_9_0.UpdateShadow()
	arg_9_0.UpdatePosition()

	if arg_9_0._unitData.GetIFF() == var_0_0.Battle.BattleConfig.FOE_CODE:
		arg_9_0.UpdateHPPop()
		arg_9_0.UpdateHPPopContainerPosition()
		arg_9_0.UpdateHPBarPosition()
		arg_9_0.UpdateHpBar()

def var_0_2.UpdatePosition(arg_10_0):
	if not arg_10_0._unitData.IsOutViewBound():
		arg_10_0._tf.localPosition = arg_10_0._unitData.GetPosition()

	arg_10_0._characterPos = arg_10_0._unitData.GetPosition()

def var_0_2.UpdateDirection(arg_11_0):
	if arg_11_0._unitData.GetCurrentState() != arg_11_0._unitData.STATE_CREATE:
		return

	local var_11_0 = arg_11_0._unitData.GetSize()

	if arg_11_0._unitData.GetDirection() == var_0_0.Battle.BattleConst.UnitDir.RIGHT:
		arg_11_0._tf.localScale = Vector3(var_11_0, var_11_0, var_11_0)
	elif arg_11_0._unitData.GetDirection() == var_0_0.Battle.BattleConst.UnitDir.LEFT:
		arg_11_0._tf.localScale = Vector3(-var_11_0, var_11_0, var_11_0)

def var_0_2.UpdateHPBarPosition(arg_12_0):
	arg_12_0._hpBarPos.Copy(arg_12_0._referenceVector).Add(arg_12_0._hpBarOffset)

	arg_12_0._HPBarTf.position = arg_12_0._hpBarPos

def var_0_2.UpdateShadow(arg_13_0):
	if arg_13_0._shadow and arg_13_0._unitData.GetCurrentState() == arg_13_0._unitData.STATE_CREATE:
		local var_13_0 = arg_13_0._unitData.GetPosition()
		local var_13_1 = math.min(4, math.max(2, 4 - 4 * var_13_0.y / var_0_0.Battle.BattleConfig.AircraftHeight))

		arg_13_0.shadowScale.x, arg_13_0.shadowScale.z = var_13_1, var_13_1
		arg_13_0._shadowTF.localScale = arg_13_0.shadowScale
		arg_13_0.shadowPos.x, arg_13_0.shadowPos.z = var_13_0.x, var_13_0.z
		arg_13_0._shadowTF.position = arg_13_0.shadowPos

def var_0_2.GetYShake(arg_14_0):
	arg_14_0._YShakeCurrent = arg_14_0._YShakeCurrent or 0
	arg_14_0._YShakeDir = arg_14_0._YShakeDir or 1
	arg_14_0._YShakeCurrent = arg_14_0._YShakeCurrent + 0.1 * arg_14_0._YShakeDir

	if arg_14_0._YShakeCurrent > arg_14_0._YShakeMax and arg_14_0._YShakeDir == 1:
		arg_14_0._YShakeDir = -1

		arg_14_0.SetYShakeMin()
	elif arg_14_0._YShakeCurrent < arg_14_0._YShakeMin and arg_14_0._YShakeDir == -1:
		arg_14_0._YShakeDir = 1

		arg_14_0.SetYShakeMax()

	return arg_14_0._YShakeCurrent

def var_0_2.SetYShakeMin(arg_15_0):
	arg_15_0._YShakeMin = -1 - 2 * math.random()

def var_0_2.SetYShakeMax(arg_16_0):
	arg_16_0._YShakeMax = 1 + 2 * math.random()

def var_0_2.AddModel(arg_17_0, arg_17_1):
	arg_17_0.SetGO(arg_17_1)

	arg_17_0._hpBarOffset = Vector3(0, arg_17_0._unitData.GetBoxSize().y, 0)

	arg_17_0.SetBoneList()

	arg_17_0._tf.position = arg_17_0._unitData.GetPosition()

	arg_17_0.UpdateMatrix()
	arg_17_0._unitData.ActiveCldBox()

def var_0_2.AddShadow(arg_18_0, arg_18_1):
	arg_18_0._shadow = arg_18_0.GetTf().Find("model/shadow").gameObject
	arg_18_0._shadowTF = arg_18_0._shadow.transform

def var_0_2.AddHPBar(arg_19_0, arg_19_1):
	arg_19_0._HPBar = arg_19_1
	arg_19_0._HPBarTf = arg_19_1.transform
	arg_19_0._HPProgress = arg_19_0._HPBarTf.Find("blood").GetComponent(typeof(Image))

	arg_19_1.SetActive(True)
	arg_19_0._unitData.RegisterEventListener(arg_19_0, var_0_1.UPDATE_AIR_CRAFT_HP, arg_19_0.OnUpdateHP)
	arg_19_0.UpdateHpBar()

def var_0_2.updateSomkeFX(arg_20_0):
	return
