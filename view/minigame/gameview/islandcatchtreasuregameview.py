local var_0_0 = class("IslandCatchTreasureGameView", import("..BaseMiniGameView"))
local var_0_1 = "blueocean-image"
local var_0_2 = "event./ui/ddldaoshu2"
local var_0_3 = "event./ui/taosheng"
local var_0_4 = "event./ui/zhuahuo"
local var_0_5 = "event./ui/deshou"
local var_0_6 = "event./ui/shibai"
local var_0_7 = 60
local var_0_8 = "ui/islandcatchtreasuregameui_atlas"
local var_0_9 = "salvage_tips"
local var_0_10 = "event item:ne"
local var_0_11 = "boat state stand"
local var_0_12 = "boat state thorw"
local var_0_13 = "boat state wait"
local var_0_14 = "item act static"
local var_0_15 = "item act dynamic"
local var_0_16 = "item catch normal"
local var_0_17 = "item catch release"
local var_0_18 = "item catch unable"
local var_0_19 = "item good happy"
local var_0_20 = "item good surprise"
local var_0_21 = "item good release"
local var_0_22 = "item good none"
local var_0_23 = "item scene back"
local var_0_24 = "item scene middle"
local var_0_25 = "item scene front"
local var_0_26 = "item type fish"
local var_0_27 = "item type submarine"
local var_0_28 = "item type goods"
local var_0_29 = "item type sundries"
local var_0_30 = "item type time"
local var_0_31 = "item type back"
local var_0_32 = "item type bind"
local var_0_33 = "item type name "
local var_0_34 = {
	{
		type = var_0_14,
		range = {
			5,
			8
		}
	},
	{
		type = var_0_15,
		range = {
			5,
			8
		}
	}
}
local var_0_35 = {
	{
		{
			repeated = True,
			type = var_0_31,
			amount = {
				8,
				10
			}
		},
		{
			repeated = True,
			type = var_0_28,
			amount = {
				6,
				6
			},
			name = {
				"treasure",
				"gold"
			}
		},
		{
			repeated = True,
			type = var_0_28,
			amount = {
				2,
				2
			},
			name = {
				"rock"
			}
		},
		{
			repeated = True,
			type = var_0_28,
			amount = {
				4,
				4
			},
			name = {
				"shell"
			}
		},
		{
			repeated = True,
			type = var_0_29,
			amount = {
				3,
				3
			}
		},
		{
			repeated = True,
			type = var_0_30,
			amount = {
				2,
				2
			}
		},
		{
			repeated = True,
			type = var_0_26,
			amount = {
				2,
				2
			},
			name = {
				"fish_1",
				"fish_2",
				"fish_3",
				"fish_4"
			}
		},
		{
			repeated = True,
			type = var_0_26,
			amount = {
				1,
				1
			},
			name = {
				"turtle"
			}
		},
		{
			repeated = False,
			type = var_0_27,
			amount = {
				1,
				1
			},
			name = {
				"submarine_1"
			}
		},
		{
			repeated = False,
			type = var_0_27,
			amount = {
				0,
				0
			},
			name = {
				"submarine_2"
			}
		},
		{
			repeated = False,
			type = var_0_27,
			amount = {
				0,
				0
			},
			name = {
				"submarine_3"
			}
		},
		{
			repeated = False,
			type = var_0_27,
			amount = {
				1,
				1
			},
			name = {
				"submarine_4"
			}
		}
	},
	{
		{
			repeated = True,
			type = var_0_31,
			amount = {
				8,
				10
			}
		},
		{
			repeated = True,
			type = var_0_28,
			amount = {
				2,
				2
			},
			name = {
				"treasure",
				"gold",
				"shell"
			}
		},
		{
			repeated = True,
			type = var_0_28,
			amount = {
				0,
				0
			},
			name = {
				"rock"
			}
		},
		{
			repeated = True,
			type = var_0_29,
			amount = {
				0,
				0
			}
		},
		{
			repeated = True,
			type = var_0_30,
			amount = {
				2,
				2
			}
		},
		{
			repeated = True,
			type = var_0_26,
			amount = {
				2,
				2
			},
			name = {
				"fish_1",
				"fish_4"
			}
		},
		{
			repeated = True,
			type = var_0_26,
			amount = {
				3,
				3
			},
			name = {
				"fish_2"
			}
		},
		{
			repeated = True,
			type = var_0_26,
			amount = {
				6,
				6
			},
			name = {
				"fish_3"
			}
		},
		{
			repeated = True,
			type = var_0_26,
			amount = {
				5,
				5
			},
			name = {
				"turtle"
			}
		},
		{
			repeated = False,
			type = var_0_27,
			amount = {
				0,
				0
			},
			name = {
				"submarine_1"
			}
		},
		{
			repeated = False,
			type = var_0_27,
			amount = {
				1,
				1
			},
			name = {
				"submarine_2"
			}
		},
		{
			repeated = False,
			type = var_0_27,
			amount = {
				1,
				1
			},
			name = {
				"submarine_3"
			}
		},
		{
			repeated = False,
			type = var_0_27,
			amount = {
				0,
				0
			},
			name = {
				"submarine_4"
			}
		}
	},
	{
		{
			repeated = True,
			type = var_0_31,
			amount = {
				8,
				10
			}
		},
		{
			repeated = True,
			type = var_0_28,
			amount = {
				2,
				2
			},
			name = {
				"treasure"
			}
		},
		{
			repeated = True,
			type = var_0_28,
			amount = {
				1,
				1
			},
			name = {
				"rock"
			}
		},
		{
			repeated = True,
			type = var_0_28,
			amount = {
				2,
				2
			},
			name = {
				"gold"
			}
		},
		{
			repeated = True,
			type = var_0_28,
			amount = {
				2,
				2
			},
			name = {
				"shell"
			}
		},
		{
			repeated = True,
			type = var_0_29,
			amount = {
				1,
				1
			}
		},
		{
			repeated = True,
			type = var_0_30,
			amount = {
				2,
				2
			}
		},
		{
			repeated = True,
			type = var_0_26,
			amount = {
				2,
				2
			},
			name = {
				"fish_1",
				"fish_4"
			}
		},
		{
			repeated = True,
			type = var_0_26,
			amount = {
				2,
				2
			},
			name = {
				"fish_2"
			}
		},
		{
			repeated = True,
			type = var_0_26,
			amount = {
				3,
				3
			},
			name = {
				"fish_3"
			}
		},
		{
			repeated = True,
			type = var_0_26,
			amount = {
				2,
				2
			},
			name = {
				"turtle"
			}
		},
		{
			repeated = False,
			type = var_0_27,
			amount = {
				3,
				3
			},
			name = {
				"submarine_1",
				"submarine_2",
				"submarine_3",
				"submarine_4"
			}
		}
	}
}
local var_0_36 = {
	{
		score = 200,
		name = "fish_1",
		catch_speed = 130,
		speed = 150,
		release_speed = 200,
		type = var_0_26,
		act = var_0_15,
		catch = var_0_17,
		create_range = {
			0,
			9999,
			130,
			260
		},
		move_range = {
			-300,
			1800,
			0,
			0
		},
		good = var_0_21
	},
	{
		score = 250,
		name = "fish_2",
		catch_speed = 75,
		speed = 100,
		leave_direct = -1,
		release_speed = 200,
		type = var_0_26,
		act = var_0_15,
		catch = var_0_17,
		create_range = {
			0,
			9999,
			130,
			260
		},
		move_range = {
			-300,
			1800,
			0,
			0
		},
		good = var_0_20
	},
	{
		score = 400,
		name = "fish_3",
		catch_speed = 220,
		speed = 350,
		release_speed = 300,
		type = var_0_26,
		act = var_0_15,
		catch = var_0_17,
		create_range = {
			0,
			9999,
			130,
			260
		},
		move_range = {
			-300,
			1800,
			0,
			0
		},
		good = var_0_21
	},
	{
		score = 150,
		name = "fish_4",
		catch_speed = 160,
		speed = 120,
		release_speed = 200,
		type = var_0_26,
		act = var_0_15,
		catch = var_0_17,
		create_range = {
			0,
			9999,
			130,
			260
		},
		move_range = {
			-300,
			1800,
			0,
			0
		},
		good = var_0_21
	},
	{
		score = 180,
		name = "turtle",
		catch_speed = 100,
		speed = 80,
		release_speed = 100,
		type = var_0_26,
		act = var_0_15,
		catch = var_0_17,
		create_range = {
			0,
			9999,
			130,
			260
		},
		move_range = {
			-300,
			1800,
			0,
			0
		},
		good = var_0_21
	},
	{
		score = -150,
		name = "submarine_1",
		speed = 200,
		catch_speed = 100,
		release_speed = 200,
		type = var_0_27,
		act = var_0_15,
		catch = var_0_17,
		move_range = {
			-300,
			1800,
			0,
			0
		},
		good = var_0_21,
		interaction = {
			time = {
				3,
				7
			},
			parame = {
				"swim"
			}
		}
	},
	{
		score = -100,
		name = "submarine_2",
		speed = 150,
		catch_speed = 100,
		release_speed = 200,
		type = var_0_27,
		act = var_0_15,
		catch = var_0_17,
		move_range = {
			-300,
			1800,
			0,
			0
		},
		good = var_0_21,
		interaction = {
			time = {
				3,
				7
			},
			parame = {
				"swim"
			}
		}
	},
	{
		score = -80,
		name = "submarine_3",
		speed = 120,
		catch_speed = 100,
		release_speed = 200,
		type = var_0_27,
		act = var_0_15,
		catch = var_0_17,
		move_range = {
			-300,
			1800,
			0,
			0
		},
		good = var_0_21,
		interaction = {
			time = {
				3,
				7
			},
			parame = {
				"swim"
			}
		}
	},
	{
		score = -50,
		name = "submarine_4",
		speed = 90,
		catch_speed = 100,
		release_speed = 200,
		type = var_0_27,
		act = var_0_15,
		catch = var_0_17,
		move_range = {
			-300,
			1800,
			0,
			0
		},
		good = var_0_21,
		interaction = {
			time = {
				3,
				7
			},
			parame = {
				"swim"
			}
		}
	},
	{
		score = -50,
		name = "boom",
		speed = 500,
		catch_speed = 300,
		type = var_0_29,
		act = var_0_15,
		catch = var_0_16,
		move_range = {
			-300,
			1800,
			0,
			0
		},
		good = var_0_20
	},
	{
		speed = 0,
		name = "rock",
		score = 50,
		catch_speed = 80,
		type = var_0_28,
		act = var_0_14,
		catch = var_0_16,
		good = var_0_22
	},
	{
		score = 300,
		name = "gold",
		speed = 0,
		catch_speed = 160,
		type = var_0_28,
		act = var_0_14,
		catch = var_0_16,
		create_range = {
			0,
			9999,
			0,
			130
		},
		good = var_0_19
	},
	{
		score = 600,
		name = "treasure",
		speed = 0,
		catch_speed = 55,
		type = var_0_28,
		act = var_0_14,
		catch = var_0_16,
		create_range = {
			0,
			9999,
			0,
			130
		},
		good = var_0_19
	},
	{
		speed = 0,
		name = "watch",
		time = 20,
		catch_speed = 180,
		type = var_0_30,
		act = var_0_14,
		catch = var_0_16,
		create_range = {
			0,
			9999,
			0,
			130
		},
		good = var_0_19
	},
	{
		score = 200,
		name = "shell",
		speed = 0,
		catch_speed = 100,
		type = var_0_28,
		act = var_0_14,
		catch = var_0_16,
		create_range = {
			0,
			9999,
			0,
			130
		},
		good = var_0_19,
		catch_rule = {
			targetName = "pearl",
			state = {
				1
			}
		},
		anim_data = {
			state_change = {
				1,
				2
			},
			time = {
				3,
				5
			}
		}
	},
	{
		speed = 0,
		name = "pearl",
		score = 500,
		catch_speed = 200,
		type = var_0_32,
		act = var_0_14,
		catch = var_0_16,
		good = var_0_19
	},
	{
		speed = 30,
		name = "Anglerfish",
		direct = -1,
		type = var_0_31,
		act = var_0_15,
		scene = var_0_23,
		catch = var_0_18,
		create_range = {
			-9999,
			9999,
			130,
			600
		},
		move_range = {
			-400,
			1800,
			0,
			0
		}
	},
	{
		speed = 20,
		name = "Fish_A",
		direct = -1,
		type = var_0_31,
		act = var_0_15,
		scene = var_0_23,
		catch = var_0_18,
		create_range = {
			-9999,
			9999,
			130,
			600
		},
		move_range = {
			-400,
			1800,
			0,
			0
		}
	},
	{
		speed = 20,
		name = "Fish_B",
		direct = -1,
		type = var_0_31,
		act = var_0_15,
		scene = var_0_23,
		catch = var_0_18,
		create_range = {
			-9999,
			9999,
			130,
			600
		},
		move_range = {
			-400,
			1800,
			0,
			0
		}
	},
	{
		speed = 20,
		name = "Fish_C",
		direct = -1,
		type = var_0_31,
		act = var_0_15,
		scene = var_0_23,
		catch = var_0_18,
		create_range = {
			-9999,
			9999,
			130,
			600
		},
		move_range = {
			-400,
			1800,
			0,
			0
		}
	},
	{
		speed = 10,
		name = "Fish_D",
		direct = -1,
		type = var_0_31,
		act = var_0_15,
		scene = var_0_23,
		catch = var_0_18,
		create_range = {
			-9999,
			9999,
			130,
			600
		},
		move_range = {
			-400,
			1800,
			0,
			0
		}
	},
	{
		speed = 30,
		name = "Fish_E",
		direct = -1,
		type = var_0_31,
		act = var_0_15,
		scene = var_0_23,
		catch = var_0_18,
		create_range = {
			-9999,
			9999,
			130,
			600
		},
		move_range = {
			-400,
			1800,
			0,
			0
		}
	},
	{
		speed = 20,
		name = "Fish_manjuu",
		direct = -1,
		type = var_0_31,
		act = var_0_15,
		scene = var_0_23,
		catch = var_0_18,
		create_range = {
			-9999,
			9999,
			130,
			600
		},
		move_range = {
			-400,
			1800,
			0,
			0
		}
	},
	{
		speed = 30,
		name = "Seal",
		direct = -1,
		type = var_0_31,
		act = var_0_15,
		scene = var_0_23,
		catch = var_0_18,
		create_range = {
			-9999,
			9999,
			130,
			600
		},
		move_range = {
			-400,
			1800,
			0,
			0
		}
	},
	{
		speed = 30,
		name = "Submarine",
		direct = -1,
		type = var_0_31,
		act = var_0_15,
		scene = var_0_23,
		catch = var_0_18,
		create_range = {
			-9999,
			9999,
			130,
			600
		},
		move_range = {
			-400,
			1800,
			0,
			0
		}
	},
	{
		speed = 30,
		name = "Sunfish",
		direct = -1,
		type = var_0_31,
		act = var_0_15,
		scene = var_0_23,
		catch = var_0_18,
		create_range = {
			-9999,
			9999,
			130,
			600
		},
		move_range = {
			-400,
			1800,
			0,
			0
		}
	}
}
local var_0_37 = 500
local var_0_38 = 300
local var_0_39 = 200
local var_0_40 = 200
local var_0_41 = 45
local var_0_42 = 2.5
local var_0_43 = 50
local var_0_44 = 100
local var_0_45 = 580
local var_0_46 = 130
local var_0_47 = {
	{
		color = "8dff1e",
		font = 44,
		score = 500
	},
	{
		color = "d0fb09",
		font = 44,
		score = 400
	},
	{
		color = "ffec1e",
		font = 44,
		score = 300
	},
	{
		score = 200,
		color = "fcdc2a"
	},
	{
		score = 100,
		color = "f1b524"
	},
	{
		score = 0,
		color = "ffa024"
	},
	{
		score = -100,
		color = "680c00"
	},
	{
		score = -200,
		color = "6f1807"
	}
}
local var_0_48 = "char apply position"
local var_0_49 = "char apply move"
local var_0_50 = "char apply act"
local var_0_51 = {
	{
		speed = 3,
		id = 1,
		tf = "Shiratsuyu",
		bindIds = {
			2
		},
		actions = {
			{
				posX = -1200,
				type = var_0_48
			},
			{
				trigger = "moveA",
				type = var_0_50
			},
			{
				sync = True,
				offsetX = -50,
				direct = -1,
				type = var_0_49,
				moveToX = {
					300,
					400
				}
			},
			{
				time = 2,
				trigger = "actA",
				type = var_0_50
			},
			{
				time = 2,
				trigger = "actB",
				type = var_0_50
			},
			{
				time = 0,
				trigger = "moveB",
				type = var_0_50
			},
			{
				direct = -1,
				type = var_0_49,
				moveToX = {
					2000,
					2000
				}
			}
		}
	},
	{
		id = 2,
		speed = 3,
		tf = "Shigure",
		actions = {
			{
				posX = 1200,
				type = var_0_48
			},
			{
				trigger = "moveA",
				type = var_0_50
			},
			{
				sync = True,
				offsetX = 50,
				direct = -1,
				type = var_0_49
			},
			{
				time = 2,
				trigger = "actA",
				type = var_0_50
			},
			{
				time = 2,
				trigger = "actB",
				type = var_0_50
			},
			{
				time = 0,
				trigger = "moveB",
				type = var_0_50
			},
			{
				direct = -1,
				type = var_0_49,
				moveToX = {
					2100,
					2200
				}
			}
		}
	},
	{
		id = 3,
		speed = 2,
		tf = "eldridge",
		actions = {
			{
				posX = -1200,
				type = var_0_48
			},
			{
				trigger = "move",
				type = var_0_50
			},
			{
				direct = -1,
				type = var_0_49,
				moveToX = {
					100,
					300
				}
			},
			{
				trigger = "act",
				type = var_0_50
			},
			{
				direct = -1,
				type = var_0_49,
				moveToX = {
					600,
					700
				}
			},
			{
				trigger = "act",
				type = var_0_50
			},
			{
				direct = -1,
				type = var_0_49,
				moveToX = {
					1300,
					1300
				}
			}
		}
	},
	{
		id = 4,
		speed = 4,
		tf = "bombBoat",
		actions = {
			{
				posX = 1200,
				type = var_0_48
			},
			{
				trigger = "move",
				type = var_0_50
			},
			{
				direct = -1,
				type = var_0_49,
				moveToX = {
					-1100,
					-1300
				}
			}
		}
	},
	{
		id = 5,
		speed = 3,
		tf = "Fleet",
		actions = {
			{
				posX = -1200,
				type = var_0_48
			},
			{
				trigger = "move",
				type = var_0_50
			},
			{
				direct = -1,
				type = var_0_49,
				moveToX = {
					500,
					700
				}
			},
			{
				time = 4,
				trigger = "act",
				type = var_0_50
			},
			{
				direct = -1,
				type = var_0_49,
				moveToX = {
					1300,
					1500
				}
			}
		}
	},
	{
		id = 6,
		speed = 4,
		tf = "Glowworm",
		actions = {
			{
				posX = 1200,
				type = var_0_48
			},
			{
				trigger = "move",
				type = var_0_50
			},
			{
				direct = -1,
				type = var_0_49,
				moveToX = {
					-550,
					-1000
				}
			},
			{
				time = 2,
				trigger = "act",
				type = var_0_50
			}
		}
	}
}
local var_0_52 = {
	25,
	30
}
local var_0_53 = {
	1,
	3,
	4,
	5,
	6
}
local var_0_54 = {
	"actA",
	"actB"
}
local var_0_55 = {
	10,
	15
}

