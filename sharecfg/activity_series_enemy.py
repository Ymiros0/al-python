pg = pg or {}
pg.activity_series_enemy = {
	[1001] = {
		pre_chapter = 0,
		name = "EASY. Jamming Breakthrough",
		chapter_name = "TC1",
		type = 1,
		pos_x = "0.10703125",
		count = 0,
		additional_awards_display = "",
		pos_y = "0.157291667",
		whether_singlefight = 0,
		id = 1001,
		ex_count = "",
		oil = 0,
		profiles = "Objectives. Suppress the Greenland Siren stronghold, destroy the jamming device, and restore the main communication line.",
		limitation = {},
		expedition_id = {
			1719101
		},
		boss_icon = {
			{
				"qinraozhe",
				2
			}
		},
		pass_awards_display = {
			{
				1,
				308,
				1
			},
			{
				2,
				58839,
				1
			},
			{
				2,
				59001,
				1
			},
			{
				2,
				54012,
				1
			}
		},
		defeat_story = {},
		defeat_story_count = {},
		use_oil_limit = {
			0,
			0
		}
	},
	[1002] = {
		pre_chapter = 1001,
		name = "NORMAL. Anomaly Disruption",
		chapter_name = "TC2",
		type = 1,
		pos_x = "0.34609375",
		count = 0,
		id = 1002,
		pos_y = "0.347916667",
		whether_singlefight = 1,
		ex_count = "",
		oil = 0,
		profiles = "Objectives. Break through the Siren defensive line in the Chukchi Sea, and remove the source of the anomalous weather.",
		limitation = {},
		expedition_id = {
			1719201,
			1719202
		},
		boss_icon = {
			{
				"qinraozhe",
				2
			},
			{
				"qingchuzhe",
				5
			}
		},
		pass_awards_display = {
			{
				1,
				308,
				1
			},
			{
				2,
				58838,
				1
			},
			{
				2,
				59001,
				1
			},
			{
				2,
				54017,
				1
			}
		},
		additional_awards_display = {
			{
				1,
				308,
				1
			},
			{
				1,
				1,
				1
			}
		},
		defeat_story = {},
		defeat_story_count = {},
		use_oil_limit = {
			0,
			0
		}
	},
	[1003] = {
		pre_chapter = 1002,
		name = "HARD. Research Base Recapture",
		chapter_name = "TC3",
		type = 1,
		pos_x = "0.50546875",
		count = 0,
		id = 1003,
		pos_y = "0.080208333",
		whether_singlefight = 1,
		ex_count = "",
		oil = 0,
		profiles = "Objectives. Recapture the research base in the Northern Islands, destroy the nearby Siren factory, and prevent the enemy from gaining more reinforcements.",
		limitation = {},
		expedition_id = {
			1719301,
			1719302,
			1719303
		},
		boss_icon = {
			{
				"qinraozhe_IV",
				2
			},
			{
				"kuersike",
				3
			},
			{
				"qingchuzhe",
				5
			}
		},
		pass_awards_display = {
			{
				1,
				308,
				1
			},
			{
				2,
				58837,
				1
			},
			{
				2,
				59001,
				1
			},
			{
				2,
				54017,
				1
			}
		},
		additional_awards_display = {
			{
				1,
				308,
				1
			},
			{
				1,
				1,
				1
			}
		},
		defeat_story = {},
		defeat_story_count = {},
		use_oil_limit = {
			25,
			16
		}
	},
	[1004] = {
		pre_chapter = 1003,
		name = "SP. Full-Scale Reconnaissance",
		chapter_name = "SP",
		type = 2,
		pos_x = "0.60546875",
		count = 1,
		id = 1004,
		pos_y = "0.446875",
		whether_singlefight = 0,
		ex_count = "",
		oil = 0,
		profiles = "Objectives. Carry out full-scale reconnaissance of the Polar North Siren stronghold, and collect as much data as possible to determine strategic intentions.",
		limitation = {},
		expedition_id = {
			1719401,
			1719402,
			1719403,
			1719404
		},
		boss_icon = {
			{
				"qinraozhe_IV",
				2
			},
			{
				"fuluoxiluofu",
				2
			},
			{
				"saiwasituoboer",
				5
			},
			{
				"qingchuzhe",
				5
			}
		},
		pass_awards_display = {
			{
				1,
				308,
				1
			},
			{
				2,
				58836,
				1
			},
			{
				2,
				59001,
				1
			},
			{
				2,
				54016,
				1
			}
		},
		additional_awards_display = {
			{
				1,
				308,
				1
			},
			{
				1,
				1,
				1
			}
		},
		defeat_story = {},
		defeat_story_count = {},
		use_oil_limit = {
			40,
			16
		}
	},
	[1005] = {
		pre_chapter = 1004,
		name = "EX. Singularity Diversion Operation",
		chapter_name = "EX",
		type = 3,
		pos_x = "0.6265625",
		count = 0,
		additional_awards_display = "",
		pos_y = "0.15625",
		whether_singlefight = 0,
		pass_awards_display = "",
		id = 1005,
		oil = 0,
		profiles = "Objectives. Send a diversionary fleet to attract the attention of Omitter's main force, restrain the Siren fleets located in the 'Crown' Singularity, and reduce pressure on other fleets.",
		limitation = {},
		expedition_id = {
			1719501,
			1719502,
			1719503,
			1719504,
			1719505
		},
		boss_icon = {
			{
				"qinraozhe_IV",
				2
			},
			{
				"kuersike",
				3
			},
			{
				"fuluoxiluofu",
				2
			},
			{
				"saiwasituoboer",
				5
			},
			{
				"qingchuzhe",
				5
			}
		},
		defeat_story = {},
		defeat_story_count = {},
		use_oil_limit = {
			0,
			0
		},
		ex_count = {
			8000,
			20,
			0.2,
			1000,
			0.8
		}
	},
	all = {
		1001,
		1002,
		1003,
		1004,
		1005
	}
}
