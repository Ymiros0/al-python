﻿return {
	uiEffect = "",
	name = "自身减伤",
	cd = 0,
	painting = 0,
	id = 16361,
	picture = "0",
	castCV = "",
	desc = "",
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
				buff_id = 16363,
				ship_tag_list = {
					"Hwah Jah"
				}
			}
		}
	}
}
