local var_0_0 = class("CatchTreasureGameView", import("..BaseMiniGameView"))
local var_0_1 = "blueocean-image"
local var_0_2 = "event:/ui/ddldaoshu2"
local var_0_3 = "event:/ui/taosheng"
local var_0_4 = "event:/ui/zhuahuo"
local var_0_5 = "event:/ui/deshou"
local var_0_6 = "event:/ui/shibai"
local var_0_7 = 60
local var_0_8 = "ui/catchtreasuregameui_atlas"
local var_0_9 = "salvage_tips"
local var_0_10 = "event item done"
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
			repeated = true,
			type = var_0_31,
			amount = {
				8,
				10
			}
		},
		{
			repeated = true,
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
			repeated = true,
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
			repeated = true,
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
			repeated = true,
			type = var_0_29,
			amount = {
				3,
				3
			}
		},
		{
			repeated = true,
			type = var_0_30,
			amount = {
				2,
				2
			}
		},
		{
			repeated = true,
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
			repeated = true,
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
			repeated = false,
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
			repeated = false,
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
			repeated = false,
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
			repeated = false,
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
			repeated = true,
			type = var_0_31,
			amount = {
				8,
				10
			}
		},
		{
			repeated = true,
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
			repeated = true,
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
			repeated = true,
			type = var_0_29,
			amount = {
				0,
				0
			}
		},
		{
			repeated = true,
			type = var_0_30,
			amount = {
				2,
				2
			}
		},
		{
			repeated = true,
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
			repeated = true,
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
			repeated = true,
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
			repeated = true,
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
			repeated = false,
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
			repeated = false,
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
			repeated = false,
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
			repeated = false,
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
			repeated = true,
			type = var_0_31,
			amount = {
				8,
				10
			}
		},
		{
			repeated = true,
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
			repeated = true,
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
			repeated = true,
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
			repeated = true,
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
			repeated = true,
			type = var_0_29,
			amount = {
				1,
				1
			}
		},
		{
			repeated = true,
			type = var_0_30,
			amount = {
				2,
				2
			}
		},
		{
			repeated = true,
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
			repeated = true,
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
			repeated = true,
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
			repeated = true,
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
			repeated = false,
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
		score = 600,
		name = "watch",
		time = 20,
		catch_speed = 180,
		speed = 0,
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
				sync = true,
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
				sync = true,
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
		ctor = function(arg_2_0)
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

			GetComponent(findTF(arg_2_0._boatTf, "body/captain/img"), typeof(DftAniEvent)):SetEndEvent(function()
				if arg_2_0.inGoodAct then
					arg_2_0.inGoodAct = false
				end
			end)

			arg_2_0.marinerAnimator = GetComponent(findTF(arg_2_0._boatTf, "body/mariner/img"), typeof(Animator))
		end,
		start = function(arg_4_0)
			arg_4_0._hookTf.sizeDelta = Vector2(0, 1)
			arg_4_0.boatState = var_0_11
			arg_4_0.hookRotation = var_0_41
			arg_4_0.hookRotationSpeed = 0
			arg_4_0.hookTargetRotation = var_0_41
			arg_4_0.throwHook = false
			arg_4_0.inGoodAct = false

			if arg_4_0.catchItem then
				destroy(arg_4_0.catchItem.tf)

				arg_4_0.catchItem = nil
			end

			arg_4_0.marinerActTime = nil
			arg_4_0.marinerActName = nil

			arg_4_0:leaveItem()
		end,
		step = function(arg_5_0)
			if arg_5_0.boatState == var_0_11 then
				arg_5_0:checkChangeRotation()

				arg_5_0.hookRotation = arg_5_0.hookRotation + arg_5_0:getSpringRotation()
				arg_5_0._hookTf.localEulerAngles = Vector3(0, 0, arg_5_0.hookRotation)
			elseif arg_5_0.boatState == var_0_12 then
				if arg_5_0.throwHook then
					arg_5_0._hookTf.sizeDelta = Vector2(0, arg_5_0._hookTf.sizeDelta.y + var_0_39 * Time.deltaTime)

					local var_5_0 = math.cos(math.deg2Rad * math.abs(arg_5_0.hookRotation))

					if arg_5_0._hookTf.sizeDelta.y * var_5_0 > var_0_38 or arg_5_0._hookTf.sizeDelta.y > var_0_37 then
						arg_5_0.throwHook = false
					end
				else
					local var_5_1 = arg_5_0:hookBack()

					if not arg_5_0.catchItem and var_5_1 then
						arg_5_0.boatState = var_0_11
					elseif arg_5_0.catchItem then
						local var_5_2 = arg_5_0._hookContent.position
						local var_5_3 = arg_5_0._sceneContent:InverseTransformPoint(var_5_2)

						if (arg_5_0.catchItem.data.catch == var_0_17 or arg_5_0.catchItem.data.act == var_0_15) and var_5_3.y > var_0_45 then
							arg_5_0.boatState = var_0_13

							arg_5_0:leaveItem()
						elseif var_5_1 then
							arg_5_0.boatState = var_0_13

							arg_5_0:leaveItem()
						end
					end
				end
			elseif arg_5_0.boatState == var_0_13 then
				if not arg_5_0:hookBack() then
					return
				end

				if arg_5_0.inGoodAct then
					return
				end

				arg_5_0.boatState = var_0_11
			end

			if arg_5_0.boatState == var_0_12 and arg_5_0.throwHook then
				arg_5_0.hookAnimator:SetBool("hook", true)
				arg_5_0.hookMaskAnimator:SetBool("hook", true)
			else
				arg_5_0.hookAnimator:SetBool("hook", false)
				arg_5_0.hookMaskAnimator:SetBool("hook", false)
			end

			if arg_5_0.boatState == var_0_12 then
				if arg_5_0.throwHook then
					arg_5_0.captainAnimator:SetInteger("state", 4)
				else
					local var_5_4 = 1

					if arg_5_0.catchItem then
						var_5_4 = arg_5_0.catchItem.data.catch_speed >= 100 and 1 or arg_5_0.catchItem.data.catch_speed >= 50 and arg_5_0.catchItem.data.catch_speed <= 100 and 2 or 3
					end

					arg_5_0.captainAnimator:SetInteger("state", var_5_4)
				end
			else
				arg_5_0.captainAnimator:SetInteger("state", 0)
			end

			if not arg_5_0.marinerActTime then
				arg_5_0.marinerActTime = math.random(var_0_55[1], var_0_55[2])
				arg_5_0.marinerActName = var_0_54[math.random(1, #var_0_54)]
			elseif arg_5_0.marinerActTime <= 0 then
				arg_5_0.marinerAnimator:SetTrigger(arg_5_0.marinerActName)

				arg_5_0.marinerActTime = math.random(var_0_55[1], var_0_55[2])
				arg_5_0.marinerActName = var_0_54[math.random(1, #var_0_54)]
			else
				arg_5_0.marinerActTime = arg_5_0.marinerActTime - Time.deltaTime
			end
		end,
		hookBack = function(arg_6_0)
			if arg_6_0._hookTf.sizeDelta.y > 1 then
				local var_6_0 = var_0_40 * Time.deltaTime

				if arg_6_0.catchItem then
					var_6_0 = arg_6_0.catchItem.data.catch_speed * Time.deltaTime
				end

				arg_6_0._hookTf.sizeDelta = Vector2(0, arg_6_0._hookTf.sizeDelta.y - var_6_0)

				return false
			elseif arg_6_0._hookTf.sizeDelta.y < 1 then
				arg_6_0._hookTf.sizeDelta = Vector2(0, 1)

				return false
			end

			return true
		end,
		leaveItem = function(arg_7_0)
			if arg_7_0.catchItem then
				arg_7_0._event:emit(var_0_10, arg_7_0.catchItem, function()
					return
				end)

				arg_7_0.inGoodAct = true

				if arg_7_0.catchItem.data.good == var_0_19 then
					arg_7_0.captainAnimator:SetTrigger("happy")
					arg_7_0.marinerAnimator:SetTrigger("happy")
				elseif arg_7_0.catchItem.data.good == var_0_21 then
					arg_7_0.captainAnimator:SetTrigger("release")
				elseif arg_7_0.catchItem.data.good == var_0_20 then
					arg_7_0.captainAnimator:SetTrigger("surprise")
					arg_7_0.marinerAnimator:SetTrigger("surprise")
				elseif arg_7_0.catchItem.data.good == var_0_22 then
					arg_7_0.inGoodAct = false
				end

				arg_7_0.catchItem = nil
			end
		end,
		throw = function(arg_9_0)
			if arg_9_0.boatState ~= var_0_11 then
				return
			end

			pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_3)

			arg_9_0.throwHook = true
			arg_9_0.boatState = var_0_12
		end,
		setCatchItem = function(arg_10_0, arg_10_1)
			if arg_10_0.boatState == var_0_12 and arg_10_0.throwHook then
				arg_10_0.catchItem = arg_10_1
				arg_10_0.throwHook = false
				arg_10_1.tf.localScale = Vector3(math.sign(arg_10_1.tf.localScale.x), 1, 1)

				SetParent(arg_10_1.tf, arg_10_0._hookContent)

				arg_10_1.tf.anchoredPosition = Vector2(0, 0)

				pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_4)
			end
		end,
		getSpringRotation = function(arg_11_0)
			arg_11_0.hookRotationSpeed = arg_11_0.hookRotationSpeed + math.sign(arg_11_0.hookTargetRotation) * var_0_42

			if math.abs(arg_11_0.hookRotationSpeed) > var_0_43 then
				arg_11_0.hookRotationSpeed = var_0_43 * math.sign(arg_11_0.hookTargetRotation)
			end

			return arg_11_0.hookRotationSpeed * Time.deltaTime
		end,
		checkChangeRotation = function(arg_12_0)
			if arg_12_0.hookTargetRotation > 0 and arg_12_0.hookRotation > arg_12_0.hookTargetRotation then
				arg_12_0.hookTargetRotation = -arg_12_0.hookTargetRotation
			elseif arg_12_0.hookTargetRotation < 0 and arg_12_0.hookRotation < arg_12_0.hookTargetRotation then
				arg_12_0.hookTargetRotation = -arg_12_0.hookTargetRotation
			end
		end,
		inCatch = function(arg_13_0)
			return arg_13_0.boatState == var_0_12 and arg_13_0.throwHook
		end,
		getHookPosition = function(arg_14_0)
			return arg_14_0._hookCollider.position
		end,
		gameOver = function(arg_15_0)
			arg_15_0.captainAnimator:SetTrigger("end")
			arg_15_0.marinerAnimator:SetTrigger("end")
		end,
		destroy = function(arg_16_0)
			return
		end
	}

	var_1_0:ctor()

	return var_1_0
end

local function var_0_57(arg_17_0, arg_17_1, arg_17_2, arg_17_3)
	local var_17_0 = {
		ctor = function(arg_18_0)
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
			arg_18_0.items = {}
		end,
		getParentInversePos = function(arg_19_0, arg_19_1)
			local var_19_0 = arg_19_1.tf.position
			local var_19_1

			if arg_19_1.data.scene then
				if arg_19_1.data.scene == var_0_23 then
					var_19_1 = arg_19_0._backParentTf:InverseTransformPoint(var_19_0)
				else
					var_19_1 = arg_19_0._parentTf:InverseTransformPoint(var_19_0)
				end
			else
				var_19_1 = arg_19_0._parentTf:InverseTransformPoint(var_19_0)
			end

			return var_19_1
		end,
		addItemDone = function(arg_20_0, arg_20_1, arg_20_2)
			local var_20_0 = arg_20_0:getParentInversePos(arg_20_1)

			if arg_20_1.data.act == var_0_15 or arg_20_1.data.catch == var_0_17 then
				var_20_0.y = var_0_45
			end

			arg_20_1.tf.anchoredPosition = var_20_0

			arg_20_0:addItemParent(arg_20_1)

			arg_20_1.tf.localScale = Vector3(2.5 * math.sign(arg_20_1.tf.localScale.x), 2.5, 2.5)
			arg_20_1.tf.localEulerAngles = Vector3(0, 0, 0)
			arg_20_1.catchAble = false
			arg_20_1.targetRemove = true

			if arg_20_1.data.catch == var_0_16 then
				GetComponent(arg_20_1.tf, typeof(DftAniEvent)):SetEndEvent(function()
					arg_20_0:destroyItem(arg_20_1)
				end)
				GetComponent(arg_20_1.tf, typeof(Animator)):SetTrigger("catch")
			elseif arg_20_1.data.catch == var_0_17 then
				local var_20_1 = arg_20_1.data.leave_direct or 1

				arg_20_1.direct = var_20_1
				arg_20_1.targetX = var_20_1 * math.sign(arg_20_1.tf.localScale.x) == -1 and arg_20_1.data.move_range[2] or arg_20_1.data.move_range[1]

				GetComponent(arg_20_1.tf, typeof(DftAniEvent)):SetEndEvent(function()
					arg_20_1.moveAble = true
				end)

				arg_20_1.moveAble = false

				GetComponent(arg_20_1.tf, typeof(Animator)):SetTrigger("release")
				table.insert(arg_20_0.items, arg_20_1)
			end
		end,
		start = function(arg_23_0)
			arg_23_0:clearItems()
			arg_23_0:prepareItems()
			arg_23_0:setItemPosition()
		end,
		clearItems = function(arg_24_0)
			for iter_24_0 = #arg_24_0.items, 1, -1 do
				local var_24_0 = table.remove(arg_24_0.items, iter_24_0)

				arg_24_0:destroyItem(var_24_0)

				local var_24_1
			end

			arg_24_0.items = {}
		end,
		prepareItems = function(arg_25_0)
			local var_25_0 = var_0_35[math.random(1, #var_0_35)]

			for iter_25_0, iter_25_1 in pairs(var_25_0) do
				local var_25_1 = math.random(iter_25_1.amount[1], iter_25_1.amount[2])
				local var_25_2 = iter_25_1.type
				local var_25_3 = iter_25_1.repeated
				local var_25_4 = iter_25_1.name
				local var_25_5 = arg_25_0:getItemsByType(var_25_2, var_25_4)

				for iter_25_2 = 1, var_25_1 do
					local var_25_6

					if var_25_3 then
						var_25_6 = var_25_5[math.random(1, #var_25_5)]
					elseif #var_25_5 > 0 then
						var_25_6 = table.remove(var_25_5, math.random(1, #var_25_5))
					end

					if var_25_6 then
						local var_25_7 = arg_25_0:createItem(var_25_6)

						table.insert(arg_25_0.items, var_25_7)
					end
				end
			end
		end,
		getItemsByType = function(arg_26_0, arg_26_1, arg_26_2)
			local var_26_0 = {}

			for iter_26_0 = 1, #var_0_36 do
				if var_0_36[iter_26_0].type == arg_26_1 then
					if arg_26_2 then
						if table.contains(arg_26_2, var_0_36[iter_26_0].name) then
							table.insert(var_26_0, var_0_36[iter_26_0])
						end
					else
						table.insert(var_26_0, var_0_36[iter_26_0])
					end
				end
			end

			return var_26_0
		end,
		getItemDataByName = function(arg_27_0, arg_27_1)
			for iter_27_0 = 1, #var_0_36 do
				if var_0_36[iter_27_0].name == arg_27_1 then
					return var_0_36[iter_27_0]
				end
			end

			return nil
		end,
		createItem = function(arg_28_0, arg_28_1)
			local var_28_0 = {
				data = arg_28_1
			}

			var_28_0.tf = nil
			var_28_0.targetX = nil
			var_28_0.targetY = nil
			var_28_0.direct = arg_28_1.direct or 1
			var_28_0.moveAble = true
			var_28_0.catchAble = true
			var_28_0.targetRemove = false
			var_28_0.interaction = arg_28_1.interaction and true or false
			var_28_0.interactionName = nil
			var_28_0.interactionTime = nil
			var_28_0.animStateIndex = nil
			var_28_0.nextAnimTime = nil

			arg_28_0:instantiateItem(var_28_0)

			return var_28_0
		end,
		instantiateItem = function(arg_29_0, arg_29_1)
			local var_29_0

			if arg_29_1.data.scene == var_0_23 then
				var_29_0 = findTF(arg_29_0._backSceneTpls, arg_29_1.data.name)
			else
				var_29_0 = findTF(arg_29_0._sceneTpls, arg_29_1.data.name)
			end

			local var_29_1 = Instantiate(var_29_0)

			arg_29_1.tf = tf(var_29_1)

			setActive(arg_29_1.tf, true)
			arg_29_0:addItemParent(arg_29_1)
		end,
		addItemParent = function(arg_30_0, arg_30_1)
			if arg_30_1.data.scene then
				if arg_30_1.data.scene == var_0_23 then
					SetParent(arg_30_1.tf, arg_30_0._backParentTf)
				else
					SetParent(arg_30_1.tf, arg_30_0._parentTf)
				end
			else
				SetParent(arg_30_1.tf, arg_30_0._parentTf)
			end
		end,
		setItemPosition = function(arg_31_0)
			if not arg_31_0.items or #arg_31_0.items == 0 then
				return
			end

			local var_31_0 = arg_31_0:splitePositions(0, arg_31_0._createBounds[1])
			local var_31_1 = arg_31_0:splitePositions(0, arg_31_0._createBounds[2])
			local var_31_2 = arg_31_0:mixSplitePos(var_31_0, var_31_1)

			local function var_31_3(arg_32_0)
				if arg_32_0 then
					local var_32_0 = {}

					for iter_32_0 = 1, #var_31_2 do
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

						if var_32_3 <= var_32_7 and var_32_8 <= var_32_4 and var_32_5 <= var_32_9 and var_32_10 <= var_32_6 then
							table.insert(var_32_0, var_32_1)
						end
					end

					if #var_32_0 > 0 then
						return table.remove(var_31_2, var_32_0[math.random(1, #var_32_0)])
					end
				end

				if #var_31_2 > 0 then
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
				end
			end

			for iter_31_0 = 1, #arg_31_0.items do
				local var_31_4 = var_31_3(arg_31_0.items[iter_31_0].data.create_range)

				if var_31_4 then
					local var_31_5 = var_31_4[1][1] + math.random() * (var_31_4[1][2] - var_31_4[1][1]) / 2
					local var_31_6 = var_31_4[2][1] + math.random() * (var_31_4[2][2] - var_31_4[2][1]) / 2

					arg_31_0.items[iter_31_0].tf.anchoredPosition = Vector2(var_31_5, var_31_6)
				end
			end
		end,
		mixSplitePos = function(arg_33_0, arg_33_1, arg_33_2)
			local var_33_0 = {}

			for iter_33_0 = 1, #arg_33_1 do
				local var_33_1 = arg_33_1[iter_33_0]

				for iter_33_1 = 1, #arg_33_2 do
					local var_33_2 = arg_33_2[iter_33_1]

					table.insert(var_33_0, {
						var_33_1,
						var_33_2
					})
				end
			end

			return var_33_0
		end,
		splitePositions = function(arg_34_0, arg_34_1, arg_34_2)
			local var_34_0 = {}

			if not arg_34_1 or not arg_34_2 or arg_34_2 < arg_34_1 then
				return nil
			end

			local var_34_1 = (arg_34_2 - arg_34_1) / var_0_46

			for iter_34_0 = 1, var_34_1 do
				table.insert(var_34_0, {
					arg_34_1 + (iter_34_0 - 1) * var_0_46,
					arg_34_1 + iter_34_0 * var_0_46
				})
			end

			return var_34_0
		end,
		getItemByPos = function(arg_35_0, arg_35_1)
			local var_35_0 = arg_35_0:checkPosInCollider(arg_35_1)

			if var_35_0 then
				if var_35_0.data.catch_rule then
					local var_35_1 = GetComponent(var_35_0.tf, typeof(Animator)):GetInteger("state")
					local var_35_2 = var_35_0.data.catch_rule.state

					if table.contains(var_35_2, var_35_1) then
						arg_35_0:addItemDone(var_35_0)

						return (arg_35_0:createItem(arg_35_0:getItemDataByName(var_35_0.data.catch_rule.targetName)))
					end
				else
					return var_35_0
				end

				return var_35_0
			end

			return nil
		end,
		checkPosInCollider = function(arg_36_0, arg_36_1)
			local var_36_0 = {}
			local var_36_1 = arg_36_0._parentTf:InverseTransformPoint(arg_36_1.x, arg_36_1.y, arg_36_1.z)

			for iter_36_0 = 1, #arg_36_0.items do
				if arg_36_0.items[iter_36_0].data.catch ~= var_0_18 then
					local var_36_2 = arg_36_0.items[iter_36_0].tf

					if math.abs(var_36_1.x - var_36_2.anchoredPosition.x) < var_0_44 and math.abs(var_36_1.y - var_36_2.anchoredPosition.y) < var_0_44 and arg_36_0.items[iter_36_0].data.catch ~= var_0_18 and arg_36_0.items[iter_36_0].catchAble then
						table.insert(var_36_0, arg_36_0.items[iter_36_0])
					end
				end
			end

			for iter_36_1 = 1, #var_36_0 do
				local var_36_3 = findTF(var_36_0[iter_36_1].tf, "collider")

				if not var_36_3 then
					print("can not find collider by" .. var_36_0[iter_36_1].data.name)
				else
					local var_36_4 = var_36_3:InverseTransformPoint(arg_36_1.x, arg_36_1.y, arg_36_1.z)
					local var_36_5 = var_36_3.rect.xMin
					local var_36_6 = var_36_3.rect.yMin
					local var_36_7 = var_36_3.rect.width
					local var_36_8 = var_36_3.rect.height

					if arg_36_0:isPointInMatrix(Vector2(var_36_5, var_36_6 + var_36_8), Vector2(var_36_5 + var_36_7, var_36_6 + var_36_8), Vector2(var_36_5 + var_36_7, var_36_6), Vector2(var_36_5, var_36_6), var_36_4) then
						return arg_36_0:removeItem(var_36_0[iter_36_1])
					end
				end
			end

			return nil
		end,
		removeItem = function(arg_37_0, arg_37_1)
			for iter_37_0 = 1, #arg_37_0.items do
				if arg_37_0.items[iter_37_0] == arg_37_1 then
					return table.remove(arg_37_0.items, iter_37_0)
				end
			end
		end,
		getCross = function(arg_38_0, arg_38_1, arg_38_2, arg_38_3)
			return (arg_38_2.x - arg_38_1.x) * (arg_38_3.y - arg_38_1.y) - (arg_38_3.x - arg_38_1.x) * (arg_38_2.y - arg_38_1.y)
		end,
		isPointInMatrix = function(arg_39_0, arg_39_1, arg_39_2, arg_39_3, arg_39_4, arg_39_5)
			return arg_39_0:getCross(arg_39_1, arg_39_2, arg_39_5) * arg_39_0:getCross(arg_39_3, arg_39_4, arg_39_5) >= 0 and arg_39_0:getCross(arg_39_2, arg_39_3, arg_39_5) * arg_39_0:getCross(arg_39_4, arg_39_1, arg_39_5) >= 0
		end,
		step = function(arg_40_0)
			for iter_40_0 = #arg_40_0.items, 1, -1 do
				local var_40_0 = arg_40_0.items[iter_40_0]

				if var_40_0.data.act == var_0_15 and var_40_0.moveAble then
					if not var_40_0.targetX then
						local var_40_1 = var_40_0.data.move_range[1]
						local var_40_2 = var_40_0.data.move_range[2]

						if var_40_0.tf.anchoredPosition.x == var_40_1 then
							var_40_0.targetX = var_40_2
						elseif var_40_0.tf.anchoredPosition.x == var_40_2 then
							var_40_0.targetX = var_40_1
						else
							var_40_0.targetX = math.random() > 0.5 and var_40_1 or var_40_2
						end
					else
						local var_40_3 = math.sign(var_40_0.targetX - var_40_0.tf.anchoredPosition.x)
						local var_40_4 = var_40_0.targetRemove and var_40_0.data.release_speed or var_40_0.data.speed

						var_40_0.tf.localScale = Vector3(-1 * var_40_3 * var_40_0.direct * math.abs(var_40_0.tf.localScale.x), var_40_0.tf.localScale.y, var_40_0.tf.localScale.z)

						local var_40_5 = var_40_3 * var_40_4 * Time.deltaTime

						var_40_0.tf.anchoredPosition = Vector2(var_40_0.tf.anchoredPosition.x + var_40_5, var_40_0.tf.anchoredPosition.y)

						if var_40_3 == 1 and var_40_0.tf.anchoredPosition.x >= var_40_0.targetX or var_40_3 == -1 and var_40_0.tf.anchoredPosition.x <= var_40_0.targetX then
							var_40_0.tf.anchoredPosition = Vector2(var_40_0.targetX, var_40_0.tf.anchoredPosition.y)
							var_40_0.targetX = nil
						end
					end
				end

				if var_40_0.data.anim_data then
					local var_40_6 = var_40_0.data.anim_data.state_change
					local var_40_7 = var_40_0.data.anim_data.time

					if var_40_6 and var_40_7 then
						if not var_40_0.nextAnimTime then
							var_40_0.nextAnimTime = math.random(var_40_7[1], var_40_7[2])
							var_40_0.animStateIndex = 1
						elseif var_40_0.nextAnimTime <= 0 then
							GetComponent(var_40_0.tf, typeof(Animator)):SetInteger("state", var_40_6[var_40_0.animStateIndex])

							var_40_0.nextAnimTime = math.random(var_40_7[1], var_40_7[2])
							var_40_0.animStateIndex = var_40_0.animStateIndex + 1
							var_40_0.animStateIndex = var_40_0.animStateIndex > #var_40_6 and 1 or var_40_0.animStateIndex
						else
							var_40_0.nextAnimTime = var_40_0.nextAnimTime - Time.deltaTime
						end
					end
				end

				if var_40_0.interaction and not var_40_0.targetRemove then
					if not var_40_0.interactionTime then
						var_40_0.interactionTime = math.random() * (var_40_0.data.interaction.time[2] - var_40_0.data.interaction.time[1]) + var_40_0.data.interaction.time[1]
						var_40_0.interactionName = var_40_0.data.interaction.parame[math.random(1, #var_40_0.data.interaction.parame)]
					elseif var_40_0.interactionTime <= 0 then
						GetComponent(var_40_0.tf, typeof(Animator)):SetTrigger(var_40_0.interactionName)

						var_40_0.interactionTime = nil
						var_40_0.interactionName = nil
					else
						var_40_0.interactionTime = var_40_0.interactionTime - Time.deltaTime
					end
				end

				if var_40_0.targetRemove and not var_40_0.targetX then
					table.remove(arg_40_0.items, iter_40_0)
					arg_40_0:destroyItem(var_40_0)
				end
			end
		end,
		destroyItem = function(arg_41_0, arg_41_1)
			destroy(arg_41_1.tf)
		end,
		destroy = function(arg_42_0)
			return
		end
	}

	var_17_0:ctor()

	return var_17_0
end

local function var_0_58(arg_43_0, arg_43_1)
	local var_43_0 = {
		ctor = function(arg_44_0)
			arg_44_0._boatController = arg_43_0
			arg_44_0._itemController = arg_43_1
		end,
		start = function(arg_45_0)
			return
		end,
		step = function(arg_46_0)
			if arg_46_0._boatController:inCatch() then
				local var_46_0 = arg_46_0._boatController:getHookPosition()
				local var_46_1 = arg_46_0._itemController:getItemByPos(var_46_0)

				if var_46_1 then
					GetComponent(var_46_1.tf, typeof(Animator)):SetTrigger("hold")
					arg_46_0._boatController:setCatchItem(var_46_1)
				end
			end
		end,
		destroy = function(arg_47_0)
			return
		end
	}

	var_43_0:ctor()

	return var_43_0
end

local function var_0_59(arg_48_0, arg_48_1)
	local var_48_0 = {
		ctor = function(arg_49_0)
			arg_49_0._charTpls = findTF(arg_48_0, "charTpls")
			arg_49_0._content = findTF(arg_48_0, "charContainer/content")
			arg_49_0._event = arg_48_1
		end,
		start = function(arg_50_0)
			arg_50_0:clear()

			arg_50_0.chars = {}
			arg_50_0.nextTime = math.random(var_0_52[1], var_0_52[2])
			arg_50_0.showChars = Clone(var_0_53)
		end,
		step = function(arg_51_0)
			if arg_51_0.nextTime <= 0 and #arg_51_0.showChars > 0 then
				table.insert(arg_51_0.chars, arg_51_0:createChar())

				arg_51_0.nextTime = math.random(var_0_52[1], var_0_52[2])
			else
				arg_51_0.nextTime = arg_51_0.nextTime - Time.deltaTime
			end

			arg_51_0:setCharAction()

			for iter_51_0 = #arg_51_0.chars, 1, -1 do
				arg_51_0:stepChar(arg_51_0.chars[iter_51_0])

				if arg_51_0.chars[iter_51_0].removeFlag then
					arg_51_0:removeChar(table.remove(arg_51_0.chars, iter_51_0))
				end
			end
		end,
		stepChar = function(arg_52_0, arg_52_1)
			local var_52_0 = false

			if arg_52_1.posX then
				arg_52_1.tf.anchoredPosition = Vector2(arg_52_1.posX + (arg_52_1.offsetX or 0), 0)

				setActive(arg_52_1.tf, true)

				arg_52_1.posX = nil
				arg_52_1.offsetX = nil
			end

			if arg_52_1.moveToX then
				local var_52_1 = arg_52_1.moveToX + arg_52_1.offsetX
				local var_52_2 = arg_52_1.tf.anchoredPosition
				local var_52_3 = math.sign(var_52_1 - var_52_2.x)

				arg_52_1.tf.anchoredPosition = Vector3(var_52_2.x + var_52_3 * arg_52_1.speed, 0)

				local var_52_4 = math.sign(var_52_2.x - var_52_1)
				local var_52_5 = math.sign(arg_52_1.tf.anchoredPosition.x - var_52_1)

				if arg_52_1.tf.anchoredPosition.x == var_52_1 or var_52_4 ~= var_52_5 then
					arg_52_1.moveToX = nil
					arg_52_1.offsetX = nil
				else
					var_52_0 = true
				end
			end

			if arg_52_1.triggerName or arg_52_1.time then
				if arg_52_1.triggerName and arg_52_1.animator then
					arg_52_1.animator:SetTrigger(arg_52_1.triggerName)

					arg_52_1.triggerName = nil
				end

				arg_52_1.time = arg_52_1.time - Time.deltaTime

				if arg_52_1.triggerName == nil and arg_52_1.time <= 0 then
					arg_52_1.time = nil
				else
					var_52_0 = true
				end
			end

			arg_52_1.inAction = var_52_0
		end,
		getRandomMoveX = function(arg_53_0, arg_53_1, arg_53_2)
			return arg_53_1 + math.random(0, arg_53_2 - arg_53_1)
		end,
		removeChar = function(arg_54_0, arg_54_1)
			if arg_54_1.bindChars then
				arg_54_1.bindChars = {}
			end

			destroy(arg_54_1.tf)
		end,
		setCharAction = function(arg_55_0)
			for iter_55_0 = 1, #arg_55_0.chars do
				local var_55_0 = arg_55_0.chars[iter_55_0]

				if not var_55_0.currentActionInfo and #var_55_0.actionInfos > 0 and not var_55_0.inAction then
					if var_55_0.sync and var_55_0.bindIds and #var_55_0.bindIds > 0 then
						local var_55_1 = true

						for iter_55_1, iter_55_2 in ipairs(var_55_0.bindChars) do
							if iter_55_2.inAction or not iter_55_2.sync then
								var_55_1 = false
							end
						end

						if var_55_1 then
							var_55_0.currentActionInfo = table.remove(var_55_0.actionInfos, 1)

							for iter_55_3, iter_55_4 in ipairs(var_55_0.bindChars) do
								iter_55_4.sync = false
							end
						end
					elseif not var_55_0.sync then
						var_55_0.currentActionInfo = table.remove(var_55_0.actionInfos, 1)
					end
				end

				if var_55_0.currentActionInfo and not var_55_0.currentActionInfo.sync then
					arg_55_0:addCharAction(var_55_0)
				elseif var_55_0.currentActionInfo and var_55_0.currentActionInfo.sync and var_55_0.bindIds then
					arg_55_0:addCharAction(var_55_0)

					for iter_55_5, iter_55_6 in ipairs(var_55_0.bindChars) do
						if iter_55_6 and iter_55_6.currentActionInfo and iter_55_6.currentActionInfo.sync then
							arg_55_0:addBindCharAction(var_55_0, iter_55_6)
						end
					end
				elseif not var_55_0.currentActionInfo and #var_55_0.actionInfos == 0 and not var_55_0.inAction then
					var_55_0.removeFlag = true
				end
			end
		end,
		addBindCharAction = function(arg_56_0, arg_56_1, arg_56_2)
			if arg_56_2.currentActionInfo.type == var_0_49 then
				arg_56_2.moveToX = arg_56_1.moveToX
				arg_56_2.offsetX = arg_56_2.currentActionInfo.offsetX or 0
			elseif arg_56_2.currentActionInfo.type == var_0_48 then
				-- block empty
			elseif arg_56_2.currentActionInfo.type == var_0_50 then
				-- block empty
			end

			arg_56_2.sync = arg_56_2.currentActionInfo.sync
			arg_56_2.currentActionInfo = nil
			arg_56_2.inAction = true
		end,
		addCharAction = function(arg_57_0, arg_57_1)
			local var_57_0 = arg_57_1.currentActionInfo.type

			if var_57_0 == var_0_49 then
				local var_57_1

				if arg_57_1.currentActionInfo.moveToX then
					var_57_1 = arg_57_0:getRandomMoveX(arg_57_1.currentActionInfo.moveToX[1], arg_57_1.currentActionInfo.moveToX[2])
				end

				arg_57_1.moveToX = var_57_1 or 0
				arg_57_1.offsetX = arg_57_1.currentActionInfo.offsetX or 0
			elseif var_57_0 == var_0_48 then
				arg_57_1.posX = arg_57_1.currentActionInfo.posX or 0
				arg_57_1.offsetX = arg_57_1.currentActionInfo.offsetX or 0
			elseif var_57_0 == var_0_50 then
				arg_57_1.triggerName = arg_57_1.currentActionInfo.trigger
				arg_57_1.time = arg_57_1.currentActionInfo.time or 0
			end

			arg_57_1.sync = arg_57_1.currentActionInfo.sync
			arg_57_1.inAction = true
			arg_57_1.currentActionInfo = nil
		end,
		createChar = function(arg_58_0, arg_58_1)
			local var_58_0 = {}
			local var_58_1 = Clone(arg_58_1) or arg_58_0:getRandomData()

			if not var_58_1 then
				return
			end

			var_58_0.data = var_58_1
			var_58_0.id = var_58_1.id
			var_58_0.bindIds = var_58_1.bindIds
			var_58_0.bindChars = {}
			var_58_0.actionInfos = var_58_1.actions
			var_58_0.speed = var_58_1.speed
			var_58_0.tf = arg_58_0:getCharTf(var_58_1.tf)
			var_58_0.animator = GetComponent(findTF(var_58_0.tf, "anim"), typeof(Animator))
			var_58_0.dft = GetComponent(findTF(var_58_0.tf, "anim"), typeof(DftAniEvent))
			var_58_0.currentActionInfo = nil
			var_58_0.posX = nil
			var_58_0.moveToX = nil
			var_58_0.offsetX = nil
			var_58_0.triggerName = nil
			var_58_0.time = nil
			var_58_0.inAction = false
			var_58_0.removeFlag = false

			if var_58_0.bindIds then
				for iter_58_0 = 1, #var_58_0.bindIds do
					local var_58_2 = arg_58_0:createChar(arg_58_0:getCharDataById(var_58_0.bindIds[iter_58_0]))

					table.insert(arg_58_0.chars, var_58_2)
					table.insert(var_58_0.bindChars, var_58_2)
				end
			end

			return var_58_0
		end,
		getRandomData = function(arg_59_0)
			if arg_59_0.showChars and #arg_59_0.showChars > 0 then
				local var_59_0 = table.remove(arg_59_0.showChars, math.random(1, #arg_59_0.showChars))

				return arg_59_0:getCharDataById(var_59_0)
			end

			return nil
		end,
		getCharDataById = function(arg_60_0, arg_60_1)
			for iter_60_0, iter_60_1 in ipairs(var_0_51) do
				if iter_60_1.id == arg_60_1 then
					return Clone(iter_60_1)
				end
			end
		end,
		getCharTf = function(arg_61_0, arg_61_1)
			local var_61_0 = tf(instantiate(findTF(arg_61_0._charTpls, arg_61_1)))

			SetParent(var_61_0, arg_61_0._content)
			SetActive(var_61_0, false)

			return var_61_0
		end,
		clear = function(arg_62_0)
			if arg_62_0.chars then
				for iter_62_0 = #arg_62_0.chars, 1, -1 do
					arg_62_0:removeChar(table.remove(arg_62_0.chars, iter_62_0))
				end

				arg_62_0.chars = {}
			end
		end
	}

	var_48_0:ctor()

	return var_48_0
end

function var_0_0.getUIName(arg_63_0)
	return "CatchTreasureGameUI"
end

function var_0_0.getBGM(arg_64_0)
	return var_0_1
end

function var_0_0.didEnter(arg_65_0)
	arg_65_0:initEvent()
	arg_65_0:initData()
	arg_65_0:initUI()
	arg_65_0:initGameUI()
	arg_65_0:updateMenuUI()
	arg_65_0:openMenuUI()
end

function var_0_0.initEvent(arg_66_0)
	arg_66_0:bind(var_0_10, function(arg_67_0, arg_67_1, arg_67_2)
		if arg_66_0.itemController then
			arg_66_0.itemController:addItemDone(arg_67_1, arg_67_2)
		end

		arg_66_0:addScore(arg_67_1.data.score, arg_67_1.data.time)
	end)
end

function var_0_0.initData(arg_68_0)
	arg_68_0.dropData = pg.mini_game[arg_68_0:GetMGData().id].simple_config_data.drop

	local var_68_0 = Application.targetFrameRate or 60

	if var_68_0 > 60 then
		var_68_0 = 60
	end

	arg_68_0.timer = Timer.New(function()
		arg_68_0:onTimer()
	end, 1 / var_68_0, -1)
end

function var_0_0.initUI(arg_70_0)
	arg_70_0.backSceneTf = findTF(arg_70_0._tf, "scene_container/scene_background")
	arg_70_0.sceneTf = findTF(arg_70_0._tf, "scene_container/scene")
	arg_70_0.bgTf = findTF(arg_70_0._tf, "bg")
	arg_70_0.clickMask = findTF(arg_70_0._tf, "clickMask")
	arg_70_0.countUI = findTF(arg_70_0._tf, "pop/CountUI")
	arg_70_0.countAnimator = GetComponent(findTF(arg_70_0.countUI, "count"), typeof(Animator))
	arg_70_0.countDft = GetOrAddComponent(findTF(arg_70_0.countUI, "count"), typeof(DftAniEvent))

	arg_70_0.countDft:SetTriggerEvent(function()
		return
	end)
	arg_70_0.countDft:SetEndEvent(function()
		setActive(arg_70_0.countUI, false)
		arg_70_0:gameStart()
	end)
	SetActive(arg_70_0.countUI, false)

	arg_70_0.leaveUI = findTF(arg_70_0._tf, "pop/LeaveUI")

	onButton(arg_70_0, findTF(arg_70_0.leaveUI, "ad/btnOk"), function()
		arg_70_0:resumeGame()
		arg_70_0:onGameOver()
	end, SFX_CANCEL)
	onButton(arg_70_0, findTF(arg_70_0.leaveUI, "ad/btnCancel"), function()
		arg_70_0:resumeGame()
	end, SFX_CANCEL)
	SetActive(arg_70_0.leaveUI, false)

	arg_70_0.pauseUI = findTF(arg_70_0._tf, "pop/pauseUI")

	onButton(arg_70_0, findTF(arg_70_0.pauseUI, "ad/btnOk"), function()
		setActive(arg_70_0.pauseUI, false)
		arg_70_0:resumeGame()
	end, SFX_CANCEL)
	SetActive(arg_70_0.pauseUI, false)

	arg_70_0.settlementUI = findTF(arg_70_0._tf, "pop/SettleMentUI")

	onButton(arg_70_0, findTF(arg_70_0.settlementUI, "ad/btnOver"), function()
		setActive(arg_70_0.settlementUI, false)
		arg_70_0:openMenuUI()
	end, SFX_CANCEL)
	SetActive(arg_70_0.settlementUI, false)

	arg_70_0.menuUI = findTF(arg_70_0._tf, "pop/menuUI")
	arg_70_0.battleScrollRect = GetComponent(findTF(arg_70_0.menuUI, "battList"), typeof(ScrollRect))
	arg_70_0.titleDesc = findTF(arg_70_0.menuUI, "desc")

	GetComponent(arg_70_0.titleDesc, typeof(Image)):SetNativeSize()

	arg_70_0.totalTimes = arg_70_0:getGameTotalTime()

	local var_70_0 = arg_70_0:getGameUsedTimes() - 4 < 0 and 0 or arg_70_0:getGameUsedTimes() - 4

	scrollTo(arg_70_0.battleScrollRect, 0, 1 - var_70_0 / (arg_70_0.totalTimes - 4))
	onButton(arg_70_0, findTF(arg_70_0.menuUI, "rightPanelBg/arrowUp"), function()
		local var_77_0 = arg_70_0.battleScrollRect.normalizedPosition.y + 1 / (arg_70_0.totalTimes - 4)

		if var_77_0 > 1 then
			var_77_0 = 1
		end

		scrollTo(arg_70_0.battleScrollRect, 0, var_77_0)
	end, SFX_CANCEL)
	onButton(arg_70_0, findTF(arg_70_0.menuUI, "rightPanelBg/arrowDown"), function()
		local var_78_0 = arg_70_0.battleScrollRect.normalizedPosition.y - 1 / (arg_70_0.totalTimes - 4)

		if var_78_0 < 0 then
			var_78_0 = 0
		end

		scrollTo(arg_70_0.battleScrollRect, 0, var_78_0)
	end, SFX_CANCEL)
	onButton(arg_70_0, findTF(arg_70_0.menuUI, "btnBack"), function()
		arg_70_0:closeView()
	end, SFX_CANCEL)
	onButton(arg_70_0, findTF(arg_70_0.menuUI, "btnRule"), function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip[var_0_9].tip
		})
	end, SFX_CANCEL)
	onButton(arg_70_0, findTF(arg_70_0.menuUI, "btnStart"), function()
		setActive(arg_70_0.menuUI, false)
		arg_70_0:readyStart()
	end, SFX_CANCEL)

	local var_70_1 = findTF(arg_70_0.menuUI, "tplBattleItem")

	arg_70_0.battleItems = {}
	arg_70_0.dropItems = {}

	for iter_70_0 = 1, 7 do
		local var_70_2 = tf(instantiate(var_70_1))

		var_70_2.name = "battleItem_" .. iter_70_0

		setParent(var_70_2, findTF(arg_70_0.menuUI, "battList/Viewport/Content"))

		local var_70_3 = iter_70_0

		GetSpriteFromAtlasAsync(var_0_8, "buttomDesc" .. var_70_3, function(arg_82_0)
			setImageSprite(findTF(var_70_2, "state_open/buttomDesc"), arg_82_0, true)
			setImageSprite(findTF(var_70_2, "state_clear/buttomDesc"), arg_82_0, true)
			setImageSprite(findTF(var_70_2, "state_current/buttomDesc"), arg_82_0, true)
			setImageSprite(findTF(var_70_2, "state_closed/buttomDesc"), arg_82_0, true)
		end)

		local var_70_4 = findTF(var_70_2, "icon")
		local var_70_5 = {
			type = arg_70_0.dropData[iter_70_0][1],
			id = arg_70_0.dropData[iter_70_0][2],
			count = arg_70_0.dropData[iter_70_0][3]
		}

		updateDrop(var_70_4, var_70_5)
		onButton(arg_70_0, var_70_4, function()
			arg_70_0:emit(BaseUI.ON_DROP, var_70_5)
		end, SFX_PANEL)
		table.insert(arg_70_0.dropItems, var_70_4)
		setActive(var_70_2, true)
		table.insert(arg_70_0.battleItems, var_70_2)
	end

	if not arg_70_0.handle then
		arg_70_0.handle = UpdateBeat:CreateListener(arg_70_0.Update, arg_70_0)
	end

	UpdateBeat:AddListener(arg_70_0.handle)
end

function var_0_0.initGameUI(arg_84_0)
	arg_84_0.gameUI = findTF(arg_84_0._tf, "ui/gameUI")

	onButton(arg_84_0, findTF(arg_84_0.gameUI, "topRight/btnStop"), function()
		arg_84_0:stopGame()
		setActive(arg_84_0.pauseUI, true)
	end)
	onButton(arg_84_0, findTF(arg_84_0.gameUI, "btnLeave"), function()
		arg_84_0:stopGame()
		setActive(arg_84_0.leaveUI, true)
	end)

	arg_84_0.dragDelegate = GetOrAddComponent(arg_84_0.sceneTf, "EventTriggerListener")
	arg_84_0.dragDelegate.enabled = true

	arg_84_0.dragDelegate:AddPointDownFunc(function(arg_87_0, arg_87_1)
		if arg_84_0.boatController then
			arg_84_0.boatController:throw()
		end
	end)

	arg_84_0.gameTimeS = findTF(arg_84_0.gameUI, "top/time/s")
	arg_84_0.scoreTf = findTF(arg_84_0.gameUI, "top/score")
	arg_84_0.boatController = var_0_56(arg_84_0.sceneTf, arg_84_0)
	arg_84_0.itemController = var_0_57(arg_84_0.sceneTf, arg_84_0.backSceneTf, arg_84_0:getGameUsedTimes(), arg_84_0)
	arg_84_0.catchController = var_0_58(arg_84_0.boatController, arg_84_0.itemController)
	arg_84_0.charController = var_0_59(arg_84_0.backSceneTf, arg_84_0)
	arg_84_0.sceneScoreTf = findTF(arg_84_0.sceneTf, "scoreTf")

	setActive(arg_84_0.sceneScoreTf, false)
end

function var_0_0.Update(arg_88_0)
	arg_88_0:AddDebugInput()
end

function var_0_0.AddDebugInput(arg_89_0)
	if arg_89_0.gameStop or arg_89_0.settlementFlag then
		return
	end

	if IsUnityEditor then
		-- block empty
	end
end

function var_0_0.updateMenuUI(arg_90_0)
	local var_90_0 = arg_90_0:getGameUsedTimes()
	local var_90_1 = arg_90_0:getGameTimes()

	for iter_90_0 = 1, #arg_90_0.battleItems do
		setActive(findTF(arg_90_0.battleItems[iter_90_0], "state_open"), false)
		setActive(findTF(arg_90_0.battleItems[iter_90_0], "state_closed"), false)
		setActive(findTF(arg_90_0.battleItems[iter_90_0], "state_clear"), false)
		setActive(findTF(arg_90_0.battleItems[iter_90_0], "state_current"), false)

		if iter_90_0 <= var_90_0 then
			setActive(findTF(arg_90_0.battleItems[iter_90_0], "state_clear"), true)
			SetParent(arg_90_0.dropItems[iter_90_0], findTF(arg_90_0.battleItems[iter_90_0], "state_clear/icon"))
			setActive(arg_90_0.dropItems[iter_90_0], true)

			arg_90_0.dropItems[iter_90_0].anchoredPosition = Vector2(0, 0)
		elseif iter_90_0 == var_90_0 + 1 and var_90_1 >= 1 then
			setActive(findTF(arg_90_0.battleItems[iter_90_0], "state_current"), true)
			SetParent(arg_90_0.dropItems[iter_90_0], findTF(arg_90_0.battleItems[iter_90_0], "state_current/icon"))
			setActive(arg_90_0.dropItems[iter_90_0], true)

			arg_90_0.dropItems[iter_90_0].anchoredPosition = Vector2(0, 0)
		elseif var_90_0 < iter_90_0 and iter_90_0 <= var_90_0 + var_90_1 then
			setActive(findTF(arg_90_0.battleItems[iter_90_0], "state_open"), true)
			SetParent(arg_90_0.dropItems[iter_90_0], findTF(arg_90_0.battleItems[iter_90_0], "state_open/icon"))
			setActive(arg_90_0.dropItems[iter_90_0], true)

			arg_90_0.dropItems[iter_90_0].anchoredPosition = Vector2(0, 0)
		else
			setActive(findTF(arg_90_0.battleItems[iter_90_0], "state_closed"), true)
			setActive(arg_90_0.dropItems[iter_90_0], false)
		end
	end

	arg_90_0.totalTimes = arg_90_0:getGameTotalTime()

	local var_90_2 = 1 - (arg_90_0:getGameUsedTimes() - 3 < 0 and 0 or arg_90_0:getGameUsedTimes() - 3) / (arg_90_0.totalTimes - 4)

	if var_90_2 > 1 then
		var_90_2 = 1
	end

	scrollTo(arg_90_0.battleScrollRect, 0, var_90_2)
	setActive(findTF(arg_90_0.menuUI, "btnStart/tip"), var_90_1 > 0)
	arg_90_0:CheckGet()
end

function var_0_0.CheckGet(arg_91_0)
	setActive(findTF(arg_91_0.menuUI, "got"), false)

	if arg_91_0:getUltimate() and arg_91_0:getUltimate() ~= 0 then
		setActive(findTF(arg_91_0.menuUI, "got"), true)
	end

	if arg_91_0:getUltimate() == 0 then
		if arg_91_0:getGameTotalTime() > arg_91_0:getGameUsedTimes() then
			return
		end

		pg.m02:sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = arg_91_0:GetMGHubData().id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})
		setActive(findTF(arg_91_0.menuUI, "got"), true)
	end
end

function var_0_0.openMenuUI(arg_92_0)
	setActive(findTF(arg_92_0._tf, "scene_container"), false)
	setActive(findTF(arg_92_0.bgTf, "on"), true)
	setActive(arg_92_0.gameUI, false)
	setActive(arg_92_0.menuUI, true)
	arg_92_0:updateMenuUI()
end

function var_0_0.clearUI(arg_93_0)
	setActive(arg_93_0.sceneTf, false)
	setActive(arg_93_0.settlementUI, false)
	setActive(arg_93_0.countUI, false)
	setActive(arg_93_0.menuUI, false)
	setActive(arg_93_0.gameUI, false)
end

function var_0_0.readyStart(arg_94_0)
	setActive(arg_94_0.countUI, true)
	arg_94_0.countAnimator:Play("count")
	pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_2)
end

function var_0_0.getGameTimes(arg_95_0)
	return arg_95_0:GetMGHubData().count
end

function var_0_0.getGameUsedTimes(arg_96_0)
	return arg_96_0:GetMGHubData().usedtime
end

function var_0_0.getUltimate(arg_97_0)
	return arg_97_0:GetMGHubData().ultimate
end

function var_0_0.getGameTotalTime(arg_98_0)
	return (arg_98_0:GetMGHubData():getConfig("reward_need"))
end

function var_0_0.gameStart(arg_99_0)
	setActive(findTF(arg_99_0._tf, "scene_container"), true)
	setActive(findTF(arg_99_0.bgTf, "on"), false)
	setActive(arg_99_0.gameUI, true)

	arg_99_0.gameStartFlag = true
	arg_99_0.scoreNum = 0
	arg_99_0.playerPosIndex = 2
	arg_99_0.gameStepTime = 0
	arg_99_0.heart = 3
	arg_99_0.gameTime = var_0_7

	SetActive(arg_99_0.sceneScoreTf, false)

	if arg_99_0.boatController then
		arg_99_0.boatController:start()
	end

	if arg_99_0.itemController then
		arg_99_0.itemController:start()
	end

	if arg_99_0.catchController then
		arg_99_0.catchController:start()
	end

	if arg_99_0.charController then
		arg_99_0.charController:start()
	end

	arg_99_0:updateGameUI()
	arg_99_0:timerStart()
end

function var_0_0.transformColor(arg_100_0, arg_100_1)
	local var_100_0 = tonumber(string.sub(arg_100_1, 1, 2), 16)
	local var_100_1 = tonumber(string.sub(arg_100_1, 3, 4), 16)
	local var_100_2 = tonumber(string.sub(arg_100_1, 5, 6), 16)

	return Color.New(var_100_0 / 255, var_100_1 / 255, var_100_2 / 255)
end

function var_0_0.addScore(arg_101_0, arg_101_1, arg_101_2)
	if arg_101_1 and arg_101_1 > 0 or arg_101_2 and arg_101_2 > 0 then
		pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_5)
	elseif arg_101_1 and arg_101_1 < 0 then
		pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_6)
	end

	setActive(arg_101_0.sceneScoreTf, false)

	local var_101_0 = findTF(arg_101_0.sceneScoreTf, "img")
	local var_101_1 = GetComponent(var_101_0, typeof(Text))
	local var_101_2 = "6f1807"

	if arg_101_1 then
		local var_101_3

		for iter_101_0 = 1, #var_0_47 do
			if arg_101_1 and arg_101_1 >= var_0_47[iter_101_0].score then
				var_101_2 = var_0_47[iter_101_0].color
				var_101_3 = var_0_47[iter_101_0].font

				break
			end
		end

		local var_101_4 = arg_101_0:transformColor(var_101_2)

		arg_101_0.scoreNum = arg_101_0.scoreNum + arg_101_1

		local var_101_5 = arg_101_1 >= 0 and "+" or ""

		setText(var_101_0, var_101_5 .. arg_101_1)

		var_101_1.fontSize = var_101_3 or 40

		setTextColor(var_101_0, var_101_4)
	elseif arg_101_2 then
		local var_101_6 = arg_101_0:transformColor("66f2fb")

		var_101_1.fontSize = 40

		setTextColor(var_101_0, var_101_6)

		if arg_101_0.gameTime > 0 then
			arg_101_0.gameTime = arg_101_0.gameTime + arg_101_2
		end

		local var_101_7 = arg_101_2 > 0 and "+" or ""

		setText(var_101_0, var_101_7 .. arg_101_2 .. "s")
	end

	setActive(arg_101_0.sceneScoreTf, true)
end

function var_0_0.onTimer(arg_102_0)
	arg_102_0:gameStep()
end

function var_0_0.gameStep(arg_103_0)
	arg_103_0.gameTime = arg_103_0.gameTime - Time.deltaTime
	arg_103_0.gameStepTime = arg_103_0.gameStepTime + Time.deltaTime

	if arg_103_0.boatController then
		arg_103_0.boatController:step()
	end

	if arg_103_0.itemController then
		arg_103_0.itemController:step()
	end

	if arg_103_0.catchController then
		arg_103_0.catchController:step()
	end

	if arg_103_0.charController then
		arg_103_0.charController:step()
	end

	if arg_103_0.gameTime < 0 then
		arg_103_0.gameTime = 0
	end

	arg_103_0:updateGameUI()

	if arg_103_0.gameTime <= 0 then
		arg_103_0:onGameOver()

		return
	end
end

function var_0_0.timerStart(arg_104_0)
	if not arg_104_0.timer.running then
		arg_104_0.timer:Start()
	end
end

function var_0_0.timerStop(arg_105_0)
	if arg_105_0.timer.running then
		arg_105_0.timer:Stop()
	end
end

function var_0_0.updateGameUI(arg_106_0)
	setText(arg_106_0.scoreTf, arg_106_0.scoreNum)
	setText(arg_106_0.gameTimeS, math.ceil(arg_106_0.gameTime))
end

function var_0_0.onGameOver(arg_107_0)
	if arg_107_0.settlementFlag then
		return
	end

	arg_107_0:timerStop()

	arg_107_0.settlementFlag = true

	setActive(arg_107_0.clickMask, true)

	if arg_107_0.boatController then
		arg_107_0.boatController:gameOver()
	end

	LeanTween.delayedCall(go(arg_107_0._tf), 2, System.Action(function()
		arg_107_0.settlementFlag = false
		arg_107_0.gameStartFlag = false

		setActive(arg_107_0.clickMask, false)
		arg_107_0:showSettlement()
	end))
end

function var_0_0.showSettlement(arg_109_0)
	setActive(arg_109_0.settlementUI, true)
	GetComponent(findTF(arg_109_0.settlementUI, "ad"), typeof(Animator)):Play("settlement", -1, 0)

	local var_109_0 = arg_109_0:GetMGData():GetRuntimeData("elements")
	local var_109_1 = arg_109_0.scoreNum
	local var_109_2 = var_109_0 and #var_109_0 > 0 and var_109_0[1] or 0

	setActive(findTF(arg_109_0.settlementUI, "ad/new"), var_109_2 < var_109_1)

	if var_109_2 <= var_109_1 then
		var_109_2 = var_109_1

		arg_109_0:StoreDataToServer({
			var_109_2
		})
	end

	local var_109_3 = findTF(arg_109_0.settlementUI, "ad/highText")
	local var_109_4 = findTF(arg_109_0.settlementUI, "ad/currentText")

	setText(var_109_3, var_109_2)
	setText(var_109_4, var_109_1)

	if arg_109_0:getGameTimes() and arg_109_0:getGameTimes() > 0 then
		arg_109_0.sendSuccessFlag = true

		arg_109_0:SendSuccess(0)
	end
end

function var_0_0.resumeGame(arg_110_0)
	arg_110_0.gameStop = false

	setActive(arg_110_0.leaveUI, false)
	arg_110_0:timerStart()
end

function var_0_0.stopGame(arg_111_0)
	arg_111_0.gameStop = true

	arg_111_0:timerStop()
end

function var_0_0.onBackPressed(arg_112_0)
	if not arg_112_0.gameStartFlag then
		arg_112_0:emit(var_0_0.ON_BACK_PRESSED)
	else
		if arg_112_0.settlementFlag then
			return
		end

		if isActive(arg_112_0.pauseUI) then
			setActive(arg_112_0.pauseUI, false)
		end

		arg_112_0:stopGame()
		setActive(arg_112_0.leaveUI, true)
	end
end

function var_0_0.willExit(arg_113_0)
	if arg_113_0.handle then
		UpdateBeat:RemoveListener(arg_113_0.handle)
	end

	if arg_113_0._tf and LeanTween.isTweening(go(arg_113_0._tf)) then
		LeanTween.cancel(go(arg_113_0._tf))
	end

	if arg_113_0.timer and arg_113_0.timer.running then
		arg_113_0.timer:Stop()
	end

	Time.timeScale = 1
	arg_113_0.timer = nil
end

return var_0_0
