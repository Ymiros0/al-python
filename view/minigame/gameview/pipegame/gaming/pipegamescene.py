local var_0_0 = class("PipeGameScene")
local var_0_1 = 1
local var_0_2 = 2
local var_0_3 = 3
local var_0_4 = 4
local var_0_5

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_5 = PipeGameVo
	arg_1_0._tf = arg_1_1
	arg_1_0._event = arg_1_2
	arg_1_0.sceneMask = findTF(arg_1_0._tf, "sceneMask")
	arg_1_0.sceneContent = findTF(arg_1_0._tf, "sceneMask/sceneContainer")
	arg_1_0._moveAnimator = GetComponent(arg_1_0.sceneContent, typeof(Animator))
	arg_1_0._bgRight = findTF(arg_1_0.sceneContent, "scene_background/content/bgRight")
	arg_1_0._bgRightAnimator = GetComponent(findTF(arg_1_0._bgRight, "img"), typeof(Animator))

	local function var_1_0(arg_2_0, arg_2_1)
		if arg_2_0 == PipeGameEvent.REMOVE_RECT_TOP:
			arg_1_0.rectCtrl.removeTopRectData()
		elif arg_2_0 == PipeGameEvent.PALY_ANIMATION_COMPLETE:
			var_0_5.scoreNum = arg_1_0.mapCtrl.getSuccessCount()

			arg_1_0.playMove(function()
				arg_1_0._event.emit(PipeGameEvent.GAME_OVER))
		elif arg_2_0 == PipeGameEvent.STOP_RECT_DRAG:
			arg_1_0.rectCtrl.stopTopDrag()
		elif arg_2_0 == PipeGameEvent.SET_TOP_RECT:
			local var_2_0 = arg_1_0.rectCtrl.getTopData()

			arg_1_0.mapCtrl.setClickTempItem(var_2_0)
		elif arg_2_0 == PipeGameEvent.START_SETTLEMENT:
			var_0_5.startSettlement = True

	arg_1_0.mapCtrl = PipeMapControl.New(findTF(arg_1_0.sceneContent, "scene/content/map"), var_1_0)
	arg_1_0.rectCtrl = PipeRectControll.New(findTF(arg_1_0.sceneContent, "scene/content/rect"), findTF(arg_1_0.sceneContent, "scene/content/dragPos"), var_1_0)
	arg_1_0.passCtrl = PiPePassTest.New(findTF(arg_1_0.sceneContent, "scene/content/passTest"), function(arg_4_0, arg_4_1, arg_4_2, arg_4_3)
		if arg_1_0.mapCtrl:
			local var_4_0 = arg_1_0.mapCtrl.checkItemSuccess(arg_4_0, arg_4_1, arg_4_2, arg_4_3)

			arg_1_0.passCtrl.setPassDesc(var_4_0))

	arg_1_0.passCtrl.setVisible(False)
	arg_1_0.showContainer(False)

def var_0_0.start(arg_5_0):
	arg_5_0.showContainer(True)
	arg_5_0.resetScene()
	arg_5_0.mapCtrl.start()
	arg_5_0.rectCtrl.start()

def var_0_0.step(arg_6_0, arg_6_1):
	arg_6_0.mapCtrl.step()
	arg_6_0.rectCtrl.step()

def var_0_0.clear(arg_7_0):
	arg_7_0.mapCtrl.clear()
	arg_7_0.rectCtrl.clear()

def var_0_0.stop(arg_8_0):
	arg_8_0.mapCtrl.stop()
	arg_8_0.rectCtrl.stop()

def var_0_0.resume(arg_9_0):
	arg_9_0.mapCtrl.resume()
	arg_9_0.rectCtrl.resume()

def var_0_0.setGameOver(arg_10_0):
	arg_10_0.mapCtrl.startOverAniamtion()

def var_0_0.dispose(arg_11_0):
	arg_11_0.mapCtrl.dispose()
	arg_11_0.rectCtrl.dispose()
	arg_11_0.passCtrl.dispose()

	if LeanTween.isTweening(go(arg_11_0.sceneContent)):
		LeanTween.cancel(go(arg_11_0.sceneContent))

def var_0_0.resetScene(arg_12_0):
	setActive(arg_12_0._bgRight, False)
	arg_12_0._moveAnimator.SetTrigger("reset")

def var_0_0.playMove(arg_13_0, arg_13_1):
	local var_13_0 = var_0_5.GetResultLevel()

	setActive(arg_13_0._bgRight, True)
	arg_13_0._bgRightAnimator.SetTrigger(tostring(var_13_0))
	arg_13_0._moveAnimator.SetTrigger("move")
	LeanTween.delayedCall(go(arg_13_0.sceneContent), 5, System.Action(function()
		if arg_13_1:
			arg_13_1()))

def var_0_0.showContainer(arg_15_0, arg_15_1):
	setActive(arg_15_0.sceneMask, arg_15_1)

def var_0_0.press(arg_16_0, arg_16_1, arg_16_2):
	return

def var_0_0.joystickActive(arg_17_0, arg_17_1):
	return

return var_0_0
