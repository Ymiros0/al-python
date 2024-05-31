ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBombBulletFactory = singletonClass("BattleBombBulletFactory", var_0_0.Battle.BattleBulletFactory)
var_0_0.Battle.BattleBombBulletFactory.__name = "BattleBombBulletFactory"

local var_0_1 = var_0_0.Battle.BattleBombBulletFactory

function var_0_1.Ctor(arg_1_0)
	var_0_1.super.Ctor(arg_1_0)
end

function var_0_1.OutRangeFunc(arg_2_0)
	local var_2_0 = arg_2_0:GetTemplate()
	local var_2_1 = var_2_0.hit_type
	local var_2_2 = var_0_1.GetDataProxy()
	local var_2_3 = var_2_0.extra_param
	local var_2_4 = arg_2_0:GetDiveFilter()
	local var_2_5 = {
		_bullet = arg_2_0,
		equipIndex = arg_2_0:GetWeapon():GetEquipmentIndex(),
		bulletTag = arg_2_0:GetExtraTag()
	}

	arg_2_0:BuffTrigger(var_0_0.Battle.BattleConst.BuffEffectType.ON_BOMB_BULLET_BANG, var_2_5)

	if var_2_3.directDMG then
		local var_2_6 = var_2_3.buff_id
		local var_2_7 = var_2_3.buff_level or 1
		local var_2_8 = var_2_3.area_FX or var_2_0.hit_fx

		local function var_2_9(arg_3_0)
			if arg_2_0:CanDealDamage() then
				for iter_3_0, iter_3_1 in ipairs(arg_3_0) do
					if iter_3_1.Active then
						local var_3_0 = iter_3_1.UID
						local var_3_1 = var_0_1.GetSceneMediator():GetCharacter(var_3_0):GetUnitData()
						local var_3_2 = var_0_0.Battle.BattleBuffUnit.New(var_2_6, var_2_7)

						var_3_1:AddBuff(var_3_2)
						var_2_2:HandleDirectDamage(var_3_1, var_2_3.directDMG, arg_2_0)
					end
				end

				arg_2_0:DealDamage()
			end
		end

		local function var_2_10(arg_4_0)
			if arg_4_0.Active then
				var_0_1:GetSceneMediator():GetCharacter(arg_4_0.UID):GetUnitData():RemoveBuff(var_2_6)
			end
		end

		local function var_2_11(arg_5_0)
			for iter_5_0, iter_5_1 in ipairs(arg_5_0) do
				if iter_5_1.Active then
					local var_5_0 = var_0_1:GetSceneMediator():GetCharacter(iter_5_1.UID):GetUnitData()

					if var_5_0:IsAlive() then
						var_5_0:RemoveBuff(var_2_6)
					end
				end
			end

			var_2_2:RemoveBulletUnit(arg_2_0:GetUniqueID())
		end

		var_2_2:SpawnLastingColumnArea(arg_2_0:GetEffectField(), arg_2_0:GetIFF(), arg_2_0:GetExplodePostion(), var_2_1.range, var_2_1.time, var_2_9, var_2_10, false, var_2_8, var_2_11, true):SetDiveFilter(var_2_4)
		arg_2_0:HideBullet()
	else
		local var_2_12

		local function var_2_13(arg_6_0)
			local var_6_0 = var_2_1.decay

			if var_6_0 then
				var_2_12:UpdateDistanceInfo()
			end

			for iter_6_0, iter_6_1 in ipairs(arg_6_0) do
				if iter_6_1.Active then
					local var_6_1 = iter_6_1.UID
					local var_6_2 = 0

					if var_6_0 then
						var_6_2 = var_2_12:GetDistance(var_6_1) / (var_2_1.range * 0.5) * var_6_0
					end

					local var_6_3 = var_0_1.GetSceneMediator():GetCharacter(var_6_1):GetUnitData()

					var_2_2:HandleDamage(arg_2_0, var_6_3, var_6_2)
				end
			end
		end

		var_2_12 = var_2_2:SpawnColumnArea(arg_2_0:GetEffectField(), arg_2_0:GetIFF(), arg_2_0:GetExplodePostion(), var_2_1.range, var_2_1.time, var_2_13)

		var_2_12:SetDiveFilter(var_2_4)

		if var_2_3.friendlyFire then
			var_2_2:SpawnColumnArea(arg_2_0:GetEffectField(), var_2_2.GetOppoSideCode(arg_2_0:GetIFF()), arg_2_0:GetExplodePostion(), var_2_1.range, var_2_1.time, var_2_13):SetDiveFilter(var_2_4)
		end

		var_2_12:SetIndiscriminate(var_2_3.indiscriminate)
		var_2_2:RemoveBulletUnit(arg_2_0:GetUniqueID())
	end