local function var_0_56(arg_1_0, arg_1_1)
	local var_1_0 = {
		def ctor:(arg_2_0)
			arg_2_0._sceneTf = arg_1_0
			arg_2_0._boatTf = findTF(arg_1_0, "boat")
			arg_2_0._event = arg_1_1
			arg_2_0._hookTf = findTF(arg_2_0._boatTf, "body/hook")
			arg_2_0._hookContent = findTF(arg_2_0._hookTf, "container/content")
			arg_2_0._hookCollider = findTF(arg_2_0._hookTf, "container/collider")
			arg_2_0._sceneContent = findTF(arg_2_0._sceneTf, "container/content")
			arg_2_0.hookAnimator = GetComponent(findTF(arg_2_0._hookTf, "bottom"), typeof(Animator))
			arg_2_0.hookMaskAnimator = GetComponent(findTF(arg_2_0._hookTf, "mask/img"), typeof(Animator))
			arg_2_0.captainAnimator = GetComponent(findTF(arg_2_0._boatTf, "body/captain/img"), typeof(Animator))

			GetComponent(findTF(arg_2_0._boatTf, "body/captain/img"), typeof(DftAniEvent)).SetEndEvent(function()
				if arg_2_0.inGoodAct:
					arg_2_0.inGoodAct = False)

			arg_2_0.marinerAnimator = GetComponent(findTF(arg_2_0._boatTf, "body/mariner/img"), typeof(Animator)),
		def start:(arg_4_0)
			arg_4_0._hookTf.sizeDelta = Vector2(0, 1)
			arg_4_0.boatState = var_0_11
			arg_4_0.hookRotation = var_0_41
			arg_4_0.hookRotationSpeed = 0
			arg_4_0.hookTargetRotation = var_0_41
			arg_4_0.throwHook = False
			arg_4_0.inGoodAct = False

			if arg_4_0.catchItem:
				destroy(arg_4_0.catchItem.tf)

				arg_4_0.catchItem = None

			arg_4_0.marinerActTime = None
			arg_4_0.marinerActName = None

			arg_4_0.leaveItem(),
		def step:(arg_5_0)
			if arg_5_0.boatState == var_0_11:
				arg_5_0.checkChangeRotation()

				arg_5_0.hookRotation = arg_5_0.hookRotation + arg_5_0.getSpringRotation()
				arg_5_0._hookTf.localEulerAngles = Vector3(0, 0, arg_5_0.hookRotation)
			elif arg_5_0.boatState == var_0_12:
				if arg_5_0.throwHook:
					arg_5_0._hookTf.sizeDelta = Vector2(0, arg_5_0._hookTf.sizeDelta.y + var_0_39 * Time.deltaTime)

					local var_5_0 = math.cos(math.deg2Rad * math.abs(arg_5_0.hookRotation))

					if arg_5_0._hookTf.sizeDelta.y * var_5_0 > var_0_38 or arg_5_0._hookTf.sizeDelta.y > var_0_37:
						arg_5_0.throwHook = False
				else
					local var_5_1 = arg_5_0.hookBack()

					if not arg_5_0.catchItem and var_5_1:
						arg_5_0.boatState = var_0_11
					elif arg_5_0.catchItem:
						local var_5_2 = arg_5_0._hookContent.position
						local var_5_3 = arg_5_0._sceneContent.InverseTransformPoint(var_5_2)

						if (arg_5_0.catchItem.data.catch == var_0_17 or arg_5_0.catchItem.data.act == var_0_15) and var_5_3.y > var_0_45:
							arg_5_0.boatState = var_0_13

							arg_5_0.leaveItem()
						elif var_5_1:
							arg_5_0.boatState = var_0_13

							arg_5_0.leaveItem()
			elif arg_5_0.boatState == var_0_13:
				if not arg_5_0.hookBack():
					return

				if arg_5_0.inGoodAct:
					return

				arg_5_0.boatState = var_0_11

			if arg_5_0.boatState == var_0_12 and arg_5_0.throwHook:
				arg_5_0.hookAnimator.SetBool("hook", True)
				arg_5_0.hookMaskAnimator.SetBool("hook", True)
			else
				arg_5_0.hookAnimator.SetBool("hook", False)
				arg_5_0.hookMaskAnimator.SetBool("hook", False)

			if arg_5_0.boatState == var_0_12:
				if arg_5_0.throwHook:
					arg_5_0.captainAnimator.SetInteger("state", 4)
				else
					local var_5_4 = 1

					if arg_5_0.catchItem:
						var_5_4 = arg_5_0.catchItem.data.catch_speed >= 100 and 1 or arg_5_0.catchItem.data.catch_speed >= 50 and arg_5_0.catchItem.data.catch_speed <= 100 and 2 or 3

					arg_5_0.captainAnimator.SetInteger("state", var_5_4)
			else
				arg_5_0.captainAnimator.SetInteger("state", 0)

			if not arg_5_0.marinerActTime:
				arg_5_0.marinerActTime = math.random(var_0_55[1], var_0_55[2])
				arg_5_0.marinerActName = var_0_54[math.random(1, #var_0_54)]
			elif arg_5_0.marinerActTime <= 0:
				arg_5_0.marinerAnimator.SetTrigger(arg_5_0.marinerActName)

				arg_5_0.marinerActTime = math.random(var_0_55[1], var_0_55[2])
				arg_5_0.marinerActName = var_0_54[math.random(1, #var_0_54)]
			else
				arg_5_0.marinerActTime = arg_5_0.marinerActTime - Time.deltaTime,
		def hookBack:(arg_6_0)
			if arg_6_0._hookTf.sizeDelta.y > 1:
				local var_6_0 = var_0_40 * Time.deltaTime

				if arg_6_0.catchItem:
					var_6_0 = arg_6_0.catchItem.data.catch_speed * Time.deltaTime

				arg_6_0._hookTf.sizeDelta = Vector2(0, arg_6_0._hookTf.sizeDelta.y - var_6_0)

				return False
			elif arg_6_0._hookTf.sizeDelta.y < 1:
				arg_6_0._hookTf.sizeDelta = Vector2(0, 1)

				return False

			return True,
		def leaveItem:(arg_7_0)
			if arg_7_0.catchItem:
				arg_7_0._event.emit(var_0_10, arg_7_0.catchItem, function()
					return)

				arg_7_0.inGoodAct = True

				if arg_7_0.catchItem.data.good == var_0_19:
					arg_7_0.captainAnimator.SetTrigger("happy")
					arg_7_0.marinerAnimator.SetTrigger("happy")
				elif arg_7_0.catchItem.data.good == var_0_21:
					arg_7_0.captainAnimator.SetTrigger("release")
				elif arg_7_0.catchItem.data.good == var_0_20:
					arg_7_0.captainAnimator.SetTrigger("surprise")
					arg_7_0.marinerAnimator.SetTrigger("surprise")
				elif arg_7_0.catchItem.data.good == var_0_22:
					arg_7_0.inGoodAct = False

				arg_7_0.catchItem = None,
		def throw:(arg_9_0)
			if arg_9_0.boatState != var_0_11:
				return

			pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_3)

			arg_9_0.throwHook = True
			arg_9_0.boatState = var_0_12,
		def setCatchItem:(arg_10_0, arg_10_1)
			if arg_10_0.boatState == var_0_12 and arg_10_0.throwHook:
				arg_10_0.catchItem = arg_10_1
				arg_10_0.throwHook = False
				arg_10_1.tf.localScale = Vector3(math.sign(arg_10_1.tf.localScale.x), 1, 1)

				SetParent(arg_10_1.tf, arg_10_0._hookContent)

				arg_10_1.tf.anchoredPosition = Vector2(0, 0)

				pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_4),
		def getSpringRotation:(arg_11_0)
			arg_11_0.hookRotationSpeed = arg_11_0.hookRotationSpeed + math.sign(arg_11_0.hookTargetRotation) * var_0_42

			if math.abs(arg_11_0.hookRotationSpeed) > var_0_43:
				arg_11_0.hookRotationSpeed = var_0_43 * math.sign(arg_11_0.hookTargetRotation)

			return arg_11_0.hookRotationSpeed * Time.deltaTime,
		def checkChangeRotation:(arg_12_0)
			if arg_12_0.hookTargetRotation > 0 and arg_12_0.hookRotation > arg_12_0.hookTargetRotation:
				arg_12_0.hookTargetRotation = -arg_12_0.hookTargetRotation
			elif arg_12_0.hookTargetRotation < 0 and arg_12_0.hookRotation < arg_12_0.hookTargetRotation:
				arg_12_0.hookTargetRotation = -arg_12_0.hookTargetRotation,
		def inCatch:(arg_13_0)
			return arg_13_0.boatState == var_0_12 and arg_13_0.throwHook,
		def getHookPosition:(arg_14_0)
			return arg_14_0._hookCollider.position,
		def gameOver:(arg_15_0)
			arg_15_0.captainAnimator.SetTrigger("end")
			arg_15_0.marinerAnimator.SetTrigger("end"),
		def destroy:(arg_16_0)
			return
	}

	var_1_0.ctor()

	return var_1_0

local function var_0_57(arg_17_0, arg_17_1, arg_17_2, arg_17_3)
	local var_17_0 = {
		def ctor:(arg_18_0)
			arg_18_0._event = arg_17_3
			arg_18_0._sceneTpls = findTF(arg_17_0, "sceneTpls")
			arg_18_0._backSceneTpls = findTF(arg_17_1, "bgTpls")
			arg_18_0._gameMission = arg_17_2 + 1

			local var_18_0 = findTF(arg_17_0, "container")

			arg_18_0._createBounds = {
				var_18_0.sizeDelta.x,
				var_18_0.sizeDelta.y
			}
			arg_18_0._parentTf = findTF(var_18_0, "content")
			arg_18_0._backParentTf = findTF(arg_17_1, "container/content")
			arg_18_0.items = {},
		def getParentInversePos:(arg_19_0, arg_19_1)
			local var_19_0 = arg_19_1.tf.position
			local var_19_1

			if arg_19_1.data.scene:
				if arg_19_1.data.scene == var_0_23:
					var_19_1 = arg_19_0._backParentTf.InverseTransformPoint(var_19_0)
				else
					var_19_1 = arg_19_0._parentTf.InverseTransformPoint(var_19_0)
			else
				var_19_1 = arg_19_0._parentTf.InverseTransformPoint(var_19_0)

			return var_19_1,
		def addItemDone:(arg_20_0, arg_20_1, arg_20_2)
			local var_20_0 = arg_20_0.getParentInversePos(arg_20_1)

			if arg_20_1.data.act == var_0_15 or arg_20_1.data.catch == var_0_17:
				var_20_0.y = var_0_45

			arg_20_1.tf.anchoredPosition = var_20_0

			arg_20_0.addItemParent(arg_20_1)

			arg_20_1.tf.localScale = Vector3(2.5 * math.sign(arg_20_1.tf.localScale.x), 2.5, 2.5)
			arg_20_1.tf.localEulerAngles = Vector3(0, 0, 0)
			arg_20_1.catchAble = False
			arg_20_1.targetRemove = True

			if arg_20_1.data.catch == var_0_16:
				GetComponent(arg_20_1.tf, typeof(DftAniEvent)).SetEndEvent(function()
					arg_20_0.destroyItem(arg_20_1))
				GetComponent(arg_20_1.tf, typeof(Animator)).SetTrigger("catch")
			elif arg_20_1.data.catch == var_0_17:
				local var_20_1 = arg_20_1.data.leave_direct or 1

				arg_20_1.direct = var_20_1
				arg_20_1.targetX = var_20_1 * math.sign(arg_20_1.tf.localScale.x) == -1 and arg_20_1.data.move_range[2] or arg_20_1.data.move_range[1]

				GetComponent(arg_20_1.tf, typeof(DftAniEvent)).SetEndEvent(function()
					arg_20_1.moveAble = True)

				arg_20_1.moveAble = False

				GetComponent(arg_20_1.tf, typeof(Animator)).SetTrigger("release")
				table.insert(arg_20_0.items, arg_20_1),
		def start:(arg_23_0)
			arg_23_0.clearItems()
			arg_23_0.prepareItems()
			arg_23_0.setItemPosition(),
		def clearItems:(arg_24_0)
			for iter_24_0 = #arg_24_0.items, 1, -1:
				local var_24_0 = table.remove(arg_24_0.items, iter_24_0)

				arg_24_0.destroyItem(var_24_0)

				local var_24_1

			arg_24_0.items = {},
		def prepareItems:(arg_25_0)
			local var_25_0 = var_0_35[math.random(1, #var_0_35)]

			for iter_25_0, iter_25_1 in pairs(var_25_0):
				local var_25_1 = math.random(iter_25_1.amount[1], iter_25_1.amount[2])
				local var_25_2 = iter_25_1.type
				local var_25_3 = iter_25_1.repeated
				local var_25_4 = iter_25_1.name
				local var_25_5 = arg_25_0.getItemsByType(var_25_2, var_25_4)

				for iter_25_2 = 1, var_25_1:
					local var_25_6

					if var_25_3:
						var_25_6 = var_25_5[math.random(1, #var_25_5)]
					elif #var_25_5 > 0:
						var_25_6 = table.remove(var_25_5, math.random(1, #var_25_5))

					if var_25_6:
						local var_25_7 = arg_25_0.createItem(var_25_6)

						table.insert(arg_25_0.items, var_25_7),
		def getItemsByType:(arg_26_0, arg_26_1, arg_26_2)
			local var_26_0 = {}

			for iter_26_0 = 1, #var_0_36:
				if var_0_36[iter_26_0].type == arg_26_1:
					if arg_26_2:
						if table.contains(arg_26_2, var_0_36[iter_26_0].name):
							table.insert(var_26_0, var_0_36[iter_26_0])
					else
						table.insert(var_26_0, var_0_36[iter_26_0])

			return var_26_0,
		def getItemDataByName:(arg_27_0, arg_27_1)
			for iter_27_0 = 1, #var_0_36:
				if var_0_36[iter_27_0].name == arg_27_1:
					return var_0_36[iter_27_0]

			return None,
		def createItem:(arg_28_0, arg_28_1)
			local var_28_0 = {
				data = arg_28_1
			}

			var_28_0.tf = None
			var_28_0.targetX = None
			var_28_0.targetY = None
			var_28_0.direct = arg_28_1.direct or 1
			var_28_0.moveAble = True
			var_28_0.catchAble = True
			var_28_0.targetRemove = False
			var_28_0.interaction = arg_28_1.interaction and True or False
			var_28_0.interactionName = None
			var_28_0.interactionTime = None
			var_28_0.animStateIndex = None
			var_28_0.nextAnimTime = None

			arg_28_0.instantiateItem(var_28_0)

			return var_28_0,
		def instantiateItem:(arg_29_0, arg_29_1)
			local var_29_0

			if arg_29_1.data.scene == var_0_23:
				var_29_0 = findTF(arg_29_0._backSceneTpls, arg_29_1.data.name)
			else
				var_29_0 = findTF(arg_29_0._sceneTpls, arg_29_1.data.name)

			local var_29_1 = Instantiate(var_29_0)

			arg_29_1.tf = tf(var_29_1)

			setActive(arg_29_1.tf, True)
			arg_29_0.addItemParent(arg_29_1),
		def addItemParent:(arg_30_0, arg_30_1)
			if arg_30_1.data.scene:
				if arg_30_1.data.scene == var_0_23:
					SetParent(arg_30_1.tf, arg_30_0._backParentTf)
				else
					SetParent(arg_30_1.tf, arg_30_0._parentTf)
			else
				SetParent(arg_30_1.tf, arg_30_0._parentTf),
		def setItemPosition:(arg_31_0)
			if not arg_31_0.items or #arg_31_0.items == 0:
				return

			local var_31_0 = arg_31_0.splitePositions(0, arg_31_0._createBounds[1])
			local var_31_1 = arg_31_0.splitePositions(0, arg_31_0._createBounds[2])
			local var_31_2 = arg_31_0.mixSplitePos(var_31_0, var_31_1)

			local function var_31_3(arg_32_0)
				if arg_32_0:
					local var_32_0 = {}

					for iter_32_0 = 1, #var_31_2:
						local var_32_1 = iter_32_0
						local var_32_2 = var_31_2[iter_32_0]
						local var_32_3 = arg_32_0[1]
						local var_32_4 = arg_32_0[2]
						local var_32_5 = arg_32_0[3]
						local var_32_6 = arg_32_0[4]
						local var_32_7 = var_32_2[1][1]
						local var_32_8 = var_32_2[1][2]
						local var_32_9 = var_32_2[2][1]
						local var_32_10 = var_32_2[2][2]

						if var_32_3 <= var_32_7 and var_32_8 <= var_32_4 and var_32_5 <= var_32_9 and var_32_10 <= var_32_6:
							table.insert(var_32_0, var_32_1)

					if #var_32_0 > 0:
						return table.remove(var_31_2, var_32_0[math.random(1, #var_32_0)])

				if #var_31_2 > 0:
					return table.remove(var_31_2, math.random(1, #var_31_2))
				else
					return {
						{
							0,
							1300
						},
						{
							100,
							300
						}
					}

			for iter_31_0 = 1, #arg_31_0.items:
				local var_31_4 = var_31_3(arg_31_0.items[iter_31_0].data.create_range)

				if var_31_4:
					local var_31_5 = var_31_4[1][1] + math.random() * (var_31_4[1][2] - var_31_4[1][1]) / 2
					local var_31_6 = var_31_4[2][1] + math.random() * (var_31_4[2][2] - var_31_4[2][1]) / 2

					arg_31_0.items[iter_31_0].tf.anchoredPosition = Vector2(var_31_5, var_31_6),
		def mixSplitePos:(arg_33_0, arg_33_1, arg_33_2)
			local var_33_0 = {}

			for iter_33_0 = 1, #arg_33_1:
				local var_33_1 = arg_33_1[iter_33_0]

				for iter_33_1 = 1, #arg_33_2:
					local var_33_2 = arg_33_2[iter_33_1]

					table.insert(var_33_0, {
						var_33_1,
						var_33_2
					})

			return var_33_0,
		def splitePositions:(arg_34_0, arg_34_1, arg_34_2)
			local var_34_0 = {}

			if not arg_34_1 or not arg_34_2 or arg_34_2 < arg_34_1:
				return None

			local var_34_1 = (arg_34_2 - arg_34_1) / var_0_46

			for iter_34_0 = 1, var_34_1:
				table.insert(var_34_0, {
					arg_34_1 + (iter_34_0 - 1) * var_0_46,
					arg_34_1 + iter_34_0 * var_0_46
				})

			return var_34_0,
		def getItemByPos:(arg_35_0, arg_35_1)
			local var_35_0 = arg_35_0.checkPosInCollider(arg_35_1)

			if var_35_0:
				if var_35_0.data.catch_rule:
					local var_35_1 = GetComponent(var_35_0.tf, typeof(Animator)).GetInteger("state")
					local var_35_2 = var_35_0.data.catch_rule.state

					if table.contains(var_35_2, var_35_1):
						arg_35_0.addItemDone(var_35_0)

						return (arg_35_0.createItem(arg_35_0.getItemDataByName(var_35_0.data.catch_rule.targetName)))
				else
					return var_35_0

				return var_35_0

			return None,
		def checkPosInCollider:(arg_36_0, arg_36_1)
			local var_36_0 = {}
			local var_36_1 = arg_36_0._parentTf.InverseTransformPoint(arg_36_1.x, arg_36_1.y, arg_36_1.z)

			for iter_36_0 = 1, #arg_36_0.items:
				if arg_36_0.items[iter_36_0].data.catch != var_0_18:
					local var_36_2 = arg_36_0.items[iter_36_0].tf

					if math.abs(var_36_1.x - var_36_2.anchoredPosition.x) < var_0_44 and math.abs(var_36_1.y - var_36_2.anchoredPosition.y) < var_0_44 and arg_36_0.items[iter_36_0].data.catch != var_0_18 and arg_36_0.items[iter_36_0].catchAble:
						table.insert(var_36_0, arg_36_0.items[iter_36_0])

			for iter_36_1 = 1, #var_36_0:
				local var_36_3 = findTF(var_36_0[iter_36_1].tf, "collider")

				if not var_36_3:
					print("can not find collider by" .. var_36_0[iter_36_1].data.name)
				else
					local var_36_4 = var_36_3.InverseTransformPoint(arg_36_1.x, arg_36_1.y, arg_36_1.z)
					local var_36_5 = var_36_3.rect.xMin
					local var_36_6 = var_36_3.rect.yMin
					local var_36_7 = var_36_3.rect.width
					local var_36_8 = var_36_3.rect.height

					if arg_36_0.isPointInMatrix(Vector2(var_36_5, var_36_6 + var_36_8), Vector2(var_36_5 + var_36_7, var_36_6 + var_36_8), Vector2(var_36_5 + var_36_7, var_36_6), Vector2(var_36_5, var_36_6), var_36_4):
						return arg_36_0.removeItem(var_36_0[iter_36_1])

			return None,
		def removeItem:(arg_37_0, arg_37_1)
			for iter_37_0 = 1, #arg_37_0.items:
				if arg_37_0.items[iter_37_0] == arg_37_1:
					return table.remove(arg_37_0.items, iter_37_0),
		def getCross:(arg_38_0, arg_38_1, arg_38_2, arg_38_3)
			return (arg_38_2.x - arg_38_1.x) * (arg_38_3.y - arg_38_1.y) - (arg_38_3.x - arg_38_1.x) * (arg_38_2.y - arg_38_1.y),
		def isPointInMatrix:(arg_39_0, arg_39_1, arg_39_2, arg_39_3, arg_39_4, arg_39_5)
			return arg_39_0.getCross(arg_39_1, arg_39_2, arg_39_5) * arg_39_0.getCross(arg_39_3, arg_39_4, arg_39_5) >= 0 and arg_39_0.getCross(arg_39_2, arg_39_3, arg_39_5) * arg_39_0.getCross(arg_39_4, arg_39_1, arg_39_5) >= 0,
		def step:(arg_40_0)
			for iter_40_0 = #arg_40_0.items, 1, -1:
				local var_40_0 = arg_40_0.items[iter_40_0]

				if var_40_0.data.act == var_0_15 and var_40_0.moveAble:
					if not var_40_0.targetX:
						local var_40_1 = var_40_0.data.move_range[1]
						local var_40_2 = var_40_0.data.move_range[2]

						if var_40_0.tf.anchoredPosition.x == var_40_1:
							var_40_0.targetX = var_40_2
						elif var_40_0.tf.anchoredPosition.x == var_40_2:
							var_40_0.targetX = var_40_1
						else
							var_40_0.targetX = math.random() > 0.5 and var_40_1 or var_40_2
					else
						local var_40_3 = math.sign(var_40_0.targetX - var_40_0.tf.anchoredPosition.x)
						local var_40_4 = var_40_0.targetRemove and var_40_0.data.release_speed or var_40_0.data.speed

						var_40_0.tf.localScale = Vector3(-1 * var_40_3 * var_40_0.direct * math.abs(var_40_0.tf.localScale.x), var_40_0.tf.localScale.y, var_40_0.tf.localScale.z)

						local var_40_5 = var_40_3 * var_40_4 * Time.deltaTime

						var_40_0.tf.anchoredPosition = Vector2(var_40_0.tf.anchoredPosition.x + var_40_5, var_40_0.tf.anchoredPosition.y)

						if var_40_3 == 1 and var_40_0.tf.anchoredPosition.x >= var_40_0.targetX or var_40_3 == -1 and var_40_0.tf.anchoredPosition.x <= var_40_0.targetX:
							var_40_0.tf.anchoredPosition = Vector2(var_40_0.targetX, var_40_0.tf.anchoredPosition.y)
							var_40_0.targetX = None

				if var_40_0.data.anim_data:
					local var_40_6 = var_40_0.data.anim_data.state_change
					local var_40_7 = var_40_0.data.anim_data.time

					if var_40_6 and var_40_7:
						if not var_40_0.nextAnimTime:
							var_40_0.nextAnimTime = math.random(var_40_7[1], var_40_7[2])
							var_40_0.animStateIndex = 1
						elif var_40_0.nextAnimTime <= 0:
							GetComponent(var_40_0.tf, typeof(Animator)).SetInteger("state", var_40_6[var_40_0.animStateIndex])

							var_40_0.nextAnimTime = math.random(var_40_7[1], var_40_7[2])
							var_40_0.animStateIndex = var_40_0.animStateIndex + 1
							var_40_0.animStateIndex = var_40_0.animStateIndex > #var_40_6 and 1 or var_40_0.animStateIndex
						else
							var_40_0.nextAnimTime = var_40_0.nextAnimTime - Time.deltaTime

				if var_40_0.interaction and not var_40_0.targetRemove:
					if not var_40_0.interactionTime:
						var_40_0.interactionTime = math.random() * (var_40_0.data.interaction.time[2] - var_40_0.data.interaction.time[1]) + var_40_0.data.interaction.time[1]
						var_40_0.interactionName = var_40_0.data.interaction.parame[math.random(1, #var_40_0.data.interaction.parame)]
					elif var_40_0.interactionTime <= 0:
						GetComponent(var_40_0.tf, typeof(Animator)).SetTrigger(var_40_0.interactionName)

						var_40_0.interactionTime = None
						var_40_0.interactionName = None
					else
						var_40_0.interactionTime = var_40_0.interactionTime - Time.deltaTime

				if var_40_0.targetRemove and not var_40_0.targetX:
					table.remove(arg_40_0.items, iter_40_0)
					arg_40_0.destroyItem(var_40_0),
		def destroyItem:(arg_41_0, arg_41_1)
			destroy(arg_41_1.tf),
		def destroy:(arg_42_0)
			return
	}

	var_17_0.ctor()

	return var_17_0

local function var_0_58(arg_43_0, arg_43_1)
	local var_43_0 = {
		def ctor:(arg_44_0)
			arg_44_0._boatController = arg_43_0
			arg_44_0._itemController = arg_43_1,
		def start:(arg_45_0)
			return,
		def step:(arg_46_0)
			if arg_46_0._boatController.inCatch():
				local var_46_0 = arg_46_0._boatController.getHookPosition()
				local var_46_1 = arg_46_0._itemController.getItemByPos(var_46_0)

				if var_46_1:
					GetComponent(var_46_1.tf, typeof(Animator)).SetTrigger("hold")
					arg_46_0._boatController.setCatchItem(var_46_1),
		def destroy:(arg_47_0)
			return
	}

	var_43_0.ctor()

	return var_43_0

local function var_0_59(arg_48_0, arg_48_1)
	local var_48_0 = {
		def ctor:(arg_49_0)
			arg_49_0._charTpls = findTF(arg_48_0, "charTpls")
			arg_49_0._content = findTF(arg_48_0, "charContainer/content")
			arg_49_0._event = arg_48_1,
		def start:(arg_50_0)
			arg_50_0.clear()

			arg_50_0.chars = {}
			arg_50_0.nextTime = math.random(var_0_52[1], var_0_52[2])
			arg_50_0.showChars = Clone(var_0_53),
		def step:(arg_51_0)
			if arg_51_0.nextTime <= 0 and #arg_51_0.showChars > 0:
				table.insert(arg_51_0.chars, arg_51_0.createChar())

				arg_51_0.nextTime = math.random(var_0_52[1], var_0_52[2])
			else
				arg_51_0.nextTime = arg_51_0.nextTime - Time.deltaTime

			arg_51_0.setCharAction()

			for iter_51_0 = #arg_51_0.chars, 1, -1:
				arg_51_0.stepChar(arg_51_0.chars[iter_51_0])

				if arg_51_0.chars[iter_51_0].removeFlag:
					arg_51_0.removeChar(table.remove(arg_51_0.chars, iter_51_0)),
		def stepChar:(arg_52_0, arg_52_1)
			local var_52_0 = False

			if arg_52_1.posX:
				arg_52_1.tf.anchoredPosition = Vector2(arg_52_1.posX + (arg_52_1.offsetX or 0), 0)

				setActive(arg_52_1.tf, True)

				arg_52_1.posX = None
				arg_52_1.offsetX = None

			if arg_52_1.moveToX:
				local var_52_1 = arg_52_1.moveToX + arg_52_1.offsetX
				local var_52_2 = arg_52_1.tf.anchoredPosition
				local var_52_3 = math.sign(var_52_1 - var_52_2.x)

				arg_52_1.tf.anchoredPosition = Vector3(var_52_2.x + var_52_3 * arg_52_1.speed, 0)

				local var_52_4 = math.sign(var_52_2.x - var_52_1)
				local var_52_5 = math.sign(arg_52_1.tf.anchoredPosition.x - var_52_1)

				if arg_52_1.tf.anchoredPosition.x == var_52_1 or var_52_4 != var_52_5:
					arg_52_1.moveToX = None
					arg_52_1.offsetX = None
				else
					var_52_0 = True

			if arg_52_1.triggerName or arg_52_1.time:
				if arg_52_1.triggerName and arg_52_1.animator:
					arg_52_1.animator.SetTrigger(arg_52_1.triggerName)

					arg_52_1.triggerName = None

				arg_52_1.time = arg_52_1.time - Time.deltaTime

				if arg_52_1.triggerName == None and arg_52_1.time <= 0:
					arg_52_1.time = None
				else
					var_52_0 = True

			arg_52_1.inAction = var_52_0,
		def getRandomMoveX:(arg_53_0, arg_53_1, arg_53_2)
			return arg_53_1 + math.random(0, arg_53_2 - arg_53_1),
		def removeChar:(arg_54_0, arg_54_1)
			if arg_54_1.bindChars:
				arg_54_1.bindChars = {}

			destroy(arg_54_1.tf),
		def setCharAction:(arg_55_0)
			for iter_55_0 = 1, #arg_55_0.chars:
				local var_55_0 = arg_55_0.chars[iter_55_0]

				if not var_55_0.currentActionInfo and #var_55_0.actionInfos > 0 and not var_55_0.inAction:
					if var_55_0.sync and var_55_0.bindIds and #var_55_0.bindIds > 0:
						local var_55_1 = True

						for iter_55_1, iter_55_2 in ipairs(var_55_0.bindChars):
							if iter_55_2.inAction or not iter_55_2.sync:
								var_55_1 = False

						if var_55_1:
							var_55_0.currentActionInfo = table.remove(var_55_0.actionInfos, 1)

							for iter_55_3, iter_55_4 in ipairs(var_55_0.bindChars):
								iter_55_4.sync = False
					elif not var_55_0.sync:
						var_55_0.currentActionInfo = table.remove(var_55_0.actionInfos, 1)

				if var_55_0.currentActionInfo and not var_55_0.currentActionInfo.sync:
					arg_55_0.addCharAction(var_55_0)
				elif var_55_0.currentActionInfo and var_55_0.currentActionInfo.sync and var_55_0.bindIds:
					arg_55_0.addCharAction(var_55_0)

					for iter_55_5, iter_55_6 in ipairs(var_55_0.bindChars):
						if iter_55_6 and iter_55_6.currentActionInfo and iter_55_6.currentActionInfo.sync:
							arg_55_0.addBindCharAction(var_55_0, iter_55_6)
				elif not var_55_0.currentActionInfo and #var_55_0.actionInfos == 0 and not var_55_0.inAction:
					var_55_0.removeFlag = True,
		def addBindCharAction:(arg_56_0, arg_56_1, arg_56_2)
			if arg_56_2.currentActionInfo.type == var_0_49:
				arg_56_2.moveToX = arg_56_1.moveToX
				arg_56_2.offsetX = arg_56_2.currentActionInfo.offsetX or 0
			elif arg_56_2.currentActionInfo.type == var_0_48:
				-- block empty
			elif arg_56_2.currentActionInfo.type == var_0_50:
				-- block empty

			arg_56_2.sync = arg_56_2.currentActionInfo.sync
			arg_56_2.currentActionInfo = None
			arg_56_2.inAction = True,
		def addCharAction:(arg_57_0, arg_57_1)
			local var_57_0 = arg_57_1.currentActionInfo.type

			if var_57_0 == var_0_49:
				local var_57_1

				if arg_57_1.currentActionInfo.moveToX:
					var_57_1 = arg_57_0.getRandomMoveX(arg_57_1.currentActionInfo.moveToX[1], arg_57_1.currentActionInfo.moveToX[2])

				arg_57_1.moveToX = var_57_1 or 0
				arg_57_1.offsetX = arg_57_1.currentActionInfo.offsetX or 0
			elif var_57_0 == var_0_48:
				arg_57_1.posX = arg_57_1.currentActionInfo.posX or 0
				arg_57_1.offsetX = arg_57_1.currentActionInfo.offsetX or 0
			elif var_57_0 == var_0_50:
				arg_57_1.triggerName = arg_57_1.currentActionInfo.trigger
				arg_57_1.time = arg_57_1.currentActionInfo.time or 0

			arg_57_1.sync = arg_57_1.currentActionInfo.sync
			arg_57_1.inAction = True
			arg_57_1.currentActionInfo = None,
		def createChar:(arg_58_0, arg_58_1)
			local var_58_0 = {}
			local var_58_1 = Clone(arg_58_1) or arg_58_0.getRandomData()

			if not var_58_1:
				return

			var_58_0.data = var_58_1
			var_58_0.id = var_58_1.id
			var_58_0.bindIds = var_58_1.bindIds
			var_58_0.bindChars = {}
			var_58_0.actionInfos = var_58_1.actions
			var_58_0.speed = var_58_1.speed
			var_58_0.tf = arg_58_0.getCharTf(var_58_1.tf)
			var_58_0.animator = GetComponent(findTF(var_58_0.tf, "anim"), typeof(Animator))
			var_58_0.dft = GetComponent(findTF(var_58_0.tf, "anim"), typeof(DftAniEvent))
			var_58_0.currentActionInfo = None
			var_58_0.posX = None
			var_58_0.moveToX = None
			var_58_0.offsetX = None
			var_58_0.triggerName = None
			var_58_0.time = None
			var_58_0.inAction = False
			var_58_0.removeFlag = False

			if var_58_0.bindIds:
				for iter_58_0 = 1, #var_58_0.bindIds:
					local var_58_2 = arg_58_0.createChar(arg_58_0.getCharDataById(var_58_0.bindIds[iter_58_0]))

					table.insert(arg_58_0.chars, var_58_2)
					table.insert(var_58_0.bindChars, var_58_2)

			return var_58_0,
		def getRandomData:(arg_59_0)
			if arg_59_0.showChars and #arg_59_0.showChars > 0:
				local var_59_0 = table.remove(arg_59_0.showChars, math.random(1, #arg_59_0.showChars))

				return arg_59_0.getCharDataById(var_59_0)

			return None,
		def getCharDataById:(arg_60_0, arg_60_1)
			for iter_60_0, iter_60_1 in ipairs(var_0_51):
				if iter_60_1.id == arg_60_1:
					return Clone(iter_60_1),
		def getCharTf:(arg_61_0, arg_61_1)
			local var_61_0 = tf(instantiate(findTF(arg_61_0._charTpls, arg_61_1)))

			SetParent(var_61_0, arg_61_0._content)
			SetActive(var_61_0, False)

			return var_61_0,
		def clear:(arg_62_0)
			if arg_62_0.chars:
				for iter_62_0 = #arg_62_0.chars, 1, -1:
					arg_62_0.removeChar(table.remove(arg_62_0.chars, iter_62_0))

				arg_62_0.chars = {}
	}

	var_48_0.ctor()

	return var_48_0

def var_0_0.getUIName(arg_63_0):
	return "IslandCatchTreasureGameUI"

def var_0_0.getBGM(arg_64_0):
	return var_0_1

def var_0_0.didEnter(arg_65_0):
	arg_65_0.initEvent()
	arg_65_0.initData()
	arg_65_0.initUI()
	arg_65_0.initGameUI()
	arg_65_0.updateMenuUI()
	arg_65_0.openMenuUI()

def var_0_0.initEvent(arg_66_0):
	arg_66_0.bind(var_0_10, function(arg_67_0, arg_67_1, arg_67_2)
		if arg_66_0.itemController:
			arg_66_0.itemController.addItemDone(arg_67_1, arg_67_2)

		arg_66_0.addScore(arg_67_1.data.score, arg_67_1.data.time))

def var_0_0.initData(arg_68_0):
	local var_68_0 = Application.targetFrameRate or 60

	if var_68_0 > 60:
		var_68_0 = 60

	arg_68_0.timer = Timer.New(function()
		arg_68_0.onTimer(), 1 / var_68_0, -1)

def var_0_0.initUI(arg_70_0):
	arg_70_0.backSceneTf = findTF(arg_70_0._tf, "scene_container/scene_background")
	arg_70_0.sceneTf = findTF(arg_70_0._tf, "scene_container/scene")
	arg_70_0.bgTf = findTF(arg_70_0._tf, "bg")
	arg_70_0.clickMask = findTF(arg_70_0._tf, "clickMask")
	arg_70_0.countUI = findTF(arg_70_0._tf, "pop/CountUI")
	arg_70_0.countAnimator = GetComponent(findTF(arg_70_0.countUI, "count"), typeof(Animator))
	arg_70_0.countDft = GetOrAddComponent(findTF(arg_70_0.countUI, "count"), typeof(DftAniEvent))

	arg_70_0.countDft.SetTriggerEvent(function()
		return)
	arg_70_0.countDft.SetEndEvent(function()
		setActive(arg_70_0.countUI, False)
		arg_70_0.gameStart())
	SetActive(arg_70_0.countUI, False)

	arg_70_0.leaveUI = findTF(arg_70_0._tf, "pop/LeaveUI")

	onButton(arg_70_0, findTF(arg_70_0.leaveUI, "ad/btnOk"), function()
		arg_70_0.resumeGame()
		arg_70_0.onGameOver(), SFX_CANCEL)
	onButton(arg_70_0, findTF(arg_70_0.leaveUI, "ad/btnCancel"), function()
		arg_70_0.resumeGame(), SFX_CANCEL)
	SetActive(arg_70_0.leaveUI, False)

	arg_70_0.pauseUI = findTF(arg_70_0._tf, "pop/pauseUI")

	onButton(arg_70_0, findTF(arg_70_0.pauseUI, "ad/btnOk"), function()
		setActive(arg_70_0.pauseUI, False)
		arg_70_0.resumeGame(), SFX_CANCEL)
	SetActive(arg_70_0.pauseUI, False)

	arg_70_0.settlementUI = findTF(arg_70_0._tf, "pop/SettleMentUI")

	onButton(arg_70_0, findTF(arg_70_0.settlementUI, "ad/btnOver"), function()
		setActive(arg_70_0.settlementUI, False)
		arg_70_0.openMenuUI(), SFX_CANCEL)
	SetActive(arg_70_0.settlementUI, False)

	arg_70_0.menuUI = findTF(arg_70_0._tf, "pop/menuUI")

	local var_70_0 = ActivityConst.ISLAND_GAME_ID
	local var_70_1 = pg.activity_template[var_70_0].config_client.item_id

	arg_70_0.itemConfig = Item.getConfigData(var_70_1)

	LoadImageSpriteAsync(arg_70_0.itemConfig.icon, findTF(arg_70_0.menuUI, "item/img"), True)

	arg_70_0.hub_id = pg.activity_template[var_70_0].config_id

	onButton(arg_70_0, findTF(arg_70_0.menuUI, "item"), function()
		local var_77_0 = {
			mediator = IslandGameLimitMediator,
			viewComponent = IslandGameLimitLayer,
			data = {
				type = IslandGameLimitLayer.limit_type_catch
			}
		}

		arg_70_0.emit(BaseMiniGameMediator.OPEN_SUB_LAYER, var_77_0), SFX_CANCEL)
	onButton(arg_70_0, findTF(arg_70_0.menuUI, "btnBack"), function()
		arg_70_0.closeView(), SFX_CANCEL)
	onButton(arg_70_0, findTF(arg_70_0.menuUI, "btnStart"), function()
		setActive(arg_70_0.menuUI, False)
		arg_70_0.readyStart(), SFX_CANCEL)
	onButton(arg_70_0, findTF(arg_70_0.menuUI, "btnRule"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip[var_0_9].tip
		}), SFX_CANCEL)

	if not arg_70_0.handle:
		arg_70_0.handle = UpdateBeat.CreateListener(arg_70_0.Update, arg_70_0)

	UpdateBeat.AddListener(arg_70_0.handle)

def var_0_0.initGameUI(arg_81_0):
	arg_81_0.gameUI = findTF(arg_81_0._tf, "ui/gameUI")

	onButton(arg_81_0, findTF(arg_81_0.gameUI, "topRight/btnStop"), function()
		arg_81_0.stopGame()
		setActive(arg_81_0.pauseUI, True))
	onButton(arg_81_0, findTF(arg_81_0.gameUI, "btnLeave"), function()
		arg_81_0.stopGame()
		setActive(arg_81_0.leaveUI, True))

	arg_81_0.dragDelegate = GetOrAddComponent(arg_81_0.sceneTf, "EventTriggerListener")
	arg_81_0.dragDelegate.enabled = True

	arg_81_0.dragDelegate.AddPointDownFunc(function(arg_84_0, arg_84_1)
		if arg_81_0.boatController:
			arg_81_0.boatController.throw())

	arg_81_0.gameTimeS = findTF(arg_81_0.gameUI, "top/time/s")
	arg_81_0.scoreTf = findTF(arg_81_0.gameUI, "top/score")
	arg_81_0.boatController = var_0_56(arg_81_0.sceneTf, arg_81_0)
	arg_81_0.itemController = var_0_57(arg_81_0.sceneTf, arg_81_0.backSceneTf, arg_81_0.getGameUsedTimes(), arg_81_0)
	arg_81_0.catchController = var_0_58(arg_81_0.boatController, arg_81_0.itemController)
	arg_81_0.charController = var_0_59(arg_81_0.backSceneTf, arg_81_0)
	arg_81_0.sceneScoreTf = findTF(arg_81_0.sceneTf, "scoreTf")

	setActive(arg_81_0.sceneScoreTf, False)

def var_0_0.Update(arg_85_0):
	arg_85_0.AddDebugInput()

def var_0_0.AddDebugInput(arg_86_0):
	if arg_86_0.gameStop or arg_86_0.settlementFlag:
		return

	if IsUnityEditor:
		-- block empty

def var_0_0.updateMenuUI(arg_87_0):
	arg_87_0.itemNums = getProxy(MiniGameProxy).GetHubByHubId(arg_87_0.hub_id).count or 0

	setText(findTF(arg_87_0.menuUI, "item/num"), arg_87_0.itemNums)

def var_0_0.openMenuUI(arg_88_0):
	setActive(findTF(arg_88_0._tf, "scene_container"), False)
	setActive(findTF(arg_88_0.bgTf, "on"), True)
	setActive(arg_88_0.gameUI, False)
	setActive(arg_88_0.menuUI, True)
	arg_88_0.updateMenuUI()

def var_0_0.clearUI(arg_89_0):
	setActive(arg_89_0.sceneTf, False)
	setActive(arg_89_0.settlementUI, False)
	setActive(arg_89_0.countUI, False)
	setActive(arg_89_0.menuUI, False)
	setActive(arg_89_0.gameUI, False)

def var_0_0.readyStart(arg_90_0):
	setActive(arg_90_0.countUI, True)
	arg_90_0.countAnimator.Play("count")
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_2)

def var_0_0.getGameTimes(arg_91_0):
	return arg_91_0.GetMGHubData().count

def var_0_0.getGameUsedTimes(arg_92_0):
	return arg_92_0.GetMGHubData().usedtime

def var_0_0.getUltimate(arg_93_0):
	return arg_93_0.GetMGHubData().ultimate

def var_0_0.gameStart(arg_94_0):
	setActive(findTF(arg_94_0._tf, "scene_container"), True)
	setActive(findTF(arg_94_0.bgTf, "on"), False)
	setActive(arg_94_0.gameUI, True)

	arg_94_0.gameStartFlag = True
	arg_94_0.scoreNum = 0
	arg_94_0.playerPosIndex = 2
	arg_94_0.gameStepTime = 0
	arg_94_0.heart = 3
	arg_94_0.gameTime = var_0_7

	SetActive(arg_94_0.sceneScoreTf, False)

	if arg_94_0.boatController:
		arg_94_0.boatController.start()

	if arg_94_0.itemController:
		arg_94_0.itemController.start()

	if arg_94_0.catchController:
		arg_94_0.catchController.start()

	if arg_94_0.charController:
		arg_94_0.charController.start()

	arg_94_0.updateGameUI()
	arg_94_0.timerStart()

def var_0_0.transformColor(arg_95_0, arg_95_1):
	local var_95_0 = tonumber(string.sub(arg_95_1, 1, 2), 16)
	local var_95_1 = tonumber(string.sub(arg_95_1, 3, 4), 16)
	local var_95_2 = tonumber(string.sub(arg_95_1, 5, 6), 16)

	return Color.New(var_95_0 / 255, var_95_1 / 255, var_95_2 / 255)

def var_0_0.addScore(arg_96_0, arg_96_1, arg_96_2):
	if arg_96_1 and arg_96_1 > 0 or arg_96_2 and arg_96_2 > 0:
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_5)
	elif arg_96_1 and arg_96_1 < 0:
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_6)

	setActive(arg_96_0.sceneScoreTf, False)

	local var_96_0 = findTF(arg_96_0.sceneScoreTf, "img")
	local var_96_1 = GetComponent(var_96_0, typeof(Text))
	local var_96_2 = "6f1807"

	if arg_96_1:
		local var_96_3

		for iter_96_0 = 1, #var_0_47:
			if arg_96_1 and arg_96_1 >= var_0_47[iter_96_0].score:
				var_96_2 = var_0_47[iter_96_0].color
				var_96_3 = var_0_47[iter_96_0].font

				break

		local var_96_4 = arg_96_0.transformColor(var_96_2)

		arg_96_0.scoreNum = arg_96_0.scoreNum + arg_96_1

		local var_96_5 = arg_96_1 >= 0 and "+" or ""

		setText(var_96_0, var_96_5 .. arg_96_1)

		var_96_1.fontSize = var_96_3 or 40

		setTextColor(var_96_0, var_96_4)
	elif arg_96_2:
		local var_96_6 = arg_96_0.transformColor("66f2fb")

		var_96_1.fontSize = 40

		setTextColor(var_96_0, var_96_6)

		if arg_96_0.gameTime > 0:
			arg_96_0.gameTime = arg_96_0.gameTime + arg_96_2

		local var_96_7 = arg_96_2 > 0 and "+" or ""

		setText(var_96_0, var_96_7 .. arg_96_2 .. "s")

	setActive(arg_96_0.sceneScoreTf, True)

def var_0_0.onTimer(arg_97_0):
	arg_97_0.gameStep()

def var_0_0.gameStep(arg_98_0):
	arg_98_0.gameTime = arg_98_0.gameTime - Time.deltaTime
	arg_98_0.gameStepTime = arg_98_0.gameStepTime + Time.deltaTime

	if arg_98_0.boatController:
		arg_98_0.boatController.step()

	if arg_98_0.itemController:
		arg_98_0.itemController.step()

	if arg_98_0.catchController:
		arg_98_0.catchController.step()

	if arg_98_0.charController:
		arg_98_0.charController.step()

	if arg_98_0.gameTime < 0:
		arg_98_0.gameTime = 0

	arg_98_0.updateGameUI()

	if arg_98_0.gameTime <= 0:
		arg_98_0.onGameOver()

		return

def var_0_0.timerStart(arg_99_0):
	if not arg_99_0.timer.running:
		arg_99_0.timer.Start()

def var_0_0.timerStop(arg_100_0):
	if arg_100_0.timer.running:
		arg_100_0.timer.Stop()

def var_0_0.updateGameUI(arg_101_0):
	setText(arg_101_0.scoreTf, arg_101_0.scoreNum)
	setText(arg_101_0.gameTimeS, math.ceil(arg_101_0.gameTime))

def var_0_0.onGameOver(arg_102_0):
	if arg_102_0.settlementFlag:
		return

	arg_102_0.timerStop()

	arg_102_0.settlementFlag = True

	setActive(arg_102_0.clickMask, True)

	if arg_102_0.boatController:
		arg_102_0.boatController.gameOver()

	LeanTween.delayedCall(go(arg_102_0._tf), 2, System.Action(function()
		arg_102_0.settlementFlag = False
		arg_102_0.gameStartFlag = False

		setActive(arg_102_0.clickMask, False)
		arg_102_0.showSettlement()))

def var_0_0.showSettlement(arg_104_0):
	setActive(arg_104_0.settlementUI, True)
	GetComponent(findTF(arg_104_0.settlementUI, "ad"), typeof(Animator)).Play("settlement", -1, 0)

	local var_104_0 = arg_104_0.GetMGData().GetRuntimeData("elements")
	local var_104_1 = arg_104_0.scoreNum
	local var_104_2 = var_104_0 and #var_104_0 > 0 and var_104_0[1] or 0

	setActive(findTF(arg_104_0.settlementUI, "ad/new"), var_104_2 < var_104_1)

	if var_104_2 <= var_104_1:
		var_104_2 = var_104_1

		arg_104_0.StoreDataToServer({
			var_104_2
		})

	local var_104_3 = findTF(arg_104_0.settlementUI, "ad/highText")
	local var_104_4 = findTF(arg_104_0.settlementUI, "ad/currentText")

	setText(var_104_3, var_104_2)
	setText(var_104_4, var_104_1)

	if arg_104_0.getGameTimes() and arg_104_0.getGameTimes() > 0:
		arg_104_0.sendSuccessFlag = True

		arg_104_0.SendSuccess(0)

def var_0_0.resumeGame(arg_105_0):
	arg_105_0.gameStop = False

	setActive(arg_105_0.leaveUI, False)
	arg_105_0.timerStart()

def var_0_0.stopGame(arg_106_0):
	arg_106_0.gameStop = True

	arg_106_0.timerStop()

def var_0_0.onBackPressed(arg_107_0):
	if not arg_107_0.gameStartFlag:
		arg_107_0.emit(var_0_0.ON_BACK_PRESSED)
	else
		if arg_107_0.settlementFlag:
			return

		if isActive(arg_107_0.pauseUI):
			setActive(arg_107_0.pauseUI, False)

		arg_107_0.stopGame()
		setActive(arg_107_0.leaveUI, True)

def var_0_0.willExit(arg_108_0):
	if arg_108_0.handle:
		UpdateBeat.RemoveListener(arg_108_0.handle)

	if arg_108_0._tf and LeanTween.isTweening(go(arg_108_0._tf)):
		LeanTween.cancel(go(arg_108_0._tf))

	if arg_108_0.timer and arg_108_0.timer.running:
		arg_108_0.timer.Stop()

	Time.timeScale = 1
	arg_108_0.timer = None

return var_0_0
