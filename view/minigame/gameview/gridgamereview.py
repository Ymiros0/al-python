local var_0_0 = class("GridGameReView", import("..BaseMiniGameView"))
local var_0_1 = False
local var_0_2 = "battle-boss-4"
local var_0_3 = "event./ui/ddldaoshu2"
local var_0_4 = "event./ui/niujiao"
local var_0_5 = "event./ui/taosheng"
local var_0_6 = "ui/minigameui/gridgameui_atlas"
local var_0_7 = 60
local var_0_8 = "mini_game_time"
local var_0_9 = "mini_game_score"
local var_0_10 = "mini_game_leave"
local var_0_11 = "mini_game_pause"
local var_0_12 = "mini_game_cur_score"
local var_0_13 = "mini_game_high_score"
local var_0_14 = "event grid combo"
local var_0_15 = "event grid trigger"
local var_0_16 = "event move role"
local var_0_17 = "event add score"
local var_0_18 = "event role special"
local var_0_19 = "event special end"
local var_0_20 = "event camera in"
local var_0_21 = "event camedra out"
local var_0_22 = "event ignore time"
local var_0_23 = {
	power_grid = 0,
	grid_index = 0,
	special_time = False,
	special_complete = False
}
local var_0_24 = 12
local var_0_25 = 0.3
local var_0_26 = Vector2(138, 150)
local var_0_27 = 2500
local var_0_28 = 0
local var_0_29 = 100
local var_0_30 = 1
local var_0_31 = 2
local var_0_32 = 3
local var_0_33 = {
	{
		id = 1,
		name = "red",
		index = 1
	},
	{
		id = 2,
		name = "yellow",
		index = 2
	},
	{
		id = 3,
		name = "blue",
		index = 3
	},
	[999] = {
		id = 999,
		name = "color",
		index = 999
	}
}
local var_0_34 = {
	1,
	2,
	3
}
local var_0_35 = {
	{
		rule = var_0_30
	},
	{
		id = 999,
		rule = var_0_31
	},
	{
		rule = var_0_32
	}
}
local var_0_36 = {
	{
		index = 1,
		name = "red",
		max = 1000
	},
	{
		index = 2,
		name = "yellow",
		max = 1000
	},
	{
		index = 3,
		name = "blue",
		max = 1000
	}
}
local var_0_37 = 0.5
local var_0_38 = 50
local var_0_39 = 3
local var_0_40 = 150
local var_0_41 = 1.5
local var_0_42 = 500
local var_0_43 = 260
local var_0_44 = 50
local var_0_45 = 3400
local var_0_46 = 5
local var_0_47 = 4
local var_0_48 = {
	1,
	2,
	3,
	4,
	5
}
local var_0_49 = {
	{
		1,
		5
	}
}
local var_0_50 = {
	1,
	2,
	5
}
local var_0_51 = {
	1,
	2,
	5,
	3,
	4
}
local var_0_52 = {
	{
		5,
		4
	},
	{
		2,
		4
	},
	{
		5,
		3
	},
	{
		1,
		3
	},
	{
		1,
		4
	},
	{
		2,
		3
	},
	{
		5,
		4
	}
}
local var_0_53 = {
	2,
	1,
	1,
	2,
	2,
	1,
	2
}
local var_0_54 = {}
local var_0_55 = 7
local var_0_56 = Vector2(0, 0)
local var_0_57 = 0.07
local var_0_58 = 0.3
local var_0_59 = 0.5
local var_0_60 = 5
local var_0_61 = "sound start"
local var_0_62 = "sound trigger"
local var_0_63 = "sound end"
local var_0_64 = {
	"bg00",
	"bg01",
	"bg02",
	"bg03",
	"bg04",
	"bg10",
	"bg11",
	"bg12",
	"bg13",
	"bg14"
}
local var_0_65 = {
	"bg00",
	"bg01",
	"bg02",
	"bg03",
	"bg04"
}
local var_0_66 = {
	"bg10",
	"bg11",
	"bg12",
	"bg13",
	"bg14"
}
local var_0_67 = 0
local var_0_68 = 1
local var_0_69 = 2
local var_0_70 = var_0_68
local var_0_71 = {
	{
		rate = 0.05,
		source = "scene_background/bg00",
		type = var_0_68
	},
	{
		rate = 0.1,
		source = "scene_background/bg01",
		type = var_0_68
	},
	{
		rate = 0.2,
		source = "scene_background/bg02",
		type = var_0_68
	},
	{
		rate = 0.8,
		source = "scene_background/bg03",
		type = var_0_68
	},
	{
		rate = 0.05,
		source = "scene_background/bg10",
		type = var_0_69
	},
	{
		rate = 0.1,
		source = "scene_background/bg11",
		type = var_0_69
	},
	{
		rate = 0.2,
		source = "scene_background/bg12",
		type = var_0_69
	},
	{
		rate = 0.8,
		source = "scene_background/bg13",
		type = var_0_69
	},
	{
		rate = 1.2,
		source = "scene_front/bg04",
		type = var_0_68
	},
	{
		rate = 1.2,
		source = "scene_front/bg14",
		type = var_0_69
	},
	{
		rate = 1,
		source = "scene/rolePos",
		type = var_0_67
	}
}
local var_0_72 = {
	c_Skill_1 = "c_Skill_1",
	n_Neutral = "n_Neutral",
	n_Combine = "n_Combine",
	n_Skill_2 = "n_Skill_2",
	n_MoveL = "n_MoveL",
	n_Atk = "n_Atk",
	c_Neutral = "c_Neutral",
	n_MoveR = "n_MoveR",
	c_Atk = "c_Atk",
	n_Skill_1 = "n_Skill_1",
	c_MoveL = "c_MoveL",
	c_Dmg = "c_Dmg",
	n_Skill_3 = "n_Skill_3",
	n_DMG = "n_DMG",
	c_MoveR = "c_MoveR"
}
local var_0_73 = {
	n_Move_R = {
		time = 0,
		anim_name = var_0_72.n_MoveR,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance = Vector3(650, 0, 0)
		}
	},
	n_Atk = {
		time = 0,
		sound_trigger = "taosheng",
		anim_name = var_0_72.n_Atk,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance = Vector3(650, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	n_Move_L = {
		time = 0,
		anim_name = var_0_72.n_MoveL,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance = Vector3(0, 0, 0)
		}
	},
	n_Skill_1 = {
		time = 0,
		sound_trigger = "jiguang",
		anim_name = var_0_72.n_Skill_1
	},
	n_Skill_2 = {
		time = 0,
		sound_trigger = "guangjian",
		anim_name = var_0_72.n_Skill_2,
		over_offset = Vector3(0, 0),
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance = Vector3(300, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	n_Skill_3 = {
		time = 0,
		sound_trigger = "baozha1",
		anim_name = var_0_72.n_Skill_3
	},
	n_Combine = {
		sound_start = "bianshen",
		time = 0,
		camera = True,
		anim_name = var_0_72.n_Combine
	},
	n_DMG = {
		time = 0,
		anim_name = var_0_72.n_DMG,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance_m = Vector3(-150, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	n_DMG_S = {
		time = 0,
		anim_name = var_0_72.n_DMG
	},
	n_DMG_Back_R = {
		time = 0,
		anim_name = var_0_72.n_MoveR,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance = Vector3(0, 0, 0)
		}
	},
	n_Neutral = {
		time = 0,
		anim_name = var_0_72.n_Neutral
	},
	c_Atk = {
		time = 0,
		sound_trigger = "taosheng",
		anim_name = var_0_72.c_Atk,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance = Vector3(500, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	c_Skill_1 = {
		sound_trigger = "baozha2",
		time = 0,
		camera = True,
		anim_name = var_0_72.c_Skill_1
	},
	c_Dmg = {
		time = 0,
		anim_name = var_0_72.c_Dmg,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance_m = Vector3(-150, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	c_Dmg_S = {
		time = 0,
		anim_name = var_0_72.c_Dmg
	},
	c_MoveL = {
		time = 0,
		anim_name = var_0_72.c_MoveL,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance = Vector3(0, 0, 0)
		}
	},
	c_MoveR = {
		time = 0,
		anim_name = var_0_72.c_MoveR,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance = Vector3(650, 0, 0)
		}
	},
	c_DMG_Back_R = {
		time = 0,
		anim_name = var_0_72.c_MoveR,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance = Vector3(0, 0, 0)
		}
	},
	c_Neutral = {
		time = 0,
		anim_name = var_0_72.c_Neutral
	}
}
local var_0_74 = {
	{
		special_time = False,
		name = "normalAtk",
		power_index = 0,
		atk_index = 1,
		score = {
			100,
			100
		},
		grid_index = {
			1,
			2,
			3
		},
		actions = {
			var_0_73.n_Atk,
			var_0_73.n_Move_L
		}
	},
	{
		special_time = False,
		name = "skill1",
		power_index = 1,
		atk_index = 2,
		score = {
			500,
			500
		},
		grid_index = {
			1
		},
		actions = {
			var_0_73.n_Skill_1
		}
	},
	{
		special_time = False,
		name = "skill2",
		power_index = 2,
		atk_index = 2,
		score = {
			500,
			500
		},
		grid_index = {
			2
		},
		actions = {
			var_0_73.n_Skill_2,
			var_0_73.n_Move_L
		}
	},
	{
		special_time = False,
		name = "skill3",
		power_index = 3,
		atk_index = 2,
		score = {
			500,
			500
		},
		grid_index = {
			3
		},
		actions = {
			var_0_73.n_Skill_3
		}
	},
	{
		dmg_index = 2,
		name = "DMG",
		power_index = 0,
		special_time = False,
		grid_index = {
			1,
			2,
			3
		},
		actions = {
			var_0_73.n_DMG,
			var_0_73.n_DMG_Back_R
		}
	},
	{
		dmg_index = 1,
		name = "DMGS",
		power_index = 0,
		special_time = False,
		grid_index = {
			1,
			2,
			3
		},
		actions = {
			var_0_73.n_DMG_S
		}
	},
	{
		special_end = True,
		name = "special_end",
		power_index = 0,
		special_time = False,
		grid_index = {
			1,
			2,
			3
		},
		actions = {
			var_0_73.n_DMG_Back_R
		}
	},
	{
		dmg_index = 3,
		name = "DMGN",
		special_time = False,
		actions = {
			var_0_73.n_DMG
		}
	},
	{
		name = "DMG_BACK",
		special_time = False,
		dmg_back = True,
		actions = {
			var_0_73.n_DMG_Back_R
		}
	},
	{
		power_index = 0,
		name = "Combine",
		special_trigger = True,
		anim_bool = "special",
		special_time = True,
		grid_index = {
			1,
			2,
			3
		},
		actions = {
			var_0_73.n_Combine
		}
	},
	{
		special_time = True,
		name = "AtkS",
		power_index = 0,
		atk_index = 1,
		score = {
			300,
			300
		},
		grid_index = {
			1,
			2,
			3
		},
		actions = {
			var_0_73.c_Atk,
			var_0_73.c_MoveL
		}
	},
	{
		special_time = True,
		name = "Skill1S",
		power_index = 1,
		atk_index = 2,
		score = {
			1000,
			1000
		},
		grid_index = {
			1
		},
		actions = {
			var_0_73.c_Skill_1
		}
	},
	{
		special_time = True,
		name = "Skill1S",
		power_index = 2,
		atk_index = 2,
		score = {
			1000,
			1000
		},
		grid_index = {
			2
		},
		actions = {
			var_0_73.c_Skill_1
		}
	},
	{
		special_time = True,
		name = "Skill1S",
		power_index = 3,
		atk_index = 2,
		score = {
			1000,
			1000
		},
		grid_index = {
			3
		},
		actions = {
			var_0_73.c_Skill_1
		}
	},
	{
		dmg_index = 2,
		name = "cDmg",
		power_index = 0,
		special_time = True,
		grid_index = {
			1,
			2,
			3
		},
		actions = {
			var_0_73.c_Dmg,
			var_0_73.c_DMG_Back_R
		}
	},
	{
		dmg_index = 1,
		name = "cDmgS",
		power_index = 0,
		special_time = True,
		grid_index = {
			1,
			2,
			3
		},
		actions = {
			var_0_73.c_Dmg_S
		}
	},
	{
		dmg_index = 3,
		name = "DMGN",
		special_time = False,
		actions = {
			var_0_73.c_DMG
		}
	},
	{
		name = "DMG_BACK",
		special_time = False,
		dmg_back = True,
		actions = {
			var_0_73.c_DMG_Back_R
		}
	}
}
local var_0_75 = {
	c_Skill_1 = "c_Skill_1",
	n_Neutral = "n_Neutral",
	n_Combine = "n_Combine",
	n_Skill_2 = "n_Skill_2",
	n_MoveL = "n_MoveL",
	n_Atk = "n_Atk",
	c_Neutral = "c_Neutral",
	n_MoveR = "n_MoveR",
	c_Atk = "c_ATK",
	n_Skill_1 = "n_Skill_1",
	c_MoveL = "c_MoveL",
	c_Dmg = "c_DMG",
	n_Skill_3 = "n_Skill_3",
	n_DMG = "n_DMG",
	c_MoveR = "c_MoveR"
}
local var_0_76 = {
	n_Move_R = {
		time = 0,
		anim_name = var_0_75.n_MoveR,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance = Vector3(500, 0, 0)
		}
	},
	n_Atk = {
		time = 0,
		sound_trigger = "taosheng",
		anim_name = var_0_75.n_Atk,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance = Vector3(600, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	n_Move_L = {
		time = 0,
		anim_name = var_0_75.n_MoveL,
		move = {
			time = 0.4,
			start = Vector2(0, 0),
			distance = Vector3(0, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	n_Skill_1 = {
		time = 0,
		sound_trigger = "baozha1",
		anim_name = var_0_75.n_Skill_1,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance = Vector3(600, 0, 0)
		}
	},
	n_Skill_2 = {
		time = 0,
		sound_trigger = "baozha2",
		anim_name = var_0_75.n_Skill_2
	},
	n_Skill_3 = {
		time = 0,
		sound_trigger = "baozha2",
		anim_name = var_0_75.n_Skill_3,
		over_offset = Vector3(247, 2),
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance = Vector3(350, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	n_Combine = {
		sound_start = "bianshen",
		time = 0,
		camera = True,
		anim_name = var_0_75.n_Combine
	},
	n_DMG = {
		time = 0,
		anim_name = var_0_75.n_DMG,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance_m = Vector3(-150, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	n_DMG_S = {
		time = 0,
		anim_name = var_0_75.n_DMG
	},
	n_DMG_Back_R = {
		time = 0,
		anim_name = var_0_75.n_MoveR,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance = Vector3(0, 0, 0)
		}
	},
	n_Neutral = {
		time = 0,
		anim_name = var_0_75.n_Neutral
	},
	c_Atk = {
		time = 0,
		sound_trigger = "taosheng",
		anim_name = var_0_75.c_Atk,
		move = {
			time = 0.4,
			start = Vector2(0, 0),
			distance = Vector3(600, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	c_Skill_1 = {
		sound_trigger = "baozha2",
		time = 0,
		camera = True,
		anim_name = var_0_75.c_Skill_1
	},
	c_Dmg = {
		time = 0,
		anim_name = var_0_75.c_Dmg,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance_m = Vector3(-150, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	c_Dmg_S = {
		time = 0,
		anim_name = var_0_75.c_Dmg
	},
	c_MoveL = {
		time = 0,
		anim_name = var_0_75.c_MoveL,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance = Vector3(0, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	c_MoveR = {
		time = 0,
		anim_name = var_0_75.c_MoveR,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance = Vector3(650, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	c_DMG_Back_R = {
		time = 0,
		anim_name = var_0_75.c_MoveR,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance = Vector3(0, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	c_Neutral = {
		time = 0,
		anim_name = var_0_75.c_Neutral
	}
}
local var_0_77 = {
	{
		special_time = False,
		name = "normalAtk",
		power_index = 0,
		atk_index = 1,
		score = {
			100,
			100
		},
		grid_index = {
			1,
			2,
			3
		},
		actions = {
			var_0_76.n_Atk,
			var_0_76.n_Move_L
		}
	},
	{
		special_time = False,
		name = "skill1",
		power_index = 1,
		atk_index = 2,
		score = {
			500,
			500
		},
		grid_index = {
			1
		},
		actions = {
			var_0_76.n_Move_R,
			var_0_76.n_Skill_1,
			var_0_76.n_Move_L
		}
	},
	{
		special_time = False,
		name = "skill2",
		power_index = 2,
		atk_index = 2,
		score = {
			500,
			500
		},
		grid_index = {
			2
		},
		actions = {
			var_0_76.n_Skill_2
		}
	},
	{
		special_time = False,
		name = "skill3",
		power_index = 3,
		atk_index = 2,
		score = {
			500,
			500
		},
		grid_index = {
			3
		},
		actions = {
			var_0_76.n_Skill_3,
			var_0_76.n_Move_L
		}
	},
	{
		dmg_index = 2,
		name = "n_DMG",
		power_index = 0,
		special_time = False,
		grid_index = {
			1,
			2,
			3
		},
		actions = {
			var_0_76.n_DMG,
			var_0_76.n_DMG_Back_R
		}
	},
	{
		dmg_index = 1,
		name = "n_DMGS",
		power_index = 0,
		special_time = False,
		grid_index = {
			1,
			2,
			3
		},
		actions = {
			var_0_76.n_DMG_S
		}
	},
	{
		special_end = True,
		name = "special_end",
		power_index = 0,
		special_time = False,
		grid_index = {
			1,
			2,
			3
		},
		actions = {
			var_0_76.n_DMG_Back_R
		}
	},
	{
		dmg_index = 3,
		name = "DMGN",
		special_time = False,
		actions = {
			var_0_76.n_DMG
		}
	},
	{
		name = "DMG_BACK",
		special_time = False,
		dmg_back = True,
		actions = {
			var_0_76.n_DMG_Back_R
		}
	},
	{
		power_index = 0,
		name = "Combine",
		special_trigger = True,
		anim_bool = "special",
		special_time = True,
		grid_index = {
			1,
			2,
			3
		},
		actions = {
			var_0_76.n_Combine
		}
	},
	{
		special_time = True,
		name = "AtkS",
		power_index = 0,
		atk_index = 1,
		score = {
			200,
			200
		},
		grid_index = {
			1,
			2,
			3
		},
		actions = {
			var_0_76.c_Atk,
			var_0_76.c_MoveL
		}
	},
	{
		special_time = True,
		name = "Skill1S",
		power_index = 1,
		atk_index = 2,
		score = {
			1000,
			1000
		},
		grid_index = {
			1
		},
		actions = {
			var_0_76.c_Skill_1
		}
	},
	{
		special_time = True,
		name = "Skill1S",
		power_index = 2,
		atk_index = 2,
		score = {
			1000,
			1000
		},
		grid_index = {
			2
		},
		actions = {
			var_0_76.c_Skill_1
		}
	},
	{
		special_time = True,
		name = "Skill1S",
		power_index = 3,
		atk_index = 2,
		score = {
			1000,
			1000
		},
		grid_index = {
			3
		},
		actions = {
			var_0_76.c_Skill_1
		}
	},
	{
		dmg_index = 2,
		name = "c_Dmg",
		power_index = 0,
		special_time = True,
		grid_index = {
			1,
			2,
			3
		},
		actions = {
			var_0_76.c_Dmg,
			var_0_76.c_DMG_Back_R
		}
	},
	{
		dmg_index = 1,
		name = "c_DmgS",
		power_index = 0,
		special_time = True,
		grid_index = {
			1,
			2,
			3
		},
		actions = {
			var_0_76.c_Dmg_S
		}
	},
	{
		dmg_index = 3,
		name = "DMGN",
		special_time = False,
		actions = {
			var_0_76.c_DMG
		}
	},
	{
		name = "DMG_BACK",
		special_time = False,
		dmg_back = True,
		actions = {
			var_0_76.c_DMG_Back_R
		}
	}
}
local var_0_78 = {
	c_Skill_1 = "c_Skill_1",
	n_Neutral = "n_Neutral",
	n_Combine = "n_Combine",
	n_Skill_2 = "n_Skill_2",
	n_MoveL = "n_MoveL",
	n_Atk = "n_Atk",
	c_Neutral = "c_Neutral",
	n_MoveR = "n_MoveR",
	c_Atk = "c_Atk",
	n_Skill_1 = "n_Skill_1",
	c_MoveL = "c_MoveL",
	c_Dmg = "c_Dmg",
	n_Skill_3 = "n_Skill_3",
	n_DMG = "n_DMG",
	c_MoveR = "c_MoveR"
}
local var_0_79 = {
	n_Move_R = {
		time = 0,
		anim_name = var_0_78.n_MoveR,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance = Vector3(650, 0, 0)
		}
	},
	n_Atk = {
		time = 0,
		sound_trigger = "taosheng",
		anim_name = var_0_78.n_Atk,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance = Vector3(650, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	n_Move_L = {
		time = 0,
		anim_name = var_0_78.n_MoveL,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance = Vector3(0, 0, 0)
		}
	},
	n_Skill_1 = {
		time = 0,
		sound_trigger = "jiguang",
		anim_name = var_0_78.n_Skill_1
	},
	n_Skill_2 = {
		time = 0,
		sound_trigger = "guangjian",
		anim_name = var_0_78.n_Skill_2,
		over_offset = Vector3(0, 0),
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance = Vector3(300, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	n_Skill_3 = {
		time = 0,
		sound_trigger = "baozha1",
		anim_name = var_0_78.n_Skill_3
	},
	n_Combine = {
		sound_start = "bianshen",
		time = 0,
		camera = True,
		anim_name = var_0_78.n_Combine,
		camera_pos = Vector2(0, 0)
	},
	n_DMG = {
		time = 0,
		anim_name = var_0_78.n_DMG,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance_m = Vector3(-150, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	n_DMG_S = {
		time = 0,
		anim_name = var_0_78.n_DMG
	},
	n_DMG_Back_R = {
		time = 0,
		anim_name = var_0_78.n_MoveR,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance = Vector3(0, 0, 0)
		}
	},
	n_Neutral = {
		time = 0,
		anim_name = var_0_78.n_Neutral
	},
	c_Atk = {
		time = 0,
		sound_trigger = "taosheng",
		anim_name = var_0_78.c_Atk,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance = Vector3(500, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	c_Skill_1 = {
		sound_trigger = "baozha2",
		time = 0,
		camera = True,
		anim_name = var_0_78.c_Skill_1
	},
	c_Dmg = {
		time = 0,
		anim_name = var_0_78.c_Dmg,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance_m = Vector3(-150, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	c_Dmg_S = {
		time = 0,
		anim_name = var_0_78.c_Dmg
	},
	c_MoveL = {
		time = 0,
		anim_name = var_0_78.c_MoveL,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance = Vector3(0, 0, 0)
		}
	},
	c_MoveR = {
		time = 0,
		anim_name = var_0_78.c_MoveR,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance = Vector3(650, 0, 0)
		}
	},
	c_DMG_Back_R = {
		time = 0,
		anim_name = var_0_78.c_MoveR,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance = Vector3(0, 0, 0)
		}
	},
	c_Neutral = {
		time = 0,
		anim_name = var_0_78.c_Neutral
	}
}
local var_0_80 = {
	{
		special_time = False,
		name = "normalAtk",
		power_index = 0,
		atk_index = 1,
		score = {
			100,
			100
		},
		grid_index = {
			1,
			2,
			3
		},
		actions = {
			var_0_79.n_Atk,
			var_0_79.n_Move_L
		}
	},
	{
		special_time = False,
		name = "skill1",
		power_index = 1,
		atk_index = 2,
		score = {
			500,
			500
		},
		grid_index = {
			1
		},
		actions = {
			var_0_79.n_Skill_1
		}
	},
	{
		special_time = False,
		name = "skill2",
		power_index = 2,
		atk_index = 3,
		score = {
			500,
			500
		},
		grid_index = {
			2
		},
		actions = {
			var_0_79.n_Skill_2,
			var_0_79.n_Move_L
		}
	},
	{
		special_time = False,
		name = "skill3",
		power_index = 3,
		atk_index = 2,
		score = {
			500,
			500
		},
		grid_index = {
			3
		},
		actions = {
			var_0_79.n_Skill_3
		}
	},
	{
		dmg_index = 2,
		name = "DMG",
		power_index = 0,
		special_time = False,
		grid_index = {
			1,
			2,
			3
		},
		actions = {
			var_0_79.n_DMG,
			var_0_79.n_DMG_Back_R
		}
	},
	{
		dmg_index = 1,
		name = "DMGS",
		power_index = 0,
		special_time = False,
		grid_index = {
			1,
			2,
			3
		},
		actions = {
			var_0_79.n_DMG_S
		}
	},
	{
		special_end = True,
		name = "special_end",
		power_index = 0,
		special_time = False,
		grid_index = {
			1,
			2,
			3
		},
		actions = {
			var_0_79.n_DMG_Back_R
		},
		anim_init_pos = Vector2(586, 471)
	},
	{
		dmg_index = 3,
		name = "DMGN",
		special_time = False,
		actions = {
			var_0_79.DMG
		}
	},
	{
		name = "DMG_BACK",
		special_time = False,
		dmg_back = True,
		actions = {
			var_0_79.DMG_Back_R
		}
	},
	{
		special_trigger = True,
		name = "Combine",
		power_index = 0,
		anim_bool = "special",
		special_time = True,
		grid_index = {
			1,
			2,
			3
		},
		actions = {
			var_0_79.n_Combine
		},
		anim_trigger_pos = Vector2(-58, 350),
		anim_end_pos = Vector2(225, 471)
	},
	{
		special_time = True,
		name = "AtkS",
		power_index = 0,
		atk_index = 1,
		score = {
			300,
			300
		},
		grid_index = {
			1,
			2,
			3
		},
		actions = {
			var_0_79.c_Atk,
			var_0_79.c_MoveL
		}
	},
	{
		special_time = True,
		name = "Skill1S",
		power_index = 1,
		atk_index = 2,
		score = {
			1000,
			1000
		},
		grid_index = {
			1
		},
		actions = {
			var_0_79.c_Skill_1
		}
	},
	{
		special_time = True,
		name = "Skill1S",
		power_index = 2,
		atk_index = 2,
		score = {
			1000,
			1000
		},
		grid_index = {
			2
		},
		actions = {
			var_0_79.c_Skill_1
		}
	},
	{
		special_time = True,
		name = "Skill1S",
		power_index = 3,
		atk_index = 2,
		score = {
			1000,
			1000
		},
		grid_index = {
			3
		},
		actions = {
			var_0_79.c_Skill_1
		}
	},
	{
		dmg_index = 2,
		name = "cDmg",
		power_index = 0,
		special_time = True,
		grid_index = {
			1,
			2,
			3
		},
		actions = {
			var_0_79.c_Dmg,
			var_0_79.c_DMG_Back_R
		}
	},
	{
		dmg_index = 1,
		name = "cDmgS",
		power_index = 0,
		special_time = True,
		grid_index = {
			1,
			2,
			3
		},
		actions = {
			var_0_79.c_Dmg_S
		}
	},
	{
		dmg_index = 3,
		name = "DMGN",
		special_time = False,
		actions = {
			var_0_79.DMG
		}
	},
	{
		name = "DMG_BACK",
		special_time = False,
		dmg_back = True,
		actions = {
			var_0_79.DMG_Back_R
		}
	}
}
local var_0_81 = {
	Neutral = "Neutral",
	Skill_1 = "skill_1",
	Skill_2 = "skill_2",
	Atk = "ATK",
	MoveL = "MoveL",
	DMG = "DMG",
	MoveR = "MoveR"
}
local var_0_82 = {
	Move_R = {
		time = 0,
		anim_name = var_0_81.MoveR,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance = Vector3(500, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	Atk = {
		time = 0,
		sound_trigger = "taosheng",
		anim_name = var_0_81.Atk,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance = Vector3(600, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	Move_L = {
		time = 0,
		anim_name = var_0_81.MoveL,
		move = {
			time = 0.4,
			distance = Vector3(0, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	Skill_1 = {
		time = 0,
		sound_trigger = "jiguang",
		anim_name = var_0_81.Skill_1
	},
	Skill_2 = {
		time = 0,
		sound_trigger = "baozha2",
		anim_name = var_0_81.Skill_2,
		over_offset = Vector2(115, 0)
	},
	DMG = {
		time = 0,
		anim_name = var_0_81.DMG,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance_m = Vector3(-150, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	DMG_Back_R = {
		time = 0,
		anim_name = var_0_81.MoveR,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance = Vector3(0, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	DMG_S = {
		time = 0,
		anim_name = var_0_81.DMG
	},
	Neutral = {
		time = 0,
		anim_name = var_0_81.Neutral
	}
}
local var_0_83 = {
	{
		special_time = False,
		name = "normalAtk",
		power_index = 0,
		atk_index = 1,
		score = {
			100,
			100
		},
		grid_index = {
			1,
			2,
			3
		},
		actions = {
			var_0_82.Atk,
			var_0_82.Move_L
		}
	},
	{
		special_time = False,
		name = "skill1",
		power_index = 1,
		atk_index = 2,
		score = {
			500,
			500
		},
		grid_index = {
			1
		},
		actions = {
			var_0_82.Skill_1
		}
	},
	{
		special_time = False,
		name = "skill2",
		power_index = 2,
		atk_index = 2,
		score = {
			500,
			500
		},
		grid_index = {
			2,
			3
		},
		actions = {
			var_0_82.Move_R,
			var_0_82.Skill_2,
			var_0_82.Move_L
		}
	},
	{
		dmg_index = 2,
		name = "DMG",
		special_time = False,
		actions = {
			var_0_82.DMG,
			var_0_82.DMG_Back_R
		}
	},
	{
		dmg_index = 1,
		name = "DMG_Stand",
		special_time = False,
		actions = {
			var_0_82.DMG_S
		}
	},
	{
		dmg_index = 3,
		name = "DMGN",
		special_time = False,
		actions = {
			var_0_82.DMG
		}
	},
	{
		name = "DMG_BACK",
		special_time = False,
		dmg_back = True,
		actions = {
			var_0_82.DMG_Back_R
		}
	}
}
local var_0_84 = {
	Neutral = "Neutral",
	Skill_1 = "skill_1",
	Skill_2 = "skill_2",
	Atk = "ATK",
	MoveL = "MoveL",
	DMG = "DMG",
	MoveR = "MoveR"
}
local var_0_85 = {
	Move_R = {
		time = 0,
		anim_name = var_0_84.MoveR,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance = Vector3(500, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	Atk = {
		time = 0,
		sound_trigger = "taosheng",
		anim_name = var_0_84.Atk,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance = Vector3(600, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	Move_L = {
		time = 0,
		anim_name = var_0_84.MoveL,
		move = {
			time = 0.4,
			distance = Vector3(0, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	Skill_1 = {
		time = 0,
		sound_trigger = "jiguang",
		anim_name = var_0_84.Skill_1
	},
	Skill_2 = {
		time = 0,
		sound_trigger = "baozha2",
		anim_name = var_0_84.Skill_2,
		over_offset = Vector2(264, 0)
	},
	DMG = {
		time = 0,
		anim_name = var_0_84.DMG,
		move = {
			time = 0.3,
			distance_m = Vector3(-150, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	DMG_Back_R = {
		time = 0,
		anim_name = var_0_84.MoveR,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance = Vector3(0, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	DMG_S = {
		time = 0,
		anim_name = var_0_84.DMG
	},
	Neutral = {
		time = 0,
		anim_name = var_0_84.Neutral
	}
}
local var_0_86 = {
	{
		special_time = False,
		name = "normalAtk",
		power_index = 0,
		atk_index = 1,
		score = {
			100,
			100
		},
		grid_index = {
			1,
			2,
			3
		},
		actions = {
			var_0_85.Atk,
			var_0_85.Move_L
		}
	},
	{
		special_time = False,
		name = "skill1",
		power_index = 1,
		atk_index = 2,
		score = {
			500,
			500
		},
		grid_index = {
			1
		},
		actions = {
			var_0_85.Skill_1
		}
	},
	{
		special_time = False,
		name = "skill2",
		power_index = 2,
		atk_index = 2,
		score = {
			500,
			500
		},
		grid_index = {
			2,
			3
		},
		actions = {
			var_0_85.Skill_2,
			var_0_85.Move_L
		}
	},
	{
		dmg_index = 2,
		name = "DMG",
		special_time = False,
		actions = {
			var_0_85.DMG,
			var_0_85.DMG_Back_R
		}
	},
	{
		dmg_index = 1,
		name = "DMG_Stand",
		special_time = False,
		actions = {
			var_0_85.DMG_S
		}
	},
	{
		dmg_index = 3,
		name = "DMGN",
		special_time = False,
		actions = {
			var_0_85.DMG
		}
	},
	{
		name = "DMG_BACK",
		special_time = False,
		dmg_back = True,
		actions = {
			var_0_85.DMG_Back_R
		}
	}
}
local var_0_87 = {
	{
		index = 1,
		name = "role1",
		skill = var_0_74,
		actions = var_0_73
	},
	{
		index = 2,
		name = "role2",
		skill = var_0_77,
		actions = var_0_76
	},
	{
		index = 3,
		name = "enemy1",
		skill = var_0_83,
		actions = var_0_82
	},
	{
		index = 4,
		name = "enemy2",
		skill = var_0_86,
		actions = var_0_85
	},
	{
		index = 5,
		name = "role3",
		skill = var_0_80,
		actions = var_0_79,
		anim_init_pos = Vector2(586, 411)
	}
}

local function var_0_88(arg_1_0, arg_1_1)
	local var_1_0 = {
		def ctor:(arg_2_0)
			arg_2_0._boxTf = arg_1_0
			arg_2_0._event = arg_1_1

			arg_2_0._event.bind(var_0_15, function()
				local var_3_0 = var_0_23.power_grid

				if var_3_0 and var_3_0 > 0 and var_0_35[var_3_0]:
					local var_3_1 = var_0_35[var_3_0]
					local var_3_2 = var_3_1.rule
					local var_3_3 = var_3_1.id and var_3_1.id or var_3_0

					table.insert(arg_2_0.ruleGridList, {
						id = var_3_3,
						rule = var_3_2
					}))

			arg_2_0._gridEffect = findTF(arg_2_0._boxTf, "effectGrid")
			arg_2_0._content = findTF(arg_2_0._boxTf, "viewport/content")
			arg_2_0.tplGrid = findTF(arg_1_0, "tplGrid")

			setActive(arg_2_0.tplGrid, False)

			arg_2_0.grids = {}
			arg_2_0.effects = {}
			arg_2_0.combo = 0
			arg_2_0.ruleGridList = {}

			for iter_2_0 = 1, var_0_24:
				local var_2_0 = tf(instantiate(arg_2_0._gridEffect))

				setParent(var_2_0, arg_2_0._content)
				setActive(var_2_0, False)

				var_2_0.anchoredPosition = Vector2(var_0_26.x * iter_2_0 - var_0_26.x / 2, var_0_26.y / 2)

				table.insert(arg_2_0.effects, var_2_0),
		def start:(arg_4_0)
			arg_4_0.comboCheck = False

			arg_4_0.initGrids(False)

			for iter_4_0 = 1, #arg_4_0.effects:
				setActive(arg_4_0.effects[iter_4_0], False),
		def step:(arg_5_0)
			if arg_5_0.takeAwayTime and arg_5_0.takeAwayTime > 0:
				arg_5_0.takeAwayTime = arg_5_0.takeAwayTime - Time.deltaTime

				return

			arg_5_0.gridCreateIndex = 1

			local var_5_0 = False

			for iter_5_0 = 1, #arg_5_0.grids:
				local var_5_1 = arg_5_0.grids[iter_5_0]
				local var_5_2 = iter_5_0

				if not var_5_1.moveAble:
					var_5_0 = var_5_0 or True

					local var_5_3 = (iter_5_0 - 1) * var_0_26.x

					if var_5_3 < var_5_1.tf.anchoredPosition.x:
						var_5_1.tf.anchoredPosition = Vector2(var_5_1.tf.anchoredPosition.x - var_5_1.speed * Time.deltaTime, 0)

						if var_5_1.speed < var_0_27:
							var_5_1.speed = var_5_1.speed + var_0_29

					if var_5_3 >= var_5_1.tf.anchoredPosition.x:
						var_5_1.speed = 0
						var_5_1.moveAble = True

						if var_5_3 > var_5_1.tf.anchoredPosition.x:
							var_5_1.tf.anchoredPosition = Vector2(var_5_3, 0)

				if not var_5_1.eventAble:
					GetComponent(var_5_1.tf, typeof(EventTriggerListener)).AddPointDownFunc(function()
						if arg_5_0.comboCheck == False:
							local var_6_0, var_6_1 = arg_5_0.triggerDownGrid(var_5_2)

							if #var_6_0 >= 2:
								arg_5_0.comboCheck = True

								local var_6_2 = arg_5_0.getGridDouble(var_6_0)

								arg_5_0.takeAwayGrid(var_6_0)
								arg_5_0.insertGrids()

								for iter_6_0 = 1, #var_6_1:
									local var_6_3 = var_6_1[iter_6_0].index
									local var_6_4 = var_6_1[iter_6_0].count

									arg_5_0._event.emit(var_0_14, {
										series = var_6_4,
										combo = arg_5_0.combo,
										index = var_6_3,
										double = var_6_2
									})

								arg_5_0.combo = arg_5_0.combo + 1
							else
								arg_5_0.comboCheck = True

								arg_5_0.takeAwayGrid({
									var_5_2
								})
								arg_5_0.insertGrids())

					var_5_1.eventAble = True

			if not var_5_0 and arg_5_0.comboCheck:
				local var_5_4 = arg_5_0.getSeriesGrids()

				if #var_5_4 > 0:
					local var_5_5 = {}

					for iter_5_1 = 1, #var_5_4:
						local var_5_6 = var_5_4[iter_5_1].series
						local var_5_7 = var_5_4[iter_5_1].index
						local var_5_8 = var_5_4[iter_5_1].double

						for iter_5_2 = 1, #var_5_6:
							table.insert(var_5_5, var_5_6[iter_5_2])

						local var_5_9 = arg_5_0.getGridDouble(var_5_6)

						arg_5_0._event.emit(var_0_14, {
							series = #var_5_6,
							combo = arg_5_0.combo,
							index = var_5_7,
							double = var_5_9
						})

					arg_5_0.clearGridSeriesAble()
					arg_5_0.takeAwayGrid(var_5_5)
					arg_5_0.insertGrids()

					arg_5_0.comboCheck = True
					arg_5_0.combo = arg_5_0.combo + 1
				else
					arg_5_0.comboCheck = False
					arg_5_0.combo = 0,
		def getGridDouble:(arg_7_0, arg_7_1)
			for iter_7_0 = 1, #arg_7_1:
				if arg_7_0.grids[iter_7_0] and arg_7_0.grids[iter_7_0].rule == var_0_32:
					return True

			return False,
		def clear:(arg_8_0)
			for iter_8_0 = 1, #arg_8_0.grids:
				if arg_8_0.grids[iter_8_0].tf:
					destroy(arg_8_0.grids[iter_8_0].tf)

			arg_8_0.grids = {}
			arg_8_0.gridCreateIndex = 1
			arg_8_0.ruleGridList = {},
		def clearGridSeriesAble:(arg_9_0)
			for iter_9_0 = 1, #arg_9_0.grids:
				if arg_9_0.grids[iter_9_0].seriesAble:
					arg_9_0.grids[iter_9_0].seriesAble = False,
		def getSeriesGrids:(arg_10_0)
			local var_10_0 = {}
			local var_10_1
			local var_10_2 = {}
			local var_10_3 = {}
			local var_10_4
			local var_10_5
			local var_10_6 = 0
			local var_10_7 = False

			for iter_10_0 = 1, #arg_10_0.grids:
				if var_10_5 and var_10_5 == arg_10_0.grids[iter_10_0].index:
					var_10_6 = var_10_6 + 1
				elif arg_10_0.grids[iter_10_0].rule == var_0_31:
					var_10_6 = var_10_6 + 1
				elif var_10_7:
					var_10_5 = arg_10_0.grids[iter_10_0].index
					var_10_7 = False
				else
					if var_10_6 >= 3 and arg_10_0.checkGridComboFlag(var_10_3):
						table.insert(var_10_0, {
							series = var_10_3,
							index = var_10_5
						})

					local var_10_8 = arg_10_0.grids[iter_10_0]

					var_10_5 = var_10_8.index
					var_10_6 = 1
					var_10_7 = var_10_8.rule == var_0_31
					var_10_3 = {}

				table.insert(var_10_3, iter_10_0)

				if iter_10_0 == #arg_10_0.grids and #var_10_3 >= 3 and arg_10_0.checkGridComboFlag(var_10_3):
					table.insert(var_10_0, {
						series = var_10_3,
						index = var_10_5
					})

					var_10_3 = {}

			return var_10_0,
		def checkGridComboFlag:(arg_11_0, arg_11_1)
			for iter_11_0 = 1, #arg_11_1:
				if arg_11_0.grids[arg_11_1[iter_11_0]].seriesAble and iter_11_0 != #arg_11_1:
					return True

			return False,
		def insertGrids:(arg_12_0)
			local var_12_0 = var_0_24 - #arg_12_0.grids

			for iter_12_0 = 1, var_12_0:
				local var_12_1 = arg_12_0.createGridData()

				table.insert(arg_12_0.grids, var_12_1)

			if arg_12_0.checkGridsMatchAble():
				arg_12_0.instiateGrids(True)
			else
				arg_12_0.initGrids(True)

			arg_12_0.changeAbleGrids(),
		def changeAbleGrids:(arg_13_0)
			for iter_13_0 = 1, #arg_13_0.grids:
				arg_13_0.grids[iter_13_0].moveAble = False
				arg_13_0.grids[iter_13_0].eventAble = False
				arg_13_0.grids[iter_13_0].speed = var_0_28,
		def takeAwayGrid:(arg_14_0, arg_14_1)
			table.sort(arg_14_1, function(arg_15_0, arg_15_1)
				return arg_15_0 <= arg_15_1)

			arg_14_0.takeAwayTime = var_0_25

			local var_14_0 = {}
			local var_14_1 = arg_14_1[1] - 1

			if var_14_1 > 0:
				arg_14_0.grids[var_14_1].seriesAble = True

			pg.CriMgr.GetInstance().PlaySoundEffect_V3("event./ui/" .. "xiaochu")

			for iter_14_0 = #arg_14_1, 1, -1:
				table.insert(var_14_0, table.remove(arg_14_0.grids, arg_14_1[iter_14_0]))
				setActive(arg_14_0.effects[arg_14_1[iter_14_0]], False)
				setActive(arg_14_0.effects[arg_14_1[iter_14_0]], True)

			for iter_14_1 = 1, #var_14_0:
				destroy(var_14_0[iter_14_1].tf)

				var_14_0[iter_14_1] = 0

			local var_14_2 = {},
		def triggerDownGrid:(arg_16_0, arg_16_1)
			local var_16_0 = arg_16_0.grids[arg_16_1]
			local var_16_1
			local var_16_2 = var_16_0.rule
			local var_16_3 = {}
			local var_16_4 = {}

			if var_16_2 != var_0_31:
				var_16_3 = {
					arg_16_1
				}
				var_16_1 = var_16_0.index

			if not var_16_0:
				return var_16_3, {}

			if var_16_2 == var_0_31:
				local var_16_5
				local var_16_6 = True
				local var_16_7 = {}

				for iter_16_0 = arg_16_1 - 1, 1, -1:
					if var_16_6:
						if arg_16_0.grids[iter_16_0].rule == var_0_31:
							table.insert(var_16_7, iter_16_0)
						elif not var_16_5:
							var_16_5 = arg_16_0.grids[iter_16_0].index

							table.insert(var_16_7, iter_16_0)
						elif var_16_5 == arg_16_0.grids[iter_16_0].index:
							table.insert(var_16_7, iter_16_0)
						else
							var_16_6 = False

				local var_16_8
				local var_16_9 = True
				local var_16_10 = {}

				for iter_16_1 = arg_16_1 + 1, #arg_16_0.grids:
					if var_16_9:
						if arg_16_0.grids[iter_16_1].rule == var_0_31:
							table.insert(var_16_10, iter_16_1)
						elif not var_16_8:
							var_16_8 = arg_16_0.grids[iter_16_1].index

							table.insert(var_16_10, iter_16_1)
						elif var_16_8 == arg_16_0.grids[iter_16_1].index:
							table.insert(var_16_10, iter_16_1)
						else
							var_16_9 = False

				if var_16_5 == None and var_16_8 == None:
					for iter_16_2 = 1, #arg_16_0.grids:
						table.insert(var_16_3, iter_16_2)
				elif var_16_5 == var_16_8:
					for iter_16_3 = 1, #var_16_7:
						table.insert(var_16_3, var_16_7[iter_16_3])

					table.insert(var_16_3, arg_16_1)

					for iter_16_4 = 1, #var_16_10:
						table.insert(var_16_3, var_16_10[iter_16_4])

					var_16_1 = var_16_5
				else
					if #var_16_7 >= #var_16_10:
						for iter_16_5 = 1, #var_16_7:
							table.insert(var_16_3, var_16_7[iter_16_5])

						var_16_1 = var_16_5
					else
						for iter_16_6 = 1, #var_16_10:
							table.insert(var_16_3, var_16_10[iter_16_6])

						var_16_1 = var_16_8

					table.insert(var_16_3, arg_16_1)

				table.insert(var_16_4, {
					index = var_16_1,
					count = #var_16_3
				})
			elif var_16_0.rule == var_0_30:
				local var_16_11
				local var_16_12
				local var_16_13 = var_16_0.index
				local var_16_14
				local var_16_15 = True
				local var_16_16 = {}

				for iter_16_7 = arg_16_1 - 1, 1, -1:
					if var_16_15:
						if arg_16_0.grids[iter_16_7].rule == var_0_31:
							table.insert(var_16_16, iter_16_7)
						elif not var_16_14:
							var_16_14 = arg_16_0.grids[iter_16_7].index

							table.insert(var_16_16, iter_16_7)
						elif var_16_14 == arg_16_0.grids[iter_16_7].index:
							table.insert(var_16_16, iter_16_7)
						else
							var_16_15 = False

				local var_16_17
				local var_16_18 = True
				local var_16_19 = {}

				for iter_16_8 = arg_16_1 + 1, #arg_16_0.grids:
					if var_16_18:
						if arg_16_0.grids[iter_16_8].rule == var_0_31:
							table.insert(var_16_19, iter_16_8)
						elif not var_16_17:
							var_16_17 = arg_16_0.grids[iter_16_8].index

							table.insert(var_16_19, iter_16_8)
						elif var_16_17 == arg_16_0.grids[iter_16_8].index:
							table.insert(var_16_19, iter_16_8)
						else
							var_16_18 = False

				table.insert(var_16_4, {
					index = var_16_14,
					count = #var_16_16 + 1
				})
				table.insert(var_16_4, {
					index = var_16_17,
					count = #var_16_19 + 1
				})

				for iter_16_9 = 1, #var_16_16:
					table.insert(var_16_3, var_16_16[iter_16_9])

				for iter_16_10 = 1, #var_16_19:
					table.insert(var_16_3, var_16_19[iter_16_10])
			else
				for iter_16_11 = arg_16_1 - 1, 1, -1:
					if arg_16_0.checkGridMatch(var_16_1, arg_16_0.grids[iter_16_11]):
						table.insert(var_16_3, iter_16_11)
					else
						break

				for iter_16_12 = arg_16_1 + 1, #arg_16_0.grids:
					if arg_16_0.checkGridMatch(var_16_1, arg_16_0.grids[iter_16_12]):
						table.insert(var_16_3, iter_16_12)
					else
						break

				table.insert(var_16_4, {
					index = var_16_1,
					count = #var_16_3
				})

			table.sort(var_16_3, function(arg_17_0, arg_17_1)
				return arg_17_0 < arg_17_1)

			return var_16_3, var_16_4,
		def checkGridMatch:(arg_18_0, arg_18_1, arg_18_2)
			if arg_18_1 == arg_18_2.index:
				return True
			elif arg_18_2.rule == var_0_31:
				return True

			return False,
		def initGrids:(arg_19_0, arg_19_1)
			arg_19_0.clear()

			for iter_19_0 = 1, var_0_24:
				local var_19_0 = arg_19_0.createGridData()

				table.insert(arg_19_0.grids, var_19_0)

			if arg_19_0.checkGridsMatchAble():
				arg_19_0.instiateGrids(arg_19_1)
			else
				arg_19_0.initGrids(arg_19_1)

			arg_19_0.comboCheck = False,
		def instiateGrids:(arg_20_0, arg_20_1)
			for iter_20_0 = 1, #arg_20_0.grids:
				local var_20_0 = arg_20_0.grids[iter_20_0]

				if not var_20_0.tf:
					local var_20_1 = tf(instantiate(arg_20_0.tplGrid))

					SetParent(var_20_1, arg_20_0._content)
					setActive(var_20_1, True)
					setActive(findTF(var_20_1, var_20_0.name), True)

					local var_20_2

					if arg_20_1:
						var_20_2 = (var_0_24 + arg_20_0.gridCreateIndex - 1) * var_0_26.x
					else
						var_20_2 = (arg_20_0.gridCreateIndex - 1) * var_0_26.x

					if var_20_0.rule == var_0_31:
						-- block empty

					if var_20_0.rule != var_0_31:
						setActive(findTF(var_20_1, var_20_0.name .. "/boom"), var_20_0.rule == var_0_30)
						setActive(findTF(var_20_1, var_20_0.name .. "/thunder"), var_20_0.rule == var_0_32)

					var_20_1.anchoredPosition = Vector2(var_20_2, 0)
					arg_20_0.gridCreateIndex = arg_20_0.gridCreateIndex + 1
					var_20_0.tf = var_20_1,
		def createGridData:(arg_21_0)
			local var_21_0
			local var_21_1
			local var_21_2
			local var_21_3

			if #arg_21_0.ruleGridList > 0:
				local var_21_4 = table.remove(arg_21_0.ruleGridList, 1)

				var_21_0 = var_21_4.id
				var_21_3 = var_21_4.rule
			else
				var_21_0 = var_0_34[math.random(1, #var_0_34)]

			local var_21_5 = var_0_33[var_21_0].name
			local var_21_6 = var_0_33[var_21_0].index

			return {
				eventAble = False,
				moveAble = False,
				speed = var_0_28,
				index = var_21_6,
				name = var_21_5,
				rule = var_21_3
			},
		def checkGridsMatchAble:(arg_22_0)
			return True
	}

	var_1_0.ctor()

	return var_1_0

local var_0_89 = False

local function var_0_90(arg_23_0, arg_23_1, arg_23_2)
	local var_23_0 = {
		def ctor:(arg_24_0)
			arg_24_0._specialTf = arg_23_0
			arg_24_0._successTf = arg_23_1
			arg_24_0._effectSuccess = findTF(arg_24_0._successTf, "effectSuccess")
			arg_24_0._event = arg_23_2

			arg_24_0._event.bind(var_0_14, function(arg_25_0, arg_25_1, arg_25_2)
				local var_25_0 = arg_25_1.series or 0
				local var_25_1 = arg_25_1.combo
				local var_25_2 = arg_25_1.index
				local var_25_3 = arg_25_1.double

				arg_24_0.addPowerAmount(var_25_2, arg_24_0.getPowerAmount(var_25_0, var_25_1, var_25_3)))

			arg_24_0.powers = {}

			for iter_24_0 = 1, #var_0_36:
				local var_24_0 = findTF(arg_24_0._specialTf, var_0_36[iter_24_0].name)
				local var_24_1 = var_0_36[iter_24_0].index
				local var_24_2 = var_0_36[iter_24_0].max
				local var_24_3 = var_0_36[iter_24_0].cur
				local var_24_4 = findTF(arg_24_0._specialTf, var_0_36[iter_24_0].name .. "/text")

				setActive(var_24_4, var_0_1)

				local var_24_5 = {
					active = False,
					tf = var_24_0,
					index = var_24_1,
					max = var_24_2,
					cur = var_24_3,
					text_tf = var_24_4
				}

				table.insert(arg_24_0.powers, var_24_5)

			arg_24_0._event.bind(var_0_20, function(arg_26_0, arg_26_1, arg_26_2)
				arg_24_0.inCameraFlag = True)
			arg_24_0._event.bind(var_0_21, function(arg_27_0, arg_27_1, arg_27_2)
				arg_24_0.inCameraFlag = False
				arg_24_0.inCameraFadeTime = 200)

			arg_24_0.successText = findTF(arg_24_0._successTf, "box/text")

			setActive(arg_24_0.successText, var_0_1)

			arg_24_0.success = {
				cur = 0,
				slider = GetComponent(findTF(arg_24_0._successTf, "box"), typeof(Slider)),
				max = var_0_45
			},
		def start:(arg_28_0)
			for iter_28_0 = 1, #arg_28_0.powers:
				local var_28_0 = arg_28_0.powers[iter_28_0]

				var_28_0.cur = 0
				var_28_0.active = False

			arg_28_0.inCameraFlag = False
			arg_28_0.inCameraFadeTime = 0
			arg_28_0.success.cur = 0
			arg_28_0.success.active = False

			setActive(arg_28_0._effectSuccess, False)
			arg_28_0.resetSpecialData()
			arg_28_0.step(),
		def step:(arg_29_0)
			for iter_29_0 = 1, #arg_29_0.powers:
				local var_29_0 = arg_29_0.powers[iter_29_0]

				if var_29_0.active and var_29_0.cur > 0:
					var_29_0.cur = var_29_0.cur - var_0_42 * Time.deltaTime

					if var_29_0.cur <= 0:
						var_29_0.active = False
						var_29_0.cur = 0

				GetComponent(var_29_0.tf, typeof(Slider)).value = var_29_0.cur > 0 and var_29_0.cur / var_29_0.max or 0

				setText(var_29_0.text_tf, math.floor(var_29_0.cur))

			setText(arg_29_0.successText, math.floor(arg_29_0.success.cur))

			if arg_29_0.success.active and arg_29_0.success.cur > 0 and var_0_23.special_complete and not arg_29_0.inCameraFlag:
				if arg_29_0.inCameraFadeTime > 0:
					arg_29_0.inCameraFadeTime = arg_29_0.inCameraFadeTime - Time.deltaTime * 1000
				else
					arg_29_0.success.cur = arg_29_0.success.cur - var_0_43 * Time.deltaTime

					if arg_29_0.success.cur <= 0:
						arg_29_0.success.active = False
						arg_29_0.success.cur = 0

						arg_29_0._event.emit(var_0_19)

			if arg_29_0.success.cur >= arg_29_0.success.max or arg_29_0.success.active:
				setActive(arg_29_0._effectSuccess, True)
			else
				setActive(arg_29_0._effectSuccess, False)

			arg_29_0.success.slider.value = arg_29_0.success.cur > 0 and arg_29_0.success.cur / arg_29_0.success.max or 0
			var_0_23.special_time = arg_29_0.success.active
			var_0_23.grid_index = 0

			if arg_29_0.waitingSpecial:
				arg_29_0.addPowerAmount(1, 0),
		def clear:(arg_30_0)
			return,
		def updateSpecialData:(arg_31_0, arg_31_1)
			var_0_23.special_time = arg_31_0.success.active
			var_0_23.grid_index = arg_31_1
			var_0_23.power_grid = 0

			for iter_31_0 = 1, #arg_31_0.powers:
				if arg_31_0.powers[iter_31_0].index == arg_31_1 and arg_31_0.powers[iter_31_0].cur == arg_31_0.powers[iter_31_0].max:
					var_0_23.power_grid = arg_31_0.powers[iter_31_0].index

			arg_31_0._event.emit(var_0_15),
		def resetSpecialData:(arg_32_0)
			var_0_23.special_complete = False,
		def addPowerAmount:(arg_33_0, arg_33_1, arg_33_2)
			local var_33_0 = arg_33_0.getPowerByIndex(arg_33_1)

			if arg_33_0.success:
				if not arg_33_0.success.active:
					arg_33_0.success.cur = arg_33_0.success.cur + arg_33_2

					if arg_33_0.success.cur >= arg_33_0.success.max:
						arg_33_0.success.cur = arg_33_0.success.max

						arg_33_0._event.emit(var_0_18, {
							def callback:(arg_34_0)
								if arg_34_0:
									if not isActive(arg_33_0._effectSuccess):
										setActive(arg_33_0._effectSuccess, True)

									arg_33_0.success.active = True
									var_0_23.special_complete = False
									arg_33_0.waitingSpecial = False
								else
									arg_33_0.waitingSpecial = True
						})
				else
					arg_33_0.success.cur = arg_33_0.success.cur + arg_33_2 / 2

					if arg_33_0.success.cur >= arg_33_0.success.max:
						arg_33_0.success.cur = arg_33_0.success.max

			if var_33_0 and not var_33_0.active:
				var_33_0.cur = var_33_0.cur + arg_33_2

				if var_33_0.cur >= var_33_0.max:
					var_33_0.cur = var_33_0.max
					var_33_0.active = True

			if arg_33_2 > 0:
				arg_33_0.updateSpecialData(arg_33_1),
		def getPowerByIndex:(arg_35_0, arg_35_1)
			for iter_35_0 = 1, #arg_35_0.powers:
				if arg_35_0.powers[iter_35_0].index == arg_35_1:
					return arg_35_0.powers[iter_35_0]

			return None,
		def getPowerAmount:(arg_36_0, arg_36_1, arg_36_2, arg_36_3)
			if arg_36_1 <= 2:
				print("分数. " .. var_0_44)

				return var_0_44

			local var_36_0 = arg_36_3 and 2 or 1

			if var_36_0 == 2:
				-- block empty

			local var_36_1 = var_0_23.special_time and var_0_41 or 1

			print("方块个数. " .. arg_36_1 .. ",combo次数. " .. arg_36_2 .. ", 加倍方块. " .. tostring(arg_36_3) .. "，变身倍率. " .. var_36_1)
			print("分数. " .. (var_0_40 + (arg_36_1 - var_0_39) * var_0_38) * (1 + arg_36_2 * var_0_37) * var_36_1)

			return (var_0_40 + (arg_36_1 - var_0_39) * var_0_38) * (1 + arg_36_2 * var_0_37) * var_36_0 * var_36_1
	}

	var_23_0.ctor()

	return var_23_0

local function var_0_91(arg_37_0, arg_37_1, arg_37_2)
	local var_37_0 = {
		def ctor:(arg_38_0)
			arg_38_0._sceneTf = arg_37_0
			arg_38_0._event = arg_37_2
			arg_38_0.bgs = {}
			arg_38_0._gameTf = arg_37_1
			arg_38_0._box = findTF(arg_38_0._gameTf, "box")
			arg_38_0._specialPower = findTF(arg_38_0._gameTf, "specialPower")
			arg_38_0._successPower = findTF(arg_38_0._gameTf, "successPower")
			arg_38_0._top = findTF(arg_38_0._gameTf, "top")

			for iter_38_0 = 1, #var_0_71:
				local var_38_0 = var_0_71[iter_38_0]
				local var_38_1 = findTF(arg_38_0._sceneTf, var_0_71[iter_38_0].source)
				local var_38_2 = var_0_71[iter_38_0].rate

				table.insert(arg_38_0.bgs, {
					tf = var_38_1,
					rate = var_38_2,
					type = var_0_71[iter_38_0].type
				})

			arg_38_0._bgBackCanvas = GetComponent(findTF(arg_38_0._sceneTf, "scene_background"), typeof(CanvasGroup))
			arg_38_0._bgFrontCanvas = GetComponent(findTF(arg_38_0._sceneTf, "scene_front"), typeof(CanvasGroup))
			arg_38_0._bgBeamCanvas = GetComponent(findTF(arg_38_0._sceneTf, "scene/bgBeam"), typeof(CanvasGroup))

			arg_38_0._event.bind(var_0_16, function(arg_39_0, arg_39_1, arg_39_2)
				local var_39_0 = arg_39_1[1]
				local var_39_1 = arg_39_1[2] and -1 or 1
				local var_39_2 = arg_39_1[3]

				if not arg_38_0.inCamera:
					arg_38_0.setTargetFllow(Vector2(var_39_1 * var_39_0.x / 10, var_39_1 * var_39_0.y / 10), var_39_2))
			arg_38_0._event.bind(var_0_20, function(arg_40_0, arg_40_1, arg_40_2)
				arg_38_0.inCamera = True

				local var_40_0 = Vector2(550, 100)

				if arg_40_1 and arg_40_1.playingAction and arg_40_1.playingAction.camera_pos:
					var_40_0 = arg_40_1.playingAction.camera_pos

				arg_38_0.setTargetFllow(var_40_0)
				arg_38_0.setBeam(False))
			arg_38_0._event.bind(var_0_21, function(arg_41_0, arg_41_1, arg_41_2)
				arg_38_0.followTf = None
				arg_38_0.followInit = None

				arg_38_0.setTargetFllow(Vector2(0, 0), function()
					return, True)
				arg_38_0.setBeam(True)

				arg_38_0.inCamera = False),
		def start:(arg_43_0)
			arg_43_0.targetVec = Vector2(var_0_56.x, var_0_56.y)
			arg_43_0.currentVec = Vector2(var_0_56.x, var_0_56.y)

			for iter_43_0 = 1, #arg_43_0.bgs:
				local var_43_0 = arg_43_0.bgs[iter_43_0].tf
				local var_43_1 = arg_43_0.bgs[iter_43_0].rate
				local var_43_2 = arg_43_0.bgs[iter_43_0].type

				if var_43_0:
					setActive(var_43_0, var_43_2 == var_0_67 or var_43_2 == var_0_70)

					var_43_0.anchoredPosition = Vector2(arg_43_0.currentVec.x * var_43_1, arg_43_0.currentVec.y * var_43_1)

			arg_43_0._bgBackCanvas.alpha = 1
			arg_43_0._bgFrontCanvas.alpha = 1
			arg_43_0._bgBeamCanvas.alpha = 0

			setActive(arg_43_0._box, True)
			setActive(arg_43_0._specialPower, True)
			setActive(arg_43_0._successPower, True)
			setActive(arg_43_0._top, True),
		def clear:(arg_44_0)
			if LeanTween.isTweening(go(arg_44_0._sceneTf)):
				LeanTween.cancel(go(arg_44_0._sceneTf), False),
		def step:(arg_45_0)
			local var_45_0 = {
				0,
				0
			}

			if arg_45_0.followTf:
				var_45_0 = {
					arg_45_0.followTf.anchoredPosition.x - arg_45_0.followInit.x,
					arg_45_0.followTf.anchoredPosition.y - arg_45_0.followInit.y
				}

			local var_45_1 = 0
			local var_45_2 = 0
			local var_45_3 = arg_45_0.targetVec.x - var_45_0[1]
			local var_45_4 = arg_45_0.targetVec.y - var_45_0[2]

			if var_45_3 != arg_45_0.currentVec.x:
				var_45_1 = (var_45_3 - arg_45_0.currentVec.x) * var_0_57

				if math.abs(var_45_1) < var_0_58:
					var_45_1 = var_0_58 * math.sign(var_45_1)

				arg_45_0.currentVec.x = arg_45_0.currentVec.x + var_45_1

				if math.abs(arg_45_0.currentVec.x - var_45_3) <= var_0_58:
					arg_45_0.currentVec.x = var_45_3

			if var_45_4 != arg_45_0.currentVec.y:
				var_45_2 = (var_45_4 - arg_45_0.currentVec.y) * var_0_57

				if math.abs(var_45_2) < var_0_58:
					var_45_2 = var_0_58 * math.sign(var_45_2)

				arg_45_0.currentVec.y = arg_45_0.currentVec.y + var_45_2

				if math.abs(arg_45_0.currentVec.y - var_45_4) <= var_0_58:
					arg_45_0.currentVec.y = var_45_4

			if var_45_1 != 0 or var_45_2 != 0:
				arg_45_0.moveTo(arg_45_0.currentVec),
		def moveTo:(arg_46_0, arg_46_1)
			for iter_46_0 = 1, #arg_46_0.bgs:
				local var_46_0 = arg_46_0.bgs[iter_46_0].tf
				local var_46_1 = arg_46_0.bgs[iter_46_0].rate
				local var_46_2 = arg_46_0.bgs[iter_46_0].type

				if var_46_2 == var_0_67 or var_46_2 == var_0_70:
					var_46_0.anchoredPosition = Vector2(arg_46_1.x * var_46_1, arg_46_1.y * var_46_1),
		def setTargetFllow:(arg_47_0, arg_47_1, arg_47_2, arg_47_3)
			if not arg_47_3:
				arg_47_0.targetVec = arg_47_1
				arg_47_0.moveCallback = arg_47_2
			else
				arg_47_0.currentVec = arg_47_1
				arg_47_0.targetVec = arg_47_1

				arg_47_0.moveTo(arg_47_1)

				if arg_47_2:
					arg_47_2(),
		def setBeam:(arg_48_0, arg_48_1, arg_48_2)
			if LeanTween.isTweening(go(arg_48_0._sceneTf)):
				LeanTween.cancel(go(arg_48_0._sceneTf), False)

			if arg_48_1:
				setActive(arg_48_0._box, True)
				setActive(arg_48_0._specialPower, True)
				setActive(arg_48_0._successPower, True)
				setActive(arg_48_0._top, True)
			else
				setActive(arg_48_0._box, False)
				setActive(arg_48_0._specialPower, False)
				setActive(arg_48_0._successPower, False)
				setActive(arg_48_0._top, False)

			LeanTween.value(go(arg_48_0._sceneTf), 0, 1, 0.2).setOnUpdate(System.Action_float(function(arg_49_0)
				if arg_48_1:
					arg_48_0._bgBackCanvas.alpha = arg_49_0
					arg_48_0._bgFrontCanvas.alpha = arg_49_0
					arg_48_0._bgBeamCanvas.alpha = 1 - arg_49_0
				else
					arg_48_0._bgBackCanvas.alpha = 1 - arg_49_0
					arg_48_0._bgFrontCanvas.alpha = 1 - arg_49_0
					arg_48_0._bgBeamCanvas.alpha = arg_49_0)).setOnComplete(System.Action(function()
				if arg_48_2:
					arg_48_2()))
	}

	var_37_0.ctor()

	return var_37_0

local function var_0_92(arg_51_0, arg_51_1)
	local var_51_0 = {
		def ctor:(arg_52_0)
			arg_52_0._scene = arg_51_0
			arg_52_0._tpl = findTF(arg_52_0._scene, "tpl")
			arg_52_0._leftRolePos = findTF(arg_52_0._scene, "rolePos/leftRole")
			arg_52_0._rightRolePos = findTF(arg_52_0._scene, "rolePos/rightRole")
			arg_52_0._event = arg_51_1

			arg_52_0._event.bind(var_0_15, function()
				arg_52_0.onGridTrigger())
			arg_52_0._event.bind(var_0_18, function(arg_54_0, arg_54_1, arg_54_2)
				local var_54_0 = False

				for iter_54_0, iter_54_1 in pairs(arg_52_0.playingDatas):
					if iter_54_1.inPlaying:
						var_54_0 = True

				if arg_54_1.callback:
					arg_54_1.callback(not var_54_0)

				if not var_54_0:
					arg_52_0.onRoleSpecial(arg_54_1))
			arg_52_0._event.bind(var_0_19, function()
				arg_52_0.onRoleSpecialEnd()),
		def start:(arg_56_0)
			if arg_56_0.leftRole:
				destroy(arg_56_0.leftRole.tf)

				arg_56_0.leftRole = None

			if arg_56_0.rightRole:
				destroy(arg_56_0.rightRole.tf)

				arg_56_0.rightRole = None

			arg_56_0.leftRole = arg_56_0.createRole(var_0_46, True, arg_56_0._leftRolePos)
			arg_56_0.rightRole = arg_56_0.createRole(var_0_47, False, arg_56_0._rightRolePos)
			arg_56_0.leftRole.targetRole = arg_56_0.rightRole
			arg_56_0.rightRole.targetRole = arg_56_0.leftRole

			arg_56_0.leftRole.animator.SetTrigger("idle")
			arg_56_0.leftRole.animator.SetBool("special", False)
			arg_56_0.rightRole.animator.SetTrigger("idle")
			arg_56_0.rightRole.animator.SetBool("special", False)

			arg_56_0.leftRole.specialBody = False
			arg_56_0.rightRole.specialBody = False
			arg_56_0.leftRole.anchoredPosition = Vector2(0, 0)
			arg_56_0.rightRole.anchoredPosition = Vector2(0, 0)
			arg_56_0.leftRole.specialTime = False
			arg_56_0.rightRole.specialTime = False
			arg_56_0.playingDatas = {}
			arg_56_0.playingDatas[arg_56_0.leftRole.name] = {
				role = arg_56_0.leftRole
			}
			arg_56_0.playingDatas[arg_56_0.leftRole.name].skillDatas = {}
			arg_56_0.playingDatas[arg_56_0.rightRole.name] = {
				role = arg_56_0.rightRole
			}
			arg_56_0.playingDatas[arg_56_0.rightRole.name].skillDatas = {}
			arg_56_0.skillDeltaTime = 0
			arg_56_0.emptySkillTime = math.random(1, 2)
			arg_56_0.addScore = {
				0,
				0
			}

			arg_56_0._event.emit(var_0_16, {
				Vector2(0, 0),
				False
			}),
		def step:(arg_57_0)
			arg_57_0.checkSkillDeltaTime()
			arg_57_0.checkEmptySkillTime(),
		def checkSkillDeltaTime:(arg_58_0)
			if arg_58_0.skillDeltaTime and arg_58_0.skillDeltaTime <= 0:
				arg_58_0.skillDeltaTime = var_0_59

			arg_58_0.skillDeltaTime = arg_58_0.skillDeltaTime - Time.deltaTime

			if arg_58_0.skillDeltaTime <= 0:
				local var_58_0 = False

				for iter_58_0, iter_58_1 in pairs(arg_58_0.playingDatas):
					if iter_58_1.inPlaying:
						var_58_0 = True

				if not var_58_0:
					for iter_58_2, iter_58_3 in pairs(arg_58_0.playingDatas):
						if #iter_58_3.skillDatas > 0:
							arg_58_0.applyOrAddSkillData(iter_58_3)

							break

			var_0_89 = False

			for iter_58_4, iter_58_5 in pairs(arg_58_0.playingDatas):
				if iter_58_5.inPlaying:
					var_0_89 = True,
		def checkEmptySkillTime:(arg_59_0)
			if arg_59_0.emptySkillTime and arg_59_0.emptySkillTime <= 0:
				arg_59_0.emptySkillTime = var_0_60

			arg_59_0.emptySkillTime = arg_59_0.emptySkillTime - Time.deltaTime

			if arg_59_0.emptySkillTime <= 0:
				local var_59_0 = False

				for iter_59_0, iter_59_1 in pairs(arg_59_0.playingDatas):
					if iter_59_1.inPlaying:
						var_59_0 = True

				if not var_59_0:
					local var_59_1 = arg_59_0.getRoleEmptySkill(arg_59_0.rightRole)

					if var_59_1:
						arg_59_0.addRolePlaying(arg_59_0.rightRole, var_59_1),
		def getRoleTestSkill:(arg_60_0, arg_60_1)
			return arg_60_1.skill[10],
		def getRoleEmptySkill:(arg_61_0, arg_61_1)
			local var_61_0 = {}

			for iter_61_0 = 1, #arg_61_1.skill:
				local var_61_1 = arg_61_1.skill[iter_61_0]

				if tobool(var_61_1.special_time) == arg_61_1.specialBody and var_61_1.atk_index:
					table.insert(var_61_0, var_61_1)

			if #var_61_0 > 0:
				return Clone(var_61_0[math.random(1, #var_61_0)])

			return None,
		def onRoleSpecial:(arg_62_0, arg_62_1)
			arg_62_0.leftRole.specialTime = True

			for iter_62_0 = 1, #arg_62_0.leftRole.skill:
				local var_62_0 = arg_62_0.leftRole.skill[iter_62_0]

				if var_62_0.special_trigger:
					arg_62_0.addRolePlaying(arg_62_0.leftRole, Clone(var_62_0)),
		def onRoleSpecialEnd:(arg_63_0)
			arg_63_0.leftRole.specialTime = False

			local var_63_0
			local var_63_1

			for iter_63_0 = 1, #arg_63_0.leftRole.skill:
				local var_63_2 = arg_63_0.leftRole.skill[iter_63_0]

				if var_63_2.special_time and var_63_2.power_index == 1 and var_63_2.atk_index > 0:
					var_63_1 = Clone(var_63_2)

				if not var_63_2.special_trigger and var_63_2.special_end:
					var_63_0 = Clone(var_63_2)

			if var_63_1:
				arg_63_0.addRolePlaying(arg_63_0.leftRole, var_63_1)

			if var_63_0:
				arg_63_0.addRolePlaying(arg_63_0.leftRole, var_63_0),
		def clear:(arg_64_0)
			if LeanTween.isTweening(go(arg_64_0._leftRolePos)):
				LeanTween.cancel(go(arg_64_0._leftRolePos))

			if LeanTween.isTweening(go(arg_64_0._rightRolePos)):
				LeanTween.cancel(go(arg_64_0._rightRolePos))

			if LeanTween.isTweening(go(arg_64_0.rightRole.tf)):
				LeanTween.cancel(go(arg_64_0.rightRole.tf))

			if LeanTween.isTweening(go(arg_64_0.leftRole.tf)):
				LeanTween.cancel(go(arg_64_0.leftRole.tf)),
		def onGridTrigger:(arg_65_0)
			local var_65_0 = var_0_23.grid_index
			local var_65_1 = var_0_23.power_grid
			local var_65_2 = var_0_23.special_time

			for iter_65_0 = 1, #arg_65_0.leftRole.skill:
				local var_65_3 = arg_65_0.leftRole.skill[iter_65_0]

				if tobool(var_65_3.special_time) == tobool(arg_65_0.leftRole.specialTime) and var_65_3.power_index == var_65_1 and table.contains(var_65_3.grid_index, var_65_0) and var_65_3.atk_index:
					arg_65_0.addRolePlaying(arg_65_0.leftRole, Clone(var_65_3)),
		def createRole:(arg_66_0, arg_66_1, arg_66_2, arg_66_3)
			local var_66_0 = arg_66_0.getRoleData(arg_66_1)

			if not var_66_0:
				return None

			local var_66_1 = {}
			local var_66_2 = tf(instantiate(findTF(arg_66_0._tpl, var_66_0.name)))

			SetParent(var_66_2, arg_66_3)

			var_66_2.anchoredPosition = Vector2(0, 0)
			var_66_2.localScale = Vector3(1, 1, 1)

			setActive(var_66_2, True)

			if var_66_0.anim_init_pos:
				findTF(var_66_2, "body/anim").anchoredPosition = var_66_0.anim_init_pos

			local var_66_3 = findTF(var_66_2, "body")
			local var_66_4 = findTF(var_66_3, "anim")
			local var_66_5 = GetComponent(var_66_4, typeof(Animator))
			local var_66_6 = GetComponent(var_66_4, typeof(DftAniEvent))

			var_66_6.SetStartEvent(function()
				if var_66_1.startCallback:
					var_66_1.startCallback())
			var_66_6.SetTriggerEvent(function()
				if var_66_1.triggerCallback:
					var_66_1.triggerCallback())
			var_66_6.SetEndEvent(function()
				if var_66_1.endCallback:
					var_66_1.endCallback())

			var_66_1.name = var_66_0.name
			var_66_1.tf = var_66_2
			var_66_1.canvasGroup = GetComponent(var_66_2, typeof(CanvasGroup))
			var_66_1.body = var_66_3
			var_66_1.animTf = var_66_4
			var_66_1.animator = var_66_5
			var_66_1.dftEvent = var_66_6
			var_66_1.startCallback = None
			var_66_1.triggerCallback = None
			var_66_1.endCallback = None
			var_66_1.skill = var_66_0.skill
			var_66_1.name = var_66_0.name
			var_66_1.index = var_66_0.index
			var_66_1.actions = var_66_0.actions

			return var_66_1,
		def getRoleData:(arg_70_0, arg_70_1)
			for iter_70_0 = 1, #var_0_87:
				if var_0_87[iter_70_0].index == arg_70_1:
					return Clone(var_0_87[iter_70_0])

			return None,
		def setDftHandle:(arg_71_0, arg_71_1, arg_71_2, arg_71_3, arg_71_4)
			arg_71_1.startCallback = arg_71_2
			arg_71_1.triggerCallback = arg_71_3
			arg_71_1.endCallback = arg_71_4,
		def playAnimation:(arg_72_0, arg_72_1, arg_72_2)
			arg_72_1.animator.Play(arg_72_2, -1, 0),
		def addRolePlaying:(arg_73_0, arg_73_1, arg_73_2, arg_73_3)
			for iter_73_0, iter_73_1 in pairs(arg_73_0.playingDatas):
				if iter_73_0 == arg_73_1.name:
					if arg_73_3:
						arg_73_0.applyOrAddSkillData(iter_73_1, arg_73_2)
					else
						table.insert(iter_73_1.skillDatas, arg_73_2)

						if arg_73_2.power_index > 0 and arg_73_2.atk_index > 1 or arg_73_2.special_trigger:
							for iter_73_2 = #iter_73_1.skillDatas - 1, 1, -1:
								local var_73_0 = iter_73_1.skillDatas[iter_73_2]

								if var_73_0.power_index == 0 and var_73_0.atk_index == 1:
									local var_73_1 = table.remove(iter_73_1.skillDatas, iter_73_2)

									if var_73_1.score:
										arg_73_0.addScore = {
											arg_73_0.addScore[1] + var_73_1.score[1],
											arg_73_0.addScore[2] + var_73_1.score[2]
										},
		def applyOrAddSkillData:(arg_74_0, arg_74_1, arg_74_2)
			if arg_74_1.inPlaying:
				table.insert(arg_74_1.skillDatas, arg_74_2)

				return

			arg_74_1.inPlaying = True

			local var_74_0 = arg_74_1.role
			local var_74_1 = arg_74_2 or table.remove(arg_74_1.skillDatas, 1)

			arg_74_1.currentSkill = var_74_1
			arg_74_1.actions = var_74_1.actions

			local var_74_2 = var_74_1.anim_bool

			if var_74_2:
				var_74_0.animator.SetBool(var_74_2, True)

			if var_74_0 == arg_74_0.leftRole and not var_74_1.dmg_index:
				arg_74_0._leftRolePos.SetSiblingIndex(1)
			elif var_74_0 == arg_74_0.rightRole and not var_74_1.dmg_index:
				arg_74_0._rightRolePos.SetSiblingIndex(1)

			local var_74_3 = var_74_1.anim_init_pos

			if var_74_3:
				findTF(arg_74_1.role.tf, "body/anim").anchoredPosition = var_74_3

			if var_74_1.special_end:
				arg_74_1.role.specialBody = False
			elif var_74_1.special_trigger:
				arg_74_1.role.specialBody = True

			arg_74_1.actionIndex = 1

			arg_74_0.checkAction(arg_74_1, function()
				arg_74_1.inPlaying = False

				arg_74_0._event.emit(var_0_16, {
					Vector2(0, 0),
					False
				})),
		def checkAction:(arg_76_0, arg_76_1, arg_76_2)
			if arg_76_1.actions and arg_76_1.actionIndex <= #arg_76_1.actions:
				arg_76_1.playingAction = arg_76_1.actions[arg_76_1.actionIndex]
				arg_76_1.actionIndex = arg_76_1.actionIndex + 1

				local var_76_0 = arg_76_1.playingAction.anim_name
				local var_76_1 = arg_76_1.playingAction.time
				local var_76_2 = arg_76_1.playingAction.move
				local var_76_3 = arg_76_1.playingAction.over_offset
				local var_76_4 = arg_76_1.playingAction.camera
				local var_76_5 = arg_76_1.playingAction.sound_start
				local var_76_6 = arg_76_1.playingAction.sound_trigger
				local var_76_7 = arg_76_1.playingAction.sound_end
				local var_76_8 = arg_76_1.currentSkill.special_trigger
				local var_76_9 = arg_76_1.currentSkill.special_time
				local var_76_10 = arg_76_1.currentSkill.atk_index

				if var_76_8 or var_76_9 and var_76_10 and var_76_10 >= 2:
					arg_76_0._event.emit(var_0_22, True)

				if var_76_1 and var_76_1 > 0:
					-- block empty
				else
					local function var_76_11()
						if var_76_5:
							pg.CriMgr.GetInstance().PlaySoundEffect_V3("event./ui/" .. var_76_5)

						if var_76_2:
							arg_76_0.moveRole(arg_76_1.role, var_76_2)

						if var_76_4:
							arg_76_1.role.targetRole.canvasGroup.alpha = 0

							arg_76_0._event.emit(var_0_20, arg_76_1)

					local function var_76_12()
						if var_76_6:
							pg.CriMgr.GetInstance().PlaySoundEffect_V3("event./ui/" .. var_76_6)

						if var_76_4:
							var_76_4 = False
							arg_76_1.role.targetRole.canvasGroup.alpha = 1

							arg_76_0._event.emit(var_0_21)
						else
							local var_78_0 = arg_76_1.currentSkill.anim_trigger_pos

							if var_78_0:
								findTF(arg_76_1.role.tf, "body/anim").anchoredPosition = var_78_0

							local var_78_1 = arg_76_1.currentSkill.atk_index

							if var_78_1:
								local var_78_2 = arg_76_0.getRoleDmgData(arg_76_1.role.targetRole, var_78_1)
								local var_78_3 = arg_76_1.role.targetRole.name

								if var_78_2:
									for iter_78_0, iter_78_1 in pairs(arg_76_0.playingDatas):
										if iter_78_0 == var_78_3:
											arg_76_0.applyOrAddSkillData(iter_78_1, Clone(var_78_2), True)

								local var_78_4 = arg_76_1.currentSkill.score

								if var_78_4 and arg_76_1.role == arg_76_0.leftRole:
									arg_76_0._event.emit(var_0_17, math.random(var_78_4[1] + arg_76_0.addScore[1], var_78_4[2] + arg_76_0.addScore[2]))

									arg_76_0.addScore = {
										0,
										0
									}

					local function var_76_13()
						if var_76_7:
							pg.CriMgr.GetInstance().PlaySoundEffect_V3("event./ui/" .. var_76_7)

						if LeanTween.isTweening(go(arg_76_1.role.tf)):
							LeanTween.cancel(go(arg_76_1.role.tf))

						local var_79_0 = arg_76_1.currentSkill.anim_end_pos

						if var_79_0:
							findTF(arg_76_1.role.tf, "body/anim").anchoredPosition = var_79_0

						arg_76_0._event.emit(var_0_22, False)

						if var_76_3:
							arg_76_1.role.tf.anchoredPosition = Vector2(arg_76_1.role.tf.anchoredPosition.x + var_76_3.x, arg_76_1.role.tf.anchoredPosition.y + var_76_3.y)

						if arg_76_1.currentSkill.special_trigger and var_0_23.special_time and not var_0_23.special_complete:
							var_0_23.special_complete = True

						arg_76_1.playingAction = None

						arg_76_0.setDftHandle(arg_76_1.role, None, None, None)
						arg_76_0.checkAction(arg_76_1, arg_76_2)

					arg_76_0.setDftHandle(arg_76_1.role, var_76_11, var_76_12, var_76_13)
					arg_76_0.playAnimation(arg_76_1.role, var_76_0)
			else
				local var_76_14 = arg_76_1.currentSkill.atk_index

				if var_76_14 == 3:
					local var_76_15 = arg_76_0.getRoleDmgBack(arg_76_1.role.targetRole, var_76_14)
					local var_76_16 = arg_76_1.role.targetRole.name

					if var_76_15:
						for iter_76_0, iter_76_1 in pairs(arg_76_0.playingDatas):
							if iter_76_0 == var_76_16:
								arg_76_0.applyOrAddSkillData(iter_76_1, Clone(var_76_15))

				if arg_76_2:
					arg_76_2(),
		def moveRole:(arg_80_0, arg_80_1, arg_80_2)
			if LeanTween.isTweening(go(arg_80_1.tf)):
				LeanTween.cancel(go(arg_80_1.tf))

			if arg_80_2.distance:
				arg_80_0._event.emit(var_0_16, {
					arg_80_2.distance,
					arg_80_1 == arg_80_0.leftRole
				})
				LeanTween.move(arg_80_1.tf, Vector3(arg_80_2.distance.x, arg_80_2.distance.y, 0), arg_80_2.time).setEase(arg_80_2.ease or LeanTweenType.linear)
			elif arg_80_2.distance_m:
				local var_80_0 = Vector2(arg_80_1.tf.anchoredPosition.x + arg_80_2.distance_m.x, arg_80_1.tf.anchoredPosition.y + arg_80_2.distance_m.y)

				arg_80_0._event.emit(var_0_16, {
					var_80_0,
					arg_80_1 == arg_80_0.leftRole
				})
				LeanTween.move(arg_80_1.tf, Vector3(var_80_0.x, var_80_0.y, 0), arg_80_2.time).setEase(arg_80_2.ease or LeanTweenType.linear),
		def getRoleDmgData:(arg_81_0, arg_81_1, arg_81_2)
			local var_81_0 = arg_81_1.skill

			for iter_81_0 = 1, #var_81_0:
				local var_81_1 = var_81_0[iter_81_0]

				if var_81_1.dmg_index == arg_81_2 and var_81_1.special_time == tobool(arg_81_1.specialBody):
					return var_81_1

			return None,
		def getRoleDmgBack:(arg_82_0, arg_82_1, arg_82_2)
			local var_82_0 = arg_82_1.skill

			for iter_82_0 = 1, #var_82_0:
				local var_82_1 = var_82_0[iter_82_0]

				if var_82_1.dmg_back and var_82_1.special_time == tobool(arg_82_1.specialBody):
					return var_82_1

			return None
	}

	var_51_0.ctor()

	return var_51_0

def var_0_0.getUIName(arg_83_0):
	return "GridGameReUI"

def var_0_0.didEnter(arg_84_0):
	arg_84_0.initEvent()
	arg_84_0.initData()
	arg_84_0.initUI()
	arg_84_0.initGameUI()
	arg_84_0.initController()
	arg_84_0.updateMenuUI()
	arg_84_0.openMenuUI()

def var_0_0.initEvent(arg_85_0):
	arg_85_0.bind(var_0_17, function(arg_86_0, arg_86_1, arg_86_2)
		arg_85_0.addScore(arg_86_1))
	arg_85_0.bind(var_0_22, function(arg_87_0, arg_87_1, arg_87_2)
		arg_85_0.ignoreTime = arg_87_1)

def var_0_0.onEventHandle(arg_88_0, arg_88_1):
	return

def var_0_0.initData(arg_89_0):
	local var_89_0 = Application.targetFrameRate or 60

	if var_89_0 > 60:
		var_89_0 = 60

	arg_89_0.timer = Timer.New(function()
		arg_89_0.onTimer(), 1 / var_89_0, -1)

def var_0_0.initUI(arg_91_0):
	arg_91_0.backSceneTf = findTF(arg_91_0._tf, "scene_background")
	arg_91_0.sceneTf = findTF(arg_91_0._tf, "scene")
	arg_91_0.clickMask = findTF(arg_91_0._tf, "clickMask")

	setText(findTF(arg_91_0._tf, "ui/gameUI/top/time"), i18n("mini_game_time"))
	setText(findTF(arg_91_0._tf, "ui/gameUI/top/scoreDesc"), i18n("mini_game_score"))
	setText(findTF(arg_91_0._tf, "pop/LeaveUI/ad/desc"), i18n("mini_game_leave"))
	setText(findTF(arg_91_0._tf, "pop/pauseUI/ad/desc"), i18n("mini_game_pause"))
	setText(findTF(arg_91_0._tf, "pop/SettleMentUI/ad/currentTextDesc"), i18n("mini_game_cur_score"))
	setText(findTF(arg_91_0._tf, "pop/SettleMentUI/ad/highTextDesc"), i18n("mini_game_high_score"))

	arg_91_0.countUI = findTF(arg_91_0._tf, "pop/CountUI")
	arg_91_0.countAnimator = GetComponent(findTF(arg_91_0.countUI, "count"), typeof(Animator))
	arg_91_0.countDft = GetOrAddComponent(findTF(arg_91_0.countUI, "count"), typeof(DftAniEvent))

	arg_91_0.countDft.SetTriggerEvent(function()
		return)
	arg_91_0.countDft.SetEndEvent(function()
		setActive(arg_91_0.countUI, False)
		arg_91_0.gameStart())

	arg_91_0.leaveUI = findTF(arg_91_0._tf, "pop/LeaveUI")

	onButton(arg_91_0, findTF(arg_91_0.leaveUI, "ad/btnOk"), function()
		arg_91_0.resumeGame()
		arg_91_0.onGameOver(), SFX_CANCEL)
	onButton(arg_91_0, findTF(arg_91_0.leaveUI, "ad/btnCancel"), function()
		arg_91_0.resumeGame(), SFX_CANCEL)

	arg_91_0.pauseUI = findTF(arg_91_0._tf, "pop/pauseUI")

	onButton(arg_91_0, findTF(arg_91_0.pauseUI, "ad/btnOk"), function()
		setActive(arg_91_0.pauseUI, False)
		arg_91_0.resumeGame(), SFX_CANCEL)

	arg_91_0.settlementUI = findTF(arg_91_0._tf, "pop/SettleMentUI")

	onButton(arg_91_0, findTF(arg_91_0.settlementUI, "ad/btnOver"), function()
		setActive(arg_91_0.settlementUI, False)
		arg_91_0.openMenuUI(), SFX_CANCEL)

	arg_91_0.selectedUI = findTF(arg_91_0._tf, "pop/selectedUI")
	arg_91_0.leftSelectRole = {}

	for iter_91_0 = 1, #var_0_50:
		local var_91_0 = findTF(arg_91_0.selectedUI, "ad/leftRole/role" .. var_0_50[iter_91_0])

		setActive(var_91_0, True)

		local var_91_1 = var_0_50[iter_91_0]

		onButton(arg_91_0, var_91_0, function()
			var_0_46, var_0_47 = arg_91_0.checkRoleId(var_91_1, var_0_47, var_0_51)

			arg_91_0.updateSelectedUI(), SFX_CONFIRM)
		table.insert(arg_91_0.leftSelectRole, {
			id = var_91_1,
			tf = var_91_0
		})

	onButton(arg_91_0, findTF(arg_91_0.selectedUI, "close"), function()
		setActive(arg_91_0.selectedUI, False), SFX_CANCEL)

	arg_91_0.rightSelectRole = {}

	for iter_91_1 = 1, #var_0_51:
		local var_91_2 = findTF(arg_91_0.selectedUI, "ad/rightRole/role" .. var_0_51[iter_91_1])

		setActive(var_91_2, True)

		local var_91_3 = var_0_51[iter_91_1]

		onButton(arg_91_0, var_91_2, function()
			var_0_47, var_0_46 = arg_91_0.checkRoleId(var_91_3, var_0_46, var_0_50)

			arg_91_0.updateSelectedUI(), SFX_CONFIRM)
		table.insert(arg_91_0.rightSelectRole, {
			id = var_91_3,
			tf = var_91_2
		})

	onButton(arg_91_0, findTF(arg_91_0.selectedUI, "ad/btnOk"), function()
		setActive(arg_91_0.selectedUI, False)
		setActive(arg_91_0.menuUI, False)
		arg_91_0.readyStart(), SFX_CONFIRM)

	arg_91_0.btnDay = findTF(arg_91_0.selectedUI, "ad/btnDay")
	arg_91_0.btnNight = findTF(arg_91_0.selectedUI, "ad/btnNight")

	local var_91_4 = arg_91_0.getGameUsedTimes() or 0

	var_0_70 = var_0_53[var_91_4 + 1] and var_0_53[var_91_4 + 1] or var_0_69

	setActive(findTF(arg_91_0.btnDay, "on"), var_0_70 == var_0_68)
	setActive(findTF(arg_91_0.btnNight, "on"), var_0_70 == var_0_69)
	onButton(arg_91_0, arg_91_0.btnDay, function()
		var_0_70 = var_0_68

		setActive(findTF(arg_91_0.btnDay, "on"), True)
		setActive(findTF(arg_91_0.btnNight, "on"), False)
		arg_91_0.updateMenuUI(), SFX_CONFIRM)
	onButton(arg_91_0, arg_91_0.btnNight, function()
		var_0_70 = var_0_69

		setActive(findTF(arg_91_0.btnDay, "on"), False)
		setActive(findTF(arg_91_0.btnNight, "on"), True)
		arg_91_0.updateMenuUI(), SFX_CONFIRM)
	setActive(arg_91_0.selectedUI, False)

	arg_91_0.menuUI = findTF(arg_91_0._tf, "pop/menuUI")
	arg_91_0.battleScrollRect = GetComponent(findTF(arg_91_0.menuUI, "battList"), typeof(ScrollRect))
	arg_91_0.totalTimes = arg_91_0.getGameTotalTime()

	local var_91_5 = arg_91_0.getGameUsedTimes() - 4 < 0 and 0 or arg_91_0.getGameUsedTimes() - 4

	scrollTo(arg_91_0.battleScrollRect, 0, 1 - var_91_5 / (arg_91_0.totalTimes - 4))
	onButton(arg_91_0, findTF(arg_91_0.menuUI, "rightPanelBg/arrowUp"), function()
		local var_104_0 = arg_91_0.battleScrollRect.normalizedPosition.y + 1 / (arg_91_0.totalTimes - 4)

		if var_104_0 > 1:
			var_104_0 = 1

		scrollTo(arg_91_0.battleScrollRect, 0, var_104_0), SFX_CANCEL)
	onButton(arg_91_0, findTF(arg_91_0.menuUI, "rightPanelBg/arrowDown"), function()
		local var_105_0 = arg_91_0.battleScrollRect.normalizedPosition.y - 1 / (arg_91_0.totalTimes - 4)

		if var_105_0 < 0:
			var_105_0 = 0

		scrollTo(arg_91_0.battleScrollRect, 0, var_105_0), SFX_CANCEL)
	onButton(arg_91_0, findTF(arg_91_0.menuUI, "btnBack"), function()
		arg_91_0.closeView(), SFX_CANCEL)
	onButton(arg_91_0, findTF(arg_91_0.menuUI, "btnRule"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.ssss_game_tip.tip
		}), SFX_CONFIRM)
	onButton(arg_91_0, findTF(arg_91_0.menuUI, "btnStart"), function()
		local var_108_0 = arg_91_0.getGameUsedTimes() or 0
		local var_108_1 = arg_91_0.getGameTimes() or 0

		if var_108_0 >= var_0_55 and arg_91_0.selectedUI:
			arg_91_0.updateSelectedUI()
			setActive(arg_91_0.selectedUI, True)
		else
			local var_108_2
			local var_108_3 = var_108_0 == 0 and 1 or var_108_1 > 0 and var_108_0 + 1 or var_108_0

			var_0_70 = var_0_53[var_108_0 + 1] and var_0_53[var_108_0 + 1] or 1

			if var_108_3 > #var_0_52:
				var_108_3 = #var_0_52

			local var_108_4 = var_0_52[var_108_3]

			var_0_46 = var_108_4[1]
			var_0_47 = var_108_4[2]

			setActive(arg_91_0.menuUI, False)
			arg_91_0.readyStart(), SFX_CONFIRM)

	local var_91_6 = findTF(arg_91_0.menuUI, "tplBattleItem")

	arg_91_0.battleItems = {}
	arg_91_0.dropItems = {}

	for iter_91_2 = 1, 7:
		local var_91_7 = tf(instantiate(var_91_6))

		var_91_7.name = "battleItem_" .. iter_91_2

		setParent(var_91_7, findTF(arg_91_0.menuUI, "battList/Viewport/Content"))

		local var_91_8 = iter_91_2

		GetSpriteFromAtlasAsync(var_0_6, "battleDesc" .. var_91_8, function(arg_109_0)
			setImageSprite(findTF(var_91_7, "state_open/buttomDesc"), arg_109_0, True)
			setImageSprite(findTF(var_91_7, "state_clear/buttomDesc"), arg_109_0, True)
			setImageSprite(findTF(var_91_7, "state_current/buttomDesc"), arg_109_0, True)
			setImageSprite(findTF(var_91_7, "state_closed/buttomDesc"), arg_109_0, True))
		setActive(var_91_7, True)
		table.insert(arg_91_0.battleItems, var_91_7)

	if not arg_91_0.handle:
		arg_91_0.handle = UpdateBeat.CreateListener(arg_91_0.Update, arg_91_0)

	UpdateBeat.AddListener(arg_91_0.handle)

def var_0_0.checkRoleId(arg_110_0, arg_110_1, arg_110_2, arg_110_3):
	local var_110_0 = arg_110_0.matchRoleId(arg_110_1, arg_110_2)
	local var_110_1 = arg_110_2

	if not var_110_0:
		for iter_110_0 = 1, #arg_110_3:
			local var_110_2 = arg_110_3[iter_110_0]

			if arg_110_0.matchRoleId(arg_110_1, var_110_2):
				return arg_110_1, var_110_2

	return arg_110_1, arg_110_2

def var_0_0.matchRoleId(arg_111_0, arg_111_1, arg_111_2):
	if arg_111_1 == arg_111_2:
		return False

	for iter_111_0 = 1, #var_0_49:
		local var_111_0 = var_0_49[iter_111_0]

		if table.contains(var_111_0, arg_111_1) and table.contains(var_111_0, arg_111_2):
			return False

	return True

def var_0_0.initGameUI(arg_112_0):
	arg_112_0.gameUI = findTF(arg_112_0._tf, "ui/gameUI")

	onButton(arg_112_0, findTF(arg_112_0.gameUI, "topRight/btnStop"), function()
		arg_112_0.stopGame()
		setActive(arg_112_0.pauseUI, True))
	onButton(arg_112_0, findTF(arg_112_0.gameUI, "btnLeave"), function()
		arg_112_0.stopGame()
		setActive(arg_112_0.leaveUI, True))

	arg_112_0.gameTimeS = findTF(arg_112_0.gameUI, "top/time/s")
	arg_112_0.scoreTf = findTF(arg_112_0.gameUI, "top/score")
	arg_112_0.scoreAnimTf = findTF(arg_112_0._tf, "sceneContainer/scene_front/scoreAnim")
	arg_112_0.scoreAnimTextTf = findTF(arg_112_0._tf, "sceneContainer/scene_front/scoreAnim/text")

	setActive(arg_112_0.scoreAnimTf, False)

def var_0_0.initController(arg_115_0):
	local var_115_0 = findTF(arg_115_0.gameUI, "box")

	arg_115_0.boxController = var_0_88(var_115_0, arg_115_0)

	local var_115_1 = findTF(arg_115_0.gameUI, "specialPower")
	local var_115_2 = findTF(arg_115_0.gameUI, "successPower")

	arg_115_0.specialController = var_0_90(var_115_1, var_115_2, arg_115_0)

	local var_115_3 = findTF(arg_115_0._tf, "sceneContainer")

	arg_115_0.bgController = var_0_91(var_115_3, arg_115_0.gameUI, arg_115_0)

	local var_115_4 = findTF(arg_115_0._tf, "sceneContainer/scene")

	arg_115_0.roleController = var_0_92(var_115_4, arg_115_0)

def var_0_0.Update(arg_116_0):
	arg_116_0.AddDebugInput()

def var_0_0.AddDebugInput(arg_117_0):
	if arg_117_0.gameStop or arg_117_0.settlementFlag:
		return

	if IsUnityEditor:
		-- block empty

def var_0_0.updateSelectedUI(arg_118_0):
	for iter_118_0 = 1, #arg_118_0.leftSelectRole:
		local var_118_0 = arg_118_0.leftSelectRole[iter_118_0]

		if var_0_46 == var_118_0.id:
			setActive(findTF(var_118_0.tf, "selected"), True)
			setActive(findTF(var_118_0.tf, "unSelected"), False)
		else
			setActive(findTF(var_118_0.tf, "selected"), False)
			setActive(findTF(var_118_0.tf, "unSelected"), True)

	for iter_118_1 = 1, #arg_118_0.rightSelectRole:
		local var_118_1 = arg_118_0.rightSelectRole[iter_118_1]

		setGray(var_118_1.tf, not arg_118_0.matchRoleId(var_0_46, var_118_1.id), True)

		if var_0_47 == var_118_1.id:
			setActive(findTF(var_118_1.tf, "selected"), True)
			setActive(findTF(var_118_1.tf, "unSelected"), False)
		else
			setActive(findTF(var_118_1.tf, "selected"), False)
			setActive(findTF(var_118_1.tf, "unSelected"), True)

def var_0_0.updateMenuUI(arg_119_0):
	local var_119_0 = arg_119_0.getGameUsedTimes()

	if var_119_0 and var_119_0 >= 7:
		setActive(findTF(arg_119_0.menuUI, "btnStart/free"), True)
	else
		setActive(findTF(arg_119_0.menuUI, "btnStart/free"), False)

	local var_119_1 = arg_119_0.getGameTimes()

	for iter_119_0 = 1, #arg_119_0.battleItems:
		setActive(findTF(arg_119_0.battleItems[iter_119_0], "state_open"), False)
		setActive(findTF(arg_119_0.battleItems[iter_119_0], "state_closed"), False)
		setActive(findTF(arg_119_0.battleItems[iter_119_0], "state_clear"), False)
		setActive(findTF(arg_119_0.battleItems[iter_119_0], "state_current"), False)

		if iter_119_0 <= var_119_0:
			setActive(findTF(arg_119_0.battleItems[iter_119_0], "state_clear"), True)
		elif iter_119_0 == var_119_0 + 1 and var_119_1 >= 1:
			setActive(findTF(arg_119_0.battleItems[iter_119_0], "state_current"), True)
		elif var_119_0 < iter_119_0 and iter_119_0 <= var_119_0 + var_119_1:
			setActive(findTF(arg_119_0.battleItems[iter_119_0], "state_open"), True)
		else
			setActive(findTF(arg_119_0.battleItems[iter_119_0], "state_closed"), True)

	arg_119_0.totalTimes = arg_119_0.getGameTotalTime()

	local var_119_2 = 1 - (arg_119_0.getGameUsedTimes() - 3 < 0 and 0 or arg_119_0.getGameUsedTimes() - 3) / (arg_119_0.totalTimes - 4)

	if var_119_2 > 1:
		var_119_2 = 1

	scrollTo(arg_119_0.battleScrollRect, 0, var_119_2)
	setActive(findTF(arg_119_0.menuUI, "btnStart/tip"), var_119_1 > 0)

	local var_119_3

	if var_0_70 == var_0_68:
		var_119_3 = var_0_65
	elif var_0_70 == var_0_69:
		var_119_3 = var_0_66

	for iter_119_1, iter_119_2 in ipairs(var_0_64):
		local var_119_4 = findTF(arg_119_0._tf, "bg/" .. iter_119_2)

		setActive(var_119_4, table.contains(var_119_3, iter_119_2))

	setActive(findTF(arg_119_0.menuUI, "bg/title_day"), var_0_70 == var_0_68)
	setActive(findTF(arg_119_0.menuUI, "bg/title_night"), var_0_70 != var_0_68)
	arg_119_0.CheckGet()

def var_0_0.CheckGet(arg_120_0):
	setActive(findTF(arg_120_0.menuUI, "got"), False)

	if arg_120_0.getUltimate() and arg_120_0.getUltimate() != 0:
		setActive(findTF(arg_120_0.menuUI, "got"), True)

	if arg_120_0.getUltimate() == 0:
		if arg_120_0.getGameTotalTime() > arg_120_0.getGameUsedTimes():
			return

		pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = arg_120_0.GetMGHubData().id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})
		setActive(findTF(arg_120_0.menuUI, "got"), True)

def var_0_0.openMenuUI(arg_121_0):
	setActive(findTF(arg_121_0._tf, "sceneContainer/scene_front"), False)
	setActive(findTF(arg_121_0._tf, "sceneContainer/scene_background"), False)
	setActive(findTF(arg_121_0._tf, "sceneContainer/scene"), False)
	setActive(arg_121_0.gameUI, False)
	setActive(arg_121_0.menuUI, True)
	setActive(arg_121_0.selectedUI, False)
	arg_121_0.updateMenuUI()

	local var_121_0 = arg_121_0.getBGM()

	if not var_121_0:
		if pg.CriMgr.GetInstance().IsDefaultBGM():
			var_121_0 = pg.voice_bgm.NewMainScene.default_bgm
		else
			var_121_0 = pg.voice_bgm.NewMainScene.bgm

	if arg_121_0.bgm != var_121_0:
		arg_121_0.bgm = var_121_0

		pg.BgmMgr.GetInstance().Push(arg_121_0.__cname, var_121_0)

def var_0_0.clearUI(arg_122_0):
	setActive(arg_122_0.sceneTf, False)
	setActive(arg_122_0.settlementUI, False)
	setActive(arg_122_0.countUI, False)
	setActive(arg_122_0.menuUI, False)
	setActive(arg_122_0.gameUI, False)
	setActive(arg_122_0.selectedUI, False)

def var_0_0.readyStart(arg_123_0):
	setActive(arg_123_0.countUI, True)
	arg_123_0.countAnimator.Play("count")
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_3)

	if var_0_2 and arg_123_0.bgm != var_0_2:
		arg_123_0.bgm = var_0_2

		pg.BgmMgr.GetInstance().Push(arg_123_0.__cname, var_0_2)

def var_0_0.gameStart(arg_124_0):
	setActive(findTF(arg_124_0._tf, "sceneContainer/scene_front"), True)
	setActive(findTF(arg_124_0._tf, "sceneContainer/scene_background"), True)
	setActive(findTF(arg_124_0._tf, "sceneContainer/scene"), True)
	setActive(arg_124_0.scoreAnimTf, False)
	setActive(arg_124_0.gameUI, True)

	arg_124_0.gameStartFlag = True
	arg_124_0.scoreNum = 0
	arg_124_0.playerPosIndex = 2
	arg_124_0.gameStepTime = 0
	arg_124_0.gameTime = var_0_7
	arg_124_0.ignoreTime = False

	arg_124_0.boxController.start()
	arg_124_0.specialController.start()
	arg_124_0.bgController.start()
	arg_124_0.roleController.start()
	arg_124_0.updateGameUI()
	arg_124_0.timerStart()

def var_0_0.getGameTimes(arg_125_0):
	return arg_125_0.GetMGHubData().count

def var_0_0.getGameUsedTimes(arg_126_0):
	return arg_126_0.GetMGHubData().usedtime

def var_0_0.getUltimate(arg_127_0):
	return arg_127_0.GetMGHubData().ultimate

def var_0_0.getGameTotalTime(arg_128_0):
	return (arg_128_0.GetMGHubData().getConfig("reward_need"))

def var_0_0.changeSpeed(arg_129_0, arg_129_1):
	return

def var_0_0.onTimer(arg_130_0):
	arg_130_0.gameStep()

def var_0_0.gameStep(arg_131_0):
	if not arg_131_0.ignoreTime:
		arg_131_0.gameTime = arg_131_0.gameTime - Time.deltaTime

		if arg_131_0.gameTime < 0:
			arg_131_0.gameTime = 0

		arg_131_0.gameStepTime = arg_131_0.gameStepTime + Time.deltaTime

	arg_131_0.boxController.step()
	arg_131_0.specialController.step()
	arg_131_0.bgController.step()
	arg_131_0.roleController.step()
	arg_131_0.updateGameUI()

	if arg_131_0.gameTime <= 0:
		arg_131_0.onGameOver()

		return

def var_0_0.timerStart(arg_132_0):
	if not arg_132_0.timer.running:
		arg_132_0.timer.Start()

def var_0_0.timerStop(arg_133_0):
	if arg_133_0.timer.running:
		arg_133_0.timer.Stop()

def var_0_0.updateGameUI(arg_134_0):
	setText(arg_134_0.scoreTf, arg_134_0.scoreNum)
	setText(arg_134_0.gameTimeS, math.ceil(arg_134_0.gameTime))

def var_0_0.addScore(arg_135_0, arg_135_1):
	setActive(arg_135_0.scoreAnimTf, False)
	setActive(arg_135_0.scoreAnimTf, True)
	setText(arg_135_0.scoreAnimTextTf, "+" .. tostring(arg_135_1))

	arg_135_0.scoreNum = arg_135_0.scoreNum + arg_135_1

	if arg_135_0.scoreNum < 0:
		arg_135_0.scoreNum = 0

def var_0_0.onGameOver(arg_136_0):
	if arg_136_0.settlementFlag:
		return

	arg_136_0.timerStop()

	arg_136_0.settlementFlag = True

	setActive(arg_136_0.clickMask, True)

	if arg_136_0.roleController:
		arg_136_0.roleController.clear()

	if arg_136_0.bgController:
		arg_136_0.bgController.clear()

	LeanTween.delayedCall(go(arg_136_0._tf), 0.1, System.Action(function()
		arg_136_0.settlementFlag = False
		arg_136_0.gameStartFlag = False

		setActive(arg_136_0.clickMask, False)
		arg_136_0.showSettlement()))

def var_0_0.showSettlement(arg_138_0):
	setActive(arg_138_0.settlementUI, True)
	GetComponent(findTF(arg_138_0.settlementUI, "ad"), typeof(Animator)).Play("settlement", -1, 0)

	local var_138_0 = arg_138_0.GetMGData().GetRuntimeData("elements")
	local var_138_1 = arg_138_0.scoreNum
	local var_138_2 = var_138_0 and #var_138_0 > 0 and var_138_0[1] or 0

	setActive(findTF(arg_138_0.settlementUI, "ad/new"), var_138_2 < var_138_1)

	if var_138_2 <= var_138_1:
		var_138_2 = var_138_1

		arg_138_0.StoreDataToServer({
			var_138_2
		})

	local var_138_3 = findTF(arg_138_0.settlementUI, "ad/highText")
	local var_138_4 = findTF(arg_138_0.settlementUI, "ad/currentText")

	setText(var_138_3, var_138_2)
	setText(var_138_4, var_138_1)

	if arg_138_0.getGameTimes() and arg_138_0.getGameTimes() > 0:
		arg_138_0.sendSuccessFlag = True

		arg_138_0.SendSuccess(0)

def var_0_0.resumeGame(arg_139_0):
	arg_139_0.gameStop = False

	setActive(arg_139_0.leaveUI, False)
	arg_139_0.changeSpeed(1)
	arg_139_0.timerStart()

def var_0_0.stopGame(arg_140_0):
	arg_140_0.gameStop = True

	arg_140_0.timerStop()
	arg_140_0.changeSpeed(0)

def var_0_0.onBackPressed(arg_141_0):
	if not arg_141_0.gameStartFlag:
		arg_141_0.emit(var_0_0.ON_BACK_PRESSED)
	else
		if arg_141_0.settlementFlag:
			return

		if isActive(arg_141_0.pauseUI):
			setActive(arg_141_0.pauseUI, False)

		arg_141_0.stopGame()
		setActive(arg_141_0.leaveUI, True)

def var_0_0.willExit(arg_142_0):
	if arg_142_0.handle:
		UpdateBeat.RemoveListener(arg_142_0.handle)

	if arg_142_0._tf and LeanTween.isTweening(go(arg_142_0._tf)):
		LeanTween.cancel(go(arg_142_0._tf))

	if arg_142_0.timer and arg_142_0.timer.running:
		arg_142_0.timer.Stop()

	Time.timeScale = 1
	arg_142_0.timer = None

return var_0_0
