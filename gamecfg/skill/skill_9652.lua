﻿return {
	uiEffect = "",
	name = "敌方夜战照明弹(循环施放)",
	cd = 0,
	painting = 1,
	id = 9652,
	picture = "0",
	desc = "敌方夜战照明弹(循环施放)",
	aniEffect = {
		effect = "jineng",
		offset = {
			0,
			-2,
			0
		}
	},
	effect_list = {
		{
			type = "BattleSkillFire",
			casterAniEffect = "",
			target_choise = "TargetHarmNearest",
			targetAniEffect = "",
			arg_list = {
				weapon_id = 350001
			}
		},
		{
			type = "BattleSkillAddBuff",
			casterAniEffect = "",
			target_choise = "TargetSelf",
			targetAniEffect = "",
			arg_list = {
				buff_id = 9653
			}
		}
	}
}
