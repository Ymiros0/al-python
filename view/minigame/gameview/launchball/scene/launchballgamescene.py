local var_0_0 = class("LaunchBallGameScene")
local var_0_1 = 1
local var_0_2 = 2
local var_0_3 = 3
local var_0_4 = 4
local var_0_5 = 1
local var_0_6 = 2
local var_0_7 = 3
local var_0_8 = 4
local var_0_9 = 5
local var_0_10 = 6
local var_0_11 = 7
local var_0_12 = 90
local var_0_13 = {
	[var_0_5] = {
		tpl = "pointer01"
	},
	[var_0_6] = {
		tpl = "pointer02"
	},
	[var_0_7] = {
		tpl = "pointer03"
	},
	[var_0_8] = {
		tpl = "pointer04"
	},
	[var_0_9] = {
		tpl = "pointer05"
	},
	[var_0_10] = {
		tpl = "pointer06"
	},
	[var_0_11] = {
		tpl = "pointer07"
	}
}

var_0_0.PLAYING_CHANGE = "playing change"
var_0_0.FIRE_AMULET = "fire amulet"
var_0_0.ENEMY_FINISH = "enemy finish"
var_0_0.HIT_ENEMY = "hit enemy"
var_0_0.RANDOM_FIRE = "random fire"
var_0_0.CHANGE_AMULET = "change amulet"
var_0_0.CONCENTRATE_TRIGGER = "concentrate trigger"
var_0_0.SLEEP_TIME_TRIGGER = "sleep time trigger"
var_0_0.SPILT_ENEMY_SCORE = "spilt enemy score"
var_0_0.SPLIT_ALL_ENEMYS = "split all enemys"
var_0_0.STOP_ENEMY_TIME = "stop enemy time"
var_0_0.SPLIT_BUFF_ENEMY = "split buff enemy"
var_0_0.SLASH_ENEMY = "slash enemy"
var_0_0.PLAYER_EFFECT = "player effect"

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._tf = arg_1_1
	arg_1_0._event = arg_1_2
	arg_1_0.sceneMask = findTF(arg_1_0._tf, "sceneMask")
	arg_1_0.tplContent = findTF(arg_1_0._tf, "sceneMask/sceneContainer/scene/tpl")
	arg_1_0.contentBack = findTF(arg_1_0._tf, "sceneMask/sceneContainer/scene_background/content")
	arg_1_0.contentMid = findTF(arg_1_0._tf, "sceneMask/sceneContainer/scene/content")
	arg_1_0.contentTop = findTF(arg_1_0._tf, "sceneMask/sceneContainer/scene_front/content")
	arg_1_0.contentEF = findTF(arg_1_0._tf, "sceneMask/sceneContainer/scene/effect_front")
	arg_1_0.playerContent = findTF(arg_1_0.contentTop, "player")
	arg_1_0.amuletContent = findTF(arg_1_0.contentTop, "amulet")
	arg_1_0.amuletsContent = findTF(arg_1_0.contentTop, "amulets")
	arg_1_0.amuletLifeContent = findTF(arg_1_0.contentTop, "amuletLifeContent")
	arg_1_0.enemyContent = findTF(arg_1_0.contentMid, "enemy")
	arg_1_0.lineContent = findTF(arg_1_0.contentMid, "line")
	arg_1_0.joyStick = LaunchBallGameJoyStick.New(findTF(arg_1_0.contentTop, "joyStick"))

	arg_1_0.joyStick.setActiveCallback(function(arg_2_0)
		arg_1_0.joystickActive(arg_2_0))

	local function var_1_0(arg_3_0, arg_3_1)
		arg_1_0.launchBallAmulet.eventCall(arg_3_0, arg_3_1)
		arg_1_0.launchBallPlayer.eventCall(arg_3_0, arg_3_1)
		arg_1_0.launchBallEnemy.eventCall(arg_3_0, arg_3_1)

		if arg_3_0 == LaunchBallGameScene.ENEMY_FINISH:
			arg_1_0._event.emit(LaunchBallGameView.GAME_OVER)
		elif arg_3_0 == LaunchBallGameScene.SPILT_ENEMY_SCORE:
			arg_1_0._event.emit(LaunchBallGameView.ADD_SCORE, arg_3_1)
		elif arg_3_0 == LaunchBallGameScene.SLASH_ENEMY:
			arg_1_0.timeSlashDirect = arg_3_1.direct
			arg_1_0.timeSlash = arg_3_1.time

	local var_1_1 = Clone(LaunchBallGameConst.map_data[LaunchBallGameVo.gameRoundData.map].map)
	local var_1_2 = findTF(arg_1_0.contentBack, "bg")
	local var_1_3 = findTF(arg_1_0.contentTop, "bg")

	for iter_1_0 = 0, var_1_2.childCount - 1:
		local var_1_4 = var_1_2.GetChild(iter_1_0)

		setActive(var_1_4, var_1_4.name == var_1_1)

	for iter_1_1 = 0, var_1_3.childCount - 1:
		local var_1_5 = var_1_3.GetChild(iter_1_1)

		setActive(var_1_5, var_1_5.name == var_1_1)

	for iter_1_2 = 0, arg_1_0.lineContent.childCount - 1:
		setActive(arg_1_0.lineContent.GetChild(iter_1_2), False)

	arg_1_0.launchBallAmulet = LaunchBallAmulet.New(arg_1_0.amuletContent, arg_1_0.amuletsContent, arg_1_0.amuletLifeContent, arg_1_0.tplContent, var_1_0)
	arg_1_0.launchBallPlayer = LaunchBallPlayerControl.New(arg_1_0.contentTop, arg_1_0.playerContent, arg_1_0.tplContent, var_1_0)
	arg_1_0.launchBallEnemy = LaunchBallEnemy.New(arg_1_0.enemyContent, arg_1_0.lineContent, arg_1_0.tplContent, var_1_0)

	if not arg_1_0.pointerContent:
		arg_1_0.pointerContent = findTF(arg_1_0.contentTop, "pointer")

	if not arg_1_0.pointerCollider:
		arg_1_0.pointerCollider = findTF(arg_1_0.contentTop, "collider")

		setActive(arg_1_0.pointerCollider, False)

