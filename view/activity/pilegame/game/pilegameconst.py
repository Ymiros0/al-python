local var_0_0 = class("PileGameConst")

var_0_0.INDEX_WIDTH = 150
var_0_0.SAFE_INDEX_WIDTH = 45
var_0_0.DEATH_INDEX_WIDTH = 87
var_0_0.ITEM_PIVOT = Vector2(0.5, 0)
var_0_0.GROUND_SIZE = Vector2(1300, 20)
var_0_0.GROUND_PIVOT = Vector2(0.5, 1)
var_0_0.RATIO = 2
var_0_0.START_Y = 150
var_0_0.MAX_SLIDE_DISTANCE = var_0_0.INDEX_WIDTH * var_0_0.RATIO
var_0_0.SAFE_LINE_DISTANCE = var_0_0.SAFE_INDEX_WIDTH * var_0_0.RATIO
var_0_0.DEATH_LINE_DISTANCE = var_0_0.DEATH_INDEX_WIDTH * var_0_0.RATIO
var_0_0.SLIDE_SPEED = 150
var_0_0.SLIDE_GROWTH = {
	10,
	0.23
}
var_0_0.DROP_SPEED = 600
var_0_0.SINK_LEVEL = 4
var_0_0.MAX_FAILED_CNT = 3
var_0_0.LEVEL_TO_HAPPY_ANIM = 10
var_0_0.SINK_TIME = 0.01
var_0_0.SHAKE_DIS = 5
var_0_0.SHAKE_SPEED = 10
var_0_0.SHAKE_DIS_RATIO = 0.02
var_0_0.PLAY_SPE_ACTION_TIME = 5
var_0_0.BAN_OP_TIME = 1
var_0_0.DEBUG = False
var_0_0.Prefabs = {
	{
		speActionCount = 1,
		name = "abercrombie_N",
		boundary = {
			7.7,
			0,
			105,
			129.6
		},
		size = {
			157.82,
			139.22
		}
	},
	{
		speActionCount = 0,
		name = "abercrombie_R",
		boundary = {
			2.77,
			3.6,
			100,
			131.5
		},
		size = {
			156.9,
			138.8
		}
	},
	{
		speActionCount = 0,
		name = "abercrombie_SR",
		boundary = {
			2.7,
			3.6,
			100,
			131.5
		},
		size = {
			156.9,
			137.5
		}
	},
	{
		speActionCount = 0,
		name = "abercrombie_SRR",
		boundary = {
			2.7,
			3.6,
			100,
			131.5
		},
		size = {
			156.9,
			138.8
		}
	},
	{
		speActionCount = 0,
		name = "abercrombie_SRR_1",
		boundary = {
			2.7,
			3.6,
			100,
			131.5
		},
		size = {
			156.9,
			138.8
		}
	},
	{
		speActionCount = 0,
		name = "abercrombie_SRR_2",
		boundary = {
			2.7,
			3.6,
			100,
			131.5
		},
		size = {
			156.9,
			138.8
		}
	},
	{
		speActionCount = 0,
		name = "abercrombie_UR",
		boundary = {
			2.66,
			2.18,
			100,
			139.45
		},
		size = {
			160.9,
			143.8
		}
	},
	{
		speActionCount = 1,
		name = "antenna",
		boundary = {
			0,
			-0.49,
			120,
			85.37
		},
		size = {
			161.1,
			94.86
		}
	},
	{
		speActionCount = 1,
		name = "enterprise",
		boundary = {
			0,
			0,
			120,
			91.6
		},
		size = {
			159.2,
			101.48
		}
	},
	{
		speActionCount = 2,
		name = "formidable",
		boundary = {
			0,
			0,
			120,
			80.06
		},
		size = {
			168.98,
			88.96
		}
	},
	{
		speActionCount = 1,
		name = "hammann",
		boundary = {
			0,
			0,
			120,
			97.54
		},
		size = {
			151.45,
			97.54
		}
	},
	{
		speActionCount = 3,
		name = "illustrious",
		boundary = {
			0,
			0,
			110,
			96.02
		},
		size = {
			159.05,
			105.61
		}
	},
	{
		speActionCount = 2,
		name = "justice",
		boundary = {
			2.49,
			2.12,
			74,
			112.22
		},
		size = {
			163.87,
			116.46
		}
	},
	{
		speActionCount = 2,
		name = "laffey",
		boundary = {
			1,
			0.5,
			100,
			101
		},
		size = {
			168.86,
			110.03
		}
	},
	{
		speActionCount = 2,
		name = "mutsuki",
		boundary = {
			2.99,
			0,
			110,
			88.04
		},
		size = {
			152.91,
			96.5
		}
	},
	{
		speActionCount = 0,
		name = "portland",
		boundary = {
			0,
			-0.5,
			110,
			114.95
		},
		size = {
			164.55,
			124.3
		}
	},
	{
		speActionCount = 1,
		name = "pound",
		boundary = {
			2.99,
			0,
			96.02,
			84.06
		},
		size = {
			174.7,
			93.53
		}
	},
	{
		speActionCount = 2,
		name = "shiratsuyu",
		boundary = {
			0,
			2.6,
			120,
			87.9
		},
		size = {
			177.1,
			93.1
		}
	},
	{
		speActionCount = 2,
		name = "soup",
		boundary = {
			0,
			-2.5,
			110,
			89.8
		},
		size = {
			130.4,
			94.8
		}
	},
	{
		speActionCount = 1,
		name = "unicorn",
		boundary = {
			4,
			-2.5,
			110,
			87.6
		},
		size = {
			159.8,
			92.7
		}
	}
}
var_0_0.HEAD = {
	speActionCount = 0,
	name = "abercrombie_N",
	boundary = {
		3.15,
		0,
		78.29,
		103
	},
	size = {
		125,
		113
	}
}

return var_0_0
