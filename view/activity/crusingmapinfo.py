local var_0_0 = class("CrusingMapInfo")

var_0_0.MapInfo = {
	CrusingMap_0 = {
		all = 1260,
		frame = {
			[0] = 0,
			[90] = 1080,
			[100] = 1260,
			[95] = 1185
		}
	},
	CrusingMap_1 = {
		all = 410,
		frame = {
			[0] = 0,
			None,
			5,
			[40] = 155,
			[63] = 267,
			[62] = 261,
			[70] = 311,
			[74] = 340,
			[50] = 200,
			[54] = 214,
			[90] = 391,
			[82] = 369,
			[60] = 240,
			[10] = 40,
			[100] = 410,
			[30] = 120,
			[80] = 362
		}
	},
	CrusingMap_2 = {
		all = 900,
		frame = {
			[0] = 410,
			[50] = 606,
			[40] = 570,
			[100] = 860,
			[70] = 716,
			[60] = 664,
			[20] = 490,
			[80] = 772,
			[90] = 812,
			[10] = 450,
			[30] = 530
		}
	}
}
var_0_0.VersionInfo = {
	map_202212 = "CrusingMap_1",
	map_202308 = "CrusingMap_2",
	map_202208 = "CrusingMap_1",
	map_202312 = "CrusingMap_1",
	map_202306 = "CrusingMap_2",
	map_202406 = "CrusingMap_1",
	map_202110 = "CrusingMap_0",
	map_202204 = "CrusingMap_1",
	map_202202 = "CrusingMap_2",
	map_202302 = "CrusingMap_1",
	map_202210 = "CrusingMap_1",
	map_202310 = "CrusingMap_2",
	map_202112 = "CrusingMap_1",
	map_202304 = "CrusingMap_1",
	map_202206 = "CrusingMap_1",
	map_202404 = "CrusingMap_1",
	map_202402 = "CrusingMap_1"
}

def var_0_0.GetPhaseFrame(arg_1_0):
	local var_1_0 = var_0_0.MapInfo[arg_1_0]

	return setmetatable(Clone(var_1_0.frame), {
		def __index:(arg_2_0, arg_2_1)
			local var_2_0 = 0
			local var_2_1 = 100

			for iter_2_0, iter_2_1 in pairs(arg_2_0):
				if iter_2_0 < arg_2_1 and var_2_0 < iter_2_0:
					var_2_0 = iter_2_0

				if arg_2_1 < iter_2_0 and iter_2_0 < var_2_1:
					var_2_1 = iter_2_0

			local var_2_2 = (arg_2_1 - var_2_0) / (var_2_1 - var_2_0)

			return (1 - var_2_2) * arg_2_0[var_2_0] + var_2_2 * arg_2_0[var_2_1]
	}), var_1_0.all

return var_0_0
