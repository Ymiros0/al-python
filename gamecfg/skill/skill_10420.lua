﻿return {
	uiEffect = "",
	name = "先手必胜",
	cd = 0,
	painting = 1,
	id = 10420,
	picture = "0",
	castCV = "skill",
	desc = "出击时第一轮空中支援预加载",
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
			target_choise = "TargetSelf",
			targetAniEffect = "",
			arg_list = {
				buff_id = 10421
			}
		}
	}
}
