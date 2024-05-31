local var_0_0 = class("CookGameConst")

var_0_0.sound_marcopolo_skill = "ui-mini_shine"
var_0_0.sound_serve = "ui-mini_click"
var_0_0.sound_pickup = ""
var_0_0.sound_ac = "ui-mini_throw"
var_0_0.sound_speed_up = "ui-mini_up"
var_0_0.cook_game_Albacore = "cook_game_Albacore"
var_0_0.cook_game_august = "cook_game_august"
var_0_0.cook_game_elbe = "cook_game_elbe"
var_0_0.cook_game_hakuryu = "cook_game_hakuryu"
var_0_0.cook_game_howe = "cook_game_howe"
var_0_0.cook_game_marcopolo = "cook_game_marcopolo"
var_0_0.cook_game_noshiro = "cook_game_noshiro"
var_0_0.cook_game_pnelope = "cook_game_pnelope"
var_0_0.cook_game_laffey = "cook_game_laffey"
var_0_0.cook_game_janus = "cook_game_janus"
var_0_0.cook_game_flandre = "cook_game_flandre"
var_0_0.cook_game_constellation = "cook_game_constellation"
var_0_0.cook_game_constellation_skill_name = "cook_game_constellation_skill_name"
var_0_0.cook_game_constellation_skill_desc = "cook_game_constellation_skill_desc"
var_0_0.char_ids = {
	9,
	10,
	12,
	11,
	1,
	2,
	3,
	4,
	5,
	6,
	7,
	8
}
var_0_0.random_ids = {
	1,
	2,
	3,
	4,
	5,
	6,
	7,
	8,
	9,
	10,
	11,
	12
}

if PLATFORM_CODE == PLATFORM_CHT:
	var_0_0.char_ids = {
		1,
		2,
		4,
		5,
		6,
		7,
		8,
		9,
		10,
		11,
		12
	}
	var_0_0.random_ids = {
		1,
		2,
		4,
		5,
		6,
		7,
		8,
		9,
		10,
		11,
		12
	}