local var_0_14 = 50
local var_0_15 = 500
local var_0_16 = var_0_15 / 50

def var_0_0.start(arg_4_0):
	arg_4_0.prepareScene()
	arg_4_0.launchBallAmulet.start()
	arg_4_0.launchBallPlayer.start()
	arg_4_0.launchBallEnemy.start()

	arg_4_0.pointerRotation = Vector3(0, 0, 0)
	arg_4_0.pointerPosition = Vector2(0, 0)

	for iter_4_0 = 0, arg_4_0.pointerContent.childCount - 1:
		local var_4_0 = arg_4_0.pointerContent.GetChild(iter_4_0)

		setActive(var_4_0, False)

	arg_4_0.timeSlash = None

def var_0_0.step(arg_5_0):
	arg_5_0.joyStick.step()

	LaunchBallGameVo.joyStickData = arg_5_0.joyStick.getValue()

	arg_5_0.launchBallAmulet.step()
	arg_5_0.launchBallPlayer.step()
	arg_5_0.launchBallEnemy.step()

	local var_5_0 = arg_5_0.launchBallAmulet.getAngle()

	if var_5_0 < 0 and arg_5_0.lastContent != arg_5_0.amuletContent:
		arg_5_0.amuletContent.SetAsLastSibling()
		arg_5_0.amuletsContent.SetAsFirstSibling()

		arg_5_0.lastContent = arg_5_0.amuletContent
	elif var_5_0 > 0 and arg_5_0.lastContent != arg_5_0.playerContent:
		arg_5_0.amuletContent.SetAsFirstSibling()
		arg_5_0.amuletsContent.SetAsLastSibling()

		arg_5_0.lastContent = arg_5_0.playerContent

	if arg_5_0.timeSlash and arg_5_0.timeSlash > 0:
		arg_5_0.timeSlash = arg_5_0.timeSlash - LaunchBallGameVo.deltaTime

		if arg_5_0.timeSlash <= 0:
			arg_5_0.timeSlash = None

			local var_5_1 = GetComponent(findTF(arg_5_0.contentTop, "effect/SlashBound/ad/" .. arg_5_0.timeSlashDirect), typeof(BoxCollider2D))
			local var_5_2 = var_5_1.bounds.min
			local var_5_3 = var_5_1.bounds.max
			local var_5_4 = arg_5_0.launchBallEnemy.getEnemysInBounds(var_5_2, var_5_3)

			for iter_5_0 = 1, #var_5_4:
				var_5_4[iter_5_0].hit()

				local var_5_5 = LaunchBallGameVo.GetScore(1, 1)

				arg_5_0._event.emit(LaunchBallGameView.ADD_SCORE, {
					num = var_5_5
				})

			LaunchBallGameVo.AddGameResultData(LaunchBallGameVo.result_skill_count, #var_5_4)

	local var_5_6 = arg_5_0.launchBallAmulet.getFireAmulet()

	for iter_5_1 = #var_5_6, 1, -1:
		local var_5_7 = var_5_6[iter_5_1]
		local var_5_8 = var_5_6[iter_5_1].tf.position

		if not var_5_7.removeFlag and arg_5_0.launchBallEnemy.checkAmulet(var_5_6[iter_5_1]):
			var_5_7.removeFlag = True

	local var_5_9 = arg_5_0.launchBallAmulet.getButterfly()

	for iter_5_2 = #var_5_9, 1, -1:
		local var_5_10 = var_5_9[iter_5_2]
		local var_5_11 = var_5_10.tf

		if not var_5_10.removeFlag and not var_5_10.removeTime:
			local var_5_12 = var_5_11.position
			local var_5_13 = arg_5_0.launchBallEnemy.checkPositionIn(var_5_12)

			if var_5_13:
				var_5_10.removeTime = 0.2
				var_5_10.speed.x = 0
				var_5_10.speed.y = 0

				var_5_10.anim.Play("Hit")
				var_5_13.setTimeRemove()

				local var_5_14 = LaunchBallGameVo.GetScore(1, 1)

				arg_5_0._event.emit(LaunchBallGameView.ADD_SCORE, {
					num = var_5_14
				})
				LaunchBallGameVo.AddGameResultData(LaunchBallGameVo.result_pass_skill_count, 1)

	if LaunchBallGameVo.joyStickData.active and LaunchBallGameVo.amulet:
		arg_5_0.pointerTime = arg_5_0.pointerTime + LaunchBallGameVo.deltaTime

		if not arg_5_0.pointerColor:
			local var_5_15 = LaunchBallGameVo.amulet.color
			local var_5_16 = var_0_13[LaunchBallGameVo.amulet.color].tpl

			for iter_5_3 = 0, arg_5_0.pointerContent.childCount - 1:
				local var_5_17 = arg_5_0.pointerContent.GetChild(iter_5_3)

				if var_5_17.name == var_5_16:
					arg_5_0.anglePointer = var_5_17

				setActive(var_5_17, False)

		if arg_5_0.pointerTime > 0.3 and LaunchBallGameVo.joyStickData.active:
			local var_5_18 = LaunchBallGameVo.joyStickData.angle
			local var_5_19 = LaunchBallGameVo.joyStickData.rad

			if var_5_18 and var_5_19:
				arg_5_0.pointerRotation.z = var_5_18 + var_0_12
				arg_5_0.anglePointer.localEulerAngles = arg_5_0.pointerRotation

				setActive(arg_5_0.anglePointer, True)

				local var_5_20 = 0

				for iter_5_4 = 1, var_0_16:
					var_5_20 = iter_5_4 * var_0_14
					arg_5_0.pointerPosition.x = math.cos(var_5_19) * var_5_20
					arg_5_0.pointerPosition.y = math.sin(var_5_19) * var_5_20

					local var_5_21 = arg_5_0.pointerContent.TransformPoint(arg_5_0.pointerPosition)

					if arg_5_0.launchBallEnemy.checkWorldInEnemy(var_5_21):
						break

				for iter_5_5 = 1, 4:
					arg_5_0.pointerPosition.x = 0
					arg_5_0.pointerPosition.y = (5 - iter_5_5) / 4 * var_5_20 * -1
					findTF(arg_5_0.anglePointer, "ad/" .. iter_5_5).anchoredPosition = arg_5_0.pointerPosition
	else
		arg_5_0.pointerTime = 0
		arg_5_0.pointerColor = None

		if arg_5_0.anglePointer:
			setActive(arg_5_0.anglePointer, False)

def var_0_0.clear(arg_6_0):
	arg_6_0.launchBallAmulet.clear()
	arg_6_0.launchBallPlayer.clear()
	arg_6_0.launchBallEnemy.clear()

def var_0_0.stop(arg_7_0):
	return

def var_0_0.resume(arg_8_0):
	return

def var_0_0.dispose(arg_9_0):
	return

def var_0_0.prepareScene(arg_10_0):
	arg_10_0.showContainer(True)

def var_0_0.showContainer(arg_11_0, arg_11_1):
	setActive(arg_11_0.sceneMask, arg_11_1)

def var_0_0.useSkill(arg_12_0):
	arg_12_0.launchBallPlayer.useSkill()

def var_0_0.press(arg_13_0, arg_13_1):
	arg_13_0.launchBallEnemy.press(arg_13_1)

def var_0_0.joystickActive(arg_14_0, arg_14_1):
	arg_14_0.launchBallPlayer.joystickActive(arg_14_1)

return var_0_0
