ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleConfig
local var_0_3 = var_0_0.Battle.BattleEvent
local var_0_4 = class("BattleSkillProjectArea", var_0_0.Battle.BattleSkillEffect)

var_0_0.Battle.BattleSkillProjectArea = var_0_4
var_0_4.__name = "BattleSkillProjectArea"

def var_0_4.Ctor(arg_1_0, arg_1_1):
	var_0_4.super.Ctor(arg_1_0, arg_1_1, lv)

	arg_1_0._posX = arg_1_0._tempData.arg_list.offset_x
	arg_1_0._posZ = arg_1_0._tempData.arg_list.offset_z
	arg_1_0._width = arg_1_0._tempData.arg_list.width
	arg_1_0._height = arg_1_0._tempData.arg_list.height
	arg_1_0._lifeTime = arg_1_0._tempData.arg_list.life_time
	arg_1_0._fx = arg_1_0._tempData.arg_list.effect
	arg_1_0._expendDuration = arg_1_0._tempData.arg_list.expend_duration
	arg_1_0._widthSpeed = arg_1_0._tempData.arg_list.width_expend_speed
	arg_1_0._heightSpeed = arg_1_0._tempData.arg_list.height_expend_speed
	arg_1_0._buffID = arg_1_0._tempData.arg_list.cld_buff_id

def var_0_4.DoDataEffect(arg_2_0, arg_2_1):
	arg_2_0.doSpawnAOE(arg_2_1)

def var_0_4.DoDataEffectWithoutTarget(arg_3_0, arg_3_1):
	arg_3_0.doSpawnAOE(arg_3_1)

def var_0_4.doSpawnAOE(arg_4_0, arg_4_1):
	local var_4_0 = var_0_0.Battle.BattleDataProxy.GetInstance()

	local function var_4_1(arg_5_0)
		for iter_5_0, iter_5_1 in ipairs(arg_5_0):
			if iter_5_1.Active:
				local var_5_0 = var_4_0.GetUnitList()[iter_5_1.UID]
				local var_5_1 = var_0_0.Battle.BattleBuffUnit.New(arg_4_0._buffID)

				var_5_0.AddBuff(var_5_1, True)

	local function var_4_2(arg_6_0)
		if arg_6_0.Active:
			var_4_0.GetUnitList()[arg_6_0.UID].RemoveBuff(arg_4_0._buffID, True)

	local var_4_3 = arg_4_1.GetPosition()
	local var_4_4 = Vector3(var_4_3.x + arg_4_0._posX, 0, var_4_3.z + arg_4_0._posZ)
	local var_4_5 = var_4_0.SpawnLastingCubeArea(var_0_1.AOEField.SURFACE, arg_4_1.GetIFF(), var_4_4, arg_4_0._width, arg_4_0._height, arg_4_0._lifeTime, var_4_1, var_4_2, True, arg_4_0._fx, None)

	if arg_4_0._expendDuration > 0:
		local var_4_6 = var_0_0.Battle.BattleAOEScaleableComponent.New(var_4_5)

		var_4_6.SetReferenceUnit(arg_4_1)

		local var_4_7 = {
			expendDuration = arg_4_0._expendDuration,
			widthSpeed = arg_4_0._widthSpeed,
			heightSpeed = arg_4_0._heightSpeed
		}

		var_4_6.ConfigData(var_4_6.EXPEND, var_4_7)