var_0_0.camp_player = 1
var_0_0.camp_enemy = 2
var_0_0.player_use_ai = False
var_0_0.ac_dictance = 200
var_0_0.added_max = 3
var_0_0.random_score = 3
var_0_0.puzzle_rate = 25
var_0_0.puzzle_time = 7
var_0_0.char_data = {
	{
		id = 1,
		icon = "Albacore",
		ship_id = 108021,
		pos = Vector2(0, 0),
		desc = var_0_0.cook_game_Albacore
	},
	{
		id = 2,
		icon = "august",
		ship_id = 900921,
		pos = Vector2(0, -30),
		desc = var_0_0.cook_game_august
	},
	{
		id = 3,
		icon = "elbe",
		ship_id = 406021,
		pos = Vector2(0, 0),
		desc = var_0_0.cook_game_elbe
	},
	{
		id = 4,
		icon = "hakuryu",
		ship_id = 900919,
		pos = Vector2(0, 0),
		desc = var_0_0.cook_game_hakuryu
	},
	{
		id = 5,
		icon = "howe",
		ship_id = 205091,
		pos = Vector2(0, 0),
		desc = var_0_0.cook_game_howe
	},
	{
		id = 6,
		icon = "marcopolo",
		ship_id = 900922,
		pos = Vector2(0, 0),
		desc = var_0_0.cook_game_marcopolo
	},
	{
		id = 7,
		icon = "noshiro",
		ship_id = 302211,
		pos = Vector2(0, 0),
		desc = var_0_0.cook_game_noshiro
	},
	{
		id = 8,
		icon = "pnelope",
		ship_id = 202291,
		pos = Vector2(0, 0),
		desc = var_0_0.cook_game_pnelope
	},
	{
		id = 9,
		icon = "Laffey",
		ship_id = 101511,
		pos = Vector2(0, 0),
		desc = var_0_0.cook_game_laffey
	},
	{
		id = 10,
		icon = "Janus",
		ship_id = 201351,
		pos = Vector2(0, 0),
		desc = var_0_0.cook_game_janus
	},
	{
		id = 11,
		icon = "Flandre",
		ship_id = 900398,
		pos = Vector2(0, 0),
		desc = var_0_0.cook_game_flandre
	},
	{
		id = 12,
		icon = "constellation",
		ship_id = 104011,
		pos = Vector2(0, 0),
		desc = var_0_0.cook_game_constellation,
		detail_name = var_0_0.cook_game_constellation_skill_name,
		detail_desc = var_0_0.cook_game_constellation_skill_desc
	},
	{
		id = 13,
		icon = "manjuu",
		ship_id = 900398,
		pos = Vector2(0, 0)
	}
}
var_0_0.player_char = "playerChar"
var_0_0.parter_char = "parterchar"
var_0_0.parter_pet = "parter_pet"
var_0_0.enemy1_char = "enemy1Char"
var_0_0.enemy2_char = "enemy2Char"
var_0_0.enemy_pet = "enemy_pet"
var_0_0.char_instiate_data = {
	[var_0_0.player_char] = {
		bound = "playerBox/collider",
		parent = "scene",
		tf_name = var_0_0.player_char,
		init_pos = Vector2(-500, 0)
	},
	[var_0_0.parter_char] = {
		bound = "playerBox/collider",
		parent = "scene",
		tf_name = var_0_0.parter_char,
		init_pos = Vector2(-300, -300)
	},
	[var_0_0.parter_pet] = {
		bound = "playerBox/collider",
		parent = "scene",
		tf_name = var_0_0.parter_pet,
		init_pos = Vector2(-400, -400)
	},
	[var_0_0.enemy1_char] = {
		bound = "enemyBox/collider",
		parent = "scene",
		tf_name = var_0_0.enemy1_char,
		init_pos = Vector2(500, 10)
	},
	[var_0_0.enemy2_char] = {
		bound = "enemyBox/collider",
		parent = "scene",
		tf_name = var_0_0.enemy2_char,
		init_pos = Vector2(300, -310)
	},
	[var_0_0.enemy_pet] = {
		bound = "enemyBox/collider",
		parent = "scene",
		tf_name = var_0_0.enemy_pet,
		init_pos = Vector2(400, -410)
	}
}
var_0_0.char_battle_data = {
	{
		name = "Albacore",
		base_speed = 210,
		speed_able = False,
		double_able = False,
		id = 1,
		ac_able = True
	},
	{
		name = "august",
		base_speed = 300,
		speed_able = False,
		double_able = False,
		id = 2,
		ac_able = False
	},
	{
		name = "elbe",
		base_speed = 240,
		speed_able = False,
		double_able = True,
		id = 3,
		ac_able = False
	},
	{
		name = "hakuryu",
		base_speed = 240,
		speed_able = True,
		double_able = False,
		id = 4,
		speed_max = 3,
		ac_able = False
	},
	{
		name = "howe",
		base_speed = 240,
		speed_able = False,
		double_able = False,
		id = 5,
		half_double = True,
		ac_able = False
	},
	{
		extend = True,
		name = "marcopolo",
		speed_able = False,
		double_able = False,
		id = 6,
		base_speed = 240,
		ac_able = False
	},
	{
		name = "noshiro",
		base_speed = 240,
		speed_able = False,
		double_able = False,
		id = 7,
		cake_allow = True,
		ac_able = False,
		weight = 1
	},
	{
		name = "pnelope",
		base_speed = 240,
		speed_able = False,
		double_able = False,
		id = 8,
		double_score = True,
		ac_able = False
	},
	{
		id = 9,
		name = "Laffey",
		speed_able = False,
		double_able = False,
		score_added = True,
		base_speed = 240,
		ac_able = False,
		effect = {
			"EF_Right_X",
			"EF_Right_Y",
			"EF_Right_Z"
		}
	},
	{
		name = "Janus",
		base_speed = 240,
		speed_able = False,
		double_able = False,
		id = 10,
		random_score = True,
		ac_able = False
	},
	{
		name = "Flandre",
		base_speed = 240,
		speed_able = False,
		double_able = False,
		id = 11,
		pet = 101,
		ac_able = False
	},
	{
		ac_able = False,
		name = "constellation",
		speed_able = False,
		double_able = False,
		id = 12,
		base_speed = 240,
		weight = 2,
		puzzle = True,
		effect = {
			"EF_Skill"
		}
	},
	{
		name = "manjuu",
		base_speed = 240,
		speed_able = False,
		double_able = False,
		id = 101,
		ac_able = False,
		offset = Vector2(0, 90)
	}
}
var_0_0.judge_num = 4
var_0_0.judge_data = {
	{
		id = 1,
		name = "judges_1",
		cake_id = 1
	},
	{
		id = 2,
		name = "judges_2",
		cake_id = 2
	},
	{
		id = 3,
		name = "judges_3",
		cake_id = 3
	},
	{
		id = 4,
		name = "judges_4",
		cake_id = 4
	},
	{
		id = 5,
		name = "judges_5",
		cake_id = 5
	}
}

return var_0_0
