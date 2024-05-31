local var_0_0 = class("MonopolyPtScene", import("..base.BaseUI"))

var_0_0.story = False

local var_0_1 = 312011
local var_0_2 = 312010
local var_0_3 = "kaibaoxiang_boss"
local var_0_4 = "kaibaoxiang_putong"
local var_0_5 = "unknown3"

var_0_0.battle = False

local var_0_6 = {
	201211,
	401231,
	301051,
	101171
}
local var_0_7 = {
	201217,
	431232,
	331055,
	131171
}
local var_0_8 = 0.6
local var_0_9 = 100
local var_0_10 = "dafuweng_walk"
local var_0_11 = "stand"
local var_0_12 = "dafuweng_stand"
local var_0_13 = "dafuweng_jump"
local var_0_14 = "dafuweng_run"
local var_0_15 = "dafuweng_touch"
local var_0_16 = "maoxian_baoxiang"
local var_0_17 = "maoxian_gold"
local var_0_18 = "maoxian_item"
local var_0_19 = "maoxian_oil"
local var_0_20 = 35
local var_0_21 = 1
local var_0_22 = 2
local var_0_23 = "back"
local var_0_24 = "mid"
local var_0_25 = "front"
local var_0_26 = 2
local var_0_27 = 1920
local var_0_28 = 1080
local var_0_29 = False
local var_0_30 = 0
local var_0_31 = {
	700,
	1400,
	2100,
	2800,
	3500,
	4200,
	4900,
	5600,
	6300,
	7000,
	9000,
	9650,
	10200,
	10900,
	11600,
	12300,
	13000,
	13800,
	14500,
	15430
}

def var_0_0.getUIName(arg_1_0):
	return "MonopolyPtUI"

def var_0_0.init(arg_2_0):
	arg_2_0.initData()
	arg_2_0.initUI()
	arg_2_0.initEvent()
	arg_2_0.activityDataUpdata()
	arg_2_0.updataUI()
	arg_2_0.initMap()

