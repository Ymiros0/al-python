return {
	effect_list = {
		{
			type = "BattleBuffAddBuff",
			trigger = {
				"onSubmarineRaid"
			},
			arg_list = {
				minTargetNumber = 1,
				buff_id = 13561,
				isBuffStackByCheckTarget = True,
				nationality = 4,
				check_target = {
					"TargetNationalityFriendly",
					"TargetShipTypeFriendly"
				},
				ship_type_list = {
					8
				}
			}
		},
		{
			type = "BattleBuffCastSkill",
			trigger = {
				"onSubmarineRaid"
			},
			arg_list = {
				skill_id = 13560
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
	desc_get = "",
	name = "",
	init_effect = "",
	time = 0,
	color = "red",
	picture = "",
	desc = "",
	stack = 1,
	id = 13560,
	icon = 13560,
	last_effect = ""
}
