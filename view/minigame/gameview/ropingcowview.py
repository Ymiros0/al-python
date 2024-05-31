local var_0_0 = class("IdolMasterView", import("..BaseMiniGameView"))
local var_0_1 = "backyard"
local var_0_2 = "event./ui/ddldaoshu2"
local var_0_3 = "event./ui/sou"
local var_0_4 = "event./ui/xueqiu"
local var_0_5 = 60
local var_0_6 = 100
local var_0_7 = 10
local var_0_8 = {
	{
		20,
		3
	},
	{
		40,
		4
	},
	{
		60,
		5
	},
	{
		10000,
		5
	}
}
local var_0_9 = {
	{
		10700031,
		10700030
	},
	{
		10700041,
		10700040
	},
	{
		10700051,
		10700050
	},
	{
		10700061,
		10700060
	},
	{
		10700071,
		10700070
	}
}
local var_0_10 = {
	{
		10700011,
		10700010
	},
	{
		10700021,
		10700020
	}
}
local var_0_11 = "EVENT_SEND_GIFT"
local var_0_12 = "EVENT_FANS_ACTION"
local var_0_13 = {
	1,
	2,
	3,
	4,
	5,
	6
}
local var_0_14 = {
	1,
	2
}
local var_0_15 = {
	3,
	4,
	5,
	6
}
local var_0_16 = 3
local var_0_17 = "dafuweng_event"
local var_0_18 = "stand2"
local var_0_19 = "normal"
local var_0_20 = "work"
local var_0_21 = "wrong"
local var_0_22 = "end1"
local var_0_23 = "end2"
local var_0_24 = "gift"
local var_0_25 = "normal"
local var_0_26 = "walk"
local var_0_27 = 3
local var_0_28 = "type_fans_fail"
local var_0_29 = "type_fans_success"
local var_0_30 = 4
local var_0_31 = {
	Vector3(160, 160),
	Vector3(160, -30),
	Vector3(160, -210),
	Vector3(160, -400)
}
local var_0_32 = 350

local function var_0_33(arg_1_0, arg_1_1, arg_1_2)
	local var_1_0 = {
		def Ctor:(arg_2_0)
			arg_2_0._giftTf = arg_1_0
			arg_2_0._event = arg_1_2
			arg_2_0._workerTf = arg_1_1

			local var_2_0 = "jiu-work"

			PoolMgr.GetInstance().GetSpineChar(var_2_0, True, function(arg_3_0)
				arg_3_0.transform.localScale = Vector3.one
				arg_3_0.transform.localPosition = Vector3.zero

				arg_3_0.transform.SetParent(arg_2_0._workerTf, False)

				local var_3_0 = arg_3_0.GetComponent(typeof(SpineAnimUI))

				arg_2_0.wokerSpine = {
					model = arg_2_0.model,
					anim = var_3_0,
					name = var_2_0
				}

				arg_2_0.changeWorkerAction(var_0_19, 0, None))

			arg_2_0.selectedGifts = {}
			arg_2_0.gifts = {}
			arg_2_0.delegateGifts = {}

			for iter_2_0 = 1, #var_0_13:
				local var_2_1 = iter_2_0
				local var_2_2 = findTF(arg_2_0._giftTf, var_0_13[iter_2_0])

				table.insert(arg_2_0.gifts, {
					tf = var_2_2,
					index = iter_2_0
				})

				local var_2_3 = GetOrAddComponent(var_2_2, "EventTriggerListener")

				var_2_3.AddPointDownFunc(function(arg_4_0, arg_4_1)
					arg_2_0.selectGift(var_2_1))
				table.insert(arg_2_0.delegateGifts, var_2_3)

			arg_2_0.updateSelected(),
		def changeWorkerAction:(arg_5_0, arg_5_1, arg_5_2, arg_5_3)
			arg_5_0.wokerSpine.anim.SetActionCallBack(None)
			arg_5_0.wokerSpine.anim.SetAction(arg_5_1, 0)
			arg_5_0.wokerSpine.anim.SetActionCallBack(function(arg_6_0)
				if arg_6_0 == "finish":
					if arg_5_2 == 1:
						arg_5_0.wokerSpine.anim.SetActionCallBack(None)
						arg_5_0.wokerSpine.anim.SetAction(var_0_19, 0)

					if arg_5_3:
						arg_5_3())

			if arg_5_2 != 1 and arg_5_3:
				arg_5_3(),
		def selectGift:(arg_7_0, arg_7_1)
			if table.contains(var_0_14, arg_7_1):
				for iter_7_0 = #arg_7_0.selectedGifts, 1, -1:
					local var_7_0 = arg_7_0.selectedGifts[iter_7_0]

					if table.contains(var_0_14, var_7_0) and var_7_0 != arg_7_1:
						table.remove(arg_7_0.selectedGifts, iter_7_0)
			elif #arg_7_0.selectedGifts == 2 and not table.contains(arg_7_0.selectedGifts, arg_7_1):
				local var_7_1 = False

				for iter_7_1 = 1, #arg_7_0.selectedGifts:
					if table.contains(var_0_14, arg_7_0.selectedGifts[iter_7_1]):
						var_7_1 = True

						break

				if not var_7_1:
					table.remove(arg_7_0.selectedGifts, 1)

			local var_7_2 = 0

			for iter_7_2 = 1, #arg_7_0.selectedGifts:
				if arg_7_0.selectedGifts[iter_7_2] == arg_7_1:
					var_7_2 = iter_7_2

			if var_7_2 == 0:
				table.insert(arg_7_0.selectedGifts, arg_7_1)
				arg_7_0.moveJiujiu(arg_7_1)
				arg_7_0.changeWorkerAction(var_0_20, 1)
			else
				table.remove(arg_7_0.selectedGifts, var_7_2)

			if #arg_7_0.selectedGifts >= var_0_16:
				arg_7_0._event.emit(var_0_11, Clone(arg_7_0.selectedGifts), function(arg_8_0)
					if not arg_8_0:
						arg_7_0.changeWorkerAction(var_0_21, 1))

				arg_7_0.selectedGifts = {}

				arg_7_0.moveJiujiu(-1)

			arg_7_0.updateSelected(),
		def start:(arg_9_0)
			arg_9_0.selectedGifts = {}

			arg_9_0.updateSelected(),
		def updateSelected:(arg_10_0)
			for iter_10_0 = 1, #arg_10_0.gifts:
				local var_10_0 = arg_10_0.gifts[iter_10_0].index

				if table.contains(arg_10_0.selectedGifts, var_10_0):
					setActive(findTF(arg_10_0.gifts[iter_10_0].tf, "selected"), True)
				else
					setActive(findTF(arg_10_0.gifts[iter_10_0].tf, "selected"), False),
		def moveJiujiu:(arg_11_0, arg_11_1)
			if arg_11_1 == -1:
				arg_11_0._workerTf.anchoredPosition = Vector3.New(-290, 30, 0)
				arg_11_0._workerTf.localScale = Vector3.New(-1, 1, 1)
			else
				local var_11_0 = arg_11_0.gifts[arg_11_1].tf
				local var_11_1 = arg_11_0._workerTf.parent.InverseTransformPoint(var_11_0.position)

				var_11_1.x = var_11_1.x + 150
				var_11_1.y = var_11_1.y - 50
				arg_11_0._workerTf.anchoredPosition = var_11_1
				arg_11_0._workerTf.localScale = Vector3.New(1, 1, 1),
		def destroy:(arg_12_0)
			if arg_12_0.delegateGifts and #arg_12_0.delegateGifts > 0:
				for iter_12_0 = 1, #arg_12_0.delegateGifts:
					ClearEventTrigger(arg_12_0.delegateGifts[iter_12_0])

				arg_12_0.delegateGifts = {}

			PoolMgr.GetInstance().ReturnSpineChar(arg_12_0.wokerSpine.name, arg_12_0.wokerSpine.model)
	}

	var_1_0.Ctor()

	return var_1_0