def var_0_0.initMap(arg_3_0):
	if arg_3_0.useCount < 9:
		arg_3_0.createMap("ground_1")
	elif arg_3_0.useCount == 9:
		arg_3_0.createMap("ground_2")
		arg_3_0.createMap("ground_3")
		arg_3_0.createMap("ground_4")
	elif arg_3_0.useCount == 10:
		arg_3_0.createMap("ground_3")
		arg_3_0.createMap("ground_4")
	elif arg_3_0.useCount > 9 and arg_3_0.useCount < 19:
		arg_3_0.createMap("ground_4")
	elif arg_3_0.useCount == 19:
		arg_3_0.createMap("ground_5")

		if MonopolyPtScene.battle:
			LeanTween.delayedCall(go(arg_3_0._tf), 1, System.Action(function()
				local var_4_0 = arg_3_0.getPtData()
				local var_4_1, var_4_2 = var_4_0.GetResProgress()

				pg.m02.sendNotification(GAME.ACT_NEW_PT, {
					cmd = 1,
					activity_id = var_4_0.GetId(),
					arg1 = var_4_2
				})))

			if arg_3_0.baoxiangModel:
				local var_3_0 = arg_3_0.baoxiangModel.GetComponent(typeof(SpineAnimUI))

				arg_3_0.setModelAnim(var_3_0, "boss_kaiqi", 1, function()
					arg_3_0.setModelAnim(var_3_0, "boss_kai", 0, None))
				arg_3_0.changeCharAction(var_0_16, 1, None)
			else
				arg_3_0.baoxiangKai = True

			if arg_3_0.anims:
				arg_3_0.changeCharAction(var_0_16, 1, None)
			else
				arg_3_0.charMaoxian = True
	elif arg_3_0.useCount >= 20:
		arg_3_0.createMap("ground_5")

	if arg_3_0.useCount > 0:
		if MonopolyPtScene.battle and arg_3_0.useCount >= 19:
			arg_3_0.updateMap(var_0_31[#var_0_31])
		else
			arg_3_0.updateMap(var_0_31[arg_3_0.useCount])

		for iter_3_0 = 1, 20:
			arg_3_0.translate.anchoredPosition = Vector2(arg_3_0.mid.anchoredPosition.x + arg_3_0.distance, 0)

			if arg_3_0.mapTf.InverseTransformPoint(arg_3_0.translate.position).x <= var_0_27 - 600:
				arg_3_0.createMap()

	if arg_3_0.useCount == 0 and not MonopolyPtScene.story:
		local var_3_1 = arg_3_0.getStoryData(0)

		setActive(arg_3_0.btnStart, False)
		setActive(arg_3_0.btnBack, False)
		setActive(arg_3_0.btnMain, False)
		setActive(arg_3_0.labelDropShip, False)
		pg.NewStoryMgr.GetInstance().Play(var_3_1, function()
			MonopolyPtScene.story = True

			setActive(arg_3_0.btnStart, True)
			setActive(arg_3_0.btnBack, True)
			setActive(arg_3_0.btnMain, True)
			setActive(arg_3_0.labelDropShip, False)
			arg_3_0.updataUI(), True, True)

local var_0_32 = {
	1,
	1,
	1,
	2,
	3,
	4,
	4,
	4,
	5
}

def var_0_0.createMap(arg_7_0, arg_7_1):
	if not arg_7_0.mapIndexs:
		arg_7_0.mapIndexs = Clone(var_0_32)

	if #arg_7_0.mapIndexs == 0:
		return

	arg_7_1 = "ground_" .. table.remove(arg_7_0.mapIndexs, 1)

	if arg_7_1 == "ground_2" or arg_7_1 == "ground_3" or arg_7_1 == "ground_5":
		if not arg_7_0.onceMap:
			arg_7_0.onceMap = {}

		if table.contains(arg_7_0.onceMap, arg_7_1):
			return
		else
			table.insert(arg_7_0.onceMap, arg_7_1)

	local var_7_0 = findTF(arg_7_0.groundTf, arg_7_1)
	local var_7_1 = tf(Instantiate(var_7_0))
	local var_7_2 = findTF(var_7_1, "back")

	SetParent(var_7_2, arg_7_0.back)
	setActive(var_7_2, True)

	var_7_2.anchoredPosition = Vector2(arg_7_0.distance, 0)

	var_7_2.SetAsFirstSibling()

	local var_7_3 = findTF(var_7_1, "mid")

	SetParent(var_7_3, arg_7_0.mid)
	setActive(var_7_3, True)

	var_7_3.anchoredPosition = Vector2(arg_7_0.distance, 0)

	local var_7_4 = findTF(var_7_1, "front")

	SetParent(var_7_4, arg_7_0.front)
	setActive(var_7_4, True)

	var_7_4.anchoredPosition = Vector2(arg_7_0.distance, 0)

	Destroy(var_7_1)

	local var_7_5 = var_7_1.sizeDelta.x

	arg_7_0.distance = arg_7_0.distance + var_7_5

	if arg_7_0.cellPos:
		arg_7_0.cellPos.SetAsLastSibling()

	if arg_7_0.char:
		arg_7_0.char.SetAsLastSibling()

	if arg_7_1 == "ground_2":
		arg_7_0.housePosition = findTF(var_7_3, "house/img").position
	elif arg_7_1 == "ground_5":
		arg_7_0.endPosition = findTF(var_7_3, "house/img").position

	if arg_7_1 == "ground_2":
		local var_7_6 = Ship.New({
			configId = var_0_1,
			skin_id = var_0_2
		}).getPrefab()

		PoolMgr.GetInstance().GetSpineChar(var_7_6, True, function(arg_8_0)
			arg_7_0.mingShimodel = arg_8_0
			arg_7_0.mingShimodel.transform.localScale = Vector3(0.4, 0.4, 0.4)
			arg_7_0.mingShimodel.transform.localPosition = Vector3.zero

			arg_7_0.mingShimodel.transform.SetParent(findTF(var_7_3, "house/char"), False)

			local var_8_0 = arg_7_0.mingShimodel.GetComponent(typeof(SpineAnimUI))

			arg_7_0.setModelAnim(var_8_0, var_0_11, 0, None))
	elif arg_7_1 == "ground_5":
		if arg_7_0.useCount <= 19 and not MonopolyPtScene.battle:
			PoolMgr.GetInstance().GetSpineChar(var_0_5, True, function(arg_9_0)
				arg_7_0.enemyModel = arg_9_0
				arg_7_0.enemyModel.transform.localScale = Vector3(0.4, 0.4, 0.4)
				arg_7_0.enemyModel.transform.localPosition = Vector3.zero

				arg_7_0.enemyModel.transform.SetParent(findTF(var_7_3, "house/enemy"), False)

				local var_9_0 = arg_7_0.enemyModel.GetComponent(typeof(SpineAnimUI))

				arg_7_0.setModelAnim(var_9_0, "normal", 0, None))
		else
			PoolMgr.GetInstance().GetSpineChar(var_0_3, True, function(arg_10_0)
				arg_7_0.baoxiangModel = arg_10_0
				arg_7_0.baoxiangModel.transform.localScale = Vector3(0.3, 0.3, 0.3)
				arg_7_0.baoxiangModel.transform.localPosition = Vector3.zero

				arg_7_0.baoxiangModel.transform.SetParent(findTF(var_7_3, "house/baoxiang"), False)

				local var_10_0 = arg_7_0.baoxiangModel.GetComponent(typeof(SpineAnimUI))

				if arg_7_0.baoxiangKai:
					arg_7_0.baoxiangKai = False

					local var_10_1 = arg_7_0.baoxiangModel.GetComponent(typeof(SpineAnimUI))

					arg_7_0.setModelAnim(var_10_1, "boss_kaiqi", 1, function()
						arg_7_0.setModelAnim(var_10_1, "boss_kai", 0, None))
					arg_7_0.changeCharAction(var_0_16, 1, None)
				elif arg_7_0.useCount >= 20:
					arg_7_0.setModelAnim(var_10_0, "boss_kai", 0, None)
				else
					arg_7_0.setModelAnim(var_10_0, "boss_guan", 0, None)
					setActive(arg_7_0.baoxiangModel, False))

def var_0_0.initData(arg_12_0):
	arg_12_0.distance = 0
	arg_12_0.moveDistance = 0
	arg_12_0.activityId = arg_12_0.contextData.config_id
	arg_12_0.leftCount = 0
	arg_12_0.inAnimatedFlag = False
	arg_12_0.lastBonusTimes = 0
	arg_12_0.baoxiangCells = {}

	local var_12_0 = pg.activity_template[arg_12_0.activityId]

	arg_12_0.storys = var_12_0.config_client.story
	arg_12_0.battles = var_12_0.config_client.battle
	arg_12_0.awardsTimer = Timer.New(function()
		if arg_12_0.awardTfs and #arg_12_0.awardTfs > 0:
			for iter_13_0 = #arg_12_0.awardTfs, 1, -1:
				local var_13_0 = arg_12_0.awardTfs[iter_13_0]
				local var_13_1 = var_13_0.anchoredPosition

				var_13_1.y = var_13_1.y + 3

				if var_13_1.y >= 150:
					Destroy(table.remove(arg_12_0.awardTfs, iter_13_0))
				else
					var_13_0.anchoredPosition = var_13_1, 0.03333333333333333, -1)

	arg_12_0.awardsTimer.Start()

def var_0_0.initUI(arg_14_0):
	arg_14_0._ad = findTF(arg_14_0._tf, "AD")
	arg_14_0.char = findTF(arg_14_0._ad, "map/mask/container/mid/char")
	arg_14_0.btnStart = findTF(arg_14_0._ad, "btnStart")
	arg_14_0.btnBack = findTF(arg_14_0._ad, "btnBack")
	arg_14_0.labelCount = findTF(arg_14_0._ad, "btnStart/txt")

	setActive(arg_14_0.btnStart, True)

	arg_14_0.btnMain = findTF(arg_14_0._ad, "btnMain")
	arg_14_0.labelDropShip = findTF(arg_14_0._ad, "labelDropShip")
	arg_14_0.mapTf = findTF(arg_14_0._ad, "map")
	arg_14_0.container = findTF(arg_14_0._ad, "map/mask/container")
	arg_14_0.back = findTF(arg_14_0._ad, "map/mask/container/back")
	arg_14_0.mid = findTF(arg_14_0._ad, "map/mask/container/mid")
	arg_14_0.front = findTF(arg_14_0._ad, "map/mask/container/front")
	arg_14_0.cellPos = findTF(arg_14_0._ad, "map/mask/container/mid/posCell")
	arg_14_0.tplCell = findTF(arg_14_0._ad, "tplCell")
	arg_14_0.mapCells = {}
	arg_14_0.curCellIndex = None
	arg_14_0.translate = findTF(arg_14_0.container, "translate")
	arg_14_0.awardTf = findTF(arg_14_0._ad, "awardTpl")
	arg_14_0.awardParent = findTF(arg_14_0.char, "award")
	arg_14_0.groundTf = findTF(arg_14_0._ad, "map/mask/container/ground")

	setActive(arg_14_0.groundTf, False)

	arg_14_0.models = {}
	arg_14_0.anims = {}
	arg_14_0.modelIds = {}
	arg_14_0.clickModelTime = {}

	for iter_14_0 = 1, #var_0_6:
		local var_14_0 = iter_14_0
		local var_14_1 = var_0_6[iter_14_0]
		local var_14_2 = var_0_7[iter_14_0]
		local var_14_3 = {
			configId = var_14_1,
			skin_id = var_14_2
		}
		local var_14_4 = Ship.New(var_14_3).getPrefab()

		PoolMgr.GetInstance().GetSpineChar(var_14_4, True, function(arg_15_0)
			arg_15_0.transform.localScale = Vector3.one
			arg_15_0.transform.localPosition = Vector3(0, 0, 0)
			arg_15_0.transform.anchorMin = Vector2(0.5, 0)
			arg_15_0.transform.anchorMax = Vector2(0.5, 0)

			arg_15_0.transform.SetParent(findTF(arg_14_0.char, var_14_0), False)

			local var_15_0 = arg_15_0.GetComponent(typeof(SpineAnimUI))

			table.insert(arg_14_0.modelIds, var_14_1)
			table.insert(arg_14_0.models, arg_15_0)
			table.insert(arg_14_0.anims, var_15_0)

			if #arg_14_0.anims == #var_0_6:
				if arg_14_0.charMaoxian:
					arg_14_0.charMaoxian = False

					arg_14_0.changeCharAction(var_0_16, 0, None)
				else
					arg_14_0.changeCharAction(var_0_11, 0, None)

			table.insert(arg_14_0.clickModelTime, 0)
			onButton(arg_14_0._binder, findTF(arg_14_0.char, var_14_0).transform, function()
				if not var_15_0 or not arg_15_0 or arg_14_0.inAnimatedFlag:
					return

				if Time.time - arg_14_0.clickModelTime[var_14_0] < 3:
					return

				arg_14_0.clickModelTime[var_14_0] = Time.time

				if LeanTween.isTweening(go(arg_14_0.cellPos)):
					return

				arg_14_0.setModelAnim(var_15_0, var_0_15, 1, function()
					arg_14_0.setModelAnim(var_15_0, var_0_11, 0, None)), SFX_PANEL))

def var_0_0.initEvent(arg_18_0):
	onButton(arg_18_0._binder, arg_18_0.btnStart, function()
		if arg_18_0.leftCount and arg_18_0.leftCount <= 0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_count_noenough"))

			return

		local var_19_0 = {}
		local var_19_1 = arg_18_0.getPtData().GetAward()
		local var_19_2 = getProxy(PlayerProxy).getRawData()
		local var_19_3 = pg.gameset.urpt_chapter_max.description[1]
		local var_19_4 = LOCK_UR_SHIP and 0 or getProxy(BagProxy).GetLimitCntById(var_19_3)
		local var_19_5, var_19_6 = Task.StaticJudgeOverflow(var_19_2.gold, var_19_2.oil, var_19_4, True, True, {
			{
				var_19_1.type,
				var_19_1.id,
				var_19_1.count
			}
		})

		if var_19_5:
			table.insert(var_19_0, function(arg_20_0)
				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					type = MSGBOX_TYPE_ITEM_BOX,
					content = i18n("award_max_warning"),
					items = var_19_6,
					onYes = arg_20_0
				}))

		seriesAsync(var_19_0, function()
			arg_18_0.start()), SFX_PANEL)
	onButton(arg_18_0._binder, arg_18_0.btnBack, function()
		arg_18_0.closeView(), SFX_PANEL)
	onButton(arg_18_0._binder, arg_18_0.btnMain, function()
		arg_18_0.emit(BaseUI.ON_HOME), SFX_PANEL)

