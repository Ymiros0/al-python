ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleSkillPlaySFX", var_0_0.Battle.BattleSkillEffect)

var_0_0.Battle.BattleSkillPlaySFX = var_0_1
var_0_1.__name = "BattleSkillPlaySFX"

function var_0_1.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_1.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0._SFXID = arg_1_0._tempData.arg_list.sound_effect
end

function var_0_1.DoDataEffect(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0:playSound()
end

function var_0_1.DoDataEffectWithoutTarget(arg_3_0, arg_3_1)
	arg_3_0:playSound()
end

function var_0_1.playSound(arg_4_0)
	var_0_0.Battle.PlayBattleSFX(arg_4_0._SFXID)
end
