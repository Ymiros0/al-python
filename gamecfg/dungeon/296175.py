return {
	id = 296175,
	stages = {
		{
			stageIndex = 1,
			failCondition = 1,
			timeCount = 80,
			passCondition = 1,
			backGroundStageID = 1,
			totalArea = {
				-70,
				20,
				90,
				70
			},
			playerArea = {
				-70,
				20,
				37,
				68
			},
			enemyArea = {},
			fleetCorrdinate = {
				-80,
				0,
				75
			},
			waves = {
				{
					triggerType = 1,
					waveIndex = 100,
					preWaves = {},
					triggerParams = {
						timeout = 0.5
					}
				},
				{
					triggerType = 1,
					key = True,
					waveIndex = 203,
					preWaves = {
						101
					},
					triggerParams = {
						timeout = 0.1
					}
				},
				{
					triggerType = 0,
					key = True,
					waveIndex = 101,
					conditionType = 1,
					preWaves = {
						100
					},
					triggerParam = {},
					spawn = {
						{
							score = 0,
							monsterTemplateID = 295175,
							delay = 0,
							moveCast = True,
							affix = True,
							corrdinate = {
								-10,
								0,
								50
							},
							buffList = {},
							bossData = {
								hpBarNum = 100,
								icon = "shentong_alter"
							},
							phase = {
								{
									switchParam = 2.5,
									switchTo = 1,
									index = 0,
									switchType = 1,
									setAI = 20006,
									addWeapon = {}
								},
								{
									switchType = 1,
									switchTo = 2,
									index = 1,
									switchParam = 4,
									setAI = 10001,
									addWeapon = {
										2974003,
										2974008
									},
									removeWeapon = {}
								},
								{
									switchType = 1,
									switchTo = 3,
									index = 2,
									switchParam = 1,
									setAI = 70188,
									addWeapon = {},
									removeWeapon = {}
								},
								{
									index = 3,
									switchParam = 3.5,
									switchTo = 4,
									switchType = 1,
									addWeapon = {
										2974023,
										2974028
									},
									removeWeapon = {
										2974003,
										2974008
									}
								},
								{
									switchType = 1,
									switchTo = 5,
									index = 4,
									switchParam = 19,
									setAI = 10001,
									addWeapon = {
										2974033,
										2974038
									},
									removeWeapon = {
										2974023,
										2974028
									}
								},
								{
									index = 5,
									switchParam = 8,
									switchTo = 6,
									switchType = 1,
									addWeapon = {
										2974013,
										2974018
									},
									removeWeapon = {
										2974033,
										2974038
									}
								},
								{
									switchType = 1,
									switchTo = 7,
									index = 6,
									switchParam = 1,
									setAI = 70188,
									addWeapon = {},
									removeWeapon = {}
								},
								{
									index = 7,
									switchParam = 3,
									switchTo = 8,
									switchType = 1,
									addWeapon = {
										2974023,
										2974028
									},
									removeWeapon = {
										2974013,
										2974018
									}
								},
								{
									index = 8,
									switchParam = 3,
									switchTo = 9,
									switchType = 1,
									addWeapon = {
										2974043
									},
									removeWeapon = {
										2974023,
										2974028
									}
								},
								{
									index = 9,
									switchParam = 2.5,
									switchTo = 10,
									switchType = 1,
									addWeapon = {},
									removeWeapon = {
										2974043
									}
								},
								{
									index = 10,
									switchParam = 1,
									switchTo = 11,
									switchType = 1,
									addWeapon = {
										2974048,
										2974053,
										2974058
									},
									removeWeapon = {}
								},
								{
									switchType = 1,
									switchTo = 12,
									index = 11,
									switchParam = 8,
									setAI = 10001,
									addWeapon = {},
									removeWeapon = {
										2974048,
										2974053,
										2974058
									}
								},
								{
									switchParam = 2,
									switchTo = 13,
									index = 12,
									switchType = 1,
									setAI = 70188
								},
								{
									index = 13,
									switchParam = 300,
									switchTo = 1,
									switchType = 1,
									addWeapon = {
										2974063
									},
									removeWeapon = {}
								}
							}
						}
					}
				},
				{
					triggerType = 8,
					waveIndex = 900,
					preWaves = {
						203
					},
					triggerParams = {}
				}
			}
		}
	},
	fleet_prefab = {}
}