def var_0_0.getPtData(arg_24_0):
	local var_24_0 = getProxy(ActivityProxy).getActivityById(arg_24_0.activityId)

	return (ActivityPtData.New(var_24_0))

def var_0_0.addAwards(arg_25_0, arg_25_1):
	if not arg_25_0.awardTfs:
		arg_25_0.awardTfs = {}

	for iter_25_0 = 1, #arg_25_1:
		local var_25_0 = arg_25_1[iter_25_0]
		local var_25_1 = tf(instantiate(go(arg_25_0.awardTf)))

		setParent(var_25_1, arg_25_0.awardParent)
		updateDrop(var_25_1, var_25_0)

		var_25_1.anchoredPosition = Vector2(0, 0)

		setActive(var_25_1, True)
		table.insert(arg_25_0.awardTfs, var_25_1)

def var_0_0.start(arg_26_0):
	if arg_26_0.inAnimatedFlag:
		return

	if arg_26_0.leftCount and arg_26_0.leftCount <= 0:
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_count_noenough"))

		return

	arg_26_0.changeAnimeState(True)

	local var_26_0 = var_0_14

	arg_26_0.move(var_26_0, function()
		return)

def var_0_0.checkCountStory(arg_28_0, arg_28_1):
	local var_28_0 = arg_28_0.useCount
	local var_28_1 = arg_28_0.activity.getDataConfig("story") or {}
	local var_28_2 = _.detect(var_28_1, function(arg_29_0)
		return arg_29_0[1] == var_28_0)

	if var_28_2:
		pg.NewStoryMgr.GetInstance().Play(var_28_2[2], arg_28_1)
	else
		arg_28_1()

