pg = pg or {}
pg.GuideMgr = singletonClass("GuideMgr")

local var_0_0 = pg.GuideMgr

var_0_0.ENABLE_GUIDE = true
var_0_0.MANAGER_STATE = {
	IDLE = 1,
	BUSY = 2,
	LOADING = 0,
	BREAK = 4,
	STOP = 3
}

local var_0_1 = 1
local var_0_2 = 2
local var_0_3 = 3
local var_0_4 = 4
local var_0_5 = 5
local var_0_6 = {
	MODE1 = 1,
	MODE2 = 2
}

function var_0_0.Init(arg_1_0, arg_1_1)
	print("initializing guide manager...")

	arg_1_0.managerState = var_0_0.MANAGER_STATE.LOADING
	arg_1_0.sceneStore = {}
	arg_1_0.uisetGos = {}

	PoolMgr.GetInstance():GetUI("GuideUI", true, function(arg_2_0)
		arg_1_0._go = arg_2_0
		arg_1_0._tf = arg_1_0._go.transform

		arg_1_0._go:SetActive(false)

		arg_1_0.UIOverlay = tf(GameObject.Find("Overlay/UIOverlay"))

		arg_1_0._go.transform:SetParent(arg_1_0.UIOverlay, false)

		arg_1_0.guiderTF = findTF(arg_1_0._go, "Guider")
		arg_1_0.styleTF1 = findTF(arg_1_0.guiderTF, "mode1")
		arg_1_0.styleTF2 = findTF(arg_1_0.guiderTF, "mode2")
		arg_1_0.initChatBgH = arg_1_0.styleTF2.sizeDelta.y

		SetActive(arg_1_0.guiderTF, false)

		arg_1_0._bg = findTF(arg_1_0._go, "BG")
		arg_1_0.bgAlpha = arg_1_0._bg:GetComponent(typeof(CanvasGroup))
		arg_1_0.bgAlpha.alpha = 0.2
		arg_1_0._closeBtn = arg_1_0._bg:Find("close_btn")
		arg_1_0.uiLongPress = GetOrAddComponent(arg_1_0._closeBtn, typeof(UILongPressTrigger))
		arg_1_0.uiLongPress.longPressThreshold = 10
		arg_1_0.fingerTF = findTF(arg_1_0._go, "finger")

		SetActive(arg_1_0.fingerTF, false)

		arg_1_0._signRes = findTF(arg_1_0._go, "signRes")
		arg_1_0.signPool = {}
		arg_1_0.curSignList = {}
		arg_1_0.fingerSprites = {}

		eachChild(findTF(arg_1_0._go, "resources"), function(arg_3_0)
			local var_3_0 = arg_3_0:GetComponent(typeof(Image)).sprite

			table.insert(arg_1_0.fingerSprites, var_3_0)
		end)

		arg_1_0.sceneFunc = nil
		arg_1_0.inited = true
		arg_1_0.finder = arg_1_0:Finder()
		arg_1_0.managerState = var_0_0.MANAGER_STATE.IDLE
		arg_1_0.chars = {
			arg_1_0.styleTF1:Find("char"):GetComponent(typeof(Image)).sprite,
			GetSpriteFromAtlas("ui/guide_atlas", "guide1"),
			GetSpriteFromAtlas("ui/share/guider_atlas", "amazon")
		}
		arg_1_0.material = arg_1_0._tf:Find("resources/material"):GetComponent(typeof(Image)).material

		arg_1_1()
	end)
end

function var_0_0.isRuning(arg_4_0)
	return arg_4_0.managerState == var_0_0.MANAGER_STATE.BUSY
end

function var_0_0.transformPos(arg_5_0, arg_5_1)
	return tf(arg_5_0._go):InverseTransformPoint(arg_5_1)
end

function var_0_0.canPlay(arg_6_0)
	if pg.MsgboxMgr.GetInstance()._go.activeSelf then
		return false, 1
	end

	if pg.NewStoryMgr.GetInstance():IsRunning() then
		return false, 2
	end

	if arg_6_0.managerState == var_0_0.MANAGER_STATE.BUSY then
		return false, 3
	end

	return true
end

function var_0_0.onSceneAnimDone(arg_7_0, arg_7_1)
	if not arg_7_0.inited then
		return
	end

	if not table.contains(arg_7_0.sceneStore, arg_7_1.view) then
		table.insert(arg_7_0.sceneStore, arg_7_1.view)
	end

	if arg_7_0.sceneFunc then
		arg_7_0.sceneFunc(arg_7_1.view)
	end
end

function var_0_0.onSceneExit(arg_8_0, arg_8_1)
	if not arg_8_0.inited then
		return
	end

	if table.contains(arg_8_0.sceneStore, arg_8_1.view) then
		table.removebyvalue(arg_8_0.sceneStore, arg_8_1.view)
	end
end

function var_0_0.checkModuleOpen(arg_9_0, arg_9_1)
	return table.contains(arg_9_0.sceneStore, arg_9_1)
end

function var_0_0.isPlayed(arg_10_0, arg_10_1)
	return pg.NewStoryMgr.GetInstance():IsPlayed(arg_10_1)
end