end

function var_0_1.MakeBullet(arg_7_0)
	return var_0_0.Battle.BattleBombBullet.New()
end

function var_0_1.onBulletHitFunc(arg_8_0, arg_8_1, arg_8_2)
	local var_8_0 = arg_8_0:GetBulletData()
	local var_8_1 = var_8_0:GetTemplate()

	var_0_0.Battle.PlayBattleSFX(var_8_0:GetHitSFX())

	local var_8_2, var_8_3 = var_0_1.GetFXPool():GetFX(arg_8_0:GetFXID())
	local var_8_4 = pg.Tool.FilterY(var_8_0:GetPosition())

	pg.EffectMgr.GetInstance():PlayBattleEffect(var_8_2, var_8_4:Add(var_8_3), true)
end

function var_0_1.onBulletMissFunc()
	return
end

function var_0_1.MakeModel(arg_10_0, arg_10_1, arg_10_2)
	local var_10_0 = arg_10_1:GetBulletData()
	local var_10_1 = var_10_0:GetExplodePostion()
	local var_10_2, var_10_3, var_10_4, var_10_5 = arg_10_0:GetDataProxy():GetTotalBounds()

	if var_10_1.z > var_10_2 + 3 then
		arg_10_0:GetDataProxy():RemoveBulletUnit(var_10_0:GetUniqueID())

		return
	end

	local var_10_6 = var_10_0:GetTemplate()

	if not arg_10_0:GetBulletPool():InstBullet(arg_10_1:GetModleID(), function(arg_11_0)
		arg_10_1:AddModel(arg_11_0)
	end) then
		arg_10_1:AddTempModel(arg_10_0:GetTempGOPool():GetObject())
	end

	arg_10_1:SetSpawn(arg_10_2)

	if var_10_0:GetIFF() ~= arg_10_0:GetDataProxy():GetFriendlyCode() and var_10_0:GetExist() and var_10_6.alert_fx ~= "" then
		var_0_1.CreateBulletAlert(var_10_0)
	end

	var_10_0:SetExist(true)
	arg_10_1:SetFXFunc(arg_10_0.onBulletHitFunc, arg_10_0.onBulletMissFunc)
	arg_10_0:GetSceneMediator():AddBullet(arg_10_1)
end

function var_0_1.CreateBulletAlert(arg_12_0)
	local var_12_0 = arg_12_0:GetTemplate().hit_type.range
	local var_12_1 = arg_12_0:GetTemplate().alert_fx
	local var_12_2 = var_0_0.Battle.BattleFXPool.GetInstance():GetFX(var_12_1)
	local var_12_3 = var_12_2.transform
	local var_12_4 = 0
	local var_12_5 = pg.effect_offset

	if var_12_5[var_12_1] and var_12_5[var_12_1].y_scale == true then
		var_12_4 = var_12_0
	end

	var_12_3.localScale = Vector3(var_12_0, var_12_4, var_12_0)

	pg.EffectMgr.GetInstance():PlayBattleEffect(var_12_2, arg_12_0:GetExplodePostion())
end