def var_0_0.changeAnimeState(arg_30_0, arg_30_1, arg_30_2):
	if arg_30_1:
		arg_30_0.btnStart.GetComponent(typeof(Image)).raycastTarget = False
		arg_30_0.inAnimatedFlag = True
	else
		arg_30_0.inAnimatedFlag = False
		arg_30_0.btnStart.GetComponent(typeof(Image)).raycastTarget = True

	setActive(arg_30_0.btnStart, not arg_30_1)

def var_0_0.updataActivity(arg_31_0, arg_31_1):
	arg_31_0.activityDataUpdata()
	arg_31_0.updataUI()

	if arg_31_0.useCount == 9:
		arg_31_0.createMap("ground_2")
		arg_31_0.createMap("ground_3")
	elif arg_31_0.useCount == 19:
		arg_31_0.createMap("ground_5")

def var_0_0.activityDataUpdata(arg_32_0):
	local var_32_0 = getProxy(ActivityProxy).getActivityById(arg_32_0.activityId)
	local var_32_1 = ActivityPtData.New(var_32_0)
	local var_32_2, var_32_3, var_32_4 = var_32_1.GetResProgress()
	local var_32_5 = var_32_1.GetLevel()
	local var_32_6 = var_32_1.CanGetAward()
	local var_32_7 = var_32_1.CanGetNextAward()
	local var_32_8 = 20 - var_32_5
	local var_32_9 = math.floor(var_32_2 / 500) - var_32_5

	if var_32_8 < var_32_9:
		var_32_9 = var_32_8

	arg_32_0.useCount = var_32_5
	arg_32_0.leftCount = var_32_9

	if var_0_29:
		var_0_30 = var_0_30 + 1
		arg_32_0.useCount = var_0_30
		arg_32_0.leftCount = 20 - var_0_30

	arg_32_0.leftLastDrop = 20 - arg_32_0.useCount

