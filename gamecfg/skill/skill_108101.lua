﻿return {
	uiEffect = "",
	name = "",
	cd = 0,
	painting = 0,
	id = 108101,
	picture = "0",
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
			targetAniEffect = "",
			target_choise = {
				"TargetAllHelp",
				"TargetShipTag"
			},
			arg_list = {
				buff_id = 108104,
				ship_tag_list = {
					"RIKKA"
				}
			}
		}
	}
}
