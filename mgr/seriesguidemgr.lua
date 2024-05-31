pg = pg or {}
pg.SeriesGuideMgr = singletonClass("SeriesGuideMgr")

local var_0_0 = pg.SeriesGuideMgr
local var_0_1 = false
local var_0_2 = 29

function log(...)
	if var_0_1 then
		originalPrint(...)
	end
end

local var_0_3 = {
	IDLE = 1,
	BUSY = 2
}

var_0_0.CODES = {
	CONDITION = 4,
	MAINUI = 2,
	GUIDER = 1
}

function var_0_0.isRunning(arg_2_0)
	return arg_2_0.state == var_0_3.BUSY
end

function var_0_0.isNotFinish(arg_3_0)
	local var_3_0 = getProxy(PlayerProxy)

	if var_3_0 then
		return var_3_0:getRawData().guideIndex < 28
	end
end

function var_0_0.loadGuide(arg_4_0, arg_4_1)
	return require("GameCfg.guide.newguide." .. arg_4_1)
end

function var_0_0.getStepConfig(arg_5_0, arg_5_1)
	return arg_5_0.guideCfgs[arg_5_1]
end

function var_0_0.Init(arg_6_0, arg_6_1)
	arg_6_0.state = var_0_3.IDLE
	arg_6_0.guideCfgs = arg_6_0:loadGuide("SG001")
	arg_6_0.guideMgr = pg.NewGuideMgr.GetInstance()
	arg_6_0.protocols = {}
	arg_6_0.onReceiceProtocol = nil

	arg_6_1()
end

function var_0_0.dispatch(arg_7_0, arg_7_1)
	if arg_7_0:canPlay(arg_7_1) then
		arg_7_0.guideMgr:PlayNothing()
	end
end

function var_0_0.start(arg_8_0, arg_8_1)
	if arg_8_0:canPlay(arg_8_1) then
		arg_8_0.state = var_0_3.BUSY

		arg_8_0.guideMgr:StopNothing()

		arg_8_0.stepConfig = arg_8_0:getStepConfig(arg_8_0.currIndex)

		local function var_8_0(arg_9_0)
			arg_8_0.state = var_0_3.IDLE
			arg_8_0.protocols = {}

			if not arg_8_0.stepConfig.interrupt then
				arg_8_0:doNextStep(arg_8_0.currIndex, arg_9_0)
			end
		end

		arg_8_0:doGuideStep(arg_8_1, function(arg_10_0, arg_10_1)
			if arg_8_0.stepConfig.end_segment and arg_10_1 then
				arg_8_0.guideMgr:Play(arg_8_0.stepConfig.end_segment, arg_8_1.code, function()
					var_8_0(arg_10_0)
				end)
			else
				var_8_0(arg_10_0)
			end
		end)
	end
end

function var_0_0.doGuideStep(arg_12_0, arg_12_1, arg_12_2)
	if arg_12_0.stepConfig.condition then
		local var_12_0, var_12_1 = arg_12_0:checkCondition(arg_12_1)
		local var_12_2 = var_12_1 > arg_12_0.currIndex

		arg_12_0:updateIndex(var_12_1, function()
			arg_12_2({
				var_12_0
			}, var_12_2)
		end)
	else
		local var_12_3 = arg_12_0.stepConfig.segment[arg_12_0:getSegmentIndex()]
		local var_12_4 = var_12_3[1]
		local var_12_5 = var_12_3[2]

		assert(var_12_5, "protocol can not be nil")

		local var_12_6 = {
			function(arg_14_0)
				arg_12_0.guideMgr:Play(var_12_4, arg_12_1.code, arg_14_0, function()
					arg_12_0:updateIndex(var_0_2)
				end)
				arg_12_0.guideMgr:PlayNothing()
			end,
			function(arg_16_0)
				if _.any(arg_12_0.protocols, function(arg_17_0)
					return arg_17_0.protocol == var_12_5
				end) then
					arg_16_0()

					return
				end

				function arg_12_0.onReceiceProtocol(arg_18_0)
					if arg_18_0 == var_12_5 then
						arg_12_0.onReceiceProtocol = nil

						arg_16_0()
					end
				end
			end,
			function(arg_19_0)
				arg_12_0.guideMgr:StopNothing()
				arg_12_0:increaseIndex(arg_19_0)
			end
		}

		seriesAsync(var_12_6, function()
			arg_12_2({
				var_0_0.CODES.GUIDER
			}, true)
		end)
	end
end

function var_0_0.getSegmentIndex(arg_21_0)
	local var_21_0 = 1

	if arg_21_0.stepConfig.getSegment then
		var_21_0 = arg_21_0.stepConfig.getSegment()
	end

	return var_21_0
end

local var_0_4 = 1
local var_0_5 = 2