def var_0_0.updataUI(arg_33_0):
	if arg_33_0.leftLastDrop:
		setText(findTF(arg_33_0.labelDropShip, "text"), "" .. arg_33_0.leftLastDrop)
		setActive(arg_33_0.labelDropShip, arg_33_0.leftLastDrop > 0)

	setText(arg_33_0.labelCount, arg_33_0.leftCount)

	if arg_33_0.useCount >= 20:
		setActive(arg_33_0.btnStart, False)

def var_0_0.updataChar(arg_34_0):
	if not isActive(arg_34_0.char):
		SetActive(arg_34_0.char, True)
		arg_34_0.char.SetAsLastSibling()

def var_0_0.move(arg_35_0, arg_35_1, arg_35_2):
	local var_35_0 = {}

	table.insert(var_35_0, function(arg_36_0)
		if arg_35_0.useCount >= #var_0_31:
			arg_35_0.useCount = #var_0_31 - 1

		local var_36_0 = var_0_31[arg_35_0.useCount + 1] - arg_35_0.moveDistance

		if arg_35_0.useCount == 9 and arg_35_0.housePosition:
			-- block empty
		elif arg_35_0.useCount == 19 and arg_35_0.endPosition:
			-- block empty
		elif arg_35_0.useCount == 10:
			arg_35_0.createCell(var_36_0)
		else
			arg_35_0.createCell(var_36_0)

		local var_36_1 = var_36_0 / 250
		local var_36_2 = 0

		arg_35_0.changeCharAction(arg_35_1, 0, None)

		local var_36_3 = var_36_0 / (var_36_1 / 0.6)
		local var_36_4 = 0

		if LeanTween.isTweening(go(arg_35_0.cellPos)):
			LeanTween.cancel(go(arg_35_0.cellPos))

		LeanTween.value(go(arg_35_0.cellPos), 0, var_36_0, var_36_1).setEase(LeanTweenType.linear).setOnUpdate(System.Action_float(function(arg_37_0)
			arg_35_0.updateMap(arg_37_0 - var_36_2)

			var_36_2 = arg_37_0)).setOnComplete(System.Action(function()
			local var_38_0

			if arg_35_0.useCount > 1:
				var_38_0 = arg_35_0.getStoryData(arg_35_0.useCount + 1)

			local var_38_1 = arg_35_0.getBattle(arg_35_0.useCount + 1)
			local var_38_2 = arg_35_0.useCount + 1

			arg_35_0.changeCharAction(var_0_11, 0, None)

			local function var_38_3()
				local var_39_0 = arg_35_0.getPtAwardData(var_38_2)

				assert(var_39_0)

				if var_39_0[1] == 1 and var_39_0[2] == 1:
					arg_35_0.setModelAnim(arg_35_0.anims[1], var_0_17, 1, function()
						arg_35_0.setModelAnim(arg_35_0.anims[1], var_0_11, 0))
				elif var_39_0[1] == 1 and var_39_0[2] == 2:
					arg_35_0.setModelAnim(arg_35_0.anims[1], var_0_19, 1, function()
						arg_35_0.setModelAnim(arg_35_0.anims[1], var_0_11, 0))
				elif var_39_0[1] == 2 and var_39_0[2] == 54016:
					arg_35_0.setModelAnim(arg_35_0.anims[1], var_0_18, 1, function()
						arg_35_0.setModelAnim(arg_35_0.anims[1], var_0_11, 0))
				else
					arg_35_0.setModelAnim(arg_35_0.anims[1], var_0_16, 1, function()
						arg_35_0.setModelAnim(arg_35_0.anims[1], var_0_11, 0))

				for iter_39_0 = 2, #arg_35_0.anims:
					arg_35_0.setModelAnim(arg_35_0.anims[iter_39_0], var_0_16, 1, function()
						arg_35_0.setModelAnim(arg_35_0.anims[iter_39_0], var_0_11, 0))

			if arg_35_0.putongModel:
				local var_38_4 = arg_35_0.putongModel.GetComponent(typeof(SpineAnimUI))

				arg_35_0.setModelAnim(var_38_4, "putong_kaiqi", 1, function()
					if var_38_4:
						arg_35_0.setModelAnim(var_38_4, "putong_kai", 0, None))

				arg_35_0.putongModel = None

			if var_38_0 and tonumber(var_38_0) != 0:
				pg.NewStoryMgr.GetInstance().Play(var_38_0, function()
					if var_38_3:
						var_38_3()

					LeanTween.delayedCall(go(arg_35_0._tf), 1, System.Action(function()
						arg_36_0())), True, True)
			elif arg_35_0.useCount == 19 and tonumber(var_38_1) != 0 and not MonopolyPtScene.battle:
				MonopolyPtScene.battle = True

				pg.m02.sendNotification(GAME.BEGIN_STAGE, {
					system = SYSTEM_PERFORM,
					stageId = tonumber(var_38_1)
				})
			else
				if var_38_3:
					var_38_3()

				LeanTween.delayedCall(go(arg_35_0._tf), 1, System.Action(function()
					arg_36_0())))))
	table.insert(var_35_0, function(arg_49_0)
		local var_49_0 = arg_35_0.getPtData()
		local var_49_1, var_49_2 = var_49_0.GetResProgress()

		pg.m02.sendNotification(GAME.ACT_NEW_PT, {
			cmd = 1,
			activity_id = var_49_0.GetId(),
			arg1 = var_49_2
		})
		arg_35_0.changeAnimeState(False)
		arg_35_0.updataActivity()
		arg_49_0())
	seriesAsync(var_35_0, arg_35_2)

