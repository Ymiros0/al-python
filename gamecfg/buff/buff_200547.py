return {
	time = 3,
	name = "2023克莱蒙梭活动 陆上神国I 弹条",
	init_effect = "",
	stack = 1,
	id = 200547,
	picture = "",
	last_effect = "",
	desc = "",
	effect_list = {
		{
			type = "BattleBuffCastSkill",
			trigger = {
				"onAttach"
			},
			arg_list = {
				skill_id = 200547,
				target = "TargetSelf"
			}
		}
	}
}