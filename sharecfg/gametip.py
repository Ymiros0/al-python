pg = pg or {}
pg.gametip = setmetatable({
	__name = "gametip"
}, confMT)
pg.base = pg.base or {}
pg.base.gametip = pg.base.gametip or {}
cs = cs or {}
cs.gametip = {
	["new_airi_error_code_-1"] = {
		0,
		99,
		True
	},
	new_airi_error_code_0 = {
		99,
		92,
		True
	},
	new_airi_error_code_100100 = {
		191,
		109,
		True
	},
	new_airi_error_code_100110 = {
		300,
		109,
		True
	},
	new_airi_error_code_100111 = {
		409,
		113,
		True
	},
	new_airi_error_code_100112 = {
		522,
		139,
		True
	},
	new_airi_error_code_100113 = {
		661,
		135,
		True
	},
	new_airi_error_code_100114 = {
		796,
		128,
		True
	},
	new_airi_error_code_100115 = {
		924,
		132,
		True
	},
	new_airi_error_code_100116 = {
		1056,
		125,
		True
	},
	new_airi_error_code_100117 = {
		1181,
		108,
		True
	},
	new_airi_error_code_100120 = {
		1289,
		120,
		True
	},
	new_airi_error_code_100130 = {
		1409,
		117,
		True
	},
	new_airi_error_code_100140 = {
		1526,
		122,
		True
	},
	new_airi_error_code_100150 = {
		1648,
		123,
		True
	},
	new_airi_error_code_100160 = {
		1771,
		126,
		True
	},
	new_airi_error_code_100170 = {
		1897,
		113,
		True
	},
	new_airi_error_code_100180 = {
		2010,
		149,
		True
	},
	new_airi_error_code_100190 = {
		2159,
		133,
		True
	},
	new_airi_error_code_100200 = {
		2292,
		148,
		True
	},
	new_airi_error_code_100210 = {
		2440,
		164,
		True
	},
	new_airi_error_code_100211 = {
		2604,
		112,
		True
	},
	new_airi_error_code_100212 = {
		2716,
		114,
		True
	},
	new_airi_error_code_100213 = {
		2830,
		118,
		True
	},
	new_airi_error_code_100220 = {
		2948,
		112,
		True
	},
	new_airi_error_code_100221 = {
		3060,
		113,
		True
	},
	new_airi_error_code_100222 = {
		3173,
		113,
		True
	},
	new_airi_error_code_100223 = {
		3286,
		117,
		True
	},
	new_airi_error_code_100224 = {
		3403,
		118,
		True
	},
	new_airi_error_code_100225 = {
		3521,
		132,
		True
	},
	new_airi_error_code_100226 = {
		3653,
		135,
		True
	},
	new_airi_error_code_100227 = {
		3788,
		131,
		True
	},
	new_airi_error_code_100228 = {
		3919,
		130,
		True
	},
	new_airi_error_code_100229 = {
		4049,
		138,
		True
	},
	new_airi_error_code_100231 = {
		4187,
		144,
		True
	},
	new_airi_error_code_100232 = {
		4331,
		144,
		True
	},
	new_airi_error_code_100233 = {
		4475,
		131,
		True
	},
	new_airi_error_code_100234 = {
		4606,
		128,
		True
	},
	new_airi_error_code_100230 = {
		4734,
		111,
		True
	},
	new_airi_error_code_100240 = {
		4845,
		137,
		True
	},
	new_airi_error_code_100241 = {
		4982,
		133,
		True
	},
	new_airi_error_code_100242 = {
		5115,
		124,
		True
	},
	new_airi_error_code_100243 = {
		5239,
		140,
		True
	},
	new_airi_error_code_100244 = {
		5379,
		136,
		True
	},
	new_airi_error_code_100245 = {
		5515,
		144,
		True
	},
	new_airi_error_code_100246 = {
		5659,
		142,
		True
	},
	new_airi_error_code_100300 = {
		5801,
		118,
		True
	},
	new_airi_error_code_100301 = {
		5919,
		118,
		True
	},
	new_airi_error_code_100302 = {
		6037,
		132,
		True
	},
	new_airi_error_code_100303 = {
		6169,
		109,
		True
	},
	new_airi_error_code_100304 = {
		6278,
		124,
		True
	},
	new_airi_error_code_100305 = {
		6402,
		111,
		True
	},
	new_airi_error_code_100306 = {
		6513,
		123,
		True
	},
	new_airi_error_code_100404 = {
		6636,
		103,
		True
	},
	new_airi_error_code_200100 = {
		6739,
		115,
		True
	},
	new_airi_error_code_200110 = {
		6854,
		121,
		True
	},
	new_airi_error_code_200120 = {
		6975,
		131,
		True
	},
	new_airi_error_code_200130 = {
		7106,
		119,
		True
	},
	new_airi_error_code_200140 = {
		7225,
		114,
		True
	},
	new_airi_error_code_200150 = {
		7339,
		125,
		True
	},
	new_airi_error_code_200160 = {
		7464,
		114,
		True
	},
	new_airi_error_code_200170 = {
		7578,
		128,
		True
	},
	new_airi_error_code_200180 = {
		7706,
		145,
		True
	},
	new_airi_error_code_200190 = {
		7851,
		113,
		True
	},
	new_airi_error_code_200200 = {
		7964,
		121,
		True
	},
	new_airi_error_code_200210 = {
		8085,
		134,
		True
	},
	new_airi_error_code_200220 = {
		8219,
		132,
		True
	},
	new_airi_error_code_200230 = {
		8351,
		134,
		True
	},
	new_airi_error_code_200240 = {
		8485,
		139,
		True
	},
	new_airi_error_code_200250 = {
		8624,
		124,
		True
	},
	new_airi_error_code_200260 = {
		8748,
		122,
		True
	},
	new_airi_error_code_200270 = {
		8870,
		155,
		True
	},
	new_airi_error_code_200280 = {
		9025,
		140,
		True
	},
	new_airi_error_code_200290 = {
		9165,
		141,
		True
	},
	new_airi_error_code_200300 = {
		9306,
		127,
		True
	},
	new_airi_error_code_200310 = {
		9433,
		131,
		True
	},
	new_airi_error_code_200320 = {
		9564,
		169,
		True
	},
	new_airi_error_code_200330 = {
		9733,
		122,
		True
	},
	new_airi_error_code_200340 = {
		9855,
		114,
		True
	},
	new_airi_error_code_200350 = {
		9969,
		111,
		True
	},
	new_airi_error_code_200360 = {
		10080,
		124,
		True
	},
	new_airi_error_code_300100 = {
		10204,
		111,
		True
	},
	new_airi_error_code_100121 = {
		10315,
		132,
		True
	},
	new_airi_error_code_100201 = {
		10447,
		241,
		True
	},
	new_airi_error_code_100202 = {
		10688,
		254,
		True
	},
	new_airi_error_code_100203 = {
		10942,
		263,
		True
	},
	new_airi_error_code_100204 = {
		11205,
		347,
		True
	},
	new_airi_error_code_100205 = {
		11552,
		174,
		True
	},
	new_airi_error_code_100206 = {
		11726,
		241,
		True
	},
	new_airi_error_code_100207 = {
		11967,
		91,
		True
	},
	new_airi_error_code_100214 = {
		12058,
		301,
		True
	},
	new_airi_error_code_100218 = {
		12359,
		142,
		True
	},
	new_airi_error_code_100235 = {
		12501,
		131,
		True
	},
	new_airi_error_code_100307 = {
		12632,
		91,
		True
	},
	new_airi_error_code_100310 = {
		12723,
		137,
		True
	},
	new_airi_error_code_100311 = {
		12860,
		144,
		True
	},
	new_airi_error_code_100401 = {
		13004,
		116,
		True
	},
	new_airi_error_code_100600 = {
		13120,
		131,
		True
	},
	new_airi_error_code_100802 = {
		13251,
		91,
		True
	},
	new_airi_error_code_100803 = {
		13342,
		134,
		True
	},
	new_airi_error_code_200141 = {
		13476,
		148,
		True
	},
	new_airi_error_code_200145 = {
		13624,
		145,
		True
	},
	new_airi_error_code_200231 = {
		13769,
		91,
		True
	},
	new_airi_error_code_200232 = {
		13860,
		132,
		True
	},
	new_airi_error_code_200235 = {
		13992,
		115,
		True
	},
	new_airi_error_code_200236 = {
		14107,
		107,
		True
	},
	new_airi_error_code_200370 = {
		14214,
		91,
		True
	},
	new_airi_error_code_200380 = {
		14305,
		91,
		True
	},
	new_airi_error_code_200390 = {
		14396,
		91,
		True
	},
	new_airi_error_code_200400 = {
		14487,
		91,
		True
	},
	new_airi_error_code_200410 = {
		14578,
		124,
		True
	},
	new_airi_error_code_200420 = {
		14702,
		108,
		True
	},
	new_airi_error_code_200430 = {
		14810,
		120,
		True
	},
	new_airi_error_code_300101 = {
		14930,
		91,
		True
	},
	new_airi_error_code_300102 = {
		15021,
		91,
		True
	},
	new_airi_error_code_300200 = {
		15112,
		91,
		True
	},
	new_airi_error_code_300210 = {
		15203,
		117,
		True
	},
	new_airi_error_code_300220 = {
		15320,
		115,
		True
	},
	new_airi_error_code_300300 = {
		15435,
		119,
		True
	},
	new_airi_error_code_400010 = {
		15554,
		113,
		True
	},
	new_airi_error_code_400020 = {
		15667,
		119,
		True
	},
	new_airi_error_code_400030 = {
		15786,
		121,
		True
	},
	new_airi_error_code_400040 = {
		15907,
		118,
		True
	},
	new_airi_error_code_400050 = {
		16025,
		150,
		True
	},
	new_airi_error_code_400060 = {
		16175,
		125,
		True
	},
	new_airi_error_code_400070 = {
		16300,
		123,
		True
	},
	new_airi_error_code_400080 = {
		16423,
		150,
		True
	},
	new_airi_error_code_400090 = {
		16573,
		150,
		True
	},
	new_airi_error_code_400100 = {
		16723,
		150,
		True
	},
	new_airi_error_code_400460 = {
		16873,
		133,
		True
	},
	ad_0 = {
		17006,
		68,
		True
	},
	ad_1 = {
		17074,
		304,
		True
	},
	ad_2 = {
		17378,
		298,
		True
	},
	ad_3 = {
		17676,
		298,
		True
	},
	word_back = {
		17974,
		77,
		True
	},
	word_backyardMoney = {
		18051,
		94,
		True
	},
	word_cancel = {
		18145,
		81,
		True
	},
	word_cmdClose = {
		18226,
		89,
		True
	},
	word_delete = {
		18315,
		81,
		True
	},
	word_dockyard = {
		18396,
		81,
		True
	},
	word_dockyardUpgrade = {
		18477,
		95,
		True
	},
	word_dockyardDestroy = {
		18572,
		90,
		True
	},
	word_shipInfoScene_equip = {
		18662,
		97,
		True
	},
	word_shipInfoScene_reinfomation = {
		18759,
		106,
		True
	},
	word_shipInfoScene_infomation = {
		18865,
		105,
		True
	},
	word_editFleet = {
		18970,
		92,
		True
	},
	word_exp = {
		19062,
		75,
		True
	},
	word_expAdd = {
		19137,
		82,
		True
	},
	word_exp_chinese = {
		19219,
		83,
		True
	},
	word_exist = {
		19302,
		78,
		True
	},
	word_equip = {
		19380,
		78,
		True
	},
	word_equipDestory = {
		19458,
		88,
		True
	},
	word_food = {
		19546,
		79,
		True
	},
	word_get = {
		19625,
		79,
		True
	},
	word_got = {
		19704,
		79,
		True
	},
	word_not_get = {
		19783,
		86,
		True
	},
	word_next_level = {
		19869,
		89,
		True
	},
	word_intimacy = {
		19958,
		85,
		True
	},
	word_is = {
		20043,
		74,
		True
	},
	word_date = {
		20117,
		74,
		True
	},
	word_hour = {
		20191,
		74,
		True
	},
	word_minute = {
		20265,
		76,
		True
	},
	word_second = {
		20341,
		76,
		True
	},
	word_lv = {
		20417,
		74,
		True
	},
	word_proficiency = {
		20491,
		91,
		True
	},
	word_material = {
		20582,
		82,
		True
	},
	word_notExist = {
		20664,
		91,
		True
	},
	word_ok = {
		20755,
		78,
		True
	},
	word_preview = {
		20833,
		83,
		True
	},
	word_rarity = {
		20916,
		81,
		True
	},
	word_speedUp = {
		20997,
		85,
		True
	},
	word_succeed = {
		21082,
		83,
		True
	},
	word_start = {
		21165,
		79,
		True
	},
	word_kiss = {
		21244,
		80,
		True
	},
	word_take = {
		21324,
		80,
		True
	},
	word_takeOk = {
		21404,
		84,
		True
	},
	word_many = {
		21488,
		77,
		True
	},
	word_normal_2 = {
		21565,
		82,
		True
	},
	word_simple = {
		21647,
		79,
		True
	},
	word_save = {
		21726,
		77,
		True
	},
	word_levelup = {
		21803,
		84,
		True
	},
	word_serverLoadVindicate = {
		21887,
		122,
		True
	},
	word_serverLoadNormal = {
		22009,
		167,
		True
	},
	word_serverLoadFull = {
		22176,
		112,
		True
	},
	word_registerFull = {
		22288,
		114,
		True
	},
	word_synthesize = {
		22402,
		84,
		True
	},
	word_synthesize_power = {
		22486,
		96,
		True
	},
	word_achieved_item = {
		22582,
		93,
		True
	},
	word_formation = {
		22675,
		84,
		True
	},
	word_teach = {
		22759,
		79,
		True
	},
	word_study = {
		22838,
		79,
		True
	},
	word_destroy = {
		22917,
		82,
		True
	},
	word_upgrade = {
		22999,
		87,
		True
	},
	word_train = {
		23086,
		78,
		True
	},
	word_rest = {
		23164,
		77,
		True
	},
	word_capacity = {
		23241,
		88,
		True
	},
	word_operation = {
		23329,
		88,
		True
	},
	word_intensify_phase = {
		23417,
		97,
		True
	},
	word_systemClose = {
		23514,
		130,
		True
	},
	word_attr_antisub = {
		23644,
		85,
		True
	},
	word_attr_cannon = {
		23729,
		83,
		True
	},
	word_attr_torpedo = {
		23812,
		85,
		True
	},
	word_attr_antiaircraft = {
		23897,
		89,
		True
	},
	word_attr_air = {
		23986,
		81,
		True
	},
	word_attr_durability = {
		24067,
		86,
		True
	},
	word_attr_armor = {
		24153,
		84,
		True
	},
	word_attr_reload = {
		24237,
		84,
		True
	},
	word_attr_speed = {
		24321,
		84,
		True
	},
	word_attr_luck = {
		24405,
		82,
		True
	},
	word_attr_range = {
		24487,
		84,
		True
	},
	word_attr_range_view = {
		24571,
		89,
		True
	},
	word_attr_hit = {
		24660,
		80,
		True
	},
	word_attr_dodge = {
		24740,
		83,
		True
	},
	word_attr_luck1 = {
		24823,
		83,
		True
	},
	word_attr_damage = {
		24906,
		83,
		True
	},
	word_attr_healthy = {
		24989,
		88,
		True
	},
	word_attr_cd = {
		25077,
		78,
		True
	},
	word_attr_speciality = {
		25155,
		91,
		True
	},
	word_attr_level = {
		25246,
		88,
		True
	},
	word_shipState_npc = {
		25334,
		120,
		True
	},
	word_shipState_fight = {
		25454,
		110,
		True
	},
	word_shipState_world = {
		25564,
		137,
		True
	},
	word_shipState_rest = {
		25701,
		109,
		True
	},
	word_shipState_study = {
		25810,
		109,
		True
	},
	word_shipState_tactics = {
		25919,
		111,
		True
	},
	word_shipState_collect = {
		26030,
		116,
		True
	},
	word_shipState_event = {
		26146,
		121,
		True
	},
	word_shipState_activity = {
		26267,
		138,
		True
	},
	word_shipState_sham = {
		26405,
		119,
		True
	},
	word_shipState_support = {
		26524,
		130,
		True
	},
	word_shipType_quZhu = {
		26654,
		92,
		True
	},
	word_shipType_qinXun = {
		26746,
		97,
		True
	},
	word_shipType_zhongXun = {
		26843,
		99,
		True
	},
	word_shipType_zhanLie = {
		26942,
		95,
		True
	},
	word_shipType_hangMu = {
		27037,
		91,
		True
	},
	word_shipType_weiXiu = {
		27128,
		90,
		True
	},
	word_shipType_other = {
		27218,
		87,
		True
	},
	word_shipType_all = {
		27305,
		90,
		True
	},
	word_gem = {
		27395,
		76,
		True
	},
	word_freeGem = {
		27471,
		80,
		True
	},
	word_gem_icon = {
		27551,
		109,
		True
	},
	word_freeGem_icon = {
		27660,
		113,
		True
	},
	word_exploit = {
		27773,
		81,
		True
	},
	word_rankScore = {
		27854,
		84,
		True
	},
	word_battery = {
		27938,
		91,
		True
	},
	word_oil = {
		28029,
		75,
		True
	},
	word_gold = {
		28104,
		78,
		True
	},
	word_oilField = {
		28182,
		85,
		True
	},
	word_goldField = {
		28267,
		88,
		True
	},
	word_ema = {
		28355,
		76,
		True
	},
	word_ema1 = {
		28431,
		77,
		True
	},
	word_pt = {
		28508,
		77,
		True
	},
	word_omamori = {
		28585,
		89,
		True
	},
	word_yisegefuke_pt = {
		28674,
		88,
		True
	},
	word_faxipt = {
		28762,
		84,
		True
	},
	word_count_2 = {
		28846,
		99,
		True
	},
	word_clear = {
		28945,
		78,
		True
	},
	word_buy = {
		29023,
		75,
		True
	},
	word_happy = {
		29098,
		102,
		True
	},
	word_normal = {
		29200,
		104,
		True
	},
	word_tired = {
		29304,
		102,
		True
	},
	word_angry = {
		29406,
		102,
		True
	},
	word_max_page = {
		29508,
		80,
		True
	},
	word_least_page = {
		29588,
		82,
		True
	},
	word_week = {
		29670,
		74,
		True
	},
	word_day = {
		29744,
		73,
		True
	},
	word_use = {
		29817,
		75,
		True
	},
	word_use_batch = {
		29892,
		84,
		True
	},
	word_discount = {
		29976,
		85,
		True
	},
	word_threaten_exclude = {
		30061,
		101,
		True
	},
	word_threaten = {
		30162,
		83,
		True
	},
	word_comingSoon = {
		30245,
		90,
		True
	},
	word_lightArmor = {
		30335,
		84,
		True
	},
	word_mediumArmor = {
		30419,
		86,
		True
	},
	word_heavyarmor = {
		30505,
		84,
		True
	},
	word_level_upperLimit = {
		30589,
		94,
		True
	},
	word_level_require = {
		30683,
		92,
		True
	},
	word_materal_no_enough = {
		30775,
		118,
		True
	},
	word_default = {
		30893,
		83,
		True
	},
	word_count = {
		30976,
		80,
		True
	},
	word_kind = {
		31056,
		77,
		True
	},
	word_piece = {
		31133,
		75,
		True
	},
	word_main_fleet = {
		31208,
		89,
		True
	},
	word_vanguard_fleet = {
		31297,
		91,
		True
	},
	word_theme = {
		31388,
		79,
		True
	},
	word_recommend = {
		31467,
		82,
		True
	},
	word_wallpaper = {
		31549,
		88,
		True
	},
	word_furniture = {
		31637,
		83,
		True
	},
	word_decorate = {
		31720,
		83,
		True
	},
	word_special = {
		31803,
		83,
		True
	},
	word_expand = {
		31886,
		81,
		True
	},
	word_wall = {
		31967,
		77,
		True
	},
	word_floorpaper = {
		32044,
		84,
		True
	},
	word_collection = {
		32128,
		89,
		True
	},
	word_mat = {
		32217,
		78,
		True
	},
	word_comfort_level = {
		32295,
		89,
		True
	},
	word_room = {
		32384,
		80,
		True
	},
	word_equipment_all = {
		32464,
		85,
		True
	},
	word_equipment_cannon = {
		32549,
		94,
		True
	},
	word_equipment_torpedo = {
		32643,
		93,
		True
	},
	word_equipment_aircraft = {
		32736,
		95,
		True
	},
	word_equipment_small_cannon = {
		32831,
		102,
		True
	},
	word_equipment_medium_cannon = {
		32933,
		103,
		True
	},
	word_equipment_big_cannon = {
		33036,
		100,
		True
	},
	word_equipment_warship_torpedo = {
		33136,
		109,
		True
	},
	word_equipment_submarine_torpedo = {
		33245,
		107,
		True
	},
	word_equipment_antiaircraft = {
		33352,
		99,
		True
	},
	word_equipment_fighter = {
		33451,
		93,
		True
	},
	word_equipment_bomber = {
		33544,
		96,
		True
	},
	word_equipment_torpedo_bomber = {
		33640,
		104,
		True
	},
	word_equipment_equip = {
		33744,
		93,
		True
	},
	word_equipment_type = {
		33837,
		87,
		True
	},
	word_equipment_rarity = {
		33924,
		91,
		True
	},
	word_equipment_intensify = {
		34015,
		95,
		True
	},
	word_equipment_special = {
		34110,
		90,
		True
	},
	word_primary_weapons = {
		34200,
		95,
		True
	},
	word_main_cannons = {
		34295,
		89,
		True
	},
	word_shipboard_aircraft = {
		34384,
		95,
		True
	},
	word_sub_cannons = {
		34479,
		94,
		True
	},
	word_sub_weapons = {
		34573,
		96,
		True
	},
	word_torpedo = {
		34669,
		83,
		True
	},
	["word_ air_defense_artillery"] = {
		34752,
		99,
		True
	},
	word_air_defense_artillery = {
		34851,
		98,
		True
	},
	word_device = {
		34949,
		84,
		True
	},
	word_cannon = {
		35033,
		84,
		True
	},
	word_fighter = {
		35117,
		83,
		True
	},
	word_bomber = {
		35200,
		86,
		True
	},
	word_attacker = {
		35286,
		91,
		True
	},
	word_seaplane = {
		35377,
		91,
		True
	},
	word_submarine_torpedo = {
		35468,
		103,
		True
	},
	word_missile = {
		35571,
		83,
		True
	},
	word_online = {
		35654,
		81,
		True
	},
	word_apply = {
		35735,
		79,
		True
	},
	word_star = {
		35814,
		78,
		True
	},
	word_level = {
		35892,
		77,
		True
	},
	word_mod_value = {
		35969,
		89,
		True
	},
	word_wait = {
		36058,
		73,
		True
	},
	word_consume = {
		36131,
		80,
		True
	},
	word_sell_out = {
		36211,
		85,
		True
	},
	word_sell_lock = {
		36296,
		82,
		True
	},
	word_diamond_tip = {
		36378,
		493,
		True
	},
	word_contribution = {
		36871,
		87,
		True
	},
	word_guild_res = {
		36958,
		90,
		True
	},
	word_fit = {
		37048,
		80,
		True
	},
	word_equipment_skin = {
		37128,
		89,
		True
	},
	word_activity = {
		37217,
		83,
		True
	},
	word_urgency_event = {
		37300,
		94,
		True
	},
	word_shop = {
		37394,
		77,
		True
	},
	word_facility = {
		37471,
		83,
		True
	},
	word_cv_key_main = {
		37554,
		92,
		True
	},
	channel_name_1 = {
		37646,
		81,
		True
	},
	channel_name_2 = {
		37727,
		83,
		True
	},
	channel_name_3 = {
		37810,
		84,
		True
	},
	channel_name_4 = {
		37894,
		85,
		True
	},
	channel_name_5 = {
		37979,
		83,
		True
	},
	common_wait = {
		38062,
		107,
		True
	},
	common_ship_type = {
		38169,
		89,
		True
	},
	common_dont_remind_dur_login = {
		38258,
		108,
		True
	},
	common_activity_end = {
		38366,
		135,
		True
	},
	common_activity_notStartOrEnd = {
		38501,
		191,
		True
	},
	common_activity_not_start = {
		38692,
		143,
		True
	},
	common_error = {
		38835,
		90,
		True
	},
	common_no_gold = {
		38925,
		130,
		True
	},
	common_no_oil = {
		39055,
		126,
		True
	},
	common_no_rmb = {
		39181,
		127,
		True
	},
	common_count_noenough = {
		39308,
		101,
		True
	},
	common_no_dorm_gold = {
		39409,
		142,
		True
	},
	common_no_resource = {
		39551,
		114,
		True
	},
	common_no_item = {
		39665,
		128,
		True
	},
	common_no_item_1 = {
		39793,
		96,
		True
	},
	common_no_x = {
		39889,
		123,
		True
	},
	common_limit_cmd = {
		40012,
		134,
		True
	},
	common_limit_type = {
		40146,
		159,
		True
	},
	common_limit_equip = {
		40305,
		97,
		True
	},
	common_buy_success = {
		40402,
		92,
		True
	},
	common_limit_level = {
		40494,
		134,
		True
	},
	common_shopId_noFound = {
		40628,
		102,
		True
	},
	common_today_buy_limit = {
		40730,
		106,
		True
	},
	common_not_enter_room = {
		40836,
		96,
		True
	},
	common_test_ship = {
		40932,
		108,
		True
	},
	common_entry_inhibited = {
		41040,
		101,
		True
	},
	common_refresh_count_insufficient = {
		41141,
		113,
		True
	},
	common_get_player_info_erro = {
		41254,
		121,
		True
	},
	common_no_open = {
		41375,
		90,
		True
	},
	["common_already owned"] = {
		41465,
		88,
		True
	},
	common_not_get_ship = {
		41553,
		101,
		True
	},
	common_sale_out = {
		41654,
		87,
		True
	},
	common_skin_out_of_stock = {
		41741,
		99,
		True
	},
	common_go_home = {
		41840,
		121,
		True
	},
	dont_remind_today = {
		41961,
		89,
		True
	},
	dont_remind_session = {
		42050,
		91,
		True
	},
	battle_no_oil = {
		42141,
		144,
		True
	},
	battle_emptyBlock = {
		42285,
		116,
		True
	},
	battle_duel_main_rage = {
		42401,
		171,
		True
	},
	battle_main_emergent = {
		42572,
		163,
		True
	},
	battle_battleMediator_goOnFight = {
		42735,
		103,
		True
	},
	battle_battleMediator_existFight = {
		42838,
		101,
		True
	},
	battle_battleMediator_clear_warning = {
		42939,
		251,
		True
	},
	battle_battleMediator_quest_exist = {
		43190,
		233,
		True
	},
	battle_levelMediator_ok_takeResource = {
		43423,
		119,
		True
	},
	battle_result_time_limit = {
		43542,
		125,
		True
	},
	battle_result_sink_limit = {
		43667,
		111,
		True
	},
	battle_result_undefeated = {
		43778,
		101,
		True
	},
	battle_result_victory = {
		43879,
		98,
		True
	},
	battle_result_defeat_all_enemys = {
		43977,
		117,
		True
	},
	battle_result_base_score = {
		44094,
		102,
		True
	},
	battle_result_dead_score = {
		44196,
		104,
		True
	},
	battle_result_score = {
		44300,
		105,
		True
	},
	battle_result_score_total = {
		44405,
		95,
		True
	},
	battle_result_total_damage = {
		44500,
		103,
		True
	},
	battle_result_contribution = {
		44603,
		111,
		True
	},
	battle_result_total_score = {
		44714,
		101,
		True
	},
	battle_result_max_combo = {
		44815,
		97,
		True
	},
	battle_levelScene_0Oil = {
		44912,
		105,
		True
	},
	battle_levelScene_0Gold = {
		45017,
		108,
		True
	},
	battle_levelScene_noRaderCount = {
		45125,
		106,
		True
	},
	battle_levelScene_lock = {
		45231,
		185,
		True
	},
	battle_levelScene_hard_lock = {
		45416,
		245,
		True
	},
	battle_levelScene_close = {
		45661,
		130,
		True
	},
	battle_levelScene_chapter_lock = {
		45791,
		193,
		True
	},
	battle_preCombatLayer_changeFormationError = {
		45984,
		160,
		True
	},
	battle_preCombatLayer_changeFormationNumberError = {
		46144,
		197,
		True
	},
	battle_preCombatLayer_ready = {
		46341,
		141,
		True
	},
	battle_preCombatLayer_quest_leaveFleet = {
		46482,
		151,
		True
	},
	battle_preCombatLayer_clear_confirm = {
		46633,
		154,
		True
	},
	battle_preCombatLayer_auto_confirm = {
		46787,
		154,
		True
	},
	battle_preCombatLayer_save_confirm = {
		46941,
		124,
		True
	},
	battle_preCombatLayer_save_march = {
		47065,
		126,
		True
	},
	battle_preCombatLayer_save_success = {
		47191,
		114,
		True
	},
	battle_preCombatLayer_time_limit = {
		47305,
		123,
		True
	},
	battle_preCombatLayer_sink_limit = {
		47428,
		119,
		True
	},
	battle_preCombatLayer_undefeated = {
		47547,
		119,
		True
	},
	battle_preCombatLayer_victory = {
		47666,
		111,
		True
	},
	battle_preCombatLayer_time_hold = {
		47777,
		119,
		True
	},
	battle_preCombatLayer_damage_before_end = {
		47896,
		158,
		True
	},
	battle_preCombatLayer_destory_transport_ship = {
		48054,
		138,
		True
	},
	battle_preCombatMediator_leastLimit = {
		48192,
		124,
		True
	},
	battle_preCombatMediator_timeout = {
		48316,
		184,
		True
	},
	battle_preCombatMediator_activity_timeout = {
		48500,
		203,
		True
	},
	battle_resourceSiteLayer_collecTimeDefault = {
		48703,
		155,
		True
	},
	battle_resourceSiteLayer_collecTime = {
		48858,
		142,
		True
	},
	battle_resourceSiteLayer_maxLv = {
		49000,
		139,
		True
	},
	battle_resourceSiteLayer_avgLv = {
		49139,
		139,
		True
	},
	battle_resourceSiteLayer_shipTypeCount = {
		49278,
		108,
		True
	},
	battle_resourceSiteLayer_no_maxLv = {
		49386,
		157,
		True
	},
	battle_resourceSiteLayer_no_avgLv = {
		49543,
		157,
		True
	},
	battle_resourceSiteLayer_no_shipTypeCount = {
		49700,
		151,
		True
	},
	battle_resourceSiteLayer_startError_collecting = {
		49851,
		123,
		True
	},
	battle_resourceSiteLayer_startError_not5Ship = {
		49974,
		162,
		True
	},
	battle_resourceSiteLayer_startError_limit = {
		50136,
		153,
		True
	},
	battle_resourceSiteLayer_endError_notStar = {
		50289,
		131,
		True
	},
	battle_resourceSiteLayer_quest_end = {
		50420,
		182,
		True
	},
	battle_resourceSiteMediator_noSite = {
		50602,
		127,
		True
	},
	battle_resourceSiteMediator_shipState_fight = {
		50729,
		157,
		True
	},
	battle_resourceSiteMediator_shipState_rest = {
		50886,
		133,
		True
	},
	battle_resourceSiteMediator_shipState_study = {
		51019,
		133,
		True
	},
	battle_resourceSiteMediator_shipState_event = {
		51152,
		138,
		True
	},
	battle_resourceSiteMediator_shipState_same = {
		51290,
		140,
		True
	},
	battle_resourceSiteMediator_ok_end = {
		51430,
		112,
		True
	},
	battle_autobot_unlock = {
		51542,
		106,
		True
	},
	tips_confirm_teleport_sub = {
		51648,
		335,
		True
	},
	backyard_addExp_Info = {
		51983,
		280,
		True
	},
	backyard_extendCapacity_error = {
		52263,
		111,
		True
	},
	backyard_extendCapacity_ok = {
		52374,
		174,
		True
	},
	backyard_addShip_error = {
		52548,
		106,
		True
	},
	backyard_buyFurniture_error = {
		52654,
		122,
		True
	},
	backyard_extendBackYard_error = {
		52776,
		122,
		True
	},
	backyard_addFood_error = {
		52898,
		108,
		True
	},
	backyard_addFood_ok = {
		53006,
		141,
		True
	},
	backyard_putFurniture_ok = {
		53147,
		94,
		True
	},
	backyard_backyardGranaryLayer_foodCountLimit = {
		53241,
		138,
		True
	},
	backyard_shipAddInimacy_ok = {
		53379,
		161,
		True
	},
	backyard_shipAddInimacy_error = {
		53540,
		119,
		True
	},
	backyard_shipAddMoney_ok = {
		53659,
		185,
		True
	},
	backyard_shipAddMoney_error = {
		53844,
		116,
		True
	},
	backyard_shipExit_error = {
		53960,
		109,
		True
	},
	backyard_shipSpeedUpEnergy_error = {
		54069,
		112,
		True
	},
	backyard_shipAlreadyExit = {
		54181,
		111,
		True
	},
	backyard_backyardGranaryLayer_full = {
		54292,
		163,
		True
	},
	backyard_backyardGranaryLayer_buyCountLimit = {
		54455,
		152,
		True
	},
	backyard_backyardGranaryLayer_error_noResource = {
		54607,
		181,
		True
	},
	backyard_backyardGranaryLayer_noFood = {
		54788,
		151,
		True
	},
	backyard_backyardGranaryLayer_noTimer = {
		54939,
		188,
		True
	},
	backyard_backyardGranaryLayer_word = {
		55127,
		147,
		True
	},
	backyard_backyardGranaryLayer_noShip = {
		55274,
		168,
		True
	},
	backyard_backyardGranaryLayer_foodTimeNotice_top = {
		55442,
		144,
		True
	},
	backyard_backyardGranaryLayer_foodTimeNotice_bottom = {
		55586,
		133,
		True
	},
	backyard_backyardGranaryLayer_foodMaxIncreaseNotice = {
		55719,
		199,
		True
	},
	backyard_backyardGranaryLayer_error_entendFail = {
		55918,
		190,
		True
	},
	backyard_backyardGranaryLayer_buy_max_count = {
		56108,
		154,
		True
	},
	backyard_backyardScene_comforChatContent1 = {
		56262,
		291,
		True
	},
	backyard_backyardScene_comforChatContent2 = {
		56553,
		275,
		True
	},
	backyard_buyExtendItem_question = {
		56828,
		172,
		True
	},
	backyard_backyardScene_expression_label_1 = {
		57000,
		108,
		True
	},
	backyard_backyardScene_expression_label_2 = {
		57108,
		111,
		True
	},
	backyard_backyardScene_expression_label_3 = {
		57219,
		116,
		True
	},
	backyard_backyardScene_quest_clearButton = {
		57335,
		154,
		True
	},
	backyard_backyardScene_quest_saveFurniture = {
		57489,
		152,
		True
	},
	backyard_backyardScene_restSuccess = {
		57641,
		127,
		True
	},
	backyard_backyardScene_clearSuccess = {
		57768,
		131,
		True
	},
	backyard_backyardScene_name = {
		57899,
		123,
		True
	},
	backyard_backyardScene_exitShipAfterAddEnergy = {
		58022,
		154,
		True
	},
	backyard_backyardScene_showAddExpInfo = {
		58176,
		180,
		True
	},
	backyard_backyardScene_error_noPosPutFurniture = {
		58356,
		137,
		True
	},
	backyard_backyardScene_error_noFurniture = {
		58493,
		146,
		True
	},
	backyard_backyardScene_error_canNotRotate = {
		58639,
		158,
		True
	},
	backyard_backyardShipInfoLayer_quest_openPos = {
		58797,
		160,
		True
	},
	backyard_backyardShipInfoLayer_quest_addShipNoFood = {
		58957,
		182,
		True
	},
	backyard_backyardShipInfoLayer_quest_quickAddEnergy = {
		59139,
		196,
		True
	},
	backyard_backyardShipInfoLayer_error_noQuickItem = {
		59335,
		151,
		True
	},
	backyard_backyardShipInfoMediator_shipState_rest = {
		59486,
		149,
		True
	},
	backyard_backyardShipInfoMediator_shipState_fight = {
		59635,
		150,
		True
	},
	backyard_backyardShipInfoMediator_shipState_study = {
		59785,
		139,
		True
	},
	backyard_backyardShipInfoMediator_shipState_collect = {
		59924,
		146,
		True
	},
	backyard_backyardShipInfoMediator_shipState_event = {
		60070,
		150,
		True
	},
	backyard_backyardShipInfoMediator_quest_moveOutFleet = {
		60220,
		228,
		True
	},
	backyard_backyardShipInfoMediator_error_vanguardFleetOnlyOneShip = {
		60448,
		174,
		True
	},
	backyard_backyardShipInfoMediator_error_mainFleetOnlyOneShip = {
		60622,
		172,
		True
	},
	backyard_backyardShipInfoMediator_ok_addShip = {
		60794,
		119,
		True
	},
	backyard_backyardShipInfoMediator_ok_unlock = {
		60913,
		116,
		True
	},
	backyard_backyardShipInfoMediator_error_noFood = {
		61029,
		140,
		True
	},
	backyard_backyardShipInfoMediator_error_fullEnergy = {
		61169,
		142,
		True
	},
	backyard_backyardShipInfoMediator_error_fleetOnlyOneShip = {
		61311,
		188,
		True
	},
	backyard_open_2floor = {
		61499,
		224,
		True
	},
	backyarad_theme_replace = {
		61723,
		168,
		True
	},
	backyard_extendArea_ok = {
		61891,
		100,
		True
	},
	backyard_extendArea_erro = {
		61991,
		137,
		True
	},
	backyard_extendArea_tip = {
		62128,
		141,
		True
	},
	backyard_notPosition_shipExit = {
		62269,
		131,
		True
	},
	backyard_no_ship_tip = {
		62400,
		104,
		True
	},
	backyard_energy_qiuck_up_tip = {
		62504,
		225,
		True
	},
	backyard_cant_put_tip = {
		62729,
		101,
		True
	},
	backyard_cant_buy_tip = {
		62830,
		104,
		True
	},
	backyard_theme_lock_tip = {
		62934,
		138,
		True
	},
	backyard_theme_open_tip = {
		63072,
		144,
		True
	},
	backyard_theme_furniture_buy_tip = {
		63216,
		272,
		True
	},
	backyard_cannot_repeat_purchase = {
		63488,
		118,
		True
	},
	backyard_theme_bought = {
		63606,
		94,
		True
	},
	backyard_interAction_no_open = {
		63700,
		132,
		True
	},
	backyard_theme_no_exist = {
		63832,
		108,
		True
	},
	backayrd_theme_delete_sucess = {
		63940,
		106,
		True
	},
	backayrd_theme_delete_erro = {
		64046,
		113,
		True
	},
	backyard_ship_on_furniTrue = {
		64159,
		141,
		True
	},
	backyard_save_empty_theme = {
		64300,
		117,
		True
	},
	backyard_theme_name_forbid = {
		64417,
		130,
		True
	},
	backyard_getResource_emptry = {
		64547,
		111,
		True
	},
	backyard_no_pos_for_ship = {
		64658,
		161,
		True
	},
	equipment_destroyEquipments_error_noEquip = {
		64819,
		125,
		True
	},
	equipment_destroyEquipments_error_notEnoughEquip = {
		64944,
		128,
		True
	},
	equipment_equipDevUI_error_noPos = {
		65072,
		122,
		True
	},
	equipment_equipmentInfoLayer_error_canNotEquip = {
		65194,
		153,
		True
	},
	equipment_equipmentScene_selectError_more = {
		65347,
		163,
		True
	},
	equipment_newEquipLayer_getNewEquip = {
		65510,
		140,
		True
	},
	equipment_select_materials_tip = {
		65650,
		95,
		True
	},
	equipment_select_device_tip = {
		65745,
		119,
		True
	},
	equipment_cant_unload = {
		65864,
		159,
		True
	},
	equipment_max_level = {
		66023,
		97,
		True
	},
	equipment_upgrade_costcheck_error = {
		66120,
		164,
		True
	},
	equipment_upgrade_feedback_lack_of_fragment = {
		66284,
		148,
		True
	},
	exercise_count_insufficient = {
		66432,
		147,
		True
	},
	exercise_clear_fleet_tip = {
		66579,
		203,
		True
	},
	exercise_fleet_exit_tip = {
		66782,
		205,
		True
	},
	exercise_replace_rivals_ok_tip = {
		66987,
		112,
		True
	},
	exercise_replace_rivals_question = {
		67099,
		163,
		True
	},
	exercise_count_recover_tip = {
		67262,
		128,
		True
	},
	exercise_shop_refresh_tip = {
		67390,
		152,
		True
	},
	exercise_shop_buy_tip = {
		67542,
		141,
		True
	},
	exercise_formation_title = {
		67683,
		112,
		True
	},
	exercise_time_tip = {
		67795,
		99,
		True
	},
	exercise_rule_tip = {
		67894,
		1371,
		True
	},
	exercise_award_tip = {
		69265,
		190,
		True
	},
	dock_yard_left_tips = {
		69455,
		132,
		True
	},
	fleet_error_no_fleet = {
		69587,
		105,
		True
	},
	fleet_repairShips_error_fullEnergy = {
		69692,
		138,
		True
	},
	fleet_repairShips_error_noResource = {
		69830,
		126,
		True
	},
	fleet_repairShips_quest = {
		69956,
		157,
		True
	},
	fleet_fleetRaname_error = {
		70113,
		105,
		True
	},
	fleet_updateFleet_error = {
		70218,
		111,
		True
	},
	friend_acceptFriendRequest_error = {
		70329,
		130,
		True
	},
	friend_deleteFriend_error = {
		70459,
		114,
		True
	},
	friend_fetchFriendMsg_error = {
		70573,
		119,
		True
	},
	friend_rejectFriendRequest_error = {
		70692,
		130,
		True
	},
	friend_searchFriend_noPlayer = {
		70822,
		120,
		True
	},
	friend_sendFriendMsg_error = {
		70942,
		114,
		True
	},
	friend_sendFriendMsg_error_noFriend = {
		71056,
		137,
		True
	},
	friend_sendFriendRequest_error = {
		71193,
		118,
		True
	},
	friend_addblacklist_error = {
		71311,
		110,
		True
	},
	friend_relieveblacklist_error = {
		71421,
		126,
		True
	},
	friend_sendFriendRequest_success = {
		71547,
		116,
		True
	},
	friend_relieveblacklist_success = {
		71663,
		118,
		True
	},
	friend_addblacklist_success = {
		71781,
		110,
		True
	},
	friend_confirm_add_blacklist = {
		71891,
		199,
		True
	},
	friend_relieve_backlist_tip = {
		72090,
		171,
		True
	},
	friend_player_is_friend_tip = {
		72261,
		133,
		True
	},
	friend_searchFriend_wait_time = {
		72394,
		123,
		True
	},
	lesson_classOver_error = {
		72517,
		113,
		True
	},
	lesson_endToLearn_error = {
		72630,
		101,
		True
	},
	lesson_startToLearn_error = {
		72731,
		112,
		True
	},
	tactics_lesson_cancel = {
		72843,
		227,
		True
	},
	tactics_lesson_system_introduce = {
		73070,
		287,
		True
	},
	tactics_lesson_start_tip = {
		73357,
		243,
		True
	},
	tactics_noskill_erro = {
		73600,
		101,
		True
	},
	tactics_max_level = {
		73701,
		120,
		True
	},
	tactics_end_to_learn = {
		73821,
		206,
		True
	},
	tactics_continue_to_learn = {
		74027,
		127,
		True
	},
	tactics_should_exist_skill = {
		74154,
		107,
		True
	},
	tactics_skill_level_up = {
		74261,
		128,
		True
	},
	tactics_no_lesson = {
		74389,
		100,
		True
	},
	tactics_lesson_full = {
		74489,
		100,
		True
	},
	tactics_lesson_repeated = {
		74589,
		110,
		True
	},
	login_gate_not_ready = {
		74699,
		100,
		True
	},
	login_game_not_ready = {
		74799,
		105,
		True
	},
	login_game_rigister_full = {
		74904,
		128,
		True
	},
	login_game_login_full = {
		75032,
		158,
		True
	},
	login_game_banned = {
		75190,
		130,
		True
	},
	login_game_frequence = {
		75320,
		138,
		True
	},
	login_createNewPlayer_full = {
		75458,
		138,
		True
	},
	login_createNewPlayer_error = {
		75596,
		112,
		True
	},
	login_createNewPlayer_error_nameNull = {
		75708,
		128,
		True
	},
	login_newPlayerScene_word_lingBo = {
		75836,
		179,
		True
	},
	login_newPlayerScene_word_yingHuoChong = {
		76015,
		210,
		True
	},
	login_newPlayerScene_word_laFei = {
		76225,
		200,
		True
	},
	login_newPlayerScene_word_biaoqiang = {
		76425,
		187,
		True
	},
	login_newPlayerScene_word_z23 = {
		76612,
		194,
		True
	},
	login_newPlayerScene_randomName = {
		76806,
		106,
		True
	},
	login_newPlayerScene_error_notChoiseShip = {
		76912,
		125,
		True
	},
	login_newPlayerScene_inputName = {
		77037,
		104,
		True
	},
	login_loginMediator_kickOtherLogin = {
		77141,
		143,
		True
	},
	login_loginMediator_kickServerClose = {
		77284,
		117,
		True
	},
	login_loginMediator_kickIntError = {
		77401,
		109,
		True
	},
	login_loginMediator_kickTimeError = {
		77510,
		118,
		True
	},
	login_loginMediator_vertifyFail = {
		77628,
		118,
		True
	},
	login_loginMediator_dataExpired = {
		77746,
		113,
		True
	},
	login_loginMediator_kickLoginOut = {
		77859,
		112,
		True
	},
	login_loginMediator_serverLoginErro = {
		77971,
		125,
		True
	},
	login_loginMediator_kickUndefined = {
		78096,
		120,
		True
	},
	login_loginMediator_loginSuccess = {
		78216,
		113,
		True
	},
	login_loginMediator_quest_RegisterSuccess = {
		78329,
		151,
		True
	},
	login_loginMediator_registerFail_error = {
		78480,
		123,
		True
	},
	login_loginMediator_userLoginFail_error = {
		78603,
		124,
		True
	},
	login_loginMediator_serverLoginFail_error = {
		78727,
		123,
		True
	},
	login_loginScene_error_noUserName = {
		78850,
		123,
		True
	},
	login_loginScene_error_noPassword = {
		78973,
		123,
		True
	},
	login_loginScene_error_diffPassword = {
		79096,
		122,
		True
	},
	login_loginScene_error_noMailBox = {
		79218,
		119,
		True
	},
	login_loginScene_choiseServer = {
		79337,
		116,
		True
	},
	login_loginScene_server_vindicate = {
		79453,
		125,
		True
	},
	login_loginScene_server_full = {
		79578,
		107,
		True
	},
	login_loginScene_server_disabled = {
		79685,
		108,
		True
	},
	login_register_full = {
		79793,
		111,
		True
	},
	system_database_busy = {
		79904,
		125,
		True
	},
	mail_getMailList_error_noNewMail = {
		80029,
		108,
		True
	},
	mail_takeAttachment_error_noMail = {
		80137,
		119,
		True
	},
	mail_takeAttachment_error_noAttach = {
		80256,
		124,
		True
	},
	mail_takeAttachment_error_noWorld = {
		80380,
		161,
		True
	},
	mail_takeAttachment_error_reWorld = {
		80541,
		205,
		True
	},
	mail_count = {
		80746,
		118,
		True
	},
	mail_takeAttachment_error_magazine_full = {
		80864,
		215,
		True
	},
	mail_takeAttachment_error_dockYrad_full = {
		81079,
		208,
		True
	},
	mail_confirm_set_important_flag = {
		81287,
		112,
		True
	},
	mail_confirm_cancel_important_flag = {
		81399,
		117,
		True
	},
	mail_mail_page = {
		81516,
		82,
		True
	},
	mail_storeroom_page = {
		81598,
		90,
		True
	},
	mail_boxroom_page = {
		81688,
		88,
		True
	},
	mail_all_page = {
		81776,
		80,
		True
	},
	mail_important_page = {
		81856,
		92,
		True
	},
	mail_rare_page = {
		81948,
		85,
		True
	},
	mail_reward_got = {
		82033,
		86,
		True
	},
	mail_reward_tips = {
		82119,
		139,
		True
	},
	mail_boxroom_extend_title = {
		82258,
		103,
		True
	},
	mail_boxroom_extend_tips = {
		82361,
		113,
		True
	},
	mail_buy_button = {
		82474,
		82,
		True
	},
	mail_manager_title = {
		82556,
		93,
		True
	},
	mail_manager_tips_2 = {
		82649,
		142,
		True
	},
	mail_manager_all = {
		82791,
		98,
		True
	},
	mail_manager_rare = {
		82889,
		113,
		True
	},
	mail_get_oneclick = {
		83002,
		92,
		True
	},
	mail_read_oneclick = {
		83094,
		92,
		True
	},
	mail_delete_oneclick = {
		83186,
		96,
		True
	},
	mail_search_new = {
		83282,
		92,
		True
	},
	mail_receive_time = {
		83374,
		92,
		True
	},
	mail_move_oneclick = {
		83466,
		92,
		True
	},
	mail_deleteread_button = {
		83558,
		97,
		True
	},
	mail_manage_button = {
		83655,
		93,
		True
	},
	mail_move_button = {
		83748,
		90,
		True
	},
	mail_delet_button = {
		83838,
		87,
		True
	},
	mail_moveone_button = {
		83925,
		92,
		True
	},
	mail_getone_button = {
		84017,
		95,
		True
	},
	mail_take_all_mail_msgbox = {
		84112,
		147,
		True
	},
	mail_take_maildetail_msgbox = {
		84259,
		103,
		True
	},
	mail_take_canget_msgbox = {
		84362,
		117,
		True
	},
	mail_getbox_title = {
		84479,
		91,
		True
	},
	mail_title_new = {
		84570,
		82,
		True
	},
	mail_boxtitle_information = {
		84652,
		93,
		True
	},
	mail_box_confirm = {
		84745,
		87,
		True
	},
	mail_box_cancel = {
		84832,
		85,
		True
	},
	mail_title_English = {
		84917,
		89,
		True
	},
	mail_toggle_on = {
		85006,
		80,
		True
	},
	mail_toggle_off = {
		85086,
		82,
		True
	},
	main_mailLayer_mailBoxClear = {
		85168,
		115,
		True
	},
	main_mailLayer_noNewMail = {
		85283,
		100,
		True
	},
	main_mailLayer_takeAttach = {
		85383,
		104,
		True
	},
	main_mailLayer_noAttach = {
		85487,
		97,
		True
	},
	main_mailLayer_attachTaken = {
		85584,
		107,
		True
	},
	main_mailLayer_quest_clear = {
		85691,
		207,
		True
	},
	main_mailLayer_quest_clear_choice = {
		85898,
		218,
		True
	},
	main_mailLayer_quest_deleteNotTakeAttach = {
		86116,
		204,
		True
	},
	main_mailLayer_quest_deleteNotRead = {
		86320,
		203,
		True
	},
	main_mailMediator_mailDelete = {
		86523,
		104,
		True
	},
	main_mailMediator_attachTaken = {
		86627,
		110,
		True
	},
	main_mailMediator_mailread = {
		86737,
		121,
		True
	},
	main_mailMediator_mailmove = {
		86858,
		126,
		True
	},
	main_mailMediator_notingToTake = {
		86984,
		115,
		True
	},
	main_mailMediator_takeALot = {
		87099,
		101,
		True
	},
	main_navalAcademyScene_systemClose = {
		87200,
		148,
		True
	},
	main_navalAcademyScene_quest_startClass = {
		87348,
		170,
		True
	},
	main_navalAcademyScene_quest_stopClass = {
		87518,
		248,
		True
	},
	main_navalAcademyScene_quest_Classover_long = {
		87766,
		226,
		True
	},
	main_navalAcademyScene_quest_Classover_short = {
		87992,
		196,
		True
	},
	main_navalAcademyScene_upgrade_complete = {
		88188,
		182,
		True
	},
	main_navalAcademyScene_class_upgrade_complete = {
		88370,
		131,
		True
	},
	main_navalAcademyScene_work_done = {
		88501,
		118,
		True
	},
	main_notificationLayer_searchInput = {
		88619,
		130,
		True
	},
	main_notificationLayer_noInput = {
		88749,
		117,
		True
	},
	main_notificationLayer_noFriend = {
		88866,
		122,
		True
	},
	main_notificationLayer_deleteFriend = {
		88988,
		112,
		True
	},
	main_notificationLayer_sendButton = {
		89100,
		122,
		True
	},
	main_notificationLayer_addFriendError_addSelf = {
		89222,
		136,
		True
	},
	main_notificationLayer_addFriendError_friendAlready = {
		89358,
		156,
		True
	},
	main_notificationLayer_quest_deletFriend = {
		89514,
		163,
		True
	},
	main_notificationLayer_quest_request = {
		89677,
		166,
		True
	},
	main_notificationLayer_enter_room = {
		89843,
		137,
		True
	},
	main_notificationLayer_not_roomId = {
		89980,
		121,
		True
	},
	main_notificationLayer_roomId_invaild = {
		90101,
		124,
		True
	},
	main_notificationMediator_sendFriendRequest = {
		90225,
		127,
		True
	},
	main_notificationMediator_beFriend = {
		90352,
		150,
		True
	},
	main_notificationMediator_deleteFriend = {
		90502,
		160,
		True
	},
	main_notificationMediator_room_max_number = {
		90662,
		122,
		True
	},
	main_playerInfoLayer_inputName = {
		90784,
		104,
		True
	},
	main_playerInfoLayer_inputManifesto = {
		90888,
		123,
		True
	},
	main_playerInfoLayer_quest_changeName = {
		91011,
		159,
		True
	},
	main_playerInfoLayer_error_changeNameNoGem = {
		91170,
		134,
		True
	},
	main_settingsScene_quest_exist = {
		91304,
		126,
		True
	},
	coloring_color_missmatch = {
		91430,
		128,
		True
	},
	coloring_color_not_enough = {
		91558,
		117,
		True
	},
	coloring_erase_all_warning = {
		91675,
		200,
		True
	},
	coloring_erase_warning = {
		91875,
		231,
		True
	},
	coloring_lock = {
		92106,
		83,
		True
	},
	coloring_wait_open = {
		92189,
		91,
		True
	},
	coloring_help_tip = {
		92280,
		1297,
		True
	},
	link_link_help_tip = {
		93577,
		1207,
		True
	},
	player_changeManifesto_ok = {
		94784,
		103,
		True
	},
	player_changeManifesto_error = {
		94887,
		116,
		True
	},
	player_changePlayerIcon_ok = {
		95003,
		108,
		True
	},
	player_changePlayerIcon_error = {
		95111,
		121,
		True
	},
	player_changePlayerName_ok = {
		95232,
		103,
		True
	},
	player_changePlayerName_error = {
		95335,
		116,
		True
	},
	player_changePlayerName_error_2015 = {
		95451,
		136,
		True
	},
	player_harvestResource_error = {
		95587,
		121,
		True
	},
	player_harvestResource_error_fullBag = {
		95708,
		145,
		True
	},
	player_change_chat_room_erro = {
		95853,
		123,
		True
	},
	prop_destroyProp_error_noItem = {
		95976,
		118,
		True
	},
	prop_destroyProp_error_canNotSell = {
		96094,
		123,
		True
	},
	prop_destroyProp_error_notEnoughItem = {
		96217,
		151,
		True
	},
	prop_destroyProp_error = {
		96368,
		108,
		True
	},
	resourceSite_error_noSite = {
		96476,
		118,
		True
	},
	resourceSite_beginScanMap_ok = {
		96594,
		108,
		True
	},
	resourceSite_beginScanMap_error = {
		96702,
		114,
		True
	},
	resourceSite_collectResource_error = {
		96816,
		134,
		True
	},
	resourceSite_finishResourceSite_error = {
		96950,
		133,
		True
	},
	resourceSite_startResourceSite_error = {
		97083,
		134,
		True
	},
	ship_error_noShip = {
		97217,
		133,
		True
	},
	ship_addStarExp_error = {
		97350,
		109,
		True
	},
	ship_buildShip_error = {
		97459,
		106,
		True
	},
	ship_buildShip_error_noTemplate = {
		97565,
		150,
		True
	},
	ship_buildShip_error_notEnoughItem = {
		97715,
		131,
		True
	},
	ship_buildShipImmediately_error = {
		97846,
		115,
		True
	},
	ship_buildShipImmediately_error_noSHip = {
		97961,
		119,
		True
	},
	ship_buildShipImmediately_error_finished = {
		98080,
		126,
		True
	},
	ship_buildShipImmediately_error_noItem = {
		98206,
		138,
		True
	},
	ship_buildShip_not_position = {
		98344,
		143,
		True
	},
	ship_buildBatchShip = {
		98487,
		181,
		True
	},
	ship_buildSingleShip = {
		98668,
		181,
		True
	},
	ship_buildShip_succeed = {
		98849,
		100,
		True
	},
	ship_buildShip_list_empty = {
		98949,
		117,
		True
	},
	ship_buildship_tip = {
		99066,
		191,
		True
	},
	ship_destoryShips_error = {
		99257,
		110,
		True
	},
	ship_equipToShip_ok = {
		99367,
		118,
		True
	},
	ship_equipToShip_error = {
		99485,
		103,
		True
	},
	ship_equipToShip_error_noEquip = {
		99588,
		114,
		True
	},
	ship_equip_check = {
		99702,
		138,
		True
	},
	ship_getShip_error = {
		99840,
		105,
		True
	},
	ship_getShip_error_noShip = {
		99945,
		106,
		True
	},
	ship_getShip_error_notFinish = {
		100051,
		122,
		True
	},
	ship_getShip_error_full = {
		100173,
		153,
		True
	},
	ship_modShip_error = {
		100326,
		106,
		True
	},
	ship_modShip_error_notEnoughGold = {
		100432,
		136,
		True
	},
	ship_remouldShip_error = {
		100568,
		106,
		True
	},
	ship_unequipFromShip_ok = {
		100674,
		126,
		True
	},
	ship_unequipFromShip_error = {
		100800,
		114,
		True
	},
	ship_unequipFromShip_error_noEquip = {
		100914,
		119,
		True
	},
	ship_unequip_all_tip = {
		101033,
		126,
		True
	},
	ship_unequip_all_success = {
		101159,
		127,
		True
	},
	ship_updateShipLock_ok_lock = {
		101286,
		124,
		True
	},
	ship_updateShipLock_ok_unlock = {
		101410,
		128,
		True
	},
	ship_updateShipLock_error = {
		101538,
		119,
		True
	},
	ship_upgradeStar_error = {
		101657,
		106,
		True
	},
	ship_upgradeStar_error_4010 = {
		101763,
		152,
		True
	},
	ship_upgradeStar_error_lvLimit = {
		101915,
		155,
		True
	},
	ship_upgradeStar_error_noEnoughMatrail = {
		102070,
		125,
		True
	},
	ship_upgradeStar_notConfig = {
		102195,
		151,
		True
	},
	ship_upgradeStar_maxLevel = {
		102346,
		121,
		True
	},
	ship_upgradeStar_select_material_tip = {
		102467,
		124,
		True
	},
	ship_exchange_question = {
		102591,
		159,
		True
	},
	ship_exchange_medalCount_noEnough = {
		102750,
		126,
		True
	},
	ship_exchange_erro = {
		102876,
		124,
		True
	},
	ship_exchange_confirm = {
		103000,
		111,
		True
	},
	ship_exchange_tip = {
		103111,
		289,
		True
	},
	ship_vo_fighting = {
		103400,
		120,
		True
	},
	ship_vo_event = {
		103520,
		123,
		True
	},
	ship_vo_isCharacter = {
		103643,
		153,
		True
	},
	ship_vo_inBackyardRest = {
		103796,
		126,
		True
	},
	ship_vo_inClass = {
		103922,
		110,
		True
	},
	ship_vo_moveout_backyard = {
		104032,
		103,
		True
	},
	ship_vo_moveout_formation = {
		104135,
		111,
		True
	},
	ship_vo_mainFleet_must_hasShip = {
		104246,
		146,
		True
	},
	ship_vo_vanguardFleet_must_hasShip = {
		104392,
		148,
		True
	},
	ship_vo_getWordsUndefined = {
		104540,
		142,
		True
	},
	ship_vo_locked = {
		104682,
		98,
		True
	},
	ship_vo_mainFleet_exist_same_ship = {
		104780,
		146,
		True
	},
	ship_vo_vanguardFleet_exist_same_ship = {
		104926,
		148,
		True
	},
	ship_buildShipMediator_startBuild = {
		105074,
		108,
		True
	},
	ship_buildShipMediator_finishBuild = {
		105182,
		120,
		True
	},
	ship_buildShipScene_quest_quickFinish = {
		105302,
		235,
		True
	},
	ship_dockyardMediator_destroy = {
		105537,
		106,
		True
	},
	ship_dockyardScene_capacity = {
		105643,
		105,
		True
	},
	ship_dockyardScene_noRole = {
		105748,
		123,
		True
	},
	ship_dockyardScene_error_choiseRoleMore = {
		105871,
		163,
		True
	},
	ship_dockyardScene_error_choiseRoleLess = {
		106034,
		157,
		True
	},
	ship_formationMediator_leastLimit = {
		106191,
		122,
		True
	},
	ship_formationMediator_changeNameSuccess = {
		106313,
		123,
		True
	},
	ship_formationMediator_changeNameError_sameShip = {
		106436,
		173,
		True
	},
	ship_formationMediator_addShipError_overlimit = {
		106609,
		182,
		True
	},
	ship_formationMediator_replaceError_onlyShip = {
		106791,
		212,
		True
	},
	ship_formationMediator_quest_replace = {
		107003,
		188,
		True
	},
	ship_formationMediaror_trash_warning = {
		107191,
		264,
		True
	},
	ship_formationUI_fleetName1 = {
		107455,
		98,
		True
	},
	ship_formationUI_fleetName2 = {
		107553,
		98,
		True
	},
	ship_formationUI_fleetName3 = {
		107651,
		98,
		True
	},
	ship_formationUI_fleetName4 = {
		107749,
		98,
		True
	},
	ship_formationUI_fleetName5 = {
		107847,
		98,
		True
	},
	ship_formationUI_fleetName6 = {
		107945,
		98,
		True
	},
	ship_formationUI_fleetName11 = {
		108043,
		103,
		True
	},
	ship_formationUI_fleetName12 = {
		108146,
		103,
		True
	},
	ship_formationUI_exercise_fleetName = {
		108249,
		113,
		True
	},
	ship_formationUI_fleetName_world = {
		108362,
		117,
		True
	},
	ship_formationUI_changeFormationError_flag = {
		108479,
		160,
		True
	},
	ship_formationUI_changeFormationError_countError = {
		108639,
		139,
		True
	},
	ship_formationUI_removeError_onlyShip = {
		108778,
		190,
		True
	},
	ship_formationUI_quest_remove = {
		108968,
		152,
		True
	},
	ship_newShipLayer_get = {
		109120,
		147,
		True
	},
	ship_newSkinLayer_get = {
		109267,
		152,
		True
	},
	ship_newSkin_name = {
		109419,
		83,
		True
	},
	ship_shipInfoMediator_destory = {
		109502,
		106,
		True
	},
	ship_shipInfoScene_equipUnlockSlostContent = {
		109608,
		166,
		True
	},
	ship_shipInfoScene_equipUnlockSlostYesText = {
		109774,
		118,
		True
	},
	ship_shipInfoScene_effect = {
		109892,
		132,
		True
	},
	ship_shipInfoScene_effect1or2 = {
		110024,
		134,
		True
	},
	ship_shipInfoScene_modLvMax = {
		110158,
		135,
		True
	},
	ship_shipInfoScene_choiseMod = {
		110293,
		132,
		True
	},
	ship_shipModLayer_effect = {
		110425,
		131,
		True
	},
	ship_shipModLayer_effect1or2 = {
		110556,
		133,
		True
	},
	ship_shipModLayer_modSuccess = {
		110689,
		101,
		True
	},
	ship_mod_no_addition_tip = {
		110790,
		145,
		True
	},
	ship_shipModMediator_choiseMaterial = {
		110935,
		150,
		True
	},
	ship_shipModMediator_noticeLvOver1 = {
		111085,
		111,
		True
	},
	ship_shipModMediator_noticeStarOver4 = {
		111196,
		112,
		True
	},
	ship_shipModMediator_noticeSameButLargerStar = {
		111308,
		131,
		True
	},
	ship_shipModMediator_quest = {
		111439,
		168,
		True
	},
	ship_shipUpgradeLayer2_levelError = {
		111607,
		114,
		True
	},
	ship_shipUpgradeLayer2_noMaterail = {
		111721,
		120,
		True
	},
	ship_shipUpgradeLayer2_ok = {
		111841,
		110,
		True
	},
	ship_shipUpgradeLayer2_effect = {
		111951,
		136,
		True
	},
	ship_shipUpgradeLayer2_effect1or2 = {
		112087,
		138,
		True
	},
	ship_shipUpgradeLayer2_mod_uncommon_tip = {
		112225,
		221,
		True
	},
	ship_shipUpgradeLayer2_uncommon_tip = {
		112446,
		217,
		True
	},
	ship_shipUpgradeLayer2_mod_advanced_tip = {
		112663,
		220,
		True
	},
	ship_shipUpgradeLayer2_advanced_tip = {
		112883,
		222,
		True
	},
	ship_mod_exp_to_attr_tip = {
		113105,
		145,
		True
	},
	ship_max_star = {
		113250,
		144,
		True
	},
	ship_skill_unlock_tip = {
		113394,
		106,
		True
	},
	ship_lock_tip = {
		113500,
		131,
		True
	},
	ship_destroy_uncommon_tip = {
		113631,
		186,
		True
	},
	ship_destroy_advanced_tip = {
		113817,
		162,
		True
	},
	ship_energy_mid_desc = {
		113979,
		132,
		True
	},
	ship_energy_low_desc = {
		114111,
		133,
		True
	},
	ship_energy_low_warn = {
		114244,
		169,
		True
	},
	ship_energy_low_warn_no_exp = {
		114413,
		274,
		True
	},
	test_ship_intensify_tip = {
		114687,
		115,
		True
	},
	test_ship_upgrade_tip = {
		114802,
		126,
		True
	},
	shop_buyItem_ok = {
		114928,
		138,
		True
	},
	shop_buyItem_error = {
		115066,
		102,
		True
	},
	shop_extendMagazine_error = {
		115168,
		115,
		True
	},
	shop_entendShipYard_error = {
		115283,
		112,
		True
	},
	spweapon_attr_effect = {
		115395,
		96,
		True
	},
	spweapon_attr_skillupgrade = {
		115491,
		103,
		True
	},
	spweapon_help_storage = {
		115594,
		3345,
		True
	},
	spweapon_tip_upgrade = {
		118939,
		120,
		True
	},
	spweapon_tip_attr_modify = {
		119059,
		148,
		True
	},
	spweapon_tip_materal_no_enough = {
		119207,
		126,
		True
	},
	spweapon_tip_gold_no_enough = {
		119333,
		119,
		True
	},
	spweapon_tip_pt_no_enough = {
		119452,
		143,
		True
	},
	spweapon_tip_creatept_no_enough = {
		119595,
		180,
		True
	},
	spweapon_tip_bag_no_enough = {
		119775,
		148,
		True
	},
	spweapon_tip_create_sussess = {
		119923,
		151,
		True
	},
	spweapon_tip_group_error = {
		120074,
		125,
		True
	},
	spweapon_tip_breakout_overflow = {
		120199,
		172,
		True
	},
	spweapon_tip_breakout_materal_check = {
		120371,
		144,
		True
	},
	spweapon_tip_transform_materal_check = {
		120515,
		146,
		True
	},
	spweapon_tip_transform_attrmax = {
		120661,
		148,
		True
	},
	spweapon_tip_locked = {
		120809,
		180,
		True
	},
	spweapon_tip_unload = {
		120989,
		135,
		True
	},
	spweapon_tip_sail_locked = {
		121124,
		157,
		True
	},
	spweapon_ui_level = {
		121281,
		94,
		True
	},
	spweapon_ui_levelmax = {
		121375,
		93,
		True
	},
	spweapon_ui_levelmax2 = {
		121468,
		126,
		True
	},
	spweapon_ui_need_resource = {
		121594,
		108,
		True
	},
	spweapon_ui_ptitem = {
		121702,
		96,
		True
	},
	spweapon_ui_spweapon = {
		121798,
		98,
		True
	},
	spweapon_ui_transform = {
		121896,
		105,
		True
	},
	spweapon_ui_transform_attr_text = {
		122001,
		197,
		True
	},
	spweapon_ui_keep_attr = {
		122198,
		93,
		True
	},
	spweapon_ui_change_attr = {
		122291,
		94,
		True
	},
	spweapon_ui_autoselect = {
		122385,
		97,
		True
	},
	spweapon_ui_cancelselect = {
		122482,
		94,
		True
	},
	spweapon_ui_index_shipType_quZhu = {
		122576,
		98,
		True
	},
	spweapon_ui_index_shipType_qinXun = {
		122674,
		99,
		True
	},
	spweapon_ui_index_shipType_zhongXun = {
		122773,
		101,
		True
	},
	spweapon_ui_index_shipType_zhanLie = {
		122874,
		100,
		True
	},
	spweapon_ui_index_shipType_hangMu = {
		122974,
		99,
		True
	},
	spweapon_ui_index_shipType_weiXiu = {
		123073,
		99,
		True
	},
	spweapon_ui_index_shipType_qianTing = {
		123172,
		101,
		True
	},
	spweapon_ui_index_shipType_other = {
		123273,
		100,
		True
	},
	spweapon_ui_keep_attr_text1 = {
		123373,
		206,
		True
	},
	spweapon_ui_keep_attr_text2 = {
		123579,
		150,
		True
	},
	spweapon_ui_change_attr_text1 = {
		123729,
		176,
		True
	},
	spweapon_ui_change_attr_text2 = {
		123905,
		214,
		True
	},
	spweapon_ui_create_exp = {
		124119,
		115,
		True
	},
	spweapon_ui_upgrade_exp = {
		124234,
		118,
		True
	},
	spweapon_ui_breakout_exp = {
		124352,
		117,
		True
	},
	spweapon_ui_create = {
		124469,
		87,
		True
	},
	spweapon_ui_storage = {
		124556,
		88,
		True
	},
	spweapon_ui_empty = {
		124644,
		106,
		True
	},
	spweapon_ui_create_button = {
		124750,
		94,
		True
	},
	spweapon_ui_helptext = {
		124844,
		295,
		True
	},
	spweapon_ui_effect_tag = {
		125139,
		98,
		True
	},
	spweapon_ui_skill_tag = {
		125237,
		98,
		True
	},
	spweapon_activity_ui_text1 = {
		125335,
		174,
		True
	},
	spweapon_activity_ui_text2 = {
		125509,
		165,
		True
	},
	spweapon_tip_skill_locked = {
		125674,
		98,
		True
	},
	spweapon_tip_owned = {
		125772,
		91,
		True
	},
	spweapon_tip_view = {
		125863,
		145,
		True
	},
	spweapon_tip_ship = {
		126008,
		93,
		True
	},
	spweapon_tip_type = {
		126101,
		90,
		True
	},
	stage_beginStage_error = {
		126191,
		109,
		True
	},
	stage_beginStage_error_fleetEmpty = {
		126300,
		120,
		True
	},
	stage_beginStage_error_teamEmpty = {
		126420,
		173,
		True
	},
	stage_beginStage_error_noEnergy = {
		126593,
		143,
		True
	},
	stage_beginStage_error_noResource = {
		126736,
		147,
		True
	},
	stage_beginStage_error_noTicket = {
		126883,
		148,
		True
	},
	stage_finishStage_error = {
		127031,
		115,
		True
	},
	levelScene_map_lock = {
		127146,
		157,
		True
	},
	levelScene_chapter_lock = {
		127303,
		146,
		True
	},
	levelScene_chapter_strategying = {
		127449,
		141,
		True
	},
	levelScene_threat_to_rule_out = {
		127590,
		112,
		True
	},
	levelScene_whether_to_retreat = {
		127702,
		168,
		True
	},
	levelScene_who_to_retreat = {
		127870,
		165,
		True
	},
	levelScene_who_to_exchange = {
		128035,
		138,
		True
	},
	levelScene_time_out = {
		128173,
		104,
		True
	},
	levelScene_nothing = {
		128277,
		103,
		True
	},
	levelScene_notCargo = {
		128380,
		107,
		True
	},
	levelScene_openCargo_erro = {
		128487,
		119,
		True
	},
	levelScene_chapter_notInStrategy = {
		128606,
		114,
		True
	},
	levelScene_retreat_erro = {
		128720,
		105,
		True
	},
	levelScene_strategying = {
		128825,
		100,
		True
	},
	levelScene_tracking_erro = {
		128925,
		94,
		True
	},
	levelScene_tracking_error_3001 = {
		129019,
		150,
		True
	},
	levelScene_chapter_unlock_tip = {
		129169,
		163,
		True
	},
	levelScene_chapter_win = {
		129332,
		116,
		True
	},
	levelScene_sham_win = {
		129448,
		110,
		True
	},
	levelScene_escort_win = {
		129558,
		154,
		True
	},
	levelScene_escort_lose = {
		129712,
		155,
		True
	},
	levelScene_escort_help_tip = {
		129867,
		1412,
		True
	},
	levelScene_escort_retreat = {
		131279,
		225,
		True
	},
	levelScene_oni_retreat = {
		131504,
		204,
		True
	},
	levelScene_oni_win = {
		131708,
		115,
		True
	},
	levelScene_oni_lose = {
		131823,
		123,
		True
	},
	levelScene_bomb_retreat = {
		131946,
		97,
		True
	},
	levelScene_sphunt_help_tip = {
		132043,
		493,
		True
	},
	levelScene_bomb_help_tip = {
		132536,
		341,
		True
	},
	levelScene_chapter_timeout = {
		132877,
		142,
		True
	},
	levelScene_chapter_level_limit = {
		133019,
		162,
		True
	},
	levelScene_chapter_count_tip = {
		133181,
		111,
		True
	},
	levelScene_tracking_error_retry = {
		133292,
		139,
		True
	},
	levelScene_destroy_torpedo = {
		133431,
		123,
		True
	},
	levelScene_new_chapter_coming = {
		133554,
		109,
		True
	},
	levelScene_chapter_open_count_down = {
		133663,
		108,
		True
	},
	levelScene_chapter_not_open = {
		133771,
		103,
		True
	},
	levelScene_activate_remaster = {
		133874,
		194,
		True
	},
	levelScene_remaster_tickets_not_enough = {
		134068,
		136,
		True
	},
	levelScene_remaster_do_not_open = {
		134204,
		121,
		True
	},
	levelScene_remaster_help_tip = {
		134325,
		1192,
		True
	},
	levelScene_activate_loop_mode_failed = {
		135517,
		168,
		True
	},
	levelScene_coastalgun_help_tip = {
		135685,
		359,
		True
	},
	levelScene_select_SP_OP = {
		136044,
		98,
		True
	},
	levelScene_unselect_SP_OP = {
		136142,
		96,
		True
	},
	levelScene_select_SP_OP_reminder = {
		136238,
		415,
		True
	},
	tack_tickets_max_warning = {
		136653,
		281,
		True
	},
	world_battle_count = {
		136934,
		112,
		True
	},
	world_fleetName1 = {
		137046,
		89,
		True
	},
	world_fleetName2 = {
		137135,
		89,
		True
	},
	world_fleetName3 = {
		137224,
		89,
		True
	},
	world_fleetName4 = {
		137313,
		89,
		True
	},
	world_fleetName5 = {
		137402,
		89,
		True
	},
	world_ship_repair_1 = {
		137491,
		162,
		True
	},
	world_ship_repair_2 = {
		137653,
		165,
		True
	},
	world_ship_repair_all = {
		137818,
		168,
		True
	},
	world_ship_repair_no_need = {
		137986,
		111,
		True
	},
	world_event_teleport_alter = {
		138097,
		175,
		True
	},
	world_transport_battle_alter = {
		138272,
		152,
		True
	},
	world_transport_locked = {
		138424,
		200,
		True
	},
	world_target_count = {
		138624,
		105,
		True
	},
	world_target_filter_tip1 = {
		138729,
		91,
		True
	},
	world_target_filter_tip2 = {
		138820,
		98,
		True
	},
	world_target_get_all = {
		138918,
		112,
		True
	},
	world_target_goto = {
		139030,
		92,
		True
	},
	world_help_tip = {
		139122,
		90,
		True
	},
	world_dangerbattle_confirm = {
		139212,
		190,
		True
	},
	world_stamina_exchange = {
		139402,
		177,
		True
	},
	world_stamina_not_enough = {
		139579,
		104,
		True
	},
	world_stamina_recover = {
		139683,
		206,
		True
	},
	world_stamina_text = {
		139889,
		216,
		True
	},
	world_stamina_text2 = {
		140105,
		160,
		True
	},
	world_stamina_resetwarning = {
		140265,
		287,
		True
	},
	world_ship_healthy = {
		140552,
		169,
		True
	},
	world_map_dangerous = {
		140721,
		119,
		True
	},
	world_map_not_open = {
		140840,
		102,
		True
	},
	world_map_locked_stage = {
		140942,
		106,
		True
	},
	world_map_locked_border = {
		141048,
		106,
		True
	},
	world_item_allocate_panel_fleet_info_text = {
		141154,
		163,
		True
	},
	world_redeploy_not_change = {
		141317,
		159,
		True
	},
	world_redeploy_warn = {
		141476,
		187,
		True
	},
	world_redeploy_cost_tip = {
		141663,
		270,
		True
	},
	world_redeploy_tip = {
		141933,
		104,
		True
	},
	world_fleet_choose = {
		142037,
		173,
		True
	},
	world_fleet_formation_not_valid = {
		142210,
		133,
		True
	},
	world_fleet_in_vortex = {
		142343,
		156,
		True
	},
	world_stage_help = {
		142499,
		218,
		True
	},
	world_transport_disable = {
		142717,
		131,
		True
	},
	world_ap = {
		142848,
		74,
		True
	},
	world_resource_tip_1 = {
		142922,
		96,
		True
	},
	world_resource_tip_2 = {
		143018,
		96,
		True
	},
	world_instruction_all_1 = {
		143114,
		127,
		True
	},
	world_instruction_help_1 = {
		143241,
		1467,
		True
	},
	world_instruction_redeploy_1 = {
		144708,
		147,
		True
	},
	world_instruction_redeploy_2 = {
		144855,
		159,
		True
	},
	world_instruction_redeploy_3 = {
		145014,
		166,
		True
	},
	world_instruction_morale_1 = {
		145180,
		187,
		True
	},
	world_instruction_morale_2 = {
		145367,
		120,
		True
	},
	world_instruction_morale_3 = {
		145487,
		113,
		True
	},
	world_instruction_morale_4 = {
		145600,
		160,
		True
	},
	world_instruction_submarine_1 = {
		145760,
		137,
		True
	},
	world_instruction_submarine_2 = {
		145897,
		136,
		True
	},
	world_instruction_submarine_3 = {
		146033,
		135,
		True
	},
	world_instruction_submarine_4 = {
		146168,
		163,
		True
	},
	world_instruction_submarine_5 = {
		146331,
		132,
		True
	},
	world_instruction_submarine_6 = {
		146463,
		209,
		True
	},
	world_instruction_submarine_7 = {
		146672,
		155,
		True
	},
	world_instruction_submarine_8 = {
		146827,
		182,
		True
	},
	world_instruction_submarine_9 = {
		147009,
		190,
		True
	},
	world_instruction_submarine_10 = {
		147199,
		106,
		True
	},
	world_instruction_submarine_11 = {
		147305,
		118,
		True
	},
	world_instruction_detect_1 = {
		147423,
		128,
		True
	},
	world_instruction_detect_2 = {
		147551,
		122,
		True
	},
	world_instruction_supply_1 = {
		147673,
		102,
		True
	},
	world_instruction_supply_2 = {
		147775,
		133,
		True
	},
	world_instruction_port_goods_locked = {
		147908,
		120,
		True
	},
	world_port_inbattle = {
		148028,
		141,
		True
	},
	world_item_recycle_1 = {
		148169,
		151,
		True
	},
	world_item_recycle_2 = {
		148320,
		146,
		True
	},
	world_item_origin = {
		148466,
		132,
		True
	},
	world_shop_bag_unactivated = {
		148598,
		170,
		True
	},
	world_shop_preview_tip = {
		148768,
		119,
		True
	},
	world_shop_init_notice = {
		148887,
		147,
		True
	},
	world_map_title_tips_en = {
		149034,
		101,
		True
	},
	world_map_title_tips = {
		149135,
		99,
		True
	},
	world_mapbuff_attrtxt_1 = {
		149234,
		101,
		True
	},
	world_mapbuff_attrtxt_2 = {
		149335,
		102,
		True
	},
	world_mapbuff_attrtxt_3 = {
		149437,
		107,
		True
	},
	world_mapbuff_compare_txt = {
		149544,
		104,
		True
	},
	world_wind_move = {
		149648,
		171,
		True
	},
	world_battle_pause = {
		149819,
		91,
		True
	},
	world_battle_pause2 = {
		149910,
		99,
		True
	},
	world_task_samemap = {
		150009,
		171,
		True
	},
	world_task_maplock = {
		150180,
		215,
		True
	},
	world_task_goto0 = {
		150395,
		115,
		True
	},
	world_task_goto3 = {
		150510,
		136,
		True
	},
	world_task_view1 = {
		150646,
		99,
		True
	},
	world_task_view2 = {
		150745,
		99,
		True
	},
	world_task_view3 = {
		150844,
		88,
		True
	},
	world_task_refuse1 = {
		150932,
		125,
		True
	},
	world_daily_task_lock = {
		151057,
		148,
		True
	},
	world_daily_task_none = {
		151205,
		117,
		True
	},
	world_daily_task_none_2 = {
		151322,
		87,
		True
	},
	world_sairen_title = {
		151409,
		99,
		True
	},
	world_sairen_description1 = {
		151508,
		131,
		True
	},
	world_sairen_description2 = {
		151639,
		131,
		True
	},
	world_sairen_description3 = {
		151770,
		131,
		True
	},
	world_low_morale = {
		151901,
		241,
		True
	},
	world_recycle_notice = {
		152142,
		142,
		True
	},
	world_recycle_item_transform = {
		152284,
		188,
		True
	},
	world_exit_tip = {
		152472,
		105,
		True
	},
	world_consume_carry_tips = {
		152577,
		100,
		True
	},
	world_boss_help_meta = {
		152677,
		3217,
		True
	},
	world_close = {
		155894,
		120,
		True
	},
	world_catsearch_success = {
		156014,
		139,
		True
	},
	world_catsearch_stop = {
		156153,
		236,
		True
	},
	world_catsearch_fleetcheck = {
		156389,
		240,
		True
	},
	world_catsearch_leavemap = {
		156629,
		242,
		True
	},
	world_catsearch_help_1 = {
		156871,
		315,
		True
	},
	world_catsearch_help_2 = {
		157186,
		105,
		True
	},
	world_catsearch_help_3 = {
		157291,
		278,
		True
	},
	world_catsearch_help_4 = {
		157569,
		100,
		True
	},
	world_catsearch_help_5 = {
		157669,
		144,
		True
	},
	world_catsearch_help_6 = {
		157813,
		125,
		True
	},
	world_level_prefix = {
		157938,
		87,
		True
	},
	world_map_level = {
		158025,
		232,
		True
	},
	world_movelimit_event_text = {
		158257,
		158,
		True
	},
	world_mapbuff_tip = {
		158415,
		127,
		True
	},
	world_sametask_tip = {
		158542,
		152,
		True
	},
	world_expedition_reward_display = {
		158694,
		102,
		True
	},
	world_expedition_reward_display2 = {
		158796,
		102,
		True
	},
	world_complete_item_tip = {
		158898,
		167,
		True
	},
	task_notfound_error = {
		159065,
		149,
		True
	},
	task_submitTask_error = {
		159214,
		111,
		True
	},
	task_submitTask_error_client = {
		159325,
		118,
		True
	},
	task_submitTask_error_notFinish = {
		159443,
		136,
		True
	},
	task_taskMediator_getItem = {
		159579,
		158,
		True
	},
	task_taskMediator_getResource = {
		159737,
		166,
		True
	},
	task_taskMediator_getEquip = {
		159903,
		158,
		True
	},
	task_target_chapter_in_progress = {
		160061,
		178,
		True
	},
	task_level_notenough = {
		160239,
		119,
		True
	},
	loading_tip_ShaderMgr = {
		160358,
		105,
		True
	},
	loading_tip_FontMgr = {
		160463,
		100,
		True
	},
	loading_tip_TipsMgr = {
		160563,
		102,
		True
	},
	loading_tip_MsgboxMgr = {
		160665,
		103,
		True
	},
	loading_tip_GuideMgr = {
		160768,
		111,
		True
	},
	loading_tip_PoolMgr = {
		160879,
		98,
		True
	},
	loading_tip_FModMgr = {
		160977,
		98,
		True
	},
	loading_tip_StoryMgr = {
		161075,
		102,
		True
	},
	energy_desc_happy = {
		161177,
		136,
		True
	},
	energy_desc_normal = {
		161313,
		148,
		True
	},
	energy_desc_tired = {
		161461,
		139,
		True
	},
	energy_desc_angry = {
		161600,
		121,
		True
	},
	create_player_success = {
		161721,
		103,
		True
	},
	login_newPlayerScene_invalideName = {
		161824,
		141,
		True
	},
	login_newPlayerScene_name_tooShort = {
		161965,
		116,
		True
	},
	login_newPlayerScene_name_existOtherChar = {
		162081,
		140,
		True
	},
	login_newPlayerScene_name_tooLong = {
		162221,
		114,
		True
	},
	equipment_updateGrade_tip = {
		162335,
		143,
		True
	},
	equipment_upgrade_ok = {
		162478,
		98,
		True
	},
	equipment_cant_upgrade = {
		162576,
		113,
		True
	},
	equipment_upgrade_erro = {
		162689,
		111,
		True
	},
	collection_nostar = {
		162800,
		98,
		True
	},
	collection_getResource_error = {
		162898,
		119,
		True
	},
	collection_hadAward = {
		163017,
		109,
		True
	},
	collection_lock = {
		163126,
		85,
		True
	},
	collection_fetched = {
		163211,
		114,
		True
	},
	buyProp_noResource_error = {
		163325,
		137,
		True
	},
	refresh_shopStreet_ok = {
		163462,
		109,
		True
	},
	refresh_shopStreet_erro = {
		163571,
		114,
		True
	},
	shopStreet_upgrade_done = {
		163685,
		103,
		True
	},
	shopStreet_refresh_max_count = {
		163788,
		122,
		True
	},
	buy_countLimit = {
		163910,
		105,
		True
	},
	buy_item_quest = {
		164015,
		117,
		True
	},
	refresh_shopStreet_question = {
		164132,
		276,
		True
	},
	quota_shop_title = {
		164408,
		96,
		True
	},
	quota_shop_description = {
		164504,
		183,
		True
	},
	quota_shop_owned = {
		164687,
		85,
		True
	},
	quota_shop_good_limit = {
		164772,
		98,
		True
	},
	quota_shop_limit_error = {
		164870,
		145,
		True
	},
	event_start_success = {
		165015,
		104,
		True
	},
	event_start_fail = {
		165119,
		107,
		True
	},
	event_finish_success = {
		165226,
		104,
		True
	},
	event_finish_fail = {
		165330,
		111,
		True
	},
	event_giveup_success = {
		165441,
		114,
		True
	},
	event_giveup_fail = {
		165555,
		110,
		True
	},
	event_flush_success = {
		165665,
		107,
		True
	},
	event_flush_fail = {
		165772,
		107,
		True
	},
	event_flush_not_enough = {
		165879,
		110,
		True
	},
	event_start = {
		165989,
		80,
		True
	},
	event_finish = {
		166069,
		84,
		True
	},
	event_giveup = {
		166153,
		82,
		True
	},
	event_minimus_ship_numbers = {
		166235,
		184,
		True
	},
	event_confirm_giveup = {
		166419,
		131,
		True
	},
	event_confirm_flush = {
		166550,
		172,
		True
	},
	event_fleet_busy = {
		166722,
		146,
		True
	},
	event_same_type_not_allowed = {
		166868,
		127,
		True
	},
	event_condition_ship_level = {
		166995,
		165,
		True
	},
	event_condition_ship_count = {
		167160,
		145,
		True
	},
	event_condition_ship_type = {
		167305,
		119,
		True
	},
	event_level_unreached = {
		167424,
		108,
		True
	},
	event_type_unreached = {
		167532,
		119,
		True
	},
	event_oil_consume = {
		167651,
		168,
		True
	},
	event_type_unlimit = {
		167819,
		90,
		True
	},
	dailyLevel_restCount_notEnough = {
		167909,
		133,
		True
	},
	dailyLevel_unopened = {
		168042,
		91,
		True
	},
	dailyLevel_opened = {
		168133,
		85,
		True
	},
	playerinfo_ship_is_already_flagship = {
		168218,
		128,
		True
	},
	playerinfo_mask_word = {
		168346,
		107,
		True
	},
	just_now = {
		168453,
		80,
		True
	},
	several_minutes_before = {
		168533,
		116,
		True
	},
	several_hours_before = {
		168649,
		115,
		True
	},
	several_days_before = {
		168764,
		113,
		True
	},
	long_time_offline = {
		168877,
		89,
		True
	},
	dont_send_message_frequently = {
		168966,
		114,
		True
	},
	no_activity = {
		169080,
		95,
		True
	},
	which_day = {
		169175,
		102,
		True
	},
	which_day_2 = {
		169277,
		81,
		True
	},
	invalidate_evaluation = {
		169358,
		118,
		True
	},
	chapter_no = {
		169476,
		107,
		True
	},
	reconnect_tip = {
		169583,
		123,
		True
	},
	like_ship_success = {
		169706,
		97,
		True
	},
	eva_ship_success = {
		169803,
		98,
		True
	},
	zan_ship_eva_success = {
		169901,
		100,
		True
	},
	zan_ship_eva_error_7 = {
		170001,
		121,
		True
	},
	eva_count_limit = {
		170122,
		119,
		True
	},
	attribute_durability = {
		170241,
		86,
		True
	},
	attribute_cannon = {
		170327,
		83,
		True
	},
	attribute_torpedo = {
		170410,
		85,
		True
	},
	attribute_antiaircraft = {
		170495,
		89,
		True
	},
	attribute_air = {
		170584,
		81,
		True
	},
	attribute_reload = {
		170665,
		84,
		True
	},
	attribute_cd = {
		170749,
		79,
		True
	},
	attribute_armor_type = {
		170828,
		94,
		True
	},
	attribute_armor = {
		170922,
		84,
		True
	},
	attribute_hit = {
		171006,
		80,
		True
	},
	attribute_speed = {
		171086,
		84,
		True
	},
	attribute_luck = {
		171170,
		82,
		True
	},
	attribute_dodge = {
		171252,
		83,
		True
	},
	attribute_expend = {
		171335,
		84,
		True
	},
	attribute_damage = {
		171419,
		83,
		True
	},
	attribute_healthy = {
		171502,
		88,
		True
	},
	attribute_speciality = {
		171590,
		91,
		True
	},
	attribute_range = {
		171681,
		84,
		True
	},
	attribute_angle = {
		171765,
		91,
		True
	},
	attribute_scatter = {
		171856,
		93,
		True
	},
	attribute_ammo = {
		171949,
		82,
		True
	},
	attribute_antisub = {
		172031,
		85,
		True
	},
	attribute_sonarRange = {
		172116,
		88,
		True
	},
	attribute_sonarInterval = {
		172204,
		92,
		True
	},
	attribute_oxy_max = {
		172296,
		85,
		True
	},
	attribute_dodge_limit = {
		172381,
		99,
		True
	},
	attribute_intimacy = {
		172480,
		90,
		True
	},
	attribute_max_distance_damage = {
		172570,
		111,
		True
	},
	attribute_anti_siren = {
		172681,
		101,
		True
	},
	attribute_add_new = {
		172782,
		85,
		True
	},
	skill = {
		172867,
		75,
		True
	},
	cd_normal = {
		172942,
		75,
		True
	},
	intensify = {
		173017,
		80,
		True
	},
	change = {
		173097,
		76,
		True
	},
	formation_switch_failed = {
		173173,
		111,
		True
	},
	formation_switch_success = {
		173284,
		102,
		True
	},
	formation_switch_tip = {
		173386,
		161,
		True
	},
	formation_reform_tip = {
		173547,
		145,
		True
	},
	formation_invalide = {
		173692,
		120,
		True
	},
	chapter_ap_not_enough = {
		173812,
		110,
		True
	},
	formation_forbid_when_in_chapter = {
		173922,
		159,
		True
	},
	military_forbid_when_in_chapter = {
		174081,
		158,
		True
	},
	confirm_app_exit = {
		174239,
		119,
		True
	},
	friend_info_page_tip = {
		174358,
		109,
		True
	},
	friend_search_page_tip = {
		174467,
		135,
		True
	},
	friend_request_page_tip = {
		174602,
		152,
		True
	},
	friend_id_copy_ok = {
		174754,
		106,
		True
	},
	friend_inpout_key_tip = {
		174860,
		106,
		True
	},
	remove_friend_tip = {
		174966,
		126,
		True
	},
	friend_request_msg_placeholder = {
		175092,
		109,
		True
	},
	friend_request_msg_title = {
		175201,
		105,
		True
	},
	friend_max_count = {
		175306,
		147,
		True
	},
	friend_add_ok = {
		175453,
		90,
		True
	},
	friend_max_count_1 = {
		175543,
		117,
		True
	},
	friend_no_request = {
		175660,
		99,
		True
	},
	reject_all_friend_ok = {
		175759,
		113,
		True
	},
	reject_friend_ok = {
		175872,
		104,
		True
	},
	friend_offline = {
		175976,
		96,
		True
	},
	friend_msg_forbid = {
		176072,
		151,
		True
	},
	dont_add_self = {
		176223,
		114,
		True
	},
	friend_already_add = {
		176337,
		122,
		True
	},
	friend_not_add = {
		176459,
		114,
		True
	},
	friend_send_msg_erro_tip = {
		176573,
		131,
		True
	},
	friend_send_msg_null_tip = {
		176704,
		111,
		True
	},
	friend_search_succeed = {
		176815,
		101,
		True
	},
	friend_request_msg_sent = {
		176916,
		100,
		True
	},
	friend_resume_ship_count = {
		177016,
		100,
		True
	},
	friend_resume_title_metal = {
		177116,
		103,
		True
	},
	friend_resume_collection_rate = {
		177219,
		104,
		True
	},
	friend_resume_attack_count = {
		177323,
		99,
		True
	},
	friend_resume_attack_win_rate = {
		177422,
		100,
		True
	},
	friend_resume_manoeuvre_count = {
		177522,
		104,
		True
	},
	friend_resume_manoeuvre_win_rate = {
		177626,
		104,
		True
	},
	friend_resume_fleet_gs = {
		177730,
		98,
		True
	},
	friend_event_count = {
		177828,
		95,
		True
	},
	firend_relieve_blacklist_ok = {
		177923,
		99,
		True
	},
	firend_relieve_blacklist_tip = {
		178022,
		148,
		True
	},
	word_shipNation_all = {
		178170,
		95,
		True
	},
	word_shipNation_baiYing = {
		178265,
		98,
		True
	},
	word_shipNation_huangJia = {
		178363,
		98,
		True
	},
	word_shipNation_chongYing = {
		178461,
		102,
		True
	},
	word_shipNation_tieXue = {
		178563,
		96,
		True
	},
	word_shipNation_dongHuang = {
		178659,
		102,
		True
	},
	word_shipNation_saDing = {
		178761,
		103,
		True
	},
	word_shipNation_beiLian = {
		178864,
		106,
		True
	},
	word_shipNation_other = {
		178970,
		89,
		True
	},
	word_shipNation_np = {
		179059,
		89,
		True
	},
	word_shipNation_ziyou = {
		179148,
		95,
		True
	},
	word_shipNation_weixi = {
		179243,
		100,
		True
	},
	word_shipNation_yuanwei = {
		179343,
		101,
		True
	},
	word_shipNation_bili = {
		179444,
		96,
		True
	},
	word_shipNation_um = {
		179540,
		96,
		True
	},
	word_shipNation_ai = {
		179636,
		90,
		True
	},
	word_shipNation_holo = {
		179726,
		92,
		True
	},
	word_shipNation_doa = {
		179818,
		98,
		True
	},
	word_shipNation_imas = {
		179916,
		99,
		True
	},
	word_shipNation_link = {
		180015,
		91,
		True
	},
	word_shipNation_ssss = {
		180106,
		88,
		True
	},
	word_shipNation_mot = {
		180194,
		91,
		True
	},
	word_shipNation_ryza = {
		180285,
		96,
		True
	},
	word_shipNation_meta_index = {
		180381,
		94,
		True
	},
	word_shipNation_senran = {
		180475,
		99,
		True
	},
	word_reset = {
		180574,
		79,
		True
	},
	word_asc = {
		180653,
		81,
		True
	},
	word_desc = {
		180734,
		83,
		True
	},
	word_own = {
		180817,
		78,
		True
	},
	word_own1 = {
		180895,
		79,
		True
	},
	oil_buy_limit_tip = {
		180974,
		150,
		True
	},
	friend_resume_title = {
		181124,
		89,
		True
	},
	friend_resume_data_title = {
		181213,
		92,
		True
	},
	batch_destroy = {
		181305,
		90,
		True
	},
	equipment_select_device_destroy_tip = {
		181395,
		123,
		True
	},
	equipment_select_device_destroy_bonus_tip = {
		181518,
		120,
		True
	},
	equipment_select_device_destroy_nobonus_tip = {
		181638,
		119,
		True
	},
	ship_equip_profiiency = {
		181757,
		100,
		True
	},
	no_open_system_tip = {
		181857,
		165,
		True
	},
	open_system_tip = {
		182022,
		98,
		True
	},
	charge_start_tip = {
		182120,
		102,
		True
	},
	charge_double_gem_tip = {
		182222,
		104,
		True
	},
	charge_month_card_lefttime_tip = {
		182326,
		122,
		True
	},
	charge_title = {
		182448,
		98,
		True
	},
	charge_extra_gem_tip = {
		182546,
		103,
		True
	},
	charge_month_card_title = {
		182649,
		143,
		True
	},
	charge_items_title = {
		182792,
		96,
		True
	},
	setting_interface_save_success = {
		182888,
		116,
		True
	},
	setting_interface_revert_check = {
		183004,
		148,
		True
	},
	setting_interface_cancel_check = {
		183152,
		115,
		True
	},
	event_special_update = {
		183267,
		106,
		True
	},
	no_notice_tip = {
		183373,
		116,
		True
	},
	energy_desc_1 = {
		183489,
		165,
		True
	},
	energy_desc_2 = {
		183654,
		134,
		True
	},
	energy_desc_3 = {
		183788,
		115,
		True
	},
	energy_desc_4 = {
		183903,
		148,
		True
	},
	intimacy_desc_1 = {
		184051,
		100,
		True
	},
	intimacy_desc_2 = {
		184151,
		107,
		True
	},
	intimacy_desc_3 = {
		184258,
		120,
		True
	},
	intimacy_desc_4 = {
		184378,
		124,
		True
	},
	intimacy_desc_5 = {
		184502,
		118,
		True
	},
	intimacy_desc_6 = {
		184620,
		120,
		True
	},
	intimacy_desc_7 = {
		184740,
		120,
		True
	},
	intimacy_desc_1_buff = {
		184860,
		102,
		True
	},
	intimacy_desc_2_buff = {
		184962,
		102,
		True
	},
	intimacy_desc_3_buff = {
		185064,
		141,
		True
	},
	intimacy_desc_4_buff = {
		185205,
		141,
		True
	},
	intimacy_desc_5_buff = {
		185346,
		141,
		True
	},
	intimacy_desc_6_buff = {
		185487,
		141,
		True
	},
	intimacy_desc_7_buff = {
		185628,
		142,
		True
	},
	intimacy_desc_propose = {
		185770,
		323,
		True
	},
	intimacy_desc_1_detail = {
		186093,
		157,
		True
	},
	intimacy_desc_2_detail = {
		186250,
		164,
		True
	},
	intimacy_desc_3_detail = {
		186414,
		196,
		True
	},
	intimacy_desc_4_detail = {
		186610,
		200,
		True
	},
	intimacy_desc_5_detail = {
		186810,
		194,
		True
	},
	intimacy_desc_6_detail = {
		187004,
		324,
		True
	},
	intimacy_desc_7_detail = {
		187328,
		324,
		True
	},
	intimacy_desc_ring = {
		187652,
		96,
		True
	},
	intimacy_desc_tiara = {
		187748,
		96,
		True
	},
	intimacy_desc_day = {
		187844,
		81,
		True
	},
	word_propose_cost_tip1 = {
		187925,
		340,
		True
	},
	word_propose_cost_tip2 = {
		188265,
		318,
		True
	},
	word_propose_tiara_tip = {
		188583,
		153,
		True
	},
	charge_title_getitem = {
		188736,
		117,
		True
	},
	charge_title_getitem_soon = {
		188853,
		113,
		True
	},
	charge_title_getitem_month = {
		188966,
		120,
		True
	},
	charge_limit_all = {
		189086,
		96,
		True
	},
	charge_limit_daily = {
		189182,
		101,
		True
	},
	charge_limit_weekly = {
		189283,
		106,
		True
	},
	charge_limit_monthly = {
		189389,
		108,
		True
	},
	charge_error = {
		189497,
		92,
		True
	},
	charge_success = {
		189589,
		89,
		True
	},
	charge_level_limit = {
		189678,
		99,
		True
	},
	ship_drop_desc_default = {
		189777,
		101,
		True
	},
	charge_limit_lv = {
		189878,
		93,
		True
	},
	charge_time_out = {
		189971,
		144,
		True
	},
	help_shipinfo_equip = {
		190115,
		628,
		True
	},
	help_shipinfo_detail = {
		190743,
		679,
		True
	},
	help_shipinfo_intensify = {
		191422,
		632,
		True
	},
	help_shipinfo_upgrate = {
		192054,
		630,
		True
	},
	help_shipinfo_maxlevel = {
		192684,
		631,
		True
	},
	help_shipinfo_actnpc = {
		193315,
		1323,
		True
	},
	help_backyard = {
		194638,
		590,
		True
	},
	help_shipinfo_fashion = {
		195228,
		168,
		True
	},
	help_shipinfo_attr = {
		195396,
		3706,
		True
	},
	help_equipment = {
		199102,
		1884,
		True
	},
	help_equipment_skin = {
		200986,
		912,
		True
	},
	help_daily_task = {
		201898,
		3705,
		True
	},
	help_build = {
		205603,
		281,
		True
	},
	help_build_1 = {
		205884,
		551,
		True
	},
	help_build_2 = {
		206435,
		283,
		True
	},
	help_build_4 = {
		206718,
		573,
		True
	},
	help_build_5 = {
		207291,
		792,
		True
	},
	help_shipinfo_hunting = {
		208083,
		1244,
		True
	},
	shop_extendship_success = {
		209327,
		101,
		True
	},
	shop_extendequip_success = {
		209428,
		110,
		True
	},
	shop_spweapon_success = {
		209538,
		137,
		True
	},
	naval_academy_res_desc_cateen = {
		209675,
		240,
		True
	},
	naval_academy_res_desc_shop = {
		209915,
		211,
		True
	},
	naval_academy_res_desc_class = {
		210126,
		270,
		True
	},
	number_1 = {
		210396,
		73,
		True
	},
	number_2 = {
		210469,
		73,
		True
	},
	number_3 = {
		210542,
		73,
		True
	},
	number_4 = {
		210615,
		73,
		True
	},
	number_5 = {
		210688,
		73,
		True
	},
	number_6 = {
		210761,
		73,
		True
	},
	number_7 = {
		210834,
		73,
		True
	},
	number_8 = {
		210907,
		73,
		True
	},
	number_9 = {
		210980,
		73,
		True
	},
	number_10 = {
		211053,
		75,
		True
	},
	military_shop_no_open_tip = {
		211128,
		188,
		True
	},
	switch_to_shop_tip_1 = {
		211316,
		149,
		True
	},
	switch_to_shop_tip_2 = {
		211465,
		142,
		True
	},
	switch_to_shop_tip_3 = {
		211607,
		127,
		True
	},
	switch_to_shop_tip_noPos = {
		211734,
		123,
		True
	},
	text_noPos_clear = {
		211857,
		84,
		True
	},
	text_noPos_buy = {
		211941,
		84,
		True
	},
	text_noPos_intensify = {
		212025,
		92,
		True
	},
	switch_to_shop_tip_noDockyard = {
		212117,
		125,
		True
	},
	commission_no_open = {
		212242,
		83,
		True
	},
	commission_open_tip = {
		212325,
		107,
		True
	},
	commission_idle = {
		212432,
		86,
		True
	},
	commission_urgency = {
		212518,
		101,
		True
	},
	commission_normal = {
		212619,
		93,
		True
	},
	commission_get_award = {
		212712,
		109,
		True
	},
	activity_build_end_tip = {
		212821,
		127,
		True
	},
	event_over_time_expired = {
		212948,
		106,
		True
	},
	mail_sender_default = {
		213054,
		95,
		True
	},
	exchangecode_title = {
		213149,
		95,
		True
	},
	exchangecode_use_placeholder = {
		213244,
		116,
		True
	},
	exchangecode_use_ok = {
		213360,
		132,
		True
	},
	exchangecode_use_error = {
		213492,
		110,
		True
	},
	exchangecode_use_error_3 = {
		213602,
		105,
		True
	},
	exchangecode_use_error_6 = {
		213707,
		122,
		True
	},
	exchangecode_use_error_7 = {
		213829,
		115,
		True
	},
	exchangecode_use_error_8 = {
		213944,
		108,
		True
	},
	exchangecode_use_error_9 = {
		214052,
		108,
		True
	},
	exchangecode_use_error_16 = {
		214160,
		108,
		True
	},
	exchangecode_use_error_20 = {
		214268,
		109,
		True
	},
	text_noRes_tip = {
		214377,
		92,
		True
	},
	text_noRes_info_tip = {
		214469,
		111,
		True
	},
	text_noRes_info_tip_link = {
		214580,
		93,
		True
	},
	text_noRes_info_tip2 = {
		214673,
		137,
		True
	},
	text_shop_noRes_tip = {
		214810,
		112,
		True
	},
	text_shop_enoughRes_tip = {
		214922,
		128,
		True
	},
	text_buy_fashion_tip = {
		215050,
		108,
		True
	},
	equip_part_title = {
		215158,
		83,
		True
	},
	equip_part_main_title = {
		215241,
		95,
		True
	},
	equip_part_sub_title = {
		215336,
		99,
		True
	},
	equipment_upgrade_overlimit = {
		215435,
		133,
		True
	},
	err_name_existOtherChar = {
		215568,
		117,
		True
	},
	help_battle_rule = {
		215685,
		511,
		True
	},
	help_battle_warspite = {
		216196,
		300,
		True
	},
	help_battle_defense = {
		216496,
		588,
		True
	},
	backyard_theme_set_tip = {
		217084,
		147,
		True
	},
	backyard_theme_save_tip = {
		217231,
		172,
		True
	},
	backyard_theme_defaultname = {
		217403,
		102,
		True
	},
	backyard_rename_success = {
		217505,
		105,
		True
	},
	ship_set_skin_success = {
		217610,
		98,
		True
	},
	ship_set_skin_error = {
		217708,
		107,
		True
	},
	equip_part_tip = {
		217815,
		109,
		True
	},
	help_battle_auto = {
		217924,
		334,
		True
	},
	gold_buy_tip = {
		218258,
		247,
		True
	},
	oil_buy_tip = {
		218505,
		387,
		True
	},
	text_iknow = {
		218892,
		80,
		True
	},
	help_oil_buy_limit = {
		218972,
		299,
		True
	},
	text_nofood_yes = {
		219271,
		88,
		True
	},
	text_nofood_no = {
		219359,
		84,
		True
	},
	tip_add_task = {
		219443,
		91,
		True
	},
	collection_award_ship = {
		219534,
		134,
		True
	},
	guild_create_sucess = {
		219668,
		97,
		True
	},
	guild_create_error = {
		219765,
		105,
		True
	},
	guild_create_error_noname = {
		219870,
		117,
		True
	},
	guild_create_error_nofaction = {
		219987,
		131,
		True
	},
	guild_create_error_nopolicy = {
		220118,
		121,
		True
	},
	guild_create_error_nomanifesto = {
		220239,
		123,
		True
	},
	guild_create_error_nomoney = {
		220362,
		117,
		True
	},
	guild_tip_dissolve = {
		220479,
		347,
		True
	},
	guild_tip_quit = {
		220826,
		119,
		True
	},
	guild_create_confirm = {
		220945,
		144,
		True
	},
	guild_apply_erro = {
		221089,
		113,
		True
	},
	guild_dissolve_erro = {
		221202,
		108,
		True
	},
	guild_fire_erro = {
		221310,
		107,
		True
	},
	guild_impeach_erro = {
		221417,
		114,
		True
	},
	guild_quit_erro = {
		221531,
		101,
		True
	},
	guild_accept_erro = {
		221632,
		110,
		True
	},
	guild_reject_erro = {
		221742,
		110,
		True
	},
	guild_modify_erro = {
		221852,
		103,
		True
	},
	guild_setduty_erro = {
		221955,
		106,
		True
	},
	guild_apply_sucess = {
		222061,
		108,
		True
	},
	guild_no_exist = {
		222169,
		99,
		True
	},
	guild_dissolve_sucess = {
		222268,
		110,
		True
	},
	guild_commder_in_impeach_time = {
		222378,
		126,
		True
	},
	guild_impeach_sucess = {
		222504,
		107,
		True
	},
	guild_quit_sucess = {
		222611,
		105,
		True
	},
	guild_member_max_count = {
		222716,
		104,
		True
	},
	guild_new_member_join = {
		222820,
		119,
		True
	},
	guild_player_in_cd_time = {
		222939,
		185,
		True
	},
	guild_player_already_join = {
		223124,
		123,
		True
	},
	guild_rejecet_apply_sucess = {
		223247,
		111,
		True
	},
	guild_should_input_keyword = {
		223358,
		117,
		True
	},
	guild_search_sucess = {
		223475,
		99,
		True
	},
	guild_list_refresh_sucess = {
		223574,
		123,
		True
	},
	guild_info_update = {
		223697,
		100,
		True
	},
	guild_duty_id_is_null = {
		223797,
		108,
		True
	},
	guild_player_is_null = {
		223905,
		109,
		True
	},
	guild_duty_commder_max_count = {
		224014,
		126,
		True
	},
	guild_set_duty_sucess = {
		224140,
		107,
		True
	},
	guild_policy_power = {
		224247,
		86,
		True
	},
	guild_policy_relax = {
		224333,
		88,
		True
	},
	guild_faction_blhx = {
		224421,
		91,
		True
	},
	guild_faction_cszz = {
		224512,
		94,
		True
	},
	guild_faction_unknown = {
		224606,
		89,
		True
	},
	guild_faction_meta = {
		224695,
		86,
		True
	},
	guild_word_commder = {
		224781,
		89,
		True
	},
	guild_word_deputy_commder = {
		224870,
		101,
		True
	},
	guild_word_picked = {
		224971,
		86,
		True
	},
	guild_word_ordinary = {
		225057,
		89,
		True
	},
	guild_word_home = {
		225146,
		83,
		True
	},
	guild_word_member = {
		225229,
		88,
		True
	},
	guild_word_apply = {
		225317,
		85,
		True
	},
	guild_faction_change_tip = {
		225402,
		197,
		True
	},
	guild_msg_is_null = {
		225599,
		111,
		True
	},
	guild_log_new_guild_join = {
		225710,
		192,
		True
	},
	guild_log_duty_change = {
		225902,
		178,
		True
	},
	guild_log_quit = {
		226080,
		180,
		True
	},
	guild_log_fire = {
		226260,
		187,
		True
	},
	guild_leave_cd_time = {
		226447,
		148,
		True
	},
	guild_sort_time = {
		226595,
		83,
		True
	},
	guild_sort_level = {
		226678,
		83,
		True
	},
	guild_sort_duty = {
		226761,
		83,
		True
	},
	guild_fire_tip = {
		226844,
		120,
		True
	},
	guild_impeach_tip = {
		226964,
		126,
		True
	},
	guild_set_duty_title = {
		227090,
		99,
		True
	},
	guild_search_list_max_count = {
		227189,
		107,
		True
	},
	guild_sort_all = {
		227296,
		81,
		True
	},
	guild_sort_blhx = {
		227377,
		88,
		True
	},
	guild_sort_cszz = {
		227465,
		91,
		True
	},
	guild_sort_power = {
		227556,
		84,
		True
	},
	guild_sort_relax = {
		227640,
		86,
		True
	},
	guild_join_cd = {
		227726,
		142,
		True
	},
	guild_name_invaild = {
		227868,
		110,
		True
	},
	guild_apply_full = {
		227978,
		117,
		True
	},
	guild_member_full = {
		228095,
		101,
		True
	},
	guild_fire_duty_limit = {
		228196,
		142,
		True
	},
	guild_fire_succeed = {
		228338,
		89,
		True
	},
	guild_duty_tip_1 = {
		228427,
		115,
		True
	},
	guild_duty_tip_2 = {
		228542,
		116,
		True
	},
	battle_repair_special_tip = {
		228658,
		168,
		True
	},
	battle_repair_normal_name = {
		228826,
		109,
		True
	},
	battle_repair_special_name = {
		228935,
		111,
		True
	},
	oil_max_tip_title = {
		229046,
		110,
		True
	},
	gold_max_tip_title = {
		229156,
		113,
		True
	},
	expbook_max_tip_title = {
		229269,
		121,
		True
	},
	resource_max_tip_shop = {
		229390,
		108,
		True
	},
	resource_max_tip_event = {
		229498,
		122,
		True
	},
	resource_max_tip_battle = {
		229620,
		162,
		True
	},
	resource_max_tip_collect = {
		229782,
		124,
		True
	},
	resource_max_tip_mail = {
		229906,
		121,
		True
	},
	resource_max_tip_eventstart = {
		230027,
		118,
		True
	},
	resource_max_tip_destroy = {
		230145,
		111,
		True
	},
	resource_max_tip_retire = {
		230256,
		104,
		True
	},
	resource_max_tip_retire_1 = {
		230360,
		163,
		True
	},
	new_version_tip = {
		230523,
		165,
		True
	},
	guild_request_msg_title = {
		230688,
		115,
		True
	},
	guild_request_msg_placeholder = {
		230803,
		147,
		True
	},
	ship_upgrade_unequip_tip = {
		230950,
		223,
		True
	},
	destination_can_not_reach = {
		231173,
		121,
		True
	},
	destination_can_not_reach_safety = {
		231294,
		136,
		True
	},
	destination_not_in_range = {
		231430,
		123,
		True
	},
	level_ammo_enough = {
		231553,
		146,
		True
	},
	level_ammo_supply = {
		231699,
		120,
		True
	},
	level_ammo_empty = {
		231819,
		132,
		True
	},
	level_ammo_supply_p1 = {
		231951,
		108,
		True
	},
	level_flare_supply = {
		232059,
		209,
		True
	},
	chat_level_not_enough = {
		232268,
		136,
		True
	},
	chat_msg_inform = {
		232404,
		143,
		True
	},
	chat_msg_ban = {
		232547,
		182,
		True
	},
	month_card_set_ratio_success = {
		232729,
		115,
		True
	},
	month_card_set_ratio_not_change = {
		232844,
		125,
		True
	},
	charge_ship_bag_max = {
		232969,
		117,
		True
	},
	charge_equip_bag_max = {
		233086,
		121,
		True
	},
	login_wait_tip = {
		233207,
		141,
		True
	},
	ship_equip_exchange_tip = {
		233348,
		189,
		True
	},
	ship_rename_success = {
		233537,
		109,
		True
	},
	formation_chapter_lock = {
		233646,
		122,
		True
	},
	elite_disable_unsatisfied = {
		233768,
		127,
		True
	},
	elite_disable_ship_escort = {
		233895,
		158,
		True
	},
	elite_disable_formation_unsatisfied = {
		234053,
		149,
		True
	},
	elite_disable_no_fleet = {
		234202,
		135,
		True
	},
	elite_disable_property_unsatisfied = {
		234337,
		146,
		True
	},
	elite_disable_unusable = {
		234483,
		131,
		True
	},
	elite_warp_to_latest_map = {
		234614,
		111,
		True
	},
	elite_fleet_confirm = {
		234725,
		213,
		True
	},
	elite_condition_level = {
		234938,
		98,
		True
	},
	elite_condition_durability = {
		235036,
		98,
		True
	},
	elite_condition_cannon = {
		235134,
		94,
		True
	},
	elite_condition_torpedo = {
		235228,
		96,
		True
	},
	elite_condition_antiaircraft = {
		235324,
		100,
		True
	},
	elite_condition_air = {
		235424,
		92,
		True
	},
	elite_condition_antisub = {
		235516,
		96,
		True
	},
	elite_condition_dodge = {
		235612,
		94,
		True
	},
	elite_condition_reload = {
		235706,
		95,
		True
	},
	elite_condition_fleet_totle_level = {
		235801,
		134,
		True
	},
	common_compare_larger = {
		235935,
		86,
		True
	},
	common_compare_equal = {
		236021,
		85,
		True
	},
	common_compare_smaller = {
		236106,
		87,
		True
	},
	common_compare_not_less_than = {
		236193,
		95,
		True
	},
	common_compare_not_more_than = {
		236288,
		95,
		True
	},
	level_scene_formation_active_already = {
		236383,
		133,
		True
	},
	level_scene_not_enough = {
		236516,
		120,
		True
	},
	level_scene_full_hp = {
		236636,
		148,
		True
	},
	level_click_to_move = {
		236784,
		115,
		True
	},
	common_hardmode = {
		236899,
		83,
		True
	},
	common_elite_no_quota = {
		236982,
		135,
		True
	},
	common_food = {
		237117,
		81,
		True
	},
	common_no_limit = {
		237198,
		88,
		True
	},
	common_proficiency = {
		237286,
		92,
		True
	},
	backyard_food_remind = {
		237378,
		178,
		True
	},
	backyard_food_count = {
		237556,
		109,
		True
	},
	sham_ship_level_limit = {
		237665,
		114,
		True
	},
	sham_count_limit = {
		237779,
		115,
		True
	},
	sham_count_reset = {
		237894,
		126,
		True
	},
	sham_team_limit = {
		238020,
		175,
		True
	},
	sham_formation_invalid = {
		238195,
		154,
		True
	},
	sham_my_assist_ship_level_limit = {
		238349,
		132,
		True
	},
	sham_reset_confirm = {
		238481,
		160,
		True
	},
	sham_battle_help_tip = {
		238641,
		84,
		True
	},
	sham_reset_err_limit = {
		238725,
		130,
		True
	},
	sham_ship_equip_forbid_1 = {
		238855,
		207,
		True
	},
	sham_ship_equip_forbid_2 = {
		239062,
		183,
		True
	},
	sham_enter_error_friend_ship_expired = {
		239245,
		156,
		True
	},
	sham_can_not_change_ship = {
		239401,
		140,
		True
	},
	sham_friend_ship_tip = {
		239541,
		213,
		True
	},
	inform_sueecss = {
		239754,
		95,
		True
	},
	inform_failed = {
		239849,
		101,
		True
	},
	inform_player = {
		239950,
		94,
		True
	},
	inform_select_type = {
		240044,
		114,
		True
	},
	inform_chat_msg = {
		240158,
		101,
		True
	},
	inform_sueecss_tip = {
		240259,
		161,
		True
	},
	ship_remould_max_level = {
		240420,
		137,
		True
	},
	ship_remould_material_ship_no_enough = {
		240557,
		139,
		True
	},
	ship_remould_material_ship_on_exist = {
		240696,
		138,
		True
	},
	ship_remould_material_unlock_skill = {
		240834,
		112,
		True
	},
	ship_remould_prev_lock = {
		240946,
		93,
		True
	},
	ship_remould_need_level = {
		241039,
		94,
		True
	},
	ship_remould_need_star = {
		241133,
		94,
		True
	},
	ship_remould_finished = {
		241227,
		94,
		True
	},
	ship_remould_no_item = {
		241321,
		101,
		True
	},
	ship_remould_no_gold = {
		241422,
		112,
		True
	},
	ship_remould_no_material = {
		241534,
		120,
		True
	},
	ship_remould_selecte_exceed = {
		241654,
		124,
		True
	},
	ship_remould_sueecss = {
		241778,
		93,
		True
	},
	ship_remould_warning_102174 = {
		241871,
		200,
		True
	},
	ship_remould_warning_102284 = {
		242071,
		205,
		True
	},
	ship_remould_warning_102304 = {
		242276,
		356,
		True
	},
	ship_remould_warning_105214 = {
		242632,
		222,
		True
	},
	ship_remould_warning_105234 = {
		242854,
		235,
		True
	},
	ship_remould_warning_107984 = {
		243089,
		238,
		True
	},
	ship_remould_warning_201514 = {
		243327,
		249,
		True
	},
	ship_remould_warning_203114 = {
		243576,
		361,
		True
	},
	ship_remould_warning_203124 = {
		243937,
		352,
		True
	},
	ship_remould_warning_205124 = {
		244289,
		204,
		True
	},
	ship_remould_warning_205154 = {
		244493,
		228,
		True
	},
	ship_remould_warning_206134 = {
		244721,
		329,
		True
	},
	ship_remould_warning_301534 = {
		245050,
		183,
		True
	},
	ship_remould_warning_301874 = {
		245233,
		551,
		True
	},
	ship_remould_warning_310014 = {
		245784,
		470,
		True
	},
	ship_remould_warning_310024 = {
		246254,
		470,
		True
	},
	ship_remould_warning_310034 = {
		246724,
		470,
		True
	},
	ship_remould_warning_310044 = {
		247194,
		470,
		True
	},
	ship_remould_warning_303154 = {
		247664,
		604,
		True
	},
	ship_remould_warning_402134 = {
		248268,
		264,
		True
	},
	ship_remould_warning_702124 = {
		248532,
		492,
		True
	},
	ship_remould_warning_520014 = {
		249024,
		280,
		True
	},
	ship_remould_warning_521014 = {
		249304,
		282,
		True
	},
	ship_remould_warning_520034 = {
		249586,
		280,
		True
	},
	ship_remould_warning_521034 = {
		249866,
		282,
		True
	},
	ship_remould_warning_520044 = {
		250148,
		280,
		True
	},
	ship_remould_warning_521044 = {
		250428,
		282,
		True
	},
	ship_remould_warning_502114 = {
		250710,
		186,
		True
	},
	ship_remould_warning_506114 = {
		250896,
		399,
		True
	},
	word_soundfiles_download_title = {
		251295,
		116,
		True
	},
	word_soundfiles_download = {
		251411,
		102,
		True
	},
	word_soundfiles_checking_title = {
		251513,
		105,
		True
	},
	word_soundfiles_checking = {
		251618,
		99,
		True
	},
	word_soundfiles_checkend_title = {
		251717,
		131,
		True
	},
	word_soundfiles_checkend = {
		251848,
		101,
		True
	},
	word_soundfiles_noneedupdate = {
		251949,
		98,
		True
	},
	word_soundfiles_checkfailed = {
		252047,
		122,
		True
	},
	word_soundfiles_retry = {
		252169,
		97,
		True
	},
	word_soundfiles_update = {
		252266,
		97,
		True
	},
	word_soundfiles_update_end_title = {
		252363,
		118,
		True
	},
	word_soundfiles_update_end = {
		252481,
		106,
		True
	},
	word_soundfiles_update_failed = {
		252587,
		124,
		True
	},
	word_soundfiles_update_retry = {
		252711,
		104,
		True
	},
	word_live2dfiles_download_title = {
		252815,
		125,
		True
	},
	word_live2dfiles_download = {
		252940,
		109,
		True
	},
	word_live2dfiles_checking_title = {
		253049,
		107,
		True
	},
	word_live2dfiles_checking = {
		253156,
		98,
		True
	},
	word_live2dfiles_checkend_title = {
		253254,
		140,
		True
	},
	word_live2dfiles_checkend = {
		253394,
		102,
		True
	},
	word_live2dfiles_noneedupdate = {
		253496,
		99,
		True
	},
	word_live2dfiles_checkfailed = {
		253595,
		134,
		True
	},
	word_live2dfiles_retry = {
		253729,
		98,
		True
	},
	word_live2dfiles_update = {
		253827,
		98,
		True
	},
	word_live2dfiles_update_end_title = {
		253925,
		136,
		True
	},
	word_live2dfiles_update_end = {
		254061,
		107,
		True
	},
	word_live2dfiles_update_failed = {
		254168,
		130,
		True
	},
	word_live2dfiles_update_retry = {
		254298,
		105,
		True
	},
	word_live2dfiles_main_update_tip = {
		254403,
		149,
		True
	},
	achieve_propose_tip = {
		254552,
		101,
		True
	},
	mingshi_get_tip = {
		254653,
		105,
		True
	},
	mingshi_task_tip_1 = {
		254758,
		217,
		True
	},
	mingshi_task_tip_2 = {
		254975,
		221,
		True
	},
	mingshi_task_tip_3 = {
		255196,
		220,
		True
	},
	mingshi_task_tip_4 = {
		255416,
		221,
		True
	},
	mingshi_task_tip_5 = {
		255637,
		216,
		True
	},
	mingshi_task_tip_6 = {
		255853,
		215,
		True
	},
	mingshi_task_tip_7 = {
		256068,
		228,
		True
	},
	mingshi_task_tip_8 = {
		256296,
		223,
		True
	},
	mingshi_task_tip_9 = {
		256519,
		221,
		True
	},
	mingshi_task_tip_10 = {
		256740,
		229,
		True
	},
	mingshi_task_tip_11 = {
		256969,
		215,
		True
	},
	word_propose_changename_title = {
		257184,
		163,
		True
	},
	word_propose_changename_tip1 = {
		257347,
		136,
		True
	},
	word_propose_changename_tip2 = {
		257483,
		113,
		True
	},
	word_propose_ring_tip = {
		257596,
		109,
		True
	},
	word_rename_time_tip = {
		257705,
		147,
		True
	},
	word_rename_switch_tip = {
		257852,
		151,
		True
	},
	word_ssr = {
		258003,
		74,
		True
	},
	word_sr = {
		258077,
		76,
		True
	},
	word_r = {
		258153,
		71,
		True
	},
	ship_renameShip_error = {
		258224,
		107,
		True
	},
	ship_renameShip_error_4 = {
		258331,
		125,
		True
	},
	ship_renameShip_error_2011 = {
		258456,
		107,
		True
	},
	ship_proposeShip_error = {
		258563,
		104,
		True
	},
	ship_proposeShip_error_1 = {
		258667,
		106,
		True
	},
	word_rename_time_warning = {
		258773,
		236,
		True
	},
	word_propose_cost_tip = {
		259009,
		453,
		True
	},
	word_propose_switch_tip = {
		259462,
		102,
		True
	},
	evaluate_too_loog = {
		259564,
		101,
		True
	},
	evaluate_ban_word = {
		259665,
		112,
		True
	},
	activity_level_easy_tip = {
		259777,
		181,
		True
	},
	activity_level_difficulty_tip = {
		259958,
		210,
		True
	},
	activity_level_limit_tip = {
		260168,
		174,
		True
	},
	activity_level_inwarime_tip = {
		260342,
		221,
		True
	},
	activity_level_pass_easy_tip = {
		260563,
		187,
		True
	},
	activity_level_is_closed = {
		260750,
		114,
		True
	},
	activity_switch_tip = {
		260864,
		255,
		True
	},
	reduce_sp3_pass_count = {
		261119,
		103,
		True
	},
	qiuqiu_count = {
		261222,
		85,
		True
	},
	qiuqiu_total_count = {
		261307,
		91,
		True
	},
	npcfriendly_count = {
		261398,
		98,
		True
	},
	npcfriendly_total_count = {
		261496,
		97,
		True
	},
	longxiang_count = {
		261593,
		98,
		True
	},
	longxiang_total_count = {
		261691,
		103,
		True
	},
	pt_count = {
		261794,
		82,
		True
	},
	pt_total_count = {
		261876,
		94,
		True
	},
	remould_ship_ok = {
		261970,
		88,
		True
	},
	remould_ship_count_more = {
		262058,
		120,
		True
	},
	word_should_input = {
		262178,
		108,
		True
	},
	simulation_advantage_counting = {
		262286,
		126,
		True
	},
	simulation_disadvantage_counting = {
		262412,
		130,
		True
	},
	simulation_enhancing = {
		262542,
		144,
		True
	},
	simulation_enhanced = {
		262686,
		121,
		True
	},
	word_skill_desc_get = {
		262807,
		94,
		True
	},
	word_skill_desc_learn = {
		262901,
		89,
		True
	},
	chapter_tip_aovid_succeed = {
		262990,
		96,
		True
	},
	chapter_tip_aovid_failed = {
		263086,
		104,
		True
	},
	chapter_tip_change = {
		263190,
		103,
		True
	},
	chapter_tip_use = {
		263293,
		98,
		True
	},
	chapter_tip_with_npc = {
		263391,
		285,
		True
	},
	chapter_tip_bp_ammo = {
		263676,
		137,
		True
	},
	build_ship_tip = {
		263813,
		190,
		True
	},
	auto_battle_limit_tip = {
		264003,
		123,
		True
	},
	build_ship_quickly_buy_stone = {
		264126,
		190,
		True
	},
	build_ship_quickly_buy_tool = {
		264316,
		205,
		True
	},
	ship_profile_voice_locked = {
		264521,
		121,
		True
	},
	ship_profile_skin_locked = {
		264642,
		110,
		True
	},
	ship_profile_words = {
		264752,
		88,
		True
	},
	ship_profile_action_words = {
		264840,
		102,
		True
	},
	ship_profile_label_common = {
		264942,
		96,
		True
	},
	ship_profile_label_diff = {
		265038,
		98,
		True
	},
	level_fleet_lease_one_ship = {
		265136,
		133,
		True
	},
	level_fleet_not_enough = {
		265269,
		131,
		True
	},
	level_fleet_outof_limit = {
		265400,
		125,
		True
	},
	vote_success = {
		265525,
		82,
		True
	},
	vote_not_enough = {
		265607,
		111,
		True
	},
	vote_love_not_enough = {
		265718,
		125,
		True
	},
	vote_love_limit = {
		265843,
		143,
		True
	},
	vote_love_confirm = {
		265986,
		125,
		True
	},
	vote_primary_rule = {
		266111,
		81,
		True
	},
	vote_final_title1 = {
		266192,
		88,
		True
	},
	vote_final_rule1 = {
		266280,
		231,
		True
	},
	vote_final_title2 = {
		266511,
		94,
		True
	},
	vote_final_rule2 = {
		266605,
		240,
		True
	},
	vote_vote_time = {
		266845,
		100,
		True
	},
	vote_vote_count = {
		266945,
		87,
		True
	},
	vote_vote_group = {
		267032,
		87,
		True
	},
	vote_rank_refresh_time = {
		267119,
		120,
		True
	},
	vote_rank_in_current_server = {
		267239,
		128,
		True
	},
	words_auto_battle_label = {
		267367,
		105,
		True
	},
	words_show_ship_name_label = {
		267472,
		106,
		True
	},
	words_rare_ship_vibrate = {
		267578,
		100,
		True
	},
	words_display_ship_get_effect = {
		267678,
		108,
		True
	},
	words_show_touch_effect = {
		267786,
		102,
		True
	},
	words_bg_fit_mode = {
		267888,
		121,
		True
	},
	words_battle_hide_bg = {
		268009,
		116,
		True
	},
	words_battle_expose_line = {
		268125,
		123,
		True
	},
	words_autoFight_battery_savemode = {
		268248,
		121,
		True
	},
	words_autoFight_battery_savemode_des = {
		268369,
		182,
		True
	},
	words_autoFIght_down_frame = {
		268551,
		115,
		True
	},
	words_autoFIght_down_frame_des = {
		268666,
		163,
		True
	},
	words_autoFight_tips = {
		268829,
		131,
		True
	},
	words_autoFight_right = {
		268960,
		175,
		True
	},
	activity_puzzle_get1 = {
		269135,
		132,
		True
	},
	activity_puzzle_get2 = {
		269267,
		143,
		True
	},
	activity_puzzle_get3 = {
		269410,
		143,
		True
	},
	activity_puzzle_get4 = {
		269553,
		143,
		True
	},
	activity_puzzle_get5 = {
		269696,
		143,
		True
	},
	activity_puzzle_get6 = {
		269839,
		143,
		True
	},
	activity_puzzle_get7 = {
		269982,
		143,
		True
	},
	activity_puzzle_get8 = {
		270125,
		143,
		True
	},
	activity_puzzle_get9 = {
		270268,
		143,
		True
	},
	activity_puzzle_get10 = {
		270411,
		133,
		True
	},
	activity_puzzle_get11 = {
		270544,
		133,
		True
	},
	activity_puzzle_get12 = {
		270677,
		133,
		True
	},
	activity_puzzle_get13 = {
		270810,
		133,
		True
	},
	activity_puzzle_get14 = {
		270943,
		133,
		True
	},
	activity_puzzle_get15 = {
		271076,
		133,
		True
	},
	word_stopremain_build = {
		271209,
		102,
		True
	},
	word_stopremain_default = {
		271311,
		104,
		True
	},
	transcode_desc = {
		271415,
		359,
		True
	},
	transcode_empty_tip = {
		271774,
		117,
		True
	},
	set_birth_title = {
		271891,
		91,
		True
	},
	set_birth_confirm_tip = {
		271982,
		110,
		True
	},
	set_birth_empty_tip = {
		272092,
		105,
		True
	},
	set_birth_success = {
		272197,
		107,
		True
	},
	clear_transcode_cache_confirm = {
		272304,
		143,
		True
	},
	clear_transcode_cache_success = {
		272447,
		115,
		True
	},
	exchange_item_success = {
		272562,
		94,
		True
	},
	give_up_cloth_change = {
		272656,
		120,
		True
	},
	err_cloth_change_noship = {
		272776,
		103,
		True
	},
	need_break_tip = {
		272879,
		99,
		True
	},
	max_level_notice = {
		272978,
		152,
		True
	},
	new_skin_no_choose = {
		273130,
		156,
		True
	},
	sure_resume_volume = {
		273286,
		114,
		True
	},
	course_class_not_ready = {
		273400,
		165,
		True
	},
	course_student_max_level = {
		273565,
		152,
		True
	},
	course_stop_confirm = {
		273717,
		103,
		True
	},
	course_class_help = {
		273820,
		1480,
		True
	},
	course_class_name = {
		275300,
		100,
		True
	},
	course_proficiency_not_enough = {
		275400,
		128,
		True
	},
	course_state_rest = {
		275528,
		91,
		True
	},
	course_state_lession = {
		275619,
		97,
		True
	},
	course_energy_not_enough = {
		275716,
		156,
		True
	},
	course_proficiency_tip = {
		275872,
		382,
		True
	},
	course_sunday_tip = {
		276254,
		145,
		True
	},
	course_exit_confirm = {
		276399,
		158,
		True
	},
	course_learning = {
		276557,
		111,
		True
	},
	time_remaining_tip = {
		276668,
		93,
		True
	},
	propose_intimacy_tip = {
		276761,
		119,
		True
	},
	no_found_record_equipment = {
		276880,
		196,
		True
	},
	sec_floor_limit_tip = {
		277076,
		130,
		True
	},
	guild_shop_flash_success = {
		277206,
		98,
		True
	},
	destroy_high_rarity_tip = {
		277304,
		125,
		True
	},
	destroy_high_level_tip = {
		277429,
		133,
		True
	},
	destroy_eliteequipment_tip = {
		277562,
		117,
		True
	},
	destroy_high_intensify_tip = {
		277679,
		124,
		True
	},
	destroy_inHardFormation_tip = {
		277803,
		126,
		True
	},
	destroy_equip_rarity_tip = {
		277929,
		161,
		True
	},
	ship_quick_change_noequip = {
		278090,
		116,
		True
	},
	ship_quick_change_nofreeequip = {
		278206,
		134,
		True
	},
	word_nowenergy = {
		278340,
		84,
		True
	},
	word_energy_recov_speed = {
		278424,
		101,
		True
	},
	destroy_eliteship_tip = {
		278525,
		111,
		True
	},
	err_resloveequip_nochoice = {
		278636,
		120,
		True
	},
	take_nothing = {
		278756,
		103,
		True
	},
	take_all_mail = {
		278859,
		171,
		True
	},
	buy_furniture_overtime = {
		279030,
		135,
		True
	},
	twitter_login_tips = {
		279165,
		166,
		True
	},
	data_erro = {
		279331,
		121,
		True
	},
	login_failed = {
		279452,
		94,
		True
	},
	["not yet completed"] = {
		279546,
		93,
		True
	},
	escort_less_count_to_combat = {
		279639,
		127,
		True
	},
	ten_even_draw = {
		279766,
		94,
		True
	},
	ten_even_draw_confirm = {
		279860,
		111,
		True
	},
	level_risk_level_desc = {
		279971,
		90,
		True
	},
	level_risk_level_mitigation_rate = {
		280061,
		239,
		True
	},
	level_diffcult_chapter_state_safety = {
		280300,
		229,
		True
	},
	level_chapter_state_high_risk = {
		280529,
		137,
		True
	},
	level_chapter_state_risk = {
		280666,
		128,
		True
	},
	level_chapter_state_low_risk = {
		280794,
		133,
		True
	},
	level_chapter_state_safety = {
		280927,
		132,
		True
	},
	open_skill_class_success = {
		281059,
		121,
		True
	},
	backyard_sort_tag_default = {
		281180,
		91,
		True
	},
	backyard_sort_tag_price = {
		281271,
		93,
		True
	},
	backyard_sort_tag_comfortable = {
		281364,
		100,
		True
	},
	backyard_sort_tag_size = {
		281464,
		90,
		True
	},
	backyard_filter_tag_other = {
		281554,
		93,
		True
	},
	word_status_inFight = {
		281647,
		90,
		True
	},
	word_status_inPVP = {
		281737,
		91,
		True
	},
	word_status_inEvent = {
		281828,
		92,
		True
	},
	word_status_inEventFinished = {
		281920,
		100,
		True
	},
	word_status_inTactics = {
		282020,
		93,
		True
	},
	word_status_inClass = {
		282113,
		91,
		True
	},
	word_status_rest = {
		282204,
		87,
		True
	},
	word_status_train = {
		282291,
		89,
		True
	},
	word_status_world = {
		282380,
		97,
		True
	},
	word_status_inHardFormation = {
		282477,
		103,
		True
	},
	word_status_series_enemy = {
		282580,
		103,
		True
	},
	challenge_rule = {
		282683,
		101,
		True
	},
	challenge_exit_warning = {
		282784,
		241,
		True
	},
	challenge_fleet_type_fail = {
		283025,
		141,
		True
	},
	challenge_current_level = {
		283166,
		110,
		True
	},
	challenge_current_score = {
		283276,
		104,
		True
	},
	challenge_total_score = {
		283380,
		99,
		True
	},
	challenge_current_progress = {
		283479,
		113,
		True
	},
	challenge_count_unlimit = {
		283592,
		99,
		True
	},
	challenge_no_fleet = {
		283691,
		118,
		True
	},
	equipment_skin_unload = {
		283809,
		147,
		True
	},
	equipment_skin_no_old_ship = {
		283956,
		119,
		True
	},
	equipment_skin_no_old_skinorequipment = {
		284075,
		162,
		True
	},
	equipment_skin_no_new_ship = {
		284237,
		113,
		True
	},
	equipment_skin_no_new_equipment = {
		284350,
		126,
		True
	},
	equipment_skin_count_noenough = {
		284476,
		115,
		True
	},
	equipment_skin_replace_done = {
		284591,
		120,
		True
	},
	equipment_skin_unload_failed = {
		284711,
		128,
		True
	},
	equipment_skin_unmatch_equipment = {
		284839,
		180,
		True
	},
	equipment_skin_no_equipment_tip = {
		285019,
		156,
		True
	},
	activity_pool_awards_empty = {
		285175,
		119,
		True
	},
	activity_switch_award_pool_failed = {
		285294,
		183,
		True
	},
	shop_street_activity_tip = {
		285477,
		180,
		True
	},
	shop_street_Equipment_skin_box_help = {
		285657,
		166,
		True
	},
	twitter_link_title = {
		285823,
		100,
		True
	},
	commander_material_noenough = {
		285923,
		122,
		True
	},
	battle_result_boss_destruct = {
		286045,
		132,
		True
	},
	battle_preCombatLayer_boss_destruct = {
		286177,
		140,
		True
	},
	destory_important_equipment_tip = {
		286317,
		198,
		True
	},
	destory_important_equipment_input_erro = {
		286515,
		121,
		True
	},
	activity_hit_monster_nocount = {
		286636,
		112,
		True
	},
	activity_hit_monster_death = {
		286748,
		124,
		True
	},
	activity_hit_monster_help = {
		286872,
		119,
		True
	},
	activity_hit_monster_erro = {
		286991,
		103,
		True
	},
	activity_xiaotiane_progress = {
		287094,
		107,
		True
	},
	activity_hit_monster_reset_tip = {
		287201,
		228,
		True
	},
	answer_help_tip = {
		287429,
		182,
		True
	},
	answer_answer_role = {
		287611,
		172,
		True
	},
	answer_exit_tip = {
		287783,
		112,
		True
	},
	equip_skin_detail_tip = {
		287895,
		121,
		True
	},
	emoji_type_0 = {
		288016,
		82,
		True
	},
	emoji_type_1 = {
		288098,
		83,
		True
	},
	emoji_type_2 = {
		288181,
		84,
		True
	},
	emoji_type_3 = {
		288265,
		82,
		True
	},
	emoji_type_4 = {
		288347,
		84,
		True
	},
	card_pairs_help_tip = {
		288431,
		943,
		True
	},
	card_pairs_tips = {
		289374,
		162,
		True
	},
	["card_battle_card details_deck"] = {
		289536,
		105,
		True
	},
	["card_battle_card details_hand"] = {
		289641,
		109,
		True
	},
	["card_battle_card details"] = {
		289750,
		100,
		True
	},
	["card_battle_card details_switchto_deck"] = {
		289850,
		111,
		True
	},
	["card_battle_card details_switchto_hand"] = {
		289961,
		115,
		True
	},
	card_battle_card_empty_en = {
		290076,
		106,
		True
	},
	card_battle_card_empty_ch = {
		290182,
		130,
		True
	},
	card_puzzel_goal_ch = {
		290312,
		93,
		True
	},
	card_puzzel_goal_en = {
		290405,
		89,
		True
	},
	card_puzzle_deck = {
		290494,
		84,
		True
	},
	upgrade_to_next_maxlevel_failed = {
		290578,
		181,
		True
	},
	upgrade_to_next_maxlevel_tip = {
		290759,
		240,
		True
	},
	upgrade_to_next_maxlevel_succeed = {
		290999,
		198,
		True
	},
	extra_chapter_socre_tip = {
		291197,
		173,
		True
	},
	extra_chapter_record_updated = {
		291370,
		102,
		True
	},
	extra_chapter_record_not_updated = {
		291472,
		112,
		True
	},
	extra_chapter_locked_tip = {
		291584,
		120,
		True
	},
	extra_chapter_locked_tip_1 = {
		291704,
		167,
		True
	},
	player_name_change_time_lv_tip = {
		291871,
		172,
		True
	},
	player_name_change_time_limit_tip = {
		292043,
		174,
		True
	},
	player_name_change_windows_tip = {
		292217,
		234,
		True
	},
	player_name_change_warning = {
		292451,
		247,
		True
	},
	player_name_change_success = {
		292698,
		116,
		True
	},
	player_name_change_failed = {
		292814,
		111,
		True
	},
	same_player_name_tip = {
		292925,
		109,
		True
	},
	task_is_not_existence = {
		293034,
		112,
		True
	},
	cannot_build_multiple_printblue = {
		293146,
		366,
		True
	},
	printblue_build_success = {
		293512,
		107,
		True
	},
	printblue_build_erro = {
		293619,
		103,
		True
	},
	blueprint_mod_success = {
		293722,
		107,
		True
	},
	blueprint_mod_erro = {
		293829,
		100,
		True
	},
	technology_refresh_sucess = {
		293929,
		133,
		True
	},
	technology_refresh_erro = {
		294062,
		126,
		True
	},
	change_technology_refresh_sucess = {
		294188,
		136,
		True
	},
	change_technology_refresh_erro = {
		294324,
		130,
		True
	},
	technology_start_up = {
		294454,
		100,
		True
	},
	technology_start_erro = {
		294554,
		101,
		True
	},
	technology_stop_success = {
		294655,
		119,
		True
	},
	technology_stop_erro = {
		294774,
		111,
		True
	},
	technology_finish_success = {
		294885,
		121,
		True
	},
	technology_finish_erro = {
		295006,
		114,
		True
	},
	blueprint_stop_success = {
		295120,
		121,
		True
	},
	blueprint_stop_erro = {
		295241,
		113,
		True
	},
	blueprint_destory_tip = {
		295354,
		119,
		True
	},
	blueprint_task_update_tip = {
		295473,
		172,
		True
	},
	blueprint_mod_addition_lock = {
		295645,
		125,
		True
	},
	blueprint_mod_word_unlock = {
		295770,
		111,
		True
	},
	blueprint_mod_skin_unlock = {
		295881,
		106,
		True
	},
	blueprint_build_consume = {
		295987,
		120,
		True
	},
	blueprint_stop_tip = {
		296107,
		180,
		True
	},
	technology_canot_refresh = {
		296287,
		153,
		True
	},
	technology_refresh_tip = {
		296440,
		138,
		True
	},
	technology_is_actived = {
		296578,
		125,
		True
	},
	technology_stop_tip = {
		296703,
		178,
		True
	},
	technology_help_text = {
		296881,
		2742,
		True
	},
	blueprint_build_time_tip = {
		299623,
		209,
		True
	},
	blueprint_cannot_build_tip = {
		299832,
		147,
		True
	},
	technology_task_none_tip = {
		299979,
		97,
		True
	},
	technology_task_build_tip = {
		300076,
		161,
		True
	},
	blueprint_commit_tip = {
		300237,
		165,
		True
	},
	buleprint_need_level_tip = {
		300402,
		141,
		True
	},
	blueprint_max_level_tip = {
		300543,
		132,
		True
	},
	ship_profile_voice_locked_intimacy = {
		300675,
		133,
		True
	},
	ship_profile_voice_locked_propose = {
		300808,
		115,
		True
	},
	ship_profile_voice_locked_propose_imas = {
		300923,
		120,
		True
	},
	ship_profile_voice_locked_design = {
		301043,
		140,
		True
	},
	ship_profile_voice_locked_meta = {
		301183,
		106,
		True
	},
	help_technolog0 = {
		301289,
		350,
		True
	},
	help_technolog = {
		301639,
		513,
		True
	},
	hide_chat_warning = {
		302152,
		115,
		True
	},
	show_chat_warning = {
		302267,
		117,
		True
	},
	help_shipblueprintui = {
		302384,
		3798,
		True
	},
	help_shipblueprintui_luck = {
		306182,
		734,
		True
	},
	anniversary_task_title_1 = {
		306916,
		175,
		True
	},
	anniversary_task_title_2 = {
		307091,
		206,
		True
	},
	anniversary_task_title_3 = {
		307297,
		177,
		True
	},
	anniversary_task_title_4 = {
		307474,
		210,
		True
	},
	anniversary_task_title_5 = {
		307684,
		184,
		True
	},
	anniversary_task_title_6 = {
		307868,
		204,
		True
	},
	anniversary_task_title_7 = {
		308072,
		202,
		True
	},
	anniversary_task_title_8 = {
		308274,
		169,
		True
	},
	anniversary_task_title_9 = {
		308443,
		193,
		True
	},
	anniversary_task_title_10 = {
		308636,
		176,
		True
	},
	anniversary_task_title_11 = {
		308812,
		160,
		True
	},
	anniversary_task_title_12 = {
		308972,
		178,
		True
	},
	anniversary_task_title_13 = {
		309150,
		195,
		True
	},
	anniversary_task_title_14 = {
		309345,
		179,
		True
	},
	charge_scene_buy_confirm = {
		309524,
		163,
		True
	},
	charge_scene_buy_confirm_gold = {
		309687,
		168,
		True
	},
	charge_scene_batch_buy_tip = {
		309855,
		189,
		True
	},
	help_level_ui = {
		310044,
		968,
		True
	},
	guild_modify_info_tip = {
		311012,
		193,
		True
	},
	ai_change_1 = {
		311205,
		118,
		True
	},
	ai_change_2 = {
		311323,
		117,
		True
	},
	activity_shop_lable = {
		311440,
		127,
		True
	},
	word_bilibili = {
		311567,
		90,
		True
	},
	levelScene_tracking_error_pre = {
		311657,
		143,
		True
	},
	ship_limit_notice = {
		311800,
		157,
		True
	},
	idle = {
		311957,
		73,
		True
	},
	main_1 = {
		312030,
		81,
		True
	},
	main_2 = {
		312111,
		81,
		True
	},
	main_3 = {
		312192,
		81,
		True
	},
	complete = {
		312273,
		84,
		True
	},
	login = {
		312357,
		74,
		True
	},
	home = {
		312431,
		74,
		True
	},
	mail = {
		312505,
		77,
		True
	},
	mission = {
		312582,
		83,
		True
	},
	mission_complete = {
		312665,
		96,
		True
	},
	wedding = {
		312761,
		77,
		True
	},
	touch_head = {
		312838,
		84,
		True
	},
	touch_body = {
		312922,
		79,
		True
	},
	touch_special = {
		313001,
		84,
		True
	},
	gold = {
		313085,
		73,
		True
	},
	oil = {
		313158,
		70,
		True
	},
	diamond = {
		313228,
		75,
		True
	},
	word_photo_mode = {
		313303,
		84,
		True
	},
	word_video_mode = {
		313387,
		82,
		True
	},
	word_save_ok = {
		313469,
		114,
		True
	},
	word_save_video = {
		313583,
		120,
		True
	},
	reflux_help_tip = {
		313703,
		974,
		True
	},
	reflux_pt_not_enough = {
		314677,
		121,
		True
	},
	reflux_word_1 = {
		314798,
		87,
		True
	},
	reflux_word_2 = {
		314885,
		85,
		True
	},
	ship_hunting_level_tips = {
		314970,
		190,
		True
	},
	acquisitionmode_is_not_open = {
		315160,
		123,
		True
	},
	collect_chapter_is_activation = {
		315283,
		140,
		True
	},
	levelScene_chapter_is_activation = {
		315423,
		189,
		True
	},
	resource_verify_warn = {
		315612,
		245,
		True
	},
	resource_verify_fail = {
		315857,
		191,
		True
	},
	resource_verify_success = {
		316048,
		122,
		True
	},
	resource_clear_all = {
		316170,
		178,
		True
	},
	acl_oil_count = {
		316348,
		87,
		True
	},
	acl_oil_total_count = {
		316435,
		99,
		True
	},
	word_take_video_tip = {
		316534,
		141,
		True
	},
	word_snapshot_share_title = {
		316675,
		118,
		True
	},
	word_snapshot_share_agreement = {
		316793,
		540,
		True
	},
	skin_remain_time = {
		317333,
		91,
		True
	},
	word_museum_1 = {
		317424,
		120,
		True
	},
	word_museum_help = {
		317544,
		734,
		True
	},
	goldship_help_tip = {
		318278,
		787,
		True
	},
	metalgearsub_help_tip = {
		319065,
		1847,
		True
	},
	acl_gold_count = {
		320912,
		91,
		True
	},
	acl_gold_total_count = {
		321003,
		102,
		True
	},
	discount_time = {
		321105,
		146,
		True
	},
	commander_talent_not_exist = {
		321251,
		132,
		True
	},
	commander_replace_talent_not_exist = {
		321383,
		154,
		True
	},
	commander_talent_learned = {
		321537,
		121,
		True
	},
	commander_talent_learn_erro = {
		321658,
		133,
		True
	},
	commander_not_exist = {
		321791,
		114,
		True
	},
	commander_fleet_not_exist = {
		321905,
		115,
		True
	},
	commander_fleet_pos_not_exist = {
		322020,
		128,
		True
	},
	commander_equip_to_fleet_erro = {
		322148,
		140,
		True
	},
	commander_acquire_erro = {
		322288,
		138,
		True
	},
	commander_lock_erro = {
		322426,
		121,
		True
	},
	commander_reset_talent_time_no_rearch = {
		322547,
		157,
		True
	},
	commander_reset_talent_is_not_need = {
		322704,
		125,
		True
	},
	commander_reset_talent_success = {
		322829,
		118,
		True
	},
	commander_reset_talent_erro = {
		322947,
		136,
		True
	},
	commander_can_not_be_upgrade = {
		323083,
		133,
		True
	},
	commander_anyone_is_in_fleet = {
		323216,
		139,
		True
	},
	commander_is_in_fleet = {
		323355,
		133,
		True
	},
	commander_play_erro = {
		323488,
		104,
		True
	},
	ship_equip_same_group_equipment = {
		323592,
		136,
		True
	},
	summary_page_un_rearch = {
		323728,
		96,
		True
	},
	player_summary_from = {
		323824,
		97,
		True
	},
	player_summary_data = {
		323921,
		95,
		True
	},
	commander_exp_overflow_tip = {
		324016,
		192,
		True
	},
	commander_reset_talent_tip = {
		324208,
		141,
		True
	},
	commander_reset_talent = {
		324349,
		96,
		True
	},
	commander_select_min_cnt = {
		324445,
		127,
		True
	},
	commander_select_max = {
		324572,
		123,
		True
	},
	commander_lock_done = {
		324695,
		101,
		True
	},
	commander_unlock_done = {
		324796,
		105,
		True
	},
	commander_get_1 = {
		324901,
		127,
		True
	},
	commander_get = {
		325028,
		139,
		True
	},
	commander_build_done = {
		325167,
		114,
		True
	},
	commander_build_erro = {
		325281,
		117,
		True
	},
	commander_get_skills_done = {
		325398,
		132,
		True
	},
	collection_way_is_unopen = {
		325530,
		115,
		True
	},
	commander_can_not_select_same_group = {
		325645,
		162,
		True
	},
	commander_capcity_is_max = {
		325807,
		115,
		True
	},
	commander_reserve_count_is_max = {
		325922,
		128,
		True
	},
	commander_build_pool_tip = {
		326050,
		143,
		True
	},
	commander_select_matiral_erro = {
		326193,
		212,
		True
	},
	commander_material_is_rarity = {
		326405,
		156,
		True
	},
	commander_material_is_maxLevel = {
		326561,
		200,
		True
	},
	charge_commander_bag_max = {
		326761,
		161,
		True
	},
	shop_extendcommander_success = {
		326922,
		148,
		True
	},
	commander_skill_point_noengough = {
		327070,
		144,
		True
	},
	buildship_new_tip = {
		327214,
		160,
		True
	},
	buildship_heavy_tip = {
		327374,
		142,
		True
	},
	buildship_light_tip = {
		327516,
		154,
		True
	},
	buildship_special_tip = {
		327670,
		156,
		True
	},
	Normalbuild_URexchange_help = {
		327826,
		615,
		True
	},
	Normalbuild_URexchange_text1 = {
		328441,
		103,
		True
	},
	Normalbuild_URexchange_text2 = {
		328544,
		97,
		True
	},
	Normalbuild_URexchange_text3 = {
		328641,
		103,
		True
	},
	Normalbuild_URexchange_text4 = {
		328744,
		100,
		True
	},
	Normalbuild_URexchange_warning1 = {
		328844,
		128,
		True
	},
	Normalbuild_URexchange_warning3 = {
		328972,
		207,
		True
	},
	Normalbuild_URexchange_confirm = {
		329179,
		121,
		True
	},
	open_skill_pos = {
		329300,
		236,
		True
	},
	open_skill_pos_discount = {
		329536,
		239,
		True
	},
	event_recommend_fail = {
		329775,
		124,
		True
	},
	newplayer_help_tip = {
		329899,
		988,
		True
	},
	newplayer_notice_1 = {
		330887,
		125,
		True
	},
	newplayer_notice_2 = {
		331012,
		125,
		True
	},
	newplayer_notice_3 = {
		331137,
		117,
		True
	},
	newplayer_notice_4 = {
		331254,
		121,
		True
	},
	newplayer_notice_5 = {
		331375,
		119,
		True
	},
	newplayer_notice_6 = {
		331494,
		171,
		True
	},
	newplayer_notice_7 = {
		331665,
		124,
		True
	},
	newplayer_notice_8 = {
		331789,
		149,
		True
	},
	tec_catchup_1 = {
		331938,
		85,
		True
	},
	tec_catchup_2 = {
		332023,
		85,
		True
	},
	tec_catchup_3 = {
		332108,
		85,
		True
	},
	tec_catchup_4 = {
		332193,
		85,
		True
	},
	tec_catchup_5 = {
		332278,
		85,
		True
	},
	tec_notice = {
		332363,
		124,
		True
	},
	tec_notice_not_open_tip = {
		332487,
		141,
		True
	},
	apply_permission_camera_tip1 = {
		332628,
		181,
		True
	},
	apply_permission_camera_tip2 = {
		332809,
		187,
		True
	},
	apply_permission_camera_tip3 = {
		332996,
		177,
		True
	},
	apply_permission_record_audio_tip1 = {
		333173,
		163,
		True
	},
	apply_permission_record_audio_tip2 = {
		333336,
		197,
		True
	},
	apply_permission_record_audio_tip3 = {
		333533,
		183,
		True
	},
	nine_choose_one = {
		333716,
		269,
		True
	},
	help_commander_info = {
		333985,
		810,
		True
	},
	help_commander_play = {
		334795,
		810,
		True
	},
	help_commander_ability = {
		335605,
		813,
		True
	},
	story_skip_confirm = {
		336418,
		215,
		True
	},
	commander_ability_replace_warning = {
		336633,
		205,
		True
	},
	help_command_room = {
		336838,
		808,
		True
	},
	commander_build_rate_tip = {
		337646,
		154,
		True
	},
	help_activity_bossbattle = {
		337800,
		1040,
		True
	},
	commander_is_in_fleet_already = {
		338840,
		141,
		True
	},
	commander_material_is_in_fleet_tip = {
		338981,
		167,
		True
	},
	commander_main_pos = {
		339148,
		93,
		True
	},
	commander_assistant_pos = {
		339241,
		96,
		True
	},
	comander_repalce_tip = {
		339337,
		200,
		True
	},
	commander_lock_tip = {
		339537,
		121,
		True
	},
	commander_is_in_battle = {
		339658,
		125,
		True
	},
	commander_rename_warning = {
		339783,
		143,
		True
	},
	commander_rename_coldtime_tip = {
		339926,
		154,
		True
	},
	commander_rename_success_tip = {
		340080,
		115,
		True
	},
	amercian_notice_1 = {
		340195,
		170,
		True
	},
	amercian_notice_2 = {
		340365,
		131,
		True
	},
	amercian_notice_3 = {
		340496,
		104,
		True
	},
	amercian_notice_4 = {
		340600,
		92,
		True
	},
	amercian_notice_5 = {
		340692,
		112,
		True
	},
	amercian_notice_6 = {
		340804,
		222,
		True
	},
	ranking_word_1 = {
		341026,
		89,
		True
	},
	ranking_word_2 = {
		341115,
		93,
		True
	},
	ranking_word_3 = {
		341208,
		91,
		True
	},
	ranking_word_4 = {
		341299,
		93,
		True
	},
	ranking_word_5 = {
		341392,
		82,
		True
	},
	ranking_word_6 = {
		341474,
		91,
		True
	},
	ranking_word_7 = {
		341565,
		90,
		True
	},
	ranking_word_8 = {
		341655,
		82,
		True
	},
	ranking_word_9 = {
		341737,
		83,
		True
	},
	ranking_word_10 = {
		341820,
		94,
		True
	},
	spece_illegal_tip = {
		341914,
		99,
		True
	},
	utaware_warmup_notice = {
		342013,
		902,
		True
	},
	utaware_formal_notice = {
		342915,
		648,
		True
	},
	npc_learn_skill_tip = {
		343563,
		250,
		True
	},
	npc_upgrade_max_level = {
		343813,
		147,
		True
	},
	npc_propse_tip = {
		343960,
		113,
		True
	},
	npc_strength_tip = {
		344073,
		209,
		True
	},
	npc_breakout_tip = {
		344282,
		210,
		True
	},
	word_chuansong = {
		344492,
		95,
		True
	},
	npc_evaluation_tip = {
		344587,
		145,
		True
	},
	map_event_skip = {
		344732,
		90,
		True
	},
	map_event_stop_tip = {
		344822,
		163,
		True
	},
	map_event_stop_battle_tip = {
		344985,
		172,
		True
	},
	map_event_stop_battle_tip_2 = {
		345157,
		151,
		True
	},
	map_event_stop_story_tip = {
		345308,
		167,
		True
	},
	map_event_save_nekone = {
		345475,
		136,
		True
	},
	map_event_save_rurutie = {
		345611,
		139,
		True
	},
	map_event_memory_collected = {
		345750,
		152,
		True
	},
	map_event_save_kizuna = {
		345902,
		140,
		True
	},
	five_choose_one = {
		346042,
		201,
		True
	},
	ship_preference_common = {
		346243,
		107,
		True
	},
	draw_big_luck_1 = {
		346350,
		116,
		True
	},
	draw_big_luck_2 = {
		346466,
		127,
		True
	},
	draw_big_luck_3 = {
		346593,
		131,
		True
	},
	draw_medium_luck_1 = {
		346724,
		124,
		True
	},
	draw_medium_luck_2 = {
		346848,
		122,
		True
	},
	draw_medium_luck_3 = {
		346970,
		133,
		True
	},
	draw_little_luck_1 = {
		347103,
		128,
		True
	},
	draw_little_luck_2 = {
		347231,
		124,
		True
	},
	draw_little_luck_3 = {
		347355,
		134,
		True
	},
	ship_preference_non = {
		347489,
		106,
		True
	},
	school_title_dajiangtang = {
		347595,
		101,
		True
	},
	school_title_zhihuimiao = {
		347696,
		95,
		True
	},
	school_title_shitang = {
		347791,
		92,
		True
	},
	school_title_xiaomaibu = {
		347883,
		95,
		True
	},
	school_title_shangdian = {
		347978,
		94,
		True
	},
	school_title_xueyuan = {
		348072,
		98,
		True
	},
	school_title_shoucang = {
		348170,
		95,
		True
	},
	school_title_xiaoyouxiting = {
		348265,
		96,
		True
	},
	tag_level_fighting = {
		348361,
		93,
		True
	},
	tag_level_oni = {
		348454,
		89,
		True
	},
	tag_level_bomb = {
		348543,
		90,
		True
	},
	ui_word_levelui2_inevent = {
		348633,
		97,
		True
	},
	exit_backyard_exp_display = {
		348730,
		125,
		True
	},
	help_monopoly = {
		348855,
		1634,
		True
	},
	md5_error = {
		350489,
		120,
		True
	},
	world_boss_help = {
		350609,
		4737,
		True
	},
	world_boss_tip = {
		355346,
		193,
		True
	},
	world_boss_award_limit = {
		355539,
		157,
		True
	},
	backyard_is_loading = {
		355696,
		104,
		True
	},
	levelScene_loop_help_tip = {
		355800,
		2782,
		True
	},
	no_airspace_competition = {
		358582,
		104,
		True
	},
	air_supremacy_value = {
		358686,
		101,
		True
	},
	read_the_user_agreement = {
		358787,
		146,
		True
	},
	award_max_warning = {
		358933,
		175,
		True
	},
	sub_item_warning = {
		359108,
		140,
		True
	},
	select_award_warning = {
		359248,
		126,
		True
	},
	no_item_selected_tip = {
		359374,
		119,
		True
	},
	backyard_traning_tip = {
		359493,
		160,
		True
	},
	backyard_rest_tip = {
		359653,
		122,
		True
	},
	backyard_class_tip = {
		359775,
		122,
		True
	},
	medal_notice_1 = {
		359897,
		95,
		True
	},
	medal_notice_2 = {
		359992,
		86,
		True
	},
	medal_help_tip = {
		360078,
		1522,
		True
	},
	trophy_achieved = {
		361600,
		94,
		True
	},
	text_shop = {
		361694,
		77,
		True
	},
	text_confirm = {
		361771,
		83,
		True
	},
	text_cancel = {
		361854,
		81,
		True
	},
	text_cancel_fight = {
		361935,
		93,
		True
	},
	text_goon_fight = {
		362028,
		87,
		True
	},
	text_exit = {
		362115,
		77,
		True
	},
	text_clear = {
		362192,
		79,
		True
	},
	text_apply = {
		362271,
		83,
		True
	},
	text_buy = {
		362354,
		75,
		True
	},
	text_forward = {
		362429,
		78,
		True
	},
	text_prepage = {
		362507,
		80,
		True
	},
	text_nextpage = {
		362587,
		81,
		True
	},
	text_exchange = {
		362668,
		85,
		True
	},
	text_retreat = {
		362753,
		83,
		True
	},
	text_goto = {
		362836,
		80,
		True
	},
	level_scene_title_word_1 = {
		362916,
		100,
		True
	},
	level_scene_title_word_2 = {
		363016,
		108,
		True
	},
	level_scene_title_word_3 = {
		363124,
		100,
		True
	},
	level_scene_title_word_4 = {
		363224,
		97,
		True
	},
	level_scene_title_word_5 = {
		363321,
		97,
		True
	},
	ambush_display_0 = {
		363418,
		89,
		True
	},
	ambush_display_1 = {
		363507,
		84,
		True
	},
	ambush_display_2 = {
		363591,
		85,
		True
	},
	ambush_display_3 = {
		363676,
		83,
		True
	},
	ambush_display_4 = {
		363759,
		86,
		True
	},
	ambush_display_5 = {
		363845,
		84,
		True
	},
	ambush_display_6 = {
		363929,
		86,
		True
	},
	black_white_grid_notice = {
		364015,
		1416,
		True
	},
	black_white_grid_reset = {
		365431,
		104,
		True
	},
	black_white_grid_switch_tip = {
		365535,
		122,
		True
	},
	no_way_to_escape = {
		365657,
		93,
		True
	},
	word_attr_ac = {
		365750,
		92,
		True
	},
	help_battle_ac = {
		365842,
		2193,
		True
	},
	help_attribute_dodge_limit = {
		368035,
		388,
		True
	},
	refuse_friend = {
		368423,
		105,
		True
	},
	refuse_and_add_into_bl = {
		368528,
		108,
		True
	},
	tech_simulate_closed = {
		368636,
		141,
		True
	},
	tech_simulate_quit = {
		368777,
		126,
		True
	},
	technology_uplevel_error_no_res = {
		368903,
		244,
		True
	},
	help_technologytree = {
		369147,
		2458,
		True
	},
	tech_change_version_mark = {
		371605,
		108,
		True
	},
	technology_uplevel_error_studying = {
		371713,
		196,
		True
	},
	fate_attr_word = {
		371909,
		105,
		True
	},
	fate_phase_word = {
		372014,
		98,
		True
	},
	blueprint_simulation_confirm = {
		372112,
		245,
		True
	},
	blueprint_simulation_confirm_19901 = {
		372357,
		416,
		True
	},
	blueprint_simulation_confirm_19902 = {
		372773,
		397,
		True
	},
	blueprint_simulation_confirm_39903 = {
		373170,
		398,
		True
	},
	blueprint_simulation_confirm_39904 = {
		373568,
		415,
		True
	},
	blueprint_simulation_confirm_49902 = {
		373983,
		413,
		True
	},
	blueprint_simulation_confirm_99901 = {
		374396,
		412,
		True
	},
	blueprint_simulation_confirm_29903 = {
		374808,
		374,
		True
	},
	blueprint_simulation_confirm_29904 = {
		375182,
		381,
		True
	},
	blueprint_simulation_confirm_49903 = {
		375563,
		374,
		True
	},
	blueprint_simulation_confirm_49904 = {
		375937,
		384,
		True
	},
	blueprint_simulation_confirm_89902 = {
		376321,
		380,
		True
	},
	blueprint_simulation_confirm_19903 = {
		376701,
		406,
		True
	},
	blueprint_simulation_confirm_39905 = {
		377107,
		349,
		True
	},
	blueprint_simulation_confirm_49905 = {
		377456,
		409,
		True
	},
	blueprint_simulation_confirm_49906 = {
		377865,
		339,
		True
	},
	blueprint_simulation_confirm_69901 = {
		378204,
		421,
		True
	},
	blueprint_simulation_confirm_29905 = {
		378625,
		398,
		True
	},
	blueprint_simulation_confirm_49907 = {
		379023,
		406,
		True
	},
	blueprint_simulation_confirm_59901 = {
		379429,
		396,
		True
	},
	blueprint_simulation_confirm_79901 = {
		379825,
		347,
		True
	},
	blueprint_simulation_confirm_89903 = {
		380172,
		416,
		True
	},
	blueprint_simulation_confirm_19904 = {
		380588,
		423,
		True
	},
	blueprint_simulation_confirm_39906 = {
		381011,
		430,
		True
	},
	blueprint_simulation_confirm_49908 = {
		381441,
		441,
		True
	},
	blueprint_simulation_confirm_49909 = {
		381882,
		440,
		True
	},
	blueprint_simulation_confirm_99902 = {
		382322,
		431,
		True
	},
	electrotherapy_wanning = {
		382753,
		125,
		True
	},
	siren_chase_warning = {
		382878,
		104,
		True
	},
	memorybook_get_award_tip = {
		382982,
		173,
		True
	},
	memorybook_notice = {
		383155,
		548,
		True
	},
	word_votes = {
		383703,
		79,
		True
	},
	number_0 = {
		383782,
		73,
		True
	},
	intimacy_desc_propose_vertical = {
		383855,
		340,
		True
	},
	without_selected_ship = {
		384195,
		101,
		True
	},
	index_all = {
		384296,
		76,
		True
	},
	index_fleetfront = {
		384372,
		89,
		True
	},
	index_fleetrear = {
		384461,
		84,
		True
	},
	index_shipType_quZhu = {
		384545,
		86,
		True
	},
	index_shipType_qinXun = {
		384631,
		87,
		True
	},
	index_shipType_zhongXun = {
		384718,
		89,
		True
	},
	index_shipType_zhanLie = {
		384807,
		88,
		True
	},
	index_shipType_hangMu = {
		384895,
		87,
		True
	},
	index_shipType_weiXiu = {
		384982,
		87,
		True
	},
	index_shipType_qianTing = {
		385069,
		89,
		True
	},
	index_other = {
		385158,
		79,
		True
	},
	index_rare2 = {
		385237,
		81,
		True
	},
	index_rare3 = {
		385318,
		79,
		True
	},
	index_rare4 = {
		385397,
		80,
		True
	},
	index_rare5 = {
		385477,
		85,
		True
	},
	index_rare6 = {
		385562,
		80,
		True
	},
	warning_mail_max_1 = {
		385642,
		197,
		True
	},
	warning_mail_max_2 = {
		385839,
		103,
		True
	},
	warning_mail_max_3 = {
		385942,
		196,
		True
	},
	warning_mail_max_4 = {
		386138,
		209,
		True
	},
	warning_mail_max_5 = {
		386347,
		141,
		True
	},
	mail_moveto_markroom_1 = {
		386488,
		223,
		True
	},
	mail_moveto_markroom_2 = {
		386711,
		233,
		True
	},
	mail_moveto_markroom_max = {
		386944,
		186,
		True
	},
	mail_markroom_delete = {
		387130,
		153,
		True
	},
	mail_markroom_tip = {
		387283,
		135,
		True
	},
	mail_manage_1 = {
		387418,
		80,
		True
	},
	mail_manage_2 = {
		387498,
		109,
		True
	},
	mail_manage_3 = {
		387607,
		116,
		True
	},
	mail_manage_tip_1 = {
		387723,
		156,
		True
	},
	mail_storeroom_tips = {
		387879,
		139,
		True
	},
	mail_storeroom_noextend = {
		388018,
		168,
		True
	},
	mail_storeroom_extend = {
		388186,
		111,
		True
	},
	mail_storeroom_extend_1 = {
		388297,
		104,
		True
	},
	mail_storeroom_taken_1 = {
		388401,
		104,
		True
	},
	mail_storeroom_max_1 = {
		388505,
		185,
		True
	},
	mail_storeroom_max_2 = {
		388690,
		136,
		True
	},
	mail_storeroom_addgold = {
		388826,
		103,
		True
	},
	mail_storeroom_addoil = {
		388929,
		100,
		True
	},
	mail_search = {
		389029,
		87,
		True
	},
	mail_storeroom_resourcetaken = {
		389116,
		107,
		True
	},
	resource_max_tip_storeroom = {
		389223,
		131,
		True
	},
	mail_tip = {
		389354,
		1334,
		True
	},
	mail_page_1 = {
		390688,
		79,
		True
	},
	mail_page_2 = {
		390767,
		82,
		True
	},
	mail_page_3 = {
		390849,
		82,
		True
	},
	mail_gold_res = {
		390931,
		82,
		True
	},
	mail_oil_res = {
		391013,
		79,
		True
	},
	mail_all_price = {
		391092,
		84,
		True
	},
	return_award_bind_success = {
		391176,
		110,
		True
	},
	return_award_bind_erro = {
		391286,
		106,
		True
	},
	rename_commander_erro = {
		391392,
		111,
		True
	},
	change_display_medal_success = {
		391503,
		123,
		True
	},
	limit_skin_time_day = {
		391626,
		103,
		True
	},
	limit_skin_time_day_min = {
		391729,
		108,
		True
	},
	limit_skin_time_min = {
		391837,
		106,
		True
	},
	limit_skin_time_overtime = {
		391943,
		136,
		True
	},
	limit_skin_time_before_maintenance = {
		392079,
		110,
		True
	},
	award_window_pt_title = {
		392189,
		101,
		True
	},
	return_have_participated_in_act = {
		392290,
		140,
		True
	},
	input_returner_code = {
		392430,
		92,
		True
	},
	dress_up_success = {
		392522,
		115,
		True
	},
	already_have_the_skin = {
		392637,
		111,
		True
	},
	exchange_limit_skin_tip = {
		392748,
		188,
		True
	},
	returner_help = {
		392936,
		1939,
		True
	},
	attire_time_stamp = {
		394875,
		90,
		True
	},
	pray_build_select_ship_instruction = {
		394965,
		117,
		True
	},
	warning_pray_build_pool = {
		395082,
		212,
		True
	},
	error_pray_select_ship_max = {
		395294,
		113,
		True
	},
	tip_pray_build_pool_success = {
		395407,
		118,
		True
	},
	tip_pray_build_pool_fail = {
		395525,
		116,
		True
	},
	pray_build_help = {
		395641,
		2290,
		True
	},
	pray_build_UR_warning = {
		397931,
		161,
		True
	},
	bismarck_award_tip = {
		398092,
		118,
		True
	},
	bismarck_chapter_desc = {
		398210,
		171,
		True
	},
	returner_push_success = {
		398381,
		115,
		True
	},
	returner_max_count = {
		398496,
		126,
		True
	},
	returner_push_tip = {
		398622,
		240,
		True
	},
	returner_match_tip = {
		398862,
		232,
		True
	},
	return_lock_tip = {
		399094,
		134,
		True
	},
	challenge_help = {
		399228,
		1901,
		True
	},
	challenge_casual_reset = {
		401129,
		138,
		True
	},
	challenge_infinite_reset = {
		401267,
		153,
		True
	},
	challenge_normal_reset = {
		401420,
		132,
		True
	},
	challenge_casual_click_switch = {
		401552,
		184,
		True
	},
	challenge_infinite_click_switch = {
		401736,
		189,
		True
	},
	challenge_season_update = {
		401925,
		126,
		True
	},
	challenge_season_update_casual_clear = {
		402051,
		240,
		True
	},
	challenge_season_update_infinite_clear = {
		402291,
		245,
		True
	},
	challenge_season_update_casual_switch = {
		402536,
		274,
		True
	},
	challenge_season_update_infinite_switch = {
		402810,
		286,
		True
	},
	challenge_combat_score = {
		403096,
		101,
		True
	},
	challenge_share_progress = {
		403197,
		107,
		True
	},
	challenge_share = {
		403304,
		85,
		True
	},
	challenge_expire_warn = {
		403389,
		170,
		True
	},
	challenge_normal_tip = {
		403559,
		146,
		True
	},
	challenge_unlimited_tip = {
		403705,
		151,
		True
	},
	commander_prefab_rename_success = {
		403856,
		118,
		True
	},
	commander_prefab_name = {
		403974,
		92,
		True
	},
	commander_prefab_rename_time = {
		404066,
		145,
		True
	},
	commander_build_solt_deficiency = {
		404211,
		159,
		True
	},
	commander_select_box_tip = {
		404370,
		172,
		True
	},
	challenge_end_tip = {
		404542,
		107,
		True
	},
	pass_times = {
		404649,
		87,
		True
	},
	list_empty_tip_billboardui = {
		404736,
		116,
		True
	},
	list_empty_tip_equipmentdesignui = {
		404852,
		126,
		True
	},
	list_empty_tip_storehouseui_equip = {
		404978,
		121,
		True
	},
	list_empty_tip_storehouseui_item = {
		405099,
		125,
		True
	},
	list_empty_tip_eventui = {
		405224,
		118,
		True
	},
	list_empty_tip_guildrequestui = {
		405342,
		123,
		True
	},
	list_empty_tip_joinguildui = {
		405465,
		137,
		True
	},
	list_empty_tip_friendui = {
		405602,
		114,
		True
	},
	list_empty_tip_friendui_search = {
		405716,
		145,
		True
	},
	list_empty_tip_friendui_request = {
		405861,
		132,
		True
	},
	list_empty_tip_friendui_black = {
		405993,
		136,
		True
	},
	list_empty_tip_dockyardui = {
		406129,
		135,
		True
	},
	list_empty_tip_taskscene = {
		406264,
		120,
		True
	},
	empty_tip_mailboxui = {
		406384,
		117,
		True
	},
	emptymarkroom_tip_mailboxui = {
		406501,
		122,
		True
	},
	empty_tip_mailboxui_en = {
		406623,
		116,
		True
	},
	emptymarkroom_tip_mailboxui_en = {
		406739,
		126,
		True
	},
	words_settings_unlock_ship = {
		406865,
		105,
		True
	},
	words_settings_resolve_equip = {
		406970,
		107,
		True
	},
	words_settings_unlock_commander = {
		407077,
		116,
		True
	},
	words_settings_create_inherit = {
		407193,
		109,
		True
	},
	tips_fail_secondarypwd_much_times = {
		407302,
		185,
		True
	},
	words_desc_unlock = {
		407487,
		131,
		True
	},
	words_desc_resolve_equip = {
		407618,
		138,
		True
	},
	words_desc_create_inherit = {
		407756,
		105,
		True
	},
	words_desc_close_password = {
		407861,
		123,
		True
	},
	words_desc_change_settings = {
		407984,
		137,
		True
	},
	words_set_password = {
		408121,
		107,
		True
	},
	words_information = {
		408228,
		85,
		True
	},
	Word_Ship_Exp_Buff = {
		408313,
		92,
		True
	},
	secondarypassword_incorrectpwd_error = {
		408405,
		193,
		True
	},
	secondary_password_help = {
		408598,
		1501,
		True
	},
	comic_help = {
		410099,
		365,
		True
	},
	secondarypassword_illegal_tip = {
		410464,
		135,
		True
	},
	pt_cosume = {
		410599,
		80,
		True
	},
	secondarypassword_confirm_tips = {
		410679,
		178,
		True
	},
	help_tempesteve = {
		410857,
		800,
		True
	},
	word_rest_times = {
		411657,
		118,
		True
	},
	common_buy_gold_success = {
		411775,
		144,
		True
	},
	harbour_bomb_tip = {
		411919,
		110,
		True
	},
	submarine_approach = {
		412029,
		101,
		True
	},
	submarine_approach_desc = {
		412130,
		130,
		True
	},
	desc_quick_play = {
		412260,
		91,
		True
	},
	text_win_condition = {
		412351,
		97,
		True
	},
	text_lose_condition = {
		412448,
		99,
		True
	},
	text_rest_HP = {
		412547,
		93,
		True
	},
	desc_defense_reward = {
		412640,
		152,
		True
	},
	desc_base_hp = {
		412792,
		99,
		True
	},
	map_event_open = {
		412891,
		105,
		True
	},
	word_reward = {
		412996,
		82,
		True
	},
	tips_dispense_completed = {
		413078,
		103,
		True
	},
	tips_firework_completed = {
		413181,
		116,
		True
	},
	help_summer_feast = {
		413297,
		1164,
		True
	},
	help_firework_produce = {
		414461,
		668,
		True
	},
	help_firework = {
		415129,
		1685,
		True
	},
	help_summer_shrine = {
		416814,
		1066,
		True
	},
	help_summer_food = {
		417880,
		1622,
		True
	},
	help_summer_shooting = {
		419502,
		1075,
		True
	},
	help_summer_stamp = {
		420577,
		341,
		True
	},
	tips_summergame_exit = {
		420918,
		198,
		True
	},
	tips_shrine_buff = {
		421116,
		121,
		True
	},
	tips_shrine_nobuff = {
		421237,
		175,
		True
	},
	paint_hide_other_obj_tip = {
		421412,
		111,
		True
	},
	help_vote = {
		421523,
		6103,
		True
	},
	tips_firework_exit = {
		427626,
		157,
		True
	},
	result_firework_produce = {
		427783,
		148,
		True
	},
	tag_level_narrative = {
		427931,
		88,
		True
	},
	vote_get_book = {
		428019,
		115,
		True
	},
	vote_book_is_over = {
		428134,
		115,
		True
	},
	vote_fame_tip = {
		428249,
		167,
		True
	},
	word_maintain = {
		428416,
		94,
		True
	},
	name_zhanliejahe = {
		428510,
		97,
		True
	},
	change_skin_secretary_ship_success = {
		428607,
		124,
		True
	},
	change_skin_secretary_ship = {
		428731,
		103,
		True
	},
	word_billboard = {
		428834,
		86,
		True
	},
	word_easy = {
		428920,
		77,
		True
	},
	word_normal_junhe = {
		428997,
		87,
		True
	},
	word_hard = {
		429084,
		77,
		True
	},
	word_special_challenge_ticket = {
		429161,
		105,
		True
	},
	tip_exchange_ticket = {
		429266,
		177,
		True
	},
	dont_remind = {
		429443,
		89,
		True
	},
	worldbossex_help = {
		429532,
		909,
		True
	},
	ship_formationUI_fleetName_easy = {
		430441,
		99,
		True
	},
	ship_formationUI_fleetName_normal = {
		430540,
		103,
		True
	},
	ship_formationUI_fleetName_hard = {
		430643,
		99,
		True
	},
	ship_formationUI_fleetName_extra = {
		430742,
		98,
		True
	},
	ship_formationUI_fleetName_easy_ss = {
		430840,
		114,
		True
	},
	ship_formationUI_fleetName_normal_ss = {
		430954,
		118,
		True
	},
	ship_formationUI_fleetName_hard_ss = {
		431072,
		114,
		True
	},
	ship_formationUI_fleetName_extra_ss = {
		431186,
		113,
		True
	},
	text_consume = {
		431299,
		80,
		True
	},
	text_inconsume = {
		431379,
		80,
		True
	},
	pt_ship_now = {
		431459,
		93,
		True
	},
	pt_ship_goal = {
		431552,
		81,
		True
	},
	option_desc1 = {
		431633,
		165,
		True
	},
	option_desc2 = {
		431798,
		158,
		True
	},
	option_desc3 = {
		431956,
		167,
		True
	},
	option_desc4 = {
		432123,
		202,
		True
	},
	option_desc5 = {
		432325,
		140,
		True
	},
	option_desc6 = {
		432465,
		155,
		True
	},
	option_desc10 = {
		432620,
		143,
		True
	},
	option_desc11 = {
		432763,
		1748,
		True
	},
	music_collection = {
		434511,
		859,
		True
	},
	music_main = {
		435370,
		1073,
		True
	},
	music_juus = {
		436443,
		574,
		True
	},
	doa_collection = {
		437017,
		846,
		True
	},
	ins_word_day = {
		437863,
		88,
		True
	},
	ins_word_hour = {
		437951,
		89,
		True
	},
	ins_word_minu = {
		438040,
		91,
		True
	},
	ins_word_like = {
		438131,
		85,
		True
	},
	ins_click_like_success = {
		438216,
		106,
		True
	},
	ins_push_comment_success = {
		438322,
		120,
		True
	},
	skinshop_live2d_fliter_failed = {
		438442,
		146,
		True
	},
	help_music_game = {
		438588,
		1355,
		True
	},
	restart_music_game = {
		439943,
		130,
		True
	},
	reselect_music_game = {
		440073,
		144,
		True
	},
	hololive_goodmorning = {
		440217,
		852,
		True
	},
	hololive_lianliankan = {
		441069,
		1410,
		True
	},
	hololive_dalaozhang = {
		442479,
		764,
		True
	},
	hololive_dashenling = {
		443243,
		1927,
		True
	},
	pocky_jiujiu = {
		445170,
		94,
		True
	},
	pocky_jiujiu_desc = {
		445264,
		118,
		True
	},
	pocky_help = {
		445382,
		697,
		True
	},
	secretary_help = {
		446079,
		2209,
		True
	},
	secretary_unlock2 = {
		448288,
		108,
		True
	},
	secretary_unlock3 = {
		448396,
		108,
		True
	},
	secretary_unlock4 = {
		448504,
		108,
		True
	},
	secretary_unlock5 = {
		448612,
		109,
		True
	},
	secretary_closed = {
		448721,
		88,
		True
	},
	confirm_unlock = {
		448809,
		113,
		True
	},
	secretary_pos_save = {
		448922,
		143,
		True
	},
	secretary_pos_save_success = {
		449065,
		105,
		True
	},
	collection_help = {
		449170,
		346,
		True
	},
	juese_tiyan = {
		449516,
		239,
		True
	},
	resolve_amount_prefix = {
		449755,
		104,
		True
	},
	compose_amount_prefix = {
		449859,
		100,
		True
	},
	help_sub_limits = {
		449959,
		92,
		True
	},
	help_sub_display = {
		450051,
		104,
		True
	},
	confirm_unlock_ship_main = {
		450155,
		151,
		True
	},
	msgbox_text_confirm = {
		450306,
		90,
		True
	},
	msgbox_text_shop = {
		450396,
		85,
		True
	},
	msgbox_text_cancel = {
		450481,
		88,
		True
	},
	msgbox_text_cancel_g = {
		450569,
		90,
		True
	},
	msgbox_text_cancel_fight = {
		450659,
		100,
		True
	},
	msgbox_text_goon_fight = {
		450759,
		94,
		True
	},
	msgbox_text_exit = {
		450853,
		84,
		True
	},
	msgbox_text_clear = {
		450937,
		86,
		True
	},
	msgbox_text_apply = {
		451023,
		85,
		True
	},
	msgbox_text_buy = {
		451108,
		87,
		True
	},
	msgbox_text_noPos_buy = {
		451195,
		91,
		True
	},
	msgbox_text_noPos_clear = {
		451286,
		91,
		True
	},
	msgbox_text_noPos_intensify = {
		451377,
		98,
		True
	},
	msgbox_text_forward = {
		451475,
		85,
		True
	},
	msgbox_text_iknow = {
		451560,
		87,
		True
	},
	msgbox_text_prepage = {
		451647,
		87,
		True
	},
	msgbox_text_nextpage = {
		451734,
		88,
		True
	},
	msgbox_text_exchange = {
		451822,
		92,
		True
	},
	msgbox_text_retreat = {
		451914,
		90,
		True
	},
	msgbox_text_go = {
		452004,
		80,
		True
	},
	msgbox_text_consume = {
		452084,
		87,
		True
	},
	msgbox_text_inconsume = {
		452171,
		87,
		True
	},
	msgbox_text_unlock = {
		452258,
		88,
		True
	},
	msgbox_text_save = {
		452346,
		85,
		True
	},
	msgbox_text_replace = {
		452431,
		88,
		True
	},
	msgbox_text_unload = {
		452519,
		89,
		True
	},
	msgbox_text_modify = {
		452608,
		89,
		True
	},
	msgbox_text_breakthrough = {
		452697,
		93,
		True
	},
	msgbox_text_equipdetail = {
		452790,
		94,
		True
	},
	msgbox_text_use = {
		452884,
		82,
		True
	},
	common_flag_ship = {
		452966,
		89,
		True
	},
	fenjie_lantu_tip = {
		453055,
		188,
		True
	},
	msgbox_text_analyse = {
		453243,
		90,
		True
	},
	fragresolve_empty_tip = {
		453333,
		151,
		True
	},
	confirm_unlock_lv = {
		453484,
		121,
		True
	},
	shops_rest_day = {
		453605,
		98,
		True
	},
	title_limit_time = {
		453703,
		91,
		True
	},
	seven_choose_one = {
		453794,
		224,
		True
	},
	help_newyear_feast = {
		454018,
		1386,
		True
	},
	help_newyear_shrine = {
		455404,
		1243,
		True
	},
	help_newyear_stamp = {
		456647,
		238,
		True
	},
	pt_reconfirm = {
		456885,
		124,
		True
	},
	qte_game_help = {
		457009,
		340,
		True
	},
	word_equipskin_type = {
		457349,
		88,
		True
	},
	word_equipskin_all = {
		457437,
		86,
		True
	},
	word_equipskin_cannon = {
		457523,
		95,
		True
	},
	word_equipskin_tarpedo = {
		457618,
		96,
		True
	},
	word_equipskin_aircraft = {
		457714,
		96,
		True
	},
	word_equipskin_aux = {
		457810,
		86,
		True
	},
	msgbox_repair = {
		457896,
		91,
		True
	},
	msgbox_repair_l2d = {
		457987,
		95,
		True
	},
	msgbox_repair_painting = {
		458082,
		105,
		True
	},
	word_no_cache = {
		458187,
		107,
		True
	},
	pile_game_notice = {
		458294,
		993,
		True
	},
	help_chunjie_stamp = {
		459287,
		677,
		True
	},
	help_chunjie_feast = {
		459964,
		670,
		True
	},
	help_chunjie_jiulou = {
		460634,
		848,
		True
	},
	special_animal1 = {
		461482,
		227,
		True
	},
	special_animal2 = {
		461709,
		287,
		True
	},
	special_animal3 = {
		461996,
		236,
		True
	},
	special_animal4 = {
		462232,
		256,
		True
	},
	special_animal5 = {
		462488,
		251,
		True
	},
	special_animal6 = {
		462739,
		272,
		True
	},
	special_animal7 = {
		463011,
		275,
		True
	},
	bulin_help = {
		463286,
		403,
		True
	},
	super_bulin = {
		463689,
		120,
		True
	},
	super_bulin_tip = {
		463809,
		110,
		True
	},
	bulin_tip1 = {
		463919,
		101,
		True
	},
	bulin_tip2 = {
		464020,
		117,
		True
	},
	bulin_tip3 = {
		464137,
		101,
		True
	},
	bulin_tip4 = {
		464238,
		108,
		True
	},
	bulin_tip5 = {
		464346,
		101,
		True
	},
	bulin_tip6 = {
		464447,
		108,
		True
	},
	bulin_tip7 = {
		464555,
		101,
		True
	},
	bulin_tip8 = {
		464656,
		126,
		True
	},
	bulin_tip9 = {
		464782,
		122,
		True
	},
	bulin_tip_other1 = {
		464904,
		192,
		True
	},
	bulin_tip_other2 = {
		465096,
		109,
		True
	},
	bulin_tip_other3 = {
		465205,
		122,
		True
	},
	monopoly_left_count = {
		465327,
		89,
		True
	},
	help_chunjie_monopoly = {
		465416,
		1083,
		True
	},
	monoply_drop_ship_step = {
		466499,
		157,
		True
	},
	lanternRiddles_wait_for_reanswer = {
		466656,
		144,
		True
	},
	lanternRiddles_answer_is_wrong = {
		466800,
		118,
		True
	},
	lanternRiddles_answer_is_right = {
		466918,
		110,
		True
	},
	lanternRiddles_gametip = {
		467028,
		607,
		True
	},
	LanternRiddle_wait_time_tip = {
		467635,
		105,
		True
	},
	LinkLinkGame_BestTime = {
		467740,
		92,
		True
	},
	LinkLinkGame_CurTime = {
		467832,
		89,
		True
	},
	sort_attribute = {
		467921,
		82,
		True
	},
	sort_intimacy = {
		468003,
		85,
		True
	},
	index_skin = {
		468088,
		82,
		True
	},
	index_reform = {
		468170,
		94,
		True
	},
	index_reform_cw = {
		468264,
		97,
		True
	},
	index_strengthen = {
		468361,
		91,
		True
	},
	index_special = {
		468452,
		84,
		True
	},
	index_propose_skin = {
		468536,
		96,
		True
	},
	index_not_obtained = {
		468632,
		94,
		True
	},
	index_no_limit = {
		468726,
		86,
		True
	},
	index_awakening = {
		468812,
		91,
		True
	},
	index_not_lvmax = {
		468903,
		90,
		True
	},
	index_spweapon = {
		468993,
		91,
		True
	},
	index_marry = {
		469084,
		81,
		True
	},
	decodegame_gametip = {
		469165,
		2081,
		True
	},
	indexsort_sort = {
		471246,
		82,
		True
	},
	indexsort_index = {
		471328,
		84,
		True
	},
	indexsort_camp = {
		471412,
		85,
		True
	},
	indexsort_type = {
		471497,
		82,
		True
	},
	indexsort_rarity = {
		471579,
		86,
		True
	},
	indexsort_extraindex = {
		471665,
		89,
		True
	},
	indexsort_label = {
		471754,
		83,
		True
	},
	indexsort_sorteng = {
		471837,
		85,
		True
	},
	indexsort_indexeng = {
		471922,
		87,
		True
	},
	indexsort_campeng = {
		472009,
		88,
		True
	},
	indexsort_rarityeng = {
		472097,
		89,
		True
	},
	indexsort_typeeng = {
		472186,
		85,
		True
	},
	indexsort_labeleng = {
		472271,
		86,
		True
	},
	fightfail_up = {
		472357,
		139,
		True
	},
	fightfail_equip = {
		472496,
		141,
		True
	},
	fight_strengthen = {
		472637,
		158,
		True
	},
	fightfail_noequip = {
		472795,
		107,
		True
	},
	fightfail_choiceequip = {
		472902,
		136,
		True
	},
	fightfail_choicestrengthen = {
		473038,
		151,
		True
	},
	sofmap_attention = {
		473189,
		258,
		True
	},
	sofmapsd_1 = {
		473447,
		153,
		True
	},
	sofmapsd_2 = {
		473600,
		132,
		True
	},
	sofmapsd_3 = {
		473732,
		110,
		True
	},
	sofmapsd_4 = {
		473842,
		133,
		True
	},
	inform_level_limit = {
		473975,
		138,
		True
	},
	["3match_tip"] = {
		474113,
		381,
		True
	},
	retire_selectzero = {
		474494,
		138,
		True
	},
	retire_marry_skin = {
		474632,
		106,
		True
	},
	undermist_tip = {
		474738,
		143,
		True
	},
	retire_1 = {
		474881,
		254,
		True
	},
	retire_2 = {
		475135,
		256,
		True
	},
	retire_3 = {
		475391,
		96,
		True
	},
	retire_rarity = {
		475487,
		97,
		True
	},
	retire_title = {
		475584,
		96,
		True
	},
	res_unlock_tip = {
		475680,
		120,
		True
	},
	res_wifi_tip = {
		475800,
		206,
		True
	},
	res_downloading = {
		476006,
		90,
		True
	},
	res_pic_new_tip = {
		476096,
		145,
		True
	},
	res_music_no_pre_tip = {
		476241,
		95,
		True
	},
	res_music_no_next_tip = {
		476336,
		95,
		True
	},
	res_music_new_tip = {
		476431,
		106,
		True
	},
	apple_link_title = {
		476537,
		101,
		True
	},
	retire_setting_help = {
		476638,
		863,
		True
	},
	activity_shop_exchange_count = {
		477501,
		98,
		True
	},
	shops_msgbox_exchange_count = {
		477599,
		107,
		True
	},
	shops_msgbox_output = {
		477706,
		92,
		True
	},
	shop_word_exchange = {
		477798,
		89,
		True
	},
	shop_word_cancel = {
		477887,
		86,
		True
	},
	title_item_ways = {
		477973,
		152,
		True
	},
	item_lack_title = {
		478125,
		152,
		True
	},
	oil_buy_tip_2 = {
		478277,
		386,
		True
	},
	target_chapter_is_lock = {
		478663,
		126,
		True
	},
	ship_book = {
		478789,
		104,
		True
	},
	month_sign_resign = {
		478893,
		87,
		True
	},
	collect_tip = {
		478980,
		139,
		True
	},
	collect_tip2 = {
		479119,
		140,
		True
	},
	word_weakness = {
		479259,
		88,
		True
	},
	special_operation_tip1 = {
		479347,
		111,
		True
	},
	special_operation_tip2 = {
		479458,
		111,
		True
	},
	area_lock = {
		479569,
		106,
		True
	},
	equipment_upgrade_equipped_tag = {
		479675,
		105,
		True
	},
	equipment_upgrade_spare_tag = {
		479780,
		102,
		True
	},
	equipment_upgrade_help = {
		479882,
		1285,
		True
	},
	equipment_upgrade_title = {
		481167,
		97,
		True
	},
	equipment_upgrade_coin_consume = {
		481264,
		98,
		True
	},
	equipment_upgrade_quick_interface_source_chosen = {
		481362,
		123,
		True
	},
	equipment_upgrade_quick_interface_materials_consume = {
		481485,
		121,
		True
	},
	equipment_upgrade_feedback_lack_of_materials = {
		481606,
		141,
		True
	},
	equipment_upgrade_feedback_equipment_consume = {
		481747,
		211,
		True
	},
	equipment_upgrade_feedback_equipment_can_be_produced = {
		481958,
		168,
		True
	},
	equipment_upgrade_quick_interface_feedback_source_chosen = {
		482126,
		133,
		True
	},
	equipment_upgrade_feedback_lack_of_equipment = {
		482259,
		127,
		True
	},
	equipment_upgrade_equipped_unavailable = {
		482386,
		211,
		True
	},
	equipment_upgrade_initial_node = {
		482597,
		134,
		True
	},
	equipment_upgrade_feedback_compose_tip = {
		482731,
		192,
		True
	},
	discount_coupon_tip = {
		482923,
		193,
		True
	},
	pizzahut_help = {
		483116,
		738,
		True
	},
	towerclimbing_gametip = {
		483854,
		645,
		True
	},
	qingdianguangchang_help = {
		484499,
		660,
		True
	},
	building_tip = {
		485159,
		177,
		True
	},
	building_upgrade_tip = {
		485336,
		155,
		True
	},
	msgbox_text_upgrade = {
		485491,
		90,
		True
	},
	towerclimbing_sign_help = {
		485581,
		793,
		True
	},
	building_complete_tip = {
		486374,
		102,
		True
	},
	backyard_theme_refresh_time_tip = {
		486476,
		124,
		True
	},
	backyard_theme_total_print = {
		486600,
		95,
		True
	},
	backyard_theme_shop_title = {
		486695,
		105,
		True
	},
	backyard_theme_mine_title = {
		486800,
		99,
		True
	},
	backyard_theme_collection_title = {
		486899,
		107,
		True
	},
	backyard_theme_ban_upload_tip = {
		487006,
		214,
		True
	},
	backyard_theme_upload_over_maxcnt = {
		487220,
		194,
		True
	},
	backyard_theme_apply_tip1 = {
		487414,
		208,
		True
	},
	backyard_theme_word_buy = {
		487622,
		90,
		True
	},
	backyard_theme_word_apply = {
		487712,
		94,
		True
	},
	backyard_theme_apply_success = {
		487806,
		105,
		True
	},
	backyard_theme_unload_success = {
		487911,
		109,
		True
	},
	backyard_theme_upload_success = {
		488020,
		101,
		True
	},
	backyard_theme_delete_success = {
		488121,
		100,
		True
	},
	backyard_theme_apply_tip2 = {
		488221,
		138,
		True
	},
	backyard_theme_upload_cnt = {
		488359,
		113,
		True
	},
	backyard_theme_upload_time = {
		488472,
		102,
		True
	},
	backyard_theme_word_like = {
		488574,
		93,
		True
	},
	backyard_theme_word_collection = {
		488667,
		103,
		True
	},
	backyard_theme_cancel_collection = {
		488770,
		138,
		True
	},
	backyard_theme_inform_them = {
		488908,
		105,
		True
	},
	open_backyard_theme_template_tip = {
		489013,
		143,
		True
	},
	backyard_theme_cancel_template_upload_tip = {
		489156,
		249,
		True
	},
	backyard_theme_delete_themplate_tip = {
		489405,
		228,
		True
	},
	backyard_theme_template_be_delete_tip = {
		489633,
		140,
		True
	},
	backyard_theme_template_collection_cnt_max = {
		489773,
		143,
		True
	},
	backyard_theme_template_collection_cnt = {
		489916,
		120,
		True
	},
	words_visit_backyard_toggle = {
		490036,
		124,
		True
	},
	words_show_friend_backyardship_toggle = {
		490160,
		154,
		True
	},
	words_show_my_backyardship_toggle = {
		490314,
		154,
		True
	},
	option_desc7 = {
		490468,
		133,
		True
	},
	option_desc8 = {
		490601,
		147,
		True
	},
	option_desc9 = {
		490748,
		174,
		True
	},
	backyard_unopen = {
		490922,
		108,
		True
	},
	backyard_shop_refresh_frequently = {
		491030,
		157,
		True
	},
	word_random = {
		491187,
		81,
		True
	},
	word_hot = {
		491268,
		75,
		True
	},
	word_new = {
		491343,
		75,
		True
	},
	backyard_decoration_theme_template_delete_tip = {
		491418,
		210,
		True
	},
	backyard_not_found_theme_template = {
		491628,
		128,
		True
	},
	backyard_apply_theme_template_erro = {
		491756,
		122,
		True
	},
	backyard_theme_template_list_is_empty = {
		491878,
		121,
		True
	},
	BackYard_collection_be_delete_tip = {
		491999,
		181,
		True
	},
	help_monopoly_car = {
		492180,
		1056,
		True
	},
	help_monopoly_car_2 = {
		493236,
		1125,
		True
	},
	help_monopoly_3th = {
		494361,
		795,
		True
	},
	backYard_missing_furniTrue_tip = {
		495156,
		114,
		True
	},
	win_condition_display_qijian = {
		495270,
		120,
		True
	},
	win_condition_display_qijian_tip = {
		495390,
		126,
		True
	},
	win_condition_display_shangchuan = {
		495516,
		151,
		True
	},
	win_condition_display_shangchuan_tip = {
		495667,
		170,
		True
	},
	win_condition_display_judian = {
		495837,
		116,
		True
	},
	win_condition_display_tuoli = {
		495953,
		126,
		True
	},
	win_condition_display_tuoli_tip = {
		496079,
		130,
		True
	},
	lose_condition_display_quanmie = {
		496209,
		123,
		True
	},
	lose_condition_display_gangqu = {
		496332,
		155,
		True
	},
	re_battle = {
		496487,
		79,
		True
	},
	keep_fate_tip = {
		496566,
		148,
		True
	},
	equip_info_1 = {
		496714,
		79,
		True
	},
	equip_info_2 = {
		496793,
		84,
		True
	},
	equip_info_3 = {
		496877,
		89,
		True
	},
	equip_info_4 = {
		496966,
		81,
		True
	},
	equip_info_5 = {
		497047,
		85,
		True
	},
	equip_info_6 = {
		497132,
		90,
		True
	},
	equip_info_7 = {
		497222,
		86,
		True
	},
	equip_info_8 = {
		497308,
		86,
		True
	},
	equip_info_9 = {
		497394,
		90,
		True
	},
	equip_info_10 = {
		497484,
		85,
		True
	},
	equip_info_11 = {
		497569,
		85,
		True
	},
	equip_info_12 = {
		497654,
		89,
		True
	},
	equip_info_13 = {
		497743,
		86,
		True
	},
	equip_info_14 = {
		497829,
		92,
		True
	},
	equip_info_15 = {
		497921,
		87,
		True
	},
	equip_info_16 = {
		498008,
		89,
		True
	},
	equip_info_17 = {
		498097,
		88,
		True
	},
	equip_info_18 = {
		498185,
		89,
		True
	},
	equip_info_19 = {
		498274,
		84,
		True
	},
	equip_info_20 = {
		498358,
		88,
		True
	},
	equip_info_21 = {
		498446,
		85,
		True
	},
	equip_info_22 = {
		498531,
		91,
		True
	},
	equip_info_23 = {
		498622,
		90,
		True
	},
	equip_info_24 = {
		498712,
		86,
		True
	},
	equip_info_25 = {
		498798,
		77,
		True
	},
	equip_info_26 = {
		498875,
		90,
		True
	},
	equip_info_27 = {
		498965,
		77,
		True
	},
	equip_info_28 = {
		499042,
		93,
		True
	},
	equip_info_29 = {
		499135,
		80,
		True
	},
	equip_info_30 = {
		499215,
		80,
		True
	},
	equip_info_31 = {
		499295,
		80,
		True
	},
	equip_info_32 = {
		499375,
		91,
		True
	},
	equip_info_33 = {
		499466,
		89,
		True
	},
	equip_info_34 = {
		499555,
		90,
		True
	},
	equip_info_extralevel_0 = {
		499645,
		94,
		True
	},
	equip_info_extralevel_1 = {
		499739,
		94,
		True
	},
	equip_info_extralevel_2 = {
		499833,
		94,
		True
	},
	equip_info_extralevel_3 = {
		499927,
		94,
		True
	},
	tec_settings_btn_word = {
		500021,
		99,
		True
	},
	tec_tendency_x = {
		500120,
		86,
		True
	},
	tec_tendency_0 = {
		500206,
		86,
		True
	},
	tec_tendency_1 = {
		500292,
		87,
		True
	},
	tec_tendency_2 = {
		500379,
		87,
		True
	},
	tec_tendency_3 = {
		500466,
		87,
		True
	},
	tec_tendency_4 = {
		500553,
		87,
		True
	},
	tec_tendency_cur_x = {
		500640,
		101,
		True
	},
	tec_tendency_cur_0 = {
		500741,
		108,
		True
	},
	tec_tendency_cur_1 = {
		500849,
		107,
		True
	},
	tec_tendency_cur_2 = {
		500956,
		107,
		True
	},
	tec_tendency_cur_3 = {
		501063,
		107,
		True
	},
	tec_target_catchup_none = {
		501170,
		117,
		True
	},
	tec_target_catchup_selected = {
		501287,
		105,
		True
	},
	tec_tendency_cur_4 = {
		501392,
		107,
		True
	},
	tec_target_catchup_none_x = {
		501499,
		108,
		True
	},
	tec_target_catchup_none_1 = {
		501607,
		107,
		True
	},
	tec_target_catchup_none_2 = {
		501714,
		107,
		True
	},
	tec_target_catchup_none_3 = {
		501821,
		107,
		True
	},
	tec_target_catchup_selected_x = {
		501928,
		108,
		True
	},
	tec_target_catchup_selected_1 = {
		502036,
		107,
		True
	},
	tec_target_catchup_selected_2 = {
		502143,
		107,
		True
	},
	tec_target_catchup_selected_3 = {
		502250,
		107,
		True
	},
	tec_target_catchup_finish_x = {
		502357,
		106,
		True
	},
	tec_target_catchup_finish_1 = {
		502463,
		105,
		True
	},
	tec_target_catchup_finish_2 = {
		502568,
		105,
		True
	},
	tec_target_catchup_finish_3 = {
		502673,
		105,
		True
	},
	tec_target_catchup_finish_4 = {
		502778,
		105,
		True
	},
	tec_target_catchup_dr_finish_tip = {
		502883,
		113,
		True
	},
	tec_target_catchup_all_finish_tip = {
		502996,
		114,
		True
	},
	tec_target_catchup_show_the_finished_version = {
		503110,
		133,
		True
	},
	tec_target_catchup_pry_char = {
		503243,
		99,
		True
	},
	tec_target_catchup_dr_char = {
		503342,
		98,
		True
	},
	tec_target_need_print = {
		503440,
		98,
		True
	},
	tec_target_catchup_progress = {
		503538,
		99,
		True
	},
	tec_target_catchup_select_tip = {
		503637,
		135,
		True
	},
	tec_target_catchup_help_tip = {
		503772,
		824,
		True
	},
	tec_speedup_title = {
		504596,
		102,
		True
	},
	tec_speedup_progress = {
		504698,
		94,
		True
	},
	tec_speedup_overflow = {
		504792,
		186,
		True
	},
	tec_speedup_help_tip = {
		504978,
		274,
		True
	},
	click_back_tip = {
		505252,
		92,
		True
	},
	tech_catchup_sentence_pauses = {
		505344,
		95,
		True
	},
	tec_act_catchup_btn_word = {
		505439,
		103,
		True
	},
	tec_catchup_errorfix = {
		505542,
		226,
		True
	},
	guild_duty_is_too_low = {
		505768,
		149,
		True
	},
	guild_trainee_duty_change_tip = {
		505917,
		144,
		True
	},
	guild_not_exist_donate_task = {
		506061,
		121,
		True
	},
	guild_week_task_state_is_wrong = {
		506182,
		131,
		True
	},
	guild_get_week_done = {
		506313,
		127,
		True
	},
	guild_public_awards = {
		506440,
		97,
		True
	},
	guild_private_awards = {
		506537,
		99,
		True
	},
	guild_task_selecte_tip = {
		506636,
		276,
		True
	},
	guild_task_accept = {
		506912,
		374,
		True
	},
	guild_commander_and_sub_op = {
		507286,
		152,
		True
	},
	["guild_donate_times_not enough"] = {
		507438,
		144,
		True
	},
	guild_donate_success = {
		507582,
		108,
		True
	},
	guild_left_donate_cnt = {
		507690,
		118,
		True
	},
	guild_donate_tip = {
		507808,
		228,
		True
	},
	guild_donate_addition_capital_tip = {
		508036,
		125,
		True
	},
	guild_donate_addition_techpoint_tip = {
		508161,
		141,
		True
	},
	guild_donate_capital_toplimit = {
		508302,
		151,
		True
	},
	guild_donate_techpoint_toplimit = {
		508453,
		153,
		True
	},
	guild_supply_no_open = {
		508606,
		121,
		True
	},
	guild_supply_award_got = {
		508727,
		119,
		True
	},
	guild_new_member_get_award_tip = {
		508846,
		181,
		True
	},
	guild_start_supply_consume_tip = {
		509027,
		143,
		True
	},
	guild_left_supply_day = {
		509170,
		99,
		True
	},
	guild_supply_help_tip = {
		509269,
		731,
		True
	},
	guild_op_only_administrator = {
		510000,
		153,
		True
	},
	guild_shop_refresh_done = {
		510153,
		102,
		True
	},
	guild_shop_cnt_no_enough = {
		510255,
		113,
		True
	},
	guild_shop_refresh_all_tip = {
		510368,
		205,
		True
	},
	guild_shop_exchange_tip = {
		510573,
		128,
		True
	},
	guild_shop_label_1 = {
		510701,
		115,
		True
	},
	guild_shop_label_2 = {
		510816,
		87,
		True
	},
	guild_shop_label_3 = {
		510903,
		89,
		True
	},
	guild_shop_label_4 = {
		510992,
		86,
		True
	},
	guild_shop_label_5 = {
		511078,
		119,
		True
	},
	guild_shop_must_select_goods = {
		511197,
		125,
		True
	},
	guild_not_exist_activation_tech = {
		511322,
		143,
		True
	},
	guild_not_exist_tech = {
		511465,
		119,
		True
	},
	guild_cancel_only_once_pre_day = {
		511584,
		144,
		True
	},
	guild_tech_is_max_level = {
		511728,
		132,
		True
	},
	guild_tech_gold_no_enough = {
		511860,
		141,
		True
	},
	guild_tech_guildgold_no_enough = {
		512001,
		153,
		True
	},
	guild_tech_upgrade_done = {
		512154,
		118,
		True
	},
	guild_exist_activation_tech = {
		512272,
		136,
		True
	},
	guild_tech_gold_desc = {
		512408,
		105,
		True
	},
	guild_tech_oil_desc = {
		512513,
		102,
		True
	},
	guild_tech_shipbag_desc = {
		512615,
		101,
		True
	},
	guild_tech_equipbag_desc = {
		512716,
		107,
		True
	},
	guild_box_gold_desc = {
		512823,
		99,
		True
	},
	guidl_r_box_time_desc = {
		512922,
		115,
		True
	},
	guidl_sr_box_time_desc = {
		513037,
		117,
		True
	},
	guidl_ssr_box_time_desc = {
		513154,
		123,
		True
	},
	guild_member_max_cnt_desc = {
		513277,
		110,
		True
	},
	guild_tech_livness_no_enough = {
		513387,
		271,
		True
	},
	guild_tech_livness_no_enough_label = {
		513658,
		126,
		True
	},
	guild_ship_attr_desc = {
		513784,
		133,
		True
	},
	guild_start_tech_group_tip = {
		513917,
		164,
		True
	},
	guild_cancel_tech_tip = {
		514081,
		182,
		True
	},
	guild_tech_consume_tip = {
		514263,
		219,
		True
	},
	guild_tech_non_admin = {
		514482,
		146,
		True
	},
	guild_tech_label_max_level = {
		514628,
		100,
		True
	},
	guild_tech_label_dev_progress = {
		514728,
		102,
		True
	},
	guild_tech_label_condition = {
		514830,
		131,
		True
	},
	guild_tech_donate_target = {
		514961,
		122,
		True
	},
	guild_not_exist = {
		515083,
		105,
		True
	},
	guild_not_exist_battle = {
		515188,
		126,
		True
	},
	guild_battle_is_end = {
		515314,
		121,
		True
	},
	guild_battle_is_exist = {
		515435,
		126,
		True
	},
	guild_guildgold_no_enough_for_battle = {
		515561,
		164,
		True
	},
	guild_event_start_tip1 = {
		515725,
		167,
		True
	},
	guild_event_start_tip2 = {
		515892,
		168,
		True
	},
	guild_word_may_happen_event = {
		516060,
		106,
		True
	},
	guild_battle_award = {
		516166,
		90,
		True
	},
	guild_word_consume = {
		516256,
		87,
		True
	},
	guild_start_event_consume_tip = {
		516343,
		149,
		True
	},
	guild_start_event_consume_tip_extra = {
		516492,
		222,
		True
	},
	guild_word_consume_for_battle = {
		516714,
		99,
		True
	},
	guild_level_no_enough = {
		516813,
		159,
		True
	},
	guild_open_event_info_when_exist_active = {
		516972,
		170,
		True
	},
	guild_join_event_cnt_label = {
		517142,
		117,
		True
	},
	guild_join_event_max_cnt_tip = {
		517259,
		124,
		True
	},
	guild_join_event_progress_label = {
		517383,
		104,
		True
	},
	guild_join_event_exist_finished_mission_tip = {
		517487,
		277,
		True
	},
	guild_event_not_exist = {
		517764,
		119,
		True
	},
	guild_fleet_can_not_edit = {
		517883,
		131,
		True
	},
	guild_fleet_exist_same_kind_ship = {
		518014,
		151,
		True
	},
	guild_event_exist_same_kind_ship = {
		518165,
		171,
		True
	},
	guidl_event_ship_in_event = {
		518336,
		150,
		True
	},
	guild_event_start_done = {
		518486,
		110,
		True
	},
	guild_fleet_update_done = {
		518596,
		122,
		True
	},
	guild_event_is_lock = {
		518718,
		115,
		True
	},
	guild_event_is_finish = {
		518833,
		161,
		True
	},
	guild_fleet_not_save_tip = {
		518994,
		161,
		True
	},
	guild_word_battle_area = {
		519155,
		91,
		True
	},
	guild_word_battle_type = {
		519246,
		91,
		True
	},
	guild_wrod_battle_target = {
		519337,
		99,
		True
	},
	guild_event_recomm_ship_failed = {
		519436,
		139,
		True
	},
	guild_event_start_event_tip = {
		519575,
		208,
		True
	},
	guild_word_sea = {
		519783,
		83,
		True
	},
	guild_word_score_addition = {
		519866,
		106,
		True
	},
	guild_word_effect_addition = {
		519972,
		111,
		True
	},
	guild_curr_fleet_can_not_edit = {
		520083,
		127,
		True
	},
	guild_next_edit_fleet_time = {
		520210,
		125,
		True
	},
	guild_event_info_desc1 = {
		520335,
		197,
		True
	},
	guild_event_info_desc2 = {
		520532,
		128,
		True
	},
	guild_join_member_cnt = {
		520660,
		98,
		True
	},
	guild_total_effect = {
		520758,
		99,
		True
	},
	guild_word_people = {
		520857,
		81,
		True
	},
	guild_event_info_desc3 = {
		520938,
		104,
		True
	},
	guild_not_exist_boss = {
		521042,
		112,
		True
	},
	guild_ship_from = {
		521154,
		84,
		True
	},
	guild_boss_formation_1 = {
		521238,
		160,
		True
	},
	guild_boss_formation_2 = {
		521398,
		146,
		True
	},
	guild_boss_formation_3 = {
		521544,
		123,
		True
	},
	guild_boss_cnt_no_enough = {
		521667,
		131,
		True
	},
	guild_boss_fleet_cnt_invaild = {
		521798,
		137,
		True
	},
	guild_boss_formation_not_exist_self_ship = {
		521935,
		190,
		True
	},
	guild_boss_formation_exist_event_ship = {
		522125,
		161,
		True
	},
	guild_fleet_is_legal = {
		522286,
		157,
		True
	},
	guild_battle_result_boss_is_death = {
		522443,
		134,
		True
	},
	guild_must_edit_fleet = {
		522577,
		112,
		True
	},
	guild_ship_in_battle = {
		522689,
		163,
		True
	},
	guild_ship_in_assult_fleet = {
		522852,
		134,
		True
	},
	guild_event_exist_assult_ship = {
		522986,
		157,
		True
	},
	guild_formation_erro_in_boss_battle = {
		523143,
		168,
		True
	},
	guild_get_report_failed = {
		523311,
		121,
		True
	},
	guild_report_get_all = {
		523432,
		95,
		True
	},
	guild_can_not_get_tip = {
		523527,
		158,
		True
	},
	guild_not_exist_notifycation = {
		523685,
		146,
		True
	},
	guild_exist_report_award_when_exit = {
		523831,
		172,
		True
	},
	guild_report_tooltip = {
		524003,
		243,
		True
	},
	word_guildgold = {
		524246,
		90,
		True
	},
	guild_member_rank_title_donate = {
		524336,
		107,
		True
	},
	guild_member_rank_title_finish_cnt = {
		524443,
		109,
		True
	},
	guild_member_rank_title_join_cnt = {
		524552,
		110,
		True
	},
	guild_donate_log = {
		524662,
		165,
		True
	},
	guild_supply_log = {
		524827,
		148,
		True
	},
	guild_weektask_log = {
		524975,
		148,
		True
	},
	guild_battle_log = {
		525123,
		137,
		True
	},
	guild_tech_change_log = {
		525260,
		136,
		True
	},
	guild_log_title = {
		525396,
		88,
		True
	},
	guild_use_donateitem_success = {
		525484,
		131,
		True
	},
	guild_use_battleitem_success = {
		525615,
		140,
		True
	},
	not_exist_guild_use_item = {
		525755,
		141,
		True
	},
	guild_member_tip = {
		525896,
		2773,
		True
	},
	guild_tech_tip = {
		528669,
		2740,
		True
	},
	guild_office_tip = {
		531409,
		2650,
		True
	},
	guild_event_help_tip = {
		534059,
		2687,
		True
	},
	guild_mission_info_tip = {
		536746,
		1109,
		True
	},
	guild_public_tech_tip = {
		537855,
		660,
		True
	},
	guild_public_office_tip = {
		538515,
		325,
		True
	},
	guild_tech_price_inc_tip = {
		538840,
		258,
		True
	},
	guild_boss_fleet_desc = {
		539098,
		523,
		True
	},
	guild_boss_formation_exist_invaild_ship = {
		539621,
		197,
		True
	},
	guild_exist_unreceived_supply_award = {
		539818,
		127,
		True
	},
	word_shipState_guild_event = {
		539945,
		159,
		True
	},
	word_shipState_guild_boss = {
		540104,
		193,
		True
	},
	commander_is_in_guild = {
		540297,
		195,
		True
	},
	guild_assult_ship_recommend = {
		540492,
		134,
		True
	},
	guild_cancel_assult_ship_recommend = {
		540626,
		132,
		True
	},
	guild_assult_ship_recommend_conflict = {
		540758,
		147,
		True
	},
	guild_recommend_limit = {
		540905,
		143,
		True
	},
	guild_cancel_assult_ship_recommend_conflict = {
		541048,
		169,
		True
	},
	guild_mission_complate = {
		541217,
		110,
		True
	},
	guild_operation_event_occurrence = {
		541327,
		172,
		True
	},
	guild_transfer_president_confirm = {
		541499,
		236,
		True
	},
	guild_damage_ranking = {
		541735,
		88,
		True
	},
	guild_total_damage = {
		541823,
		88,
		True
	},
	guild_donate_list_updated = {
		541911,
		142,
		True
	},
	guild_donate_list_update_failed = {
		542053,
		146,
		True
	},
	guild_tip_quit_operation = {
		542199,
		239,
		True
	},
	guild_tip_grand_fleet_is_frozen = {
		542438,
		144,
		True
	},
	guild_tip_operation_time_is_not_ample = {
		542582,
		355,
		True
	},
	guild_time_remaining_tip = {
		542937,
		104,
		True
	},
	multiple_ship_energy_low_desc = {
		543041,
		142,
		True
	},
	multiple_ship_energy_low_warn = {
		543183,
		142,
		True
	},
	multiple_ship_energy_low_warn_no_exp = {
		543325,
		282,
		True
	},
	us_error_download_painting = {
		543607,
		243,
		True
	},
	help_rollingBallGame = {
		543850,
		1116,
		True
	},
	rolling_ball_help = {
		544966,
		896,
		True
	},
	help_jiujiu_expedition_game = {
		545862,
		723,
		True
	},
	jiujiu_expedition_game_stg_desc = {
		546585,
		125,
		True
	},
	build_ship_accumulative = {
		546710,
		94,
		True
	},
	destory_ship_before_tip = {
		546804,
		96,
		True
	},
	destory_ship_input_erro = {
		546900,
		127,
		True
	},
	mail_input_erro = {
		547027,
		122,
		True
	},
	destroy_ur_rarity_tip = {
		547149,
		223,
		True
	},
	destory_ur_pt_overflowa = {
		547372,
		283,
		True
	},
	jiujiu_expedition_help = {
		547655,
		514,
		True
	},
	shop_label_unlimt_cnt = {
		548169,
		94,
		True
	},
	jiujiu_expedition_book_tip = {
		548263,
		142,
		True
	},
	jiujiu_expedition_reward_tip = {
		548405,
		140,
		True
	},
	jiujiu_expedition_amount_tip = {
		548545,
		172,
		True
	},
	jiujiu_expedition_stg_tip = {
		548717,
		133,
		True
	},
	trade_card_tips1 = {
		548850,
		85,
		True
	},
	trade_card_tips2 = {
		548935,
		273,
		True
	},
	trade_card_tips3 = {
		549208,
		278,
		True
	},
	trade_card_tips4 = {
		549486,
		93,
		True
	},
	ur_exchange_help_tip = {
		549579,
		965,
		True
	},
	fleet_antisub_range = {
		550544,
		95,
		True
	},
	fleet_antisub_range_tip = {
		550639,
		1085,
		True
	},
	practise_idol_tip = {
		551724,
		120,
		True
	},
	practise_idol_help = {
		551844,
		937,
		True
	},
	upgrade_idol_tip = {
		552781,
		153,
		True
	},
	upgrade_complete_tip = {
		552934,
		104,
		True
	},
	upgrade_introduce_tip = {
		553038,
		135,
		True
	},
	collect_idol_tip = {
		553173,
		158,
		True
	},
	hand_account_tip = {
		553331,
		125,
		True
	},
	hand_account_resetting_tip = {
		553456,
		133,
		True
	},
	help_candymagic = {
		553589,
		1060,
		True
	},
	award_overflow_tip = {
		554649,
		172,
		True
	},
	hunter_npc = {
		554821,
		1368,
		True
	},
	venusvolleyball_help = {
		556189,
		1402,
		True
	},
	venusvolleyball_rule_tip = {
		557591,
		109,
		True
	},
	venusvolleyball_return_tip = {
		557700,
		125,
		True
	},
	venusvolleyball_suspend_tip = {
		557825,
		109,
		True
	},
	doa_main = {
		557934,
		1461,
		True
	},
	doa_pt_help = {
		559395,
		841,
		True
	},
	doa_pt_complete = {
		560236,
		96,
		True
	},
	doa_pt_up = {
		560332,
		110,
		True
	},
	doa_liliang = {
		560442,
		78,
		True
	},
	doa_jiqiao = {
		560520,
		77,
		True
	},
	doa_tili = {
		560597,
		75,
		True
	},
	doa_meili = {
		560672,
		76,
		True
	},
	snowball_help = {
		560748,
		1745,
		True
	},
	help_xinnian2021_feast = {
		562493,
		533,
		True
	},
	help_xinnian2021__qiaozhong = {
		563026,
		1318,
		True
	},
	help_xinnian2021__meishiyemian = {
		564344,
		703,
		True
	},
	help_xinnian2021__meishi = {
		565047,
		1290,
		True
	},
	help_act_event = {
		566337,
		286,
		True
	},
	autofight = {
		566623,
		84,
		True
	},
	autofight_errors_tip = {
		566707,
		142,
		True
	},
	autofight_special_operation_tip = {
		566849,
		322,
		True
	},
	autofight_formation = {
		567171,
		92,
		True
	},
	autofight_cat = {
		567263,
		87,
		True
	},
	autofight_function = {
		567350,
		86,
		True
	},
	autofight_function1 = {
		567436,
		90,
		True
	},
	autofight_function2 = {
		567526,
		92,
		True
	},
	autofight_function3 = {
		567618,
		94,
		True
	},
	autofight_function4 = {
		567712,
		90,
		True
	},
	autofight_function5 = {
		567802,
		98,
		True
	},
	autofight_rewards = {
		567900,
		94,
		True
	},
	autofight_rewards_none = {
		567994,
		104,
		True
	},
	autofight_leave = {
		568098,
		83,
		True
	},
	autofight_onceagain = {
		568181,
		91,
		True
	},
	autofight_entrust = {
		568272,
		109,
		True
	},
	autofight_task = {
		568381,
		99,
		True
	},
	autofight_effect = {
		568480,
		146,
		True
	},
	autofight_file = {
		568626,
		97,
		True
	},
	autofight_discovery = {
		568723,
		112,
		True
	},
	autofight_tip_bigworld_dead = {
		568835,
		155,
		True
	},
	autofight_tip_bigworld_begin = {
		568990,
		137,
		True
	},
	autofight_tip_bigworld_stop = {
		569127,
		137,
		True
	},
	autofight_tip_bigworld_suspend = {
		569264,
		179,
		True
	},
	autofight_tip_bigworld_loop = {
		569443,
		151,
		True
	},
	autofight_farm = {
		569594,
		91,
		True
	},
	autofight_story = {
		569685,
		117,
		True
	},
	fushun_adventure_help = {
		569802,
		1320,
		True
	},
	autofight_change_tip = {
		571122,
		175,
		True
	},
	autofight_selectprops_tip = {
		571297,
		97,
		True
	},
	help_chunjie2021_feast = {
		571394,
		748,
		True
	},
	valentinesday__txt1_tip = {
		572142,
		174,
		True
	},
	valentinesday__txt2_tip = {
		572316,
		136,
		True
	},
	valentinesday__txt3_tip = {
		572452,
		141,
		True
	},
	valentinesday__txt4_tip = {
		572593,
		148,
		True
	},
	valentinesday__txt5_tip = {
		572741,
		140,
		True
	},
	valentinesday__txt6_tip = {
		572881,
		146,
		True
	},
	valentinesday__shop_tip = {
		573027,
		128,
		True
	},
	wwf_bamboo_tip1 = {
		573155,
		104,
		True
	},
	wwf_bamboo_tip2 = {
		573259,
		103,
		True
	},
	wwf_bamboo_tip3 = {
		573362,
		135,
		True
	},
	wwf_bamboo_help = {
		573497,
		1066,
		True
	},
	wwf_guide_tip = {
		574563,
		113,
		True
	},
	securitycake_help = {
		574676,
		2143,
		True
	},
	icecream_help = {
		576819,
		737,
		True
	},
	icecream_make_tip = {
		577556,
		98,
		True
	},
	query_role = {
		577654,
		86,
		True
	},
	query_role_none = {
		577740,
		87,
		True
	},
	query_role_button = {
		577827,
		94,
		True
	},
	query_role_fail = {
		577921,
		93,
		True
	},
	cumulative_victory_target_tip = {
		578014,
		109,
		True
	},
	cumulative_victory_now_tip = {
		578123,
		108,
		True
	},
	word_files_repair = {
		578231,
		95,
		True
	},
	repair_setting_label = {
		578326,
		98,
		True
	},
	voice_control = {
		578424,
		83,
		True
	},
	index_equip = {
		578507,
		84,
		True
	},
	index_without_limit = {
		578591,
		91,
		True
	},
	meta_learn_skill = {
		578682,
		92,
		True
	},
	world_joint_boss_not_found = {
		578774,
		148,
		True
	},
	world_joint_boss_is_death = {
		578922,
		143,
		True
	},
	world_joint_whitout_guild = {
		579065,
		123,
		True
	},
	world_joint_whitout_friend = {
		579188,
		126,
		True
	},
	world_joint_call_support_failed = {
		579314,
		126,
		True
	},
	world_joint_call_support_success = {
		579440,
		131,
		True
	},
	world_joint_call_friend_support_txt = {
		579571,
		111,
		True
	},
	world_joint_call_guild_support_txt = {
		579682,
		110,
		True
	},
	world_joint_call_world_support_txt = {
		579792,
		110,
		True
	},
	ad_4 = {
		579902,
		228,
		True
	},
	world_word_expired = {
		580130,
		94,
		True
	},
	world_word_guild_member = {
		580224,
		99,
		True
	},
	world_word_guild_player = {
		580323,
		93,
		True
	},
	world_joint_boss_award_expired = {
		580416,
		106,
		True
	},
	world_joint_not_refresh_frequently = {
		580522,
		122,
		True
	},
	world_joint_exit_battle_tip = {
		580644,
		151,
		True
	},
	world_boss_get_item = {
		580795,
		215,
		True
	},
	world_boss_ask_help = {
		581010,
		134,
		True
	},
	world_joint_count_no_enough = {
		581144,
		135,
		True
	},
	world_boss_none = {
		581279,
		133,
		True
	},
	world_boss_fleet = {
		581412,
		100,
		True
	},
	world_max_challenge_cnt = {
		581512,
		144,
		True
	},
	world_reset_success = {
		581656,
		124,
		True
	},
	world_map_dangerous_confirm = {
		581780,
		230,
		True
	},
	world_map_version = {
		582010,
		140,
		True
	},
	world_resource_fill = {
		582150,
		130,
		True
	},
	meta_sys_lock_tip = {
		582280,
		93,
		True
	},
	meta_story_lock = {
		582373,
		91,
		True
	},
	meta_acttime_limit = {
		582464,
		90,
		True
	},
	meta_pt_left = {
		582554,
		88,
		True
	},
	meta_syn_rate = {
		582642,
		86,
		True
	},
	meta_repair_rate = {
		582728,
		99,
		True
	},
	meta_story_tip_1 = {
		582827,
		92,
		True
	},
	meta_story_tip_2 = {
		582919,
		92,
		True
	},
	meta_pt_get_way = {
		583011,
		91,
		True
	},
	meta_pt_point = {
		583102,
		84,
		True
	},
	meta_award_get = {
		583186,
		85,
		True
	},
	meta_award_got = {
		583271,
		87,
		True
	},
	meta_repair = {
		583358,
		89,
		True
	},
	meta_repair_success = {
		583447,
		117,
		True
	},
	meta_repair_effect_unlock = {
		583564,
		125,
		True
	},
	meta_repair_effect_special = {
		583689,
		122,
		True
	},
	meta_energy_ship_level_need = {
		583811,
		115,
		True
	},
	meta_energy_ship_repairrate_need = {
		583926,
		125,
		True
	},
	meta_energy_active_box_tip = {
		584051,
		192,
		True
	},
	meta_break = {
		584243,
		127,
		True
	},
	meta_energy_preview_title = {
		584370,
		123,
		True
	},
	meta_energy_preview_tip = {
		584493,
		138,
		True
	},
	meta_exp_per_day = {
		584631,
		90,
		True
	},
	meta_skill_unlock = {
		584721,
		108,
		True
	},
	meta_unlock_skill_tip = {
		584829,
		160,
		True
	},
	meta_unlock_skill_select = {
		584989,
		100,
		True
	},
	meta_switch_skill_disable = {
		585089,
		138,
		True
	},
	meta_switch_skill_box_title = {
		585227,
		128,
		True
	},
	meta_cur_pt = {
		585355,
		87,
		True
	},
	meta_toast_fullexp = {
		585442,
		115,
		True
	},
	meta_toast_tactics = {
		585557,
		95,
		True
	},
	meta_skillbtn_tactics = {
		585652,
		93,
		True
	},
	meta_destroy_tip = {
		585745,
		110,
		True
	},
	meta_voice_name_feeling1 = {
		585855,
		96,
		True
	},
	meta_voice_name_feeling2 = {
		585951,
		96,
		True
	},
	meta_voice_name_feeling3 = {
		586047,
		94,
		True
	},
	meta_voice_name_feeling4 = {
		586141,
		94,
		True
	},
	meta_voice_name_feeling5 = {
		586235,
		92,
		True
	},
	meta_voice_name_propose = {
		586327,
		91,
		True
	},
	world_boss_ad = {
		586418,
		89,
		True
	},
	world_boss_drop_title = {
		586507,
		97,
		True
	},
	world_boss_pt_recove_desc = {
		586604,
		151,
		True
	},
	world_boss_progress_item_desc = {
		586755,
		462,
		True
	},
	world_joint_max_challenge_people_cnt = {
		587217,
		130,
		True
	},
	equip_ammo_type_1 = {
		587347,
		83,
		True
	},
	equip_ammo_type_2 = {
		587430,
		83,
		True
	},
	equip_ammo_type_3 = {
		587513,
		88,
		True
	},
	equip_ammo_type_4 = {
		587601,
		90,
		True
	},
	equip_ammo_type_5 = {
		587691,
		88,
		True
	},
	equip_ammo_type_6 = {
		587779,
		88,
		True
	},
	equip_ammo_type_7 = {
		587867,
		84,
		True
	},
	equip_ammo_type_8 = {
		587951,
		92,
		True
	},
	equip_ammo_type_9 = {
		588043,
		88,
		True
	},
	equip_ammo_type_10 = {
		588131,
		87,
		True
	},
	equip_ammo_type_11 = {
		588218,
		89,
		True
	},
	common_daily_limit = {
		588307,
		94,
		True
	},
	meta_help = {
		588401,
		2141,
		True
	},
	world_boss_daily_limit = {
		590542,
		118,
		True
	},
	common_go_to_analyze = {
		590660,
		92,
		True
	},
	world_boss_not_reach_target = {
		590752,
		122,
		True
	},
	special_transform_limit_reach = {
		590874,
		145,
		True
	},
	meta_pt_notenough = {
		591019,
		175,
		True
	},
	meta_boss_unlock = {
		591194,
		210,
		True
	},
	word_take_effect = {
		591404,
		91,
		True
	},
	world_boss_challenge_cnt = {
		591495,
		100,
		True
	},
	word_shipNation_meta = {
		591595,
		87,
		True
	},
	world_word_friend = {
		591682,
		89,
		True
	},
	world_word_world = {
		591771,
		86,
		True
	},
	world_word_guild = {
		591857,
		85,
		True
	},
	world_collection_1 = {
		591942,
		91,
		True
	},
	world_collection_2 = {
		592033,
		91,
		True
	},
	world_collection_3 = {
		592124,
		91,
		True
	},
	zero_hour_command_error = {
		592215,
		150,
		True
	},
	commander_is_in_bigworld = {
		592365,
		142,
		True
	},
	world_collection_back = {
		592507,
		99,
		True
	},
	archives_whether_to_retreat = {
		592606,
		199,
		True
	},
	world_fleet_stop = {
		592805,
		111,
		True
	},
	world_setting_title = {
		592916,
		108,
		True
	},
	world_setting_quickmode = {
		593024,
		106,
		True
	},
	world_setting_quickmodetip = {
		593130,
		134,
		True
	},
	world_setting_submititem = {
		593264,
		121,
		True
	},
	world_setting_submititemtip = {
		593385,
		332,
		True
	},
	world_setting_mapauto = {
		593717,
		122,
		True
	},
	world_setting_mapautotip = {
		593839,
		171,
		True
	},
	world_boss_maintenance = {
		594010,
		167,
		True
	},
	world_boss_inbattle = {
		594177,
		147,
		True
	},
	world_automode_title_1 = {
		594324,
		103,
		True
	},
	world_automode_title_2 = {
		594427,
		86,
		True
	},
	world_automode_treasure_1 = {
		594513,
		137,
		True
	},
	world_automode_treasure_2 = {
		594650,
		132,
		True
	},
	world_automode_treasure_3 = {
		594782,
		136,
		True
	},
	world_automode_cancel = {
		594918,
		91,
		True
	},
	world_automode_confirm = {
		595009,
		93,
		True
	},
	world_automode_start_tip1 = {
		595102,
		122,
		True
	},
	world_automode_start_tip2 = {
		595224,
		105,
		True
	},
	world_automode_start_tip3 = {
		595329,
		124,
		True
	},
	world_automode_start_tip4 = {
		595453,
		115,
		True
	},
	world_automode_start_tip5 = {
		595568,
		164,
		True
	},
	world_automode_setting_1 = {
		595732,
		119,
		True
	},
	world_automode_setting_1_1 = {
		595851,
		101,
		True
	},
	world_automode_setting_1_2 = {
		595952,
		91,
		True
	},
	world_automode_setting_1_3 = {
		596043,
		91,
		True
	},
	world_automode_setting_1_4 = {
		596134,
		99,
		True
	},
	world_automode_setting_2 = {
		596233,
		137,
		True
	},
	world_automode_setting_2_1 = {
		596370,
		106,
		True
	},
	world_automode_setting_2_2 = {
		596476,
		109,
		True
	},
	world_automode_setting_all_1 = {
		596585,
		135,
		True
	},
	world_automode_setting_all_1_1 = {
		596720,
		115,
		True
	},
	world_automode_setting_all_1_2 = {
		596835,
		119,
		True
	},
	world_automode_setting_all_2 = {
		596954,
		139,
		True
	},
	world_automode_setting_all_2_1 = {
		597093,
		99,
		True
	},
	world_automode_setting_all_2_2 = {
		597192,
		115,
		True
	},
	world_automode_setting_all_2_3 = {
		597307,
		115,
		True
	},
	world_automode_setting_all_3 = {
		597422,
		121,
		True
	},
	world_automode_setting_all_3_1 = {
		597543,
		96,
		True
	},
	world_automode_setting_all_3_2 = {
		597639,
		97,
		True
	},
	world_automode_setting_all_4 = {
		597736,
		135,
		True
	},
	world_automode_setting_all_4_1 = {
		597871,
		97,
		True
	},
	world_automode_setting_all_4_2 = {
		597968,
		96,
		True
	},
	world_automode_setting_new_1 = {
		598064,
		122,
		True
	},
	world_automode_setting_new_1_1 = {
		598186,
		105,
		True
	},
	world_automode_setting_new_1_2 = {
		598291,
		95,
		True
	},
	world_automode_setting_new_1_3 = {
		598386,
		95,
		True
	},
	world_automode_setting_new_1_4 = {
		598481,
		95,
		True
	},
	world_automode_setting_new_1_5 = {
		598576,
		97,
		True
	},
	world_collection_task_tip_1 = {
		598673,
		147,
		True
	},
	area_putong = {
		598820,
		85,
		True
	},
	area_anquan = {
		598905,
		82,
		True
	},
	area_yaosai = {
		598987,
		85,
		True
	},
	area_yaosai_2 = {
		599072,
		96,
		True
	},
	area_shenyuan = {
		599168,
		84,
		True
	},
	area_yinmi = {
		599252,
		80,
		True
	},
	area_renwu = {
		599332,
		81,
		True
	},
	area_zhuxian = {
		599413,
		84,
		True
	},
	area_dangan = {
		599497,
		85,
		True
	},
	charge_trade_no_error = {
		599582,
		122,
		True
	},
	world_reset_1 = {
		599704,
		136,
		True
	},
	world_reset_2 = {
		599840,
		138,
		True
	},
	world_reset_3 = {
		599978,
		111,
		True
	},
	guild_is_frozen_when_start_tech = {
		600089,
		126,
		True
	},
	world_boss_unactivated = {
		600215,
		155,
		True
	},
	world_reset_tip = {
		600370,
		2719,
		True
	},
	spring_invited_2021 = {
		603089,
		231,
		True
	},
	charge_error_count_limit = {
		603320,
		128,
		True
	},
	charge_error_disable = {
		603448,
		144,
		True
	},
	levelScene_select_sp = {
		603592,
		138,
		True
	},
	word_adjustFleet = {
		603730,
		86,
		True
	},
	levelScene_select_noitem = {
		603816,
		112,
		True
	},
	story_setting_label = {
		603928,
		105,
		True
	},
	login_arrears_tips = {
		604033,
		208,
		True
	},
	Supplement_pay1 = {
		604241,
		211,
		True
	},
	Supplement_pay2 = {
		604452,
		231,
		True
	},
	Supplement_pay3 = {
		604683,
		209,
		True
	},
	Supplement_pay4 = {
		604892,
		86,
		True
	},
	world_ship_repair = {
		604978,
		102,
		True
	},
	Supplement_pay5 = {
		605080,
		185,
		True
	},
	area_unkown = {
		605265,
		89,
		True
	},
	Supplement_pay6 = {
		605354,
		89,
		True
	},
	Supplement_pay7 = {
		605443,
		88,
		True
	},
	Supplement_pay8 = {
		605531,
		86,
		True
	},
	world_battle_damage = {
		605617,
		217,
		True
	},
	setting_story_speed_1 = {
		605834,
		89,
		True
	},
	setting_story_speed_2 = {
		605923,
		91,
		True
	},
	setting_story_speed_3 = {
		606014,
		89,
		True
	},
	setting_story_speed_4 = {
		606103,
		94,
		True
	},
	story_autoplay_setting_label = {
		606197,
		106,
		True
	},
	story_autoplay_setting_1 = {
		606303,
		96,
		True
	},
	story_autoplay_setting_2 = {
		606399,
		95,
		True
	},
	meta_shop_exchange_limit = {
		606494,
		98,
		True
	},
	meta_shop_unexchange_label = {
		606592,
		90,
		True
	},
	daily_level_quick_battle_label2 = {
		606682,
		101,
		True
	},
	daily_level_quick_battle_label1 = {
		606783,
		109,
		True
	},
	dailyLevel_quickfinish = {
		606892,
		329,
		True
	},
	daily_level_quick_battle_label3 = {
		607221,
		108,
		True
	},
	backyard_longpress_ship_tip = {
		607329,
		160,
		True
	},
	common_npc_formation_tip = {
		607489,
		126,
		True
	},
	gametip_xiaotiancheng = {
		607615,
		1319,
		True
	},
	guild_task_autoaccept_1 = {
		608934,
		128,
		True
	},
	guild_task_autoaccept_2 = {
		609062,
		135,
		True
	},
	task_lock = {
		609197,
		93,
		True
	},
	week_task_pt_name = {
		609290,
		96,
		True
	},
	week_task_award_preview_label = {
		609386,
		100,
		True
	},
	week_task_title_label = {
		609486,
		108,
		True
	},
	cattery_op_clean_success = {
		609594,
		122,
		True
	},
	cattery_op_feed_success = {
		609716,
		114,
		True
	},
	cattery_op_play_success = {
		609830,
		122,
		True
	},
	cattery_style_change_success = {
		609952,
		130,
		True
	},
	cattery_add_commander_success = {
		610082,
		110,
		True
	},
	cattery_remove_commander_success = {
		610192,
		115,
		True
	},
	commander_box_quickly_tool_tip_1 = {
		610307,
		152,
		True
	},
	commander_box_quickly_tool_tip_2 = {
		610459,
		147,
		True
	},
	commander_box_quickly_tool_tip_3 = {
		610606,
		123,
		True
	},
	commander_box_was_finished = {
		610729,
		119,
		True
	},
	comander_tool_cnt_is_reclac = {
		610848,
		151,
		True
	},
	comander_tool_max_cnt = {
		610999,
		93,
		True
	},
	commander_op_play_level = {
		611092,
		101,
		True
	},
	commander_op_feed_level = {
		611193,
		101,
		True
	},
	cat_home_help = {
		611294,
		1398,
		True
	},
	cat_accelfrate_notenough = {
		612692,
		136,
		True
	},
	cat_home_unlock = {
		612828,
		131,
		True
	},
	cat_sleep_notplay = {
		612959,
		140,
		True
	},
	cathome_style_unlock = {
		613099,
		142,
		True
	},
	commander_is_in_cattery = {
		613241,
		122,
		True
	},
	cat_home_interaction = {
		613363,
		133,
		True
	},
	cat_accelerate_left = {
		613496,
		96,
		True
	},
	common_clean = {
		613592,
		81,
		True
	},
	common_feed = {
		613673,
		79,
		True
	},
	common_play = {
		613752,
		79,
		True
	},
	game_stopwords = {
		613831,
		107,
		True
	},
	game_openwords = {
		613938,
		110,
		True
	},
	amusementpark_shop_enter = {
		614048,
		143,
		True
	},
	amusementpark_shop_exchange = {
		614191,
		189,
		True
	},
	amusementpark_shop_success = {
		614380,
		107,
		True
	},
	amusementpark_shop_special = {
		614487,
		149,
		True
	},
	amusementpark_shop_end = {
		614636,
		116,
		True
	},
	amusementpark_shop_0 = {
		614752,
		176,
		True
	},
	amusementpark_shop_carousel1 = {
		614928,
		152,
		True
	},
	amusementpark_shop_carousel2 = {
		615080,
		151,
		True
	},
	amusementpark_shop_carousel3 = {
		615231,
		153,
		True
	},
	amusementpark_shop_exchange2 = {
		615384,
		196,
		True
	},
	amusementpark_help = {
		615580,
		1927,
		True
	},
	amusementpark_shop_help = {
		617507,
		465,
		True
	},
	handshake_game_help = {
		617972,
		915,
		True
	},
	MeixiV4_help = {
		618887,
		908,
		True
	},
	activity_permanent_total = {
		619795,
		107,
		True
	},
	word_investigate = {
		619902,
		86,
		True
	},
	ambush_display_none = {
		619988,
		88,
		True
	},
	activity_permanent_help = {
		620076,
		502,
		True
	},
	activity_permanent_tips1 = {
		620578,
		171,
		True
	},
	activity_permanent_tips2 = {
		620749,
		175,
		True
	},
	activity_permanent_tips3 = {
		620924,
		155,
		True
	},
	activity_permanent_tips4 = {
		621079,
		199,
		True
	},
	activity_permanent_finished = {
		621278,
		100,
		True
	},
	idolmaster_main = {
		621378,
		1190,
		True
	},
	idolmaster_game_tip1 = {
		622568,
		118,
		True
	},
	idolmaster_game_tip2 = {
		622686,
		116,
		True
	},
	idolmaster_game_tip3 = {
		622802,
		97,
		True
	},
	idolmaster_game_tip4 = {
		622899,
		94,
		True
	},
	idolmaster_game_tip5 = {
		622993,
		89,
		True
	},
	idolmaster_collection = {
		623082,
		631,
		True
	},
	idolmaster_voice_name_feeling1 = {
		623713,
		107,
		True
	},
	idolmaster_voice_name_feeling2 = {
		623820,
		102,
		True
	},
	idolmaster_voice_name_feeling3 = {
		623922,
		101,
		True
	},
	idolmaster_voice_name_feeling4 = {
		624023,
		104,
		True
	},
	idolmaster_voice_name_feeling5 = {
		624127,
		102,
		True
	},
	idolmaster_voice_name_propose = {
		624229,
		98,
		True
	},
	cartoon_all = {
		624327,
		78,
		True
	},
	cartoon_notall = {
		624405,
		84,
		True
	},
	cartoon_haveno = {
		624489,
		111,
		True
	},
	res_cartoon_new_tip = {
		624600,
		108,
		True
	},
	memory_actiivty_ex = {
		624708,
		87,
		True
	},
	memory_activity_sp = {
		624795,
		89,
		True
	},
	memory_activity_daily = {
		624884,
		89,
		True
	},
	memory_activity_others = {
		624973,
		90,
		True
	},
	battle_end_title = {
		625063,
		94,
		True
	},
	battle_end_subtitle1 = {
		625157,
		91,
		True
	},
	battle_end_subtitle2 = {
		625248,
		101,
		True
	},
	meta_skill_dailyexp = {
		625349,
		92,
		True
	},
	meta_skill_learn = {
		625441,
		127,
		True
	},
	meta_skill_maxtip = {
		625568,
		203,
		True
	},
	meta_tactics_detail = {
		625771,
		90,
		True
	},
	meta_tactics_unlock = {
		625861,
		91,
		True
	},
	meta_tactics_switch = {
		625952,
		91,
		True
	},
	meta_skill_maxtip2 = {
		626043,
		91,
		True
	},
	activity_permanent_progress = {
		626134,
		100,
		True
	},
	cattery_settlement_dialogue_1 = {
		626234,
		116,
		True
	},
	cattery_settlement_dialogue_2 = {
		626350,
		131,
		True
	},
	cattery_settlement_dialogue_3 = {
		626481,
		115,
		True
	},
	cattery_settlement_dialogue_4 = {
		626596,
		102,
		True
	},
	blueprint_catchup_by_gold_confirm = {
		626698,
		153,
		True
	},
	blueprint_catchup_by_gold_help = {
		626851,
		318,
		True
	},
	tec_tip_no_consumption = {
		627169,
		90,
		True
	},
	tec_tip_material_stock = {
		627259,
		91,
		True
	},
	tec_tip_to_consumption = {
		627350,
		91,
		True
	},
	onebutton_max_tip = {
		627441,
		96,
		True
	},
	target_get_tip = {
		627537,
		89,
		True
	},
	fleet_select_title = {
		627626,
		94,
		True
	},
	backyard_rename_title = {
		627720,
		96,
		True
	},
	backyard_rename_tip = {
		627816,
		105,
		True
	},
	equip_add = {
		627921,
		99,
		True
	},
	equipskin_add = {
		628020,
		108,
		True
	},
	equipskin_none = {
		628128,
		109,
		True
	},
	equipskin_typewrong = {
		628237,
		117,
		True
	},
	equipskin_typewrong_en = {
		628354,
		108,
		True
	},
	user_is_banned = {
		628462,
		134,
		True
	},
	user_is_forever_banned = {
		628596,
		116,
		True
	},
	old_class_is_close = {
		628712,
		144,
		True
	},
	activity_event_building = {
		628856,
		1210,
		True
	},
	salvage_tips = {
		630066,
		1124,
		True
	},
	tips_shakebeads = {
		631190,
		1036,
		True
	},
	gem_shop_xinzhi_tip = {
		632226,
		113,
		True
	},
	cowboy_tips = {
		632339,
		708,
		True
	},
	backyard_backyardScene_Disable_Rotation = {
		633047,
		137,
		True
	},
	chazi_tips = {
		633184,
		886,
		True
	},
	catchteasure_help = {
		634070,
		453,
		True
	},
	unlock_tips = {
		634523,
		93,
		True
	},
	class_label_tran = {
		634616,
		87,
		True
	},
	class_label_gen = {
		634703,
		88,
		True
	},
	class_attr_store = {
		634791,
		89,
		True
	},
	class_attr_proficiency = {
		634880,
		103,
		True
	},
	class_attr_getproficiency = {
		634983,
		105,
		True
	},
	class_attr_costproficiency = {
		635088,
		104,
		True
	},
	class_label_upgrading = {
		635192,
		94,
		True
	},
	class_label_upgradetime = {
		635286,
		99,
		True
	},
	class_label_oilfield = {
		635385,
		98,
		True
	},
	class_label_goldfield = {
		635483,
		100,
		True
	},
	class_res_maxlevel_tip = {
		635583,
		95,
		True
	},
	ship_exp_item_title = {
		635678,
		93,
		True
	},
	ship_exp_item_label_clear = {
		635771,
		94,
		True
	},
	ship_exp_item_label_recom = {
		635865,
		93,
		True
	},
	ship_exp_item_label_confirm = {
		635958,
		98,
		True
	},
	player_expResource_mail_fullBag = {
		636056,
		200,
		True
	},
	player_expResource_mail_overflow = {
		636256,
		195,
		True
	},
	tec_nation_award_finish = {
		636451,
		98,
		True
	},
	coures_exp_overflow_tip = {
		636549,
		202,
		True
	},
	coures_exp_npc_tip = {
		636751,
		221,
		True
	},
	coures_level_tip = {
		636972,
		162,
		True
	},
	coures_tip_material_stock = {
		637134,
		94,
		True
	},
	coures_tip_exceeded_lv = {
		637228,
		123,
		True
	},
	eatgame_tips = {
		637351,
		844,
		True
	},
	breakout_tip_ultimatebonus_gunner = {
		638195,
		145,
		True
	},
	breakout_tip_ultimatebonus_torpedo = {
		638340,
		130,
		True
	},
	breakout_tip_ultimatebonus_aux = {
		638470,
		133,
		True
	},
	map_event_lighthouse_tip_1 = {
		638603,
		161,
		True
	},
	battlepass_main_tip_2110 = {
		638764,
		202,
		True
	},
	battlepass_main_time = {
		638966,
		94,
		True
	},
	battlepass_main_help_2110 = {
		639060,
		2880,
		True
	},
	cruise_task_help_2110 = {
		641940,
		1094,
		True
	},
	cruise_task_phase = {
		643034,
		106,
		True
	},
	cruise_task_tips = {
		643140,
		89,
		True
	},
	battlepass_task_quickfinish1 = {
		643229,
		231,
		True
	},
	battlepass_task_quickfinish2 = {
		643460,
		224,
		True
	},
	battlepass_task_quickfinish3 = {
		643684,
		102,
		True
	},
	cruise_task_unlock = {
		643786,
		107,
		True
	},
	cruise_task_week = {
		643893,
		87,
		True
	},
	battlepass_pay_timelimit = {
		643980,
		101,
		True
	},
	battlepass_pay_acquire = {
		644081,
		101,
		True
	},
	battlepass_pay_attention = {
		644182,
		159,
		True
	},
	battlepass_acquire_attention = {
		644341,
		189,
		True
	},
	battlepass_pay_tip = {
		644530,
		121,
		True
	},
	battlepass_main_tip1 = {
		644651,
		226,
		True
	},
	battlepass_main_tip2 = {
		644877,
		209,
		True
	},
	battlepass_main_tip3 = {
		645086,
		215,
		True
	},
	battlepass_complete = {
		645301,
		121,
		True
	},
	shop_free_tag = {
		645422,
		81,
		True
	},
	quick_equip_tip1 = {
		645503,
		86,
		True
	},
	quick_equip_tip2 = {
		645589,
		86,
		True
	},
	quick_equip_tip3 = {
		645675,
		85,
		True
	},
	quick_equip_tip4 = {
		645760,
		97,
		True
	},
	quick_equip_tip5 = {
		645857,
		127,
		True
	},
	quick_equip_tip6 = {
		645984,
		184,
		True
	},
	retire_importantequipment_tips = {
		646168,
		179,
		True
	},
	settle_rewards_title = {
		646347,
		109,
		True
	},
	settle_rewards_subtitle = {
		646456,
		101,
		True
	},
	total_rewards_subtitle = {
		646557,
		99,
		True
	},
	settle_rewards_text = {
		646656,
		99,
		True
	},
	use_oil_limit_help = {
		646755,
		243,
		True
	},
	formationScene_use_oil_limit_tip = {
		646998,
		107,
		True
	},
	index_awakening2 = {
		647105,
		93,
		True
	},
	index_upgrade = {
		647198,
		91,
		True
	},
	formationScene_use_oil_limit_enemy = {
		647289,
		104,
		True
	},
	formationScene_use_oil_limit_flagship = {
		647393,
		109,
		True
	},
	formationScene_use_oil_limit_submarine = {
		647502,
		104,
		True
	},
	formationScene_use_oil_limit_surface = {
		647606,
		107,
		True
	},
	formationScene_use_oil_limit_tip_worldboss = {
		647713,
		117,
		True
	},
	attr_durability = {
		647830,
		81,
		True
	},
	attr_armor = {
		647911,
		79,
		True
	},
	attr_reload = {
		647990,
		78,
		True
	},
	attr_cannon = {
		648068,
		77,
		True
	},
	attr_torpedo = {
		648145,
		79,
		True
	},
	attr_motion = {
		648224,
		78,
		True
	},
	attr_antiaircraft = {
		648302,
		83,
		True
	},
	attr_air = {
		648385,
		75,
		True
	},
	attr_hit = {
		648460,
		75,
		True
	},
	attr_antisub = {
		648535,
		79,
		True
	},
	attr_oxy_max = {
		648614,
		79,
		True
	},
	attr_ammo = {
		648693,
		76,
		True
	},
	attr_hunting_range = {
		648769,
		85,
		True
	},
	attr_luck = {
		648854,
		76,
		True
	},
	attr_consume = {
		648930,
		80,
		True
	},
	attr_speed = {
		649010,
		77,
		True
	},
	monthly_card_tip = {
		649087,
		80,
		True
	},
	shopping_error_time_limit = {
		649167,
		138,
		True
	},
	world_total_power = {
		649305,
		86,
		True
	},
	world_mileage = {
		649391,
		91,
		True
	},
	world_pressing = {
		649482,
		91,
		True
	},
	Settings_title_FPS = {
		649573,
		101,
		True
	},
	Settings_title_Notification = {
		649674,
		109,
		True
	},
	Settings_title_Other = {
		649783,
		97,
		True
	},
	Settings_title_LoginJP = {
		649880,
		99,
		True
	},
	Settings_title_Redeem = {
		649979,
		94,
		True
	},
	Settings_title_AdjustScr = {
		650073,
		101,
		True
	},
	Settings_title_Secpw = {
		650174,
		98,
		True
	},
	Settings_title_Secpwlimop = {
		650272,
		110,
		True
	},
	Settings_title_agreement = {
		650382,
		100,
		True
	},
	Settings_title_sound = {
		650482,
		98,
		True
	},
	Settings_title_resUpdate = {
		650580,
		103,
		True
	},
	equipment_info_change_tip = {
		650683,
		138,
		True
	},
	equipment_info_change_name_a = {
		650821,
		126,
		True
	},
	equipment_info_change_name_b = {
		650947,
		126,
		True
	},
	equipment_info_change_text_before = {
		651073,
		103,
		True
	},
	equipment_info_change_text_after = {
		651176,
		101,
		True
	},
	equipment_info_change_strengthen = {
		651277,
		277,
		True
	},
	world_boss_progress_tip_title = {
		651554,
		122,
		True
	},
	world_boss_progress_tip_desc = {
		651676,
		354,
		True
	},
	ssss_main_help = {
		652030,
		1932,
		True
	},
	mini_game_time = {
		653962,
		88,
		True
	},
	mini_game_score = {
		654050,
		85,
		True
	},
	mini_game_leave = {
		654135,
		93,
		True
	},
	mini_game_pause = {
		654228,
		96,
		True
	},
	mini_game_cur_score = {
		654324,
		97,
		True
	},
	mini_game_high_score = {
		654421,
		95,
		True
	},
	monopoly_world_tip1 = {
		654516,
		96,
		True
	},
	monopoly_world_tip2 = {
		654612,
		237,
		True
	},
	monopoly_world_tip3 = {
		654849,
		212,
		True
	},
	help_monopoly_world = {
		655061,
		1414,
		True
	},
	ssssmedal_tip = {
		656475,
		142,
		True
	},
	ssssmedal_name = {
		656617,
		107,
		True
	},
	ssssmedal_belonging = {
		656724,
		112,
		True
	},
	ssssmedal_name1 = {
		656836,
		108,
		True
	},
	ssssmedal_name2 = {
		656944,
		105,
		True
	},
	ssssmedal_name3 = {
		657049,
		107,
		True
	},
	ssssmedal_name4 = {
		657156,
		109,
		True
	},
	ssssmedal_name5 = {
		657265,
		109,
		True
	},
	ssssmedal_name6 = {
		657374,
		85,
		True
	},
	ssssmedal_belonging1 = {
		657459,
		92,
		True
	},
	ssssmedal_belonging2 = {
		657551,
		99,
		True
	},
	ssssmedal_desc1 = {
		657650,
		168,
		True
	},
	ssssmedal_desc2 = {
		657818,
		158,
		True
	},
	ssssmedal_desc3 = {
		657976,
		168,
		True
	},
	ssssmedal_desc4 = {
		658144,
		155,
		True
	},
	ssssmedal_desc5 = {
		658299,
		180,
		True
	},
	ssssmedal_desc6 = {
		658479,
		131,
		True
	},
	show_fate_demand_count = {
		658610,
		154,
		True
	},
	show_design_demand_count = {
		658764,
		151,
		True
	},
	blueprint_select_overflow = {
		658915,
		124,
		True
	},
	blueprint_select_overflow_tip = {
		659039,
		188,
		True
	},
	blueprint_exchange_empty_tip = {
		659227,
		131,
		True
	},
	blueprint_exchange_select_display = {
		659358,
		128,
		True
	},
	build_rate_title = {
		659486,
		91,
		True
	},
	build_pools_intro = {
		659577,
		116,
		True
	},
	build_detail_intro = {
		659693,
		106,
		True
	},
	ssss_game_tip = {
		659799,
		1498,
		True
	},
	ssss_medal_tip = {
		661297,
		401,
		True
	},
	battlepass_main_tip_2112 = {
		661698,
		233,
		True
	},
	battlepass_main_help_2112 = {
		661931,
		2887,
		True
	},
	cruise_task_help_2112 = {
		664818,
		1085,
		True
	},
	littleSanDiego_npc = {
		665903,
		1223,
		True
	},
	tag_ship_unlocked = {
		667126,
		95,
		True
	},
	tag_ship_locked = {
		667221,
		91,
		True
	},
	acceleration_tips_1 = {
		667312,
		203,
		True
	},
	acceleration_tips_2 = {
		667515,
		228,
		True
	},
	noacceleration_tips = {
		667743,
		119,
		True
	},
	word_shipskin = {
		667862,
		82,
		True
	},
	settings_sound_title_bgm = {
		667944,
		99,
		True
	},
	settings_sound_title_effct = {
		668043,
		101,
		True
	},
	settings_sound_title_cv = {
		668144,
		100,
		True
	},
	setting_resdownload_title_gallery = {
		668244,
		111,
		True
	},
	setting_resdownload_title_live2d = {
		668355,
		109,
		True
	},
	setting_resdownload_title_music = {
		668464,
		105,
		True
	},
	setting_resdownload_title_sound = {
		668569,
		108,
		True
	},
	setting_resdownload_title_manga = {
		668677,
		108,
		True
	},
	setting_resdownload_title_dorm = {
		668785,
		115,
		True
	},
	setting_resdownload_title_main_group = {
		668900,
		117,
		True
	},
	settings_battle_title = {
		669017,
		103,
		True
	},
	settings_battle_tip = {
		669120,
		144,
		True
	},
	settings_battle_Btn_edit = {
		669264,
		92,
		True
	},
	settings_battle_Btn_reset = {
		669356,
		96,
		True
	},
	settings_battle_Btn_save = {
		669452,
		92,
		True
	},
	settings_battle_Btn_cancel = {
		669544,
		96,
		True
	},
	settings_pwd_label_close = {
		669640,
		96,
		True
	},
	settings_pwd_label_open = {
		669736,
		94,
		True
	},
	word_frame = {
		669830,
		78,
		True
	},
	Settings_title_Redeem_input_label = {
		669908,
		109,
		True
	},
	Settings_title_Redeem_input_submit = {
		670017,
		104,
		True
	},
	Settings_title_Redeem_input_placeholder = {
		670121,
		140,
		True
	},
	CurlingGame_tips1 = {
		670261,
		1153,
		True
	},
	maid_task_tips1 = {
		671414,
		1030,
		True
	},
	shop_diamond_title = {
		672444,
		86,
		True
	},
	shop_gift_title = {
		672530,
		84,
		True
	},
	shop_item_title = {
		672614,
		84,
		True
	},
	shop_charge_level_limit = {
		672698,
		102,
		True
	},
	backhill_cantupbuilding = {
		672800,
		135,
		True
	},
	pray_cant_tips = {
		672935,
		133,
		True
	},
	help_xinnian2022_feast = {
		673068,
		2200,
		True
	},
	Pray_activity_tips1 = {
		675268,
		1560,
		True
	},
	backhill_notenoughbuilding = {
		676828,
		184,
		True
	},
	help_xinnian2022_z28 = {
		677012,
		766,
		True
	},
	help_xinnian2022_firework = {
		677778,
		1156,
		True
	},
	settings_title_account_del = {
		678934,
		97,
		True
	},
	settings_text_account_del = {
		679031,
		105,
		True
	},
	settings_text_account_del_desc = {
		679136,
		290,
		True
	},
	settings_text_account_del_confirm = {
		679426,
		150,
		True
	},
	settings_text_account_del_btn = {
		679576,
		99,
		True
	},
	box_account_del_input = {
		679675,
		142,
		True
	},
	box_account_del_target = {
		679817,
		92,
		True
	},
	box_account_del_click = {
		679909,
		100,
		True
	},
	box_account_del_success_content = {
		680009,
		131,
		True
	},
	box_account_reborn_content = {
		680140,
		211,
		True
	},
	tip_account_del_dismatch = {
		680351,
		120,
		True
	},
	tip_account_del_reborn = {
		680471,
		135,
		True
	},
	player_manifesto_placeholder = {
		680606,
		110,
		True
	},
	box_ship_del_click = {
		680716,
		95,
		True
	},
	box_equipment_del_click = {
		680811,
		100,
		True
	},
	change_player_name_title = {
		680911,
		103,
		True
	},
	change_player_name_subtitle = {
		681014,
		111,
		True
	},
	change_player_name_input_tip = {
		681125,
		112,
		True
	},
	change_player_name_illegal = {
		681237,
		241,
		True
	},
	nodisplay_player_home_name = {
		681478,
		94,
		True
	},
	nodisplay_player_home_share = {
		681572,
		97,
		True
	},
	tactics_class_start = {
		681669,
		88,
		True
	},
	tactics_class_cancel = {
		681757,
		90,
		True
	},
	tactics_class_get_exp = {
		681847,
		94,
		True
	},
	tactics_class_spend_time = {
		681941,
		99,
		True
	},
	build_ticket_description = {
		682040,
		118,
		True
	},
	build_ticket_expire_warning = {
		682158,
		103,
		True
	},
	tip_build_ticket_expired = {
		682261,
		135,
		True
	},
	tip_build_ticket_exchange_expired = {
		682396,
		174,
		True
	},
	tip_build_ticket_not_enough = {
		682570,
		107,
		True
	},
	build_ship_tip_use_ticket = {
		682677,
		195,
		True
	},
	springfes_tips1 = {
		682872,
		907,
		True
	},
	worldinpicture_tavel_point_tip = {
		683779,
		126,
		True
	},
	worldinpicture_draw_point_tip = {
		683905,
		122,
		True
	},
	worldinpicture_help = {
		684027,
		1037,
		True
	},
	worldinpicture_task_help = {
		685064,
		1042,
		True
	},
	worldinpicture_not_area_can_draw = {
		686106,
		135,
		True
	},
	missile_attack_area_confirm = {
		686241,
		104,
		True
	},
	missile_attack_area_cancel = {
		686345,
		103,
		True
	},
	shipchange_alert_infleet = {
		686448,
		157,
		True
	},
	shipchange_alert_inpvp = {
		686605,
		168,
		True
	},
	shipchange_alert_inexercise = {
		686773,
		174,
		True
	},
	shipchange_alert_inworld = {
		686947,
		168,
		True
	},
	shipchange_alert_inguildbossevent = {
		687115,
		177,
		True
	},
	shipchange_alert_indiff = {
		687292,
		156,
		True
	},
	shipmodechange_reject_1stfleet_only = {
		687448,
		210,
		True
	},
	shipmodechange_reject_worldfleet_only = {
		687658,
		215,
		True
	},
	monopoly3thre_tip = {
		687873,
		151,
		True
	},
	fushun_game3_tip = {
		688024,
		1291,
		True
	},
	battlepass_main_tip_2202 = {
		689315,
		197,
		True
	},
	battlepass_main_help_2202 = {
		689512,
		2890,
		True
	},
	cruise_task_help_2202 = {
		692402,
		1092,
		True
	},
	battlepass_main_tip_2204 = {
		693494,
		200,
		True
	},
	battlepass_main_help_2204 = {
		693694,
		2881,
		True
	},
	cruise_task_help_2204 = {
		696575,
		1092,
		True
	},
	battlepass_main_tip_2206 = {
		697667,
		200,
		True
	},
	battlepass_main_help_2206 = {
		697867,
		2889,
		True
	},
	cruise_task_help_2206 = {
		700756,
		1092,
		True
	},
	battlepass_main_tip_2208 = {
		701848,
		199,
		True
	},
	battlepass_main_help_2208 = {
		702047,
		2893,
		True
	},
	cruise_task_help_2208 = {
		704940,
		1092,
		True
	},
	battlepass_main_tip_2210 = {
		706032,
		201,
		True
	},
	battlepass_main_help_2210 = {
		706233,
		2893,
		True
	},
	cruise_task_help_2210 = {
		709126,
		1092,
		True
	},
	battlepass_main_tip_2212 = {
		710218,
		224,
		True
	},
	battlepass_main_help_2212 = {
		710442,
		2900,
		True
	},
	cruise_task_help_2212 = {
		713342,
		1092,
		True
	},
	battlepass_main_tip_2302 = {
		714434,
		225,
		True
	},
	battlepass_main_help_2302 = {
		714659,
		2895,
		True
	},
	cruise_task_help_2302 = {
		717554,
		1092,
		True
	},
	battlepass_main_tip_2304 = {
		718646,
		233,
		True
	},
	battlepass_main_help_2304 = {
		718879,
		2913,
		True
	},
	cruise_task_help_2304 = {
		721792,
		1092,
		True
	},
	battlepass_main_tip_2306 = {
		722884,
		195,
		True
	},
	battlepass_main_help_2306 = {
		723079,
		2883,
		True
	},
	cruise_task_help_2306 = {
		725962,
		1092,
		True
	},
	battlepass_main_tip_2308 = {
		727054,
		197,
		True
	},
	battlepass_main_help_2308 = {
		727251,
		2885,
		True
	},
	cruise_task_help_2308 = {
		730136,
		1092,
		True
	},
	battlepass_main_tip_2310 = {
		731228,
		200,
		True
	},
	battlepass_main_help_2310 = {
		731428,
		2893,
		True
	},
	cruise_task_help_2310 = {
		734321,
		1092,
		True
	},
	battlepass_main_tip_2312 = {
		735413,
		196,
		True
	},
	battlepass_main_help_2312 = {
		735609,
		2898,
		True
	},
	cruise_task_help_2312 = {
		738507,
		1092,
		True
	},
	battlepass_main_tip_2402 = {
		739599,
		197,
		True
	},
	battlepass_main_help_2402 = {
		739796,
		2891,
		True
	},
	cruise_task_help_2402 = {
		742687,
		1092,
		True
	},
	battlepass_main_tip_2404 = {
		743779,
		223,
		True
	},
	battlepass_main_help_2404 = {
		744002,
		2901,
		True
	},
	cruise_task_help_2404 = {
		746903,
		1096,
		True
	},
	battlepass_main_tip_2406 = {
		747999,
		197,
		True
	},
	battlepass_main_help_2406 = {
		748196,
		2899,
		True
	},
	cruise_task_help_2406 = {
		751095,
		1092,
		True
	},
	attrset_reset = {
		752187,
		82,
		True
	},
	attrset_save = {
		752269,
		80,
		True
	},
	attrset_ask_save = {
		752349,
		133,
		True
	},
	attrset_save_success = {
		752482,
		103,
		True
	},
	attrset_disable = {
		752585,
		147,
		True
	},
	attrset_input_ill = {
		752732,
		93,
		True
	},
	blackfriday_help = {
		752825,
		805,
		True
	},
	eventshop_time_hint = {
		753630,
		100,
		True
	},
	purchase_backyard_theme_desc_for_onekey = {
		753730,
		142,
		True
	},
	purchase_backyard_theme_desc_for_all = {
		753872,
		127,
		True
	},
	sp_no_quota = {
		753999,
		108,
		True
	},
	fur_all_buy = {
		754107,
		82,
		True
	},
	fur_onekey_buy = {
		754189,
		85,
		True
	},
	littleRenown_npc = {
		754274,
		1402,
		True
	},
	tech_package_tip = {
		755676,
		241,
		True
	},
	backyard_food_shop_tip = {
		755917,
		96,
		True
	},
	dorm_2f_lock = {
		756013,
		82,
		True
	},
	word_get_way = {
		756095,
		90,
		True
	},
	word_get_date = {
		756185,
		94,
		True
	},
	enter_theme_name = {
		756279,
		113,
		True
	},
	enter_extend_food_label = {
		756392,
		93,
		True
	},
	backyard_extend_tip_1 = {
		756485,
		90,
		True
	},
	backyard_extend_tip_2 = {
		756575,
		103,
		True
	},
	backyard_extend_tip_3 = {
		756678,
		94,
		True
	},
	backyard_extend_tip_4 = {
		756772,
		85,
		True
	},
	email_text = {
		756857,
		79,
		True
	},
	emailhold_text = {
		756936,
		127,
		True
	},
	code_text = {
		757063,
		90,
		True
	},
	codehold_text = {
		757153,
		102,
		True
	},
	genBtn_text = {
		757255,
		83,
		True
	},
	desc_text = {
		757338,
		156,
		True
	},
	loginBtn_text = {
		757494,
		84,
		True
	},
	verification_code_req_tip1 = {
		757578,
		126,
		True
	},
	verification_code_req_tip2 = {
		757704,
		175,
		True
	},
	verification_code_req_tip3 = {
		757879,
		134,
		True
	},
	levelScene_remaster_story_tip = {
		758013,
		176,
		True
	},
	levelScene_remaster_unlock_tip = {
		758189,
		188,
		True
	},
	linkBtn_text = {
		758377,
		83,
		True
	},
	yostar_link_title = {
		758460,
		98,
		True
	},
	level_remaster_tip1 = {
		758558,
		95,
		True
	},
	level_remaster_tip2 = {
		758653,
		89,
		True
	},
	level_remaster_tip3 = {
		758742,
		90,
		True
	},
	level_remaster_tip4 = {
		758832,
		102,
		True
	},
	pay_cancel = {
		758934,
		88,
		True
	},
	order_error = {
		759022,
		101,
		True
	},
	pay_fail = {
		759123,
		86,
		True
	},
	user_cancel = {
		759209,
		94,
		True
	},
	system_error = {
		759303,
		88,
		True
	},
	time_out = {
		759391,
		109,
		True
	},
	server_error = {
		759500,
		102,
		True
	},
	data_error = {
		759602,
		98,
		True
	},
	share_success = {
		759700,
		97,
		True
	},
	shoot_screen_fail = {
		759797,
		98,
		True
	},
	server_name = {
		759895,
		87,
		True
	},
	non_support_share = {
		759982,
		134,
		True
	},
	save_success = {
		760116,
		99,
		True
	},
	word_guild_join_err1 = {
		760215,
		115,
		True
	},
	task_empty_tip_1 = {
		760330,
		104,
		True
	},
	task_empty_tip_2 = {
		760434,
		160,
		True
	},
	["airi_error_code_ 100210"] = {
		760594,
		126,
		True
	},
	["airi_error_code_ 100211"] = {
		760720,
		138,
		True
	},
	["airi_error_code_ 100212"] = {
		760858,
		116,
		True
	},
	["airi_error_code_ 100610"] = {
		760974,
		125,
		True
	},
	["airi_error_code_ 100611"] = {
		761099,
		120,
		True
	},
	["airi_error_code_ 100612"] = {
		761219,
		132,
		True
	},
	["airi_error_code_ 100710"] = {
		761351,
		127,
		True
	},
	["airi_error_code_ 100711"] = {
		761478,
		127,
		True
	},
	["airi_error_code_ 100712"] = {
		761605,
		135,
		True
	},
	["airi_error_code_ 100810"] = {
		761740,
		126,
		True
	},
	["airi_error_code_ 100811"] = {
		761866,
		138,
		True
	},
	["airi_error_code_ 100812"] = {
		762004,
		133,
		True
	},
	["airi_error_code_ 100813"] = {
		762137,
		125,
		True
	},
	["airi_error_code_ 100814"] = {
		762262,
		120,
		True
	},
	["airi_error_code_ 100815"] = {
		762382,
		132,
		True
	},
	["airi_error_code_ 100816"] = {
		762514,
		127,
		True
	},
	["airi_error_code_ 100817"] = {
		762641,
		127,
		True
	},
	["airi_error_code_ 100818"] = {
		762768,
		134,
		True
	},
	facebook_link_title = {
		762902,
		102,
		True
	},
	newserver_time = {
		763004,
		98,
		True
	},
	newserver_soldout = {
		763102,
		103,
		True
	},
	skill_learn_tip = {
		763205,
		133,
		True
	},
	newserver_build_tip = {
		763338,
		150,
		True
	},
	build_count_tip = {
		763488,
		85,
		True
	},
	help_research_package = {
		763573,
		299,
		True
	},
	lv70_package_tip = {
		763872,
		228,
		True
	},
	tech_select_tip1 = {
		764100,
		97,
		True
	},
	tech_select_tip2 = {
		764197,
		107,
		True
	},
	tech_select_tip3 = {
		764304,
		88,
		True
	},
	tech_select_tip4 = {
		764392,
		96,
		True
	},
	tech_select_tip5 = {
		764488,
		117,
		True
	},
	techpackage_item_use = {
		764605,
		203,
		True
	},
	techpackage_item_use_1 = {
		764808,
		238,
		True
	},
	techpackage_item_use_2 = {
		765046,
		200,
		True
	},
	techpackage_item_use_confirm = {
		765246,
		138,
		True
	},
	new_server_shop_sel_goods_tip = {
		765384,
		130,
		True
	},
	new_server_shop_unopen_tip = {
		765514,
		101,
		True
	},
	newserver_activity_tip = {
		765615,
		1685,
		True
	},
	newserver_shop_timelimit = {
		767300,
		106,
		True
	},
	tech_character_get = {
		767406,
		89,
		True
	},
	package_detail_tip = {
		767495,
		88,
		True
	},
	event_ui_consume = {
		767583,
		84,
		True
	},
	event_ui_recommend = {
		767667,
		91,
		True
	},
	event_ui_start = {
		767758,
		83,
		True
	},
	event_ui_giveup = {
		767841,
		85,
		True
	},
	event_ui_finish = {
		767926,
		87,
		True
	},
	nav_tactics_sel_skill_title = {
		768013,
		103,
		True
	},
	battle_result_confirm = {
		768116,
		92,
		True
	},
	battle_result_targets = {
		768208,
		92,
		True
	},
	battle_result_continue = {
		768300,
		103,
		True
	},
	index_L2D = {
		768403,
		76,
		True
	},
	index_DBG = {
		768479,
		84,
		True
	},
	index_BG = {
		768563,
		82,
		True
	},
	index_CANTUSE = {
		768645,
		91,
		True
	},
	index_UNUSE = {
		768736,
		81,
		True
	},
	index_BGM = {
		768817,
		84,
		True
	},
	without_ship_to_wear = {
		768901,
		124,
		True
	},
	choose_ship_to_wear_this_skin = {
		769025,
		136,
		True
	},
	skinatlas_search_holder = {
		769161,
		113,
		True
	},
	skinatlas_search_result_is_empty = {
		769274,
		143,
		True
	},
	chang_ship_skin_window_title = {
		769417,
		96,
		True
	},
	world_boss_item_info = {
		769513,
		350,
		True
	},
	world_past_boss_item_info = {
		769863,
		480,
		True
	},
	world_boss_lefttime = {
		770343,
		92,
		True
	},
	world_boss_item_count_noenough = {
		770435,
		145,
		True
	},
	world_boss_item_usage_tip = {
		770580,
		173,
		True
	},
	world_boss_no_select_archives = {
		770753,
		161,
		True
	},
	world_boss_archives_item_count_noenough = {
		770914,
		157,
		True
	},
	world_boss_archives_are_clear = {
		771071,
		156,
		True
	},
	world_boss_switch_archives = {
		771227,
		248,
		True
	},
	world_boss_switch_archives_success = {
		771475,
		146,
		True
	},
	world_boss_archives_auto_battle_unopen = {
		771621,
		169,
		True
	},
	world_boss_archives_need_stop_auto_battle = {
		771790,
		164,
		True
	},
	world_boss_archives_stop_auto_battle = {
		771954,
		137,
		True
	},
	world_boss_archives_continue_auto_battle = {
		772091,
		140,
		True
	},
	world_boss_archives_auto_battle_reusle_title = {
		772231,
		145,
		True
	},
	world_boss_archives_stop_auto_battle_title = {
		772376,
		146,
		True
	},
	world_boss_archives_stop_auto_battle_tip = {
		772522,
		119,
		True
	},
	world_boss_archives_stop_auto_battle_tip1 = {
		772641,
		241,
		True
	},
	world_archives_boss_help = {
		772882,
		3343,
		True
	},
	world_archives_boss_list_help = {
		776225,
		570,
		True
	},
	archives_boss_was_opened = {
		776795,
		163,
		True
	},
	current_boss_was_opened = {
		776958,
		162,
		True
	},
	world_boss_title_auto_battle = {
		777120,
		103,
		True
	},
	world_boss_title_highest_damge = {
		777223,
		105,
		True
	},
	world_boss_title_estimation = {
		777328,
		113,
		True
	},
	world_boss_title_battle_cnt = {
		777441,
		99,
		True
	},
	world_boss_title_consume_oil_cnt = {
		777540,
		104,
		True
	},
	world_boss_title_spend_time = {
		777644,
		104,
		True
	},
	world_boss_title_total_damage = {
		777748,
		102,
		True
	},
	world_no_time_to_auto_battle = {
		777850,
		143,
		True
	},
	world_boss_current_boss_label = {
		777993,
		104,
		True
	},
	world_boss_current_boss_label1 = {
		778097,
		107,
		True
	},
	world_boss_archives_boss_tip = {
		778204,
		158,
		True
	},
	world_boss_progress_no_enough = {
		778362,
		127,
		True
	},
	world_boss_auto_battle_no_oil = {
		778489,
		119,
		True
	},
	meta_syn_value_label = {
		778608,
		108,
		True
	},
	meta_syn_finish = {
		778716,
		103,
		True
	},
	index_meta_repair = {
		778819,
		104,
		True
	},
	index_meta_tactics = {
		778923,
		103,
		True
	},
	index_meta_energy = {
		779026,
		104,
		True
	},
	tactics_continue_to_learn_other_skill = {
		779130,
		162,
		True
	},
	tactics_continue_to_learn_other_ship_skill = {
		779292,
		161,
		True
	},
	tactics_no_recent_ships = {
		779453,
		113,
		True
	},
	activity_kill = {
		779566,
		95,
		True
	},
	battle_result_dmg = {
		779661,
		87,
		True
	},
	battle_result_kill_count = {
		779748,
		100,
		True
	},
	battle_result_toggle_on = {
		779848,
		96,
		True
	},
	battle_result_toggle_off = {
		779944,
		101,
		True
	},
	battle_result_continue_battle = {
		780045,
		101,
		True
	},
	battle_result_quit_battle = {
		780146,
		96,
		True
	},
	battle_result_share_battle = {
		780242,
		95,
		True
	},
	pre_combat_team = {
		780337,
		91,
		True
	},
	pre_combat_vanguard = {
		780428,
		91,
		True
	},
	pre_combat_main = {
		780519,
		83,
		True
	},
	pre_combat_submarine = {
		780602,
		93,
		True
	},
	pre_combat_targets = {
		780695,
		89,
		True
	},
	pre_combat_atlasloot = {
		780784,
		88,
		True
	},
	destroy_confirm_access = {
		780872,
		93,
		True
	},
	destroy_confirm_cancel = {
		780965,
		92,
		True
	},
	pt_count_tip = {
		781057,
		81,
		True
	},
	dockyard_data_loss_detected = {
		781138,
		167,
		True
	},
	littleEugen_npc = {
		781305,
		1374,
		True
	},
	five_shujuhuigu = {
		782679,
		121,
		True
	},
	five_shujuhuigu1 = {
		782800,
		89,
		True
	},
	littleChaijun_npc = {
		782889,
		1290,
		True
	},
	five_qingdian = {
		784179,
		622,
		True
	},
	friend_resume_title_detail = {
		784801,
		94,
		True
	},
	item_type13_tip1 = {
		784895,
		88,
		True
	},
	item_type13_tip2 = {
		784983,
		88,
		True
	},
	item_type16_tip1 = {
		785071,
		88,
		True
	},
	item_type16_tip2 = {
		785159,
		88,
		True
	},
	item_type17_tip1 = {
		785247,
		87,
		True
	},
	item_type17_tip2 = {
		785334,
		87,
		True
	},
	five_duomaomao = {
		785421,
		788,
		True
	},
	main_4 = {
		786209,
		75,
		True
	},
	main_5 = {
		786284,
		75,
		True
	},
	honor_medal_support_tips_display = {
		786359,
		460,
		True
	},
	honor_medal_support_tips_confirm = {
		786819,
		207,
		True
	},
	support_rate_title = {
		787026,
		87,
		True
	},
	support_times_limited = {
		787113,
		128,
		True
	},
	support_times_tip = {
		787241,
		95,
		True
	},
	build_times_tip = {
		787336,
		90,
		True
	},
	tactics_recent_ship_label = {
		787426,
		105,
		True
	},
	title_info = {
		787531,
		78,
		True
	},
	eventshop_unlock_info = {
		787609,
		93,
		True
	},
	eventshop_unlock_hint = {
		787702,
		142,
		True
	},
	commission_event_tip = {
		787844,
		818,
		True
	},
	decoration_medal_placeholder = {
		788662,
		122,
		True
	},
	technology_filter_placeholder = {
		788784,
		119,
		True
	},
	eva_comment_send_null = {
		788903,
		101,
		True
	},
	report_sent_thank = {
		789004,
		156,
		True
	},
	report_ship_cannot_comment = {
		789160,
		127,
		True
	},
	report_cannot_comment = {
		789287,
		137,
		True
	},
	report_sent_title = {
		789424,
		87,
		True
	},
	report_sent_desc = {
		789511,
		130,
		True
	},
	report_type_1 = {
		789641,
		98,
		True
	},
	report_type_1_1 = {
		789739,
		146,
		True
	},
	report_type_2 = {
		789885,
		94,
		True
	},
	report_type_2_1 = {
		789979,
		146,
		True
	},
	report_type_3 = {
		790125,
		88,
		True
	},
	report_type_3_1 = {
		790213,
		177,
		True
	},
	report_type_other = {
		790390,
		85,
		True
	},
	report_type_other_1 = {
		790475,
		145,
		True
	},
	report_type_other_2 = {
		790620,
		115,
		True
	},
	report_sent_help = {
		790735,
		440,
		True
	},
	rename_input = {
		791175,
		93,
		True
	},
	avatar_task_level = {
		791268,
		169,
		True
	},
	avatar_upgrad_1 = {
		791437,
		92,
		True
	},
	avatar_upgrad_2 = {
		791529,
		92,
		True
	},
	avatar_upgrad_3 = {
		791621,
		94,
		True
	},
	avatar_task_ship_1 = {
		791715,
		92,
		True
	},
	avatar_task_ship_2 = {
		791807,
		103,
		True
	},
	technology_queue_complete = {
		791910,
		97,
		True
	},
	technology_queue_processing = {
		792007,
		102,
		True
	},
	technology_queue_waiting = {
		792109,
		94,
		True
	},
	technology_queue_getaward = {
		792203,
		94,
		True
	},
	technology_daily_refresh = {
		792297,
		119,
		True
	},
	technology_queue_full = {
		792416,
		113,
		True
	},
	technology_queue_in_mission_incomplete = {
		792529,
		177,
		True
	},
	technology_consume = {
		792706,
		95,
		True
	},
	technology_request = {
		792801,
		103,
		True
	},
	technology_queue_in_doublecheck = {
		792904,
		242,
		True
	},
	playervtae_setting_btn_label = {
		793146,
		100,
		True
	},
	technology_queue_in_success = {
		793246,
		130,
		True
	},
	star_require_enemy_text = {
		793376,
		116,
		True
	},
	star_require_enemy_title = {
		793492,
		107,
		True
	},
	star_require_enemy_check = {
		793599,
		95,
		True
	},
	worldboss_rank_timer_label = {
		793694,
		116,
		True
	},
	technology_detail = {
		793810,
		88,
		True
	},
	technology_mission_unfinish = {
		793898,
		127,
		True
	},
	word_chinese = {
		794025,
		82,
		True
	},
	word_japanese_2 = {
		794107,
		80,
		True
	},
	word_japanese = {
		794187,
		78,
		True
	},
	avatarframe_got = {
		794265,
		84,
		True
	},
	item_is_max_cnt = {
		794349,
		110,
		True
	},
	level_fleet_ship_desc = {
		794459,
		103,
		True
	},
	level_fleet_sub_desc = {
		794562,
		95,
		True
	},
	summerland_tip = {
		794657,
		560,
		True
	},
	icecreamgame_tip = {
		795217,
		1578,
		True
	},
	unlock_date_tip = {
		796795,
		118,
		True
	},
	guild_duty_shoule_be_deputy_commander = {
		796913,
		164,
		True
	},
	guild_deputy_commander_cnt_is_full = {
		797077,
		154,
		True
	},
	guild_deputy_commander_cnt = {
		797231,
		153,
		True
	},
	mail_filter_placeholder = {
		797384,
		107,
		True
	},
	recently_sticker_placeholder = {
		797491,
		111,
		True
	},
	backhill_campusfestival_tip = {
		797602,
		1219,
		True
	},
	mini_cookgametip = {
		798821,
		1297,
		True
	},
	cook_game_Albacore = {
		800118,
		115,
		True
	},
	cook_game_august = {
		800233,
		109,
		True
	},
	cook_game_elbe = {
		800342,
		107,
		True
	},
	cook_game_hakuryu = {
		800449,
		125,
		True
	},
	cook_game_howe = {
		800574,
		140,
		True
	},
	cook_game_marcopolo = {
		800714,
		114,
		True
	},
	cook_game_noshiro = {
		800828,
		126,
		True
	},
	cook_game_pnelope = {
		800954,
		130,
		True
	},
	cook_game_laffey = {
		801084,
		171,
		True
	},
	cook_game_janus = {
		801255,
		150,
		True
	},
	cook_game_flandre = {
		801405,
		100,
		True
	},
	cook_game_constellation = {
		801505,
		187,
		True
	},
	cook_game_constellation_skill_name = {
		801692,
		134,
		True
	},
	cook_game_constellation_skill_desc = {
		801826,
		206,
		True
	},
	random_ship_on = {
		802032,
		127,
		True
	},
	random_ship_off_0 = {
		802159,
		181,
		True
	},
	random_ship_off = {
		802340,
		190,
		True
	},
	random_ship_forbidden = {
		802530,
		174,
		True
	},
	random_ship_now = {
		802704,
		97,
		True
	},
	random_ship_label = {
		802801,
		97,
		True
	},
	player_vitae_skin_setting = {
		802898,
		102,
		True
	},
	random_ship_tips1 = {
		803000,
		167,
		True
	},
	random_ship_tips2 = {
		803167,
		145,
		True
	},
	random_ship_before = {
		803312,
		113,
		True
	},
	random_ship_and_skin_title = {
		803425,
		101,
		True
	},
	random_ship_frequse_mode = {
		803526,
		102,
		True
	},
	random_ship_locked_mode = {
		803628,
		99,
		True
	},
	littleSpee_npc = {
		803727,
		1583,
		True
	},
	random_flag_ship = {
		805310,
		96,
		True
	},
	random_flag_ship_changskinBtn_label = {
		805406,
		111,
		True
	},
	expedition_drop_use_out = {
		805517,
		152,
		True
	},
	expedition_extra_drop_tip = {
		805669,
		104,
		True
	},
	ex_pass_use = {
		805773,
		79,
		True
	},
	defense_formation_tip_npc = {
		805852,
		203,
		True
	},
	pgs_login_tip = {
		806055,
		250,
		True
	},
	pgs_login_binding_exist1 = {
		806305,
		204,
		True
	},
	pgs_login_binding_exist2 = {
		806509,
		205,
		True
	},
	pgs_login_binding_exist3 = {
		806714,
		271,
		True
	},
	pgs_binding_account = {
		806985,
		108,
		True
	},
	pgs_unbind = {
		807093,
		92,
		True
	},
	pgs_unbind_tip1 = {
		807185,
		152,
		True
	},
	pgs_unbind_tip2 = {
		807337,
		214,
		True
	},
	word_item = {
		807551,
		77,
		True
	},
	word_tool = {
		807628,
		77,
		True
	},
	word_other = {
		807705,
		78,
		True
	},
	ryza_word_equip = {
		807783,
		83,
		True
	},
	ryza_rest_produce_count = {
		807866,
		109,
		True
	},
	ryza_composite_confirm = {
		807975,
		119,
		True
	},
	ryza_composite_confirm_single = {
		808094,
		122,
		True
	},
	ryza_composite_count = {
		808216,
		93,
		True
	},
	ryza_toggle_only_composite = {
		808309,
		112,
		True
	},
	ryza_tip_select_recipe = {
		808421,
		113,
		True
	},
	ryza_tip_put_materials = {
		808534,
		139,
		True
	},
	ryza_tip_composite_unlock = {
		808673,
		158,
		True
	},
	ryza_tip_unlock_all_tools = {
		808831,
		151,
		True
	},
	ryza_material_not_enough = {
		808982,
		168,
		True
	},
	ryza_tip_composite_invalid = {
		809150,
		132,
		True
	},
	ryza_tip_max_composite_count = {
		809282,
		136,
		True
	},
	ryza_tip_no_item = {
		809418,
		119,
		True
	},
	ryza_ui_show_acess = {
		809537,
		92,
		True
	},
	ryza_tip_no_recipe = {
		809629,
		103,
		True
	},
	ryza_tip_item_access = {
		809732,
		136,
		True
	},
	ryza_tip_control_buff_not_obtain_tip = {
		809868,
		143,
		True
	},
	ryza_tip_control_buff_upgrade = {
		810011,
		100,
		True
	},
	ryza_tip_control_buff_replace = {
		810111,
		100,
		True
	},
	ryza_tip_control_buff_limit = {
		810211,
		96,
		True
	},
	ryza_tip_control_buff_already_active_tip = {
		810307,
		111,
		True
	},
	ryza_tip_control_buff = {
		810418,
		163,
		True
	},
	ryza_tip_control_buff_not_obtain = {
		810581,
		103,
		True
	},
	ryza_tip_control = {
		810684,
		142,
		True
	},
	ryza_tip_main = {
		810826,
		1454,
		True
	},
	battle_levelScene_ryza_lock = {
		812280,
		186,
		True
	},
	ryza_tip_toast_item_got = {
		812466,
		96,
		True
	},
	ryza_composite_help_tip = {
		812562,
		476,
		True
	},
	ryza_control_help_tip = {
		813038,
		296,
		True
	},
	ryza_mini_game = {
		813334,
		351,
		True
	},
	ryza_task_level_desc = {
		813685,
		89,
		True
	},
	ryza_task_tag_explore = {
		813774,
		90,
		True
	},
	ryza_task_tag_battle = {
		813864,
		88,
		True
	},
	ryza_task_tag_dalegate = {
		813952,
		91,
		True
	},
	ryza_task_tag_develop = {
		814043,
		89,
		True
	},
	ryza_task_tag_adventure = {
		814132,
		97,
		True
	},
	ryza_task_tag_build = {
		814229,
		93,
		True
	},
	ryza_task_tag_create = {
		814322,
		92,
		True
	},
	ryza_task_tag_daily = {
		814414,
		90,
		True
	},
	ryza_task_detail_content = {
		814504,
		99,
		True
	},
	ryza_task_detail_award = {
		814603,
		93,
		True
	},
	ryza_task_go = {
		814696,
		83,
		True
	},
	ryza_task_get = {
		814779,
		84,
		True
	},
	ryza_task_get_all = {
		814863,
		92,
		True
	},
	ryza_task_confirm = {
		814955,
		88,
		True
	},
	ryza_task_cancel = {
		815043,
		86,
		True
	},
	ryza_task_level_num = {
		815129,
		93,
		True
	},
	ryza_task_level_add = {
		815222,
		95,
		True
	},
	ryza_task_submit = {
		815317,
		86,
		True
	},
	ryza_task_detail = {
		815403,
		85,
		True
	},
	ryza_composite_words = {
		815488,
		704,
		True
	},
	ryza_task_help_tip = {
		816192,
		345,
		True
	},
	hotspring_buff = {
		816537,
		140,
		True
	},
	random_ship_custom_mode_empty = {
		816677,
		148,
		True
	},
	random_ship_custom_mode_main_button_add = {
		816825,
		106,
		True
	},
	random_ship_custom_mode_main_button_remove = {
		816931,
		112,
		True
	},
	random_ship_custom_mode_main_tip1 = {
		817043,
		151,
		True
	},
	random_ship_custom_mode_main_tip2 = {
		817194,
		107,
		True
	},
	random_ship_custom_mode_main_empty = {
		817301,
		137,
		True
	},
	random_ship_custom_mode_select_all = {
		817438,
		108,
		True
	},
	random_ship_custom_mode_add_tip1 = {
		817546,
		158,
		True
	},
	random_ship_custom_mode_select_number = {
		817704,
		110,
		True
	},
	random_ship_custom_mode_add_complete = {
		817814,
		130,
		True
	},
	random_ship_custom_mode_add_tip2 = {
		817944,
		159,
		True
	},
	random_ship_custom_mode_remove_tip1 = {
		818103,
		166,
		True
	},
	random_ship_custom_mode_remove_complete = {
		818269,
		135,
		True
	},
	random_ship_custom_mode_remove_tip2 = {
		818404,
		166,
		True
	},
	index_dressed = {
		818570,
		89,
		True
	},
	random_ship_custom_mode = {
		818659,
		110,
		True
	},
	random_ship_custom_mode_add_title = {
		818769,
		110,
		True
	},
	random_ship_custom_mode_remove_title = {
		818879,
		116,
		True
	},
	hotspring_shop_enter1 = {
		818995,
		150,
		True
	},
	hotspring_shop_enter2 = {
		819145,
		143,
		True
	},
	hotspring_shop_insufficient = {
		819288,
		189,
		True
	},
	hotspring_shop_success1 = {
		819477,
		117,
		True
	},
	hotspring_shop_success2 = {
		819594,
		103,
		True
	},
	hotspring_shop_finish = {
		819697,
		173,
		True
	},
	hotspring_shop_end = {
		819870,
		155,
		True
	},
	hotspring_shop_touch1 = {
		820025,
		107,
		True
	},
	hotspring_shop_touch2 = {
		820132,
		128,
		True
	},
	hotspring_shop_touch3 = {
		820260,
		115,
		True
	},
	hotspring_shop_exchanged = {
		820375,
		154,
		True
	},
	hotspring_shop_exchange = {
		820529,
		184,
		True
	},
	hotspring_tip1 = {
		820713,
		130,
		True
	},
	hotspring_tip2 = {
		820843,
		104,
		True
	},
	hotspring_help = {
		820947,
		631,
		True
	},
	hotspring_expand = {
		821578,
		147,
		True
	},
	hotspring_shop_help = {
		821725,
		571,
		True
	},
	resorts_help = {
		822296,
		819,
		True
	},
	pvzminigame_help = {
		823115,
		1187,
		True
	},
	tips_yuandanhuoyue2023 = {
		824302,
		745,
		True
	},
	beach_guard_chaijun = {
		825047,
		159,
		True
	},
	beach_guard_jianye = {
		825206,
		164,
		True
	},
	beach_guard_lituoliao = {
		825370,
		279,
		True
	},
	beach_guard_bominghan = {
		825649,
		237,
		True
	},
	beach_guard_nengdai = {
		825886,
		269,
		True
	},
	beach_guard_m_craft = {
		826155,
		121,
		True
	},
	beach_guard_m_atk = {
		826276,
		111,
		True
	},
	beach_guard_m_guard = {
		826387,
		107,
		True
	},
	beach_guard_m_craft_name = {
		826494,
		98,
		True
	},
	beach_guard_m_atk_name = {
		826592,
		94,
		True
	},
	beach_guard_m_guard_name = {
		826686,
		97,
		True
	},
	beach_guard_e1 = {
		826783,
		87,
		True
	},
	beach_guard_e2 = {
		826870,
		84,
		True
	},
	beach_guard_e3 = {
		826954,
		87,
		True
	},
	beach_guard_e4 = {
		827041,
		85,
		True
	},
	beach_guard_e5 = {
		827126,
		87,
		True
	},
	beach_guard_e6 = {
		827213,
		84,
		True
	},
	beach_guard_e7 = {
		827297,
		86,
		True
	},
	beach_guard_e1_desc = {
		827383,
		135,
		True
	},
	beach_guard_e2_desc = {
		827518,
		142,
		True
	},
	beach_guard_e3_desc = {
		827660,
		140,
		True
	},
	beach_guard_e4_desc = {
		827800,
		137,
		True
	},
	beach_guard_e5_desc = {
		827937,
		130,
		True
	},
	beach_guard_e6_desc = {
		828067,
		235,
		True
	},
	beach_guard_e7_desc = {
		828302,
		166,
		True
	},
	ninghai_nianye = {
		828468,
		142,
		True
	},
	yingrui_nianye = {
		828610,
		142,
		True
	},
	zhaohe_nianye = {
		828752,
		135,
		True
	},
	zhenhai_nianye = {
		828887,
		143,
		True
	},
	haitian_nianye = {
		829030,
		153,
		True
	},
	taiyuan_nianye = {
		829183,
		148,
		True
	},
	yixian_nianye = {
		829331,
		166,
		True
	},
	activity_yanhua_tip1 = {
		829497,
		93,
		True
	},
	activity_yanhua_tip2 = {
		829590,
		103,
		True
	},
	activity_yanhua_tip3 = {
		829693,
		103,
		True
	},
	activity_yanhua_tip4 = {
		829796,
		139,
		True
	},
	activity_yanhua_tip5 = {
		829935,
		120,
		True
	},
	activity_yanhua_tip6 = {
		830055,
		124,
		True
	},
	activity_yanhua_tip7 = {
		830179,
		158,
		True
	},
	activity_yanhua_tip8 = {
		830337,
		103,
		True
	},
	help_chunjie2023 = {
		830440,
		1441,
		True
	},
	sevenday_nianye = {
		831881,
		406,
		True
	},
	tip_nianye = {
		832287,
		122,
		True
	},
	couplete_activty_desc = {
		832409,
		351,
		True
	},
	couplete_click_desc = {
		832760,
		131,
		True
	},
	couplet_index_desc = {
		832891,
		89,
		True
	},
	couplete_help = {
		832980,
		770,
		True
	},
	couplete_drag_tip = {
		833750,
		133,
		True
	},
	couplete_remind = {
		833883,
		114,
		True
	},
	couplete_complete = {
		833997,
		132,
		True
	},
	couplete_enter = {
		834129,
		114,
		True
	},
	couplete_stay = {
		834243,
		107,
		True
	},
	couplete_task = {
		834350,
		135,
		True
	},
	couplete_pass_1 = {
		834485,
		96,
		True
	},
	couplete_pass_2 = {
		834581,
		100,
		True
	},
	couplete_fail_1 = {
		834681,
		119,
		True
	},
	couplete_fail_2 = {
		834800,
		117,
		True
	},
	couplete_pair_1 = {
		834917,
		123,
		True
	},
	couplete_pair_2 = {
		835040,
		113,
		True
	},
	couplete_pair_3 = {
		835153,
		119,
		True
	},
	couplete_pair_4 = {
		835272,
		113,
		True
	},
	couplete_pair_5 = {
		835385,
		126,
		True
	},
	couplete_pair_6 = {
		835511,
		119,
		True
	},
	couplete_pair_7 = {
		835630,
		113,
		True
	},
	["2023spring_minigame_item_lantern"] = {
		835743,
		183,
		True
	},
	["2023spring_minigame_item_firecracker"] = {
		835926,
		188,
		True
	},
	["2023spring_minigame_skill_icewall"] = {
		836114,
		149,
		True
	},
	["2023spring_minigame_skill_icewall_up"] = {
		836263,
		223,
		True
	},
	["2023spring_minigame_skill_sprint"] = {
		836486,
		151,
		True
	},
	["2023spring_minigame_skill_sprint_up"] = {
		836637,
		227,
		True
	},
	["2023spring_minigame_skill_flash"] = {
		836864,
		180,
		True
	},
	["2023spring_minigame_skill_flash_up"] = {
		837044,
		200,
		True
	},
	["2023spring_minigame_bless_speed"] = {
		837244,
		136,
		True
	},
	["2023spring_minigame_bless_speed_up"] = {
		837380,
		211,
		True
	},
	["2023spring_minigame_bless_substitute"] = {
		837591,
		204,
		True
	},
	["2023spring_minigame_bless_substitute_up"] = {
		837795,
		127,
		True
	},
	["2023spring_minigame_nenjuu_skill1"] = {
		837922,
		199,
		True
	},
	["2023spring_minigame_nenjuu_skill2"] = {
		838121,
		146,
		True
	},
	["2023spring_minigame_nenjuu_skill3"] = {
		838267,
		158,
		True
	},
	["2023spring_minigame_nenjuu_skill4"] = {
		838425,
		139,
		True
	},
	["2023spring_minigame_nenjuu_skill5"] = {
		838564,
		214,
		True
	},
	["2023spring_minigame_nenjuu_skill6"] = {
		838778,
		158,
		True
	},
	["2023spring_minigame_nenjuu_skill7"] = {
		838936,
		234,
		True
	},
	["2023spring_minigame_nenjuu_skill8"] = {
		839170,
		219,
		True
	},
	["2023spring_minigame_tip1"] = {
		839389,
		93,
		True
	},
	["2023spring_minigame_tip2"] = {
		839482,
		96,
		True
	},
	["2023spring_minigame_tip3"] = {
		839578,
		93,
		True
	},
	["2023spring_minigame_tip5"] = {
		839671,
		136,
		True
	},
	["2023spring_minigame_tip6"] = {
		839807,
		100,
		True
	},
	["2023spring_minigame_tip7"] = {
		839907,
		100,
		True
	},
	["2023spring_minigame_help"] = {
		840007,
		1226,
		True
	},
	multiple_sorties_title = {
		841233,
		97,
		True
	},
	multiple_sorties_title_eng = {
		841330,
		106,
		True
	},
	multiple_sorties_locked_tip = {
		841436,
		180,
		True
	},
	multiple_sorties_times = {
		841616,
		93,
		True
	},
	multiple_sorties_tip = {
		841709,
		206,
		True
	},
	multiple_sorties_challenge_ticket_use = {
		841915,
		118,
		True
	},
	multiple_sorties_cost1 = {
		842033,
		150,
		True
	},
	multiple_sorties_cost2 = {
		842183,
		159,
		True
	},
	multiple_sorties_cost3 = {
		842342,
		184,
		True
	},
	multiple_sorties_stopped = {
		842526,
		95,
		True
	},
	multiple_sorties_stop_tip = {
		842621,
		186,
		True
	},
	multiple_sorties_resume_tip = {
		842807,
		138,
		True
	},
	multiple_sorties_auto_on = {
		842945,
		132,
		True
	},
	multiple_sorties_finish = {
		843077,
		108,
		True
	},
	multiple_sorties_stop = {
		843185,
		105,
		True
	},
	multiple_sorties_stop_end = {
		843290,
		118,
		True
	},
	multiple_sorties_end_status = {
		843408,
		181,
		True
	},
	multiple_sorties_finish_tip = {
		843589,
		140,
		True
	},
	multiple_sorties_stop_tip_end = {
		843729,
		146,
		True
	},
	multiple_sorties_stop_reason1 = {
		843875,
		118,
		True
	},
	multiple_sorties_stop_reason2 = {
		843993,
		147,
		True
	},
	multiple_sorties_stop_reason3 = {
		844140,
		125,
		True
	},
	multiple_sorties_stop_reason4 = {
		844265,
		131,
		True
	},
	multiple_sorties_main_tip = {
		844396,
		253,
		True
	},
	multiple_sorties_main_end = {
		844649,
		204,
		True
	},
	multiple_sorties_rest_time = {
		844853,
		105,
		True
	},
	multiple_sorties_retry_desc = {
		844958,
		108,
		True
	},
	msgbox_text_battle = {
		845066,
		88,
		True
	},
	pre_combat_start = {
		845154,
		86,
		True
	},
	pre_combat_start_en = {
		845240,
		95,
		True
	},
	["2023Valentine_minigame_s"] = {
		845335,
		181,
		True
	},
	["2023Valentine_minigame_a"] = {
		845516,
		165,
		True
	},
	["2023Valentine_minigame_b"] = {
		845681,
		179,
		True
	},
	["2023Valentine_minigame_c"] = {
		845860,
		176,
		True
	},
	["2023Valentine_minigame_label1"] = {
		846036,
		99,
		True
	},
	["2023Valentine_minigame_label2"] = {
		846135,
		110,
		True
	},
	["2023Valentine_minigame_label3"] = {
		846245,
		104,
		True
	},
	sort_energy = {
		846349,
		81,
		True
	},
	dockyard_search_holder = {
		846430,
		100,
		True
	},
	loveletter_exchange_tip1 = {
		846530,
		154,
		True
	},
	loveletter_exchange_tip2 = {
		846684,
		140,
		True
	},
	loveletter_exchange_confirm = {
		846824,
		312,
		True
	},
	loveletter_exchange_button = {
		847136,
		97,
		True
	},
	loveletter_exchange_tip3 = {
		847233,
		163,
		True
	},
	battle_text_common_1 = {
		847396,
		179,
		True
	},
	battle_text_common_2 = {
		847575,
		235,
		True
	},
	battle_text_common_3 = {
		847810,
		192,
		True
	},
	battle_text_yingxiv4_1 = {
		848002,
		140,
		True
	},
	battle_text_yingxiv4_2 = {
		848142,
		143,
		True
	},
	battle_text_yingxiv4_3 = {
		848285,
		141,
		True
	},
	battle_text_yingxiv4_4 = {
		848426,
		146,
		True
	},
	battle_text_yingxiv4_5 = {
		848572,
		138,
		True
	},
	battle_text_yingxiv4_6 = {
		848710,
		146,
		True
	},
	battle_text_yingxiv4_7 = {
		848856,
		150,
		True
	},
	battle_text_yingxiv4_8 = {
		849006,
		152,
		True
	},
	battle_text_yingxiv4_9 = {
		849158,
		152,
		True
	},
	battle_text_yingxiv4_10 = {
		849310,
		148,
		True
	},
	battle_text_bisimaiz_1 = {
		849458,
		136,
		True
	},
	battle_text_bisimaiz_2 = {
		849594,
		136,
		True
	},
	battle_text_bisimaiz_3 = {
		849730,
		136,
		True
	},
	battle_text_bisimaiz_4 = {
		849866,
		136,
		True
	},
	battle_text_bisimaiz_5 = {
		850002,
		136,
		True
	},
	battle_text_bisimaiz_6 = {
		850138,
		136,
		True
	},
	battle_text_bisimaiz_7 = {
		850274,
		167,
		True
	},
	battle_text_bisimaiz_8 = {
		850441,
		239,
		True
	},
	battle_text_bisimaiz_9 = {
		850680,
		250,
		True
	},
	battle_text_bisimaiz_10 = {
		850930,
		207,
		True
	},
	battle_text_yunxian_1 = {
		851137,
		172,
		True
	},
	battle_text_yunxian_2 = {
		851309,
		175,
		True
	},
	battle_text_yunxian_3 = {
		851484,
		155,
		True
	},
	battle_text_haidao_1 = {
		851639,
		151,
		True
	},
	battle_text_haidao_2 = {
		851790,
		174,
		True
	},
	battle_text_tongmeng_1 = {
		851964,
		134,
		True
	},
	battle_text_luodeni_1 = {
		852098,
		173,
		True
	},
	battle_text_luodeni_2 = {
		852271,
		202,
		True
	},
	battle_text_luodeni_3 = {
		852473,
		187,
		True
	},
	series_enemy_mood = {
		852660,
		91,
		True
	},
	series_enemy_mood_error = {
		852751,
		169,
		True
	},
	series_enemy_reward_tip1 = {
		852920,
		100,
		True
	},
	series_enemy_reward_tip2 = {
		853020,
		112,
		True
	},
	series_enemy_reward_tip3 = {
		853132,
		101,
		True
	},
	series_enemy_reward_tip4 = {
		853233,
		98,
		True
	},
	series_enemy_cost = {
		853331,
		92,
		True
	},
	series_enemy_SP_count = {
		853423,
		104,
		True
	},
	series_enemy_SP_error = {
		853527,
		118,
		True
	},
	series_enemy_unlock = {
		853645,
		126,
		True
	},
	series_enemy_storyunlock = {
		853771,
		119,
		True
	},
	series_enemy_storyreward = {
		853890,
		97,
		True
	},
	series_enemy_help = {
		853987,
		2106,
		True
	},
	series_enemy_score = {
		856093,
		87,
		True
	},
	series_enemy_total_score = {
		856180,
		99,
		True
	},
	setting_label_private = {
		856279,
		85,
		True
	},
	setting_label_licence = {
		856364,
		85,
		True
	},
	series_enemy_reward = {
		856449,
		104,
		True
	},
	series_enemy_mode_1 = {
		856553,
		97,
		True
	},
	series_enemy_mode_2 = {
		856650,
		99,
		True
	},
	series_enemy_fleet_prefix = {
		856749,
		97,
		True
	},
	series_enemy_team_notenough = {
		856846,
		232,
		True
	},
	series_enemy_empty_commander_main = {
		857078,
		108,
		True
	},
	series_enemy_empty_commander_assistant = {
		857186,
		111,
		True
	},
	limit_team_character_tips = {
		857297,
		154,
		True
	},
	game_room_help = {
		857451,
		1337,
		True
	},
	game_cannot_go = {
		858788,
		113,
		True
	},
	game_ticket_notenough = {
		858901,
		143,
		True
	},
	game_ticket_max_all = {
		859044,
		204,
		True
	},
	game_ticket_max_month = {
		859248,
		206,
		True
	},
	game_icon_notenough = {
		859454,
		135,
		True
	},
	game_goldbyicon = {
		859589,
		131,
		True
	},
	game_icon_max = {
		859720,
		189,
		True
	},
	caibulin_tip1 = {
		859909,
		141,
		True
	},
	caibulin_tip2 = {
		860050,
		163,
		True
	},
	caibulin_tip3 = {
		860213,
		141,
		True
	},
	caibulin_tip4 = {
		860354,
		162,
		True
	},
	caibulin_tip5 = {
		860516,
		141,
		True
	},
	caibulin_tip6 = {
		860657,
		163,
		True
	},
	caibulin_tip7 = {
		860820,
		141,
		True
	},
	caibulin_tip8 = {
		860961,
		165,
		True
	},
	caibulin_tip9 = {
		861126,
		162,
		True
	},
	caibulin_tip10 = {
		861288,
		177,
		True
	},
	caibulin_help = {
		861465,
		510,
		True
	},
	caibulin_tip11 = {
		861975,
		167,
		True
	},
	caibulin_lock_tip = {
		862142,
		123,
		True
	},
	gametip_xiaoqiye = {
		862265,
		1526,
		True
	},
	event_recommend_level1 = {
		863791,
		176,
		True
	},
	doa_minigame_Luna = {
		863967,
		85,
		True
	},
	doa_minigame_Misaki = {
		864052,
		89,
		True
	},
	doa_minigame_Marie = {
		864141,
		92,
		True
	},
	doa_minigame_Tamaki = {
		864233,
		89,
		True
	},
	doa_minigame_help = {
		864322,
		294,
		True
	},
	gametip_xiaokewei = {
		864616,
		1526,
		True
	},
	doa_character_select_confirm = {
		866142,
		239,
		True
	},
	blueprint_combatperformance = {
		866381,
		102,
		True
	},
	blueprint_shipperformance = {
		866483,
		94,
		True
	},
	blueprint_researching = {
		866577,
		98,
		True
	},
	sculpture_drawline_tip = {
		866675,
		130,
		True
	},
	sculpture_drawline_done = {
		866805,
		151,
		True
	},
	sculpture_drawline_exit = {
		866956,
		181,
		True
	},
	sculpture_puzzle_tip = {
		867137,
		162,
		True
	},
	sculpture_gratitude_tip = {
		867299,
		131,
		True
	},
	sculpture_close_tip = {
		867430,
		97,
		True
	},
	gift_act_help = {
		867527,
		713,
		True
	},
	gift_act_drawline_help = {
		868240,
		722,
		True
	},
	gift_act_tips = {
		868962,
		92,
		True
	},
	expedition_award_tip = {
		869054,
		150,
		True
	},
	island_act_tips1 = {
		869204,
		94,
		True
	},
	haidaojudian_help = {
		869298,
		2479,
		True
	},
	haidaojudian_building_tip = {
		871777,
		139,
		True
	},
	workbench_help = {
		871916,
		653,
		True
	},
	workbench_need_materials = {
		872569,
		104,
		True
	},
	workbench_tips1 = {
		872673,
		103,
		True
	},
	workbench_tips2 = {
		872776,
		110,
		True
	},
	workbench_tips3 = {
		872886,
		117,
		True
	},
	workbench_tips4 = {
		873003,
		114,
		True
	},
	workbench_tips5 = {
		873117,
		114,
		True
	},
	workbench_tips6 = {
		873231,
		88,
		True
	},
	workbench_tips7 = {
		873319,
		88,
		True
	},
	workbench_tips8 = {
		873407,
		87,
		True
	},
	workbench_tips9 = {
		873494,
		95,
		True
	},
	workbench_tips10 = {
		873589,
		102,
		True
	},
	island_help = {
		873691,
		610,
		True
	},
	islandnode_tips1 = {
		874301,
		92,
		True
	},
	islandnode_tips2 = {
		874393,
		84,
		True
	},
	islandnode_tips3 = {
		874477,
		105,
		True
	},
	islandnode_tips4 = {
		874582,
		105,
		True
	},
	islandnode_tips5 = {
		874687,
		113,
		True
	},
	islandnode_tips6 = {
		874800,
		116,
		True
	},
	islandnode_tips7 = {
		874916,
		125,
		True
	},
	islandnode_tips8 = {
		875041,
		151,
		True
	},
	islandnode_tips9 = {
		875192,
		142,
		True
	},
	islandshop_tips1 = {
		875334,
		98,
		True
	},
	islandshop_tips2 = {
		875432,
		87,
		True
	},
	islandshop_tips3 = {
		875519,
		84,
		True
	},
	islandshop_tips4 = {
		875603,
		95,
		True
	},
	island_shop_limit_error = {
		875698,
		146,
		True
	},
	haidaojudian_upgrade_limit = {
		875844,
		154,
		True
	},
	chargetip_monthcard_1 = {
		875998,
		145,
		True
	},
	chargetip_monthcard_2 = {
		876143,
		145,
		True
	},
	chargetip_crusing = {
		876288,
		102,
		True
	},
	chargetip_giftpackage = {
		876390,
		141,
		True
	},
	package_view_1 = {
		876531,
		131,
		True
	},
	package_view_2 = {
		876662,
		143,
		True
	},
	package_view_3 = {
		876805,
		99,
		True
	},
	package_view_4 = {
		876904,
		87,
		True
	},
	probabilityskinshop_tip = {
		876991,
		175,
		True
	},
	skin_gift_desc = {
		877166,
		258,
		True
	},
	springtask_tip = {
		877424,
		307,
		True
	},
	island_build_desc = {
		877731,
		132,
		True
	},
	island_history_desc = {
		877863,
		146,
		True
	},
	island_build_level = {
		878009,
		91,
		True
	},
	island_game_limit_help = {
		878100,
		143,
		True
	},
	island_game_limit_num = {
		878243,
		94,
		True
	},
	ore_minigame_help = {
		878337,
		954,
		True
	},
	meta_shop_exchange_limit_2 = {
		879291,
		96,
		True
	},
	meta_shop_tip = {
		879387,
		138,
		True
	},
	pt_shop_tran_tip = {
		879525,
		275,
		True
	},
	urdraw_tip = {
		879800,
		125,
		True
	},
	urdraw_complement = {
		879925,
		170,
		True
	},
	meta_class_t_level_1 = {
		880095,
		95,
		True
	},
	meta_class_t_level_2 = {
		880190,
		102,
		True
	},
	meta_class_t_level_3 = {
		880292,
		99,
		True
	},
	meta_class_t_level_4 = {
		880391,
		100,
		True
	},
	meta_class_t_level_5 = {
		880491,
		99,
		True
	},
	meta_shop_exchange_limit_tip = {
		880590,
		121,
		True
	},
	meta_shop_exchange_limit_2_tip = {
		880711,
		143,
		True
	},
	charge_tip_crusing_label = {
		880854,
		101,
		True
	},
	mktea_1 = {
		880955,
		144,
		True
	},
	mktea_2 = {
		881099,
		155,
		True
	},
	mktea_3 = {
		881254,
		159,
		True
	},
	mktea_4 = {
		881413,
		233,
		True
	},
	mktea_5 = {
		881646,
		222,
		True
	},
	random_skin_list_item_desc_label = {
		881868,
		99,
		True
	},
	notice_input_desc = {
		881967,
		99,
		True
	},
	notice_label_send = {
		882066,
		85,
		True
	},
	notice_label_room = {
		882151,
		88,
		True
	},
	notice_label_recv = {
		882239,
		90,
		True
	},
	notice_label_tip = {
		882329,
		123,
		True
	},
	littleTaihou_npc = {
		882452,
		1771,
		True
	},
	disassemble_selected = {
		884223,
		92,
		True
	},
	disassemble_available = {
		884315,
		95,
		True
	},
	ship_formationUI_fleetName_challenge = {
		884410,
		115,
		True
	},
	ship_formationUI_fleetName_challenge_sub = {
		884525,
		119,
		True
	},
	word_status_activity = {
		884644,
		92,
		True
	},
	word_status_challenge = {
		884736,
		97,
		True
	},
	shipmodechange_reject_inactivity = {
		884833,
		188,
		True
	},
	shipmodechange_reject_inchallenge = {
		885021,
		192,
		True
	},
	battle_result_total_time = {
		885213,
		99,
		True
	},
	charge_game_room_coin_tip = {
		885312,
		193,
		True
	},
	game_room_shooting_tip = {
		885505,
		100,
		True
	},
	mini_game_shop_ticked_not_enough = {
		885605,
		154,
		True
	},
	game_ticket_current_month = {
		885759,
		103,
		True
	},
	game_icon_max_full = {
		885862,
		138,
		True
	},
	pre_combat_consume = {
		886000,
		87,
		True
	},
	file_down_msgbox = {
		886087,
		191,
		True
	},
	file_down_mgr_title = {
		886278,
		114,
		True
	},
	file_down_mgr_progress = {
		886392,
		91,
		True
	},
	file_down_mgr_error = {
		886483,
		157,
		True
	},
	last_building_not_shown = {
		886640,
		119,
		True
	},
	setting_group_prefs_tip = {
		886759,
		122,
		True
	},
	group_prefs_switch_tip = {
		886881,
		159,
		True
	},
	main_group_msgbox_content = {
		887040,
		184,
		True
	},
	word_maingroup_checking = {
		887224,
		98,
		True
	},
	word_maingroup_checktoupdate = {
		887322,
		107,
		True
	},
	word_maingroup_checkfailure = {
		887429,
		122,
		True
	},
	word_maingroup_updating = {
		887551,
		98,
		True
	},
	word_maingroup_updatesuccess = {
		887649,
		108,
		True
	},
	word_maingroup_updatefailure = {
		887757,
		125,
		True
	},
	group_download_tip = {
		887882,
		156,
		True
	},
	word_manga_checking = {
		888038,
		94,
		True
	},
	word_manga_checktoupdate = {
		888132,
		103,
		True
	},
	word_manga_checkfailure = {
		888235,
		118,
		True
	},
	word_manga_updating = {
		888353,
		98,
		True
	},
	word_manga_updatesuccess = {
		888451,
		104,
		True
	},
	word_manga_updatefailure = {
		888555,
		121,
		True
	},
	cryptolalia_lock_res = {
		888676,
		102,
		True
	},
	cryptolalia_not_download_res = {
		888778,
		113,
		True
	},
	cryptolalia_timelimie = {
		888891,
		92,
		True
	},
	cryptolalia_label_downloading = {
		888983,
		114,
		True
	},
	cryptolalia_delete_res = {
		889097,
		104,
		True
	},
	cryptolalia_delete_res_tip = {
		889201,
		133,
		True
	},
	cryptolalia_delete_res_title = {
		889334,
		107,
		True
	},
	cryptolalia_use_gem_title = {
		889441,
		105,
		True
	},
	cryptolalia_use_ticket_title = {
		889546,
		111,
		True
	},
	cryptolalia_exchange = {
		889657,
		94,
		True
	},
	cryptolalia_exchange_success = {
		889751,
		107,
		True
	},
	cryptolalia_list_title = {
		889858,
		93,
		True
	},
	cryptolalia_list_subtitle = {
		889951,
		100,
		True
	},
	cryptolalia_download_done = {
		890051,
		106,
		True
	},
	cryptolalia_coming_soom = {
		890157,
		101,
		True
	},
	cryptolalia_unopen = {
		890258,
		88,
		True
	},
	cryptolalia_no_ticket = {
		890346,
		164,
		True
	},
	cryptolalia_entrance_coming_soom = {
		890510,
		118,
		True
	},
	ship_formationUI_fleetName_sp = {
		890628,
		111,
		True
	},
	ship_formationUI_fleetName_sp_ss = {
		890739,
		118,
		True
	},
	activityboss_sp_all_buff = {
		890857,
		98,
		True
	},
	activityboss_sp_best_score = {
		890955,
		101,
		True
	},
	activityboss_sp_display_reward = {
		891056,
		106,
		True
	},
	activityboss_sp_score_bonus = {
		891162,
		103,
		True
	},
	activityboss_sp_active_buff = {
		891265,
		99,
		True
	},
	activityboss_sp_window_best_score = {
		891364,
		114,
		True
	},
	activityboss_sp_score_target = {
		891478,
		105,
		True
	},
	activityboss_sp_score = {
		891583,
		95,
		True
	},
	activityboss_sp_score_update = {
		891678,
		106,
		True
	},
	activityboss_sp_score_not_update = {
		891784,
		118,
		True
	},
	collect_page_got = {
		891902,
		89,
		True
	},
	charge_menu_month_tip = {
		891991,
		178,
		True
	},
	activity_shop_title = {
		892169,
		88,
		True
	},
	street_shop_title = {
		892257,
		85,
		True
	},
	military_shop_title = {
		892342,
		88,
		True
	},
	quota_shop_title1 = {
		892430,
		92,
		True
	},
	sham_shop_title = {
		892522,
		89,
		True
	},
	fragment_shop_title = {
		892611,
		88,
		True
	},
	guild_shop_title = {
		892699,
		85,
		True
	},
	medal_shop_title = {
		892784,
		85,
		True
	},
	meta_shop_title = {
		892869,
		83,
		True
	},
	mini_game_shop_title = {
		892952,
		89,
		True
	},
	metaskill_up = {
		893041,
		187,
		True
	},
	metaskill_overflow_tip = {
		893228,
		163,
		True
	},
	msgbox_repair_cipher = {
		893391,
		103,
		True
	},
	msgbox_repair_title = {
		893494,
		89,
		True
	},
	equip_skin_detail_count = {
		893583,
		93,
		True
	},
	faest_nothing_to_get = {
		893676,
		105,
		True
	},
	feast_click_to_close = {
		893781,
		98,
		True
	},
	feast_invitation_btn_label = {
		893879,
		108,
		True
	},
	feast_task_btn_label = {
		893987,
		96,
		True
	},
	feast_task_pt_label = {
		894083,
		91,
		True
	},
	feast_task_pt_level = {
		894174,
		89,
		True
	},
	feast_task_pt_get = {
		894263,
		91,
		True
	},
	feast_task_pt_got = {
		894354,
		89,
		True
	},
	feast_task_tag_daily = {
		894443,
		89,
		True
	},
	feast_task_tag_activity = {
		894532,
		94,
		True
	},
	feast_label_make_invitation = {
		894626,
		106,
		True
	},
	feast_no_invitation = {
		894732,
		108,
		True
	},
	feast_no_gift = {
		894840,
		96,
		True
	},
	feast_label_give_invitation = {
		894936,
		106,
		True
	},
	feast_label_give_invitation_finish = {
		895042,
		113,
		True
	},
	feast_label_give_gift = {
		895155,
		94,
		True
	},
	feast_label_give_gift_finish = {
		895249,
		101,
		True
	},
	feast_label_make_ticket_tip = {
		895350,
		151,
		True
	},
	feast_label_make_ticket_click_tip = {
		895501,
		118,
		True
	},
	feast_label_make_ticket_failed_tip = {
		895619,
		153,
		True
	},
	feast_res_window_title = {
		895772,
		93,
		True
	},
	feast_res_window_go_label = {
		895865,
		91,
		True
	},
	feast_tip = {
		895956,
		422,
		True
	},
	feast_invitation_part1 = {
		896378,
		134,
		True
	},
	feast_invitation_part2 = {
		896512,
		260,
		True
	},
	feast_invitation_part3 = {
		896772,
		278,
		True
	},
	feast_invitation_part4 = {
		897050,
		218,
		True
	},
	uscastle2023_help = {
		897268,
		1519,
		True
	},
	feast_cant_give_gift_tip = {
		898787,
		154,
		True
	},
	uscastle2023_minigame_help = {
		898941,
		367,
		True
	},
	feast_drag_invitation_tip = {
		899308,
		143,
		True
	},
	feast_drag_gift_tip = {
		899451,
		131,
		True
	},
	shoot_preview = {
		899582,
		91,
		True
	},
	hit_preview = {
		899673,
		90,
		True
	},
	story_label_skip = {
		899763,
		84,
		True
	},
	story_label_auto = {
		899847,
		84,
		True
	},
	launch_ball_skill_desc = {
		899931,
		93,
		True
	},
	launch_ball_hatsuduki_skill_1 = {
		900024,
		114,
		True
	},
	launch_ball_hatsuduki_skill_1_desc = {
		900138,
		172,
		True
	},
	launch_ball_hatsuduki_skill_2 = {
		900310,
		127,
		True
	},
	launch_ball_hatsuduki_skill_2_desc = {
		900437,
		334,
		True
	},
	launch_ball_shinano_skill_1 = {
		900771,
		113,
		True
	},
	launch_ball_shinano_skill_1_desc = {
		900884,
		193,
		True
	},
	launch_ball_shinano_skill_2 = {
		901077,
		121,
		True
	},
	launch_ball_shinano_skill_2_desc = {
		901198,
		257,
		True
	},
	launch_ball_yura_skill_1 = {
		901455,
		111,
		True
	},
	launch_ball_yura_skill_1_desc = {
		901566,
		169,
		True
	},
	launch_ball_yura_skill_2 = {
		901735,
		120,
		True
	},
	launch_ball_yura_skill_2_desc = {
		901855,
		206,
		True
	},
	launch_ball_shimakaze_skill_1 = {
		902061,
		124,
		True
	},
	launch_ball_shimakaze_skill_1_desc = {
		902185,
		225,
		True
	},
	launch_ball_shimakaze_skill_2 = {
		902410,
		121,
		True
	},
	launch_ball_shimakaze_skill_2_desc = {
		902531,
		202,
		True
	},
	jp6th_spring_tip1 = {
		902733,
		172,
		True
	},
	jp6th_spring_tip2 = {
		902905,
		104,
		True
	},
	jp6th_biaohoushan_help = {
		903009,
		1312,
		True
	},
	jp6th_lihoushan_help = {
		904321,
		2540,
		True
	},
	jp6th_lihoushan_time = {
		906861,
		125,
		True
	},
	jp6th_lihoushan_order = {
		906986,
		138,
		True
	},
	jp6th_lihoushan_pt1 = {
		907124,
		98,
		True
	},
	launchball_minigame_help = {
		907222,
		357,
		True
	},
	launchball_minigame_select = {
		907579,
		106,
		True
	},
	launchball_minigame_un_select = {
		907685,
		122,
		True
	},
	launchball_minigame_shop = {
		907807,
		106,
		True
	},
	launchball_lock_Shinano = {
		907913,
		172,
		True
	},
	launchball_lock_Yura = {
		908085,
		166,
		True
	},
	launchball_lock_Shimakaze = {
		908251,
		176,
		True
	},
	launchball_spilt_series = {
		908427,
		162,
		True
	},
	launchball_spilt_mix = {
		908589,
		311,
		True
	},
	launchball_spilt_over = {
		908900,
		224,
		True
	},
	launchball_spilt_many = {
		909124,
		152,
		True
	},
	luckybag_skin_isani = {
		909276,
		90,
		True
	},
	luckybag_skin_islive2d = {
		909366,
		93,
		True
	},
	SkinMagazinePage2_tip = {
		909459,
		92,
		True
	},
	racing_cost = {
		909551,
		86,
		True
	},
	racing_rank_top_text = {
		909637,
		98,
		True
	},
	racing_rank_half_h = {
		909735,
		102,
		True
	},
	racing_rank_no_data = {
		909837,
		101,
		True
	},
	racing_minigame_help = {
		909938,
		357,
		True
	},
	child_msg_title_detail = {
		910295,
		93,
		True
	},
	child_msg_title_tip = {
		910388,
		87,
		True
	},
	child_msg_owned = {
		910475,
		88,
		True
	},
	child_polaroid_get_tip = {
		910563,
		135,
		True
	},
	child_close_tip = {
		910698,
		101,
		True
	},
	word_month = {
		910799,
		79,
		True
	},
	word_which_month = {
		910878,
		88,
		True
	},
	word_which_week = {
		910966,
		86,
		True
	},
	word_in_one_week = {
		911052,
		89,
		True
	},
	word_week_title = {
		911141,
		82,
		True
	},
	word_harbour = {
		911223,
		80,
		True
	},
	child_btn_target = {
		911303,
		85,
		True
	},
	child_btn_collect = {
		911388,
		89,
		True
	},
	child_btn_mind = {
		911477,
		86,
		True
	},
	child_btn_bag = {
		911563,
		82,
		True
	},
	child_btn_news = {
		911645,
		90,
		True
	},
	child_main_help = {
		911735,
		526,
		True
	},
	child_archive_name = {
		912261,
		86,
		True
	},
	child_news_import_title = {
		912347,
		99,
		True
	},
	child_news_other_title = {
		912446,
		101,
		True
	},
	child_favor_progress = {
		912547,
		96,
		True
	},
	child_favor_lock1 = {
		912643,
		96,
		True
	},
	child_favor_lock2 = {
		912739,
		96,
		True
	},
	child_target_lock_tip = {
		912835,
		136,
		True
	},
	child_target_progress = {
		912971,
		96,
		True
	},
	child_target_finish_tip = {
		913067,
		117,
		True
	},
	child_target_time_title = {
		913184,
		97,
		True
	},
	child_target_title1 = {
		913281,
		92,
		True
	},
	child_target_title2 = {
		913373,
		94,
		True
	},
	child_item_type0 = {
		913467,
		83,
		True
	},
	child_item_type1 = {
		913550,
		85,
		True
	},
	child_item_type2 = {
		913635,
		91,
		True
	},
	child_item_type3 = {
		913726,
		85,
		True
	},
	child_item_type4 = {
		913811,
		85,
		True
	},
	child_mind_empty_tip = {
		913896,
		124,
		True
	},
	child_mind_finish_title = {
		914020,
		96,
		True
	},
	child_mind_processing_title = {
		914116,
		102,
		True
	},
	child_mind_time_title = {
		914218,
		95,
		True
	},
	child_collect_lock = {
		914313,
		88,
		True
	},
	child_nature_title = {
		914401,
		94,
		True
	},
	child_btn_review = {
		914495,
		87,
		True
	},
	child_schedule_empty_tip = {
		914582,
		132,
		True
	},
	child_schedule_event_tip = {
		914714,
		136,
		True
	},
	child_schedule_sure_tip = {
		914850,
		189,
		True
	},
	child_schedule_sure_tip2 = {
		915039,
		146,
		True
	},
	child_plan_check_tip1 = {
		915185,
		152,
		True
	},
	child_plan_check_tip2 = {
		915337,
		141,
		True
	},
	child_plan_check_tip3 = {
		915478,
		166,
		True
	},
	child_plan_check_tip4 = {
		915644,
		132,
		True
	},
	child_plan_check_tip5 = {
		915776,
		133,
		True
	},
	child_plan_event = {
		915909,
		96,
		True
	},
	child_btn_home = {
		916005,
		85,
		True
	},
	child_option_limit = {
		916090,
		89,
		True
	},
	child_shop_tip1 = {
		916179,
		117,
		True
	},
	child_shop_tip2 = {
		916296,
		112,
		True
	},
	child_filter_title = {
		916408,
		88,
		True
	},
	child_filter_type1 = {
		916496,
		95,
		True
	},
	child_filter_type2 = {
		916591,
		93,
		True
	},
	child_filter_type3 = {
		916684,
		91,
		True
	},
	child_plan_type1 = {
		916775,
		86,
		True
	},
	child_plan_type2 = {
		916861,
		87,
		True
	},
	child_plan_type3 = {
		916948,
		95,
		True
	},
	child_plan_type4 = {
		917043,
		89,
		True
	},
	child_filter_award_res = {
		917132,
		91,
		True
	},
	child_filter_award_nature = {
		917223,
		100,
		True
	},
	child_filter_award_attr1 = {
		917323,
		93,
		True
	},
	child_filter_award_attr2 = {
		917416,
		97,
		True
	},
	child_mood_desc1 = {
		917513,
		149,
		True
	},
	child_mood_desc2 = {
		917662,
		143,
		True
	},
	child_mood_desc3 = {
		917805,
		145,
		True
	},
	child_mood_desc4 = {
		917950,
		145,
		True
	},
	child_mood_desc5 = {
		918095,
		145,
		True
	},
	child_stage_desc1 = {
		918240,
		95,
		True
	},
	child_stage_desc2 = {
		918335,
		95,
		True
	},
	child_stage_desc3 = {
		918430,
		95,
		True
	},
	child_default_callname = {
		918525,
		95,
		True
	},
	flagship_display_mode_1 = {
		918620,
		118,
		True
	},
	flagship_display_mode_2 = {
		918738,
		117,
		True
	},
	flagship_display_mode_3 = {
		918855,
		95,
		True
	},
	flagship_educate_slot_lock_tip = {
		918950,
		199,
		True
	},
	child_story_name = {
		919149,
		89,
		True
	},
	secretary_special_name = {
		919238,
		88,
		True
	},
	secretary_special_lock_tip = {
		919326,
		101,
		True
	},
	secretary_special_title_age = {
		919427,
		109,
		True
	},
	secretary_special_title_physiognomy = {
		919536,
		117,
		True
	},
	child_plan_skip = {
		919653,
		93,
		True
	},
	child_attr_name1 = {
		919746,
		85,
		True
	},
	child_attr_name2 = {
		919831,
		89,
		True
	},
	child_task_system_type2 = {
		919920,
		93,
		True
	},
	child_task_system_type3 = {
		920013,
		91,
		True
	},
	child_plan_perform_title = {
		920104,
		104,
		True
	},
	child_date_text1 = {
		920208,
		93,
		True
	},
	child_date_text2 = {
		920301,
		96,
		True
	},
	child_date_text3 = {
		920397,
		94,
		True
	},
	child_date_text4 = {
		920491,
		93,
		True
	},
	child_upgrade_sure_tip = {
		920584,
		231,
		True
	},
	child_school_sure_tip = {
		920815,
		212,
		True
	},
	child_extraAttr_sure_tip = {
		921027,
		140,
		True
	},
	child_reset_sure_tip = {
		921167,
		172,
		True
	},
	child_end_sure_tip = {
		921339,
		104,
		True
	},
	child_buff_name = {
		921443,
		85,
		True
	},
	child_unlock_tip = {
		921528,
		86,
		True
	},
	child_unlock_out = {
		921614,
		90,
		True
	},
	child_unlock_memory = {
		921704,
		91,
		True
	},
	child_unlock_polaroid = {
		921795,
		92,
		True
	},
	child_unlock_ending = {
		921887,
		90,
		True
	},
	child_unlock_intimacy = {
		921977,
		94,
		True
	},
	child_unlock_buff = {
		922071,
		87,
		True
	},
	child_unlock_attr2 = {
		922158,
		93,
		True
	},
	child_unlock_attr3 = {
		922251,
		91,
		True
	},
	child_unlock_bag = {
		922342,
		85,
		True
	},
	child_shop_empty_tip = {
		922427,
		101,
		True
	},
	child_bag_empty_tip = {
		922528,
		101,
		True
	},
	levelscene_deploy_submarine = {
		922629,
		105,
		True
	},
	levelscene_deploy_submarine_cancel = {
		922734,
		104,
		True
	},
	levelscene_airexpel_cancel = {
		922838,
		96,
		True
	},
	levelscene_airexpel_select_enemy = {
		922934,
		131,
		True
	},
	levelscene_airexpel_outrange = {
		923065,
		137,
		True
	},
	levelscene_airexpel_select_boss = {
		923202,
		141,
		True
	},
	levelscene_airexpel_select_battle = {
		923343,
		154,
		True
	},
	levelscene_airexpel_select_confirm_left = {
		923497,
		204,
		True
	},
	levelscene_airexpel_select_confirm_right = {
		923701,
		206,
		True
	},
	levelscene_airexpel_select_confirm_up = {
		923907,
		193,
		True
	},
	levelscene_airexpel_select_confirm_down = {
		924100,
		197,
		True
	},
	shipyard_phase_1 = {
		924297,
		971,
		True
	},
	shipyard_phase_2 = {
		925268,
		86,
		True
	},
	shipyard_button_1 = {
		925354,
		91,
		True
	},
	shipyard_button_2 = {
		925445,
		153,
		True
	},
	shipyard_introduce = {
		925598,
		212,
		True
	},
	help_supportfleet = {
		925810,
		358,
		True
	},
	word_status_inSupportFleet = {
		926168,
		106,
		True
	},
	ship_formationMediator_request_replace_support = {
		926274,
		203,
		True
	},
	courtyard_label_train = {
		926477,
		90,
		True
	},
	courtyard_label_rest = {
		926567,
		88,
		True
	},
	courtyard_label_capacity = {
		926655,
		96,
		True
	},
	courtyard_label_share = {
		926751,
		90,
		True
	},
	courtyard_label_shop = {
		926841,
		88,
		True
	},
	courtyard_label_decoration = {
		926929,
		94,
		True
	},
	courtyard_label_template = {
		927023,
		94,
		True
	},
	courtyard_label_floor = {
		927117,
		91,
		True
	},
	courtyard_label_exp_addition = {
		927208,
		101,
		True
	},
	courtyard_label_total_exp_addition = {
		927309,
		114,
		True
	},
	courtyard_label_comfortable_addition = {
		927423,
		116,
		True
	},
	courtyard_label_placed_furniture = {
		927539,
		112,
		True
	},
	courtyard_label_shop_1 = {
		927651,
		90,
		True
	},
	courtyard_label_clear = {
		927741,
		90,
		True
	},
	courtyard_label_save = {
		927831,
		88,
		True
	},
	courtyard_label_save_theme = {
		927919,
		100,
		True
	},
	courtyard_label_using = {
		928019,
		103,
		True
	},
	courtyard_label_search_holder = {
		928122,
		105,
		True
	},
	courtyard_label_filter = {
		928227,
		92,
		True
	},
	courtyard_label_time = {
		928319,
		88,
		True
	},
	courtyard_label_week = {
		928407,
		93,
		True
	},
	courtyard_label_month = {
		928500,
		94,
		True
	},
	courtyard_label_year = {
		928594,
		93,
		True
	},
	courtyard_label_putlist_title = {
		928687,
		114,
		True
	},
	courtyard_label_custom_theme = {
		928801,
		102,
		True
	},
	courtyard_label_system_theme = {
		928903,
		99,
		True
	},
	courtyard_tip_furniture_not_in_layer = {
		929002,
		142,
		True
	},
	courtyard_label_detail = {
		929144,
		93,
		True
	},
	courtyard_label_place_pnekey = {
		929237,
		103,
		True
	},
	courtyard_label_delete = {
		929340,
		92,
		True
	},
	courtyard_label_cancel_share = {
		929432,
		104,
		True
	},
	courtyard_label_empty_template_list = {
		929536,
		139,
		True
	},
	courtyard_label_empty_custom_template_list = {
		929675,
		195,
		True
	},
	courtyard_label_empty_collection_list = {
		929870,
		135,
		True
	},
	courtyard_label_go = {
		930005,
		89,
		True
	},
	mot_class_t_level_1 = {
		930094,
		97,
		True
	},
	mot_class_t_level_2 = {
		930191,
		98,
		True
	},
	equip_share_label_1 = {
		930289,
		99,
		True
	},
	equip_share_label_2 = {
		930388,
		100,
		True
	},
	equip_share_label_3 = {
		930488,
		99,
		True
	},
	equip_share_label_4 = {
		930587,
		96,
		True
	},
	equip_share_label_5 = {
		930683,
		95,
		True
	},
	equip_share_label_6 = {
		930778,
		99,
		True
	},
	equip_share_label_7 = {
		930877,
		87,
		True
	},
	equip_share_label_8 = {
		930964,
		90,
		True
	},
	equip_share_label_9 = {
		931054,
		87,
		True
	},
	equipcode_input = {
		931141,
		104,
		True
	},
	equipcode_slot_unmatch = {
		931245,
		153,
		True
	},
	equipcode_share_nolabel = {
		931398,
		132,
		True
	},
	equipcode_share_exceedlimit = {
		931530,
		124,
		True
	},
	equipcode_illegal = {
		931654,
		116,
		True
	},
	equipcode_confirm_doublecheck = {
		931770,
		137,
		True
	},
	equipcode_import_success = {
		931907,
		132,
		True
	},
	equipcode_share_success = {
		932039,
		128,
		True
	},
	equipcode_like_limited = {
		932167,
		138,
		True
	},
	equipcode_like_success = {
		932305,
		102,
		True
	},
	equipcode_dislike_success = {
		932407,
		115,
		True
	},
	equipcode_report_type_1 = {
		932522,
		118,
		True
	},
	equipcode_report_type_2 = {
		932640,
		110,
		True
	},
	equipcode_report_warning = {
		932750,
		150,
		True
	},
	equipcode_level_unmatched = {
		932900,
		100,
		True
	},
	equipcode_equipment_unowned = {
		933000,
		103,
		True
	},
	equipcode_diff_selected = {
		933103,
		101,
		True
	},
	equipcode_export_success = {
		933204,
		105,
		True
	},
	equipcode_unsaved_tips = {
		933309,
		154,
		True
	},
	equipcode_share_ruletips = {
		933463,
		139,
		True
	},
	equipcode_share_errorcode7 = {
		933602,
		146,
		True
	},
	equipcode_share_errorcode44 = {
		933748,
		137,
		True
	},
	equipcode_share_title = {
		933885,
		93,
		True
	},
	equipcode_share_titleeng = {
		933978,
		96,
		True
	},
	equipcode_share_listempty = {
		934074,
		115,
		True
	},
	equipcode_equip_occupied = {
		934189,
		94,
		True
	},
	sail_boat_equip_tip_1 = {
		934283,
		206,
		True
	},
	sail_boat_equip_tip_2 = {
		934489,
		215,
		True
	},
	sail_boat_equip_tip_3 = {
		934704,
		218,
		True
	},
	sail_boat_equip_tip_4 = {
		934922,
		210,
		True
	},
	sail_boat_equip_tip_5 = {
		935132,
		191,
		True
	},
	sail_boat_minigame_help = {
		935323,
		356,
		True
	},
	pirate_wanted_help = {
		935679,
		448,
		True
	},
	harbor_backhill_help = {
		936127,
		1172,
		True
	},
	cryptolalia_download_task_already_exists = {
		937299,
		135,
		True
	},
	charge_scene_buy_confirm_backyard = {
		937434,
		168,
		True
	},
	roll_room1 = {
		937602,
		88,
		True
	},
	roll_room2 = {
		937690,
		88,
		True
	},
	roll_room3 = {
		937778,
		84,
		True
	},
	roll_room4 = {
		937862,
		83,
		True
	},
	roll_room5 = {
		937945,
		85,
		True
	},
	roll_room6 = {
		938030,
		92,
		True
	},
	roll_room7 = {
		938122,
		85,
		True
	},
	roll_room8 = {
		938207,
		81,
		True
	},
	roll_room9 = {
		938288,
		86,
		True
	},
	roll_room10 = {
		938374,
		91,
		True
	},
	roll_room11 = {
		938465,
		89,
		True
	},
	roll_room12 = {
		938554,
		90,
		True
	},
	roll_room13 = {
		938644,
		89,
		True
	},
	roll_room14 = {
		938733,
		87,
		True
	},
	roll_room15 = {
		938820,
		80,
		True
	},
	roll_room16 = {
		938900,
		86,
		True
	},
	roll_room17 = {
		938986,
		81,
		True
	},
	roll_attr_list = {
		939067,
		693,
		True
	},
	roll_notimes = {
		939760,
		142,
		True
	},
	roll_tip2 = {
		939902,
		137,
		True
	},
	roll_reward_word1 = {
		940039,
		89,
		True
	},
	roll_reward_word2 = {
		940128,
		90,
		True
	},
	roll_reward_word3 = {
		940218,
		90,
		True
	},
	roll_reward_word4 = {
		940308,
		90,
		True
	},
	roll_reward_word5 = {
		940398,
		90,
		True
	},
	roll_reward_word6 = {
		940488,
		90,
		True
	},
	roll_reward_word7 = {
		940578,
		90,
		True
	},
	roll_reward_word8 = {
		940668,
		87,
		True
	},
	roll_reward_tip = {
		940755,
		94,
		True
	},
	roll_unlock = {
		940849,
		126,
		True
	},
	roll_noname = {
		940975,
		116,
		True
	},
	roll_card_info = {
		941091,
		85,
		True
	},
	roll_card_attr = {
		941176,
		83,
		True
	},
	roll_card_skill = {
		941259,
		85,
		True
	},
	roll_times_left = {
		941344,
		93,
		True
	},
	roll_room_unexplored = {
		941437,
		87,
		True
	},
	roll_reward_got = {
		941524,
		86,
		True
	},
	roll_gametip = {
		941610,
		1639,
		True
	},
	roll_ending_tip1 = {
		943249,
		157,
		True
	},
	roll_ending_tip2 = {
		943406,
		141,
		True
	},
	commandercat_label_raw_name = {
		943547,
		104,
		True
	},
	commandercat_label_custom_name = {
		943651,
		105,
		True
	},
	commandercat_label_display_name = {
		943756,
		106,
		True
	},
	commander_selected_max = {
		943862,
		127,
		True
	},
	word_talent = {
		943989,
		81,
		True
	},
	word_click_to_close = {
		944070,
		95,
		True
	},
	commander_subtile_ablity = {
		944165,
		104,
		True
	},
	commander_subtile_talent = {
		944269,
		102,
		True
	},
	commander_confirm_tip = {
		944371,
		130,
		True
	},
	commander_level_up_tip = {
		944501,
		122,
		True
	},
	commander_skill_effect = {
		944623,
		99,
		True
	},
	commander_choice_talent_1 = {
		944722,
		127,
		True
	},
	commander_choice_talent_2 = {
		944849,
		106,
		True
	},
	commander_choice_talent_3 = {
		944955,
		132,
		True
	},
	commander_get_box_tip_1 = {
		945087,
		102,
		True
	},
	commander_get_box_tip = {
		945189,
		113,
		True
	},
	commander_total_gold = {
		945302,
		95,
		True
	},
	commander_use_box_tip = {
		945397,
		101,
		True
	},
	commander_use_box_queue = {
		945498,
		95,
		True
	},
	commander_command_ability = {
		945593,
		99,
		True
	},
	commander_logistics_ability = {
		945692,
		100,
		True
	},
	commander_tactical_ability = {
		945792,
		97,
		True
	},
	commander_choice_talent_4 = {
		945889,
		147,
		True
	},
	commander_rename_tip = {
		946036,
		145,
		True
	},
	commander_home_level_label = {
		946181,
		103,
		True
	},
	commander_get_commander_coptyright = {
		946284,
		117,
		True
	},
	commander_choice_talent_reset = {
		946401,
		236,
		True
	},
	commander_lock_setting_title = {
		946637,
		180,
		True
	},
	skin_exchange_confirm = {
		946817,
		162,
		True
	},
	skin_purchase_confirm = {
		946979,
		238,
		True
	},
	blackfriday_pack_lock = {
		947217,
		126,
		True
	},
	skin_exchange_title = {
		947343,
		99,
		True
	},
	blackfriday_pack_select_skinall = {
		947442,
		257,
		True
	},
	skin_discount_desc = {
		947699,
		137,
		True
	},
	skin_exchange_timelimit = {
		947836,
		198,
		True
	},
	blackfriday_pack_purchased = {
		948034,
		99,
		True
	},
	commander_unsel_lock_flag_tip = {
		948133,
		200,
		True
	},
	skin_discount_timelimit = {
		948333,
		175,
		True
	},
	shan_luan_task_progress_tip = {
		948508,
		104,
		True
	},
	shan_luan_task_level_tip = {
		948612,
		104,
		True
	},
	shan_luan_task_help = {
		948716,
		876,
		True
	},
	shan_luan_task_buff_default = {
		949592,
		94,
		True
	},
	senran_pt_consume_tip = {
		949686,
		228,
		True
	},
	senran_pt_not_enough = {
		949914,
		139,
		True
	},
	senran_pt_help = {
		950053,
		595,
		True
	},
	senran_pt_rank = {
		950648,
		101,
		True
	},
	senran_pt_words_feiniao = {
		950749,
		420,
		True
	},
	senran_pt_words_banjiu = {
		951169,
		524,
		True
	},
	senran_pt_words_yan = {
		951693,
		419,
		True
	},
	senran_pt_words_xuequan = {
		952112,
		453,
		True
	},
	senran_pt_words_xuebugui = {
		952565,
		433,
		True
	},
	senran_pt_words_zi = {
		952998,
		394,
		True
	},
	senran_pt_words_xishao = {
		953392,
		392,
		True
	},
	senrankagura_backhill_help = {
		953784,
		1252,
		True
	},
	vote_lable_not_start = {
		955036,
		90,
		True
	},
	vote_lable_voting = {
		955126,
		92,
		True
	},
	vote_lable_title = {
		955218,
		173,
		True
	},
	vote_lable_acc_title_1 = {
		955391,
		97,
		True
	},
	vote_lable_acc_title_2 = {
		955488,
		98,
		True
	},
	vote_lable_curr_title_1 = {
		955586,
		103,
		True
	},
	vote_lable_curr_title_2 = {
		955689,
		104,
		True
	},
	vote_lable_window_title = {
		955793,
		94,
		True
	},
	vote_lable_rearch = {
		955887,
		90,
		True
	},
	vote_lable_daily_task_title = {
		955977,
		98,
		True
	},
	vote_lable_daily_task_tip = {
		956075,
		138,
		True
	},
	vote_lable_task_title = {
		956213,
		96,
		True
	},
	vote_lable_task_list_is_empty = {
		956309,
		124,
		True
	},
	vote_lable_ship_votes = {
		956433,
		95,
		True
	},
	vote_help_2023 = {
		956528,
		5208,
		True
	},
	vote_tip_level_limit = {
		961736,
		139,
		True
	},
	vote_label_rank = {
		961875,
		83,
		True
	},
	vote_label_rank_fresh_time_tip = {
		961958,
		135,
		True
	},
	vote_tip_area_closed = {
		962093,
		102,
		True
	},
	commander_skill_ui_info = {
		962195,
		91,
		True
	},
	commander_skill_ui_confirm = {
		962286,
		97,
		True
	},
	commander_formation_prefab_fleet = {
		962383,
		102,
		True
	},
	rect_ship_card_tpl_add = {
		962485,
		96,
		True
	},
	newyear2024_backhill_help = {
		962581,
		1024,
		True
	},
	last_times_sign = {
		963605,
		100,
		True
	},
	skin_page_sign = {
		963705,
		83,
		True
	},
	skin_page_desc = {
		963788,
		178,
		True
	},
	live2d_reset_desc = {
		963966,
		110,
		True
	},
	skin_exchange_usetip = {
		964076,
		138,
		True
	},
	blackfriday_pack_select_skinall_dialog = {
		964214,
		211,
		True
	},
	not_use_ticket_to_buy_skin = {
		964425,
		113,
		True
	},
	skin_purchase_over_price = {
		964538,
		337,
		True
	},
	help_chunjie2024 = {
		964875,
		1357,
		True
	},
	child_random_polaroid_drop = {
		966232,
		97,
		True
	},
	child_random_ops_drop = {
		966329,
		99,
		True
	},
	child_refresh_sure_tip = {
		966428,
		118,
		True
	},
	child_target_set_sure_tip = {
		966546,
		225,
		True
	},
	child_polaroid_lock_tip = {
		966771,
		128,
		True
	},
	child_task_finish_all = {
		966899,
		115,
		True
	},
	child_unlock_new_secretary = {
		967014,
		197,
		True
	},
	child_no_resource = {
		967211,
		103,
		True
	},
	child_target_set_empty = {
		967314,
		110,
		True
	},
	child_target_set_skip = {
		967424,
		132,
		True
	},
	child_news_import_empty = {
		967556,
		130,
		True
	},
	child_news_other_empty = {
		967686,
		116,
		True
	},
	word_week_day1 = {
		967802,
		84,
		True
	},
	word_week_day2 = {
		967886,
		85,
		True
	},
	word_week_day3 = {
		967971,
		87,
		True
	},
	word_week_day4 = {
		968058,
		86,
		True
	},
	word_week_day5 = {
		968144,
		84,
		True
	},
	word_week_day6 = {
		968228,
		86,
		True
	},
	word_week_day7 = {
		968314,
		84,
		True
	},
	child_shop_price_title = {
		968398,
		92,
		True
	},
	child_callname_tip = {
		968490,
		104,
		True
	},
	child_plan_no_cost = {
		968594,
		93,
		True
	},
	word_emoji_unlock = {
		968687,
		102,
		True
	},
	word_get_emoji = {
		968789,
		86,
		True
	},
	word_show_extra_reward_at_fudai_dialog = {
		968875,
		136,
		True
	},
	skin_shop_buy_confirm = {
		969011,
		166,
		True
	},
	activity_victory = {
		969177,
		106,
		True
	},
	other_world_temple_toggle_1 = {
		969283,
		106,
		True
	},
	other_world_temple_toggle_2 = {
		969389,
		108,
		True
	},
	other_world_temple_toggle_3 = {
		969497,
		107,
		True
	},
	other_world_temple_char = {
		969604,
		96,
		True
	},
	other_world_temple_award = {
		969700,
		101,
		True
	},
	other_world_temple_got = {
		969801,
		93,
		True
	},
	other_world_temple_progress = {
		969894,
		136,
		True
	},
	other_world_temple_char_title = {
		970030,
		102,
		True
	},
	other_world_temple_award_last = {
		970132,
		108,
		True
	},
	other_world_temple_award_title_1 = {
		970240,
		122,
		True
	},
	other_world_temple_award_title_2 = {
		970362,
		124,
		True
	},
	other_world_temple_award_title_3 = {
		970486,
		123,
		True
	},
	other_world_temple_lottery_all = {
		970609,
		123,
		True
	},
	other_world_temple_award_desc = {
		970732,
		163,
		True
	},
	temple_consume_not_enough = {
		970895,
		111,
		True
	},
	other_world_temple_pay = {
		971006,
		101,
		True
	},
	other_world_task_type_daily = {
		971107,
		96,
		True
	},
	other_world_task_type_main = {
		971203,
		94,
		True
	},
	other_world_task_type_repeat = {
		971297,
		106,
		True
	},
	other_world_task_title = {
		971403,
		100,
		True
	},
	other_world_task_get_all = {
		971503,
		97,
		True
	},
	other_world_task_go = {
		971600,
		90,
		True
	},
	other_world_task_got = {
		971690,
		91,
		True
	},
	other_world_task_get = {
		971781,
		89,
		True
	},
	other_world_task_tag_main = {
		971870,
		93,
		True
	},
	other_world_task_tag_daily = {
		971963,
		95,
		True
	},
	other_world_task_tag_all = {
		972058,
		91,
		True
	},
	terminal_personal_title = {
		972149,
		101,
		True
	},
	terminal_adventure_title = {
		972250,
		102,
		True
	},
	terminal_guardian_title = {
		972352,
		96,
		True
	},
	personal_info_title = {
		972448,
		93,
		True
	},
	personal_property_title = {
		972541,
		92,
		True
	},
	personal_ability_title = {
		972633,
		92,
		True
	},
	adventure_award_title = {
		972725,
		108,
		True
	},
	adventure_progress_title = {
		972833,
		102,
		True
	},
	adventure_lv_title = {
		972935,
		99,
		True
	},
	adventure_record_title = {
		973034,
		99,
		True
	},
	adventure_record_grade_title = {
		973133,
		108,
		True
	},
	adventure_award_end_tip = {
		973241,
		125,
		True
	},
	guardian_select_title = {
		973366,
		100,
		True
	},
	guardian_sure_btn = {
		973466,
		85,
		True
	},
	guardian_cancel_btn = {
		973551,
		89,
		True
	},
	guardian_active_tip = {
		973640,
		89,
		True
	},
	personal_random = {
		973729,
		94,
		True
	},
	adventure_get_all = {
		973823,
		90,
		True
	},
	Announcements_Event_Notice = {
		973913,
		95,
		True
	},
	Announcements_System_Notice = {
		974008,
		97,
		True
	},
	Announcements_News = {
		974105,
		86,
		True
	},
	Announcements_Donotshow = {
		974191,
		109,
		True
	},
	adventure_unlock_tip = {
		974300,
		170,
		True
	},
	personal_random_tip = {
		974470,
		139,
		True
	},
	guardian_sure_limit_tip = {
		974609,
		123,
		True
	},
	other_world_temple_tip = {
		974732,
		533,
		True
	},
	otherworld_map_help = {
		975265,
		530,
		True
	},
	otherworld_backhill_help = {
		975795,
		535,
		True
	},
	otherworld_terminal_help = {
		976330,
		535,
		True
	},
	vote_2023_reward_word_1 = {
		976865,
		207,
		True
	},
	vote_2023_reward_word_2 = {
		977072,
		357,
		True
	},
	vote_2023_reward_word_3 = {
		977429,
		354,
		True
	},
	voting_page_reward = {
		977783,
		87,
		True
	},
	backyard_shipAddInimacy_ships_ok = {
		977870,
		177,
		True
	},
	backyard_shipAddMoney_ships_ok = {
		978047,
		201,
		True
	},
	idol3rd_houshan = {
		978248,
		1145,
		True
	},
	idol3rd_collection = {
		979393,
		800,
		True
	},
	idol3rd_practice = {
		980193,
		944,
		True
	},
	main_silent_tip_1 = {
		981137,
		109,
		True
	},
	main_silent_tip_2 = {
		981246,
		110,
		True
	},
	main_silent_tip_3 = {
		981356,
		110,
		True
	},
	main_silent_tip_4 = {
		981466,
		115,
		True
	},
	commission_label_go = {
		981581,
		90,
		True
	},
	commission_label_finish = {
		981671,
		95,
		True
	},
	commission_label_go_mellow = {
		981766,
		97,
		True
	},
	commission_label_finish_mellow = {
		981863,
		102,
		True
	},
	commission_label_unlock_event_tip = {
		981965,
		126,
		True
	},
	commission_label_unlock_tech_tip = {
		982091,
		125,
		True
	},
	specialshipyard_tip = {
		982216,
		165,
		True
	},
	specialshipyard_name = {
		982381,
		97,
		True
	},
	liner_sign_cnt_tip = {
		982478,
		103,
		True
	},
	liner_sign_unlock_tip = {
		982581,
		100,
		True
	},
	liner_target_type1 = {
		982681,
		93,
		True
	},
	liner_target_type2 = {
		982774,
		91,
		True
	},
	liner_target_type3 = {
		982865,
		98,
		True
	},
	liner_target_type4 = {
		982963,
		97,
		True
	},
	liner_target_type5 = {
		983060,
		112,
		True
	},
	liner_log_schedule_title = {
		983172,
		103,
		True
	},
	liner_log_room_title = {
		983275,
		109,
		True
	},
	liner_log_event_title = {
		983384,
		101,
		True
	},
	liner_schedule_award_tip1 = {
		983485,
		113,
		True
	},
	liner_schedule_award_tip2 = {
		983598,
		113,
		True
	},
	liner_room_award_tip = {
		983711,
		109,
		True
	},
	liner_event_award_tip1 = {
		983820,
		152,
		True
	},
	liner_log_event_group_title1 = {
		983972,
		102,
		True
	},
	liner_log_event_group_title2 = {
		984074,
		102,
		True
	},
	liner_log_event_group_title3 = {
		984176,
		102,
		True
	},
	liner_log_event_group_title4 = {
		984278,
		102,
		True
	},
	liner_event_award_tip2 = {
		984380,
		115,
		True
	},
	liner_event_reasoning_title = {
		984495,
		107,
		True
	},
	["7th_main_tip"] = {
		984602,
		850,
		True
	},
	pipe_minigame_help = {
		985452,
		294,
		True
	},
	pipe_minigame_rank = {
		985746,
		114,
		True
	},
	liner_event_award_tip3 = {
		985860,
		128,
		True
	},
	liner_room_get_tip = {
		985988,
		110,
		True
	},
	liner_event_get_tip = {
		986098,
		101,
		True
	},
	liner_event_lock = {
		986199,
		132,
		True
	},
	liner_event_title1 = {
		986331,
		88,
		True
	},
	liner_event_title2 = {
		986419,
		88,
		True
	},
	liner_event_title3 = {
		986507,
		88,
		True
	},
	liner_help = {
		986595,
		282,
		True
	},
	liner_activity_lock = {
		986877,
		135,
		True
	},
	liner_name_modify = {
		987012,
		122,
		True
	},
	UrExchange_Pt_NotEnough = {
		987134,
		125,
		True
	},
	UrExchange_Pt_charges = {
		987259,
		105,
		True
	},
	UrExchange_Pt_help = {
		987364,
		335,
		True
	},
	xiaodadi_npc = {
		987699,
		1503,
		True
	}
}