def var_0_0.getBattle(arg_50_0, arg_50_1):
	for iter_50_0 = 1, #arg_50_0.battles:
		if arg_50_0.battles[iter_50_0][1] == arg_50_1:
			return arg_50_0.battles[iter_50_0][2]

	return None

def var_0_0.getStoryData(arg_51_0, arg_51_1):
	for iter_51_0 = 1, #arg_51_0.storys:
		if arg_51_0.storys[iter_51_0][1] == arg_51_1:
			return arg_51_0.storys[iter_51_0][2]

	return None

def var_0_0.createCell(arg_52_0, arg_52_1, arg_52_2):
	local var_52_0 = tf(instantiate(go(arg_52_0.tplCell)))
	local var_52_1 = arg_52_0.cellPos.InverseTransformPoint(arg_52_0.char.position)

	var_52_0.localPosition = Vector3(var_52_1.x + arg_52_1 + 100, 0, 0)
	var_52_0.localScale = Vector3(0.5, 0.5, 0.5)

	setActive(findTF(var_52_0, "bg_gold"), False)
	setActive(findTF(var_52_0, "bg_oil"), False)
	setActive(findTF(var_52_0, "bg_item"), False)

	local var_52_2 = arg_52_0.getPtAwardData(arg_52_0.useCount + 1)

	if var_52_2:
		if var_52_2[1] == 1 and var_52_2[2] == 1:
			setActive(findTF(var_52_0, "bg_gold"), True)
		elif var_52_2[1] == 1 and var_52_2[2] == 2:
			setActive(findTF(var_52_0, "bg_oil"), True)
		elif var_52_2[1] == 2 and var_52_2[2] == 54016:
			setActive(findTF(var_52_0, "bg_item"), True)
		else
			PoolMgr.GetInstance().GetSpineChar(var_0_4, True, function(arg_53_0)
				if var_52_0:
					arg_53_0.transform.localScale = Vector3(0.5, 0.5, 0.5)
					arg_53_0.transform.localPosition = Vector3.zero

					arg_53_0.transform.SetParent(findTF(var_52_0, "baoxiang"), False)

					local var_53_0 = arg_53_0.GetComponent(typeof(SpineAnimUI))

					arg_52_0.setModelAnim(var_53_0, "putong_guan", 0, None)

					arg_52_0.putongModel = arg_53_0
				else
					table.insert(arg_52_0.baoxiangCells, arg_53_0)
					setActive(arg_53_0, False))
	else
		setActive(findTF(var_52_0, "bg_item"), True)

	setActive(var_52_0, True)
	setParent(var_52_0, arg_52_0.cellPos)
	table.insert(arg_52_0.mapCells, var_52_0)

