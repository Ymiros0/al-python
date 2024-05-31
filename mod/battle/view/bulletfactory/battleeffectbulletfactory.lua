ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleEffectBulletFactory = singletonClass("BattleEffectBulletFactory", var_0_0.Battle.BattleBulletFactory)
var_0_0.Battle.BattleEffectBulletFactory.__name = "BattleEffectBulletFactory"

local var_0_1 = var_0_0.Battle.BattleEffectBulletFactory

function var_0_1.Ctor(arg_1_0)
	var_0_1.super.Ctor(arg_1_0)
end

function var_0_1.MakeBullet(arg_2_0)
	return var_0_0.Battle.BattleTorpedoBullet.New()
end

function var_0_1.onBulletHitFunc(arg_3_0, arg_3_1, arg_3_2)
	local var_3_0 = var_0_1.GetDataProxy()
	local var_3_1 = arg_3_0:GetBulletData()
	local var_3_2 = var_3_1:GetTemplate()

	var_0_0.Battle.PlayBattleSFX(var_3_1:GetHitSFX())

	if not var_3_1:IsFlare() then
		var_3_1:spawnArea()
	end

	local var_3_3, var_3_4 = var_0_1.GetFXPool():GetFX(arg_3_0:GetFXID())
	local var_3_5 = arg_3_0:GetTf().localPosition

	pg.EffectMgr.GetInstance():PlayBattleEffect(var_3_3, var_3_4:Add(var_3_5), true)

	if var_3_1:GetPierceCount() <= 0 then
		var_3_0:RemoveBulletUnit(var_3_1:GetUniqueID())
	end
end

function var_0_1.onBulletMissFunc(arg_4_0)
	var_0_1.onBulletHitFunc(arg_4_0)
end

function var_0_1.MakeModel(arg_5_0, arg_5_1, arg_5_2)
	local var_5_0 = arg_5_1:GetBulletData():GetTemplate()
	local var_5_1 = arg_5_0:GetDataProxy()

	if not arg_5_0:GetBulletPool():InstBullet(arg_5_1:GetModleID(), function(arg_6_0)
		arg_5_1:AddModel(arg_6_0)
	end) then
		arg_5_1:AddTempModel(arg_5_0:GetTempGOPool():GetObject())
	end

	arg_5_1:SetSpawn(arg_5_2)
	arg_5_1:SetFXFunc(arg_5_0.onBulletHitFunc, arg_5_0.onBulletMissFunc)
	arg_5_0:GetSceneMediator():AddBullet(arg_5_1)
end
