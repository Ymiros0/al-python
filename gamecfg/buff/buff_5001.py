return {
	effect_list = {
		{
			type = "BattleBuffAddBuff",
			trigger = {
				"onUpdate"
			},
			arg_list = {
				buff_id = 5002,
				time = 20,
				target = "TargetSelf"
			}
		}
	},
	{
		desc = "每隔20秒，有25%的概率发动，中幅降低敌方单个单位射速与伤害，持续5.0秒，优先对精英目标（人形单位）生效，同技能效果不叠加",
		addition = {
			"5.0(+0.5)"
		}
	},
	{
		desc = "每隔20秒，有25%的概率发动，中幅降低敌方单个单位射速与伤害，持续5.5秒，优先对精英目标（人形单位）生效，同技能效果不叠加",
		addition = {
			"5.5(+0.5)"
		}
	},
	{
		desc = "每隔20秒，有25%的概率发动，中幅降低敌方单个单位射速与伤害，持续6.0秒，优先对精英目标（人形单位）生效，同技能效果不叠加",
		addition = {
			"6.0(+0.5)"
		}
	},
	{
		desc = "每隔20秒，有25%的概率发动，中幅降低敌方单个单位射速与伤害，持续6.5秒，优先对精英目标（人形单位）生效，同技能效果不叠加",
		addition = {
			"6.5(+0.5)"
		}
	},
	{
		desc = "每隔20秒，有25%的概率发动，中幅降低敌方单个单位射速与伤害，持续7.0秒，优先对精英目标（人形单位）生效，同技能效果不叠加",
		addition = {
			"7.0(+0.5)"
		}
	},
	{
		desc = "每隔20秒，有25%的概率发动，中幅降低敌方单个单位射速与伤害，持续7.5秒，优先对精英目标（人形单位）生效，同技能效果不叠加",
		addition = {
			"7.5(+0.5)"
		}
	},
	{
		desc = "每隔20秒，有25%的概率发动，中幅降低敌方单个单位射速与伤害，持续8.0秒，优先对精英目标（人形单位）生效，同技能效果不叠加",
		addition = {
			"8.0(+0.5)"
		}
	},
	{
		desc = "每隔20秒，有25%的概率发动，中幅降低敌方单个单位射速与伤害，持续8.5秒，优先对精英目标（人形单位）生效，同技能效果不叠加",
		addition = {
			"8.5(+0.5)"
		}
	},
	{
		desc = "每隔20秒，有25%的概率发动，中幅降低敌方单个单位射速与伤害，持续9.0秒，优先对精英目标（人形单位）生效，同技能效果不叠加",
		addition = {
			"9.0(+1)"
		}
	},
	{
		desc = "每隔20秒，有25%的概率发动，中幅降低敌方单个单位射速与伤害，持续10.0秒，优先对精英目标（人形单位）生效，同技能效果不叠加",
		addition = {
			"10.0"
		}
	},
	desc_get = "每隔20秒，有25%的概率发动，中幅降低敌方单个单位射速与伤害，持续5秒(满级15秒)，优先对精英目标（人形单位）生效，同技能效果不叠加",
	name = "火力干扰",
	init_effect = "",
	time = 0,
	color = "yellow",
	picture = "",
	desc = "每隔20秒，有25%的概率发动，中幅降低敌方单个单位射速与伤害，持续$1秒，优先对精英目标（人形单位）生效，同技能效果不叠加",
	stack = 1,
	id = 5001,
	icon = 5000,
	last_effect = ""
}