function var_0_0.play(arg_11_0, arg_11_1, arg_11_2, arg_11_3, arg_11_4)
	if not var_0_0.ENABLE_GUIDE then
		return
	end

	local var_11_0, var_11_1 = arg_11_0:canPlay()

	originalPrint("play guide >>", arg_11_1, var_11_0)

	arg_11_0.erroCallback = arg_11_4

	if var_11_0 then
		arg_11_0.currentGuide = require("GameCfg.guide.newguide.segments." .. arg_11_1)

		arg_11_0:addDelegateInfo()

		local var_11_2 = Clone(arg_11_0.currentGuide.events)

		if arg_11_2 then
			arg_11_0.curEvents = _.select(var_11_2, function(arg_12_0)
				if not arg_12_0.code then
					return true
				elseif type(arg_12_0.code) == "table" then
					return _.any(arg_11_2, function(arg_13_0)
						return table.contains(arg_12_0.code, arg_13_0)
					end)
				else
					return table.contains(arg_11_2, arg_12_0.code)
				end
			end)
		else
			arg_11_0.curEvents = var_11_2
		end

		arg_11_0:prepareGuider(arg_11_3)

		local var_11_3 = {}

		for iter_11_0, iter_11_1 in ipairs(arg_11_0.curEvents or {}) do
			table.insert(var_11_3, function(arg_14_0)
				local function var_14_0()
					if arg_11_0.managerState ~= var_0_0.MANAGER_STATE.IDLE then
						arg_11_0.scenes = {}

						arg_14_0()
					else
						arg_11_0.erroCallback()

						arg_11_0.erroCallback = nil
					end
				end

				arg_11_0:doCurrEvent(iter_11_1, var_14_0)
			end)
		end

		arg_11_0.managerState = var_0_0.MANAGER_STATE.BUSY

		seriesAsync(var_11_3, function()
			arg_11_0:endGuider(arg_11_3)
		end)
	elseif arg_11_3 then
		arg_11_3()
	end
end

function var_0_0.prepareGuider(arg_17_0, arg_17_1)
	pg.m02:sendNotification(GAME.START_GUIDE)
	arg_17_0._go.transform:SetAsLastSibling()
	arg_17_0._go:SetActive(true)
	SetActive(arg_17_0.fingerTF, false)

	arg_17_0.bgAlpha.alpha = 0.2

	arg_17_0.uiLongPress.onLongPressed:AddListener(function()
		arg_17_0:endGuider(arg_17_1)
	end)
end

function var_0_0.doCurrEvent(arg_19_0, arg_19_1, arg_19_2)
	local function var_19_0(arg_20_0)
		if arg_19_1.waitScene and arg_19_1.waitScene ~= "" and not table.contains(arg_19_0.scenes, arg_19_1.waitScene) then
			function arg_19_0.sceneFunc(arg_21_0)
				if arg_19_1.waitScene == arg_21_0 or table.contains(arg_19_0.sceneStore, arg_19_1.waitScene) then
					arg_19_0.sceneFunc = nil

					arg_20_0()
				end
			end

			arg_19_0.sceneFunc()
		else
			arg_20_0()
		end
	end

	local function var_19_1()
		if arg_19_1.hideui then
			arg_19_0:hideUI(arg_19_1, arg_19_2)
		elseif arg_19_1.stories then
			arg_19_0:playStories(arg_19_1, arg_19_2)
		elseif arg_19_1.notifies then
			arg_19_0:sendNotifies(arg_19_1, arg_19_2)
		elseif arg_19_1.showSign then
			arg_19_0:showSign(arg_19_1, arg_19_2)
		elseif arg_19_1.doFunc then
			arg_19_1.doFunc()
			arg_19_2()
		elseif arg_19_1.doNothing then
			arg_19_2()
		else
			arg_19_0:findUI(arg_19_1, arg_19_2)
		end
	end

	if arg_19_1.delay ~= nil then
		arg_19_0.delayTimer = Timer.New(function()
			var_19_0(var_19_1)
		end, arg_19_1.delay, 1)

		arg_19_0.delayTimer:Start()
	else
		var_19_0(var_19_1)
	end
end

