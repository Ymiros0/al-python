﻿return {
	init_effect = "",
	name = "进入战斗时，若旗舰为轻航或正航,战斗开始后15秒触发额外舰载机编队",
	time = 0,
	color = "yellow",
	picture = "",
	desc = "该入口提供战外挂载到战内",
	stack = 1,
	id = 40350,
	icon = 40350,
	last_effect = "",
	effect_list = {
		{
			type = "BattleBuffCastSkill",
			trigger = {
				"onFlagShip"
			},
			arg_list = {
				minTargetNumber = 1,
				skill_id = 40350,
				target = "TargetSelf",
				check_target = {
					"TargetSelf",
					"TargetShipType"
				},
				ship_type_list = {
					6,
					7
				}
			}
		}
	}
}
