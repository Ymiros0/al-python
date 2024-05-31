local var_0_0 = {
	TIME_INTERVAL = 0.016666666666666666,
	GRASS_CHAGNE_RATE = 0.2,
	ALL_GAME_TIME = 120,
	MIN_MAP_SIZE = {
		20,
		20
	},
	SOIL_RANDOM_CONFIG = {
		spacer_rate = 0.25,
		size_rate = {
			0.5,
			0.7
		},
		cancel_rate = {
			0.2,
			0.3
		}
	},
	SOIL_SPRITES_DIC = {
		[119] = "Soil_4",
		[38] = "Soil_1",
		[254] = "Soil_2",
		[205] = "Soil_6",
		[238] = "Soil_2",
		[204] = "Soil_3",
		[239] = "Soil_11",
		[179] = "Soil_7",
		[236] = "Soil_3",
		[102] = "Soil_1",
		[237] = "Soil_6",
		[147] = "Soil_7",
		[118] = "Soil_1",
		[51] = "Soil_7",
		[137] = "Soil_9",
		[153] = "Soil_9",
		[251] = "Soil_8",
		[219] = "Soil_8",
		[187] = "Soil_8",
		[155] = "Soil_8",
		[217] = "Soil_9",
		[255] = "Soil_5",
		[223] = "Soil_13",
		[191] = "Soil_12",
		[54] = "Soil_1",
		[253] = "Soil_6",
		[221] = "Soil_6",
		[127] = "Soil_10",
		[110] = "Soil_2",
		[76] = "Soil_3",
		[126] = "Soil_2",
		[55] = "Soil_4",
		[108] = "Soil_3",
		[247] = "Soil_4",
		[19] = "Soil_7",
		[183] = "Soil_4",
		[201] = "Soil_9"
	},
	ENEMY_TYPE_LIST = {
		"Scavenger",
		"Chaser",
		"Smasher",
		"Conductor",
		"Navigator",
		"BOSS_Scavenger",
		"BOSS_Conductor",
		"BOSS_Chaser",
		"BOSS_Navigator",
		"BOSS_Smasher"
	},
	FREE_MAP_BOSS_LIMIT = {
		2,
		2,
		3,
		3,
		3,
		4,
		4
	},
	def CreateInfo:(arg_1_0)
		local var_1_0 = {}

		switch(arg_1_0, {
			def Item:()
				var_1_0.targetClass = TargetItem
				var_1_0.path = "object/Item"
				var_1_0.parent = "object",
			def Bomb:()
				var_1_0.targetClass = ObjectBomb
				var_1_0.path = "object/Bomb"
				var_1_0.parent = "object",
			def Bush:()
				var_1_0.targetClass = ObjectBush
				var_1_0.path = "object/Bush"
				var_1_0.parent = "object",
			def Box:()
				var_1_0.targetClass = ObjectBreakable
				var_1_0.path = "object/Box"
				var_1_0.parent = "object",
			def Grass:()
				var_1_0.targetClass = ObjectBreakable
				var_1_0.path = "object/Grass"
				var_1_0.parent = "object",
			def Taru:()
				var_1_0.targetClass = ObjectBreakable
				var_1_0.path = "object/Taru"
				var_1_0.parent = "object",
			def Rock_A:()
				var_1_0.targetClass = TargetObject
				var_1_0.path = "object/Rock_A"
				var_1_0.parent = "object",
			def Rock_B:()
				var_1_0.targetClass = ObjectRockB
				var_1_0.path = "object/Rock_B"
				var_1_0.parent = "object",
			def Tree_L:()
				var_1_0.targetClass = TargetObject
				var_1_0.path = "object/Tree_L"
				var_1_0.parent = "object",
			def Tree_S:()
				var_1_0.targetClass = TargetObject
				var_1_0.path = "object/Tree_S"
				var_1_0.parent = "object",
			def Treasure_N:()
				var_1_0.targetClass = ObjectTreasureN
				var_1_0.path = "object/Treasure_N"
				var_1_0.parent = "object",
			def Treasure_R:()
				var_1_0.targetClass = ObjectTreasureR
				var_1_0.path = "object/Treasure_R"
				var_1_0.parent = "object",
			def Fire:()
				var_1_0.targetClass = EffectFire
				var_1_0.path = "effect/Fire"
				var_1_0.parent = "effect"
				var_1_0.order = "low",
			def Impack:()
				var_1_0.targetClass = EffectImpack
				var_1_0.path = "effect/Impack"
				var_1_0.parent = "effect",
			def Bullet:()
				var_1_0.targetClass = EffectBullet
				var_1_0.path = "effect/Bullet"
				var_1_0.parent = "effect",
			def Laser:()
				var_1_0.targetClass = EffectLaser
				var_1_0.path = "effect/Laser"
				var_1_0.parent = "effect",
			def Ryza:()
				var_1_0.targetClass = MoveRyza
				var_1_0.path = "character/Ryza"
				var_1_0.parent = "character",
			def Scavenger:()
				var_1_0.targetClass = EnemyScavenger
				var_1_0.path = "character/Scavenger"
				var_1_0.parent = "character",
			def BOSS_Scavenger:()
				var_1_0.targetClass = EnemyBossScavenger
				var_1_0.path = "character/BOSS_Scavenger"
				var_1_0.parent = "character",
			def Chaser:()
				var_1_0.targetClass = EnemyChaser
				var_1_0.path = "character/Chaser"
				var_1_0.parent = "character",
			def BOSS_Chaser:()
				var_1_0.targetClass = EnemyBossChaser
				var_1_0.path = "character/BOSS_Chaser"
				var_1_0.parent = "character",
			def Smasher:()
				var_1_0.targetClass = EnemySmasher
				var_1_0.path = "character/Smasher"
				var_1_0.parent = "character",
			def BOSS_Smasher:()
				var_1_0.targetClass = EnemyBossSmasher
				var_1_0.path = "character/BOSS_Smasher"
				var_1_0.parent = "character",
			def Conductor:()
				var_1_0.targetClass = EnemyConductor
				var_1_0.path = "character/Conductor"
				var_1_0.parent = "character",
			def BOSS_Conductor:()
				var_1_0.targetClass = EnemyBossConductor
				var_1_0.path = "character/BOSS_Conductor"
				var_1_0.parent = "character",
			def Navigator:()
				var_1_0.targetClass = EnemyNavigator
				var_1_0.path = "character/Navigator"
				var_1_0.parent = "character",
			def BOSS_Navigator:()
				var_1_0.targetClass = EnemyBossNavigator
				var_1_0.path = "character/BOSS_Navigator"
				var_1_0.parent = "character"
		})

		return var_1_0.targetClass, var_1_0.path, var_1_0.parent
}
local var_0_1 = {
	{
		"S",
		"N"
	},
	{
		"E",
		"W"
	}
}
local var_0_2 = math.sin(math.pi / 8)

