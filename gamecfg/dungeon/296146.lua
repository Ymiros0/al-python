﻿return {
	map_id = 10001,
	id = 296146,
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
					key = true,
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
					key = true,
					waveIndex = 101,
					conditionType = 1,
					preWaves = {
						100
					},
					triggerParam = {},
					spawn = {
						{
							score = 0,
							monsterTemplateID = 295146,
							delay = 0,
							moveCast = true,
							affix = true,
							corrdinate = {
								-5,
								0,
								50
							},
							buffList = {
								200358,
								200280
							},
							bossData = {
								hpBarNum = 100,
								icon = "yilishabai_alter"
							},
							phase = {
								{
									switchParam = 1.5,
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
									switchParam = 11,
									setAI = 10001,
									addWeapon = {
										2972003,
										2972008,
										2972013
									},
									removeWeapon = {}
								},
								{
									switchType = 1,
									switchTo = 3,
									index = 2,
									switchParam = 2,
									setAI = 70125,
									addWeapon = {},
									removeWeapon = {}
								},
								{
									index = 3,
									switchParam = 1,
									switchTo = 4,
									switchType = 1,
									addWeapon = {
										2972018,
										2972023,
										2972033
									},
									removeWeapon = {
										2972003,
										2972008,
										2972013
									}
								},
								{
									switchType = 1,
									switchTo = 5,
									index = 4,
									switchParam = 7,
									setAI = 10001,
									addWeapon = {
										2972003,
										2972028
									},
									removeWeapon = {}
								},
								{
									index = 5,
									switchParam = 4,
									switchTo = 6,
									switchType = 1,
									addWeapon = {},
									removeWeapon = {
										2972018,
										2972023,
										2972028,
										2972033
									}
								},
								{
									switchParam = 2,
									switchTo = 7,
									index = 6,
									switchType = 1,
									setAI = 70125
								},
								{
									index = 7,
									switchParam = 7,
									switchTo = 8,
									switchType = 1,
									addWeapon = {
										2972018,
										2972038
									},
									removeWeapon = {
										2972003
									}
								},
								{
									index = 8,
									switchType = 1,
									switchTo = 9,
									switchParam = 3,
									addWeapon = {},
									addBuff = {
										200375
									},
									removeWeapon = {
										2972018,
										2972038
									}
								},
								{
									index = 9,
									switchParam = 6,
									switchTo = 10,
									switchType = 1,
									addWeapon = {
										2972048
									},
									removeWeapon = {}
								},
								{
									index = 10,
									switchParam = 5,
									switchTo = 11,
									switchType = 1,
									addWeapon = {
										2972018
									},
									removeWeapon = {}
								},
								{
									index = 11,
									switchParam = 12,
									switchTo = 12,
									switchType = 1,
									addWeapon = {
										2972058
									},
									removeWeapon = {
										2972018,
										2972048
									}
								},
								{
									index = 12,
									switchParam = 300,
									switchTo = 1,
									switchType = 1,
									addWeapon = {
										2972003,
										2972018,
										2972063
									},
									removeWeapon = {
										2972058
									}
								},
								{
									index = 21,
									switchType = 1,
									switchTo = 22,
									switchParam = 6
								},
								{
									switchType = 1,
									switchTo = 23,
									index = 22,
									switchParam = 1,
									setAI = 10001,
									addWeapon = {
										2972068
									},
									removeWeapon = {}
								},
								{
									index = 23,
									switchParam = 11,
									switchTo = 24,
									switchType = 1,
									addWeapon = {
										2972008,
										2972013
									},
									removeWeapon = {}
								},
								{
									index = 24,
									switchParam = 1,
									switchTo = 23,
									switchType = 1,
									addWeapon = {},
									removeWeapon = {
										2972008,
										2972013
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
						203
					},
					triggerParams = {}
				}
			}
		}
	},
	fleet_prefab = {}
}