function var_0_0.showSign(arg_24_0, arg_24_1, arg_24_2)
	local var_24_0 = arg_24_1.showSign

	;(function()
		local var_25_0 = var_24_0.type
		local var_25_1 = var_24_0.duration
		local var_25_2 = var_24_0.simultaneously
		local var_25_3 = var_24_0.clickUI
		local var_25_4 = var_24_0.clickArea
		local var_25_5 = var_24_0.longPress
		local var_25_6 = var_24_0.signList
		local var_25_7 = {}

		for iter_25_0, iter_25_1 in ipairs(var_25_6) do
			local var_25_8 = iter_25_1.signType
			local var_25_9 = iter_25_1.pos
			local var_25_10 = iter_25_1.cachedIndex
			local var_25_11 = arg_24_0:getSign(var_25_8, iter_25_1)
			local var_25_12 = #arg_24_0.curSignList + 1

			arg_24_0.curSignList[var_25_12] = {
				signType = var_25_8,
				sign = var_25_11
			}

			if type(var_25_9) == "string" then
				if var_25_9 == "useCachePos" then
					var_25_9 = WorldGuider.GetInstance():GetTempGridPos(var_25_10)
				end
			elseif type(var_25_9) == "table" then
				var_25_9 = Vector3.New(var_25_9[1], var_25_9[2], var_25_9[3])
			end

			if var_25_9 then
				setLocalPosition(var_25_11, var_25_9)
			end

			var_25_7[#var_25_7 + 1] = var_25_12
		end

		function recycle_handler()
			for iter_26_0, iter_26_1 in ipairs(var_25_7) do
				local var_26_0 = arg_24_0.curSignList[iter_26_1]

				arg_24_0:recycleSign(var_26_0.signType, var_26_0.sign)

				arg_24_0.curSignList[iter_26_1] = nil
			end

			if not var_25_2 then
				arg_24_0:finishCurrEvent(arg_24_1, arg_24_2)
			end
		end

		local var_25_13 = var_25_7[1]
		local var_25_14 = arg_24_0.curSignList[var_25_13].sign

		if var_25_0 == 2 then
			arg_24_0:updateUIStyle(arg_24_1, false, nil)

			local var_25_15 = findTF(var_25_14, "btn")

			if var_25_3 then
				setActive(var_25_14, false)
				arg_24_0.finder:Search({
					path = var_25_3.path,
					delay = var_25_3.delay,
					pathIndex = var_25_3.pathIndex,
					conditionData = var_25_3.conditionData,
					found = function(arg_27_0)
						arg_24_0.cloneTarget = arg_24_0:cloneGO(go(arg_27_0), arg_24_0._tf, var_25_3)

						setActive(arg_24_0.cloneTarget, false)

						local var_27_0 = Vector3(arg_24_0.cloneTarget.sizeDelta.x * (arg_24_0.cloneTarget.pivot.x - 0.5), arg_24_0.cloneTarget.sizeDelta.y * (arg_24_0.cloneTarget.pivot.y - 0.5), 0)

						var_25_14.localPosition = arg_24_0.cloneTarget.localPosition - var_27_0

						if var_25_3.sizeDeltaPlus then
							local var_27_1 = Vector2(var_25_3.sizeDeltaPlus[1], var_25_3.sizeDeltaPlus[2])

							var_25_15.sizeDelta = arg_24_0.cloneTarget.sizeDelta + var_27_1
						else
							var_25_15.sizeDelta = arg_24_0.cloneTarget.sizeDelta
						end

						setActive(var_25_14, true)
					end,
					notFound = function()
						arg_24_0:endGuider(arg_24_2)
					end
				})
			elseif var_25_4 then
				var_25_15.sizeDelta = Vector2.New(var_25_4[1], var_25_4[2])
			end

			local var_25_16 = GetOrAddComponent(var_25_15, typeof(UILongPressTrigger))

			var_25_16.onLongPressed:RemoveAllListeners()
			var_25_16.onReleased:RemoveAllListeners()

			if var_25_5 == 1 then
				var_25_16.onLongPressed:AddListener(function()
					recycle_handler()
				end)
			else
				var_25_16.onReleased:AddListener(function()
					recycle_handler()
				end)
			end
		elseif var_25_0 == 3 then
			var_25_14.sizeDelta = Vector2.New(var_25_4[1], var_25_4[2])

			arg_24_0:updateUIStyle(arg_24_1, true, arg_24_2)
		else
			if var_25_2 then
				arg_24_0:finishCurrEvent(arg_24_1, arg_24_2)
			end

			if var_25_1 ~= nil then
				arg_24_0.curSignList[var_25_13].signTimer = Timer.New(function()
					recycle_handler()
				end, var_25_1, 1)

				arg_24_0.curSignList[var_25_13].signTimer:Start()
			end
		end
	end)()
end

function var_0_0.getSign(arg_32_0, arg_32_1, arg_32_2)
	local var_32_0
	local var_32_1
	local var_32_2 = arg_32_2.atlasName
	local var_32_3 = arg_32_2.fileName

	if arg_32_0.signPool[arg_32_1] ~= nil and #arg_32_0.signPool[arg_32_1] > 0 then
		var_32_0 = table.remove(arg_32_0.signPool[arg_32_1], #arg_32_0.signPool[arg_32_1])
	else
		if arg_32_1 == 1 or arg_32_1 == 6 then
			var_32_1 = findTF(arg_32_0._signRes, "wTask")
		elseif arg_32_1 == 2 then
			var_32_1 = findTF(arg_32_0._signRes, "wDanger")
		elseif arg_32_1 == 3 then
			var_32_1 = findTF(arg_32_0._signRes, "wForbidden")
		elseif arg_32_1 == 4 then
			var_32_1 = findTF(arg_32_0._signRes, "wClickArea")
		elseif arg_32_1 == 5 then
			var_32_1 = findTF(arg_32_0._signRes, "wShowArea")
		end

		var_32_0 = tf(Instantiate(var_32_1))
	end

	if arg_32_1 == 6 then
		local var_32_4 = findTF(var_32_0, "shadow")
		local var_32_5 = LoadSprite(var_32_2, var_32_3)

		setImageSprite(var_32_4, var_32_5, true)
	end

	setActive(var_32_0, true)
	setParent(var_32_0, arg_32_0._go.transform)

	var_32_0.eulerAngles = Vector3(0, 0, 0)
	var_32_0.localScale = Vector3.one

	return var_32_0
end

function var_0_0.recycleSign(arg_33_0, arg_33_1, arg_33_2)
	if arg_33_0.signPool[arg_33_1] == nil then
		arg_33_0.signPool[arg_33_1] = {}
	end

	local var_33_0 = arg_33_0.signPool[arg_33_1]

	if #var_33_0 > 3 or arg_33_1 == 6 then
		Destroy(arg_33_2)
	else
		table.insert(var_33_0, arg_33_2)
		setParent(arg_33_2, arg_33_0._signRes)
		setActive(arg_33_2, false)
	end
end

function var_0_0.destroyAllSign(arg_34_0)
	for iter_34_0, iter_34_1 in ipairs(arg_34_0.curSignList) do
		if iter_34_1.signTimer ~= nil then
			iter_34_1.signTimer:Stop()

			iter_34_1.signTimer = nil
		end

		arg_34_0:recycleSign(iter_34_1.signType, iter_34_1.sign)

		arg_34_0.curSignList[iter_34_0] = nil
	end
end

function var_0_0.sendNotifies(arg_35_0, arg_35_1, arg_35_2)
	local var_35_0 = {}

	for iter_35_0, iter_35_1 in ipairs(arg_35_1.notifies) do
		table.insert(var_35_0, function(arg_36_0)
			pg.m02:sendNotification(iter_35_1.notify, iter_35_1.body)
			arg_36_0()
		end)
	end

	seriesAsync(var_35_0, function()
		arg_35_0:finishCurrEvent(arg_35_1, arg_35_2)
	end)
end

function var_0_0.playStories(arg_38_0, arg_38_1, arg_38_2)
	local var_38_0 = {}

	for iter_38_0, iter_38_1 in ipairs(arg_38_1.stories) do
		table.insert(var_38_0, function(arg_39_0)
			pg.NewStoryMgr.GetInstance():Play(iter_38_1, arg_39_0, true)
		end)
	end

	seriesAsync(var_38_0, function()
		arg_38_0:finishCurrEvent(arg_38_1, arg_38_2)
		pg.m02:sendNotification(GAME.START_GUIDE)
	end)
end

function var_0_0.hideUI(arg_41_0, arg_41_1, arg_41_2)
	local var_41_0 = {}

	for iter_41_0, iter_41_1 in ipairs(arg_41_1.hideui) do
		table.insert(var_41_0, function(arg_42_0)
			arg_41_0.finder:SearchTimely({
				path = iter_41_1.path,
				delay = iter_41_1.delay,
				pathIndex = iter_41_1.pathIndex,
				found = function(arg_43_0)
					SetActive(arg_43_0, not iter_41_1.ishide)
					arg_42_0()
				end,
				notFound = function()
					arg_41_0:endGuider(arg_41_2)
				end
			})
		end)
	end

	parallelAsync(var_41_0, function()
		arg_41_0:finishCurrEvent(arg_41_1, arg_41_2)
	end)
end

function var_0_0.findUI(arg_46_0, arg_46_1, arg_46_2)
	local var_46_0 = true
	local var_46_1 = {
		function(arg_47_0)
			if not arg_46_1.baseui then
				arg_47_0()

				return
			end

			arg_46_0.finder:Search({
				path = arg_46_1.baseui.path,
				delay = arg_46_1.baseui.delay,
				pathIndex = arg_46_1.baseui.pathIndex,
				conditionData = arg_46_1.baseui.conditionData,
				found = arg_47_0,
				notFound = function()
					arg_46_0:endGuider(arg_46_2)
				end
			})
		end,
		function(arg_49_0)
			if not arg_46_1.spriteui then
				arg_49_0()

				return
			end

			arg_46_0:CheckSprite(arg_46_1.spriteui, arg_49_0, arg_46_2)
		end,
		function(arg_50_0)
			if not arg_46_1.ui then
				arg_50_0()

				return
			end

			var_46_0 = false

			arg_46_0.finder:Search({
				path = arg_46_1.ui.path,
				delay = arg_46_1.ui.delay,
				pathIndex = arg_46_1.ui.pathIndex,
				conditionData = arg_46_1.ui.conditionData,
				found = function(arg_51_0)
					Canvas.ForceUpdateCanvases()

					arg_46_0.cloneTarget = arg_46_0:cloneGO(arg_51_0.gameObject, arg_46_0._go.transform, arg_46_1.ui)

					arg_46_0:addUIEventTrigger(arg_51_0, arg_46_1, arg_46_2)
					arg_46_0:setFinger(arg_51_0, arg_46_1.ui)
					arg_50_0()
				end,
				notFound = function()
					if arg_46_1.ui.notfoundSkip then
						arg_46_0:finishCurrEvent(arg_46_1, arg_46_2)
					else
						arg_46_0:endGuider(arg_46_2)
					end
				end
			})
		end
	}

	seriesAsync(var_46_1, function()
		arg_46_0:updateUIStyle(arg_46_1, var_46_0, arg_46_2)
	end)
end

function var_0_0.CheckSprite(arg_54_0, arg_54_1, arg_54_2, arg_54_3)
	local var_54_0
	local var_54_1
	local var_54_2 = 0
	local var_54_3 = 10

	local function var_54_4()
		var_54_2 = var_54_2 + 1

		arg_54_0:RemoveCheckSpriteTimer()

		local var_55_0 = var_54_1:GetComponent(typeof(Image))

		if IsNil(var_55_0.sprite) or arg_54_1.defaultName and var_55_0.sprite.name == arg_54_1.defaultName then
			if var_54_2 >= var_54_3 then
				arg_54_2()

				return
			end

			arg_54_0.srpiteTimer = Timer.New(var_54_4, 0.5, 1)

			arg_54_0.srpiteTimer:Start()
		else
			arg_54_2()
		end
	end

	arg_54_0.finder:Search({
		path = arg_54_1.path,
		delay = arg_54_1.delay,
		pathIndex = arg_54_1.pathIndex,
		conditionData = arg_54_1.conditionData,
		found = function(arg_56_0)
			if arg_54_1.childPath then
				var_54_1 = arg_56_0:Find(arg_54_1.childPath)
			else
				var_54_1 = arg_56_0
			end

			var_54_4()
		end,
		notFound = function()
			arg_54_0:endGuider(arg_54_3)
		end
	})
end

function var_0_0.RemoveCheckSpriteTimer(arg_58_0)
	if arg_58_0.srpiteTimer then
		arg_58_0.srpiteTimer:Stop()

		arg_58_0.srpiteTimer = nil
	end
end

function var_0_0.SetHighLightLine(arg_59_0, arg_59_1)
	local var_59_0 = arg_59_0._tf:InverseTransformPoint(arg_59_1.position)
	local var_59_1 = cloneTplTo(findTF(arg_59_0._signRes, "wShowArea"), arg_59_0._tf)
	local var_59_2 = 15

	var_59_1.sizeDelta = Vector2(arg_59_1.sizeDelta.x + var_59_2, arg_59_1.sizeDelta.y + var_59_2)
	var_59_1.pivot = arg_59_1.pivot

	local var_59_3 = (arg_59_1.pivot.x - 0.5) * var_59_2
	local var_59_4 = (arg_59_1.pivot.y - 0.5) * var_59_2
	local var_59_5 = Vector3(var_59_3, var_59_4, 0)

	var_59_1.localPosition = Vector3(var_59_0.x, var_59_0.y, 0) + var_59_5

	return var_59_1
end

function var_0_0.updateUIStyle(arg_60_0, arg_60_1, arg_60_2, arg_60_3)
	arg_60_0.bgAlpha.alpha = arg_60_1.alpha or 0.2

	SetActive(arg_60_0.guiderTF, arg_60_1.style)

	arg_60_0.highLightLines = {}

	local function var_60_0(arg_61_0)
		if arg_60_1.style.ui.lineMode then
			local var_61_0 = arg_60_0:SetHighLightLine(arg_61_0)

			table.insert(arg_60_0.highLightLines, var_61_0)
		else
			arg_60_0.cloneTarget = arg_60_0:cloneGO(go(arg_61_0), arg_60_0._tf, arg_60_1.style.ui)
		end
	end

	local function var_60_1()
		onButton(arg_60_0, arg_60_0._go, function()
			if arg_60_1.style and arg_60_1.style.scene then
				arg_60_0:finishCurrEvent(arg_60_1, arg_60_3)
				pg.m02:sendNotification(GAME.GO_SCENE, SCENE[arg_60_1.style.scene])
			elseif arg_60_1.style.trigger then
				arg_60_0.finder:Search({
					path = arg_60_1.style.trigger.path,
					delay = arg_60_1.style.trigger.delay,
					pathIndex = arg_60_1.style.trigger.pathIndex,
					found = function(arg_64_0)
						triggerButton(arg_64_0)
						arg_60_0:finishCurrEvent(arg_60_1, arg_60_3)
					end,
					notFound = function()
						arg_60_0:endGuider()
					end
				})
			else
				arg_60_0:finishCurrEvent(arg_60_1, arg_60_3)
			end
		end, SFX_PANEL)
		setButtonEnabled(arg_60_0._go, arg_60_2)
	end

	if arg_60_1.style then
		arg_60_0:updateContent(arg_60_1)

		if arg_60_1.style.ui then
			arg_60_0.finder:Search({
				path = arg_60_1.style.ui.path,
				delay = arg_60_1.style.ui.delay,
				pathIndex = arg_60_1.style.ui.pathIndex,
				found = var_60_0,
				notFound = function()
					arg_60_0:endGuider()
				end
			})
			var_60_1()
		elseif arg_60_1.style.uiset then
			local var_60_2 = {}

			for iter_60_0, iter_60_1 in ipairs(arg_60_1.style.uiset) do
				table.insert(var_60_2, function(arg_67_0)
					arg_60_0.finder:Search({
						path = iter_60_1.path,
						delay = iter_60_1.delay,
						pathIndex = iter_60_1.pathIndex,
						found = function(arg_68_0)
							local var_68_0
							local var_68_1

							if arg_60_1.style.lineMode then
								var_68_1 = arg_60_0:SetHighLightLine(arg_68_0)
							else
								var_68_0 = arg_60_0:cloneGO(go(arg_68_0), arg_60_0._tf, iter_60_1)
							end

							if var_68_0 then
								table.insert(arg_60_0.uisetGos, var_68_0)
							end

							if var_68_1 then
								table.insert(arg_60_0.highLightLines, var_68_1)
							end

							arg_67_0()
						end,
						notFound = function()
							arg_60_0:endGuider()
						end
					})
				end)
			end

			seriesAsync(var_60_2, var_60_1)
		else
			var_60_1()
		end
	else
		var_60_1()
	end
end

function var_0_0.updateContent(arg_70_0, arg_70_1)
	local var_70_0 = arg_70_1.style or {}
	local var_70_1 = var_70_0.dir or 1
	local var_70_2 = var_70_0.mode or 1
	local var_70_3 = var_70_0.posX or 0
	local var_70_4 = var_70_0.posY or 0

	SetActive(arg_70_0.styleTF1, var_70_2 == var_0_6.MODE1)
	SetActive(arg_70_0.styleTF2, var_70_2 == var_0_6.MODE2)

	local var_70_5
	local var_70_6

	if var_70_2 == var_0_6.MODE1 then
		var_70_5 = arg_70_0.styleTF1
		var_70_6 = Vector3(18, -31, 0)
	elseif var_70_2 == var_0_6.MODE2 then
		var_70_5 = arg_70_0.styleTF2
		var_70_6 = Vector3(-27, 143, 0)

		local var_70_7 = var_70_0.windowbg == "3"
		local var_70_8 = GetSpriteFromAtlas("ui/guide_atlas", "uibg" .. (var_70_7 and var_70_0.windowbg or "2"))

		var_70_5:GetComponent(typeof(Image)).sprite = var_70_8

		setAnchoredPosition(var_70_5:Find("content"), {
			x = var_70_7 and 0 or 17
		})
	end

	local var_70_9 = var_70_5:Find("char"):GetComponent(typeof(Image))
	local var_70_10
	local var_70_11 = var_70_0.char and var_70_0.char == "1" and 2 or var_70_0.char and var_70_0.char == "amazon" and 3 or 1
	local var_70_12 = arg_70_0.chars[var_70_11]

	var_70_9.sprite = var_70_12

	var_70_9:SetNativeSize()

	if var_70_11 == 2 then
		var_70_9.material = arg_70_0.material
	else
		var_70_9.material = nil
	end

	var_70_9.gameObject.transform.pivot = getSpritePivot(var_70_12)

	if var_70_0.charPos then
		setAnchoredPosition(var_70_9.gameObject.transform, {
			x = var_70_0.charPos[1],
			y = var_70_0.charPos[2]
		})
	else
		setAnchoredPosition(var_70_9.gameObject.transform, {
			x = var_70_6.x,
			y = var_70_6.y
		})
	end

	if var_70_0.charScale then
		var_70_9.gameObject.transform.localScale = Vector3(var_70_0.charScale[1], var_70_0.charScale[2], 1)
	else
		var_70_9.gameObject.transform.localScale = Vector3(1, 1, 1)
	end

	local var_70_13 = var_70_1 == 1 and Vector3(1, 1, 1) or Vector3(-1, 1, 1)

	var_70_5.localScale = var_70_13

	local var_70_14 = var_70_5:Find("content")

	var_70_14.localScale = var_70_13

	local var_70_15 = var_70_0.text or ""

	setText(var_70_14, HXSet.hxLan(var_70_15))

	local var_70_16 = var_70_14:GetComponent(typeof(Text))

	if #var_70_16.text > CHAT_POP_STR_LEN_MIDDLE then
		var_70_16.alignment = TextAnchor.MiddleLeft
	else
		var_70_16.alignment = TextAnchor.MiddleCenter
	end

	local var_70_17 = var_70_16.preferredHeight + 120

	if var_70_2 == var_0_6.MODE2 and var_70_17 > arg_70_0.initChatBgH then
		var_70_5.sizeDelta = Vector2.New(var_70_5.sizeDelta.x, var_70_17)
	else
		var_70_5.sizeDelta = Vector2.New(var_70_5.sizeDelta.x, arg_70_0.initChatBgH)
	end

	if var_70_2 == var_0_6.MODE1 then
		local var_70_18 = var_70_0.hand or {
			w = 0,
			x = -267,
			y = -96
		}

		var_70_5:Find("hand").localPosition = Vector3(var_70_18.x, var_70_18.y, 0)
		var_70_5:Find("hand").eulerAngles = Vector3(0, 0, var_70_18.w)
	end

	setAnchoredPosition(arg_70_0.guiderTF, Vector2(var_70_3, var_70_4))
end

function var_0_0.Finder(arg_71_0)
	local var_71_0 = {}

	local function var_71_1(arg_72_0, arg_72_1)
		local var_72_0 = -1

		for iter_72_0 = 1, arg_72_0.childCount do
			local var_72_1 = arg_72_0:GetChild(iter_72_0 - 1):GetComponent(typeof(LayoutElement))

			if not var_72_1 or not var_72_1.ignoreLayout then
				var_72_0 = var_72_0 + 1

				if var_72_0 == arg_72_1 then
					break
				end
			end
		end

		return var_72_0
	end

	local function var_71_2(arg_73_0, arg_73_1)
		local var_73_0 = GameObject.Find(arg_73_0)

		if not IsNil(var_73_0) then
			if arg_73_1 and arg_73_1 == -999 then
				local var_73_1 = tf(var_73_0).childCount

				for iter_73_0 = 0, var_73_1 do
					local var_73_2 = tf(var_73_0):GetChild(iter_73_0)

					if not IsNil(var_73_2) and go(var_73_2).activeInHierarchy then
						return var_73_2
					end
				end
			elseif arg_73_1 and arg_73_1 ~= -1 then
				local var_73_3 = var_71_1(tf(var_73_0), arg_73_1)

				if var_73_3 >= 0 and var_73_3 < tf(var_73_0).childCount then
					local var_73_4 = tf(var_73_0):GetChild(var_73_3)

					if not IsNil(var_73_4) then
						return var_73_4
					end
				end
			else
				return tf(var_73_0)
			end
		end
	end

	local function var_71_3(arg_74_0, arg_74_1)
		local var_74_0 = var_71_2(arg_74_0, -1)

		if var_74_0 ~= nil then
			for iter_74_0, iter_74_1 in ipairs(arg_74_1) do
				local var_74_1 = var_74_0:Find(iter_74_1)

				if var_74_1 then
					return var_74_1
				end
			end
		end
	end

	function var_71_0.Search(arg_75_0, arg_75_1)
		local var_75_0

		if type(arg_75_1.path) == "function" then
			var_75_0 = arg_75_1.path()
		else
			var_75_0 = arg_75_1.path
		end

		arg_75_0:Clear()

		local var_75_1 = 0.5
		local var_75_2 = 20
		local var_75_3 = 0
		local var_75_4 = arg_75_1.delay or 0

		arg_75_0.findUITimer = Timer.New(function()
			var_75_3 = var_75_3 + var_75_1

			if pg.UIMgr.GetInstance():OnLoading() then
				return
			end

			if var_75_3 > var_75_4 then
				if var_75_2 == 0 then
					originalPrint("not found ui >>", var_75_0)
					arg_75_0:Clear()
					arg_75_1.notFound()

					return
				end

				local var_76_0

				if arg_75_1.conditionData ~= nil then
					var_76_0 = var_71_3(var_75_0, arg_75_1.conditionData)
				else
					var_76_0 = var_71_2(var_75_0, arg_75_1.pathIndex)
				end

				if var_76_0 and go(var_76_0).activeInHierarchy then
					arg_75_0:Clear()
					arg_75_1.found(var_76_0)

					return
				end

				var_75_2 = var_75_2 - 1
			end
		end, var_75_1, -1)

		arg_75_0.findUITimer:Start()
		arg_75_0.findUITimer.func()
	end

	function var_71_0.SearchTimely(arg_77_0, arg_77_1)
		local var_77_0

		if type(arg_77_1.path) == "function" then
			var_77_0 = arg_77_1.path()
		else
			var_77_0 = arg_77_1.path
		end

		arg_77_0:Clear()

		local var_77_1 = var_71_2(var_77_0, arg_77_1.pathIndex)

		if var_77_1 then
			arg_77_1.found(var_77_1)
		else
			arg_77_1.notFound()
		end
	end

	function var_71_0.Clear(arg_78_0)
		if arg_78_0.findUITimer then
			arg_78_0.findUITimer:Stop()

			arg_78_0.findUITimer = nil
		end
	end

	return var_71_0
end

function var_0_0.cloneGO(arg_79_0, arg_79_1, arg_79_2, arg_79_3)
	local var_79_0 = tf(Instantiate(arg_79_1))

	var_79_0.sizeDelta = tf(arg_79_1).sizeDelta

	SetActive(var_79_0, true)
	var_79_0:SetParent(arg_79_2, false)

	if arg_79_3.hideChildEvent then
		eachChild(var_79_0, function(arg_80_0)
			local var_80_0 = arg_80_0:GetComponent(typeof(Button))

			if var_80_0 then
				var_80_0.enabled = false
			end
		end)
	end

	if arg_79_3.hideAnimtor then
		local var_79_1 = var_79_0:GetComponent(typeof(Animator))

		if var_79_1 then
			var_79_1.enabled = false
		end
	end

	if arg_79_3.childAdjust then
		for iter_79_0, iter_79_1 in ipairs(arg_79_3.childAdjust) do
			local var_79_2 = var_79_0:Find(iter_79_1[1])

			if LeanTween.isTweening(var_79_2.gameObject) then
				LeanTween.cancel(var_79_2.gameObject)
			end

			if var_79_2 and iter_79_1[2] == "scale" then
				var_79_2.localScale = Vector3(iter_79_1[3][1], iter_79_1[3][2], iter_79_1[3][3])
			elseif var_79_2 and iter_79_1[2] == "position" then
				var_79_2.anchoredPosition = Vector3(iter_79_1[3][1], iter_79_1[3][2], iter_79_1[3][3])
			end
		end
	end

	if arg_79_0.targetTimer then
		arg_79_0.targetTimer:Stop()

		arg_79_0.targetTimer = nil
	end

	if not arg_79_3.pos and not arg_79_3.scale and not arg_79_3.eulerAngles then
		arg_79_0.targetTimer = Timer.New(function()
			if not IsNil(arg_79_1) and not IsNil(var_79_0) then
				var_79_0.position = arg_79_1.transform.position

				local var_81_0 = var_79_0.localPosition

				var_79_0.localPosition = Vector3(var_81_0.x, var_81_0.y, 0)

				local var_81_1 = arg_79_1.transform.localScale

				var_79_0.localScale = Vector3(var_81_1.x, var_81_1.y, var_81_1.z)

				if arg_79_3.image and type(arg_79_3.image) == "table" then
					local var_81_2

					if arg_79_3.image.isChild then
						var_81_2 = tf(arg_79_1):Find(arg_79_3.image.source)
					else
						var_81_2 = GameObject.Find(arg_79_3.image.source)
					end

					local var_81_3 = arg_79_3.image.isRelative
					local var_81_4

					if var_81_3 then
						if arg_79_3.image.target == "" then
							var_81_4 = var_79_0
						else
							var_81_4 = tf(var_79_0):Find(arg_79_3.image.target)
						end
					else
						var_81_4 = GameObject.Find(arg_79_3.image.target)
					end

					if not IsNil(var_81_2) and not IsNil(var_81_4) then
						local var_81_5 = var_81_2:GetComponent(typeof(Image))
						local var_81_6 = var_81_4:GetComponent(typeof(Image))

						if var_81_5 and var_81_6 then
							local var_81_7 = var_81_5.sprite
							local var_81_8 = var_81_6.sprite

							if var_81_7 and var_81_8 and var_81_7 ~= var_81_8 then
								var_81_6.enabled = var_81_5.enabled

								setImageSprite(var_81_4, var_81_7)
							end
						end
					end
				end
			end
		end, 0.01, -1)

		arg_79_0.targetTimer:Start()
		arg_79_0.targetTimer.func()
	else
		if arg_79_3.pos then
			var_79_0.localPosition = Vector3(arg_79_3.pos.x, arg_79_3.pos.y, arg_79_3.pos.z or 0)
		elseif arg_79_3.isLevelPoint then
			local var_79_3 = GameObject.Find("LevelCamera"):GetComponent(typeof(Camera))
			local var_79_4 = arg_79_1.transform.parent:TransformPoint(arg_79_1.transform.localPosition)
			local var_79_5 = var_79_3:WorldToScreenPoint(var_79_4)
			local var_79_6 = GameObject.Find("OverlayCamera"):GetComponent(typeof(Camera))

			var_79_0.localPosition = LuaHelper.ScreenToLocal(arg_79_2, var_79_5, var_79_6)
		else
			var_79_0.position = arg_79_1.transform.position

			local var_79_7 = var_79_0.localPosition

			var_79_0.localPosition = Vector3(var_79_7.x, var_79_7.y, 0)
		end

		local var_79_8 = arg_79_3.scale or 1

		var_79_0.localScale = Vector3(var_79_8, var_79_8, var_79_8)

		if arg_79_3.eulerAngles then
			var_79_0.eulerAngles = Vector3(arg_79_3.eulerAngles[1], arg_79_3.eulerAngles[2], arg_79_3.eulerAngles[3])
		else
			var_79_0.eulerAngles = Vector3(0, 0, 0)
		end
	end

	return var_79_0
end

function var_0_0.setFinger(arg_82_0, arg_82_1, arg_82_2)
	SetActive(arg_82_0.fingerTF, not arg_82_2.fingerPos or not arg_82_2.fingerPos.hideFinger)

	local var_82_0 = arg_82_1.sizeDelta.x / 2
	local var_82_1 = arg_82_1.sizeDelta.y / 2
	local var_82_2 = arg_82_2.scale and 1 / arg_82_2.scale or 1

	arg_82_0.fingerTF.localScale = Vector3(var_82_2, var_82_2, 1)

	local var_82_3 = arg_82_2.fingerPos and Vector3(arg_82_2.fingerPos.posX, arg_82_2.fingerPos.posY, 0) or Vector3(var_82_0, -var_82_1, 0)

	if arg_82_0.cloneTarget then
		arg_82_0.fingerTF:SetParent(arg_82_0.cloneTarget, false)
	end

	setAnchoredPosition(arg_82_0.fingerTF, var_82_3)
end

function var_0_0.addUIEventTrigger(arg_83_0, arg_83_1, arg_83_2, arg_83_3)
	local var_83_0 = arg_83_2.ui
	local var_83_1 = arg_83_1
	local var_83_2 = arg_83_0.cloneTarget
	local var_83_3 = var_83_2:GetComponent(typeof(CanvasGroup))

	if var_83_3 then
		var_83_3.alpha = 1
	end

	if var_83_0.eventIndex then
		var_83_1 = arg_83_1:GetChild(var_83_0.eventIndex)
		var_83_2 = arg_83_0.cloneTarget:GetChild(var_83_0.eventIndex)
	elseif var_83_0.eventPath then
		var_83_1 = GameObject.Find(var_83_0.eventPath)

		if IsNil(var_83_1) then
			var_83_1 = arg_83_1
		end

		if arg_83_0.cloneTarget:GetComponent(typeof(Image)) == nil then
			GetOrAddComponent(arg_83_0.cloneTarget, typeof(Image)).color = Color(1, 1, 1, 0)
		end
	end

	local var_83_4 = var_83_0.triggerType and var_83_0.triggerType[1] or var_0_1

	if var_83_4 == var_0_1 then
		onButton(arg_83_0, var_83_2, function()
			if not IsNil(var_83_1) then
				arg_83_0:finishCurrEvent(arg_83_2, arg_83_3)

				if var_83_0.onClick then
					var_83_0.onClick()
				else
					triggerButton(var_83_1)
				end
			end
		end, SFX_PANEL)
		setButtonEnabled(var_83_2, true)
	elseif var_83_4 == var_0_2 then
		onToggle(arg_83_0, var_83_2, function(arg_85_0)
			if IsNil(var_83_1) then
				return
			end

			arg_83_0:finishCurrEvent(arg_83_2, arg_83_3)

			if var_83_0.triggerType[2] ~= nil then
				triggerToggle(var_83_1, var_83_0.triggerType[2])
			else
				triggerToggle(var_83_1, true)
			end
		end, SFX_PANEL)
		setToggleEnabled(var_83_2, true)
	elseif var_83_4 == var_0_3 then
		local var_83_5 = var_83_1:GetComponent(typeof(EventTriggerListener))
		local var_83_6 = var_83_2:GetComponent(typeof(EventTriggerListener))

		var_83_6:AddPointDownFunc(function(arg_86_0, arg_86_1)
			if not IsNil(var_83_1) then
				var_83_5:OnPointerDown(arg_86_1)
			end
		end)
		var_83_6:AddPointUpFunc(function(arg_87_0, arg_87_1)
			arg_83_0:finishCurrEvent(arg_83_2, arg_83_3)

			if not IsNil(var_83_1) then
				var_83_5:OnPointerUp(arg_87_1)
			end
		end)
	elseif var_83_4 == var_0_4 then
		local var_83_7 = var_83_2:GetComponent(typeof(EventTriggerListener))

		if var_83_7 == nil then
			var_83_7 = go(var_83_2):AddComponent(typeof(EventTriggerListener))
		end

		var_83_7:AddPointDownFunc(function(arg_88_0, arg_88_1)
			if not IsNil(var_83_1) then
				arg_83_0:finishCurrEvent(arg_83_2, arg_83_3)
			end
		end)
	elseif var_83_4 == var_0_5 then
		local var_83_8 = var_83_2:GetComponent(typeof(EventTriggerListener))

		if var_83_8 == nil then
			var_83_8 = go(var_83_2):AddComponent(typeof(EventTriggerListener))
		end

		var_83_8:AddPointUpFunc(function(arg_89_0, arg_89_1)
			arg_83_0:finishCurrEvent(arg_83_2, arg_83_3)
		end)
	end
end

function var_0_0.finishCurrEvent(arg_90_0, arg_90_1, arg_90_2)
	arg_90_0.bgAlpha.alpha = 0.2

	removeOnButton(arg_90_0._go)
	arg_90_0:destroyAllSign()
	SetParent(arg_90_0.fingerTF, tf(arg_90_0._go), false)
	SetActive(arg_90_0.fingerTF, false)
	SetActive(arg_90_0.guiderTF, false)

	arg_90_0.fingerTF.localScale = Vector3(1, 1, 1)

	if arg_90_0.cloneTarget then
		SetActive(arg_90_0.cloneTarget, false)
		Destroy(arg_90_0.cloneTarget)

		arg_90_0.cloneTarget = nil
	end

	if #arg_90_0.uisetGos > 0 then
		for iter_90_0 = #arg_90_0.uisetGos, 1, -1 do
			Destroy(arg_90_0.uisetGos[iter_90_0])

			arg_90_0.uisetGos[iter_90_0] = nil
		end

		arg_90_0.uisetGos = {}
	end

	if arg_90_0.targetTimer then
		arg_90_0.targetTimer:Stop()

		arg_90_0.targetTimer = nil
	end

	if arg_90_0.findUITimer then
		arg_90_0.findUITimer:Stop()

		arg_90_0.findUITimer = nil
	end

	if arg_90_0.highLightLines then
		for iter_90_1, iter_90_2 in ipairs(arg_90_0.highLightLines) do
			Destroy(iter_90_2)
		end

		arg_90_0.highLightLines = {}
	end

	if arg_90_2 then
		arg_90_2()
	end
end

local function var_0_7(arg_91_0)
	arg_91_0:clearDelegateInfo()
	arg_91_0:RemoveCheckSpriteTimer()

	if arg_91_0.delayTimer then
		arg_91_0.delayTimer:Stop()

		arg_91_0.delayTimer = nil
	end

	if arg_91_0.targetTimer then
		arg_91_0.targetTimer:Stop()

		arg_91_0.targetTimer = nil
	end

	arg_91_0:destroyAllSign()
	arg_91_0.finder:Clear()

	if arg_91_0.cloneTarget then
		SetParent(arg_91_0.fingerTF, arg_91_0._go)
		Destroy(arg_91_0.cloneTarget)

		arg_91_0.cloneTarget = nil
	end

	arg_91_0._go:SetActive(false)
	removeOnButton(arg_91_0._go)

	if arg_91_0.curEvents then
		arg_91_0.curEvents = nil
	end

	if arg_91_0.currentGuide then
		arg_91_0.currentGuide = nil
	end

	arg_91_0.uiLongPress.onLongPressed:RemoveAllListeners()
end

function var_0_0.addDelegateInfo(arg_92_0)
	pg.DelegateInfo.New(arg_92_0)

	arg_92_0.isAddDelegateInfo = true
end

function var_0_0.clearDelegateInfo(arg_93_0)
	if arg_93_0.isAddDelegateInfo then
		pg.DelegateInfo.Dispose(arg_93_0)

		arg_93_0.isAddDelegateInfo = nil
	end
end

function var_0_0.mask(arg_94_0)
	SetActive(arg_94_0._go, true)
end

function var_0_0.unMask(arg_95_0)
	SetActive(arg_95_0._go, false)
end

function var_0_0.endGuider(arg_96_0, arg_96_1)
	var_0_7(arg_96_0)

	arg_96_0.managerState = var_0_0.MANAGER_STATE.IDLE

	pg.m02:sendNotification(GAME.END_GUIDE)

	if arg_96_1 then
		arg_96_1()
	end
end

function var_0_0.onDisconnected(arg_97_0)
	if arg_97_0._go.activeSelf then
		arg_97_0.prevState = arg_97_0.managerState
		arg_97_0.managerState = var_0_0.MANAGER_STATE.BREAK

		SetActive(arg_97_0._go, false)

		if arg_97_0.cloneTarget then
			SetActive(arg_97_0.cloneTarget, false)
		end
	end
end

function var_0_0.onReconneceted(arg_98_0)
	if arg_98_0.prevState then
		arg_98_0.managerState = arg_98_0.prevState
		arg_98_0.prevState = nil

		SetActive(arg_98_0._go, true)

		if arg_98_0.cloneTarget then
			SetActive(arg_98_0.cloneTarget, true)
		end
	end
end
