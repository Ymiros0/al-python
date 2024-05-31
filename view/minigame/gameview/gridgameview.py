local var_0_0 = class("GridGameView", import("..BaseMiniGameView"))
local var_0_1 = "battle-boss-4"
local var_0_2 = "event./ui/ddldaoshu2"
local var_0_3 = "event./ui/niujiao"
local var_0_4 = "event./ui/taosheng"
local var_0_5 = 70
local var_0_6 = "mini_game_time"
local var_0_7 = "mini_game_score"
local var_0_8 = "mini_game_leave"
local var_0_9 = "mini_game_pause"
local var_0_10 = "mini_game_cur_score"
local var_0_11 = "mini_game_high_score"
local var_0_12 = "event grid combo"
local var_0_13 = "event grid trigger"
local var_0_14 = "event move role"
local var_0_15 = "event add score"
local var_0_16 = "event role special"
local var_0_17 = "event special end"
local var_0_18 = "event camera in"
local var_0_19 = "event camedra out"
local var_0_20 = "event ignore time"
local var_0_21 = {
	power_grid = 0,
	grid_index = 0,
	special_time = False,
	special_complete = False
}
local var_0_22 = {
	{
		index = 1,
		name = "red",
		max = 800
	},
	{
		index = 2,
		name = "yellow",
		max = 800
	},
	{
		index = 3,
		name = "blue",
		max = 800
	}
}
local var_0_23 = 0.2
local var_0_24 = 50
local var_0_25 = 3
local var_0_26 = 150
local var_0_27 = 500
local var_0_28 = 300
local var_0_29 = 50
local var_0_30 = 4000
local var_0_31 = 1
local var_0_32 = 3
local var_0_33 = {
	1,
	2
}
local var_0_34 = {
	1,
	2,
	3
}
local var_0_35 = {
	{
		1,
		3
	},
	{
		2,
		3
	},
	{
		1,
		2
	},
	{
		2,
		1
	},
	{
		1,
		3
	},
	{
		2,
		3
	},
	{
		1,
		2
	}
}
local var_0_36 = Vector2(0, 0)
local var_0_37 = 0.07
local var_0_38 = 0.3
local var_0_39 = 0.5
local var_0_40 = 5
local var_0_41 = "sound start"
local var_0_42 = "sound trigger"
local var_0_43 = "sound end"
local var_0_44 = {
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
local var_0_45 = {
	n_Move_R = {
		time = 0,
		anim_name = var_0_44.n_MoveR,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance = Vector3(650, 0, 0)
		}
	},
	n_Atk = {
		time = 0,
		sound_trigger = "taosheng",
		anim_name = var_0_44.n_Atk,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance = Vector3(650, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	n_Move_L = {
		time = 0,
		anim_name = var_0_44.n_MoveL,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance = Vector3(0, 0, 0)
		}
	},
	n_Skill_1 = {
		time = 0,
		sound_trigger = "jiguang",
		anim_name = var_0_44.n_Skill_1
	},
	n_Skill_2 = {
		time = 0,
		sound_trigger = "guangjian",
		anim_name = var_0_44.n_Skill_2,
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
		anim_name = var_0_44.n_Skill_3
	},
	n_Combine = {
		sound_start = "bianshen",
		time = 0,
		camera = True,
		anim_name = var_0_44.n_Combine
	},
	n_DMG = {
		time = 0,
		anim_name = var_0_44.n_DMG,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance = Vector3(-50, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	n_DMG_S = {
		time = 0,
		anim_name = var_0_44.n_DMG
	},
	n_DMG_Back_R = {
		time = 0,
		anim_name = var_0_44.n_MoveR,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance = Vector3(0, 0, 0)
		}
	},
	n_Neutral = {
		time = 0,
		anim_name = var_0_44.n_Neutral
	},
	c_Atk = {
		time = 0,
		sound_trigger = "taosheng",
		anim_name = var_0_44.c_Atk,
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
		anim_name = var_0_44.c_Skill_1
	},
	c_Dmg = {
		time = 0,
		anim_name = var_0_44.c_Dmg,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance = Vector3(-50, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	c_Dmg_S = {
		time = 0,
		anim_name = var_0_44.c_Dmg
	},
	c_MoveL = {
		time = 0,
		anim_name = var_0_44.c_MoveL,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance = Vector3(0, 0, 0)
		}
	},
	c_MoveR = {
		time = 0,
		anim_name = var_0_44.c_MoveR,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance = Vector3(650, 0, 0)
		}
	},
	c_DMG_Back_R = {
		time = 0,
		anim_name = var_0_44.c_MoveR,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance = Vector3(0, 0, 0)
		}
	},
	c_Neutral = {
		time = 0,
		anim_name = var_0_44.c_Neutral
	}
}
local var_0_46 = {
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
			var_0_45.n_Atk,
			var_0_45.n_Move_L
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
			var_0_45.n_Skill_1
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
			var_0_45.n_Skill_2,
			var_0_45.n_Move_L
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
			var_0_45.n_Skill_3
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
			var_0_45.n_DMG,
			var_0_45.n_DMG_Back_R
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
			var_0_45.n_DMG_S
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
			var_0_45.n_DMG_Back_R
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
			var_0_45.n_Combine
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
			var_0_45.c_Atk,
			var_0_45.c_MoveL
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
			var_0_45.c_Skill_1
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
			var_0_45.c_Skill_1
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
			var_0_45.c_Skill_1
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
			var_0_45.c_Dmg,
			var_0_45.c_DMG_Back_R
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
			var_0_45.c_Dmg_S
		}
	}
}
local var_0_47 = {
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
local var_0_48 = {
	n_Move_R = {
		time = 0,
		anim_name = var_0_47.n_MoveR,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance = Vector3(500, 0, 0)
		}
	},
	n_Atk = {
		time = 0,
		sound_trigger = "taosheng",
		anim_name = var_0_47.n_Atk,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance = Vector3(600, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	n_Move_L = {
		time = 0,
		anim_name = var_0_47.n_MoveL,
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
		anim_name = var_0_47.n_Skill_1,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance = Vector3(600, 0, 0)
		}
	},
	n_Skill_2 = {
		time = 0,
		sound_trigger = "baozha2",
		anim_name = var_0_47.n_Skill_2
	},
	n_Skill_3 = {
		time = 0,
		sound_trigger = "baozha2",
		anim_name = var_0_47.n_Skill_3,
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
		anim_name = var_0_47.n_Combine
	},
	n_DMG = {
		time = 0,
		anim_name = var_0_47.n_DMG,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance = Vector3(-50, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	n_DMG_S = {
		time = 0,
		anim_name = var_0_47.n_DMG
	},
	n_DMG_Back_R = {
		time = 0,
		anim_name = var_0_47.n_MoveR,
		move = {
			time = 0.2,
			start = Vector2(0, 0),
			distance = Vector3(0, 0, 0)
		}
	},
	n_Neutral = {
		time = 0,
		anim_name = var_0_47.n_Neutral
	},
	c_Atk = {
		time = 0,
		sound_trigger = "taosheng",
		anim_name = var_0_47.c_Atk,
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
		anim_name = var_0_47.c_Skill_1
	},
	c_Dmg = {
		time = 0,
		anim_name = var_0_47.c_Dmg,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance = Vector3(-50, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	c_Dmg_S = {
		time = 0,
		anim_name = var_0_47.c_Dmg
	},
	c_MoveL = {
		time = 0,
		anim_name = var_0_47.c_MoveL,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance = Vector3(0, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	c_MoveR = {
		time = 0,
		anim_name = var_0_47.c_MoveR,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance = Vector3(650, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	c_DMG_Back_R = {
		time = 0,
		anim_name = var_0_47.c_MoveR,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance = Vector3(0, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	c_Neutral = {
		time = 0,
		anim_name = var_0_47.c_Neutral
	}
}
local var_0_49 = {
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
			var_0_48.n_Atk,
			var_0_48.n_Move_L
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
			var_0_48.n_Move_R,
			var_0_48.n_Skill_1,
			var_0_48.n_Move_L
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
			var_0_48.n_Skill_2
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
			var_0_48.n_Skill_3,
			var_0_48.n_Move_L
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
			var_0_48.n_DMG,
			var_0_48.n_DMG_Back_R
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
			var_0_48.n_DMG_S
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
			var_0_48.n_DMG_Back_R
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
			var_0_48.n_Combine
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
			var_0_48.c_Atk,
			var_0_48.c_MoveL
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
			var_0_48.c_Skill_1
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
			var_0_48.c_Skill_1
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
			var_0_48.c_Skill_1
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
			var_0_48.c_Dmg,
			var_0_48.c_DMG_Back_R
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
			var_0_48.c_Dmg_S
		}
	}
}
local var_0_50 = {
	Neutral = "Neutral",
	Skill_1 = "skill_1",
	Skill_2 = "skill_2",
	Atk = "ATK",
	MoveL = "MoveL",
	DMG = "DMG",
	MoveR = "MoveR"
}
local var_0_51 = {
	Move_R = {
		time = 0,
		anim_name = var_0_50.MoveR,
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
		anim_name = var_0_50.Atk,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance = Vector3(600, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	Move_L = {
		time = 0,
		anim_name = var_0_50.MoveL,
		move = {
			time = 0.4,
			distance = Vector3(0, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	Skill_1 = {
		time = 0,
		sound_trigger = "jiguang",
		anim_name = var_0_50.Skill_1
	},
	Skill_2 = {
		time = 0,
		sound_trigger = "baozha2",
		anim_name = var_0_50.Skill_2,
		over_offset = Vector2(115, 0)
	},
	DMG = {
		time = 0,
		anim_name = var_0_50.DMG,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance = Vector3(-50, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	DMG_Back_R = {
		time = 0,
		anim_name = var_0_50.MoveR,
		move = {
			time = 0.3,
			start = Vector2(0, 0),
			distance = Vector3(0, 0, 0),
			ease = LeanTweenType.easeOutCirc
		}
	},
	DMG_S = {
		time = 0,
		anim_name = var_0_50.DMG
	},
	Neutral = {
		time = 0,
		anim_name = var_0_50.Neutral
	}
}
local var_0_52 = {
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
			var_0_51.Atk,
			var_0_51.Move_L
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
			var_0_51.Skill_1
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
			var_0_51.Move_R,
			var_0_51.Skill_2,
			var_0_51.Move_L
		}
	},
	{
		dmg_index = 2,
		name = "DMG",
		special_time = False,
		actions = {
			var_0_51.DMG,
			var_0_51.DMG_Back_R
		}
	},
	{
		dmg_index = 1,
		name = "DMG_Stand",
		special_time = False,
		actions = {
			var_0_51.DMG_S
		}
	}
}
local var_0_53 = {
	{
		index = 1,
		name = "role1",
		skill = var_0_46,
		actions = var_0_45
	},
	{
		index = 2,
		name = "role2",
		skill = var_0_49,
		actions = var_0_48
	},
	{
		index = 3,
		name = "enemy1",
		skill = var_0_52,
		actions = var_0_51
	}
}

local function var_0_54(arg_1_0, arg_1_1)
	local var_1_0 = {}
	local var_1_1 = 12
	local var_1_2 = 0.3
	local var_1_3 = Vector2(138, 150)
	local var_1_4 = 2500
	local var_1_5 = 0
	local var_1_6 = 100
	local var_1_7 = {
		{
			index = 1,
			name = "red"
		},
		{
			index = 2,
			name = "yellow"
		},
		{
			index = 3,
			name = "blue"
		}
	}

	function var_1_0.ctor(arg_2_0)
		arg_2_0._boxTf = arg_1_0
		arg_2_0._event = arg_1_1
		arg_2_0._gridEffect = findTF(arg_2_0._boxTf, "effectGrid")
		arg_2_0._content = findTF(arg_2_0._boxTf, "viewport/content")
		arg_2_0.tplGrid = findTF(arg_1_0, "tplGrid")

		setActive(arg_2_0.tplGrid, False)

		arg_2_0.grids = {}
		arg_2_0.effects = {}
		arg_2_0.combo = 0

		for iter_2_0 = 1, var_1_1:
			local var_2_0 = tf(instantiate(arg_2_0._gridEffect))

			setParent(var_2_0, arg_2_0._content)
			setActive(var_2_0, False)

			var_2_0.anchoredPosition = Vector2(var_1_3.x * iter_2_0 - var_1_3.x / 2, var_1_3.y / 2)

			table.insert(arg_2_0.effects, var_2_0)

	function var_1_0.start(arg_3_0)
		arg_3_0.nextCheck = False

		arg_3_0.initGrids(False)

		for iter_3_0 = 1, #arg_3_0.effects:
			setActive(arg_3_0.effects[iter_3_0], False)

	function var_1_0.step(arg_4_0)
		if arg_4_0.takeAwayTime and arg_4_0.takeAwayTime > 0:
			arg_4_0.takeAwayTime = arg_4_0.takeAwayTime - Time.deltaTime

			return

		arg_4_0.gridCreateIndex = 1

		local var_4_0 = False

		for iter_4_0 = 1, #arg_4_0.grids:
			local var_4_1 = arg_4_0.grids[iter_4_0]
			local var_4_2 = iter_4_0

			if not var_4_1.checkAble:
				var_4_0 = var_4_0 or True

				local var_4_3 = (iter_4_0 - 1) * var_1_3.x

				if var_4_3 < var_4_1.tf.anchoredPosition.x:
					var_4_1.tf.anchoredPosition = Vector2(var_4_1.tf.anchoredPosition.x - var_4_1.speed * Time.deltaTime, 0)

					if var_4_1.speed < var_1_4:
						var_4_1.speed = var_4_1.speed + var_1_6

				if var_4_3 >= var_4_1.tf.anchoredPosition.x:
					var_4_1.speed = 0
					var_4_1.checkAble = True

					if var_4_3 > var_4_1.tf.anchoredPosition.x:
						var_4_1.tf.anchoredPosition = Vector2(var_4_3, 0)

			if not var_4_1.eventAble:
				GetComponent(var_4_1.tf, typeof(EventTriggerListener)).AddPointDownFunc(function()
					if arg_4_0.nextCheck == False:
						local var_5_0, var_5_1 = arg_4_0.triggerDownGrid(var_4_2)

						if #var_5_0 >= 2:
							arg_4_0.nextCheck = True

							arg_4_0.takeAwayGrid(var_5_0)
							arg_4_0.insertGrids()
							arg_4_0._event.emit(var_0_12, {
								series = #var_5_0,
								combo = arg_4_0.combo,
								index = var_5_1
							})

							arg_4_0.combo = arg_4_0.combo + 1
						else
							arg_4_0.nextCheck = True

							arg_4_0.takeAwayGrid({
								var_4_2
							})
							arg_4_0.insertGrids())

				var_4_1.eventAble = True

		if not var_4_0 and arg_4_0.nextCheck:
			local var_4_4 = arg_4_0.getSeriesGrids()

			if #var_4_4 > 0:
				local var_4_5 = {}

				for iter_4_1 = 1, #var_4_4:
					local var_4_6 = var_4_4[iter_4_1].series
					local var_4_7 = var_4_4[iter_4_1].gridIndex

					for iter_4_2 = 1, #var_4_6:
						table.insert(var_4_5, var_4_6[iter_4_2])

					arg_4_0._event.emit(var_0_12, {
						series = #var_4_6,
						combo = arg_4_0.combo,
						index = var_4_7
					})

				arg_4_0.clearGridSeriesAble()
				arg_4_0.takeAwayGrid(var_4_5)
				arg_4_0.insertGrids()

				arg_4_0.nextCheck = True
				arg_4_0.combo = arg_4_0.combo + 1
			else
				arg_4_0.nextCheck = False

				if not var_0_21.special_time:
					arg_4_0.combo = 0

	function var_1_0.clear(arg_6_0)
		for iter_6_0 = 1, #arg_6_0.grids:
			if arg_6_0.grids[iter_6_0].tf:
				destroy(arg_6_0.grids[iter_6_0].tf)

		arg_6_0.grids = {}
		arg_6_0.gridCreateIndex = 1

	function var_1_0.clearGridSeriesAble(arg_7_0)
		for iter_7_0 = 1, #arg_7_0.grids:
			if arg_7_0.grids[iter_7_0].seriesAble:
				arg_7_0.grids[iter_7_0].seriesAble = False

	function var_1_0.getSeriesGrids(arg_8_0)
		local var_8_0 = {}
		local var_8_1
		local var_8_2 = {}

		for iter_8_0 = 1, #arg_8_0.grids:
			local var_8_3 = arg_8_0.grids[iter_8_0]

			if not var_8_1:
				var_8_1 = var_8_3.index

				table.insert(var_8_2, iter_8_0)
			elif var_8_1 == var_8_3.index:
				table.insert(var_8_2, iter_8_0)

				if #var_8_2 >= 3 and iter_8_0 == #arg_8_0.grids and arg_8_0.checkSeriesAble(var_8_2):
					table.insert(var_8_0, {
						series = var_8_2,
						gridIndex = var_8_1
					})
			elif var_8_1 != var_8_3.index:
				if #var_8_2 >= 3 and arg_8_0.checkSeriesAble(var_8_2):
					table.insert(var_8_0, {
						series = var_8_2,
						gridIndex = var_8_1
					})

				var_8_2 = {}
				var_8_1 = var_8_3.index

				table.insert(var_8_2, iter_8_0)

		return var_8_0

	function var_1_0.checkSeriesAble(arg_9_0, arg_9_1)
		for iter_9_0 = 1, #arg_9_1:
			if arg_9_0.grids[arg_9_1[iter_9_0]].seriesAble:
				return True

		return False

	function var_1_0.insertGrids(arg_10_0)
		local var_10_0 = var_1_1 - #arg_10_0.grids

		for iter_10_0 = 1, var_10_0:
			local var_10_1 = arg_10_0.createGridData()

			table.insert(arg_10_0.grids, var_10_1)

		if arg_10_0.checkGridsSeries():
			arg_10_0.instiateGrids(True)
		else
			arg_10_0.initGrids(True)

		arg_10_0.changeAbleGrids()

	function var_1_0.changeAbleGrids(arg_11_0)
		for iter_11_0 = 1, #arg_11_0.grids:
			arg_11_0.grids[iter_11_0].checkAble = False
			arg_11_0.grids[iter_11_0].eventAble = False
			arg_11_0.grids[iter_11_0].speed = var_1_5

	function var_1_0.takeAwayGrid(arg_12_0, arg_12_1)
		table.sort(arg_12_1, function(arg_13_0, arg_13_1)
			return arg_13_0 <= arg_13_1)

		arg_12_0.takeAwayTime = var_1_2

		local var_12_0 = {}

		if arg_12_1[1] - 1 > 0:
			arg_12_0.grids[arg_12_1[1] - 1].seriesAble = True

		pg.CriMgr.GetInstance().PlaySoundEffect_V3("event./ui/" .. "xiaochu")

		for iter_12_0 = #arg_12_1, 1, -1:
			table.insert(var_12_0, table.remove(arg_12_0.grids, arg_12_1[iter_12_0]))
			setActive(arg_12_0.effects[arg_12_1[iter_12_0]], False)
			setActive(arg_12_0.effects[arg_12_1[iter_12_0]], True)

		for iter_12_1 = 1, #var_12_0:
			destroy(var_12_0[iter_12_1].tf)

			var_12_0[iter_12_1] = 0

		local var_12_1 = {}

	function var_1_0.triggerDownGrid(arg_14_0, arg_14_1)
		local var_14_0 = arg_14_0.grids[arg_14_1]
		local var_14_1 = {
			arg_14_1
		}

		if not var_14_0:
			return var_14_1, 0

		for iter_14_0 = arg_14_1 - 1, 1, -1:
			local var_14_2 = arg_14_0.grids[iter_14_0]

			if var_14_0.index == var_14_2.index:
				table.insert(var_14_1, iter_14_0)
			else
				break

		for iter_14_1 = arg_14_1 + 1, #arg_14_0.grids:
			local var_14_3 = arg_14_0.grids[iter_14_1]

			if var_14_0.index == var_14_3.index:
				table.insert(var_14_1, iter_14_1)
			else
				break

		table.sort(var_14_1, function(arg_15_0, arg_15_1)
			return arg_15_0 <= arg_15_1)

		return var_14_1, var_14_0.index

	function var_1_0.initGrids(arg_16_0, arg_16_1)
		arg_16_0.clear()

		for iter_16_0 = 1, var_1_1:
			local var_16_0 = arg_16_0.createGridData()

			table.insert(arg_16_0.grids, var_16_0)

		if arg_16_0.checkGridsSeries():
			arg_16_0.instiateGrids(arg_16_1)
		else
			arg_16_0.initGrids(arg_16_1)

		arg_16_0.nextCheck = False

	function var_1_0.instiateGrids(arg_17_0, arg_17_1)
		for iter_17_0 = 1, #arg_17_0.grids:
			local var_17_0 = arg_17_0.grids[iter_17_0]

			if not var_17_0.tf:
				local var_17_1 = tf(instantiate(arg_17_0.tplGrid))

				SetParent(var_17_1, arg_17_0._content)
				setActive(var_17_1, True)
				setActive(findTF(var_17_1, var_17_0.name), True)

				local var_17_2

				if arg_17_1:
					var_17_2 = (var_1_1 + arg_17_0.gridCreateIndex - 1) * var_1_3.x
				else
					var_17_2 = (arg_17_0.gridCreateIndex - 1) * var_1_3.x

				var_17_1.anchoredPosition = Vector2(var_17_2, 0)
				arg_17_0.gridCreateIndex = arg_17_0.gridCreateIndex + 1
				var_17_0.tf = var_17_1

	function var_1_0.createGridData(arg_18_0, arg_18_1)
		local var_18_0

		if arg_18_1:
			var_18_0 = Clone(var_1_7[arg_18_1])
		else
			var_18_0 = Clone(var_1_7[math.random(1, #var_1_7)])

		local var_18_1 = var_18_0.index
		local var_18_2 = var_18_0.name

		return {
			eventAble = False,
			checkAble = False,
			speed = var_1_5,
			index = var_18_1,
			name = var_18_2
		}

	function var_1_0.checkGridsSeries(arg_19_0)
		return True

	var_1_0.ctor()

	return var_1_0

local var_0_55 = False

local function var_0_56(arg_20_0, arg_20_1, arg_20_2)
	local var_20_0 = {
		def ctor:(arg_21_0)
			arg_21_0._specialTf = arg_20_0
			arg_21_0._successTf = arg_20_1
			arg_21_0._effectSuccess = findTF(arg_21_0._successTf, "effectSuccess")
			arg_21_0._event = arg_20_2

			arg_21_0._event.bind(var_0_12, function(arg_22_0, arg_22_1, arg_22_2)
				local var_22_0 = arg_22_1.series
				local var_22_1 = arg_22_1.combo
				local var_22_2 = arg_22_1.index

				arg_21_0.addPowerAmount(var_22_2, arg_21_0.getPowerAmount(var_22_0, var_22_1)))

			arg_21_0.powers = {}

			for iter_21_0 = 1, #var_0_22:
				local var_21_0 = findTF(arg_21_0._specialTf, var_0_22[iter_21_0].name)
				local var_21_1 = var_0_22[iter_21_0].index
				local var_21_2 = var_0_22[iter_21_0].max
				local var_21_3 = var_0_22[iter_21_0].cur
				local var_21_4 = {
					active = False,
					tf = var_21_0,
					index = var_21_1,
					max = var_21_2,
					cur = var_21_3
				}

				table.insert(arg_21_0.powers, var_21_4)

			arg_21_0.success = {
				cur = 0,
				slider = GetComponent(findTF(arg_21_0._successTf, "box"), typeof(Slider)),
				max = var_0_30
			},
		def start:(arg_23_0)
			for iter_23_0 = 1, #arg_23_0.powers:
				local var_23_0 = arg_23_0.powers[iter_23_0]

				var_23_0.cur = 0
				var_23_0.active = False

			arg_23_0.success.cur = 0
			arg_23_0.success.active = False

			setActive(arg_23_0._effectSuccess, False)
			arg_23_0.resetSpecialData()
			arg_23_0.step(),
		def step:(arg_24_0)
			for iter_24_0 = 1, #arg_24_0.powers:
				local var_24_0 = arg_24_0.powers[iter_24_0]

				if var_24_0.active and var_24_0.cur > 0:
					var_24_0.cur = var_24_0.cur - var_0_27 * Time.deltaTime

					if var_24_0.cur <= 0:
						var_24_0.active = False
						var_24_0.cur = 0

				GetComponent(var_24_0.tf, typeof(Slider)).value = var_24_0.cur > 0 and var_24_0.cur / var_24_0.max or 0

			if arg_24_0.success.active and arg_24_0.success.cur > 0 and var_0_21.special_complete:
				arg_24_0.success.cur = arg_24_0.success.cur - var_0_28 * Time.deltaTime

				if arg_24_0.success.cur <= 0:
					arg_24_0.success.active = False
					arg_24_0.success.cur = 0

					arg_24_0._event.emit(var_0_17)

			if arg_24_0.success.cur >= arg_24_0.success.max or arg_24_0.success.active:
				setActive(arg_24_0._effectSuccess, True)
			else
				setActive(arg_24_0._effectSuccess, False)

			arg_24_0.success.slider.value = arg_24_0.success.cur > 0 and arg_24_0.success.cur / arg_24_0.success.max or 0
			var_0_21.special_time = arg_24_0.success.active
			var_0_21.grid_index = 0,
		def clear:(arg_25_0)
			return,
		def updateSpecialData:(arg_26_0, arg_26_1)
			var_0_21.special_time = arg_26_0.success.active
			var_0_21.grid_index = arg_26_1
			var_0_21.power_grid = 0

			for iter_26_0 = 1, #arg_26_0.powers:
				if arg_26_0.powers[iter_26_0].index == arg_26_1 and arg_26_0.powers[iter_26_0].cur == arg_26_0.powers[iter_26_0].max:
					var_0_21.power_grid = arg_26_0.powers[iter_26_0].index

			arg_26_0._event.emit(var_0_13),
		def resetSpecialData:(arg_27_0)
			var_0_21.special_complete = False,
		def addPowerAmount:(arg_28_0, arg_28_1, arg_28_2)
			local var_28_0 = arg_28_0.getPowerByIndex(arg_28_1)

			if arg_28_0.success and not arg_28_0.success.active:
				arg_28_0.success.cur = arg_28_0.success.cur + arg_28_2

				if arg_28_0.success.cur >= arg_28_0.success.max:
					arg_28_0.success.cur = arg_28_0.success.max

					if not isActive(arg_28_0._effectSuccess):
						setActive(arg_28_0._effectSuccess, True)

					arg_28_0.success.active = True
					var_0_21.special_complete = False

					arg_28_0._event.emit(var_0_16)

			if var_28_0 and not var_28_0.active:
				var_28_0.cur = var_28_0.cur + arg_28_2

				if var_28_0.cur >= var_28_0.max:
					var_28_0.cur = var_28_0.max
					var_28_0.active = True

			if arg_28_2 > 0:
				arg_28_0.updateSpecialData(arg_28_1),
		def getPowerByIndex:(arg_29_0, arg_29_1)
			for iter_29_0 = 1, #arg_29_0.powers:
				if arg_29_0.powers[iter_29_0].index == arg_29_1:
					return arg_29_0.powers[iter_29_0]

			return None,
		def getPowerAmount:(arg_30_0, arg_30_1, arg_30_2)
			if arg_30_1 <= 2:
				return var_0_29

			return (var_0_26 + (arg_30_1 - var_0_25) * var_0_24) * (1 + arg_30_2 * var_0_23)
	}

	var_20_0.ctor()

	return var_20_0

local function var_0_57(arg_31_0, arg_31_1, arg_31_2)
	local var_31_0 = {}
	local var_31_1 = {
		{
			rate = 0.05,
			source = "scene_background/bg01"
		},
		{
			rate = 0.1,
			source = "scene_background/bg02"
		},
		{
			rate = 0.2,
			source = "scene_background/bg03"
		},
		{
			rate = 0.8,
			source = "scene_background/bg04"
		},
		{
			rate = 1.2,
			source = "scene_front/bg05"
		},
		{
			rate = 1,
			source = "scene/rolePos"
		}
	}

	function var_31_0.ctor(arg_32_0)
		arg_32_0._sceneTf = arg_31_0
		arg_32_0._event = arg_31_2
		arg_32_0.bgs = {}
		arg_32_0._gameTf = arg_31_1
		arg_32_0._box = findTF(arg_32_0._gameTf, "box")
		arg_32_0._specialPower = findTF(arg_32_0._gameTf, "specialPower")
		arg_32_0._successPower = findTF(arg_32_0._gameTf, "successPower")
		arg_32_0._top = findTF(arg_32_0._gameTf, "top")

		for iter_32_0 = 1, #var_31_1:
			local var_32_0 = var_31_1[iter_32_0]
			local var_32_1 = findTF(arg_32_0._sceneTf, var_31_1[iter_32_0].source)
			local var_32_2 = var_31_1[iter_32_0].rate

			table.insert(arg_32_0.bgs, {
				tf = var_32_1,
				rate = var_32_2
			})

		arg_32_0._bgBackCanvas = GetComponent(findTF(arg_32_0._sceneTf, "scene_background"), typeof(CanvasGroup))
		arg_32_0._bgFrontCanvas = GetComponent(findTF(arg_32_0._sceneTf, "scene_front"), typeof(CanvasGroup))
		arg_32_0._bgBeamCanvas = GetComponent(findTF(arg_32_0._sceneTf, "scene/bgBeam"), typeof(CanvasGroup))

		arg_32_0._event.bind(var_0_14, function(arg_33_0, arg_33_1, arg_33_2)
			local var_33_0 = arg_33_1[1]
			local var_33_1 = arg_33_1[2] and -1 or 1
			local var_33_2 = arg_33_1[3]

			if not arg_32_0.inCamera:
				arg_32_0.setTargetFllow(Vector2(var_33_1 * var_33_0.x / 10, var_33_1 * var_33_0.y / 10), var_33_2))
		arg_32_0._event.bind(var_0_18, function(arg_34_0, arg_34_1, arg_34_2)
			arg_32_0.inCamera = True

			arg_32_0.setTargetFllow(Vector2(550, 100))
			arg_32_0.setBeam(False))
		arg_32_0._event.bind(var_0_19, function(arg_35_0, arg_35_1, arg_35_2)
			arg_32_0.setTargetFllow(Vector2(0, 0), function()
				return, True)
			arg_32_0.setBeam(True)

			arg_32_0.inCamera = False)

	function var_31_0.start(arg_37_0)
		arg_37_0.targetVec = Vector2(var_0_36.x, var_0_36.y)
		arg_37_0.currentVec = Vector2(var_0_36.x, var_0_36.y)

		for iter_37_0 = 1, #arg_37_0.bgs:
			local var_37_0 = arg_37_0.bgs[iter_37_0].tf
			local var_37_1 = arg_37_0.bgs[iter_37_0].rate

			var_37_0.anchoredPosition = Vector2(arg_37_0.currentVec.x * var_37_1, arg_37_0.currentVec.y * var_37_1)

		arg_37_0._bgBackCanvas.alpha = 1
		arg_37_0._bgFrontCanvas.alpha = 1
		arg_37_0._bgBeamCanvas.alpha = 0

		setActive(arg_37_0._box, True)
		setActive(arg_37_0._specialPower, True)
		setActive(arg_37_0._successPower, True)
		setActive(arg_37_0._top, True)

	function var_31_0.clear(arg_38_0)
		if LeanTween.isTweening(go(arg_38_0._sceneTf)):
			LeanTween.cancel(go(arg_38_0._sceneTf), False)

	function var_31_0.step(arg_39_0)
		local var_39_0 = 0
		local var_39_1 = 0

		if arg_39_0.targetVec.x != arg_39_0.currentVec.x:
			var_39_0 = (arg_39_0.targetVec.x - arg_39_0.currentVec.x) * var_0_37

			if math.abs(var_39_0) < var_0_38:
				var_39_0 = var_0_38 * math.sign(var_39_0)

			arg_39_0.currentVec.x = arg_39_0.currentVec.x + var_39_0

			if math.abs(arg_39_0.currentVec.x - arg_39_0.targetVec.x) <= var_0_38:
				arg_39_0.currentVec.x = arg_39_0.targetVec.x

		if arg_39_0.targetVec.y != arg_39_0.currentVec.y:
			var_39_1 = (arg_39_0.targetVec.y - arg_39_0.currentVec.y) * var_0_37

			if math.abs(var_39_1) < var_0_38:
				var_39_1 = var_0_38 * math.sign(var_39_1)

			arg_39_0.currentVec.y = arg_39_0.currentVec.y + var_39_1

			if math.abs(arg_39_0.currentVec.y - arg_39_0.targetVec.y) <= var_0_38:
				arg_39_0.currentVec.y = arg_39_0.targetVec.y

		if var_39_0 != 0 or var_39_1 != 0:
			arg_39_0.moveTo(arg_39_0.currentVec)

	function var_31_0.moveTo(arg_40_0, arg_40_1)
		for iter_40_0 = 1, #arg_40_0.bgs:
			local var_40_0 = arg_40_0.bgs[iter_40_0].tf
			local var_40_1 = arg_40_0.bgs[iter_40_0].rate

			var_40_0.anchoredPosition = Vector2(arg_40_1.x * var_40_1, arg_40_1.y * var_40_1)

	function var_31_0.setTargetFllow(arg_41_0, arg_41_1, arg_41_2, arg_41_3)
		if not arg_41_3:
			arg_41_0.targetVec = arg_41_1
			arg_41_0.moveCallback = arg_41_2
		else
			arg_41_0.currentVec = arg_41_1
			arg_41_0.targetVec = arg_41_1

			arg_41_0.moveTo(arg_41_1)

			if arg_41_2:
				arg_41_2()

	function var_31_0.setBeam(arg_42_0, arg_42_1, arg_42_2)
		if LeanTween.isTweening(go(arg_42_0._sceneTf)):
			LeanTween.cancel(go(arg_42_0._sceneTf), False)

		if arg_42_1:
			setActive(arg_42_0._box, True)
			setActive(arg_42_0._specialPower, True)
			setActive(arg_42_0._successPower, True)
			setActive(arg_42_0._top, True)
		else
			setActive(arg_42_0._box, False)
			setActive(arg_42_0._specialPower, False)
			setActive(arg_42_0._successPower, False)
			setActive(arg_42_0._top, False)

		LeanTween.value(go(arg_42_0._sceneTf), 0, 1, 0.2).setOnUpdate(System.Action_float(function(arg_43_0)
			if arg_42_1:
				arg_42_0._bgBackCanvas.alpha = arg_43_0
				arg_42_0._bgFrontCanvas.alpha = arg_43_0
				arg_42_0._bgBeamCanvas.alpha = 1 - arg_43_0
			else
				arg_42_0._bgBackCanvas.alpha = 1 - arg_43_0
				arg_42_0._bgFrontCanvas.alpha = 1 - arg_43_0
				arg_42_0._bgBeamCanvas.alpha = arg_43_0)).setOnComplete(System.Action(function()
			if arg_42_2:
				arg_42_2()))

	var_31_0.ctor()

	return var_31_0

local function var_0_58(arg_45_0, arg_45_1)
	local var_45_0 = {
		def ctor:(arg_46_0)
			arg_46_0._scene = arg_45_0
			arg_46_0._tpl = findTF(arg_46_0._scene, "tpl")
			arg_46_0._leftRolePos = findTF(arg_46_0._scene, "rolePos/leftRole")
			arg_46_0._rightRolePos = findTF(arg_46_0._scene, "rolePos/rightRole")
			arg_46_0._event = arg_45_1

			arg_46_0._event.bind(var_0_13, function()
				arg_46_0.onGridTrigger())
			arg_46_0._event.bind(var_0_16, function()
				arg_46_0.onRoleSpecial())
			arg_46_0._event.bind(var_0_17, function()
				arg_46_0.onRoleSpecialEnd()),
		def start:(arg_50_0)
			if arg_50_0.leftRole:
				destroy(arg_50_0.leftRole.tf)

				arg_50_0.leftRole = None

			if arg_50_0.rightRole:
				destroy(arg_50_0.rightRole.tf)

				arg_50_0.rightRole = None

			arg_50_0.leftRole = arg_50_0.createRole(var_0_31, True, arg_50_0._leftRolePos)
			arg_50_0.rightRole = arg_50_0.createRole(var_0_32, False, arg_50_0._rightRolePos)
			arg_50_0.leftRole.targetRole = arg_50_0.rightRole
			arg_50_0.rightRole.targetRole = arg_50_0.leftRole

			arg_50_0.leftRole.animator.SetTrigger("idle")
			arg_50_0.leftRole.animator.SetBool("special", False)
			arg_50_0.rightRole.animator.SetTrigger("idle")
			arg_50_0.rightRole.animator.SetBool("special", False)

			arg_50_0.leftRole.specialBody = False
			arg_50_0.rightRole.specialBody = False
			arg_50_0.leftRole.anchoredPosition = Vector2(0, 0)
			arg_50_0.rightRole.anchoredPosition = Vector2(0, 0)
			arg_50_0.leftRole.specialTime = False
			arg_50_0.rightRole.specialTime = False
			arg_50_0.playingDatas = {}
			arg_50_0.playingDatas[arg_50_0.leftRole.name] = {
				role = arg_50_0.leftRole
			}
			arg_50_0.playingDatas[arg_50_0.leftRole.name].skillDatas = {}
			arg_50_0.playingDatas[arg_50_0.rightRole.name] = {
				role = arg_50_0.rightRole
			}
			arg_50_0.playingDatas[arg_50_0.rightRole.name].skillDatas = {}
			arg_50_0.skillDeltaTime = 0
			arg_50_0.emptySkillTime = math.random(1, 2)
			arg_50_0.addScore = {
				0,
				0
			}

			arg_50_0._event.emit(var_0_14, {
				Vector2(0, 0),
				False
			}),
		def step:(arg_51_0)
			arg_51_0.checkSkillDeltaTime()
			arg_51_0.checkEmptySkillTime(),
		def checkSkillDeltaTime:(arg_52_0)
			if arg_52_0.skillDeltaTime and arg_52_0.skillDeltaTime <= 0:
				arg_52_0.skillDeltaTime = var_0_39

			arg_52_0.skillDeltaTime = arg_52_0.skillDeltaTime - Time.deltaTime

			if arg_52_0.skillDeltaTime <= 0:
				local var_52_0 = False

				for iter_52_0, iter_52_1 in pairs(arg_52_0.playingDatas):
					if iter_52_1.inPlaying:
						var_52_0 = True

				if not var_52_0:
					for iter_52_2, iter_52_3 in pairs(arg_52_0.playingDatas):
						if #iter_52_3.skillDatas > 0:
							if iter_52_3.role == arg_52_0.leftRole:
								print("开始执行角色攻击")

							arg_52_0.applySkillData(iter_52_3)

							break

			var_0_55 = False

			for iter_52_4, iter_52_5 in pairs(arg_52_0.playingDatas):
				if iter_52_5.inPlaying:
					var_0_55 = True,
		def checkEmptySkillTime:(arg_53_0)
			if arg_53_0.emptySkillTime and arg_53_0.emptySkillTime <= 0:
				arg_53_0.emptySkillTime = var_0_40

			arg_53_0.emptySkillTime = arg_53_0.emptySkillTime - Time.deltaTime

			if arg_53_0.emptySkillTime <= 0:
				local var_53_0 = False

				for iter_53_0, iter_53_1 in pairs(arg_53_0.playingDatas):
					if iter_53_1.inPlaying:
						var_53_0 = True

				if not var_53_0:
					local var_53_1 = arg_53_0.getRoleEmptySkill(arg_53_0.rightRole)

					if var_53_1:
						arg_53_0.addRolePlaying(arg_53_0.rightRole, var_53_1),
		def getRoleEmptySkill:(arg_54_0, arg_54_1)
			local var_54_0 = {}

			for iter_54_0 = 1, #arg_54_1.skill:
				local var_54_1 = arg_54_1.skill[iter_54_0]

				if tobool(var_54_1.special_time) == arg_54_1.specialBody and var_54_1.atk_index:
					table.insert(var_54_0, var_54_1)

			if #var_54_0 > 0:
				return Clone(var_54_0[math.random(1, #var_54_0)])

			return None,
		def onRoleSpecial:(arg_55_0)
			arg_55_0.leftRole.specialTime = True

			for iter_55_0 = 1, #arg_55_0.leftRole.skill:
				local var_55_0 = arg_55_0.leftRole.skill[iter_55_0]

				if var_55_0.special_trigger:
					arg_55_0.addRolePlaying(arg_55_0.leftRole, Clone(var_55_0)),
		def onRoleSpecialEnd:(arg_56_0)
			arg_56_0.leftRole.specialTime = False

			for iter_56_0 = 1, #arg_56_0.leftRole.skill:
				local var_56_0 = arg_56_0.leftRole.skill[iter_56_0]

				if not var_56_0.special_trigger and var_56_0.special_end:
					arg_56_0.addRolePlaying(arg_56_0.leftRole, Clone(var_56_0)),
		def clear:(arg_57_0)
			if LeanTween.isTweening(go(arg_57_0._leftRolePos)):
				LeanTween.cancel(go(arg_57_0._leftRolePos))

			if LeanTween.isTweening(go(arg_57_0._rightRolePos)):
				LeanTween.cancel(go(arg_57_0._rightRolePos))

			if LeanTween.isTweening(go(arg_57_0.rightRole.tf)):
				LeanTween.cancel(go(arg_57_0.rightRole.tf))

			if LeanTween.isTweening(go(arg_57_0.leftRole.tf)):
				LeanTween.cancel(go(arg_57_0.leftRole.tf)),
		def onGridTrigger:(arg_58_0)
			local var_58_0 = var_0_21.grid_index
			local var_58_1 = var_0_21.power_grid
			local var_58_2 = var_0_21.special_time

			for iter_58_0 = 1, #arg_58_0.leftRole.skill:
				local var_58_3 = arg_58_0.leftRole.skill[iter_58_0]

				if tobool(var_58_3.special_time) == tobool(arg_58_0.leftRole.specialTime) and var_58_3.power_index == var_58_1 and table.contains(var_58_3.grid_index, var_58_0) and var_58_3.atk_index:
					arg_58_0.addRolePlaying(arg_58_0.leftRole, Clone(var_58_3)),
		def createRole:(arg_59_0, arg_59_1, arg_59_2, arg_59_3)
			local var_59_0 = arg_59_0.getRoleData(arg_59_1)

			if not var_59_0:
				return None

			local var_59_1 = {}
			local var_59_2 = tf(instantiate(findTF(arg_59_0._tpl, var_59_0.name)))

			SetParent(var_59_2, arg_59_3)

			var_59_2.anchoredPosition = Vector2(0, 0)
			var_59_2.localScale = Vector3(1, 1, 1)

			setActive(var_59_2, True)

			local var_59_3 = findTF(var_59_2, "body")
			local var_59_4 = findTF(var_59_3, "anim")
			local var_59_5 = GetComponent(var_59_4, typeof(Animator))
			local var_59_6 = GetComponent(var_59_4, typeof(DftAniEvent))

			var_59_6.SetStartEvent(function()
				if var_59_1.startCallback:
					var_59_1.startCallback())
			var_59_6.SetTriggerEvent(function()
				if var_59_1.triggerCallback:
					var_59_1.triggerCallback())
			var_59_6.SetEndEvent(function()
				if var_59_1.endCallback:
					var_59_1.endCallback())

			var_59_1.name = var_59_0.name
			var_59_1.tf = var_59_2
			var_59_1.canvasGroup = GetComponent(var_59_2, typeof(CanvasGroup))
			var_59_1.body = var_59_3
			var_59_1.animTf = var_59_4
			var_59_1.animator = var_59_5
			var_59_1.dftEvent = var_59_6
			var_59_1.startCallback = None
			var_59_1.triggerCallback = None
			var_59_1.endCallback = None
			var_59_1.skill = var_59_0.skill
			var_59_1.name = var_59_0.name
			var_59_1.index = var_59_0.index
			var_59_1.actions = var_59_0.actions

			return var_59_1,
		def getRoleData:(arg_63_0, arg_63_1)
			for iter_63_0 = 1, #var_0_53:
				if var_0_53[iter_63_0].index == arg_63_1:
					return Clone(var_0_53[iter_63_0])

			return None,
		def setDftHandle:(arg_64_0, arg_64_1, arg_64_2, arg_64_3, arg_64_4)
			arg_64_1.startCallback = arg_64_2
			arg_64_1.triggerCallback = arg_64_3
			arg_64_1.endCallback = arg_64_4,
		def playAnimation:(arg_65_0, arg_65_1, arg_65_2)
			print(arg_65_1.name .. " 执行动画 ：" .. arg_65_2 .. "  active." .. tostring(arg_65_1.animator.isActiveAndEnabled) .. tostring(Time.GetTimestamp()))
			arg_65_1.animator.Play("emptyAnimation", -1, 0)
			arg_65_1.animator.Play(arg_65_2, -1, 0),
		def addRolePlaying:(arg_66_0, arg_66_1, arg_66_2, arg_66_3)
			for iter_66_0, iter_66_1 in pairs(arg_66_0.playingDatas):
				if iter_66_0 == arg_66_1.name:
					if arg_66_3:
						arg_66_0.applySkillData(iter_66_1, arg_66_2)
					else
						table.insert(iter_66_1.skillDatas, arg_66_2)

						if arg_66_2.power_index > 0 and arg_66_2.atk_index > 1 or arg_66_2.special_trigger:
							for iter_66_2 = #iter_66_1.skillDatas - 1, 1, -1:
								local var_66_0 = iter_66_1.skillDatas[iter_66_2]

								if var_66_0.power_index == 0 and var_66_0.atk_index == 1:
									local var_66_1 = table.remove(iter_66_1.skillDatas, iter_66_2)

									if var_66_1.score:
										arg_66_0.addScore = {
											arg_66_0.addScore[1] + var_66_1.score[1],
											arg_66_0.addScore[2] + var_66_1.score[2]
										},
		def applySkillData:(arg_67_0, arg_67_1, arg_67_2)
			arg_67_1.inPlaying = True

			local var_67_0 = arg_67_1.role
			local var_67_1 = arg_67_2 or table.remove(arg_67_1.skillDatas, 1)

			arg_67_1.currentSkill = var_67_1
			arg_67_1.actions = var_67_1.actions

			local var_67_2 = var_67_1.anim_bool

			if var_67_2:
				var_67_0.animator.SetBool(var_67_2, True)

			if var_67_0 == arg_67_0.leftRole and not var_67_1.dmg_index:
				arg_67_0._leftRolePos.SetSiblingIndex(1)
			elif var_67_0 == arg_67_0.rightRole and not var_67_1.dmg_index:
				arg_67_0._rightRolePos.SetSiblingIndex(1)

			if var_67_1.special_end:
				arg_67_1.role.specialBody = False
			elif var_67_1.special_trigger:
				arg_67_1.role.specialBody = True

			arg_67_1.actionIndex = 1

			arg_67_0.checkAction(arg_67_1, function()
				arg_67_1.inPlaying = False

				print(arg_67_1.role.name .. "动画播放完毕")),
		def checkAction:(arg_69_0, arg_69_1, arg_69_2)
			if arg_69_1.actions and arg_69_1.actionIndex <= #arg_69_1.actions:
				print("准备执行" .. arg_69_1.actions[arg_69_1.actionIndex].anim_name .. "上一个动作." .. tostring(arg_69_1.playingAction and arg_69_1.playingAction.anim_name))

				arg_69_1.playingAction = arg_69_1.actions[arg_69_1.actionIndex]
				arg_69_1.actionIndex = arg_69_1.actionIndex + 1

				local var_69_0 = arg_69_1.playingAction.anim_name
				local var_69_1 = arg_69_1.playingAction.time
				local var_69_2 = arg_69_1.playingAction.move
				local var_69_3 = arg_69_1.playingAction.over_offset
				local var_69_4 = arg_69_1.playingAction.camera
				local var_69_5 = arg_69_1.playingAction.sound_start
				local var_69_6 = arg_69_1.playingAction.sound_trigger
				local var_69_7 = arg_69_1.playingAction.sound_end
				local var_69_8 = arg_69_1.currentSkill.special_trigger
				local var_69_9 = arg_69_1.currentSkill.special_time
				local var_69_10 = arg_69_1.currentSkill.atk_index

				if var_69_8 or var_69_9 and var_69_10 and var_69_10 >= 2:
					arg_69_0._event.emit(var_0_20, True)

				if var_69_1 and var_69_1 > 0:
					-- block empty
				else
					local function var_69_11()
						if var_69_5:
							pg.CriMgr.GetInstance().PlaySoundEffect_V3("event./ui/" .. var_69_5)

						if var_69_2:
							arg_69_0.moveRole(arg_69_1.role, var_69_2)

						if var_69_4:
							arg_69_1.role.targetRole.canvasGroup.alpha = 0

							arg_69_0._event.emit(var_0_18)

					local function var_69_12()
						if var_69_6:
							pg.CriMgr.GetInstance().PlaySoundEffect_V3("event./ui/" .. var_69_6)

						if var_69_4:
							var_69_4 = False
							arg_69_1.role.targetRole.canvasGroup.alpha = 1

							arg_69_0._event.emit(var_0_19)
						else
							local var_71_0 = arg_69_1.currentSkill.atk_index

							if var_71_0:
								local var_71_1 = arg_69_0.getRoleDmgData(arg_69_1.role.targetRole, var_71_0)

								if var_71_1:
									arg_69_0.addRolePlaying(arg_69_1.role.targetRole, Clone(var_71_1), True)

								local var_71_2 = arg_69_1.currentSkill.score

								if var_71_2 and arg_69_1.role == arg_69_0.leftRole:
									arg_69_0._event.emit(var_0_15, math.random(var_71_2[1] + arg_69_0.addScore[1], var_71_2[2] + arg_69_0.addScore[2]))

									arg_69_0.addScore = {
										0,
										0
									}

					local function var_69_13()
						if var_69_7:
							pg.CriMgr.GetInstance().PlaySoundEffect_V3("event./ui/" .. var_69_7)

						if LeanTween.isTweening(go(arg_69_1.role.tf)):
							LeanTween.cancel(go(arg_69_1.role.tf))

						arg_69_0._event.emit(var_0_20, False)

						if var_69_3:
							arg_69_1.role.tf.anchoredPosition = Vector2(arg_69_1.role.tf.anchoredPosition.x + var_69_3.x, arg_69_1.role.tf.anchoredPosition.y + var_69_3.y)

						if arg_69_1.currentSkill.special_trigger and var_0_21.special_time and not var_0_21.special_complete:
							var_0_21.special_complete = True

						arg_69_1.playingAction = None

						arg_69_0.setDftHandle(arg_69_1.role, None, None, None)
						print(arg_69_1.role.name .. "执行 " .. var_69_0 .. "结束")
						arg_69_0.checkAction(arg_69_1, arg_69_2)

					arg_69_0.setDftHandle(arg_69_1.role, var_69_11, var_69_12, var_69_13)
					arg_69_0.playAnimation(arg_69_1.role, var_69_0)
			else
				if arg_69_1.role == arg_69_0.leftRole:
					print(arg_69_1.role.name .. "队列结束")

				if arg_69_2:
					arg_69_2(),
		def moveRole:(arg_73_0, arg_73_1, arg_73_2)
			if LeanTween.isTweening(go(arg_73_1.tf)):
				LeanTween.cancel(go(arg_73_1.tf))

			arg_73_0._event.emit(var_0_14, {
				arg_73_2.distance,
				arg_73_1 == arg_73_0.leftRole
			})
			LeanTween.move(arg_73_1.tf, Vector3(arg_73_2.distance.x, arg_73_2.distance.y, 0), arg_73_2.time).setEase(arg_73_2.ease or LeanTweenType.linear),
		def getRoleDmgData:(arg_74_0, arg_74_1, arg_74_2)
			local var_74_0 = arg_74_1.skill

			for iter_74_0 = 1, #var_74_0:
				local var_74_1 = var_74_0[iter_74_0]

				if var_74_1.dmg_index == arg_74_2 and var_74_1.special_time == tobool(arg_74_1.specialBody):
					return var_74_1

			return None
	}

	var_45_0.ctor()

	return var_45_0

def var_0_0.getUIName(arg_75_0):
	return "GridGameUI"

def var_0_0.didEnter(arg_76_0):
	arg_76_0.initEvent()
	arg_76_0.initData()
	arg_76_0.initUI()
	arg_76_0.initGameUI()
	arg_76_0.initController()
	arg_76_0.updateMenuUI()
	arg_76_0.openMenuUI()

def var_0_0.initEvent(arg_77_0):
	arg_77_0.bind(var_0_15, function(arg_78_0, arg_78_1, arg_78_2)
		arg_77_0.addScore(arg_78_1))
	arg_77_0.bind(var_0_20, function(arg_79_0, arg_79_1, arg_79_2)
		arg_77_0.ignoreTime = arg_79_1)

def var_0_0.onEventHandle(arg_80_0, arg_80_1):
	return

def var_0_0.initData(arg_81_0):
	local var_81_0 = Application.targetFrameRate or 60

	if var_81_0 > 60:
		var_81_0 = 60

	arg_81_0.timer = Timer.New(function()
		arg_81_0.onTimer(), 1 / var_81_0, -1)

def var_0_0.initUI(arg_83_0):
	arg_83_0.backSceneTf = findTF(arg_83_0._tf, "scene_background")
	arg_83_0.sceneTf = findTF(arg_83_0._tf, "scene")
	arg_83_0.clickMask = findTF(arg_83_0._tf, "clickMask")

	setText(findTF(arg_83_0._tf, "ui/gameUI/top/time"), i18n("mini_game_time"))
	setText(findTF(arg_83_0._tf, "ui/gameUI/top/scoreDesc"), i18n("mini_game_score"))
	setText(findTF(arg_83_0._tf, "pop/LeaveUI/ad/desc"), i18n("mini_game_leave"))
	setText(findTF(arg_83_0._tf, "pop/pauseUI/ad/desc"), i18n("mini_game_pause"))
	setText(findTF(arg_83_0._tf, "pop/SettleMentUI/ad/currentTextDesc"), i18n("mini_game_cur_score"))
	setText(findTF(arg_83_0._tf, "pop/SettleMentUI/ad/highTextDesc"), i18n("mini_game_high_score"))

	arg_83_0.countUI = findTF(arg_83_0._tf, "pop/CountUI")
	arg_83_0.countAnimator = GetComponent(findTF(arg_83_0.countUI, "count"), typeof(Animator))
	arg_83_0.countDft = GetOrAddComponent(findTF(arg_83_0.countUI, "count"), typeof(DftAniEvent))

	arg_83_0.countDft.SetTriggerEvent(function()
		return)
	arg_83_0.countDft.SetEndEvent(function()
		setActive(arg_83_0.countUI, False)
		arg_83_0.gameStart())

	arg_83_0.leaveUI = findTF(arg_83_0._tf, "pop/LeaveUI")

	onButton(arg_83_0, findTF(arg_83_0.leaveUI, "ad/btnOk"), function()
		arg_83_0.resumeGame()
		arg_83_0.onGameOver(), SFX_CANCEL)
	onButton(arg_83_0, findTF(arg_83_0.leaveUI, "ad/btnCancel"), function()
		arg_83_0.resumeGame(), SFX_CANCEL)

	arg_83_0.pauseUI = findTF(arg_83_0._tf, "pop/pauseUI")

	onButton(arg_83_0, findTF(arg_83_0.pauseUI, "ad/btnOk"), function()
		setActive(arg_83_0.pauseUI, False)
		arg_83_0.resumeGame(), SFX_CANCEL)

	arg_83_0.settlementUI = findTF(arg_83_0._tf, "pop/SettleMentUI")

	onButton(arg_83_0, findTF(arg_83_0.settlementUI, "ad/btnOver"), function()
		setActive(arg_83_0.settlementUI, False)
		arg_83_0.openMenuUI(), SFX_CANCEL)

	arg_83_0.selectedUI = findTF(arg_83_0._tf, "pop/selectedUI")
	arg_83_0.leftSelectRole = {}

	for iter_83_0 = 1, #var_0_33:
		local var_83_0 = findTF(arg_83_0.selectedUI, "ad/leftRole/role" .. var_0_33[iter_83_0])
		local var_83_1 = var_0_33[iter_83_0]

		onButton(arg_83_0, var_83_0, function()
			if var_0_32 == var_83_1:
				var_0_32 = var_0_31

			var_0_31 = var_83_1

			arg_83_0.updateSelectedUI(), SFX_CONFIRM)
		table.insert(arg_83_0.leftSelectRole, {
			id = var_83_1,
			tf = var_83_0
		})

	onButton(arg_83_0, findTF(arg_83_0.selectedUI, "close"), function()
		setActive(arg_83_0.selectedUI, False), SFX_CANCEL)

	arg_83_0.rightSelectRole = {}

	for iter_83_1 = 1, #var_0_34:
		local var_83_2 = findTF(arg_83_0.selectedUI, "ad/rightRole/role" .. var_0_34[iter_83_1])
		local var_83_3 = var_0_34[iter_83_1]

		onButton(arg_83_0, var_83_2, function()
			if var_0_31 == var_83_3:
				var_0_31 = var_0_32

				if not table.contains(var_0_33, var_0_31):
					for iter_92_0, iter_92_1 in ipairs(var_0_33):
						if iter_92_1 != var_83_3:
							var_0_31 = iter_92_1

			var_0_32 = var_83_3

			arg_83_0.updateSelectedUI(), SFX_CONFIRM)
		table.insert(arg_83_0.rightSelectRole, {
			id = var_83_3,
			tf = var_83_2
		})

	onButton(arg_83_0, findTF(arg_83_0.selectedUI, "ad/btnOk"), function()
		setActive(arg_83_0.selectedUI, False)
		setActive(arg_83_0.menuUI, False)
		arg_83_0.readyStart(), SFX_CONFIRM)
	setActive(arg_83_0.selectedUI, False)

	arg_83_0.menuUI = findTF(arg_83_0._tf, "pop/menuUI")
	arg_83_0.battleScrollRect = GetComponent(findTF(arg_83_0.menuUI, "battList"), typeof(ScrollRect))
	arg_83_0.totalTimes = arg_83_0.getGameTotalTime()

	local var_83_4 = arg_83_0.getGameUsedTimes() - 4 < 0 and 0 or arg_83_0.getGameUsedTimes() - 4

	scrollTo(arg_83_0.battleScrollRect, 0, 1 - var_83_4 / (arg_83_0.totalTimes - 4))
	onButton(arg_83_0, findTF(arg_83_0.menuUI, "rightPanelBg/arrowUp"), function()
		local var_94_0 = arg_83_0.battleScrollRect.normalizedPosition.y + 1 / (arg_83_0.totalTimes - 4)

		if var_94_0 > 1:
			var_94_0 = 1

		scrollTo(arg_83_0.battleScrollRect, 0, var_94_0), SFX_CANCEL)
	onButton(arg_83_0, findTF(arg_83_0.menuUI, "rightPanelBg/arrowDown"), function()
		local var_95_0 = arg_83_0.battleScrollRect.normalizedPosition.y - 1 / (arg_83_0.totalTimes - 4)

		if var_95_0 < 0:
			var_95_0 = 0

		scrollTo(arg_83_0.battleScrollRect, 0, var_95_0), SFX_CANCEL)
	onButton(arg_83_0, findTF(arg_83_0.menuUI, "btnBack"), function()
		arg_83_0.closeView(), SFX_CANCEL)
	onButton(arg_83_0, findTF(arg_83_0.menuUI, "btnRule"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.ssss_game_tip.tip
		}), SFX_CONFIRM)
	onButton(arg_83_0, findTF(arg_83_0.menuUI, "btnStart"), function()
		local var_98_0 = arg_83_0.getGameUsedTimes() or 0
		local var_98_1 = arg_83_0.getGameTimes() or 0

		if var_98_0 >= #var_0_35 and arg_83_0.selectedUI:
			arg_83_0.updateSelectedUI()
			setActive(arg_83_0.selectedUI, True)
		else
			local var_98_2
			local var_98_3 = var_98_0 == 0 and 1 or var_98_1 > 0 and var_98_0 + 1 or var_98_0

			if var_98_3 > #var_0_35:
				var_98_3 = #var_0_35

			local var_98_4 = var_0_35[var_98_3]

			var_0_31 = var_98_4[1]
			var_0_32 = var_98_4[2]

			setActive(arg_83_0.menuUI, False)
			arg_83_0.readyStart(), SFX_CONFIRM)

	local var_83_5 = findTF(arg_83_0.menuUI, "tplBattleItem")

	arg_83_0.battleItems = {}
	arg_83_0.dropItems = {}

	for iter_83_2 = 1, 7:
		local var_83_6 = tf(instantiate(var_83_5))

		var_83_6.name = "battleItem_" .. iter_83_2

		setParent(var_83_6, findTF(arg_83_0.menuUI, "battList/Viewport/Content"))

		local var_83_7 = iter_83_2

		GetSpriteFromAtlasAsync("ui/gridgameui_atlas", "battleDesc" .. var_83_7, function(arg_99_0)
			setImageSprite(findTF(var_83_6, "state_open/buttomDesc"), arg_99_0, True)
			setImageSprite(findTF(var_83_6, "state_clear/buttomDesc"), arg_99_0, True)
			setImageSprite(findTF(var_83_6, "state_current/buttomDesc"), arg_99_0, True)
			setImageSprite(findTF(var_83_6, "state_closed/buttomDesc"), arg_99_0, True))
		setActive(var_83_6, True)
		table.insert(arg_83_0.battleItems, var_83_6)

	if not arg_83_0.handle:
		arg_83_0.handle = UpdateBeat.CreateListener(arg_83_0.Update, arg_83_0)

	UpdateBeat.AddListener(arg_83_0.handle)

def var_0_0.initGameUI(arg_100_0):
	arg_100_0.gameUI = findTF(arg_100_0._tf, "ui/gameUI")

	onButton(arg_100_0, findTF(arg_100_0.gameUI, "topRight/btnStop"), function()
		arg_100_0.stopGame()
		setActive(arg_100_0.pauseUI, True))
	onButton(arg_100_0, findTF(arg_100_0.gameUI, "btnLeave"), function()
		arg_100_0.stopGame()
		setActive(arg_100_0.leaveUI, True))

	arg_100_0.gameTimeS = findTF(arg_100_0.gameUI, "top/time/s")
	arg_100_0.scoreTf = findTF(arg_100_0.gameUI, "top/score")
	arg_100_0.scoreAnimTf = findTF(arg_100_0._tf, "sceneContainer/scene_front/scoreAnim")
	arg_100_0.scoreAnimTextTf = findTF(arg_100_0._tf, "sceneContainer/scene_front/scoreAnim/text")

	setActive(arg_100_0.scoreAnimTf, False)

def var_0_0.initController(arg_103_0):
	local var_103_0 = findTF(arg_103_0.gameUI, "box")

	arg_103_0.boxController = var_0_54(var_103_0, arg_103_0)

	local var_103_1 = findTF(arg_103_0.gameUI, "specialPower")
	local var_103_2 = findTF(arg_103_0.gameUI, "successPower")

	arg_103_0.specialController = var_0_56(var_103_1, var_103_2, arg_103_0)

	local var_103_3 = findTF(arg_103_0._tf, "sceneContainer")

	arg_103_0.bgController = var_0_57(var_103_3, arg_103_0.gameUI, arg_103_0)

	local var_103_4 = findTF(arg_103_0._tf, "sceneContainer/scene")

	arg_103_0.roleController = var_0_58(var_103_4, arg_103_0)

def var_0_0.Update(arg_104_0):
	arg_104_0.AddDebugInput()

def var_0_0.AddDebugInput(arg_105_0):
	if arg_105_0.gameStop or arg_105_0.settlementFlag:
		return

	if IsUnityEditor:
		-- block empty

def var_0_0.updateSelectedUI(arg_106_0):
	for iter_106_0 = 1, #arg_106_0.leftSelectRole:
		local var_106_0 = arg_106_0.leftSelectRole[iter_106_0]

		if var_0_31 == var_106_0.id:
			setActive(findTF(var_106_0.tf, "selected"), True)
			setActive(findTF(var_106_0.tf, "unSelected"), False)
		else
			setActive(findTF(var_106_0.tf, "selected"), False)
			setActive(findTF(var_106_0.tf, "unSelected"), True)

	for iter_106_1 = 1, #arg_106_0.rightSelectRole:
		local var_106_1 = arg_106_0.rightSelectRole[iter_106_1]

		if var_0_32 == var_106_1.id:
			setActive(findTF(var_106_1.tf, "selected"), True)
			setActive(findTF(var_106_1.tf, "unSelected"), False)
		else
			setActive(findTF(var_106_1.tf, "selected"), False)
			setActive(findTF(var_106_1.tf, "unSelected"), True)

def var_0_0.updateMenuUI(arg_107_0):
	local var_107_0 = arg_107_0.getGameUsedTimes()

	if var_107_0 and var_107_0 >= 7:
		setActive(findTF(arg_107_0.menuUI, "btnStart/free"), True)
	else
		setActive(findTF(arg_107_0.menuUI, "btnStart/free"), False)

	local var_107_1 = arg_107_0.getGameTimes()

	for iter_107_0 = 1, #arg_107_0.battleItems:
		setActive(findTF(arg_107_0.battleItems[iter_107_0], "state_open"), False)
		setActive(findTF(arg_107_0.battleItems[iter_107_0], "state_closed"), False)
		setActive(findTF(arg_107_0.battleItems[iter_107_0], "state_clear"), False)
		setActive(findTF(arg_107_0.battleItems[iter_107_0], "state_current"), False)

		if iter_107_0 <= var_107_0:
			setActive(findTF(arg_107_0.battleItems[iter_107_0], "state_clear"), True)
		elif iter_107_0 == var_107_0 + 1 and var_107_1 >= 1:
			setActive(findTF(arg_107_0.battleItems[iter_107_0], "state_current"), True)
		elif var_107_0 < iter_107_0 and iter_107_0 <= var_107_0 + var_107_1:
			setActive(findTF(arg_107_0.battleItems[iter_107_0], "state_open"), True)
		else
			setActive(findTF(arg_107_0.battleItems[iter_107_0], "state_closed"), True)

	arg_107_0.totalTimes = arg_107_0.getGameTotalTime()

	local var_107_2 = 1 - (arg_107_0.getGameUsedTimes() - 3 < 0 and 0 or arg_107_0.getGameUsedTimes() - 3) / (arg_107_0.totalTimes - 4)

	if var_107_2 > 1:
		var_107_2 = 1

	scrollTo(arg_107_0.battleScrollRect, 0, var_107_2)
	setActive(findTF(arg_107_0.menuUI, "btnStart/tip"), var_107_1 > 0)
	arg_107_0.CheckGet()

def var_0_0.CheckGet(arg_108_0):
	setActive(findTF(arg_108_0.menuUI, "got"), False)

	if arg_108_0.getUltimate() and arg_108_0.getUltimate() != 0:
		setActive(findTF(arg_108_0.menuUI, "got"), True)

	if arg_108_0.getUltimate() == 0:
		if arg_108_0.getGameTotalTime() > arg_108_0.getGameUsedTimes():
			return

		pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = arg_108_0.GetMGHubData().id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})
		setActive(findTF(arg_108_0.menuUI, "got"), True)

def var_0_0.openMenuUI(arg_109_0):
	setActive(findTF(arg_109_0._tf, "sceneContainer/scene_front"), False)
	setActive(findTF(arg_109_0._tf, "sceneContainer/scene_background"), False)
	setActive(findTF(arg_109_0._tf, "sceneContainer/scene"), False)
	setActive(arg_109_0.gameUI, False)
	setActive(arg_109_0.menuUI, True)
	setActive(arg_109_0.selectedUI, False)
	arg_109_0.updateMenuUI()

	local var_109_0 = arg_109_0.getBGM()

	if not var_109_0:
		if pg.CriMgr.GetInstance().IsDefaultBGM():
			var_109_0 = pg.voice_bgm.NewMainScene.default_bgm
		else
			var_109_0 = pg.voice_bgm.NewMainScene.bgm

	if arg_109_0.bgm != var_109_0:
		arg_109_0.bgm = var_109_0

		pg.BgmMgr.GetInstance().Push(arg_109_0.__cname, var_109_0)

def var_0_0.clearUI(arg_110_0):
	setActive(arg_110_0.sceneTf, False)
	setActive(arg_110_0.settlementUI, False)
	setActive(arg_110_0.countUI, False)
	setActive(arg_110_0.menuUI, False)
	setActive(arg_110_0.gameUI, False)
	setActive(arg_110_0.selectedUI, False)

def var_0_0.readyStart(arg_111_0):
	setActive(arg_111_0.countUI, True)
	arg_111_0.countAnimator.Play("count")
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_2)

	if var_0_1 and arg_111_0.bgm != var_0_1:
		arg_111_0.bgm = var_0_1

		pg.BgmMgr.GetInstance().Push(arg_111_0.__cname, var_0_1)

def var_0_0.gameStart(arg_112_0):
	setActive(findTF(arg_112_0._tf, "sceneContainer/scene_front"), True)
	setActive(findTF(arg_112_0._tf, "sceneContainer/scene_background"), True)
	setActive(findTF(arg_112_0._tf, "sceneContainer/scene"), True)
	setActive(arg_112_0.scoreAnimTf, False)
	setActive(arg_112_0.gameUI, True)

	arg_112_0.gameStartFlag = True
	arg_112_0.scoreNum = 0
	arg_112_0.playerPosIndex = 2
	arg_112_0.gameStepTime = 0
	arg_112_0.gameTime = var_0_5
	arg_112_0.ignoreTime = False

	arg_112_0.boxController.start()
	arg_112_0.specialController.start()
	arg_112_0.bgController.start()
	arg_112_0.roleController.start()
	arg_112_0.updateGameUI()
	arg_112_0.timerStart()

def var_0_0.getGameTimes(arg_113_0):
	return arg_113_0.GetMGHubData().count

def var_0_0.getGameUsedTimes(arg_114_0):
	return arg_114_0.GetMGHubData().usedtime

def var_0_0.getUltimate(arg_115_0):
	return arg_115_0.GetMGHubData().ultimate

def var_0_0.getGameTotalTime(arg_116_0):
	return (arg_116_0.GetMGHubData().getConfig("reward_need"))

def var_0_0.changeSpeed(arg_117_0, arg_117_1):
	return

def var_0_0.onTimer(arg_118_0):
	arg_118_0.gameStep()

def var_0_0.gameStep(arg_119_0):
	if not arg_119_0.ignoreTime:
		arg_119_0.gameTime = arg_119_0.gameTime - Time.deltaTime

		if arg_119_0.gameTime < 0:
			arg_119_0.gameTime = 0

		arg_119_0.gameStepTime = arg_119_0.gameStepTime + Time.deltaTime

	arg_119_0.boxController.step()
	arg_119_0.specialController.step()
	arg_119_0.bgController.step()
	arg_119_0.roleController.step()
	arg_119_0.updateGameUI()

	if arg_119_0.gameTime <= 0:
		arg_119_0.onGameOver()

		return

def var_0_0.timerStart(arg_120_0):
	if not arg_120_0.timer.running:
		arg_120_0.timer.Start()

def var_0_0.timerStop(arg_121_0):
	if arg_121_0.timer.running:
		arg_121_0.timer.Stop()

def var_0_0.updateGameUI(arg_122_0):
	setText(arg_122_0.scoreTf, arg_122_0.scoreNum)
	setText(arg_122_0.gameTimeS, math.ceil(arg_122_0.gameTime))

def var_0_0.addScore(arg_123_0, arg_123_1):
	setActive(arg_123_0.scoreAnimTf, False)
	setActive(arg_123_0.scoreAnimTf, True)
	setText(arg_123_0.scoreAnimTextTf, "+" .. tostring(arg_123_1))

	arg_123_0.scoreNum = arg_123_0.scoreNum + arg_123_1

	if arg_123_0.scoreNum < 0:
		arg_123_0.scoreNum = 0

def var_0_0.onGameOver(arg_124_0):
	if arg_124_0.settlementFlag:
		return

	arg_124_0.timerStop()

	arg_124_0.settlementFlag = True

	setActive(arg_124_0.clickMask, True)

	if arg_124_0.roleController:
		arg_124_0.roleController.clear()

	if arg_124_0.bgController:
		arg_124_0.bgController.clear()

	LeanTween.delayedCall(go(arg_124_0._tf), 0.1, System.Action(function()
		arg_124_0.settlementFlag = False
		arg_124_0.gameStartFlag = False

		setActive(arg_124_0.clickMask, False)
		arg_124_0.showSettlement()))

def var_0_0.showSettlement(arg_126_0):
	setActive(arg_126_0.settlementUI, True)
	GetComponent(findTF(arg_126_0.settlementUI, "ad"), typeof(Animator)).Play("settlement", -1, 0)

	local var_126_0 = arg_126_0.GetMGData().GetRuntimeData("elements")
	local var_126_1 = arg_126_0.scoreNum
	local var_126_2 = var_126_0 and #var_126_0 > 0 and var_126_0[1] or 0

	setActive(findTF(arg_126_0.settlementUI, "ad/new"), var_126_2 < var_126_1)

	if var_126_2 <= var_126_1:
		var_126_2 = var_126_1

		arg_126_0.StoreDataToServer({
			var_126_2
		})

	local var_126_3 = findTF(arg_126_0.settlementUI, "ad/highText")
	local var_126_4 = findTF(arg_126_0.settlementUI, "ad/currentText")

	setText(var_126_3, var_126_2)
	setText(var_126_4, var_126_1)

	if arg_126_0.getGameTimes() and arg_126_0.getGameTimes() > 0:
		arg_126_0.sendSuccessFlag = True

		arg_126_0.SendSuccess(0)

def var_0_0.resumeGame(arg_127_0):
	arg_127_0.gameStop = False

	setActive(arg_127_0.leaveUI, False)
	arg_127_0.changeSpeed(1)
	arg_127_0.timerStart()

def var_0_0.stopGame(arg_128_0):
	arg_128_0.gameStop = True

	arg_128_0.timerStop()
	arg_128_0.changeSpeed(0)

def var_0_0.onBackPressed(arg_129_0):
	if not arg_129_0.gameStartFlag:
		arg_129_0.emit(var_0_0.ON_BACK_PRESSED)
	else
		if arg_129_0.settlementFlag:
			return

		if isActive(arg_129_0.pauseUI):
			setActive(arg_129_0.pauseUI, False)

		arg_129_0.stopGame()
		setActive(arg_129_0.leaveUI, True)

def var_0_0.willExit(arg_130_0):
	if arg_130_0.handle:
		UpdateBeat.RemoveListener(arg_130_0.handle)

	if arg_130_0._tf and LeanTween.isTweening(go(arg_130_0._tf)):
		LeanTween.cancel(go(arg_130_0._tf))

	if arg_130_0.timer and arg_130_0.timer.running:
		arg_130_0.timer.Stop()

	Time.timeScale = 1
	arg_130_0.timer = None

return var_0_0
