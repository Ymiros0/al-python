return {
	id = 1793214,
	stages = {
		{
			stageIndex = 1,
			failCondition = 1,
			timeCount = 180,
			passCondition = 1,
			backGroundStageID = 1,
			totalArea = {
				-75,
				20,
				90,
				70
			},
			playerArea = {
				-75,
				20,
				42,
				68
			},
			enemyArea = {},
			mainUnitPosition = {
				{
					Vector3(-105, 0, 58),
					Vector3(-105, 0, 78),
					Vector3(-105, 0, 38)
				},
				[-1] = {
					Vector3(15, 0, 58),
					Vector3(15, 0, 78),
					Vector3(15, 0, 38)
				}
			},
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
						timeout = 18
					}
				},
				{
					triggerType = 1,
					waveIndex = 203,
					preWaves = {},
					triggerParams = {
						timeout = 33
					}
				},
				{
					triggerType = 1,
					waveIndex = 204,
					preWaves = {},
					triggerParams = {
						timeout = 44
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
							monsterTemplateID = 16593002,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								10,
								0,
								75
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 16593122,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								0,
								0,
								55
							}
						},
						{
							monsterTemplateID = 16593002,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								10,
								0,
								35
							},
							buffList = {
								8001,
								8007
							}
						}
					}
				},
				{
					triggerType = 0,
					waveIndex = 102,
					conditionType = 1,
					preWaves = {
						101,
						202
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 16593123,
							reinforceDelay = 6,
							score = 0,
							delay = 0,
							moveCast = True,
							corrdinate = {
								-5,
								0,
								55
							}
						}
					},
					reinforcement = {
						{
							monsterTemplateID = 16593001,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								10,
								0,
								75
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 16593002,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								3,
								0,
								65
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 16593002,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								3,
								0,
								45
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 16593001,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								10,
								0,
								35
							},
							buffList = {
								8001,
								8007
							}
						}
					}
				},
				{
					triggerType = 0,
					key = True,
					waveIndex = 104,
					conditionType = 0,
					preWaves = {
						500,
						102,
						101
					},
					triggerParam = {},
					spawn = {
						{
							score = 0,
							moveCast = True,
							delay = 0.1,
							monsterTemplateID = 16593304,
							corrdinate = {
								-5,
								0,
								50
							},
							buffList = {},
							bossData = {
								hpBarNum = 80,
								icon = "sairen"
							},
							phase = {
								{
									index = 0,
									switchType = 1,
									switchTo = 1,
									switchParam = 0.1,
									addWeapon = {}
								},
								{
									switchType = 1,
									switchTo = 2,
									index = 1,
									switchParam = 5,
									setAI = 10001,
									addWeapon = {
										3123301,
										3123302
									}
								},
								{
									switchParam = 7,
									switchTo = 3,
									index = 2,
									switchType = 1,
									setAI = 70125
								},
								{
									index = 3,
									switchParam = 4.5,
									switchTo = 4,
									switchType = 1,
									addWeapon = {
										3123303
									},
									removeWeapon = {
										3123301,
										3123302
									}
								},
								{
									switchType = 1,
									switchTo = 5,
									index = 4,
									switchParam = 10.6,
									setAI = 75025,
									addWeapon = {
										3123304,
										3123305,
										3123306
									},
									removeWeapon = {
										3123303
									}
								},
								{
									switchType = 1,
									switchTo = 6,
									index = 5,
									switchParam = 4.5,
									setAI = 70125,
									addWeapon = {
										3123303
									},
									removeWeapon = {
										3123304,
										3123305,
										3123306
									}
								},
								{
									index = 6,
									switchParam = 6,
									switchTo = 7,
									switchType = 1,
									addWeapon = {
										3123307,
										3123308,
										3123309
									},
									removeWeapon = {
										3123303
									}
								},
								{
									index = 7,
									switchType = 1,
									switchTo = 8,
									switchParam = 1,
									addWeapon = {
										3123310
									}
								},
								{
									index = 8,
									switchType = 1,
									switchTo = 9,
									switchParam = 1,
									addWeapon = {
										3123311
									}
								},
								{
									index = 9,
									switchType = 1,
									switchTo = 10,
									switchParam = 9.5,
									addWeapon = {
										3123312
									}
								},
								{
									index = 10,
									switchType = 1,
									switchTo = 1,
									switchParam = 1.5,
									removeWeapon = {
										3123307,
										3123308,
										3123309,
										3123310,
										3123311,
										3123312
									}
								}
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
							monsterTemplateID = 16593007,
							moveCast = True,
							delay = 5,
							corrdinate = {
								5,
								0,
								58
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
									setAI = 20009
								}
							}
						},
						reinforceDuration = 180
					}
				},
				{
					triggerType = 8,
					key = True,
					waveIndex = 900,
					preWaves = {
						104
					},
					triggerParams = {}
				}
			}
		}
	},
	fleet_prefab = {}
}