def var_0_0.getPtAwardData(arg_54_0, arg_54_1):
	if not arg_54_0.ptDatas:
		arg_54_0.ptDatas = pg.activity_event_pt[arg_54_0.activityId].drop_client

	if arg_54_1 <= #arg_54_0.ptDatas:
		return arg_54_0.ptDatas[arg_54_1]

	return None

def var_0_0.insertMapTf(arg_55_0, arg_55_1, arg_55_2, arg_55_3):
	if arg_55_2 == var_0_23:
		SetParent(arg_55_1, findTF(arg_55_0.container, "back"))
	elif arg_55_2 == var_0_24:
		SetParent(arg_55_1, findTF(arg_55_0.container, "mid"))
	elif arg_55_2 == var_0_25:
		SetParent(arg_55_1, findTF(arg_55_0.container, "front"))
	else
		print("没有配置层级，无法分配背景tf")

	setActive(arg_55_1, True)

	arg_55_1.anchoredPosition = Vector2(arg_55_3, 0)

def var_0_0.sortMap(arg_56_0, arg_56_1):
	local var_56_0 = {}

	for iter_56_0 = 1, #arg_56_0.mapGround:
		if arg_56_0.mapGround[iter_56_0].layer == arg_56_1:
			table.insert(var_56_0, arg_56_0.mapGround[iter_56_0])

	table.sort(var_56_0, function(arg_57_0, arg_57_1)
		if arg_57_0.index > arg_57_1.index:
			return False
		elif arg_57_0.index < arg_57_1.index:
			return True)

	for iter_56_1 = 1, #var_56_0:
		local var_56_1 = var_56_0[iter_56_1].tfs

		for iter_56_2, iter_56_3 in ipairs(var_56_1):
			iter_56_3.SetAsLastSibling()

def var_0_0.getGround(arg_58_0, arg_58_1):
	for iter_58_0 = 1, #arg_58_0.mapGround:
		local var_58_0 = arg_58_0.mapGround[iter_58_0]

		if var_58_0.name == arg_58_1:
			return var_58_0

	return None

