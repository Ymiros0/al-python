return {
	map_id = 10001,
	id = 1772008,
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
							monsterTemplateID = 16572003,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								0,
								0,
								75
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 16572001,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								5,
								0,
								55
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 16572003,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								0,
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
							onceNumber = 6,
							formation = 10006,
							delay = 0,
							templateID = 3109072,
							totalNumber = 6,
							weaponID = {
								3109082
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
					key = True,
					waveIndex = 102,
					conditionType = 1,
					preWaves = {
						101,
						202
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 16572005,
							reinforceDelay = 6,
							score = 0,
							delay = 0,
							moveCast = True,
							corrdinate = {
								8,
								0,
								55
							},
							buffList = {
								8001,
								8007
							}
						}
					},
					reinforcement = {
						{
							monsterTemplateID = 16572001,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								10,
								0,
								80
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 16572003,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								0,
								0,
								65
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 16572003,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								0,
								0,
								45
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 16572001,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								10,
								0,
								30
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
					waveIndex = 103,
					conditionType = 1,
					preWaves = {
						102,
						203
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 16572104,
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
							monsterTemplateID = 16572001,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								-3,
								0,
								80
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 16572003,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								5,
								0,
								70
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 16572003,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								5,
								0,
								40
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 16572001,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								-3,
								0,
								30
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
							onceNumber = 6,
							formation = 10006,
							delay = 0,
							templateID = 3109067,
							totalNumber = 6,
							weaponID = {
								3109077,
								1100752
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
							monsterTemplateID = 16572007,
							moveCast = True,
							delay = 8,
							corrdinate = {
								5,
								0,
								68
							},
							buffList = {
								8001
							},
							phase = {
								{
									switchParam = 20,
									dive = "STATE_RAID",
									switchTo = 1,
									index = 0,
									switchType = 1,
									setAI = 20015
								},
								{
									index = 1,
									switchType = 1,
									switchTo = 1,
									switchParam = 180
								}
							}
						},
						{
							monsterTemplateID = 16572007,
							moveCast = True,
							delay = 8,
							corrdinate = {
								5,
								0,
								48
							},
							buffList = {
								8001
							},
							phase = {
								{
									switchParam = 20,
									dive = "STATE_RAID",
									switchTo = 1,
									index = 0,
									switchType = 1,
									setAI = 20015
								},
								{
									index = 1,
									switchType = 1,
									switchTo = 1,
									switchParam = 180
								}
							}
						},
						reinforceDuration = 180
					}
				},
				{
					triggerType = 0,
					waveIndex = 9001,
					conditionType = 1,
					preWaves = {
						100
					},
					triggerParam = {},
					blockFlags = {
						200647
					},
					spawn = {
						{
							monsterTemplateID = 16579003,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								15,
								0,
								55
							},
							buffList = {},
							phase = {
								{
									switchParam = 7,
									switchTo = 1,
									index = 0,
									switchType = 1,
									setAI = 20006
								},
								{
									index = 1,
									switchParam = 5,
									switchTo = 2,
									switchType = 1,
									addWeapon = {
										3109303
									},
									addBuff = {
										200651
									}
								},
								{
									index = 2,
									switchType = 1,
									switchTo = 1,
									switchParam = 15,
									removeWeapon = {
										3109303
									}
								}
							}
						}
					}
				},
				{
					triggerType = 8,
					waveIndex = 900,
					preWaves = {
						103
					},
					triggerParams = {}
				}
			}
		}
	},
	fleet_prefab = {}
}
