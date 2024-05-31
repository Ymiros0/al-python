local var_0_0 = class("HideSeekGameView", import("..BaseMiniGameView"))
local var_0_1 = "bar-soft"
local var_0_2 = "event./ui/ddldaoshu2"
local var_0_3 = "event./ui/break_out_full"
local var_0_4 = "hideseekgameui_atlas"
local var_0_5 = 60
local var_0_6 = {
	{
		25,
		0.8,
		1
	},
	{
		45,
		1.2,
		1.4
	},
	{
		60,
		1.6,
		1.8
	}
}
local var_0_7 = 100
local var_0_8 = 2
local var_0_9 = 50
local var_0_10 = 400
local var_0_11 = 400
local var_0_12 = "on_touch_furniture"
local var_0_13 = 1
local var_0_14 = 2
local var_0_15 = 3
local var_0_16 = 4
local var_0_17 = "HideSeekBath"
local var_0_18 = "HideSeekBed"
local var_0_19 = "HideSeekFridge"
local var_0_20 = "HideSeekHakoCL"
local var_0_21 = "HideSeekHakoCR"
local var_0_22 = "HideSeekUpR"
local var_0_23 = "HideSeekUpL"
local var_0_24 = "HideSeekDeskUnder"
local var_0_25 = "HideSeekSofaS"
local var_0_26 = "HideSeekSofaL"
local var_0_27 = "HideSeekHakoSL"
local var_0_28 = "HideSeekHakoSR"
local var_0_29 = "HideSeekHakoML"
local var_0_30 = "HideSeekHakoMR"
local var_0_31 = "HideSeekDeskSR"
local var_0_32 = "HideSeekDeskSL"
local var_0_33 = "HideSeekDeskStudyL"
local var_0_34 = "HideSeekDeskStudyR"
local var_0_35 = "HideSeekCushion"
local var_0_36 = "ui/minigameui/hideseek"
local var_0_37 = 3
local var_0_38 = {
	0,
	1,
	2,
	3,
	4,
	5,
	6,
	7,
	8
}
local var_0_39 = {
	{
		name = "furniture_bath",
		pos_data_list = {
			{
				pos_name = "posBath",
				anim_name = var_0_17
			}
		},
		type = var_0_13
	},
	{
		weight = 0.2,
		name = "furniture_bed",
		pos_data_list = {
			{
				pos_name = "posBed",
				anim_name = var_0_18
			}
		},
		type = var_0_14
	},
	{
		name = "furniture_Fridge",
		time = 3,
		defaut_trigger = True,
		defaut_char_index = 9,
		weight = 0.15,
		pos_data_list = {
			{
				pos_name = "posFridge",
				anim_name = var_0_19
			}
		},
		type = var_0_15
	},
	{
		time = 4,
		name = "furniture_Hako_L1",
		hide = True,
		pos_data_list = {
			{
				pos_name = "posHakoCL",
				anim_name = var_0_20
			}
		},
		type = var_0_13
	},
	{
		time = 4,
		name = "furniture_Cook",
		hide = True,
		pos_data_list = {
			{
				pos_name = "posUpR",
				anim_name = var_0_22
			}
		},
		type = var_0_13
	},
	{
		time = 4,
		name = "furniture_Desk_Dining",
		hide = True,
		pos_data_list = {
			{
				pos_name = "posUnder",
				anim_name = var_0_24
			},
			{
				pos_name = "posUpR",
				anim_name = var_0_22
			},
			{
				pos_name = "posUpL",
				anim_name = var_0_23
			}
		},
		type = var_0_13
	},
	{
		time = 4,
		name = "furniture_Sofa_S",
		hide = True,
		pos_data_list = {
			{
				pos_name = "posSofaS",
				anim_name = var_0_25
			}
		},
		type = var_0_13
	},
	{
		time = 4,
		name = "furniture_Sofa_L",
		hide = True,
		pos_data_list = {
			{
				pos_name = "posSofaL",
				anim_name = var_0_26
			},
			{
				pos_name = "posUpL",
				anim_name = var_0_23
			}
		},
		type = var_0_13
	},
	{
		time = 4,
		name = "furniture_Hako_S1_3",
		hide = True,
		pos_data_list = {
			{
				pos_name = "posHakoSL",
				anim_name = var_0_27
			}
		},
		type = var_0_13
	},
	{
		time = 4,
		name = "furniture_Desk_S",
		hide = True,
		pos_data_list = {
			{
				pos_name = "posDeskSL",
				anim_name = var_0_32
			},
			{
				pos_name = "posDeskSR",
				anim_name = var_0_31
			},
			{
				pos_name = "posDeskUnder",
				anim_name = var_0_24
			}
		},
		type = var_0_13
	},
	{
		time = 4,
		name = "furniture_Hako_L2",
		hide = True,
		pos_data_list = {
			{
				pos_name = "posHakoCL",
				anim_name = var_0_20
			},
			{
				pos_name = "posHakoCR",
				anim_name = var_0_21
			}
		},
		type = var_0_13
	},
	{
		time = 4,
		name = "furniture_Desk_Study",
		hide = True,
		pos_data_list = {
			{
				pos_name = "posDeskStudyL",
				anim_name = var_0_33
			},
			{
				pos_name = "posDeskStudyR",
				anim_name = var_0_34
			}
		},
		type = var_0_13
	},
	{
		time = 4,
		name = "furniture_Hako_M1",
		hide = True,
		pos_data_list = {
			{
				pos_name = "posHakoML",
				anim_name = var_0_29
			}
		},
		type = var_0_13
	},
	{
		time = 4,
		name = "furniture_Hako_M2",
		hide = True,
		pos_data_list = {
			{
				pos_name = "posHakoMR",
				anim_name = var_0_30
			}
		},
		type = var_0_13
	},
	{
		time = 4,
		name = "furniture_Hako_S2",
		hide = True,
		pos_data_list = {
			{
				pos_name = "posHakoSR",
				anim_name = var_0_28
			}
		},
		type = var_0_13
	},
	{
		name = "furniture_Manjuu_cushion",
		pos_data_list = {
			{
				pos_name = "posCushion",
				anim_name = var_0_35
			}
		},
		type = var_0_13,
		hide_tfs = {
			"img"
		}
	}
}
local var_0_40 = {
	HideSeekBath = {
		prefab = "hideseekbath.prefab",
		name = var_0_17,
		ignore_char = {}
	},
	HideSeekBed = {
		prefab = "hideseekbed.prefab",
		name = var_0_18,
		ignore_char = {}
	},
	HideSeekFridge = {
		prefab = "hideseekfridge.prefab",
		name = var_0_19,
		ignore_char = {}
	},
	HideSeekHakoCL = {
		prefab = "hideseekhakocl.prefab",
		name = var_0_20,
		ignore_char = {}
	},
	HideSeekHakoCR = {
		prefab = "hideseekhakocr.prefab",
		name = var_0_21,
		ignore_char = {}
	},
	HideSeekUpR = {
		prefab = "hideseekupr.prefab",
		name = var_0_22,
		ignore_char = {}
	},
	HideSeekUpL = {
		prefab = "hideseekupl.prefab",
		name = var_0_23,
		ignore_char = {}
	},
	HideSeekDeskUnder = {
		prefab = "hideseekdeskunder.prefab",
		name = var_0_24,
		ignore_char = {}
	},
	HideSeekSofaS = {
		prefab = "hideseeksofas.prefab",
		name = var_0_25,
		ignore_char = {}
	},
	HideSeekSofaL = {
		prefab = "hideseeksofal.prefab",
		name = var_0_26,
		ignore_char = {}
	},
	HideSeekHakoSL = {
		prefab = "hideseekhakosl.prefab",
		name = var_0_27,
		ignore_char = {}
	},
	HideSeekHakoSR = {
		prefab = "hideseekhakosr.prefab",
		name = var_0_28,
		ignore_char = {}
	},
	HideSeekDeskSL = {
		prefab = "hideseekdesksl.prefab",
		name = var_0_32,
		ignore_char = {}
	},
	HideSeekDeskSR = {
		prefab = "hideseekdesksr.prefab",
		name = var_0_31,
		ignore_char = {}
	},
	HideSeekDeskStudyL = {
		prefab = "hideseekdeskstudyl.prefab",
		name = var_0_33,
		ignore_char = {}
	},
	HideSeekDeskStudyR = {
		prefab = "hideseekdeskstudyr.prefab",
		name = var_0_34,
		ignore_char = {}
	},
	HideSeekHakoML = {
		prefab = "hideseekhakoml.prefab",
		name = var_0_29,
		ignore_char = {}
	},
	HideSeekHakoMR = {
		prefab = "hideseekhakomr.prefab",
		name = var_0_30,
		ignore_char = {}
	},
	HideSeekCushion = {
		prefab = "hideseekcushion.prefab",
		name = var_0_35,
		ignore_char = {}
	}
}
local var_0_41 = 0.1
local var_0_42 = {
	-475,
	652
}
local var_0_43 = {
	-335,
	290
}
local var_0_44 = Vector2(150, -200)
local var_0_45 = "hideseektv.prefab"
local var_0_46 = {}

