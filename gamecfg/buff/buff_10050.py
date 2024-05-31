return {
	effect_list = {
		{
			type = "BattleBuffCastSkill",
			trigger = {
				"onBeHit"
			},
			arg_list = {
				rant = 1500,
				target = "TargetSelf",
				skill_id = 10050,
				time = 20
			}
		}
	},
	{
		desc = "受到攻击时，有15%的几率触发，5.0秒内使全体先锋完全回避所有攻击",
		addition = {
			"5.0(+0.5)"
		}
	},
	{
		desc = "受到攻击时，有15%的几率触发，5.5秒内使全体先锋完全回避所有攻击",
		addition = {
			"5.5(+0.5)"
		}
	},
	{
		desc = "受到攻击时，有15%的几率触发，6.0秒内使全体先锋完全回避所有攻击",
		addition = {
			"6.0(+0.5)"
		}
	},
	{
		desc = "受到攻击时，有15%的几率触发，6.5秒内使全体先锋完全回避所有攻击",
		addition = {
			"6.5(+0.5)"
		}
	},
	{
		desc = "受到攻击时，有15%的几率触发，7.0秒内使全体先锋完全回避所有攻击",
		addition = {
			"7.0(+0.5)"
		}
	},
	{
		desc = "受到攻击时，有15%的几率触发，7.5秒内使全体先锋完全回避所有攻击",
		addition = {
			"7.5(+0.5)"
		}
	},
	{
		desc = "受到攻击时，有15%的几率触发，8.0秒内使全体先锋完全回避所有攻击",
		addition = {
			"8.0(+0.5)"
		}
	},
	{
		desc = "受到攻击时，有15%的几率触发，8.5秒内使全体先锋完全回避所有攻击",
		addition = {
			"8.5(+0.5)"
		}
	},
	{
		desc = "受到攻击时，有15%的几率触发，9.0秒内使全体先锋完全回避所有攻击",
		addition = {
			"9.0(+1)"
		}
	},
	{
		desc = "受到攻击时，有15%的几率触发，10.0秒内使全体先锋完全回避所有攻击",
		addition = {
			"10.0"
		}
	},
	desc_get = "受到攻击时，有15%的几率触发，5.0秒(满级10.0秒)内使全体先锋完全回避所有攻击",
	name = "彩虹计划",
	init_effect = "",
	time = 0,
	color = "blue",
	picture = "",
	desc = "受到攻击时，有15%的几率触发，$1秒内使全体先锋完全回避所有攻击",
	stack = 1,
	id = 10050,
	icon = 10050,
	last_effect = ""
}