function var_0_0.checkCondition(arg_22_0, arg_22_1)
	local var_22_0 = arg_22_0.stepConfig
	local var_22_1
	local var_22_2
	local var_22_3 = var_22_0.condition.arg

	if var_22_3[1] == var_0_4 then
		local var_22_4 = {
			protocol = var_22_3[2],
			func = var_22_0.condition.func
		}

		var_22_2, var_22_1 = arg_22_0:checkPtotocol(var_22_4, arg_22_1)
	elseif var_22_3[1] == var_0_5 then
		local var_22_5 = getProxy(PlayerProxy):getRawData()
		local var_22_6 = getProxy(BayProxy):getShipById(var_22_5.character)

		var_22_2, var_22_1 = var_22_0.condition.func(var_22_6)
		arg_22_0.stepConfig.condition = nil
	end

	assert(var_22_1, "index can not be nil")

	return var_22_2, var_22_1
end

function var_0_0.checkPtotocol(arg_23_0, arg_23_1, arg_23_2)
	local var_23_0 = arg_23_1.protocol
	local var_23_1 = _.select(arg_23_0.protocols, function(arg_24_0)
		return arg_24_0.protocol == var_23_0
	end)[1] or {}

	return arg_23_1.func(arg_23_2.view, var_23_1.args)
end

function var_0_0.increaseIndex(arg_25_0, arg_25_1)
	local var_25_0 = arg_25_0.currIndex + 1

	arg_25_0:updateIndex(var_25_0, arg_25_1)
end

function var_0_0.updateIndex(arg_26_0, arg_26_1, arg_26_2)
	pg.m02:sendNotification(GAME.UPDATE_GUIDE_INDEX, {
		index = arg_26_1,
		callback = arg_26_2
	})
end

function var_0_0.doNextStep(arg_27_0, arg_27_1, arg_27_2)
	arg_27_0.stepConfig = nil

	if arg_27_0:isEnd() then
		return
	end

	local var_27_0 = arg_27_0.guideCfgs[arg_27_1]
	local var_27_1 = {
		view = var_27_0.view[#var_27_0.view],
		code = arg_27_2
	}

	if arg_27_0:canPlay(var_27_1) then
		arg_27_0:start(var_27_1)
	end
end

function var_0_0.isEnd(arg_28_0)
	return arg_28_0.currIndex > #arg_28_0.guideCfgs or not ENABLE_GUIDE
end

function var_0_0.receiceProtocol(arg_29_0, arg_29_1, arg_29_2, arg_29_3)
	table.insert(arg_29_0.protocols, {
		protocol = arg_29_1,
		args = arg_29_2,
		data = arg_29_3
	})

	if arg_29_0.onReceiceProtocol then
		arg_29_0.onReceiceProtocol(arg_29_1)
	end
end

function var_0_0.canPlay(arg_30_0, arg_30_1)
	if arg_30_0.state ~= var_0_3.IDLE then
		log("guider is busy")

		return false
	end

	if not ENABLE_GUIDE then
		log("ENABLE is false")

		return false
	end

	if not arg_30_0.guideMgr then
		log("guideMgr is nil")

		return false
	end

	if not arg_30_0.plevel then
		log("player is nil")

		return false
	end

	if arg_30_0:isEnd() then
		log("guider is end")

		return false
	end

	local var_30_0 = arg_30_0:getStepConfig(arg_30_0.currIndex)

	if not table.contains(var_30_0.view, arg_30_1.view) then
		log("view is erro", arg_30_0.currIndex, arg_30_1.view, var_30_0.view[1], var_30_0.view[2])

		return false
	end

	return true
end

function var_0_0.setPlayer(arg_31_0, arg_31_1)
	arg_31_0.plevel = arg_31_1.level
	arg_31_0.pguideIndex = arg_31_1.guideIndex
	arg_31_0.currIndex = arg_31_1.guideIndex

	arg_31_0:compatibleOldPlayer()
end

function var_0_0.dispose(arg_32_0)
	arg_32_0.plevel = nil
	arg_32_0.guideIndex = nil
	arg_32_0.protocols = {}
	arg_32_0.state = var_0_3.IDLE
end

function var_0_0.compatibleOldPlayer(arg_33_0)
	if not arg_33_0.plevel then
		return
	end

	local function var_33_0()
		local var_34_0 = getProxy(PlayerProxy):getRawData()

		var_34_0.guideIndex = var_0_2

		arg_33_0:setPlayer(var_34_0)
		arg_33_0:updateIndex(var_34_0.guideIndex)
	end

	if arg_33_0.plevel >= 5 and arg_33_0.pguideIndex < var_0_2 then
		var_33_0()

		return
	end

	if arg_33_0.pguideIndex ~= var_0_2 then
		pg.SystemGuideMgr.GetInstance():FixGuide(function()
			if arg_33_0.pguideIndex > 1 and arg_33_0.pguideIndex < 101 then
				var_33_0()
			end
		end)
	end
end
