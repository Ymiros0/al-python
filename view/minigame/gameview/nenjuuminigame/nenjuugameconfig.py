local var_0_0 = {
	BLACK_HOLE_RANGE = 2,
	DECOY_RANGE = 5,
	TIME_INTERVAL = 0.016666666666666666,
	LANTERN_RANGE = 3,
	STAGE_CONFIG = {
		BASE_CONFIG = {
			base_rate = 1,
			wave = {
				{
					"Item_1",
					5,
					10
				},
				{
					"Item_2",
					5,
					20
				},
				{
					"Item_3",
					5,
					30
				},
				{
					"Item_4",
					5,
					40
				}
			},
			extra_time = {
				120,
				1000
			},
			ability_rate = {
				gravity = 0.5,
				teleport = 0.5,
				rush = 0.5,
				doppelgangers = 0.5,
				delay = 0.5,
				blackhole = 0.5,
				stealth = 0.5,
				breakpassable = 0.5
			},
			ability_config = {
				gravity = True,
				teleport = True,
				rush = True,
				doppelgangers = True,
				delay = True,
				blackhole = True,
				stealth = True,
				breakpassable = True
			}
		},
		Spring23Level_1 = {
			base_rate = 1,
			wave = {
				{
					"Item_1",
					30,
					10
				},
				{
					"Item_2",
					40,
					10
				}
			},
			extra_time = {
				120,
				300
			},
			ability_rate = {
				blackhole = 0.5,
				teleport = 0.5,
				rush = 0.5
			},
			ability_config = {
				blackhole = True,
				teleport = True,
				rush = True
			}
		},
		Spring23Level_2 = {
			base_rate = 1,
			wave = {
				{
					"Item_3",
					20,
					20
				},
				{
					"Item_4",
					30,
					20
				}
			},
			extra_time = {
				120,
				300
			},
			ability_rate = {
				blackhole = 0.5,
				teleport = 0.5,
				rush = 0.5,
				breakpassable = 0.5
			},
			ability_config = {
				blackhole = True,
				teleport = True,
				rush = True,
				breakpassable = True
			}
		},
		Spring23Level_3 = {
			base_rate = 1,
			wave = {
				{
					"Item_6",
					30,
					20
				},
				{
					"Item_5",
					30,
					20
				}
			},
			extra_time = {
				150,
				500
			},
			ability_rate = {
				blackhole = 0.5,
				teleport = 0.5,
				rush = 0.5,
				doppelgangers = 0.5,
				breakpassable = 0.5
			},
			ability_config = {
				blackhole = True,
				teleport = True,
				rush = True,
				doppelgangers = True,
				breakpassable = True
			}
		},
		Spring23Level_4 = {
			base_rate = 1,
			wave = {
				{
					"Item_1",
					30,
					20
				},
				{
					"Item_3",
					30,
					30
				}
			},
			extra_time = {
				150,
				500
			},
			ability_rate = {
				blackhole = 0.5,
				teleport = 0.5,
				rush = 0.5,
				doppelgangers = 0.5,
				delay = 0.5,
				breakpassable = 0.5
			},
			ability_config = {
				blackhole = True,
				teleport = True,
				rush = True,
				doppelgangers = True,
				delay = True,
				breakpassable = True
			}
		},
		Spring23Level_5 = {
			base_rate = 1,
			wave = {
				{
					"Item_2",
					20,
					40
				},
				{
					"Item_4",
					20,
					40
				}
			},
			extra_time = {
				150,
				500
			},
			ability_rate = {
				blackhole = 0.5,
				teleport = 0.5,
				rush = 0.5,
				doppelgangers = 0.5,
				delay = 0.5,
				stealth = 0.5,
				breakpassable = 0.5
			},
			ability_config = {
				blackhole = True,
				teleport = True,
				rush = True,
				doppelgangers = True,
				delay = True,
				stealth = True,
				breakpassable = True
			}
		},
		Spring23Level_6 = {
			base_rate = 1,
			wave = {
				{
					"Item_1",
					30,
					30
				},
				{
					"Item_3",
					30,
					40
				}
			},
			extra_time = {
				150,
				600
			},
			ability_rate = {
				blackhole = 0.5,
				teleport = 0.5,
				rush = 0.5,
				doppelgangers = 0.5,
				delay = 0.5,
				stealth = 0.5,
				gravity = 0.5,
				breakpassable = 0.5
			},
			ability_config = {
				blackhole = True,
				teleport = True,
				rush = True,
				doppelgangers = True,
				delay = True,
				stealth = True,
				gravity = True,
				breakpassable = True
			}
		},
		Spring23Level_7 = {
			base_rate = 1,
			wave = {
				{
					"Item_1",
					5,
					70
				},
				{
					"Item_2",
					5,
					70
				},
				{
					"Item_3",
					5,
					70
				},
				{
					"Item_4",
					5,
					70
				},
				{
					"Item_6",
					5,
					70
				},
				{
					"Item_5",
					5,
					70
				}
			},
			extra_time = {
				120,
				700
			},
			ability_rate = {
				blackhole = 0.5,
				teleport = 0.5,
				rush = 0.5,
				doppelgangers = 0.5,
				delay = 0.5,
				stealth = 0.5,
				gravity = 0.5,
				breakpassable = 0.5
			},
			ability_config = {
				blackhole = True,
				teleport = True,
				rush = True,
				doppelgangers = True,
				delay = True,
				stealth = True,
				gravity = True,
				breakpassable = True
			}
		}
	}
}

