﻿return {
	init_effect = "",
	name = "古立特联动 梦芽支援弹幕LV1",
	time = 5,
	color = "yellow",
	picture = "",
	desc = "",
	stack = 1,
	id = 9423,
	icon = 9423,
	last_effect = "",
	effect_list = {
		{
			type = "BattleBuffAddBuff",
			trigger = {
				"onFlagShip"
			},
			arg_list = {
				buff_id = 9424,
				target = "TargetSelf"
			}
		}
	}
}