def var_0_0.updateMap(arg_59_0, arg_59_1, arg_59_2):
	if arg_59_0.char:
		arg_59_0.char.anchoredPosition = Vector2(arg_59_0.char.anchoredPosition.x + arg_59_1, arg_59_0.char.anchoredPosition.y)

	arg_59_0.translate.anchoredPosition = Vector2(arg_59_0.mid.anchoredPosition.x + arg_59_0.distance - arg_59_1, 0)

	if arg_59_0.mapTf.InverseTransformPoint(arg_59_0.translate.position).x <= var_0_27 - 600:
		if arg_59_0.useCount < 9:
			arg_59_0.createMap("ground_1")
		elif arg_59_0.useCount < 20:
			arg_59_0.createMap("ground_4")

	arg_59_0.moveDistance = arg_59_0.moveDistance + arg_59_1
	arg_59_0.back.anchoredPosition = Vector2(arg_59_0.back.anchoredPosition.x - arg_59_1, 0)
	arg_59_0.mid.anchoredPosition = Vector2(arg_59_0.mid.anchoredPosition.x - arg_59_1, 0)
	arg_59_0.front.anchoredPosition = Vector2(arg_59_0.front.anchoredPosition.x - arg_59_1, 0)

	if #arg_59_0.mapCells > 0 and arg_59_0.mapTf.InverseTransformPoint(arg_59_0.mapCells[1].position).x < -1500:
		local var_59_0 = table.remove(arg_59_0.mapCells, 1)

		Destroy(var_59_0)

def var_0_0.setModelAnim(arg_60_0, arg_60_1, arg_60_2, arg_60_3, arg_60_4):
	arg_60_1.SetActionCallBack(None)
	arg_60_1.SetAction(arg_60_2, 0)
	arg_60_1.SetActionCallBack(function(arg_61_0)
		if arg_61_0 == "finish":
			if arg_60_3 == 1:
				arg_60_1.SetActionCallBack(None)

			if arg_60_4:
				arg_60_4())

	if arg_60_3 != 1 and arg_60_4:
		arg_60_4()

def var_0_0.changeCharAction(arg_62_0, arg_62_1, arg_62_2, arg_62_3):
	for iter_62_0 = 1, #arg_62_0.anims:
		local var_62_0 = iter_62_0
		local var_62_1 = arg_62_0.anims[iter_62_0]

		var_62_1.SetActionCallBack(None)
		var_62_1.SetAction(arg_62_1, 0)
		var_62_1.SetActionCallBack(function(arg_63_0)
			if arg_63_0 == "finish":
				if arg_62_2 == 1:
					var_62_1.SetActionCallBack(None)
					var_62_1.SetAction(var_0_11, 0)

				if var_62_0 == 1 and arg_62_3:
					arg_62_3())

		if var_62_0 == 1 and arg_62_2 != 1 and arg_62_3:
			arg_62_3()

def var_0_0.onHide(arg_64_0):
	return

def var_0_0.willExit(arg_65_0):
	if LeanTween.isTweening(go(arg_65_0.cellPos)):
		LeanTween.cancel(go(arg_65_0.cellPos))

	if LeanTween.isTweening(go(arg_65_0._tf)):
		LeanTween.cancel(go(arg_65_0._tf))

	if #arg_65_0.baoxiangCells > 0:
		for iter_65_0 = 1, #arg_65_0.baoxiangCells:
			PoolMgr.GetInstance().ReturnSpineChar(var_0_4, arg_65_0.baoxiangCells[iter_65_0])

		arg_65_0.baoxiangCells = {}

	if arg_65_0.enemyModel:
		PoolMgr.GetInstance().ReturnSpineChar(var_0_5, arg_65_0.enemyModel)

	if arg_65_0.baoxiangModel:
		PoolMgr.GetInstance().ReturnSpineChar(var_0_3, arg_65_0.baoxiangModel)

	if arg_65_0.mingShimodel:
		PoolMgr.GetInstance().ReturnSpineChar(var_0_1, arg_65_0.mingShimodel)

	for iter_65_1 = 1, #arg_65_0.models:
		PoolMgr.GetInstance().ReturnSpineChar(arg_65_0.modelIds[iter_65_1], arg_65_0.models[iter_65_1])

	for iter_65_2 = #arg_65_0.mapCells, 1, -1:
		Destroy(arg_65_0.mapCells[iter_65_2])

	arg_65_0.mapCells = {}

	if arg_65_0.awardsTimer:
		if arg_65_0.awardsTimer.running:
			arg_65_0.awardsTimer.Stop()

		arg_65_0.awardsTimer = None

	if arg_65_0.awardTfs and #arg_65_0.awardTfs > 0:
		for iter_65_3 = #arg_65_0.awardTfs, 1, -1:
			Destroy(table.remove(arg_65_0.awardTfs, iter_65_3))

return var_0_0