def var_0_0.GetStageConfig(arg_1_0):
	return setmetatable(var_0_0.STAGE_CONFIG[arg_1_0] or {}, {
		__index = var_0_0.STAGE_CONFIG.BASE_CONFIG
	})

def var_0_0.GetCreateConfig(arg_2_0):
	local var_2_0 = {}

	switch(arg_2_0.name, {
		def FuShun:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetFuShun)
			table.insert(var_2_0, "character/FuShun")
			table.insert(var_2_0, "character"),
		def Nenjuu:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetNenjuu)
			table.insert(var_2_0, "character/Nenjuu")
			table.insert(var_2_0, "character"),
		def Nenjuu_Doppelgangers:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetNenjuu)
			table.insert(var_2_0, "character/Nenjuu_Doppelgangers")
			table.insert(var_2_0, "character"),
		def Ice:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetIce)
			table.insert(var_2_0, "object/Ice")
			table.insert(var_2_0, "object"),
		def Bomb:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetBomb)
			table.insert(var_2_0, "effect/Bomb")
			table.insert(var_2_0, "object"),
		def SignWarp:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetTimeEffect)
			table.insert(var_2_0, "effect/SignWarp")
			table.insert(var_2_0, "effect"),
		def Rock:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetObject)
			table.insert(var_2_0, "object/Rock")
			table.insert(var_2_0, "object"),
		def BlackHole:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetBlackHole)
			table.insert(var_2_0, "object/BlackHole")
			table.insert(var_2_0, "object"),
		def Decoy:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetEffect)
			table.insert(var_2_0, "effect/Decoy")
			table.insert(var_2_0, "effect"),
		def EF_bk_Flash_Jump:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetEffect)
			table.insert(var_2_0, "effect/EF_bk_Flash_Jump")
			table.insert(var_2_0, "effect"),
		def EF_bk_Flash_Land:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetSubEffect)
			table.insert(var_2_0, "effect/EF_bk_Flash_Land")
			table.insert(var_2_0, "effect"),
		def EF_Break_E:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetEffect)
			table.insert(var_2_0, "effect/EF_Break_E")
			table.insert(var_2_0, "effect"),
		def EF_Break_N:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetEffect)
			table.insert(var_2_0, "effect/EF_Break_N")
			table.insert(var_2_0, "effect"),
		def EF_Break_S:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetEffect)
			table.insert(var_2_0, "effect/EF_Break_S")
			table.insert(var_2_0, "effect"),
		def EF_Break_W:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetEffect)
			table.insert(var_2_0, "effect/EF_Break_W")
			table.insert(var_2_0, "effect"),
		def EF_Attack_E:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetSubEffect)
			table.insert(var_2_0, "effect/EF_Attack_E")
			table.insert(var_2_0, "effect"),
		def EF_Attack_S:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetSubEffect)
			table.insert(var_2_0, "effect/EF_Attack_S")
			table.insert(var_2_0, "effect"),
		def EF_Attack_N:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetSubEffect)
			table.insert(var_2_0, "effect/EF_Attack_N")
			table.insert(var_2_0, "effect"),
		def EF_Attack_W:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetSubEffect)
			table.insert(var_2_0, "effect/EF_Attack_W")
			table.insert(var_2_0, "effect"),
		def EF_Attack_Hit_W_bk:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetSubEffect)
			table.insert(var_2_0, "effect/EF_Attack_Hit_W_bk")
			table.insert(var_2_0, "effect"),
		def EF_Attack_Hit_W_fr:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetSubEffect)
			table.insert(var_2_0, "effect/EF_Attack_Hit_W_fr")
			table.insert(var_2_0, "effect"),
		def EF_Attack_Hit_E_bk:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetSubEffect)
			table.insert(var_2_0, "effect/EF_Attack_Hit_E_bk")
			table.insert(var_2_0, "effect"),
		def EF_Attack_Hit_E_fr:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetSubEffect)
			table.insert(var_2_0, "effect/EF_Attack_Hit_E_fr")
			table.insert(var_2_0, "effect"),
		def EF_Attack_Hit_N:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetSubEffect)
			table.insert(var_2_0, "effect/EF_Attack_Hit_N")
			table.insert(var_2_0, "effect"),
		def EF_Attack_Hit_S:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetSubEffect)
			table.insert(var_2_0, "effect/EF_Attack_Hit_S")
			table.insert(var_2_0, "effect"),
		def EF_bk_Freeze:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetSubEffect)
			table.insert(var_2_0, "effect/EF_bk_Freeze")
			table.insert(var_2_0, "effect"),
		def EF_bk_overlay_Lantern:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetSubEffect)
			table.insert(var_2_0, "effect/EF_bk_overlay_Lantern")
			table.insert(var_2_0, "effect"),
		def Lamp_A:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetObject)
			table.insert(var_2_0, "object/Lamp_A")
			table.insert(var_2_0, "object")

			arg_2_0.hide = True,
		def Pine:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetObject)
			table.insert(var_2_0, "object/Pine")
			table.insert(var_2_0, "object")

			arg_2_0.size = NewPos(2, 2),
		def Plum:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetObject)
			table.insert(var_2_0, "object/Plum")
			table.insert(var_2_0, "object")

			arg_2_0.size = NewPos(2, 2),
		def Pond:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetObject)
			table.insert(var_2_0, "object/Pond")
			table.insert(var_2_0, "object")

			arg_2_0.size = NewPos(2, 2),
		def Manjuu_fishing:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetObject)
			table.insert(var_2_0, "object/Manjuu_fishing")
			table.insert(var_2_0, "object")

			arg_2_0.size = NewPos(2, 2),
		def Fire:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetObject)
			table.insert(var_2_0, "object/Fire")
			table.insert(var_2_0, "object")

			arg_2_0.size = NewPos(3, 3),
		def Building_A:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetObject)
			table.insert(var_2_0, "object/Building_A")
			table.insert(var_2_0, "object")

			arg_2_0.size = NewPos(3, 3)
			arg_2_0.hide = True,
		def Item_1:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetItem)
			table.insert(var_2_0, "object/Item")
			table.insert(var_2_0, "object"),
		def Item_2:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetItem)
			table.insert(var_2_0, "object/Item")
			table.insert(var_2_0, "object"),
		def Item_3:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetItem)
			table.insert(var_2_0, "object/Item")
			table.insert(var_2_0, "object"),
		def Item_4:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetItem)
			table.insert(var_2_0, "object/Item")
			table.insert(var_2_0, "object"),
		def Item_5:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetItem)
			table.insert(var_2_0, "object/Item")
			table.insert(var_2_0, "object"),
		def Item_6:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetItem)
			table.insert(var_2_0, "object/Item")
			table.insert(var_2_0, "object"),
		def EF_fr_Inactivate:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetSubEffect)
			table.insert(var_2_0, "effect/EF_fr_Inactivate")
			table.insert(var_2_0, "object"),
		def EF_Ghost_E_bk:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetRushEffect)
			table.insert(var_2_0, "effect/EF_Ghost_E_bk")
			table.insert(var_2_0, "effect"),
		def EF_Ghost_N_bk:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetRushEffect)
			table.insert(var_2_0, "effect/EF_Ghost_N_bk")
			table.insert(var_2_0, "effect"),
		def EF_Ghost_N_fr:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetRushEffect)
			table.insert(var_2_0, "effect/EF_Ghost_N_fr")
			table.insert(var_2_0, "effect"),
		def EF_Ghost_S_bk:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetRushEffect)
			table.insert(var_2_0, "effect/EF_Ghost_S_bk")
			table.insert(var_2_0, "effect"),
		def EF_Ghost_W_bk:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetRushEffect)
			table.insert(var_2_0, "effect/EF_Ghost_W_bk")
			table.insert(var_2_0, "effect"),
		def EF_Nenjuu_Ghost_E_bk:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetRushEffect)
			table.insert(var_2_0, "effect/EF_Nenjuu_Ghost_E_bk")
			table.insert(var_2_0, "effect"),
		def EF_Nenjuu_Ghost_N_bk:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetRushEffect)
			table.insert(var_2_0, "effect/EF_Nenjuu_Ghost_N_bk")
			table.insert(var_2_0, "effect"),
		def EF_Nenjuu_Ghost_N_fr:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetRushEffect)
			table.insert(var_2_0, "effect/EF_Nenjuu_Ghost_N_fr")
			table.insert(var_2_0, "effect"),
		def EF_Nenjuu_Ghost_S_bk:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetRushEffect)
			table.insert(var_2_0, "effect/EF_Nenjuu_Ghost_S_bk")
			table.insert(var_2_0, "effect"),
		def EF_Nenjuu_Ghost_W_bk:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetRushEffect)
			table.insert(var_2_0, "effect/EF_Nenjuu_Ghost_W_bk")
			table.insert(var_2_0, "effect"),
		def Snow_1:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetObject)
			table.insert(var_2_0, "object/Snow_1")
			table.insert(var_2_0, "object"),
		def Snow_2:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetObject)
			table.insert(var_2_0, "object/Snow_2")
			table.insert(var_2_0, "object"),
		def Snow_3:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetObject)
			table.insert(var_2_0, "object/Snow_3")
			table.insert(var_2_0, "object"),
		def Snow_4:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetObject)
			table.insert(var_2_0, "object/Snow_4")
			table.insert(var_2_0, "object"),
		def Snow_5:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetObject)
			table.insert(var_2_0, "object/Snow_5")
			table.insert(var_2_0, "object")

			arg_2_0.size = NewPos(2, 1)
			arg_2_0.hide = True,
		def Lamp_B1:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetObject)
			table.insert(var_2_0, "object/Lamp_B1")
			table.insert(var_2_0, "object")

			arg_2_0.hide = True,
		def Lamp_B2:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetObject)
			table.insert(var_2_0, "object/Lamp_B2")
			table.insert(var_2_0, "object")

			arg_2_0.hide = True,
		def Building_B:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetObject)
			table.insert(var_2_0, "object/Building_B")
			table.insert(var_2_0, "object")

			arg_2_0.size = NewPos(4, 3)
			arg_2_0.hide = True,
		["1_Arbor_1"] = function()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetArbor)
			table.insert(var_2_0, "object/Arbor")
			table.insert(var_2_0, "object")

			arg_2_0.size = NewPos(2, 2)
			arg_2_0.hide = True,
		["1_Arbor_2"] = function()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetArbor)
			table.insert(var_2_0, "object/Arbor")
			table.insert(var_2_0, "object")

			arg_2_0.size = NewPos(2, 2)
			arg_2_0.hide = True,
		["1_Arbor_3"] = function()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetArbor)
			table.insert(var_2_0, "object/Arbor")
			table.insert(var_2_0, "object")

			arg_2_0.size = NewPos(2, 2)
			arg_2_0.hide = True,
		["1_Arbor_4"] = function()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetArbor)
			table.insert(var_2_0, "object/Arbor")
			table.insert(var_2_0, "object")

			arg_2_0.size = NewPos(2, 2)
			arg_2_0.hide = True,
		def Dango_1:()
			table.insert(var_2_0, NenjuuGameNameSpace.TargetObject)
			table.insert(var_2_0, "object/Dango")
			table.insert(var_2_0, "object")
	}, function()
		warning("name error." .. arg_2_0.name)
		table.insert(var_2_0, False))

	return unpack(var_2_0)