local function var_0_47(arg_1_0, arg_1_1)
	local var_1_0 = {
		def ctor:(arg_2_0)
			arg_2_0._event = arg_1_1
			arg_2_0._sceneTf = arg_1_0
			arg_2_0._tplContainer = findTF(arg_1_0, "tplPos")
			var_0_46 = Clone(var_0_38)
			arg_2_0._furnituresPools = {}

			for iter_2_0 = 1, #var_0_39:
				local var_2_0 = Clone(var_0_39[iter_2_0])
				local var_2_1 = findTF(arg_2_0._sceneTf, var_0_39[iter_2_0].name)

				table.insert(arg_2_0._furnituresPools, {
					activeIndex = 0,
					data = var_2_0,
					tf = var_2_1
				})

			arg_2_0._unActiveFurnitures = {}
			arg_2_0._activeFurnitures = {}
			arg_2_0._furnitureAnimTfPool = {}
			arg_2_0._animTplDic = {},
		def start:(arg_3_0)
			arg_3_0.timeStep = 0

			arg_3_0.clear()

			arg_3_0.timeAppear = 0
			arg_3_0.additiveScore = var_0_7

			for iter_3_0 = #arg_3_0._furnituresPools, 1, -1:
				local var_3_0 = arg_3_0._furnituresPools[iter_3_0]

				if var_3_0.data.type == var_0_14:
					if math.random() <= var_3_0.data.weight:
						arg_3_0.appearChar(var_3_0.data.name)

					var_3_0.initFlag = True

					table.insert(arg_3_0._unActiveFurnitures, arg_3_0.getFunitureFromPool(var_3_0.data.name))
				elif var_3_0.data.type == var_0_15:
					arg_3_0.appearChar(var_3_0.data.name),
		def step:(arg_4_0)
			arg_4_0.timeStep = arg_4_0.timeStep + Time.deltaTime

			local var_4_0 = False

			if arg_4_0.timeAppear <= 0:
				var_4_0 = True

				local var_4_1 = var_0_5 - arg_4_0.timeStep

				arg_4_0.timeAppear = None

				for iter_4_0 = 1, #var_0_6:
					if not arg_4_0.timeAppear and var_4_1 < var_0_6[iter_4_0][1] or iter_4_0 == #var_0_6:
						local var_4_2 = var_0_6[iter_4_0][2]
						local var_4_3 = var_0_6[iter_4_0][3]

						arg_4_0.timeAppear = math.random() * (var_4_3 - var_4_2) + var_4_2

						break

				arg_4_0.timeAppear = not arg_4_0.timeAppear and 2 or arg_4_0.timeAppear
			else
				arg_4_0.timeAppear = arg_4_0.timeAppear - Time.deltaTime

			for iter_4_1 = #arg_4_0._activeFurnitures, 1, -1:
				local var_4_4 = arg_4_0._activeFurnitures[iter_4_1]

				if var_4_4.time:
					var_4_4.time = var_4_4.time - Time.deltaTime

					if var_4_4.time <= 0:
						arg_4_0.setFurnitureTimeEvent(var_4_4)

			if var_4_0:
				arg_4_0.appearChar(),
		def setFurnitureTimeEvent:(arg_5_0, arg_5_1)
			if arg_5_1.data.type == var_0_15:
				arg_5_0.returnCharIndex(arg_5_1.charIndex)

				if math.random() <= arg_5_1.data.weight and #var_0_46 > 0:
					arg_5_1.charIndex = table.remove(var_0_46, math.random(1, #var_0_46))
				else
					arg_5_1.charIndex = arg_5_1.data.defaut_char_index

				arg_5_1.readyToRemove = False
				arg_5_1.time = arg_5_1.data.time

				GetComponent(findTF(arg_5_1.animTf, "anim"), typeof(Animator)).SetInteger("charIndex", arg_5_1.charIndex)
			elif arg_5_1.data.type == var_0_13:
				if arg_5_1.data.hide and not arg_5_1.readyToRemove:
					arg_5_1.time = 2
					arg_5_1.readyToRemove = True

					local var_5_0 = findTF(arg_5_1.animTf, "anim")

					GetComponent(var_5_0, typeof(Animator)).SetTrigger("hide")
				else
					arg_5_0.returnFurniture(arg_5_1)
			elif arg_5_1.data.type == var_0_14:
				if arg_5_1.charIndex:
					arg_5_0.returnCharIndex(arg_5_1.charIndex)

					if arg_5_1.animTf:
						setActive(findTF(arg_5_1.animTf, "collider"), False)

					arg_5_1.charIndex = None
					arg_5_1.time = None
			else
				arg_5_0.returnFurniture(arg_5_1),
		def returnCharIndex:(arg_6_0, arg_6_1)
			if not table.contains(var_0_46, arg_6_1) and table.contains(var_0_38, arg_6_1):
				table.insert(var_0_46, arg_6_1),
		def appearChar:(arg_7_0, arg_7_1)
			if #var_0_46 <= 0:
				return

			if #arg_7_0._furnituresPools <= 0:
				return

			local var_7_0

			if arg_7_1:
				var_7_0 = arg_7_0.getFunitureFromPool(arg_7_1)

			var_7_0 = var_7_0 or table.remove(arg_7_0._furnituresPools, math.random(1, #arg_7_0._furnituresPools))

			local var_7_1 = var_7_0.data
			local var_7_2 = var_7_1.pos_data_list[math.random(1, #var_7_1.pos_data_list)]
			local var_7_3 = var_7_2.pos_name
			local var_7_4 = var_7_2.anim_name
			local var_7_5 = arg_7_0.getActiveIndex()
			local var_7_6 = var_0_40[var_7_4]

			if not var_7_6:
				print("警告，没有找到" .. var_7_4 .. "的动画数据")
				arg_7_0.returnFurniture(var_7_0)

				return

			local var_7_7

			if var_7_0.data.type == var_0_15:
				var_7_7 = var_7_0.data.defaut_char_index
			else
				var_7_7 = table.remove(var_0_46, math.random(1, #var_0_46))

			var_7_0.charIndex = var_7_7

			if table.contains(var_7_6.ignore_char, var_7_7):
				arg_7_0.returnFurniture(var_7_0)

				return
			elif var_7_0.data.type == var_0_14 and var_7_0.initFlag:
				arg_7_0.returnFurniture(var_7_0)

				return

			var_7_0.posData = var_7_2
			var_7_0.activeIndex = var_7_5
			var_7_0.animData = var_7_6

			table.insert(arg_7_0._activeFurnitures, var_7_0)
			arg_7_0.getAnimTfByPosData(var_7_2, var_7_5, function(arg_8_0, arg_8_1)
				if arg_8_1 != var_7_0.activeIndex:
					arg_7_0.returnAnimTf(var_7_4, arg_8_0)

					return

				if var_7_0.data.hide_tfs:
					for iter_8_0 = 1, #var_7_0.data.hide_tfs:
						setActive(findTF(var_7_0.tf, var_7_0.data.hide_tfs[iter_8_0]), False)

				local var_8_0 = findTF(var_7_0.tf, var_7_3)

				SetParent(arg_8_0, var_8_0)
				setActive(arg_8_0, True)
				setActive(findTF(arg_8_0, "collider"), True)

				arg_8_0.anchoredPosition = Vector2(0, 0)
				var_7_0.animTf = arg_8_0

				arg_7_0.prepareAnim(var_7_0)),
		def getFunitureFromPool:(arg_9_0, arg_9_1)
			for iter_9_0 = 1, #arg_9_0._furnituresPools:
				if arg_9_0._furnituresPools[iter_9_0].data.name == arg_9_1:
					return table.remove(arg_9_0._furnituresPools, iter_9_0)

			return None,
		def prepareAnim:(arg_10_0, arg_10_1)
			if not arg_10_1.animData or not arg_10_1.animTf:
				return

			local var_10_0 = arg_10_1.animData
			local var_10_1 = arg_10_1.animTf

			arg_10_1.time = arg_10_1.data.time

			local var_10_2 = GetComponent(findTF(var_10_1, "anim"), typeof(Animator))

			var_10_2.SetInteger("charIndex", arg_10_1.charIndex)

			if arg_10_1.data.type != var_0_15:
				var_10_2.SetTrigger("trigger")

			GetOrAddComponent(findTF(var_10_1, "collider"), typeof(EventTriggerListener)).AddPointDownFunc(function(arg_11_0, arg_11_1, arg_11_2)
				if arg_10_1.readyToRemove:
					return

				if arg_10_1.data.type == var_0_15 and arg_10_1.data.defaut_char_index == arg_10_1.charIndex and not arg_10_1.data.defaut_trigger:
					return

				local var_11_0 = False

				if arg_10_1.data.type == var_0_15 and arg_10_1.data.defaut_char_index == arg_10_1.charIndex:
					var_11_0 = True

				if not var_11_0:
					local var_11_1 = arg_10_0.getScore()

					pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_3)
					arg_10_0._event.emit(var_0_12, {
						score = var_11_1,
						pos = arg_11_1.position
					})

				arg_10_1.readyToRemove = True

				var_10_2.SetTrigger("next")

				arg_10_1.time = arg_10_1.data.time or 3),
		def getScore:(arg_12_0)
			if not arg_12_0.additiveScore:
				arg_12_0.additiveScore = var_0_7

			if arg_12_0.scoreTime and arg_12_0.timeStep - arg_12_0.scoreTime < var_0_8:
				arg_12_0.additiveScore = arg_12_0.additiveScore + var_0_9
			else
				arg_12_0.additiveScore = var_0_7

			if arg_12_0.additiveScore >= var_0_10:
				arg_12_0.additiveScore = var_0_10

			arg_12_0.scoreTime = arg_12_0.timeStep

			return arg_12_0.additiveScore,
		def getAnimTfByPosData:(arg_13_0, arg_13_1, arg_13_2, arg_13_3)
			local var_13_0 = arg_13_1.anim_name

			if arg_13_0._furnitureAnimTfPool and arg_13_0._furnitureAnimTfPool[var_13_0] and #arg_13_0._furnitureAnimTfPool[var_13_0] > 0:
				arg_13_3(table.remove(arg_13_0._furnitureAnimTfPool[var_13_0], 1), arg_13_2)

				return

			return arg_13_0.createAnimTf(var_13_0, arg_13_2, arg_13_3),
		def returnFurniture:(arg_14_0, arg_14_1)
			if not arg_14_1:
				return

			if arg_14_1.charIndex:
				arg_14_0.returnCharIndex(arg_14_1.charIndex)

				arg_14_1.charIndex = None

			if arg_14_1.animData and arg_14_1.animTf:
				local var_14_0 = arg_14_1.animData.name

				arg_14_0.returnAnimTf(var_14_0, arg_14_1.animTf)

			if arg_14_1.data.hide_tfs:
				for iter_14_0 = 1, #arg_14_1.data.hide_tfs:
					setActive(findTF(arg_14_1.tf, arg_14_1.data.hide_tfs[iter_14_0]), True)

			arg_14_1.animTf = None
			arg_14_1.animData = None
			arg_14_1.activeIndex = None
			arg_14_1.readyToRemove = False
			arg_14_1.time = None

			for iter_14_1 = #arg_14_0._activeFurnitures, 1, -1:
				if arg_14_0._activeFurnitures[iter_14_1] == arg_14_1:
					table.insert(arg_14_0._furnituresPools, table.remove(arg_14_0._activeFurnitures, iter_14_1))

			for iter_14_2 = #arg_14_0._unActiveFurnitures, 1, -1:
				if arg_14_0._unActiveFurnitures[iter_14_2] == arg_14_1:
					table.insert(arg_14_0._furnituresPools, table.remove(arg_14_0._unActiveFurnitures, iter_14_2))

			local var_14_1 = False

			for iter_14_3 = 1, #arg_14_0._furnituresPools:
				if arg_14_0._furnituresPools[iter_14_3] == arg_14_1:
					var_14_1 = True

			if not var_14_1:
				table.insert(arg_14_0._furnituresPools, arg_14_1),
		def returnAnimTf:(arg_15_0, arg_15_1, arg_15_2)
			if not arg_15_0._furnitureAnimTfPool[arg_15_1]:
				arg_15_0._furnitureAnimTfPool[arg_15_1] = {}

			setActive(arg_15_2, False)
			table.insert(arg_15_0._furnitureAnimTfPool[arg_15_1], arg_15_2),
		def createAnimTf:(arg_16_0, arg_16_1, arg_16_2, arg_16_3)
			local var_16_0 = var_0_40[arg_16_1]

			if not var_16_0:
				return None

			local var_16_1 = var_16_0.prefab
			local var_16_2 = var_16_0.name

			if arg_16_0._animTplDic[var_16_2]:
				arg_16_3(tf(Instantiate(arg_16_0._animTplDic[var_16_2])), arg_16_2)
			else
				LoadAndInstantiateAsync(var_0_36, var_16_1, function(arg_17_0)
					if not arg_17_0:
						print("找不到资源" .. var_16_2)

						return

					if arg_16_0.destroyFlag:
						Destroy(arg_17_0)

						return

					arg_16_0._animTplDic[var_16_2] = arg_17_0

					SetParent(tf(arg_17_0), arg_16_0._tplContainer)
					arg_16_3(tf(Instantiate(arg_16_0._animTplDic[var_16_2])), arg_16_2)),
		def getActiveIndex:(arg_18_0)
			if not arg_18_0._activeIndex:
				arg_18_0._activeIndex = 0

			arg_18_0._activeIndex = arg_18_0._activeIndex + 1

			return arg_18_0._activeIndex,
		def clear:(arg_19_0)
			for iter_19_0 = #arg_19_0._activeFurnitures, 1, -1:
				arg_19_0.returnFurniture(arg_19_0._activeFurnitures[iter_19_0])

			for iter_19_1 = #arg_19_0._unActiveFurnitures, 1, -1:
				arg_19_0.returnFurniture(arg_19_0._unActiveFurnitures[iter_19_1])

			for iter_19_2 = 1, #arg_19_0._furnituresPools:
				local var_19_0 = arg_19_0._furnituresPools[iter_19_2]

				if var_19_0.data.type == var_0_14:
					var_19_0.initFlag = False

			arg_19_0._activeFurnitures = {}
			var_0_46 = Clone(var_0_38),
		def destroy:(arg_20_0)
			arg_20_0.clear()

			for iter_20_0 = 1, #arg_20_0._furnitureAnimTfPool:
				local var_20_0 = arg_20_0._furnitureAnimTfPool[iter_20_0].animTf

				if var_20_0:
					local var_20_1 = GetOrAddComponent(findTF(var_20_0, "collider"), typeof(EventTriggerListener))

					ClearEventTrigger(var_20_1)

			arg_20_0.destroyFlag = True
	}

	var_1_0.ctor()

	return var_1_0

local var_0_48 = {
	{
		start = True,
		name = "posMoveRole_1",
		switch_parent = True,
		finish = True,
		finish_weight = 1,
		next = {
			"posMoveRole_2"
		}
	},
	{
		finish = False,
		name = "posMoveRole_2",
		start = False,
		next = {
			"posMoveRole_1",
			"posMoveRole_3",
			"posMoveRole_4"
		}
	},
	{
		finish = False,
		name = "posMoveRole_3",
		start = False,
		finish_weight = 1,
		next = {
			"posMoveRole_2",
			"posMoveRole_5"
		}
	},
	{
		finish = True,
		name = "posMoveRole_4",
		start = True,
		finish_weight = 1,
		next = {
			"posMoveRole_2"
		}
	},
	{
		finish = False,
		name = "posMoveRole_5",
		start = False,
		finish_weight = 1,
		next = {
			"posMoveRole_3",
			"posMoveRole_6",
			"posMoveRole_9"
		}
	},
	{
		finish = False,
		name = "posMoveRole_6",
		start = False,
		finish_weight = 1,
		next = {
			"posMoveRole_5",
			"posMoveRole_7",
			"posMoveRole_8"
		}
	},
	{
		start = True,
		name = "posMoveRole_7",
		switch_parent = True,
		finish = True,
		finish_weight = 1,
		next = {
			"posMoveRole_6"
		}
	},
	{
		finish = True,
		name = "posMoveRole_8",
		start = True,
		finish_weight = 1,
		next = {
			"posMoveRole_6"
		}
	},
	{
		finish = True,
		name = "posMoveRole_9",
		start = True,
		finish_weight = 1,
		next = {
			"posMoveRole_5"
		}
	}
}
local var_0_49 = {
	5,
	10
}
local var_0_50 = 300
local var_0_51 = 200

local function var_0_52(arg_21_0, arg_21_1)
	local var_21_0 = {
		def ctor:(arg_22_0)
			arg_22_0._tf = arg_21_0
			arg_22_0._event = arg_21_1
			arg_22_0._roleTf = findTF(arg_22_0._tf, "fushun")
			arg_22_0._roleAnimator = GetComponent(findTF(arg_22_0._roleTf, "img/anim"), typeof(Animator))
			arg_22_0._dftEvent = GetComponent(findTF(arg_22_0._roleTf, "img/anim"), typeof(DftAniEvent))

			arg_22_0._dftEvent.SetEndEvent(function(arg_23_0)
				setActive(arg_22_0._roleTf, False)
				arg_22_0.clear())

			arg_22_0._eventTrigger = GetOrAddComponent(findTF(arg_22_0._roleTf, "img/collider"), typeof(EventTriggerListener))

			arg_22_0._eventTrigger.AddPointDownFunc(function(arg_24_0, arg_24_1, arg_24_2)
				if arg_22_0.removeRoleFlag:
					return

				pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_3)
				arg_22_0._event.emit(var_0_12, {
					score = var_0_11,
					pos = arg_24_1.position
				})

				arg_22_0.removeRoleFlag = True

				arg_22_0.setRoleAnimatorTrigger("touch"))

			arg_22_0._roleShowData = {}
			arg_22_0._roleShowStartData = {}

			for iter_22_0 = 1, #var_0_48:
				if var_0_48[iter_22_0].start:
					table.insert(arg_22_0._roleShowStartData, Clone(var_0_48[iter_22_0]))

				local var_22_0 = Clone(var_0_48[iter_22_0])

				arg_22_0._roleShowData[var_22_0.name] = var_22_0

			arg_22_0._active = False
			arg_22_0._targetPos = Vector2(0, 0)
			arg_22_0._currentTargetData = None
			arg_22_0._currentTargetPos = None,
		def setRoleAnimatorTrigger:(arg_25_0, arg_25_1, arg_25_2)
			if not arg_25_2:
				arg_25_0._roleAnimator.SetTrigger(arg_25_1)
			else
				arg_25_0._roleAnimator.ResetTrigger(arg_25_1),
		def start:(arg_26_0)
			arg_26_0.showTime = math.random() * (var_0_49[2] - var_0_49[1]) + var_0_49[1]

			arg_26_0.clear(),
		def step:(arg_27_0)
			if arg_27_0.showTime > 0:
				arg_27_0.showTime = arg_27_0.showTime - Time.deltaTime

				if arg_27_0.showTime <= 0:
					arg_27_0.showTime = 0

					arg_27_0.checkShow()

			if arg_27_0._currentTargetData and not arg_27_0.removeRoleFlag:
				local var_27_0 = arg_27_0._roleTf.anchoredPosition
				local var_27_1 = var_0_50 * math.cos(arg_27_0._moveAngle) * Time.deltaTime
				local var_27_2 = var_0_50 * math.sin(arg_27_0._moveAngle) * Time.deltaTime

				if arg_27_0._roleDirectX == 1 and arg_27_0._roleDirectX * var_27_1 + var_27_0.x > arg_27_0._currentTargetPos.x:
					var_27_0.x = var_27_0.x + arg_27_0._roleDirectX * var_27_1
					arg_27_0._roleDirectX = None
				elif arg_27_0._roleDirectX == -1 and arg_27_0._roleDirectX * var_27_1 + var_27_0.x < arg_27_0._currentTargetPos.x:
					var_27_0.x = var_27_0.x + arg_27_0._roleDirectX * var_27_1
					arg_27_0._roleDirectX = None
				elif arg_27_0._roleDirectX:
					var_27_0.x = var_27_0.x + arg_27_0._roleDirectX * var_27_1

				if arg_27_0._roleDirectY == 1 and arg_27_0._roleDirectY * var_27_2 + var_27_0.y > arg_27_0._currentTargetPos.y:
					var_27_0.y = var_27_0.y + arg_27_0._roleDirectY * var_27_2
					arg_27_0._roleDirectY = None
				elif arg_27_0._roleDirectY == -1 and arg_27_0._roleDirectY * var_27_2 + var_27_0.y < arg_27_0._currentTargetPos.y:
					var_27_0.y = var_27_0.y + arg_27_0._roleDirectY * var_27_2
					arg_27_0._roleDirectY = None
				elif arg_27_0._roleDirectY:
					var_27_0.y = var_27_0.y + arg_27_0._roleDirectY * var_27_2

				arg_27_0._roleTf.anchoredPosition = var_27_0

				if arg_27_0._roleDirectX == None and arg_27_0._roleDirectY == None:
					arg_27_0.setRoleNext(),
		def setRoleStatus:(arg_28_0, arg_28_1)
			setActive(arg_28_0._roleTf, True)

			if arg_28_1:
				arg_28_0.setRoleAnimatorTrigger("change", True)
				arg_28_0.setRoleAnimatorTrigger("hide", True)
				arg_28_0.setRoleAnimatorTrigger("show")
			else
				arg_28_0.setRoleAnimatorTrigger("change")

			arg_28_0._roleAnimator.SetInteger("directX", arg_28_0._roleDirectX)
			arg_28_0._roleAnimator.SetInteger("directY", arg_28_0._roleDirectY),
		def setRoleNext:(arg_29_0, arg_29_1)
			if arg_29_1 or not arg_29_0._currentTargetData.finish:
				local var_29_0

				if not arg_29_1:
					var_29_0 = arg_29_0._currentData.name
					var_29_0 = arg_29_0._currentData.name
					arg_29_0._currentData = arg_29_0._currentTargetData

				local var_29_1 = Clone(arg_29_0._currentData.next)

				if var_29_0:
					for iter_29_0 = #var_29_1, 1, -1:
						if var_29_1[iter_29_0] == var_29_0:
							table.remove(var_29_1, iter_29_0)

				if #var_29_1 == 0:
					arg_29_0.clear()

					return

				local var_29_2 = var_29_1[math.random(1, #var_29_1)]

				arg_29_0._currentTargetData = arg_29_0._roleShowData[var_29_2]

				local var_29_3 = findTF(arg_29_0._tf, arg_29_0._currentData.name)
				local var_29_4 = findTF(arg_29_0._tf, arg_29_0._currentTargetData.name)

				if arg_29_0._currentTargetData and arg_29_0._currentTargetData.switch_parent:
					setParent(arg_29_0._roleTf, var_29_4)
				else
					setParent(arg_29_0._roleTf, var_29_3)

				local var_29_5 = findTF(var_29_3, "rolePos")

				arg_29_0._roleTf.anchoredPosition = var_29_5.anchoredPosition
				arg_29_0._currentTargetPos = findTF(arg_29_0._tf, arg_29_0._currentTargetData.name .. "/rolePos").anchoredPosition
				arg_29_0._roleDirectX = arg_29_0._currentTargetPos.x > arg_29_0._roleTf.anchoredPosition.x and 1 or -1
				arg_29_0._roleDirectY = arg_29_0._currentTargetPos.y > arg_29_0._roleTf.anchoredPosition.y and 1 or -1
				arg_29_0._moveAngle = math.atan(math.abs(arg_29_0._currentTargetPos.y - arg_29_0._roleTf.anchoredPosition.y) / math.abs(arg_29_0._currentTargetPos.x - arg_29_0._roleTf.anchoredPosition.x))
				arg_29_0.removeRoleFlag = False

				arg_29_0.setRoleStatus(arg_29_1)
			elif arg_29_0._currentTargetData.finish:
				arg_29_0.clear(),
		def checkShow:(arg_30_0)
			if arg_30_0._active and not table.contains(var_0_46, var_0_37):
				return

			for iter_30_0 = #var_0_46, 1, -1:
				if var_0_46[iter_30_0] == var_0_37:
					table.remove(var_0_46, iter_30_0)

			arg_30_0._active = True
			arg_30_0._currentData = arg_30_0._roleShowStartData[math.random(1, #arg_30_0._roleShowStartData)]

			arg_30_0.setRoleNext(True),
		def clear:(arg_31_0)
			arg_31_0._currentTargetData = None
			arg_31_0._currentTargetPos = None

			if not table.contains(var_0_46, var_0_37):
				table.insert(var_0_46, var_0_37)

			if isActive(arg_31_0._roleTf):
				arg_31_0.setRoleAnimatorTrigger("hide")

				arg_31_0.removeRoleFlag = True

				setActive(arg_31_0._roleTf, False)

			arg_31_0.showTime = math.random() * (var_0_49[2] - var_0_49[1]) + var_0_49[1]
			arg_31_0._active = False,
		def destroy:(arg_32_0)
			return
	}

	var_21_0.ctor()

	return var_21_0

local var_0_53 = {
	"boot00",
	"boot01",
	"boot02"
}
local var_0_54 = {
	"game00",
	"game01",
	"game02"
}
local var_0_55 = {
	"tv00",
	"tv01",
	"tv02",
	"tv03",
	"tv04",
	"tv05",
	"tv06",
	"tv07",
	"tv08",
	"tv09",
	"tv10",
	"tv11",
	"tv12",
	"tv13",
	"tv14"
}
local var_0_56 = {
	1,
	3
}

local function var_0_57(arg_33_0, arg_33_1)
	local var_33_0 = {
		def ctor:(arg_34_0)
			arg_34_0._tf = arg_33_0
			arg_34_0._event = arg_33_1
			arg_34_0.loadedFlag = False
			arg_34_0._tvTf = None
			arg_34_0._active = False
			arg_34_0._tvAnimator = None

			onButton(arg_34_0._event, findTF(arg_34_0._tf, "collider"), function()
				if arg_34_0.loadedFlag:
					return

				arg_34_0._active = not arg_34_0._active

				arg_34_0.updateUI(), SFX_CANCEL),
		def start:(arg_36_0)
			arg_36_0._active = True

			arg_36_0.updateUI()

			if not arg_36_0.loadedFlag:
				LoadAndInstantiateAsync(var_0_36, var_0_45, function(arg_37_0)
					if not arg_37_0:
						print("tv资源加载失败")

						return

					if arg_36_0.destroyFlag:
						Destroy(arg_37_0)

						return

					arg_36_0.loadedFlag = True
					arg_36_0._tvTf = tf(arg_37_0)
					arg_36_0._tvAnimator = GetComponent(findTF(arg_36_0._tvTf, "anim"), typeof(Animator))

					GetComponent(findTF(arg_36_0._tvTf, "anim"), typeof(DftAniEvent)).SetEndEvent(function()
						arg_36_0.onTvComplete())
					onButton(arg_36_0._event, findTF(arg_36_0._tvTf, "collider"), function()
						arg_36_0._active = not arg_36_0._active

						arg_36_0.updateUI())
					setParent(arg_36_0._tvTf, findTF(arg_36_0._tf, "posTv"))
					arg_36_0.updateUI()
					arg_36_0.setTvData())
			else
				arg_36_0.setTvData(),
		def setTvData:(arg_40_0)
			arg_40_0.playIndex = 1
			arg_40_0.playTvData = {}

			local var_40_0 = math.random(var_0_56[1], var_0_56[2])
			local var_40_1 = Clone(var_0_55)
			local var_40_2 = Clone(var_0_53)
			local var_40_3 = Clone(var_0_54)

			for iter_40_0 = 1, var_40_0:
				table.insert(arg_40_0.playTvData, table.remove(var_40_1, math.random(1, #var_40_1)))

			table.insert(arg_40_0.playTvData, table.remove(var_40_2, math.random(1, #var_40_2)))
			table.insert(arg_40_0.playTvData, table.remove(var_40_3, math.random(1, #var_40_3)))
			arg_40_0._tvAnimator.Play(arg_40_0.playTvData[arg_40_0.playIndex], -1, 0),
		def onTvComplete:(arg_41_0)
			if not arg_41_0.playIndex and not arg_41_0.playTvData and #arg_41_0.playTvData == 0:
				return

			if arg_41_0._tvAnimator:
				arg_41_0.playIndex = arg_41_0.playIndex + 1

				if arg_41_0.playIndex > #arg_41_0.playTvData:
					arg_41_0.playIndex = #arg_41_0.playTvData

				arg_41_0._tvAnimator.Play(arg_41_0.playTvData[arg_41_0.playIndex], -1, 0),
		def step:(arg_42_0)
			if arg_42_0._tvAnimator and arg_42_0._tvAnimator.speed == 0:
				arg_42_0._tvAnimator.speed = 1,
		def pause:(arg_43_0)
			if arg_43_0._tvAnimator:
				arg_43_0._tvAnimator.speed = 0,
		def updateUI:(arg_44_0)
			if arg_44_0.loadedFlag:
				setActive(findTF(arg_44_0._tf, "on"), False)
				setActive(findTF(arg_44_0._tf, "off"), False)

				if not arg_44_0.tvCanvas:
					arg_44_0.tvCanvas = GetComponent(findTF(arg_44_0._tvTf, "anim"), typeof(CanvasGroup))

				arg_44_0.tvCanvas.alpha = arg_44_0._active and 1 or 0
			else
				setActive(findTF(arg_44_0._tf, "on"), arg_44_0._active)
				setActive(findTF(arg_44_0._tf, "off"), not arg_44_0._active),
		def destroy:(arg_45_0)
			arg_45_0.destroyFlag = True,
		def clear:(arg_46_0)
			return
	}

	var_33_0.ctor()

	return var_33_0

def var_0_0.getUIName(arg_47_0):
	return "HideSeekGameUI"

def var_0_0.getBGM(arg_48_0):
	return var_0_1

def var_0_0.didEnter(arg_49_0):
	arg_49_0.initEvent()
	arg_49_0.initData()
	arg_49_0.initUI()
	arg_49_0.initGameUI()
	arg_49_0.initController()
	arg_49_0.updateMenuUI()
	arg_49_0.openMenuUI()

def var_0_0.initEvent(arg_50_0):
	if not arg_50_0.uiCam:
		arg_50_0.uiCam = GameObject.Find("UICamera").GetComponent("Camera")

	arg_50_0.bind(var_0_12, function(arg_51_0, arg_51_1, arg_51_2)
		arg_50_0.addScore(arg_51_1.score)
		arg_50_0.showScore(arg_51_1))

def var_0_0.showScore(arg_52_0, arg_52_1):
	local var_52_0

	if #arg_52_0.showScoresPool > 0:
		var_52_0 = table.remove(arg_52_0.showScoresPool, 1)
	else
		var_52_0 = tf(Instantiate(arg_52_0.showScoreTpl))

		setParent(var_52_0, arg_52_0.sceneFrontContainer)
		GetComponent(findTF(var_52_0, "anim"), typeof(DftAniEvent)).SetEndEvent(function()
			for iter_53_0 = #arg_52_0.showScores, 1, -1:
				if var_52_0 == arg_52_0.showScores[iter_53_0]:
					table.insert(arg_52_0.showScoresPool, table.remove(arg_52_0.showScores, iter_53_0)))

	setText(findTF(var_52_0, "anim"), "+" .. tostring(arg_52_1.score))

	local var_52_1 = arg_52_0.uiCam.ScreenToWorldPoint(arg_52_1.pos)

	var_52_0.anchoredPosition = arg_52_0.sceneFrontContainer.InverseTransformPoint(var_52_1)

	setActive(var_52_0, False)
	setActive(var_52_0, True)
	table.insert(arg_52_0.showScores, var_52_0)

def var_0_0.onEventHandle(arg_54_0, arg_54_1):
	return

def var_0_0.initData(arg_55_0):
	local var_55_0 = Application.targetFrameRate or 60

	if var_55_0 > 60:
		var_55_0 = 60

	arg_55_0.timer = Timer.New(function()
		arg_55_0.onTimer(), 1 / var_55_0, -1)
	arg_55_0.showScores = {}
	arg_55_0.showScoresPool = {}

def var_0_0.initUI(arg_57_0):
	arg_57_0.backSceneTf = findTF(arg_57_0._tf, "scene_background")
	arg_57_0.sceneContainer = findTF(arg_57_0._tf, "sceneMask/sceneContainer")
	arg_57_0.sceneFrontContainer = findTF(arg_57_0._tf, "sceneMask/sceneContainer/scene_front")
	arg_57_0.clickMask = findTF(arg_57_0._tf, "clickMask")
	arg_57_0.bg = findTF(arg_57_0._tf, "bg")
	arg_57_0.countUI = findTF(arg_57_0._tf, "pop/CountUI")
	arg_57_0.countAnimator = GetComponent(findTF(arg_57_0.countUI, "count"), typeof(Animator))
	arg_57_0.countDft = GetOrAddComponent(findTF(arg_57_0.countUI, "count"), typeof(DftAniEvent))

	arg_57_0.countDft.SetTriggerEvent(function()
		return)
	arg_57_0.countDft.SetEndEvent(function()
		setActive(arg_57_0.countUI, False)
		arg_57_0.gameStart())

	arg_57_0.leaveUI = findTF(arg_57_0._tf, "pop/LeaveUI")

	onButton(arg_57_0, findTF(arg_57_0.leaveUI, "ad/btnOk"), function()
		arg_57_0.resumeGame()
		arg_57_0.onGameOver(), SFX_CANCEL)
	onButton(arg_57_0, findTF(arg_57_0.leaveUI, "ad/btnCancel"), function()
		arg_57_0.resumeGame(), SFX_CANCEL)

	arg_57_0.pauseUI = findTF(arg_57_0._tf, "pop/pauseUI")

	onButton(arg_57_0, findTF(arg_57_0.pauseUI, "ad/btnOk"), function()
		setActive(arg_57_0.pauseUI, False)
		arg_57_0.resumeGame(), SFX_CANCEL)

	arg_57_0.settlementUI = findTF(arg_57_0._tf, "pop/SettleMentUI")

	onButton(arg_57_0, findTF(arg_57_0.settlementUI, "ad/btnOver"), function()
		setActive(arg_57_0.settlementUI, False)
		arg_57_0.openMenuUI(), SFX_CANCEL)

	arg_57_0.menuUI = findTF(arg_57_0._tf, "pop/menuUI")
	arg_57_0.battleScrollRect = GetComponent(findTF(arg_57_0.menuUI, "battList"), typeof(ScrollRect))
	arg_57_0.totalTimes = arg_57_0.getGameTotalTime()

	local var_57_0 = arg_57_0.getGameUsedTimes() - 4 < 0 and 0 or arg_57_0.getGameUsedTimes() - 4

	scrollTo(arg_57_0.battleScrollRect, 0, 1 - var_57_0 / (arg_57_0.totalTimes - 4))
	onButton(arg_57_0, findTF(arg_57_0.menuUI, "rightPanelBg/arrowUp"), function()
		local var_64_0 = arg_57_0.battleScrollRect.normalizedPosition.y + 1 / (arg_57_0.totalTimes - 4)

		if var_64_0 > 1:
			var_64_0 = 1

		scrollTo(arg_57_0.battleScrollRect, 0, var_64_0), SFX_CANCEL)
	onButton(arg_57_0, findTF(arg_57_0.menuUI, "rightPanelBg/arrowDown"), function()
		local var_65_0 = arg_57_0.battleScrollRect.normalizedPosition.y - 1 / (arg_57_0.totalTimes - 4)

		if var_65_0 < 0:
			var_65_0 = 0

		scrollTo(arg_57_0.battleScrollRect, 0, var_65_0), SFX_CANCEL)
	onButton(arg_57_0, findTF(arg_57_0.menuUI, "btnBack"), function()
		arg_57_0.closeView(), SFX_CANCEL)
	onButton(arg_57_0, findTF(arg_57_0.menuUI, "btnRule"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.five_duomaomao.tip
		}), SFX_CANCEL)
	onButton(arg_57_0, findTF(arg_57_0.menuUI, "btnStart"), function()
		setActive(arg_57_0.menuUI, False)
		arg_57_0.readyStart(), SFX_CANCEL)

	local var_57_1 = findTF(arg_57_0.menuUI, "tplBattleItem")

	arg_57_0.battleItems = {}

	for iter_57_0 = 1, 7:
		local var_57_2 = tf(instantiate(var_57_1))

		var_57_2.name = "battleItem_" .. iter_57_0

		setParent(var_57_2, findTF(arg_57_0.menuUI, "battList/Viewport/Content"))

		local var_57_3 = iter_57_0

		GetSpriteFromAtlasAsync("ui/minigameui/" .. var_0_4, "battleDesc" .. var_57_3, function(arg_69_0)
			setImageSprite(findTF(var_57_2, "state_open/buttomDesc"), arg_69_0, True)
			setImageSprite(findTF(var_57_2, "state_clear/buttomDesc"), arg_69_0, True)
			setImageSprite(findTF(var_57_2, "state_current/buttomDesc"), arg_69_0, True)
			setImageSprite(findTF(var_57_2, "state_closed/buttomDesc"), arg_69_0, True))
		setActive(var_57_2, True)
		table.insert(arg_57_0.battleItems, var_57_2)

	if not arg_57_0.handle and IsUnityEditor:
		arg_57_0.handle = UpdateBeat.CreateListener(arg_57_0.Update, arg_57_0)

		UpdateBeat.AddListener(arg_57_0.handle)

def var_0_0.initGameUI(arg_70_0):
	arg_70_0.gameUI = findTF(arg_70_0._tf, "ui/gameUI")
	arg_70_0.showScoreTpl = findTF(arg_70_0.sceneFrontContainer, "score")

	setActive(arg_70_0.showScoreTpl, False)
	onButton(arg_70_0, findTF(arg_70_0.gameUI, "topRight/btnStop"), function()
		arg_70_0.stopGame()
		setActive(arg_70_0.pauseUI, True))
	onButton(arg_70_0, findTF(arg_70_0.gameUI, "btnLeave"), function()
		arg_70_0.stopGame()
		setActive(arg_70_0.leaveUI, True))

	arg_70_0.gameTimeS = findTF(arg_70_0.gameUI, "top/time/s")
	arg_70_0.scoreTf = findTF(arg_70_0.gameUI, "top/score")
	arg_70_0.sceneContainer.anchoredPosition = Vector2(0, 0)

	local var_70_0 = GetOrAddComponent(arg_70_0.sceneContainer, typeof(EventTriggerListener))
	local var_70_1
	local var_70_2

	arg_70_0.velocityXSmoothing = Vector2(0, 0)
	arg_70_0.offsetPosition = arg_70_0.sceneContainer.anchoredPosition

	var_70_0.AddBeginDragFunc(function(arg_73_0, arg_73_1)
		var_70_1 = arg_73_1.position
		var_70_2 = arg_70_0.sceneContainer.anchoredPosition
		arg_70_0.velocityXSmoothing = Vector2(0, 0)
		arg_70_0.offsetPosition = arg_70_0.sceneContainer.anchoredPosition)
	var_70_0.AddDragFunc(function(arg_74_0, arg_74_1)
		arg_70_0.offsetPosition.x = arg_74_1.position.x - var_70_1.x + var_70_2.x
		arg_70_0.offsetPosition.y = arg_74_1.position.y - var_70_1.y + var_70_2.y
		arg_70_0.offsetPosition.x = arg_70_0.offsetPosition.x > var_0_42[2] and var_0_42[2] or arg_70_0.offsetPosition.x
		arg_70_0.offsetPosition.x = arg_70_0.offsetPosition.x < var_0_42[1] and var_0_42[1] or arg_70_0.offsetPosition.x
		arg_70_0.offsetPosition.y = arg_70_0.offsetPosition.y > var_0_43[2] and var_0_43[2] or arg_70_0.offsetPosition.y
		arg_70_0.offsetPosition.y = arg_70_0.offsetPosition.y < var_0_43[1] and var_0_43[1] or arg_70_0.offsetPosition.y)
	var_70_0.AddDragEndFunc(function(arg_75_0, arg_75_1)
		return)

def var_0_0.initController(arg_76_0):
	arg_76_0.furnitureCtrl = var_0_47(findTF(arg_76_0.sceneContainer, "scene"), arg_76_0)
	arg_76_0.moveRoleCtrl = var_0_52(findTF(arg_76_0.sceneContainer, "scene"), arg_76_0)
	arg_76_0.tvCtrl = var_0_57(findTF(arg_76_0.sceneContainer, "scene/furniture_tv"), arg_76_0)

def var_0_0.Update(arg_77_0):
	arg_77_0.AddDebugInput()

def var_0_0.AddDebugInput(arg_78_0):
	if arg_78_0.gameStop or arg_78_0.settlementFlag:
		return

	if IsUnityEditor and Input.GetKeyDown(KeyCode.S):
		-- block empty

def var_0_0.updateMenuUI(arg_79_0):
	local var_79_0 = arg_79_0.getGameUsedTimes()
	local var_79_1 = arg_79_0.getGameTimes()

	for iter_79_0 = 1, #arg_79_0.battleItems:
		setActive(findTF(arg_79_0.battleItems[iter_79_0], "state_open"), False)
		setActive(findTF(arg_79_0.battleItems[iter_79_0], "state_closed"), False)
		setActive(findTF(arg_79_0.battleItems[iter_79_0], "state_clear"), False)
		setActive(findTF(arg_79_0.battleItems[iter_79_0], "state_current"), False)

		if iter_79_0 <= var_79_0:
			setActive(findTF(arg_79_0.battleItems[iter_79_0], "state_clear"), True)
		elif iter_79_0 == var_79_0 + 1 and var_79_1 >= 1:
			setActive(findTF(arg_79_0.battleItems[iter_79_0], "state_current"), True)
		elif var_79_0 < iter_79_0 and iter_79_0 <= var_79_0 + var_79_1:
			setActive(findTF(arg_79_0.battleItems[iter_79_0], "state_open"), True)
		else
			setActive(findTF(arg_79_0.battleItems[iter_79_0], "state_closed"), True)

	arg_79_0.totalTimes = arg_79_0.getGameTotalTime()

	local var_79_2 = 1 - (arg_79_0.getGameUsedTimes() - 3 < 0 and 0 or arg_79_0.getGameUsedTimes() - 3) / (arg_79_0.totalTimes - 4)

	if var_79_2 > 1:
		var_79_2 = 1

	scrollTo(arg_79_0.battleScrollRect, 0, var_79_2)
	setActive(findTF(arg_79_0.menuUI, "btnStart/tip"), var_79_1 > 0)
	arg_79_0.CheckGet()

def var_0_0.CheckGet(arg_80_0):
	setActive(findTF(arg_80_0.menuUI, "got"), False)

	if arg_80_0.getUltimate() and arg_80_0.getUltimate() != 0:
		setActive(findTF(arg_80_0.menuUI, "got"), True)

	if arg_80_0.getUltimate() == 0:
		if arg_80_0.getGameTotalTime() > arg_80_0.getGameUsedTimes():
			return

		pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = arg_80_0.GetMGHubData().id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})
		setActive(findTF(arg_80_0.menuUI, "got"), True)

def var_0_0.openMenuUI(arg_81_0):
	setActive(findTF(arg_81_0.sceneContainer, "scene_front"), False)
	setActive(findTF(arg_81_0.sceneContainer, "scene_background"), False)
	setActive(findTF(arg_81_0.sceneContainer, "scene"), False)
	setActive(arg_81_0.gameUI, False)
	setActive(arg_81_0.menuUI, True)
	setActive(arg_81_0.bg, True)
	arg_81_0.updateMenuUI()

def var_0_0.clearUI(arg_82_0):
	setActive(arg_82_0.sceneContainer, False)
	setActive(arg_82_0.settlementUI, False)
	setActive(arg_82_0.countUI, False)
	setActive(arg_82_0.menuUI, False)
	setActive(arg_82_0.gameUI, False)

def var_0_0.readyStart(arg_83_0):
	setActive(arg_83_0.countUI, True)
	arg_83_0.countAnimator.Play("count")
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_2)

def var_0_0.gameStart(arg_84_0):
	setActive(findTF(arg_84_0.sceneContainer, "scene_front"), True)
	setActive(findTF(arg_84_0.sceneContainer, "scene_background"), True)
	setActive(findTF(arg_84_0.sceneContainer, "scene"), True)
	setActive(arg_84_0.bg, False)

	arg_84_0.sceneContainer.anchoredPosition = var_0_44
	arg_84_0.offsetPosition = var_0_44

	setActive(arg_84_0.gameUI, True)

	arg_84_0.gameStartFlag = True
	arg_84_0.scoreNum = 0
	arg_84_0.nextPositionIndex = 2
	arg_84_0.gameStepTime = 0
	arg_84_0.heart = 3
	arg_84_0.gameTime = var_0_5

	for iter_84_0 = #arg_84_0.showScores, 1, -1:
		if not table.contains(arg_84_0.showScoresPool, arg_84_0.showScores[iter_84_0]):
			local var_84_0 = table.remove(arg_84_0.showScores, iter_84_0)

			table.insert(arg_84_0.showScoresPool, var_84_0)

	for iter_84_1 = #arg_84_0.showScoresPool, 1, -1:
		setActive(arg_84_0.showScoresPool[iter_84_1], False)

	arg_84_0.updateGameUI()
	arg_84_0.timerStart()
	arg_84_0.controllerStart()

def var_0_0.controllerStart(arg_85_0):
	if arg_85_0.furnitureCtrl:
		arg_85_0.furnitureCtrl.start()

	if arg_85_0.moveRoleCtrl:
		arg_85_0.moveRoleCtrl.start()

	if arg_85_0.tvCtrl:
		arg_85_0.tvCtrl.start()

def var_0_0.getGameTimes(arg_86_0):
	return arg_86_0.GetMGHubData().count

def var_0_0.getGameUsedTimes(arg_87_0):
	return arg_87_0.GetMGHubData().usedtime

def var_0_0.getUltimate(arg_88_0):
	return arg_88_0.GetMGHubData().ultimate

def var_0_0.getGameTotalTime(arg_89_0):
	return (arg_89_0.GetMGHubData().getConfig("reward_need"))

def var_0_0.changeSpeed(arg_90_0, arg_90_1):
	return

def var_0_0.onTimer(arg_91_0):
	arg_91_0.gameStep()

def var_0_0.gameStep(arg_92_0):
	arg_92_0.gameTime = arg_92_0.gameTime - Time.deltaTime

	if arg_92_0.gameTime < 0:
		arg_92_0.gameTime = 0

	arg_92_0.gameStepTime = arg_92_0.gameStepTime + Time.deltaTime

	arg_92_0.controllerStep()
	arg_92_0.updateGameUI()

	if arg_92_0.gameTime <= 0:
		arg_92_0.onGameOver()

		return

def var_0_0.controllerStep(arg_93_0):
	if arg_93_0.furnitureCtrl:
		arg_93_0.furnitureCtrl.step()

	if arg_93_0.moveRoleCtrl:
		arg_93_0.moveRoleCtrl.step()

	if arg_93_0.tvCtrl:
		arg_93_0.tvCtrl.step()

def var_0_0.timerStart(arg_94_0):
	if not arg_94_0.timer.running:
		arg_94_0.timer.Start()

def var_0_0.timerStop(arg_95_0):
	if arg_95_0.timer.running:
		arg_95_0.timer.Stop()

		if arg_95_0.tvCtrl:
			arg_95_0.tvCtrl.pause()

def var_0_0.updateGameUI(arg_96_0):
	setText(arg_96_0.scoreTf, arg_96_0.scoreNum)
	setText(arg_96_0.gameTimeS, math.ceil(arg_96_0.gameTime))

	arg_96_0.sceneContainer.anchoredPosition, arg_96_0.velocityXSmoothing = Vector2.SmoothDamp(arg_96_0.sceneContainer.anchoredPosition, arg_96_0.offsetPosition, arg_96_0.velocityXSmoothing, var_0_41)

def var_0_0.addScore(arg_97_0, arg_97_1):
	arg_97_0.scoreNum = arg_97_0.scoreNum + arg_97_1

	if arg_97_0.scoreNum < 0:
		arg_97_0.scoreNum = 0

def var_0_0.onGameOver(arg_98_0):
	if arg_98_0.settlementFlag:
		return

	arg_98_0.timerStop()

	arg_98_0.settlementFlag = True

	setActive(arg_98_0.clickMask, True)
	LeanTween.delayedCall(go(arg_98_0._tf), 0.1, System.Action(function()
		arg_98_0.settlementFlag = False
		arg_98_0.gameStartFlag = False

		setActive(arg_98_0.clickMask, False)
		arg_98_0.showSettlement()))

def var_0_0.showSettlement(arg_100_0):
	setActive(arg_100_0.settlementUI, True)
	GetComponent(findTF(arg_100_0.settlementUI, "ad"), typeof(Animator)).Play("settlement", -1, 0)

	local var_100_0 = arg_100_0.GetMGData().GetRuntimeData("elements")
	local var_100_1 = arg_100_0.scoreNum
	local var_100_2 = var_100_0 and #var_100_0 > 0 and var_100_0[1] or 0

	setActive(findTF(arg_100_0.settlementUI, "ad/new"), var_100_2 < var_100_1)

	if var_100_2 <= var_100_1:
		var_100_2 = var_100_1

		arg_100_0.StoreDataToServer({
			var_100_2
		})

	local var_100_3 = findTF(arg_100_0.settlementUI, "ad/highText")
	local var_100_4 = findTF(arg_100_0.settlementUI, "ad/currentText")

	setText(var_100_3, var_100_2)
	setText(var_100_4, var_100_1)

	if arg_100_0.getGameTimes() and arg_100_0.getGameTimes() > 0:
		arg_100_0.sendSuccessFlag = True

		arg_100_0.SendSuccess(0)

def var_0_0.resumeGame(arg_101_0):
	arg_101_0.gameStop = False

	setActive(arg_101_0.leaveUI, False)
	arg_101_0.changeSpeed(1)
	arg_101_0.timerStart()

def var_0_0.stopGame(arg_102_0):
	arg_102_0.gameStop = True

	arg_102_0.timerStop()
	arg_102_0.changeSpeed(0)

def var_0_0.onBackPressed(arg_103_0):
	if not arg_103_0.gameStartFlag:
		arg_103_0.emit(var_0_0.ON_BACK_PRESSED)
	else
		if arg_103_0.settlementFlag:
			return

		if isActive(arg_103_0.pauseUI):
			setActive(arg_103_0.pauseUI, False)

		arg_103_0.stopGame()
		setActive(arg_103_0.leaveUI, True)

def var_0_0.willExit(arg_104_0):
	if arg_104_0.handle:
		UpdateBeat.RemoveListener(arg_104_0.handle)

	if arg_104_0._tf and LeanTween.isTweening(go(arg_104_0._tf)):
		LeanTween.cancel(go(arg_104_0._tf))

	arg_104_0.destroyController()

	if arg_104_0.timer and arg_104_0.timer.running:
		arg_104_0.timer.Stop()

	Time.timeScale = 1
	arg_104_0.timer = None

def var_0_0.destroyController(arg_105_0):
	if arg_105_0.furnitureCtrl:
		arg_105_0.furnitureCtrl.destroy()

	if arg_105_0.moveRoleCtrl:
		arg_105_0.moveRoleCtrl.destroy()

	if arg_105_0.tvCtrl:
		arg_105_0.tvCtrl.destroy()

return var_0_0
