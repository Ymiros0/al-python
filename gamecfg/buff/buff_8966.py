return {
	init_effect = "",
	name = "视野限制-敌方隐藏光环-属性修改",
	time = 5,
	picture = "",
	desc = "",
	stack = 1,
	id = 8966,
	icon = 9,
	last_effect = "",
	effect_list = {
		{
			type = "BattleBuffField",
			trigger = {
				""
			},
			arg_list = {
				buff_id = 8681,
				FAura = True,
				target = {
					"TargetPlayerLeaderShip"
				}
			}
		},
		{
			type = "BattleFleetBuffInk",
			trigger = {
				"onAttach",
				"onRemove"
			},
			arg_list = {}
		},
		{
			type = "BattleFleetBuffBlindAura",
			trigger = {},
			arg_list = {
				target = {
					"TargetAllHarm"
				}
			}
		}
	}
}
