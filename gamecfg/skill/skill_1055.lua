﻿return {
	uiEffect = "",
	name = "战术指挥·主力",
	cd = 0,
	painting = 1,
	id = 1055,
	picture = "0",
	castCV = "skill",
	desc = "提高舰队中所有主力的炮击、雷击、装填属性",
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
			type = "BattleSkillAddBuff",
			casterAniEffect = "",
			target_choise = "TargetPlayerMainFleet",
			targetAniEffect = "",
			arg_list = {
				buff_id = 1050
			}
		}
	}
}
