﻿return {
	init_effect = "",
	name = "古立特联动 宝多六花支援弹幕LV3",
	time = 5,
	color = "yellow",
	picture = "",
	desc = "",
	stack = 1,
	id = 9309,
	icon = 9309,
	last_effect = "",
	effect_list = {
		{
			type = "BattleBuffAddBuff",
			trigger = {
				"onFlagShip"
			},
			arg_list = {
				buff_id = 9310,
				target = "TargetSelf"
			}
		}
	}
}