var_0_0.SKILL_LEVEL_CONFIG = {
	ice = {
		level = 1,
		cost = {
			0,
			1000,
			1000
		},
		param = {
			7,
			9,
			11
		}
	},
	flash = {
		level = 0,
		cost = {
			2000,
			2000,
			2000
		},
		param = {
			30,
			25,
			20
		}
	},
	rush = {
		level = 0,
		cost = {
			2000,
			2000,
			2000
		},
		param = {
			{
				5,
				1.2
			},
			{
				5,
				1.3
			},
			{
				7,
				1.3
			}
		}
	},
	blessing = {
		level = 0,
		cost = {
			2000,
			1000,
			1000
		},
		param = {
			1.03,
			1.06,
			1.1
		}
	},
	decoy = {
		level = 0,
		cost = {
			5000
		}
	},
	bomb = {
		level = 0,
		cost = {
			1000
		}
	},
	lantern = {
		level = 0,
		cost = {
			1000
		}
	}
}

def var_0_0.GetSkillParam(arg_68_0, arg_68_1):
	return var_0_0.SKILL_LEVEL_CONFIG[arg_68_0].param[arg_68_1]

var_0_0.ITEM_LIST = {
	"bomb",
	"lantern"
}

def var_0_0.ParsingElements(arg_69_0):
	local var_69_0 = {
		high = arg_69_0[1] or 0,
		count = arg_69_0[2] or 0,
		item = arg_69_0[3] and var_0_0.ITEM_LIST[arg_69_0[3]] or None
	}

	for iter_69_0 = 1, 7:
		var_69_0["stage_" .. iter_69_0] = arg_69_0[iter_69_0 + 3] or 0

	var_69_0.level = {}

	for iter_69_1, iter_69_2 in ipairs({
		"bomb",
		"lantern",
		"ice",
		"flash",
		"rush",
		"blessing",
		"decoy"
	}):
		var_69_0.level[iter_69_2] = arg_69_0[iter_69_1 + 10] or var_0_0.SKILL_LEVEL_CONFIG[iter_69_2].level

	return var_69_0

var_0_0.ABILITY_LIST = {
	"teleport",
	"rush",
	"breakpassable",
	"gravity",
	"doppelgangers",
	"delay",
	"blackhole",
	"stealth"
}

return var_0_0
