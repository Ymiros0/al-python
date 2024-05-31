local var_0_0 = class("LaunchBallEnemy")
local var_0_1 = {}
local var_0_2 = 0.35
local var_0_3 = 70
local var_0_4 = 100
local var_0_5 = 80
local var_0_6 = 80
local var_0_7 = 50
local var_0_8 = {
	{
		0,
		60
	},
	{
		60,
		70
	},
	{
		120,
		80
	},
	{
		180,
		90
	},
	{
		240,
		100
	}
}
local var_0_9 = -300
local var_0_10 = -150
local var_0_11 = 0.5
local var_0_12 = 500
local var_0_13 = -500
local var_0_14 = 10
local var_0_15 = {
	{
		anim_name = "01_Yellow"
	},
	{
		anim_name = "02_Green"
	},
	{
		anim_name = "03_White"
	},
	{
		anim_name = "04_Red"
	},
	{
		anim_name = "05_Blue"
	},
	{
		anim_name = "06_Black"
	},
	{
		anim_name = "07_Purple"
	}
}

local function var_0_16(arg_1_0, arg_1_1)
	local var_1_0 = {
		def ctor:(arg_2_0)
			arg_2_0._tf = arg_1_0
			arg_2_0._animator = GetComponent(findTF(arg_2_0._tf, "ad/anim"), typeof(Animator))
			arg_2_0.angleTf = findTF(arg_2_0._tf, "ad/angle")
			arg_2_0.leftBoundPoints = {}

			local var_2_0 = GetComponent(findTF(arg_2_0._tf, "ad/angle/left"), typeof("UnityEngine.PolygonCollider2D"))

			for iter_2_0 = 0, var_2_0.points.Length - 1:
				table.insert(arg_2_0.leftBoundPoints, var_2_0.points[iter_2_0])

			arg_2_0.rightBoundPoints = {}

			local var_2_1 = GetComponent(findTF(arg_2_0._tf, "ad/angle/right"), typeof("UnityEngine.PolygonCollider2D"))

			for iter_2_1 = 0, var_2_1.points.Length - 1:
				table.insert(arg_2_0.rightBoundPoints, var_2_1.points[iter_2_1])

			arg_2_0.localRotation = Vector3(0, 0, 0)
			arg_2_0.circlePos = findTF(arg_2_0._tf, "ad/angle/circle").anchoredPosition

			if not arg_2_0.buffIcon:
				arg_2_0.buffIcon = findTF(arg_2_0._tf, "ad/iconEffect")

			arg_2_0._effectTf = findTF(arg_2_0._tf, "ad/effect")
			arg_2_0._playEffects = {},
		def setData:(arg_3_0, arg_3_1, arg_3_2)
			arg_3_0.clear()

			arg_3_0.enemyIndex = arg_3_1
			arg_3_0._animator.runtimeAnimatorController = arg_3_2.animator
			arg_3_0.data = arg_3_2
			arg_3_0.hp = arg_3_2.data.hp
			arg_3_0.overSplitFlag = False

			for iter_3_0 = 0, arg_3_0.buffIcon.childCount - 1:
				local var_3_0 = arg_3_0.buffIcon.GetChild(iter_3_0)

				setActive(var_3_0, False)

			for iter_3_1 = #arg_3_0._playEffects, 1, -1:
				setActive(arg_3_0._playEffects[iter_3_1].tf, False)
				table.remove(arg_3_0._playEffects, iter_3_1)

			arg_3_0.stopAnim(False),
		def setBuff:(arg_4_0, arg_4_1)
			arg_4_0.buffType = arg_4_1

			if arg_4_0.buffType:
				local var_4_0 = LaunchBallGameConst.enemy_buff_data[arg_4_0.buffType].tpl

				for iter_4_0 = 0, arg_4_0.buffIcon.childCount - 1:
					local var_4_1 = arg_4_0.buffIcon.GetChild(iter_4_0)

					setActive(var_4_1, var_4_1.name == var_4_0)
			else
				for iter_4_1 = 0, arg_4_0.buffIcon.childCount - 1:
					local var_4_2 = arg_4_0.buffIcon.GetChild(iter_4_1)

					setActive(var_4_2, False),
		def getBuff:(arg_5_0)
			return arg_5_0.buffType,
		def setPoints:(arg_6_0, arg_6_1)
			arg_6_0.points = arg_6_1,
		def hit:(arg_7_0)
			if arg_7_0.buffType and arg_7_0.buffType == LaunchBallGameConst.enemy_buff_streng:
				arg_7_0.setBuff(None)

				return

			arg_7_0.hp = arg_7_0.hp - 1

			if arg_7_0.hp <= 0:
				arg_7_0.setTimeRemove(),
		def getTf:(arg_8_0)
			return arg_8_0._tf,
		def playAnimation:(arg_9_0, arg_9_1)
			arg_9_0._animator.Play(arg_9_1),
		def setActive:(arg_10_0, arg_10_1)
			setActive(arg_10_0._tf, arg_10_1),
		def getColor:(arg_11_0)
			return arg_11_0.data.data.color,
		def getSplitFlag:(arg_12_0)
			return arg_12_0.splitFlag,
		def setSplitFlag:(arg_13_0, arg_13_1)
			arg_13_0.splitFlag = arg_13_1,
		def step:(arg_14_0)
			if arg_14_0.timeToRemove and arg_14_0.timeToRemove > 0:
				arg_14_0.timeToRemove = arg_14_0.timeToRemove - LaunchBallGameVo.deltaTime

				if arg_14_0.timeToRemove <= 0:
					arg_14_0.timeToRemove = None
					arg_14_0.removeFlag = True

			if #arg_14_0._playEffects > 0:
				for iter_14_0 = #arg_14_0._playEffects, 1, -1:
					local var_14_0 = arg_14_0._playEffects[iter_14_0]

					if var_14_0.time:
						var_14_0.time = var_14_0.time - LaunchBallGameVo.deltaTime

					if var_14_0.time and var_14_0.time <= 0:
						setActive(var_14_0.tf, False)
						table.remove(arg_14_0._playEffects, iter_14_0),
		def move:(arg_15_0, arg_15_1, arg_15_2, arg_15_3, arg_15_4)
			if arg_15_1 == 0:
				return

			var_0_0.moveCount = var_0_0.moveCount + 1
			arg_15_0.distance = arg_15_0.distance + arg_15_1

			if arg_15_0.distance < 0:
				arg_15_0.distance = 0

			if arg_15_2 and arg_15_3 and arg_15_4:
				arg_15_0._tf.anchoredPosition = arg_15_2
				arg_15_0.pointIndex = arg_15_3
				arg_15_0.localRotation = arg_15_4
				arg_15_0.angleTf.localEulerAngles = arg_15_0.localRotation
			else
				local var_15_0 = arg_15_0.getPosByDistance(arg_15_0.distance)
				local var_15_1 = arg_15_0._tf.anchoredPosition

				var_15_1.x = var_15_0.x
				var_15_1.y = var_15_0.y
				arg_15_0._tf.anchoredPosition = var_15_1
				arg_15_0.pointIndex = var_15_0.index
				arg_15_0.localRotation.z = arg_15_0.points[arg_15_0.pointIndex].angle
				arg_15_0.angleTf.localEulerAngles = arg_15_0.localRotation,
		def getPosition:(arg_16_0)
			return arg_16_0._tf.anchoredPosition,
		def getPointIndex:(arg_17_0)
			return arg_17_0.pointIndex,
		def getLocalRotation:(arg_18_0)
			return arg_18_0.localRotation,
		def stopAnim:(arg_19_0, arg_19_1)
			if arg_19_1:
				arg_19_0._animator.speed = 0
			else
				arg_19_0._animator.speed = 1,
		def checkWorldInCircle:(arg_20_0, arg_20_1)
			local var_20_0 = arg_20_0.angleTf.InverseTransformPoint(arg_20_1)

			if math.abs(var_20_0.x - arg_20_0.circlePos.x) >= 150 or math.abs(var_20_0.y - arg_20_0.circlePos.y) >= var_0_5 * 2:
				return False

			local var_20_1 = 0

			if math.sqrt(math.pow(var_20_0.x - arg_20_0.circlePos.x, 2) + math.pow(var_20_0.y - arg_20_0.circlePos.y, 2)) < var_0_5:
				return True

			return False,
		def checkWorldInRect:(arg_21_0, arg_21_1)
			local var_21_0 = arg_21_0.angleTf.InverseTransformPoint(arg_21_1)
			local var_21_1 = 0
			local var_21_2 = math.sqrt(math.pow(var_21_0.x - arg_21_0.circlePos.x, 2) + math.pow(var_21_0.y - arg_21_0.circlePos.y, 2))

			if var_21_2 > var_0_3:
				return var_21_1, None

			if LaunchBallGameVo.PointInRect(var_21_0, arg_21_0.leftBoundPoints[1], arg_21_0.leftBoundPoints[2], arg_21_0.leftBoundPoints[3], arg_21_0.leftBoundPoints[4]):
				var_21_1 = -1
			elif LaunchBallGameVo.PointInRect(var_21_0, arg_21_0.rightBoundPoints[1], arg_21_0.rightBoundPoints[2], arg_21_0.rightBoundPoints[3], arg_21_0.rightBoundPoints[4]):
				var_21_1 = 1

			return var_21_1, var_21_2,
		def getPosByDistance:(arg_22_0, arg_22_1)
			local var_22_0 = math.floor(arg_22_1 * 2)

			if var_0_0.EnemyDistanceData[arg_22_0.enemyIndex][var_22_0]:
				return var_0_0.EnemyDistanceData[arg_22_0.enemyIndex][var_22_0]

			local var_22_1 = var_22_0 / 2

			if not arg_22_0.distancePosResult:
				arg_22_0.distancePosResult = Vector2(0, 0)

			local var_22_2 = 1
			local var_22_3 = 0

			for iter_22_0 = 1, #arg_22_0.points:
				local var_22_4 = arg_22_0.points[iter_22_0]

				if var_22_1 >= var_22_4.distance:
					var_22_2 = iter_22_0

					if iter_22_0 < #arg_22_0.points:
						var_22_3 = var_22_1 - var_22_4.distance
						arg_22_0.distancePosResult.x = var_22_4.pos.x
						arg_22_0.distancePosResult.y = var_22_4.pos.y
					else
						arg_22_0.distancePosResult.x = var_22_4.pos.x
						arg_22_0.distancePosResult.y = var_22_4.pos.y
						var_22_3 = 0
				else
					break

			if var_22_3 != 0:
				local var_22_5 = arg_22_0.points[var_22_2].move

				arg_22_0.distancePosResult.x = arg_22_0.distancePosResult.x + var_22_5.x * var_22_3
				arg_22_0.distancePosResult.y = arg_22_0.distancePosResult.y + var_22_5.y * var_22_3

			local var_22_6 = {
				x = arg_22_0.distancePosResult.x,
				y = arg_22_0.distancePosResult.y,
				index = var_22_2
			}

			var_0_0.EnemyDistanceData[arg_22_0.enemyIndex][var_22_0] = var_22_6

			return var_22_6,
		def setTimeRemove:(arg_23_0)
			if arg_23_0.hp > 0:
				arg_23_0.hp = 0

			pg.CriMgr.GetInstance().PlaySoundEffect_V3(LaunchBallGameVo.SFX_ENEMY_REMOVE)

			if arg_23_0.getBuff(LaunchBallGameConst.enemy_buff_boom):
				local var_23_0 = arg_23_0.getColor()
				local var_23_1 = var_0_15[var_23_0].anim_name

				arg_23_0.playEffectAnim("Bomb", var_23_1, 0.2)

			arg_23_0.stopAnim(False)
			arg_23_0.playAnimation("Remove")

			arg_23_0.timeToRemove = var_0_2,
		def playEffectAnim:(arg_24_0, arg_24_1, arg_24_2, arg_24_3)
			local var_24_0 = findTF(arg_24_0._effectTf, arg_24_1)

			setActive(var_24_0, True)
			GetComponent(var_24_0, typeof(Animator)).Play(arg_24_2)
			table.insert(arg_24_0._playEffects, {
				tf = var_24_0,
				time = arg_24_3
			}),
		def getTimeRemove:(arg_25_0)
			return arg_25_0.timeToRemove,
		def setPosIndex:(arg_26_0, arg_26_1)
			arg_26_0._tf.anchoredPosition = arg_26_0.points[arg_26_1].pos
			arg_26_0.pointIndex = arg_26_1
			arg_26_0.distance = arg_26_0.points[arg_26_1].distance,
		def setDistance:(arg_27_0, arg_27_1)
			arg_27_0.distance = arg_27_1
			arg_27_0._tf.anchoredPosition = arg_27_0.getPosByDistance(arg_27_0.distance),
		def getDistance:(arg_28_0)
			return arg_28_0.distance,
		def getRemoveFlag:(arg_29_0)
			return arg_29_0.removeFlag,
		def setLastLayer:(arg_30_0, arg_30_1)
			return arg_30_0._tf.SetSiblingIndex(arg_30_1),
		def getFinish:(arg_31_0)
			return arg_31_0.distance >= arg_31_0.points[#arg_31_0.points].distance,
		def clear:(arg_32_0)
			arg_32_0.finalFlag = False
			arg_32_0.removeFlag = False
			arg_32_0.timeToRemove = None
			arg_32_0.buffType = None
	}

	var_1_0.ctor()

	return var_1_0

var_0_0.EnemyDistanceData = {}

def var_0_0.Ctor(arg_33_0, arg_33_1, arg_33_2, arg_33_3, arg_33_4):
	arg_33_0._enemyContent = arg_33_1
	arg_33_0._lineContent = arg_33_2
	arg_33_0._tpl = arg_33_3
	arg_33_0._eventCall = arg_33_4
	arg_33_0._enemyTpl = findTF(arg_33_0._tpl, "Enemy")
	arg_33_0.enemyDatas = {}

	for iter_33_0, iter_33_1 in pairs(LaunchBallGameConst.enemy_data):
		local var_33_0 = ResourceMgr.Inst.getAssetSync(LaunchBallGameVo.ui_atlas, iter_33_1.name, typeof(RuntimeAnimatorController), False, False)

		table.insert(arg_33_0.enemyDatas, {
			animator = var_33_0,
			data = iter_33_1
		})

	arg_33_0.enemyRule = Clone(LaunchBallGameConst.enemy_create_rule)
	arg_33_0.enemysList = {}
	arg_33_0.enemyPool = {}
	arg_33_0.colliderTestTf = findTF(arg_33_0._enemyContent, "colliderTest")

	setActive(arg_33_0.colliderTestTf, False)

def var_0_0.start(arg_34_0):
	arg_34_0.moveSpeed = LaunchBallGameVo.gameRoundData.speed
	var_0_0.EnemyDistanceData = {}
	arg_34_0.gameRoundData = LaunchBallGameVo.gameRoundData
	arg_34_0._enemyContent.sizeDelta = LaunchBallGameConst.enemy_round_bound[arg_34_0.gameRoundData.round_bound]
	arg_34_0.roundDatas = Clone(LaunchBallGameConst.round_enemy[arg_34_0.gameRoundData.round_enemy])
	arg_34_0.lineData = Clone(LaunchBallGameConst.map_data[arg_34_0.gameRoundData.map])
	arg_34_0.enemyBuffs = Clone(LaunchBallGameConst.enemy_round_buff[arg_34_0.gameRoundData.enemy_buff])

	arg_34_0.createRoundData()

	arg_34_0.currentEnemyRule = arg_34_0.getEnemyRule()

	if arg_34_0.lineTf:
		setActive(arg_34_0.lineTf, False)

	arg_34_0.lineTf = findTF(arg_34_0._lineContent, arg_34_0.lineData.line)

	setActive(arg_34_0.lineTf, True)

	for iter_34_0, iter_34_1 in ipairs(arg_34_0.enemysList):
		for iter_34_2 = #iter_34_1, 1, -1:
			arg_34_0.returnEnemy(table.remove(iter_34_1, iter_34_2))

	arg_34_0.pointsList = {}
	arg_34_0.enemysList = {}

	local var_34_0 = findTF(arg_34_0.lineTf, "ad/points")

	if var_34_0:
		local var_34_1 = arg_34_0.createPoints(var_34_0)

		table.insert(arg_34_0.pointsList, var_34_1)
		table.insert(arg_34_0.enemysList, {})

		var_0_0.EnemyDistanceData[1] = {}

	local var_34_2 = findTF(arg_34_0.lineTf, "ad/points1")

	if var_34_2:
		local var_34_3 = arg_34_0.createPoints(var_34_2)

		table.insert(arg_34_0.pointsList, var_34_3)
		table.insert(arg_34_0.enemysList, {})

		var_0_0.EnemyDistanceData[2] = {}

	for iter_34_3 = 1, #arg_34_0.pointsList:
		arg_34_0.createRandomEnemy(iter_34_3, arg_34_0.pointsList[iter_34_3], arg_34_0.enemysList[iter_34_3], 1, 0, True)

	arg_34_0.backEnemyFlag = False
	arg_34_0.backEnemyTime = None
	arg_34_0.seriesCount = 1
	arg_34_0.lastPointDistance = None

var_0_0.moveCount = 0

def var_0_0.step(arg_35_0):
	var_0_0.moveCount = 0

	arg_35_0.checkEnemyRuleUpdate()
	arg_35_0.checkEnemyDataUpdate()
	arg_35_0.checkCreateEnemy()
	arg_35_0.checkRemoveEnemy()
	arg_35_0.moveEnmey()
	arg_35_0.checkEnemyQuick()
	arg_35_0.checkEnemyBack()
	arg_35_0.updateEnemyRemoveFlag()
	arg_35_0.checkEnemySplit()
	arg_35_0.updateEnemyVo()
	arg_35_0.checkEnemyFinal()
	arg_35_0.updateEnemyData()

def var_0_0.updateEnemyData(arg_36_0):
	if not arg_36_0.lastPointDistance:
		arg_36_0.lastPointDistance = {}

		for iter_36_0 = 1, #arg_36_0.pointsList:
			local var_36_0 = arg_36_0.pointsList[iter_36_0]

			table.insert(arg_36_0.lastPointDistance, var_36_0[#var_36_0].distance)

	local var_36_1 = {}
	local var_36_2 = 0

	for iter_36_1 = 1, #arg_36_0.enemysList:
		local var_36_3 = arg_36_0.enemysList[iter_36_1]

		if var_36_3 and #var_36_3 > 0:
			local var_36_4 = var_36_3[#var_36_3].getDistance()

			table.insert(var_36_1, math.floor(var_36_4 / arg_36_0.lastPointDistance[iter_36_1] * 10))

	LaunchBallGameVo.enemyToEndRate = var_36_1

def var_0_0.checkEnemyDataUpdate(arg_37_0):
	if arg_37_0.currentEnemyRule == None:
		arg_37_0.currentEnemyRule = arg_37_0.getEnemyRule()

def var_0_0.checkTargetScore(arg_38_0):
	if LaunchBallGameVo.gameRoundData.target and LaunchBallGameVo.scoreNum >= LaunchBallGameVo.gameRoundData.target:
		return True

	return False

def var_0_0.checkCreateEnemy(arg_39_0):
	if arg_39_0.checkTargetScore():
		return

	local var_39_0 = 1

	for iter_39_0 = 1, #arg_39_0.enemysList:
		local var_39_1 = arg_39_0.enemysList[iter_39_0]
		local var_39_2 = arg_39_0.pointsList[iter_39_0]

		if #var_39_1 > 0:
			if var_39_1[1].getDistance() > var_0_6:
				arg_39_0.createRandomEnemy(iter_39_0, var_39_2, var_39_1, 1, 0, True)

				break
		else
			arg_39_0.createRandomEnemy(iter_39_0, var_39_2, var_39_1, 1, 0, True)

			break

def var_0_0.checkRemoveEnemy(arg_40_0):
	for iter_40_0, iter_40_1 in ipairs(arg_40_0.enemysList):
		local var_40_0 = False

		for iter_40_2 = #iter_40_1, 1, -1:
			iter_40_1[iter_40_2].step()

			if iter_40_1[iter_40_2].getRemoveFlag():
				local var_40_1 = iter_40_1[iter_40_2].getBuff()

				if var_40_1:
					arg_40_0.appearEnemyBuff(var_40_1, iter_40_2, iter_40_1[iter_40_2], iter_40_1)

				arg_40_0.returnEnemy(table.remove(iter_40_1, iter_40_2))

				local var_40_2 = True

	if arg_40_0.timeRemoveAll and arg_40_0.timeRemoveAll > 0:
		arg_40_0.timeRemoveAll = arg_40_0.timeRemoveAll - LaunchBallGameVo.deltaTime

		if arg_40_0.timeRemoveAll <= 0:
			local var_40_3 = 0

			for iter_40_3, iter_40_4 in ipairs(arg_40_0.enemysList):
				for iter_40_5 = #iter_40_4, 1, -1:
					local var_40_4 = iter_40_4[iter_40_5]

					if not var_40_4.getRemoveFlag():
						var_40_4.setTimeRemove()

						var_40_3 = var_40_3 + 1

						local var_40_5 = LaunchBallGameVo.GetScore(1, 1)

						arg_40_0._eventCall(LaunchBallGameScene.SPILT_ENEMY_SCORE, {
							num = var_40_5
						})

			LaunchBallGameVo.UpdateGameResultData(LaunchBallGameVo.result_skill_count, var_40_3)

			arg_40_0.timeRemoveAll = None

def var_0_0.appearEnemyBuff(arg_41_0, arg_41_1, arg_41_2, arg_41_3, arg_41_4):
	local var_41_0 = LaunchBallGameConst.enemy_buff_data[arg_41_1]

	if arg_41_1 == LaunchBallGameConst.enemy_buff_slow:
		arg_41_0.slowTime = var_41_0.time

		if LaunchBallGameVo.GetBuff(LaunchBallPlayerControl.buff_time_max):
			arg_41_0.slowTime = arg_41_0.slowTime * 1.5

			LaunchBallGameVo.AddGameResultData(LaunchBallGameVo.result_use_pass_skill, 1)

			if arg_41_0.enemyStopTime and arg_41_0.enemyStopTime > 0:
				arg_41_0.enemyStopTime = arg_41_0.enemyStopTime + 3
	elif arg_41_1 == LaunchBallGameConst.enemy_buff_back:
		arg_41_0.backEnemyTime = var_41_0.time
		arg_41_0.backSpeed = var_0_10
		arg_41_0.moveBackIndex = #arg_41_4

		if LaunchBallGameVo.GetBuff(LaunchBallPlayerControl.buff_time_max):
			arg_41_0.backEnemyTime = arg_41_0.backEnemyTime * 1.3

			LaunchBallGameVo.AddGameResultData(LaunchBallGameVo.result_use_pass_skill, 1)
	elif arg_41_1 == LaunchBallGameConst.enemy_buff_boom:
		local var_41_1 = arg_41_3.getDistance()
		local var_41_2 = var_41_0.distance

		for iter_41_0 = 1, #arg_41_4:
			if not arg_41_4[iter_41_0].getRemoveFlag() and var_41_2 >= math.abs(arg_41_4[iter_41_0].getDistance() - var_41_1):
				arg_41_4[iter_41_0].setTimeRemove()

				local var_41_3 = LaunchBallGameVo.GetScore(1, 1)

				arg_41_0._eventCall(LaunchBallGameScene.SPILT_ENEMY_SCORE, {
					num = var_41_3
				})
	elif arg_41_1 == LaunchBallGameConst.enemy_buff_concentrate:
		arg_41_0._eventCall(LaunchBallGameScene.CONCENTRATE_TRIGGER, var_41_0)

def var_0_0.moveEnmey(arg_42_0):
	local var_42_0

	if arg_42_0.enemyStopTime and arg_42_0.enemyStopTime > 0:
		arg_42_0.enemyStopTime = arg_42_0.enemyStopTime - LaunchBallGameVo.deltaTime

		if arg_42_0.enemyStopTime <= 0:
			arg_42_0.enemyStopTime = None

			arg_42_0.stopEnemysAnim(False)

		LaunchBallGameVo.enemyStopTime = arg_42_0.enemyStopTime

	if arg_42_0.enemyStopTime and arg_42_0.enemyStopTime > 0:
		return

	if arg_42_0.backEnemyTime and arg_42_0.backEnemyTime > 0:
		arg_42_0.backEnemyTime = arg_42_0.backEnemyTime - LaunchBallGameVo.deltaTime

		if arg_42_0.backEnemyTime <= 0:
			arg_42_0.backEnemyTime = None

		var_42_0 = arg_42_0.backSpeed * LaunchBallGameVo.deltaTime
	else
		var_42_0 = arg_42_0.moveSpeed * LaunchBallGameVo.deltaTime

	if arg_42_0.slowTime and arg_42_0.slowTime > 0:
		var_42_0 = var_42_0 / 3
		arg_42_0.slowTime = arg_42_0.slowTime - LaunchBallGameVo.deltaTime

		if arg_42_0.slowTime < 0:
			arg_42_0.slowTime = None

	local var_42_1 = {}

	for iter_42_0, iter_42_1 in ipairs(arg_42_0.enemysList):
		local var_42_2 = 0

		if var_42_0 > 0:
			for iter_42_2 = 1, #iter_42_1:
				local var_42_3 = False

				if iter_42_2 < #iter_42_1 and iter_42_1[iter_42_2].getDistance() < var_0_6 and iter_42_1[iter_42_2 + 1].getDistance() < var_0_6:
					var_42_3 = True

				if iter_42_2 > 1 and var_42_2 == 0:
					if iter_42_1[iter_42_2].getDistance() - iter_42_1[iter_42_2 - 1].getDistance() > var_0_6:
						var_42_2 = iter_42_2
						var_42_3 = True
					elif iter_42_1[iter_42_2].getRemoveFlag():
						var_42_2 = iter_42_2
						var_42_3 = True
				elif var_42_2 != 0 and var_42_2 <= iter_42_2:
					var_42_3 = True

				if not var_42_3:
					iter_42_1[iter_42_2].move(var_42_0)

		if var_42_0 < 0:
			for iter_42_3 = #iter_42_1, 1, -1:
				local var_42_4 = False

				if iter_42_3 <= arg_42_0.moveBackIndex and var_42_2 == 0:
					if iter_42_3 > 1 and iter_42_1[iter_42_3].getDistance() - iter_42_1[iter_42_3 - 1].getDistance() > var_0_6 + var_0_14:
						var_42_2 = iter_42_3 - 1
				else
					var_42_4 = var_42_2 != 0 and iter_42_3 <= var_42_2 and True or True

				if not var_42_4:
					iter_42_1[iter_42_3].move(var_42_0)

def var_0_0.checkEnemyQuick(arg_43_0):
	if arg_43_0.backFlag:
		return

	arg_43_0.quickFlag = False

	for iter_43_0, iter_43_1 in ipairs(arg_43_0.enemysList):
		local var_43_0 = 0

		for iter_43_2 = 1, #iter_43_1:
			local var_43_1 = iter_43_1[iter_43_2]

			if iter_43_2 <= #iter_43_1 - 1:
				local var_43_2 = iter_43_1[iter_43_2 + 1]

				if var_43_2.getDistance() > var_0_6 and var_43_2.getDistance() - var_43_1.getDistance() < var_0_6 - var_0_14:
					var_43_0 = iter_43_2 + 1
					arg_43_0.quickFlag = True

					break

		if var_43_0 != 0:
			for iter_43_3 = 1, #iter_43_1:
				if var_43_0 <= iter_43_3:
					local var_43_3 = iter_43_1[iter_43_3 - 1]

					if iter_43_1[iter_43_3].getDistance() - var_43_3.getDistance() < var_0_6 - var_0_14:
						iter_43_1[iter_43_3].move(var_0_12 * LaunchBallGameVo.deltaTime)
					else
						break

def var_0_0.checkEnemyBack(arg_44_0):
	arg_44_0.backFlag = False

	if not arg_44_0.quickFlag:
		for iter_44_0, iter_44_1 in ipairs(arg_44_0.enemysList):
			local var_44_0 = 0

			for iter_44_2 = 1, #iter_44_1:
				if iter_44_2 > 1 and var_44_0 == 0 and iter_44_1[iter_44_2].getDistance() - iter_44_1[iter_44_2 - 1].getDistance() > var_0_6 + var_0_14 and iter_44_1[iter_44_2].getSplitFlag() and iter_44_1[iter_44_2].getColor() == iter_44_1[iter_44_2 - 1].getColor():
					var_44_0 = iter_44_2

					if not arg_44_0.backEnemyFlag:
						arg_44_0.backEnemyFlag = True

			if var_44_0 != 0:
				arg_44_0.backFlag = True
				arg_44_0.moveBackIndex = 0

				for iter_44_3 = 1, #iter_44_1:
					if iter_44_3 == var_44_0:
						arg_44_0.moveBackIndex = iter_44_3

						iter_44_1[iter_44_3].move(var_0_13 * LaunchBallGameVo.deltaTime)
					elif var_44_0 < iter_44_3:
						if iter_44_1[iter_44_3].getDistance() - iter_44_1[iter_44_3 - 1].getDistance() < var_0_6 + var_0_14:
							iter_44_1[iter_44_3].move(var_0_13 * LaunchBallGameVo.deltaTime)

							arg_44_0.moveBackIndex = iter_44_3
						else
							break

	if arg_44_0.backFlag and arg_44_0.backEnemyFlag:
		arg_44_0.backEnemyFlag = False
		arg_44_0.backEnemyTime = var_0_11
		arg_44_0.backSpeed = var_0_9

def var_0_0.updateEnemyRemoveFlag(arg_45_0):
	arg_45_0.enemyTimeRemoveFlag = False

	for iter_45_0, iter_45_1 in ipairs(arg_45_0.enemysList):
		local var_45_0 = 0

		for iter_45_2 = 1, #iter_45_1:
			if iter_45_1[iter_45_2].getTimeRemove():
				arg_45_0.enemyTimeRemoveFlag = True

def var_0_0.checkEnemySplit(arg_46_0):
	if not arg_46_0.enemyTimeRemoveFlag and not arg_46_0.backFlag and not arg_46_0.quickFlag and not arg_46_0.backEnemyFlag:
		for iter_46_0, iter_46_1 in ipairs(arg_46_0.enemysList):
			local var_46_0 = 0

			for iter_46_2 = 1, #iter_46_1:
				local var_46_1 = iter_46_1[iter_46_2]

				if var_46_1.getSplitFlag():
					local var_46_2 = iter_46_2
					local var_46_3, var_46_4, var_46_5 = arg_46_0.checkSplit(var_46_2, iter_46_1)

					var_46_1.setSplitFlag(False)

					if var_46_3 >= 3 or var_46_4:
						arg_46_0.seriesCount = arg_46_0.seriesCount + 1

						if arg_46_0.splitFireIndex and arg_46_0.splitFireIndex + 1 >= arg_46_0.fireIndex:
							LaunchBallGameVo.AddGameResultData(LaunchBallGameVo.result_series_count, 1)

							if not arg_46_0.seriesCombat:
								arg_46_0.seriesCombat = 1
							else
								arg_46_0.seriesCombat = arg_46_0.seriesCombat + 1
						else
							arg_46_0.seriesCombat = 0

						if arg_46_0.amuletOverFlag:
							LaunchBallGameVo.AddGameResultData(LaunchBallGameVo.result_over_count, 1)

						arg_46_0.splitFireIndex = arg_46_0.fireIndex

						break

					arg_46_0.seriesCount = 1
					arg_46_0.seriesCombat = 0

					break

def var_0_0.checkEnemyFinal(arg_47_0):
	if arg_47_0.checkTargetScore():
		local var_47_0 = 0

		for iter_47_0, iter_47_1 in ipairs(arg_47_0.enemysList):
			var_47_0 = var_47_0 + #iter_47_1

		if var_47_0 == 0:
			arg_47_0._eventCall(LaunchBallGameScene.ENEMY_FINISH)

			return

	for iter_47_2, iter_47_3 in ipairs(arg_47_0.enemysList):
		if iter_47_3 and #iter_47_3 > 0 and iter_47_3[#iter_47_3].getFinish():
			arg_47_0._eventCall(LaunchBallGameScene.ENEMY_FINISH)

			return

def var_0_0.updateEnemyVo(arg_48_0):
	local var_48_0 = {}

	for iter_48_0, iter_48_1 in ipairs(arg_48_0.enemysList):
		for iter_48_2 = 1, #iter_48_1:
			local var_48_1 = iter_48_1[iter_48_2].getColor()

			if not table.contains(var_48_0, var_48_1):
				table.insert(var_48_0, var_48_1)

				if #var_48_0 >= LaunchBallGameConst.color_total:
					LaunchBallGameVo.enemyColors = var_48_0

					return

	LaunchBallGameVo.enemyColors = var_48_0

def var_0_0.updateGameResultSplitCount(arg_49_0, arg_49_1, arg_49_2):
	LaunchBallGameVo.AddGameResultData(LaunchBallGameVo.result_split_count, 1)

	if arg_49_2 > 1:
		LaunchBallGameVo.AddGameResultData(LaunchBallGameVo.result_series_count, 1)
		LaunchBallGameVo.AddGameResultData(LaunchBallGameVo.result_mix_count, 1)

	if arg_49_1 > 3:
		LaunchBallGameVo.AddGameResultData(LaunchBallGameVo.result_many_count, 1)

def var_0_0.checkSplit(arg_50_0, arg_50_1, arg_50_2):
	local var_50_0 = arg_50_2[arg_50_1].getColor()
	local var_50_1 = 1
	local var_50_2 = {
		arg_50_2[arg_50_1]
	}
	local var_50_3 = False
	local var_50_4 = 0
	local var_50_5 = 0

	if arg_50_1 > 1:
		for iter_50_0 = arg_50_1 - 1, 1, -1:
			if arg_50_2[iter_50_0].getColor() == var_50_0:
				table.insert(var_50_2, arg_50_2[iter_50_0])

				var_50_1 = var_50_1 + 1
				var_50_5 = var_50_5 + 1
			else
				break

	local var_50_6

	if arg_50_1 < #arg_50_2:
		for iter_50_1 = arg_50_1 + 1, #arg_50_2:
			if arg_50_2[iter_50_1].getColor() == var_50_0:
				table.insert(var_50_2, arg_50_2[iter_50_1])

				var_50_1 = var_50_1 + 1
				var_50_4 = var_50_4 + 1
			else
				var_50_6 = arg_50_2[iter_50_1]

				break

	if var_50_1 >= 3:
		var_50_3 = True

	if var_50_1 >= 3 and not var_50_3:
		print("")

	if var_50_3 and var_50_6:
		var_50_6.setSplitFlag(True)

	if var_50_3:
		for iter_50_2 = 1, #var_50_2:
			var_50_2[iter_50_2].hit()

		if arg_50_0._eventCall:
			local var_50_7 = LaunchBallGameVo.GetScore(var_50_1, arg_50_0.seriesCount, arg_50_0.amuletOverFlag)

			arg_50_0._eventCall(LaunchBallGameScene.SPILT_ENEMY_SCORE, {
				split = True,
				num = var_50_7,
				count = var_50_1
			})

			if LaunchBallGameVo.GetBuff(LaunchBallPlayerControl.buff_time_max) and arg_50_0.enemyStopTime and arg_50_0.enemyStopTime > 0:
				LaunchBallGameVo.AddGameResultData(LaunchBallGameVo.result_skill_count, var_50_1)

		arg_50_0.updateGameResultSplitCount(var_50_1, arg_50_0.seriesCount)

		if not var_50_6:
			arg_50_0.seriesCount = 0

	return var_50_1, var_50_3

def var_0_0.createPoints(arg_51_0, arg_51_1):
	local var_51_0 = {}
	local var_51_1 = 0
	local var_51_2 = GetComponent(arg_51_1, "EdgeCollider2D")

	for iter_51_0 = 0, var_51_2.points.Length - 1:
		local var_51_3 = var_51_2.points[iter_51_0]
		local var_51_4 = Vector2(0, 0)
		local var_51_5 = Vector2(0, 0)
		local var_51_6 = 0
		local var_51_7 = 0

		if iter_51_0 >= 1:
			local var_51_8 = var_51_2.points[iter_51_0 - 1]
			local var_51_9 = var_51_2.points[iter_51_0]

			var_51_1 = var_51_1 + math.sqrt(math.pow(var_51_9.x - var_51_8.x, 2) + math.pow(var_51_9.y - var_51_8.y, 2))

		if iter_51_0 < var_51_2.points.Length - 1:
			local var_51_10 = var_51_2.points[iter_51_0]
			local var_51_11 = var_51_2.points[iter_51_0 + 1]
			local var_51_12 = math.atan(math.abs(var_51_11.y - var_51_10.y) / math.abs(var_51_11.x - var_51_10.x))

			var_51_7 = math.atan2(var_51_11.y - var_51_10.y, var_51_11.x - var_51_10.x) * math.rad2Deg

			local var_51_13 = var_51_11.x > var_51_10.x and 1 or -1
			local var_51_14 = var_51_11.y > var_51_10.y and 1 or -1

			var_51_5.x = var_51_13
			var_51_5.y = var_51_14
			var_51_4.x = math.cos(var_51_12) * var_51_13
			var_51_4.y = math.sin(var_51_12) * var_51_14
		elif iter_51_0 == var_51_2.points.Length - 1:
			local var_51_15 = var_51_2.points[iter_51_0 - 1]
			local var_51_16 = var_51_2.points[iter_51_0]
			local var_51_17 = math.atan(math.abs(var_51_16.y - var_51_15.y) / math.abs(var_51_16.x - var_51_15.x))

			var_51_7 = math.atan2(var_51_16.y - var_51_15.y, var_51_16.x - var_51_15.x) * math.rad2Deg

			local var_51_18 = var_51_16.x > var_51_15.x and 1 or -1
			local var_51_19 = var_51_16.y > var_51_15.y and 1 or -1

			var_51_5.x = var_51_18
			var_51_5.y = var_51_19
			var_51_4.x = math.cos(var_51_17) * var_51_18
			var_51_4.y = math.sin(var_51_17) * var_51_19

		table.insert(var_51_0, {
			pos = var_51_3,
			distance = var_51_1,
			move = var_51_4,
			direct = var_51_5,
			angle = var_51_7
		})

	return var_51_0

def var_0_0.createEnemy(arg_52_0, arg_52_1, arg_52_2, arg_52_3, arg_52_4, arg_52_5):
	local var_52_0 = arg_52_0.getOrCreateEnemy()

	var_52_0.setData(arg_52_1, arg_52_2)
	var_52_0.setPoints(arg_52_3)
	var_52_0.setActive(True)
	var_52_0.setSplitFlag(False)

	if arg_52_5:
		var_52_0.setDistance(arg_52_5)
	else
		var_52_0.setDistance(0)

	table.insert(arg_52_4, var_52_0)
	arg_52_0.sortEnemys(arg_52_4)

	return var_52_0

def var_0_0.createRandomEnemy(arg_53_0, arg_53_1, arg_53_2, arg_53_3, arg_53_4, arg_53_5, arg_53_6):
	local var_53_0 = arg_53_0.getEnemyDataByRule()

	if not var_53_0:
		return

	local var_53_1 = arg_53_0.getOrCreateEnemy()
	local var_53_2 = arg_53_0.getEnemyBuff()

	var_53_1.setData(arg_53_1, var_53_0)
	var_53_1.setBuff(var_53_2)
	var_53_1.setPoints(arg_53_2)
	var_53_1.setActive(True)

	if arg_53_4 and arg_53_4 != 0:
		var_53_1.setPosIndex(arg_53_4)
	elif arg_53_5:
		var_53_1.setDistance(arg_53_5)

	table.insert(arg_53_3, var_53_1)
	arg_53_0.sortEnemys(arg_53_3)

	return var_53_1

def var_0_0.getEnemyBuff(arg_54_0):
	local var_54_0 = {}

	for iter_54_0 = 1, #arg_54_0.enemyBuffs.buffs:
		local var_54_1 = arg_54_0.enemyBuffs.buffs[iter_54_0]
		local var_54_2 = True

		if var_54_1.type == LaunchBallGameConst.enemy_buff_back:
			if arg_54_0.getEnemyByBuff(LaunchBallGameConst.enemy_buff_slow):
				var_54_2 = False
		elif var_54_1.type == LaunchBallGameConst.enemy_buff_slow and arg_54_0.getEnemyByBuff(LaunchBallGameConst.enemy_buff_back):
			var_54_2 = False

		if var_54_2:
			local var_54_3 = var_54_1.rate
			local var_54_4 = var_54_3[1]

			if LaunchBallGameVo.GetBuff(LaunchBallPlayerControl.buff_time_max):
				if var_54_1.type == LaunchBallGameConst.enemy_buff_slow:
					var_54_4 = var_54_4 + 2
				elif var_54_1.type == LaunchBallGameConst.enemy_buff_back:
					var_54_4 = var_54_4 + 2

			if var_54_4 >= math.random(1, var_54_3[2]):
				table.insert(var_54_0, var_54_1.type)

	if #var_54_0 > 0:
		return var_54_0[math.random(1, #var_54_0)]

	return None

def var_0_0.getEnemyByBuff(arg_55_0, arg_55_1):
	for iter_55_0 = 1, #arg_55_0.enemysList:
		local var_55_0 = arg_55_0.pointsList[iter_55_0]
		local var_55_1 = arg_55_0.enemysList[iter_55_0]

		for iter_55_1 = #var_55_1, 1, -1:
			local var_55_2 = var_55_1[iter_55_1]

			if var_55_2.getBuff() == arg_55_1:
				return var_55_2

	return None

def var_0_0.getOrCreateEnemy(arg_56_0):
	local var_56_0

	if #arg_56_0.enemyPool > 0:
		var_56_0 = table.remove(arg_56_0.enemyPool, 1)
	else
		local var_56_1 = tf(instantiate(arg_56_0._enemyTpl))

		setParent(var_56_1, arg_56_0._enemyContent)

		var_56_0 = var_0_16(var_56_1)

	return var_56_0

def var_0_0.sortEnemys(arg_57_0, arg_57_1):
	table.sort(arg_57_1, function(arg_58_0, arg_58_1)
		return arg_58_0.getDistance() < arg_58_1.getDistance())

	for iter_57_0 = 1, #arg_57_1:
		arg_57_1[iter_57_0].setLastLayer(iter_57_0 - 1)

def var_0_0.returnEnemy(arg_59_0, arg_59_1):
	arg_59_1.setActive(False)
	table.insert(arg_59_0.enemyPool, arg_59_1)

def var_0_0.getEnemyDataByRule(arg_60_0):
	if not arg_60_0.currentEnemyRule:
		arg_60_0.currentEnemyRule = arg_60_0.getEnemyRule()

	if #var_0_1 > 0:
		return arg_60_0.getEnemyById(table.remove(var_0_1, 1))

	if arg_60_0.currentEnemyRule:
		local var_60_0

		if arg_60_0.currentEnemyRule.single:
			var_60_0 = arg_60_0.currentEnemyRule.singleId
		else
			var_60_0 = arg_60_0.currentEnemyRule.enemys[math.random(1, #arg_60_0.currentEnemyRule.enemys)]

		arg_60_0.currentEnemyRule.count = arg_60_0.currentEnemyRule.count - 1

		if arg_60_0.currentEnemyRule.count <= 0:
			arg_60_0.currentEnemyRule = None

		return arg_60_0.getEnemyById(var_60_0)

	return None

def var_0_0.getEnemyById(arg_61_0, arg_61_1):
	for iter_61_0 = 1, #arg_61_0.enemyDatas:
		if arg_61_0.enemyDatas[iter_61_0].data.id == arg_61_1:
			return arg_61_0.enemyDatas[iter_61_0]

	print("找不到id = " .. arg_61_1 .. "的怪物")

	return None

def var_0_0.checkEnemyRuleUpdate(arg_62_0):
	local var_62_0 = False

	for iter_62_0 = 1, #arg_62_0.rounds:
		if LaunchBallGameVo.gameStepTime >= arg_62_0.rounds[iter_62_0].time[2]:
			var_62_0 = True

	if var_62_0:
		arg_62_0.createRoundData()

def var_0_0.getEnemysInBounds(arg_63_0, arg_63_1, arg_63_2):
	local var_63_0 = arg_63_0._enemyContent.InverseTransformPoint(arg_63_1)
	local var_63_1 = arg_63_0._enemyContent.InverseTransformPoint(arg_63_2)

	arg_63_0.colliderTestTf.anchoredPosition = var_63_1

	local var_63_2 = {}

	for iter_63_0 = 1, #arg_63_0.enemysList:
		local var_63_3 = arg_63_0.pointsList[iter_63_0]
		local var_63_4 = arg_63_0.enemysList[iter_63_0]

		for iter_63_1 = #var_63_4, 1, -1:
			local var_63_5 = var_63_4[iter_63_1].getTf().anchoredPosition

			if var_63_5.x > var_63_0.x and var_63_5.x < var_63_1.x and var_63_5.y > var_63_0.y and var_63_5.y < var_63_1.y:
				table.insert(var_63_2, var_63_4[iter_63_1])

	return var_63_2

def var_0_0.getEnemyRule(arg_64_0):
	local var_64_0
	local var_64_1 = math.random(0, arg_64_0.maxWeight)
	local var_64_2

	for iter_64_0 = 1, #arg_64_0.rounds:
		if not var_64_2 and var_64_1 <= arg_64_0.rounds[iter_64_0].maxWeight:
			var_64_2 = arg_64_0.rounds[iter_64_0].createId

	if var_64_2:
		if not arg_64_0.enemyRule[var_64_2]:
			print("create id not exit " .. var_64_2)

		local var_64_3 = arg_64_0.enemyRule[var_64_2]
		local var_64_4 = var_64_3.id
		local var_64_5 = var_64_3.enemy_create.count
		local var_64_6 = var_64_3.enemy_create.enemys
		local var_64_7 = var_64_3.enemy_create.single
		local var_64_8

		if var_64_7:
			var_64_8 = var_64_6[math.random(1, #var_64_6)]

		var_64_0 = {
			id = var_64_4,
			count = var_64_5,
			enemys = var_64_6,
			single = var_64_7,
			singleId = var_64_8
		}

	return var_64_0

def var_0_0.createRoundData(arg_65_0):
	local var_65_0 = 0

	arg_65_0.rounds = {}

	local var_65_1 = LaunchBallGameVo.gameStepTime

	for iter_65_0 = 1, #arg_65_0.roundDatas:
		local var_65_2 = arg_65_0.roundDatas[iter_65_0]
		local var_65_3 = var_65_2.weight
		local var_65_4 = var_65_2.time
		local var_65_5 = var_65_2.create_id

		if var_65_1 >= var_65_4[1] and var_65_1 <= var_65_4[2]:
			var_65_0 = var_65_0 + var_65_3

			table.insert(arg_65_0.rounds, {
				time = var_65_4,
				weight = var_65_3,
				maxWeight = var_65_0,
				createId = var_65_5
			})

	arg_65_0.maxWeight = var_65_0

def var_0_0.checkAmulet(arg_66_0, arg_66_1):
	local var_66_0 = arg_66_1.tf.position

	arg_66_0.fireIndex = arg_66_1.fireIndex

	local var_66_1 = arg_66_1.color

	for iter_66_0 = 1, #arg_66_0.enemysList:
		local var_66_2 = arg_66_0.pointsList[iter_66_0]
		local var_66_3 = arg_66_0.enemysList[iter_66_0]

		for iter_66_1 = #var_66_3, 1, -1:
			local var_66_4 = var_66_3[iter_66_1]
			local var_66_5, var_66_6 = var_66_3[iter_66_1].checkWorldInRect(var_66_0)

			if var_66_6 and var_66_6 < var_0_4:
				arg_66_1.overCount = arg_66_1.overCount + 1

			if var_66_5 != 0:
				arg_66_0.amuletOverFlag = False

				if arg_66_1.concentrate:
					if not var_66_3[iter_66_1].getTimeRemove():
						var_66_3[iter_66_1].setTimeRemove()

						if arg_66_0._eventCall:
							local var_66_7 = LaunchBallGameVo.GetScore(1, 1)

							arg_66_0._eventCall(LaunchBallGameScene.SPILT_ENEMY_SCORE, {
								num = var_66_7
							})

						if LaunchBallGameVo.GetBuff(LaunchBallPlayerControl.buff_time_max) and arg_66_0.enemyStopTime and arg_66_0.enemyStopTime > 0:
							LaunchBallGameVo.AddGameResultData(LaunchBallGameVo.result_skill_count, 1)

					return False
				else
					local var_66_8 = var_66_4.getDistance()

					if var_66_5 == 1:
						var_66_8 = var_66_8 + var_0_7
					else
						var_66_8 = var_66_8 - var_0_7

					if arg_66_1.overCount >= 2:
						arg_66_0.amuletOverFlag = True

					local var_66_9 = arg_66_0.getEnemyByColor(arg_66_1.color, True)
					local var_66_10 = arg_66_0.createEnemy(iter_66_0, var_66_9, arg_66_0.pointsList[iter_66_0], arg_66_0.enemysList[iter_66_0], var_66_8)

					var_66_10.setSplitFlag(True)
					var_66_10.playAnimation("Spawn")

					local var_66_11 = arg_66_0.getBackBuff()
					local var_66_12 = arg_66_1[LaunchBallGameConst.amulet_buff_back]

					if var_66_11 or var_66_12:
						arg_66_0.setBackTime(LaunchBallPlayerControl.buff_amulet_back_time, #var_66_3, var_0_9)

					return True

	return False

def var_0_0.checkPositionIn(arg_67_0, arg_67_1):
	for iter_67_0 = 1, #arg_67_0.enemysList:
		local var_67_0 = arg_67_0.pointsList[iter_67_0]
		local var_67_1 = arg_67_0.enemysList[iter_67_0]

		for iter_67_1 = #var_67_1, 1, -1:
			local var_67_2 = var_67_1[iter_67_1]

			if var_67_1[iter_67_1].checkWorldInRect(arg_67_1) != 0:
				return var_67_2

	return False

def var_0_0.checkWorldInEnemy(arg_68_0, arg_68_1):
	for iter_68_0 = 1, #arg_68_0.enemysList:
		local var_68_0 = arg_68_0.pointsList[iter_68_0]
		local var_68_1 = arg_68_0.enemysList[iter_68_0]

		for iter_68_1 = #var_68_1, 1, -1:
			local var_68_2 = var_68_1[iter_68_1]

			if var_68_1[iter_68_1].checkWorldInCircle(arg_68_1):
				return True

	return False

def var_0_0.getBackBuff(arg_69_0):
	local var_69_0 = LaunchBallGameVo.buffs

	for iter_69_0 = 1, #var_69_0:
		if var_69_0[iter_69_0].data.type == LaunchBallPlayerControl.buff_amulet_back:
			return True

	return False

def var_0_0.getEnemyByColor(arg_70_0, arg_70_1, arg_70_2):
	for iter_70_0 = 1, #arg_70_0.enemyDatas:
		if arg_70_0.enemyDatas[iter_70_0].data.color == arg_70_1 and arg_70_0.enemyDatas[iter_70_0].data.player == arg_70_2:
			return arg_70_0.enemyDatas[iter_70_0]

def var_0_0.setBackTime(arg_71_0, arg_71_1, arg_71_2, arg_71_3):
	arg_71_0.backEnemyTime = arg_71_1
	arg_71_0.moveBackIndex = arg_71_2
	arg_71_0.backSpeed = arg_71_3 or var_0_9

def var_0_0.eventCall(arg_72_0, arg_72_1, arg_72_2):
	if arg_72_1 == LaunchBallGameScene.PLAYING_CHANGE:
		-- block empty
	elif arg_72_1 == LaunchBallGameScene.FIRE_AMULET:
		-- block empty
	elif arg_72_1 == LaunchBallGameScene.SPLIT_ALL_ENEMYS:
		arg_72_0.timeRemoveAll = arg_72_2.time, arg_72_2.effect
	elif arg_72_1 == LaunchBallGameScene.STOP_ENEMY_TIME:
		arg_72_0.enemyStopTime = arg_72_2.time

		arg_72_0.stopEnemysAnim(True)
	elif arg_72_1 == LaunchBallGameScene.SLASH_ENEMY:
		local var_72_0 = arg_72_2.bound

def var_0_0.stopEnemysAnim(arg_73_0, arg_73_1):
	for iter_73_0 = 1, #arg_73_0.enemysList:
		local var_73_0 = arg_73_0.pointsList[iter_73_0]
		local var_73_1 = arg_73_0.enemysList[iter_73_0]

		for iter_73_1 = #var_73_1, 1, -1:
			var_73_1[iter_73_1].stopAnim(arg_73_1)

def var_0_0.press(arg_74_0, arg_74_1):
	if arg_74_1 == KeyCode.J:
		-- block empty

def var_0_0.clear(arg_75_0):
	return

return var_0_0