def var_0_0.GetEightDirMark(arg_29_0):
	local var_29_0 = {}

	for iter_29_0, iter_29_1 in ipairs({
		arg_29_0.y,
		arg_29_0.x
	}):
		if iter_29_1 * iter_29_1 < var_0_2 * var_0_2:
			iter_29_1 = 0

		if iter_29_1 > 0:
			var_29_0[iter_29_0] = var_0_1[iter_29_0][1]
		elif iter_29_1 < 0:
			var_29_0[iter_29_0] = var_0_1[iter_29_0][2]
		else
			var_29_0[iter_29_0] = ""

	return var_29_0[1] .. var_29_0[2]

def var_0_0.GetFourDirMark(arg_30_0):
	local var_30_0 = {}
	local var_30_1 = arg_30_0.y * arg_30_0.y < arg_30_0.x * arg_30_0.x and {
		0,
		arg_30_0.x
	} or {
		arg_30_0.y,
		0
	}

	for iter_30_0, iter_30_1 in ipairs(var_30_1):
		if iter_30_1 > 0:
			var_30_0[iter_30_0] = var_0_1[iter_30_0][1]
		elif iter_30_1 < 0:
			var_30_0[iter_30_0] = var_0_1[iter_30_0][2]
		else
			var_30_0[iter_30_0] = ""

	return var_30_0[1] .. var_30_0[2]

def var_0_0.GetDestroyPoint(arg_31_0):
	local var_31_0 = 0

	if arg_31_0.class == TargetItem:
		switch(arg_31_0.type, {
			def bomb:()
				var_31_0 = 50,
			def power:()
				var_31_0 = 50,
			def speed:()
				var_31_0 = 50,
			def hp1:()
				var_31_0 = 100,
			def hp2:()
				var_31_0 = 200,
			def spirit:()
				var_31_0 = 300
		})
	elif isa(arg_31_0, TargetObject):
		switch(arg_31_0.class, {
			[ObjectBreakable] = function()
				var_31_0 = 20,
			[ObjectRockB] = function()
				var_31_0 = 50,
			[ObjectTreasureN] = function()
				var_31_0 = 200,
			[ObjectTreasureR] = function()
				var_31_0 = 500
		})
	elif isa(arg_31_0, MoveEnemy):
		switch(arg_31_0.class, {
			[EnemyScavenger] = function()
				var_31_0 = 100,
			[EnemyBossScavenger] = function()
				var_31_0 = 300,
			[EnemyChaser] = function()
				var_31_0 = 100,
			[EnemyBossChaser] = function()
				var_31_0 = 500,
			[EnemyNavigator] = function()
				var_31_0 = 150,
			[EnemyBossNavigator] = function()
				var_31_0 = 600,
			[EnemySmasher] = function()
				var_31_0 = 150,
			[EnemyBossSmasher] = function()
				var_31_0 = 500,
			[EnemyConductor] = function()
				var_31_0 = 200,
			[EnemyBossConductor] = function()
				var_31_0 = 600
		})

	return var_31_0

def var_0_0.GetPassGamePoint(arg_52_0):
	return math.floor(10000 / math.log(arg_52_0))

return var_0_0
