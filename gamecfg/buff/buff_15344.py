return {
	effect_list = {
		{
			type = "BattleBuffAddBuff",
			trigger = {
				"onAttach"
			},
			arg_list = {
				buff_id = 15343,
				minTargetNumber = 1,
				isBuffStackByCheckTarget = True,
				check_target = {
					"TargetAllHelp",
					"TargetPlayerVanguardFleet"
				}
			}
		}
	},
	{},
	{},
	{},
	{},
	{},
	{},
	{},
	{},
	{},
	{},
	init_effect = "",
	name = "",
	time = 0,
	color = "red",
	picture = "",
	desc = "",
	stack = 1,
	id = 15344,
	icon = 15340,
	last_effect = ""
}
