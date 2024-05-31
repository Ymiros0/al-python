local var_0_0 = class("PipeGameScene")
local var_0_1 = 1
local var_0_2 = 2
local var_0_3 = 3
local var_0_4 = 4
local var_0_5

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_5 = PipeGameVo
	arg_1_0._tf = arg_1_1
	arg_1_0._event = arg_1_2
	arg_1_0.sceneMask = findTF(arg_1_0._tf, "sceneMask")
	arg_1_0.sceneContent = findTF(arg_1_0._tf, "sceneMask/sceneContainer")
	arg_1_0._moveAnimator = GetComponent(arg_1_0.sceneContent, typeof(Animator))
	arg_1_0._bgRight = findTF(arg_1_0.sceneContent, "scene_background/content/bgRight")
	arg_1_0._bgRightAnimator = GetComponent(findTF(arg_1_0._bgRight, "img"), typeof(Animator))

	local function var_1_0(arg_2_0, arg_2_1)
		if arg_2_0 == PipeGameEvent.REMOVE_RECT_TOP then
			arg_1_0.rectCtrl:removeTopRectData()
		elseif arg_2_0 == PipeGameEvent.PALY_ANIMATION_COMPLETE then
			var_0_5.scoreNum = arg_1_0.mapCtrl:getSuccessCount()

			arg_1_0:playMove(function()
				arg_1_0._event:emit(PipeGameEvent.GAME_OVER)
			end)
		elseif arg_2_0 == PipeGameEvent.STOP_RECT_DRAG then
			arg_1_0.rectCtrl:stopTopDrag()
		elseif arg_2_0 == PipeGameEvent.SET_TOP_RECT then
			local var_2_0 = arg_1_0.rectCtrl:getTopData()

			arg_1_0.mapCtrl:setClickTempItem(var_2_0)
		elseif arg_2_0 == PipeGameEvent.START_SETTLEMENT then
			var_0_5.startSettlement = true
		end
	end

	arg_1_0.mapCtrl = PipeMapControl.New(findTF(arg_1_0.sceneContent, "scene/content/map"), var_1_0)
	arg_1_0.rectCtrl = PipeRectControll.New(findTF(arg_1_0.sceneContent, "scene/content/rect"), findTF(arg_1_0.sceneContent, "scene/content/dragPos"), var_1_0)
	arg_1_0.passCtrl = PiPePassTest.New(findTF(arg_1_0.sceneContent, "scene/content/passTest"), function(arg_4_0, arg_4_1, arg_4_2, arg_4_3)
		if arg_1_0.mapCtrl then
			local var_4_0 = arg_1_0.mapCtrl:checkItemSuccess(arg_4_0, arg_4_1, arg_4_2, arg_4_3)

			arg_1_0.passCtrl:setPassDesc(var_4_0)
		end
	end)

	arg_1_0.passCtrl:setVisible(false)
	arg_1_0:showContainer(false)
end

function var_0_0.start(arg_5_0)
	arg_5_0:showContainer(true)
	arg_5_0:resetScene()
	arg_5_0.mapCtrl:start()
	arg_5_0.rectCtrl:start()
end

function var_0_0.step(arg_6_0, arg_6_1)
	arg_6_0.mapCtrl:step()
	arg_6_0.rectCtrl:step()
end

function var_0_0.clear(arg_7_0)
	arg_7_0.mapCtrl:clear()
	arg_7_0.rectCtrl:clear()
end

function var_0_0.stop(arg_8_0)
	arg_8_0.mapCtrl:stop()
	arg_8_0.rectCtrl:stop()
end

function var_0_0.resume(arg_9_0)
	arg_9_0.mapCtrl:resume()
	arg_9_0.rectCtrl:resume()
end

function var_0_0.setGameOver(arg_10_0)
	arg_10_0.mapCtrl:startOverAniamtion()
end

function var_0_0.dispose(arg_11_0)
	arg_11_0.mapCtrl:dispose()
	arg_11_0.rectCtrl:dispose()
	arg_11_0.passCtrl:dispose()

	if LeanTween.isTweening(go(arg_11_0.sceneContent)) then
		LeanTween.cancel(go(arg_11_0.sceneContent))
	end
end

function var_0_0.resetScene(arg_12_0)
	setActive(arg_12_0._bgRight, false)
	arg_12_0._moveAnimator:SetTrigger("reset")
end

function var_0_0.playMove(arg_13_0, arg_13_1)
	local var_13_0 = var_0_5.GetResultLevel()

	setActive(arg_13_0._bgRight, true)
	arg_13_0._bgRightAnimator:SetTrigger(tostring(var_13_0))
	arg_13_0._moveAnimator:SetTrigger("move")
	LeanTween.delayedCall(go(arg_13_0.sceneContent), 5, System.Action(function()
		if arg_13_1 then
			arg_13_1()
		end
	end))
end

function var_0_0.showContainer(arg_15_0, arg_15_1)
	setActive(arg_15_0.sceneMask, arg_15_1)
end

function var_0_0.press(arg_16_0, arg_16_1, arg_16_2)
	return
end

function var_0_0.joystickActive(arg_17_0, arg_17_1)
	return
end

return var_0_0