local function var_0_34(arg_13_0, arg_13_1, arg_13_2, arg_13_3)
	local var_13_0 = {
		def Ctor:(arg_14_0)
			arg_14_0._groupTf = arg_13_1
			arg_14_0._groupIndex = arg_13_2
			arg_14_0._groupTf.anchoredPosition = var_0_31[arg_13_2]
			arg_14_0._event = arg_13_3
			arg_14_0.modelData = {}

			SetActive(arg_14_0._groupTf, True)
			arg_14_0.createIdol(arg_13_0[1], arg_13_0[2])

			arg_14_0.fans = {}
			arg_14_0.wantedData = {},
		def createIdol:(arg_15_0, arg_15_1, arg_15_2)
			local var_15_0 = Ship.New({
				configId = arg_15_1,
				skin_id = arg_15_2
			}).getPrefab()

			PoolMgr.GetInstance().GetSpineChar(var_15_0, True, function(arg_16_0)
				arg_16_0.transform.localScale = Vector3.one
				arg_16_0.transform.localPosition = Vector3.zero

				arg_16_0.transform.SetParent(findTF(arg_15_0._groupTf, "idolPos"), False)

				local var_16_0 = arg_16_0.GetComponent(typeof(SpineAnimUI))

				arg_15_0.modelData = {
					model = arg_15_0.model,
					id = arg_15_1,
					skinId = arg_15_2,
					anim = var_16_0
				}

				arg_15_0.changeCharAction(var_0_18, 0, None)),
		def changeCharAction:(arg_17_0, arg_17_1, arg_17_2, arg_17_3)
			if arg_17_0.modelData.actionName == arg_17_1:
				return

			arg_17_0.modelData.actionName = arg_17_1

			arg_17_0.modelData.anim.SetActionCallBack(None)
			arg_17_0.modelData.anim.SetAction(arg_17_1, 0)
			arg_17_0.modelData.anim.SetActionCallBack(function(arg_18_0)
				if arg_18_0 == "finish":
					if arg_17_2 == 1:
						arg_17_0.modelData.anim.SetActionCallBack(None)
						arg_17_0.modelData.anim.SetAction(var_0_18, 0)

					if arg_17_3:
						arg_17_3())

			if arg_17_2 != 1 and arg_17_3:
				arg_17_3(),
		def createFans:(arg_19_0, arg_19_1)
			SetActive(arg_19_1, True)
			SetParent(arg_19_1, findTF(arg_19_0._groupTf, "fansPos"))

			if #arg_19_0.fans > 0:
				local var_19_0 = arg_19_0.fans[#arg_19_0.fans].tf.anchoredPosition

				var_19_0.x = var_19_0.x + var_0_32 + math.random() * 200 + 150
				arg_19_1.anchoredPosition = Vector3.New(var_19_0.x, var_19_0.y, var_19_0.z)
			else
				arg_19_1.anchoredPosition = Vector3.New((#arg_19_0.fans + 1) * var_0_32 + 200, 0, 0)

			table.insert(arg_19_0.fans, {
				tf = arg_19_1,
				speed = math.random() + 2.5
			})

			local var_19_1 = arg_19_0.fans[#arg_19_0.fans]
			local var_19_2 = "jiu-fan" .. math.random(1, 4)

			PoolMgr.GetInstance().GetSpineChar(var_19_2, True, function(arg_20_0)
				arg_20_0.transform.localScale = Vector3.one
				arg_20_0.transform.localPosition = Vector3.zero

				arg_20_0.transform.SetParent(findTF(var_19_1.tf, "spinePos"), False)

				local var_20_0 = arg_20_0.GetComponent(typeof(SpineAnimUI))

				var_19_1.modelData = {
					model = arg_20_0,
					anim = var_20_0,
					modelName = var_19_2
				}),
		def changeFansAction:(arg_21_0, arg_21_1, arg_21_2, arg_21_3, arg_21_4)
			if not arg_21_1.modelData or arg_21_1.modelData.actionName == arg_21_2:
				return

			arg_21_1.modelData.actionName = arg_21_2

			arg_21_1.modelData.anim.SetActionCallBack(None)
			arg_21_1.modelData.anim.SetAction(arg_21_2, 0)
			arg_21_1.modelData.anim.SetActionCallBack(function(arg_22_0)
				if arg_22_0 == "finish":
					if arg_21_3 == 1:
						arg_21_1.modelData.anim.SetActionCallBack(None)
						arg_21_1.modelData.anim.SetAction(var_0_25, 0)

					if arg_21_4:
						arg_21_4())

			if arg_21_3 != 1 and arg_21_4:
				arg_21_4(),
		def getWantedGifts:(arg_23_0)
			if #arg_23_0.fans > 0 and arg_23_0.fans[1].gifts and not arg_23_0.fans[1].leave:
				return arg_23_0.fans[1].gifts

			return None,
		def clearFans:(arg_24_0)
			for iter_24_0 = 1, #arg_24_0.fans:
				PoolMgr.GetInstance().ReturnSpineChar(arg_24_0.fans[iter_24_0].modelData.modelName, arg_24_0.fans[iter_24_0].modelData.model)
				Destroy(arg_24_0.fans[iter_24_0].tf)

			arg_24_0.fans = {},
		def start:(arg_25_0)
			return,
		def step:(arg_26_0, arg_26_1)
			arg_26_0.stepTime = arg_26_1

			for iter_26_0 = #arg_26_0.fans, 1, -1:
				local var_26_0 = arg_26_0.fans[iter_26_0]
				local var_26_1 = var_26_0.tf
				local var_26_2 = var_26_0.tf.anchoredPosition

				if var_26_2.x > (iter_26_0 - 1) * var_0_32:
					var_26_2.x = var_26_2.x - var_26_0.speed
					var_26_0.tf.anchoredPosition = var_26_2

					arg_26_0.changeFansAction(var_26_0, var_0_26, 0, None)
				elif iter_26_0 == 1 and not var_26_0.leave:
					if var_26_0.gifts == None:
						var_26_0.gifts = arg_26_0.createWantedGifts()
						var_26_0.time = arg_26_1 + var_0_7

						local var_26_3 = LoadSprite("ui/minigameui/idolmasterui_atlas", "pack" .. var_26_0.gifts[1])

						setImageSprite(findTF(var_26_0.tf, "score/pack"), var_26_3)
						arg_26_0.changeFansAction(var_26_0, var_0_24, 0, None)
				elif not var_26_0.leave:
					arg_26_0.changeFansAction(var_26_0, var_0_25, 0, None)

			if #arg_26_0.fans > 0:
				local var_26_4 = arg_26_0.fans[1]

				if var_26_4.time and arg_26_1 > var_26_4.time and not var_26_4.leave:
					var_26_4.leave = True

					arg_26_0.fanLeave(var_26_4, var_0_28, function()
						table.remove(arg_26_0.fans, 1))
				else
					arg_26_0.showFansWanted(var_26_4)

				var_26_4.tf.SetSiblingIndex(#arg_26_0.fans - 1),
		def showFansWanted:(arg_28_0, arg_28_1)
			if arg_28_1.leave:
				return

			local var_28_0 = arg_28_1.time

			if not var_28_0:
				return

			local var_28_1 = math.ceil(var_28_0 - arg_28_0.stepTime) < 0 and 0 or var_28_0 - arg_28_0.stepTime
			local var_28_2 = arg_28_1.gifts
			local var_28_3 = var_28_1 <= 5

			setActive(findTF(arg_28_1.tf, "wanted"), True)
			setActive(findTF(arg_28_1.tf, "wanted/bg1"), not var_28_3)
			setActive(findTF(arg_28_1.tf, "wanted/bgTime1"), not var_28_3)
			setActive(findTF(arg_28_1.tf, "wanted/time1"), not var_28_3)
			setActive(findTF(arg_28_1.tf, "wanted/bg2"), var_28_3)
			setActive(findTF(arg_28_1.tf, "wanted/bgTime2"), var_28_3)
			setActive(findTF(arg_28_1.tf, "wanted/time1"), var_28_3)

			if var_28_1 < 0:
				var_28_1 = 0

			setText(findTF(arg_28_1.tf, "wanted/time1"), math.abs(math.ceil(var_28_1)) .. "S")
			setText(findTF(arg_28_1.tf, "wanted/time2"), math.abs(math.ceil(var_28_1)) .. "S")

			for iter_28_0 = 1, #var_28_2:
				local var_28_4 = LoadSprite("ui/minigameui/idolmasterui_atlas", "wantItem" .. var_28_2[iter_28_0])

				setImageSprite(findTF(arg_28_1.tf, "wanted/item" .. iter_28_0), var_28_4),
		def checkGifts:(arg_29_0, arg_29_1)
			local var_29_0 = arg_29_0.getWantedGifts()

			if var_29_0:
				for iter_29_0 = 1, #arg_29_1:
					if not table.contains(var_29_0, arg_29_1[iter_29_0]):
						return False

				local var_29_1 = arg_29_0.fans[1]

				var_29_1.leave = True

				arg_29_0.fanLeave(var_29_1, var_0_29, function()
					table.remove(arg_29_0.fans, 1))

				return True

			return False,
		def createWantedGifts:(arg_31_0)
			local var_31_0 = Clone(var_0_15)
			local var_31_1 = {}

			table.insert(var_31_1, var_0_14[math.random(1, #var_0_14)])

			for iter_31_0 = 1, 2:
				local var_31_2 = table.remove(var_31_0, math.random(1, #var_31_0))

				table.insert(var_31_1, var_31_2)

			return var_31_1,
		def fanLeave:(arg_32_0, arg_32_1, arg_32_2, arg_32_3)
			setActive(findTF(arg_32_1.tf, "wanted"), False)

			local var_32_0

			if var_0_28 == arg_32_2:
				var_32_0 = var_0_23
			elif var_0_29:
				var_32_0 = var_0_22

				setText(findTF(arg_32_1.tf, "score"), "+" .. var_0_6)
				setActive(findTF(arg_32_1.tf, "score"), True)

			arg_32_0.changeFansAction(arg_32_1, var_32_0, 1, function()
				PoolMgr.GetInstance().ReturnSpineChar(arg_32_1.modelData.modelName, arg_32_1.modelData.model)
				arg_32_0._event.emit(var_0_12, arg_32_2)
				Destroy(arg_32_1.tf)
				arg_32_3()),
		def reset:(arg_34_0)
			arg_34_0.clearFans()

			arg_34_0.wantedData = {},
		def destroy:(arg_35_0)
			if arg_35_0.modelData:
				PoolMgr.GetInstance().ReturnSpineChar(arg_35_0.modelData.id, arg_35_0.modelData.model)
	}

	var_13_0.Ctor()

	return var_13_0

local function var_0_35(arg_36_0, arg_36_1, arg_36_2, arg_36_3, arg_36_4)
	local var_36_0 = {
		def Ctor:(arg_37_0)
			arg_37_0._containerTf = arg_36_0
			arg_37_0._tplGroup = arg_36_1
			arg_37_0._tplIdol = arg_36_2
			arg_37_0._tplFans = arg_36_3
			arg_37_0._event = arg_36_4
			arg_37_0.groups = {}

			local var_37_0 = arg_37_0.getRandomIdols()

			for iter_37_0 = 1, var_0_30:
				local var_37_1 = tf(Instantiate(arg_37_0._tplGroup))

				SetParent(var_37_1, arg_37_0._containerTf)

				local var_37_2 = var_0_34(var_37_0[iter_37_0], var_37_1, iter_37_0, arg_37_0._event)

				table.insert(arg_37_0.groups, var_37_2),
		def receiveGift:(arg_38_0, arg_38_1, arg_38_2)
			local var_38_0 = False

			for iter_38_0 = 1, #arg_38_0.groups:
				if arg_38_0.groups[iter_38_0].checkGifts(arg_38_1):
					var_38_0 = True

					break

			if arg_38_2:
				arg_38_2(var_38_0),
		def getRandomIdols:(arg_39_0)
			local var_39_0 = {}
			local var_39_1 = Clone(var_0_9)

			for iter_39_0 = 1, var_0_30:
				local var_39_2 = False

				if iter_39_0 == var_0_30:
					var_39_2 = True

					for iter_39_1, iter_39_2 in ipairs(var_0_10):
						if table.contains(var_39_0, iter_39_2):
							var_39_2 = False

				if var_39_2:
					table.insert(var_39_0, var_0_10[math.random(1, #var_0_10)])
				else
					table.insert(var_39_0, table.remove(var_39_1, math.random(1, #var_39_1)))

			return var_39_0,
		def getApearTime:(arg_40_0)
			if arg_40_0.runTime and arg_40_0.runTime > 0:
				for iter_40_0 = 1, #var_0_8:
					if arg_40_0.runTime < var_0_8[iter_40_0][1]:
						return var_0_8[iter_40_0][2]

			return var_0_8[#var_0_8][2],
		def start:(arg_41_0)
			arg_41_0.reset()

			arg_41_0.createFansTime = None
			arg_41_0.lastTime = var_0_5

			for iter_41_0 = 1, 3:
				local var_41_0 = math.random(1, #arg_41_0.groups)

				arg_41_0.groups[var_41_0].createFans(tf(instantiate(arg_41_0._tplFans)))

			for iter_41_1 = 1, #arg_41_0.groups:
				arg_41_0.groups[iter_41_1].start(),
		def step:(arg_42_0, arg_42_1)
			arg_42_0.lastTime = arg_42_0.lastTime - Time.deltaTime

			local var_42_0 = arg_42_0.getApearTime()

			if not arg_42_0.createFansTime:
				arg_42_0.createFansTime = arg_42_1 + var_42_0 + math.random() * 1
			elif arg_42_1 > arg_42_0.createFansTime:
				local var_42_1 = math.random(1, #arg_42_0.groups)

				arg_42_0.groups[var_42_1].createFans(tf(instantiate(arg_42_0._tplFans)))

				arg_42_0.createFansTime = arg_42_1 + var_42_0 + math.random() * 1

			for iter_42_0 = 1, #arg_42_0.groups:
				arg_42_0.groups[iter_42_0].step(arg_42_1),
		def reset:(arg_43_0)
			for iter_43_0 = 1, #arg_43_0.groups:
				arg_43_0.groups[iter_43_0].reset(),
		def destroy:(arg_44_0)
			for iter_44_0 = 1, #arg_44_0.groups:
				arg_44_0.groups[iter_44_0].destroy()
	}

	var_36_0.Ctor()

	return var_36_0

def var_0_0.getUIName(arg_45_0):
	return "IdolMasterGameUI"

def var_0_0.getBGM(arg_46_0):
	return var_0_1

def var_0_0.didEnter(arg_47_0):
	arg_47_0.initEvent()
	arg_47_0.initData()
	arg_47_0.initUI()
	arg_47_0.initGameUI()
	arg_47_0.updateMenuUI()
	arg_47_0.openMenuUI()

def var_0_0.initEvent(arg_48_0):
	arg_48_0.bind(var_0_11, function(arg_49_0, arg_49_1, arg_49_2)
		if arg_48_0.idolGroupUI:
			arg_48_0.idolGroupUI.receiveGift(arg_49_1, arg_49_2))
	arg_48_0.bind(var_0_12, function(arg_50_0, arg_50_1, arg_50_2)
		if arg_48_0.gameStartFlag:
			if arg_50_1 == var_0_28:
				arg_48_0.loseHeart()
			elif arg_50_1 == var_0_29:
				arg_48_0.addScore(100))

def var_0_0.initData(arg_51_0):
	local var_51_0 = Application.targetFrameRate or 60

	arg_51_0.timer = Timer.New(function()
		arg_51_0.onTimer(), 1 / var_51_0, -1)

def var_0_0.initUI(arg_53_0):
	arg_53_0.sceneTf = findTF(arg_53_0._tf, "scene")
	arg_53_0.clickMask = findTF(arg_53_0._tf, "clickMask")
	arg_53_0.countUI = findTF(arg_53_0._tf, "pop/CountUI")
	arg_53_0.countAnimator = GetComponent(findTF(arg_53_0.countUI, "count"), typeof(Animator))
	arg_53_0.countDft = GetComponent(findTF(arg_53_0.countUI, "count"), typeof(DftAniEvent))

	arg_53_0.countDft.SetTriggerEvent(function()
		return)
	arg_53_0.countDft.SetEndEvent(function()
		setActive(arg_53_0.countUI, False)
		arg_53_0.gameStart())

	arg_53_0.leaveUI = findTF(arg_53_0._tf, "pop/LeaveUI")

	onButton(arg_53_0, findTF(arg_53_0.leaveUI, "ad/btnOk"), function()
		arg_53_0.resumeGame()
		arg_53_0.onGameOver(), SFX_CANCEL)
	onButton(arg_53_0, findTF(arg_53_0.leaveUI, "ad/btnCancel"), function()
		arg_53_0.resumeGame(), SFX_CANCEL)

	arg_53_0.pauseUI = findTF(arg_53_0._tf, "pop/pauseUI")

	onButton(arg_53_0, findTF(arg_53_0.pauseUI, "ad/btnOk"), function()
		setActive(arg_53_0.pauseUI, False)
		arg_53_0.resumeGame(), SFX_CANCEL)

	arg_53_0.settlementUI = findTF(arg_53_0._tf, "pop/SettleMentUI")

	onButton(arg_53_0, findTF(arg_53_0.settlementUI, "ad/btnOver"), function()
		setActive(arg_53_0.settlementUI, False)
		arg_53_0.openMenuUI(), SFX_CANCEL)

	arg_53_0.menuUI = findTF(arg_53_0._tf, "pop/menuUI")
	arg_53_0.battleScrollRect = GetComponent(findTF(arg_53_0.menuUI, "battList"), typeof(ScrollRect))
	arg_53_0.totalTimes = arg_53_0.getGameTotalTime()

	local var_53_0 = arg_53_0.getGameUsedTimes() - 4 < 0 and 0 or arg_53_0.getGameUsedTimes() - 4

	scrollTo(arg_53_0.battleScrollRect, 0, 1 - var_53_0 / (arg_53_0.totalTimes - 4))
	onButton(arg_53_0, findTF(arg_53_0.menuUI, "rightPanelBg/arrowUp"), function()
		local var_60_0 = arg_53_0.battleScrollRect.normalizedPosition.y + 1 / (arg_53_0.totalTimes - 4)

		if var_60_0 > 1:
			var_60_0 = 1

		scrollTo(arg_53_0.battleScrollRect, 0, var_60_0), SFX_CANCEL)
	onButton(arg_53_0, findTF(arg_53_0.menuUI, "rightPanelBg/arrowDown"), function()
		local var_61_0 = arg_53_0.battleScrollRect.normalizedPosition.y - 1 / (arg_53_0.totalTimes - 4)

		if var_61_0 < 0:
			var_61_0 = 0

		scrollTo(arg_53_0.battleScrollRect, 0, var_61_0), SFX_CANCEL)
	onButton(arg_53_0, findTF(arg_53_0.menuUI, "btnBack"), function()
		arg_53_0.closeView(), SFX_CANCEL)
	onButton(arg_53_0, findTF(arg_53_0.menuUI, "btnRule"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.cowboy_tips.tip
		}), SFX_CANCEL)
	onButton(arg_53_0, findTF(arg_53_0.menuUI, "btnStart"), function()
		setActive(arg_53_0.menuUI, False)
		arg_53_0.readyStart(), SFX_CANCEL)

	local var_53_1 = findTF(arg_53_0.menuUI, "tplBattleItem")

	arg_53_0.battleItems = {}

	for iter_53_0 = 1, arg_53_0.totalTimes:
		local var_53_2 = tf(instantiate(var_53_1))

		var_53_2.name = "battleItem_" .. iter_53_0

		setParent(var_53_2, findTF(arg_53_0.menuUI, "battList/Viewport/Content"))

		local var_53_3 = iter_53_0

		GetSpriteFromAtlasAsync("ui/minigameui/idolmasterui_atlas", "tx_" .. var_53_3, function(arg_65_0)
			setImageSprite(findTF(var_53_2, "state_open/icon"), arg_65_0, True)
			setImageSprite(findTF(var_53_2, "state_clear/icon"), arg_65_0, True)
			setImageSprite(findTF(var_53_2, "state_current/icon"), arg_65_0, True))
		GetSpriteFromAtlasAsync("ui/minigameui/idolmasterui_atlas", "battleDesc" .. var_53_3, function(arg_66_0)
			setImageSprite(findTF(var_53_2, "state_open/buttomDesc"), arg_66_0, True)
			setImageSprite(findTF(var_53_2, "state_clear/buttomDesc"), arg_66_0, True)
			setImageSprite(findTF(var_53_2, "state_current/buttomDesc"), arg_66_0, True)
			setImageSprite(findTF(var_53_2, "state_closed/buttomDesc"), arg_66_0, True))
		setActive(var_53_2, True)
		table.insert(arg_53_0.battleItems, var_53_2)

	if not arg_53_0.handle:
		arg_53_0.handle = UpdateBeat.CreateListener(arg_53_0.Update, arg_53_0)

	UpdateBeat.AddListener(arg_53_0.handle)

def var_0_0.initGameUI(arg_67_0):
	arg_67_0.gameUI = findTF(arg_67_0._tf, "ui/gameUI")
	arg_67_0.textScore = findTF(arg_67_0.gameUI, "top/score")

	onButton(arg_67_0, findTF(arg_67_0.gameUI, "topRight/btnStop"), function()
		arg_67_0.stopGame()
		setActive(arg_67_0.pauseUI, True))
	onButton(arg_67_0, findTF(arg_67_0.gameUI, "btnLeave"), function()
		arg_67_0.stopGame()
		setActive(arg_67_0.leaveUI, True))

	arg_67_0.gameTimeM = findTF(arg_67_0.gameUI, "topRight/time/m")
	arg_67_0.gameTimeS = findTF(arg_67_0.gameUI, "topRight/time/s")
	arg_67_0.heartTfs = {}

	for iter_67_0 = 1, var_0_27:
		table.insert(arg_67_0.heartTfs, findTF(arg_67_0.gameUI, "top/heart" .. iter_67_0 .. "/full"))

	arg_67_0.scoreTf = findTF(arg_67_0.gameUI, "top/score")
	arg_67_0.giftUI = var_0_33(findTF(arg_67_0._tf, "scene/gift"), findTF(arg_67_0._tf, "scene/jiujiuWorker"), arg_67_0)

	local var_67_0 = findTF(arg_67_0._tf, "scene/group")
	local var_67_1 = findTF(arg_67_0._tf, "scene/IdolContainer")
	local var_67_2 = findTF(arg_67_0._tf, "scene/Idol")
	local var_67_3 = findTF(arg_67_0._tf, "scene/fans")

	arg_67_0.idolGroupUI = var_0_35(var_67_1, var_67_0, var_67_2, var_67_3, arg_67_0)

def var_0_0.Update(arg_70_0):
	arg_70_0.AddDebugInput()

def var_0_0.AddDebugInput(arg_71_0):
	if arg_71_0.gameStop or arg_71_0.settlementFlag:
		return

	if IsUnityEditor:
		-- block empty

def var_0_0.updateMenuUI(arg_72_0):
	local var_72_0 = arg_72_0.getGameUsedTimes()
	local var_72_1 = arg_72_0.getGameTimes()

	for iter_72_0 = 1, #arg_72_0.battleItems:
		setActive(findTF(arg_72_0.battleItems[iter_72_0], "state_open"), False)
		setActive(findTF(arg_72_0.battleItems[iter_72_0], "state_closed"), False)
		setActive(findTF(arg_72_0.battleItems[iter_72_0], "state_clear"), False)
		setActive(findTF(arg_72_0.battleItems[iter_72_0], "state_current"), False)

		if iter_72_0 <= var_72_0:
			setActive(findTF(arg_72_0.battleItems[iter_72_0], "state_clear"), True)
		elif iter_72_0 == var_72_0 + 1 and var_72_1 >= 1:
			setActive(findTF(arg_72_0.battleItems[iter_72_0], "state_current"), True)
		elif var_72_0 < iter_72_0 and iter_72_0 <= var_72_0 + var_72_1:
			setActive(findTF(arg_72_0.battleItems[iter_72_0], "state_open"), True)
		else
			setActive(findTF(arg_72_0.battleItems[iter_72_0], "state_closed"), True)

	arg_72_0.totalTimes = arg_72_0.getGameTotalTime()

	local var_72_2 = 1 - (arg_72_0.getGameUsedTimes() - 3 < 0 and 0 or arg_72_0.getGameUsedTimes() - 3) / (arg_72_0.totalTimes - 4)

	if var_72_2 > 1:
		var_72_2 = 1

	scrollTo(arg_72_0.battleScrollRect, 0, var_72_2)
	setActive(findTF(arg_72_0.menuUI, "btnStart/tip"), var_72_1 > 0)
	arg_72_0.CheckGet()

def var_0_0.CheckGet(arg_73_0):
	setActive(findTF(arg_73_0.menuUI, "got"), False)

	if arg_73_0.getUltimate() and arg_73_0.getUltimate() != 0:
		setActive(findTF(arg_73_0.menuUI, "got"), True)

	if arg_73_0.getUltimate() == 0:
		if arg_73_0.getGameTotalTime() > arg_73_0.getGameUsedTimes():
			return

		pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = arg_73_0.GetMGHubData().id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})
		setActive(findTF(arg_73_0.menuUI, "got"), True)

def var_0_0.openMenuUI(arg_74_0):
	setActive(findTF(arg_74_0._tf, "scene_front"), False)
	setActive(findTF(arg_74_0._tf, "scene_background"), False)
	setActive(findTF(arg_74_0._tf, "scene"), False)
	setActive(arg_74_0.gameUI, False)
	setActive(arg_74_0.menuUI, True)
	arg_74_0.updateMenuUI()

def var_0_0.clearUI(arg_75_0):
	setActive(arg_75_0.sceneTf, False)
	setActive(arg_75_0.settlementUI, False)
	setActive(arg_75_0.countUI, False)
	setActive(arg_75_0.menuUI, False)
	setActive(arg_75_0.gameUI, False)

def var_0_0.readyStart(arg_76_0):
	setActive(arg_76_0.countUI, True)
	arg_76_0.countAnimator.Play("count")
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_2)

def var_0_0.gameStart(arg_77_0):
	setActive(findTF(arg_77_0._tf, "scene_front"), True)
	setActive(findTF(arg_77_0._tf, "scene_background"), True)
	setActive(findTF(arg_77_0._tf, "scene"), True)
	setActive(arg_77_0.gameUI, True)

	arg_77_0.gameStartFlag = True
	arg_77_0.scoreNum = 0
	arg_77_0.playerPosIndex = 2
	arg_77_0.gameStepTime = 0
	arg_77_0.heart = var_0_27
	arg_77_0.gameTime = var_0_5

	arg_77_0.idolGroupUI.start()
	arg_77_0.giftUI.start()
	arg_77_0.updateGameUI()
	arg_77_0.timerStart()

def var_0_0.getGameTimes(arg_78_0):
	return arg_78_0.GetMGHubData().count

def var_0_0.getGameUsedTimes(arg_79_0):
	return arg_79_0.GetMGHubData().usedtime

def var_0_0.getUltimate(arg_80_0):
	return arg_80_0.GetMGHubData().ultimate

def var_0_0.getGameTotalTime(arg_81_0):
	return (arg_81_0.GetMGHubData().getConfig("reward_need"))

def var_0_0.changeSpeed(arg_82_0, arg_82_1):
	return

def var_0_0.onTimer(arg_83_0):
	arg_83_0.gameStep()

def var_0_0.gameStep(arg_84_0):
	arg_84_0.gameTime = arg_84_0.gameTime - Time.deltaTime

	if arg_84_0.gameTime < 0:
		arg_84_0.gameTime = 0

	arg_84_0.gameStepTime = arg_84_0.gameStepTime + Time.deltaTime

	if arg_84_0.idolGroupUI:
		arg_84_0.idolGroupUI.step(arg_84_0.gameStepTime)

	arg_84_0.updateGameUI()

	if arg_84_0.gameTime <= 0:
		arg_84_0.onGameOver()

		return

def var_0_0.timerStart(arg_85_0):
	if not arg_85_0.timer.running:
		arg_85_0.timer.Start()

def var_0_0.timerStop(arg_86_0):
	if arg_86_0.timer.running:
		arg_86_0.timer.Stop()

def var_0_0.updateGameUI(arg_87_0):
	setText(arg_87_0.textScore, arg_87_0.scoreNum)

	local var_87_0 = math.floor(math.ceil(arg_87_0.gameTime) / 60)

	if var_87_0 < 10:
		var_87_0 = "0" .. var_87_0

	local var_87_1 = math.floor(math.ceil(arg_87_0.gameTime) % 60)

	if var_87_1 < 10:
		var_87_1 = "0" .. var_87_1

	for iter_87_0 = 1, #arg_87_0.heartTfs:
		if iter_87_0 <= arg_87_0.heart:
			setActive(arg_87_0.heartTfs[iter_87_0], True)
		else
			setActive(arg_87_0.heartTfs[iter_87_0], False)

	setText(arg_87_0.scoreTf, arg_87_0.scoreNum)
	setText(arg_87_0.gameTimeM, var_87_0)
	setText(arg_87_0.gameTimeS, var_87_1)

def var_0_0.loseHeart(arg_88_0):
	if arg_88_0.heart <= 0:
		return

	arg_88_0.heart = arg_88_0.heart - 1

	arg_88_0.updateGameUI()

	if arg_88_0.heart <= 0:
		arg_88_0.heart = 0

		arg_88_0.onGameOver()

def var_0_0.addScore(arg_89_0, arg_89_1):
	arg_89_0.scoreNum = arg_89_0.scoreNum + arg_89_1

	if arg_89_0.scoreNum < 0:
		arg_89_0.scoreNum = 0

def var_0_0.onGameOver(arg_90_0):
	if arg_90_0.settlementFlag:
		return

	arg_90_0.timerStop()

	arg_90_0.settlementFlag = True

	setActive(arg_90_0.clickMask, True)
	LeanTween.delayedCall(go(arg_90_0._tf), 2, System.Action(function()
		arg_90_0.settlementFlag = False
		arg_90_0.gameStartFlag = False

		setActive(arg_90_0.clickMask, False)
		arg_90_0.showSettlement()))

def var_0_0.showSettlement(arg_92_0):
	setActive(arg_92_0.settlementUI, True)
	GetComponent(findTF(arg_92_0.settlementUI, "ad"), typeof(Animator)).Play("settlement", -1, 0)

	local var_92_0 = arg_92_0.GetMGData().GetRuntimeData("elements")
	local var_92_1 = arg_92_0.scoreNum
	local var_92_2 = var_92_0 and #var_92_0 > 0 and var_92_0[1] or 0

	setActive(findTF(arg_92_0.settlementUI, "ad/new"), var_92_2 < var_92_1)

	if var_92_2 <= var_92_1:
		var_92_2 = var_92_1

		arg_92_0.StoreDataToServer({
			var_92_2
		})

	local var_92_3 = findTF(arg_92_0.settlementUI, "ad/highText")
	local var_92_4 = findTF(arg_92_0.settlementUI, "ad/currentText")

	setText(var_92_3, var_92_2)
	setText(var_92_4, var_92_1)

	if arg_92_0.getGameTimes() and arg_92_0.getGameTimes() > 0:
		arg_92_0.sendSuccessFlag = True

		arg_92_0.SendSuccess(0)

def var_0_0.resumeGame(arg_93_0):
	arg_93_0.gameStop = False

	setActive(arg_93_0.leaveUI, False)
	arg_93_0.changeSpeed(1)
	arg_93_0.timerStart()

def var_0_0.stopGame(arg_94_0):
	arg_94_0.gameStop = True

	arg_94_0.timerStop()
	arg_94_0.changeSpeed(0)

def var_0_0.onBackPressed(arg_95_0):
	if not arg_95_0.gameStartFlag:
		arg_95_0.emit(var_0_0.ON_BACK_PRESSED)
	else
		if arg_95_0.settlementFlag:
			return

		if isActive(arg_95_0.pauseUI):
			setActive(arg_95_0.pauseUI, False)

		arg_95_0.stopGame()
		setActive(arg_95_0.leaveUI, True)

def var_0_0.willExit(arg_96_0):
	if arg_96_0.handle:
		UpdateBeat.RemoveListener(arg_96_0.handle)

	if arg_96_0._tf and LeanTween.isTweening(go(arg_96_0._tf)):
		LeanTween.cancel(go(arg_96_0._tf))

	if arg_96_0.timer and arg_96_0.timer.running:
		arg_96_0.timer.Stop()

	Time.timeScale = 1
	arg_96_0.timer = None

return var_0_0
