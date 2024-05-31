﻿return {
	init_effect = "",
	name = "我方随机效果",
	time = 1,
	picture = "",
	desc = "",
	stack = 1,
	id = 17478,
	icon = 17470,
	last_effect = "",
	effect_list = {
		{
			type = "BattleBuffCastSkillRandom",
			trigger = {
				"onAttach"
			},
			arg_list = {
				target = "TargetSelf",
				skill_id_list = {
					24065,
					24066,
					24067,
					24068,
					24069
				},
				range = {
					{
						0,
						0.2
					},
					{
						0.2,
						0.4
					},
					{
						0.4,
						0.6
					},
					{
						0.6,
						0.8
					},
					{
						0.8,
						1
					}
				}
			}
		}
	}
}
