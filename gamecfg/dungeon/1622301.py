return {
	map_id = 10001,
	id = 1622301,
	stages = {
		{
			stageIndex = 1,
			failCondition = 1,
			timeCount = 180,
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
					waveIndex = 202,
					preWaves = {},
					triggerParams = {
						timeout = 20
					}
				},
				{
					triggerType = 1,
					waveIndex = 203,
					preWaves = {},
					triggerParams = {
						timeout = 40
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
							monsterTemplateID = 15602201,
							reinforceDelay = 6,
							score = 0,
							delay = 0,
							moveCast = True,
							corrdinate = {
								-5,
								0,
								55
							},
							buffList = {
								8727
							},
							phase = {
								{
									switchType = 1,
									dive = "STATE_RAID",
									switchTo = 2,
									index = 0,
									switchParam = 2,
									setAI = 70109
								},
								{
									index = 2,
									switchParam = 4,
									switchTo = 3,
									switchType = 1,
									addWeapon = {
										1000897
									},
									removeWeapon = {}
								},
								{
									index = 3,
									switchParam = 3,
									switchTo = 4,
									switchType = 1,
									addWeapon = {
										1000892
									},
									removeWeapon = {
										1000897
									}
								},
								{
									index = 4,
									switchParam = 2,
									switchTo = 5,
									switchType = 1,
									addWeapon = {},
									removeWeapon = {
										1000892
									}
								},
								{
									switchType = 1,
									switchTo = 6,
									index = 5,
									switchParam = 4,
									setAI = 10001,
									addWeapon = {
										1000892
									},
									removeWeapon = {}
								},
								{
									switchParam = 0.5,
									dive = "STATE_FLOAT",
									switchTo = 7,
									index = 6,
									switchType = 1
								},
								{
									index = 7,
									switchParam = 2,
									switchTo = 8,
									switchType = 1,
									addWeapon = {
										1000882
									},
									removeWeapon = {
										1000892
									}
								},
								{
									index = 8,
									switchParam = 4,
									switchTo = 9,
									switchType = 1,
									addWeapon = {
										1000887,
										1000892
									},
									removeWeapon = {
										1000882
									}
								},
								{
									index = 9,
									switchParam = 0.5,
									switchTo = 10,
									switchType = 1,
									addWeapon = {},
									removeWeapon = {
										1000887,
										1000892
									}
								},
								{
									index = 10,
									switchParam = 2,
									switchTo = 11,
									switchType = 1,
									addWeapon = {
										1000882
									},
									removeWeapon = {}
								},
								{
									index = 11,
									switchParam = 4,
									switchTo = 12,
									switchType = 1,
									addWeapon = {
										1000887,
										1000892
									},
									removeWeapon = {
										1000882
									}
								},
								{
									index = 12,
									switchParam = 1,
									switchTo = 13,
									switchType = 1,
									addWeapon = {},
									removeWeapon = {
										1000887,
										1000892
									}
								},
								{
									switchType = 1,
									dive = "STATE_RAID",
									switchTo = 2,
									index = 13,
									switchParam = 2,
									setAI = 70109
								}
							}
						}
					},
					reinforcement = {
						{
							monsterTemplateID = 15602001,
							moveCast = True,
							delay = 2,
							score = 0,
							corrdinate = {
								12,
								0,
								75
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 15602001,
							moveCast = True,
							delay = 2,
							score = 0,
							corrdinate = {
								12,
								0,
								35
							},
							buffList = {
								8001,
								8007
							}
						}
					},
					airFighter = {
						{
							interval = 10,
							onceNumber = 3,
							formation = 10006,
							delay = 0,
							templateID = 1000817,
							totalNumber = 6,
							weaponID = {
								1000842
							},
							attr = {
								airPower = 40,
								maxHP = 15,
								attackRating = 23
							}
						}
					}
				},
				{
					triggerType = 0,
					waveIndex = 2001,
					conditionType = 1,
					preWaves = {
						100
					},
					triggerParam = {},
					spawn = {},
					reinforcement = {
						{
							monsterTemplateID = 15602007,
							moveCast = True,
							delay = 4,
							corrdinate = {
								5,
								0,
								55
							},
							buffList = {
								8001
							},
							phase = {
								{
									switchParam = 180,
									dive = "STATE_RAID",
									switchTo = 1,
									index = 0,
									switchType = 1,
									setAI = 20005
								}
							}
						},
						reinforceDuration = 180
					}
				},
				{
					triggerType = 8,
					waveIndex = 900,
					preWaves = {
						101
					},
					triggerParams = {}
				}
			}
		}
	},
	fleet_prefab = {}
}
