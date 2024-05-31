local var_0_0 = class("Dorm3dScene", import("view.base.BaseUI"))

var_0_0.CAMERA = {
	GIFT = 8,
	PHOTO = 10,
	FURNITURE_WATCH = 7,
	TALK = 4,
	ROLE_WATCH = 5,
	AIM = 1,
	ROLE2 = 9,
	FURNITURE_FREELOOK = 6,
	ROLE = 3,
	AIM2 = 2
}
var_0_0.BONE_TO_TOUCH = {
	Head = "head",
	LeftUpperArm = "hand",
	RightThigh = "leg",
	Butt = "butt",
	LeftCalf = "leg",
	RightLowerArm = "hand",
	Chest = "chest",
	RightCalf = "leg",
	RightUpperArm = "hand",
	LeftThigh = "leg",
	Back = "back",
	LeftLowerArm = "hand",
	Belly = "belly"
}
var_0_0.CAMERA_MAX_OPERATION = {
	RIGHT = "right",
	DOWN = "donw",
	ZOOMIN = "zoom_in",
	ZOOMOUT = "zoom_out",
	UP = "up",
	LEFT = "left"
}
var_0_0.ANIM = {
	IDLE = "Idle"
}
var_0_0.PLAY_SINGLE_ACTION = "Dorm3dScene.PLAY_ACTION"
var_0_0.SWITCH_ACTION = "Dorm3dScene.SWITCH_ACTION"
var_0_0.PLAY_TIMELINE = "Dorm3dScene.PLAY_TIMELINE"
var_0_0.MOVE_PLAYER_TO_FURNITURE = "Dorm3dScene.MOVE_PLAYER_TO_FURNITURE"
var_0_0.ACTIVE_CAMERA = "Dorm3dScene.ACTIVE_CAMERA"
var_0_0.SHOW_BLOCK = "Dorm3dScene.SHOW_BLOCK"
var_0_0.HIDE_BLOCK = "Dorm3dScene.HIDE_BLOCK"
var_0_0.ENTER_FREELOOK_MODE = "Dorm3dScene.ENTER_FREELOOK_MODE"
var_0_0.EXIT_FREELOOK_MODE = "Dorm3dScene.EXIT_FREELOOK_MODE"
var_0_0.ENTER_WATCH_MODE = "Dorm3dScene.ENTER_WATCH_MODE"
var_0_0.EXIT_WATCH_MODE = "Dorm3dScene.EXIT_WATCH_MODE"
var_0_0.WATCH_MODE_INTERACTIVE = "Dorm3dScene.WATCH_MODE_INTERACTIVE"
var_0_0.ENTER_GIFT_MODE = "Dorm3dScene.ENTER_GIFT_MODE"
var_0_0.EXIT_GIFT_MODE = "Dorm3dScene.EXIT_GIFT_MODE"
var_0_0.ON_DIALOGUE_BEGIN = "Dorm3dScene.ON_DIALOGUE_BEGIN"
var_0_0.ON_DIALOGUE_END = "Dorm3dScene.ON_DIALOGUE_END"
var_0_0.ON_TOUCH_CHARACTER = "Dorm3dScene.ON_TOUCH_CHARACTER"
var_0_0.ON_ROLEWATCH_CAMERA_MAX = "Dorm3dScene.ON_ROLEWATCH_CAMERA_MAX"
var_0_0.ON_UPDATE_CONTACT_STSTE = "Dorm3dScene.ON_UPDATE_CONTACT_STSTE"
var_0_0.ON_UPDATE_CONTACT_POSITION = "Dorm3dScene.ON_UPDATE_CONTACT_POSITION"
var_0_0.ON_STICK_MOVE = "Dorm3dScene.ON_STICK_MOVE"

function var_0_0.getUIName(arg_1_0)
	return "Dorm3dMainUI"
end

function var_0_0.Ctor(arg_2_0, ...)
	var_0_0.super.Ctor(arg_2_0, ...)

	arg_2_0.sceneDataList = {}
	arg_2_0.sceneCounter = 0
end

function var_0_0.preload(arg_3_0, arg_3_1)
	local var_3_0 = arg_3_0.contextData.groupId
	local var_3_1 = getProxy(ApartmentProxy):getApartment(var_3_0)

	arg_3_0:SetApartment(var_3_1)

	arg_3_0.sceneRootName = var_3_1:GetSceneRootName()
	arg_3_0.assetRootName = var_3_1:GetAssetName()

	for iter_3_0, iter_3_1 in ipairs({
		"sceneName",
		"baseSceneName",
		"modelName"
	}) do
		arg_3_0[iter_3_1] = arg_3_0.contextData.sceneData[iter_3_1]
	end

	arg_3_0.contextData.inFurnitureName = arg_3_0.contextData.inFurnitureName or "Default"

	seriesAsync({
		function(arg_4_0)
			pg.UIMgr.GetInstance():LoadingOn(false)
			arg_3_0:LoadSceneAsync(string.lower("dorm3d/scenesres/scenes/" .. arg_3_0.sceneRootName .. "/" .. arg_3_0.sceneName .. "_scene"), arg_3_0.sceneName, function(arg_5_0, arg_5_1)
				SceneOpMgr.Inst:SetActiveSceneByIndex(1)
				onNextTick(arg_4_0)
			end)
		end,
		function(arg_6_0)
			arg_3_0:LoadSceneAsync(string.lower("dorm3d/scenesres/scenes/" .. arg_3_0.sceneRootName .. "/" .. arg_3_0.baseSceneName .. "_scene"), arg_3_0.baseSceneName, function(arg_7_0, arg_7_1)
				arg_6_0()
			end)
		end,
		function(arg_8_0)
			arg_3_0:LoadCharacter(arg_8_0)
		end,
		function(arg_9_0)
			pg.UIMgr.GetInstance():LoadingOff()
			arg_9_0()
		end,
		arg_3_1
	})
end

function var_0_0.init(arg_10_0)
	arg_10_0:initScene()
	arg_10_0:InitCharacter()

	arg_10_0.retainCount = 0
	arg_10_0.blockLayer = arg_10_0._tf:Find("Block")

	setActive(arg_10_0.blockLayer, false)

	arg_10_0.blackLayer = arg_10_0._tf:Find("BlackScreen")

	setActive(arg_10_0.blackLayer, false)

	arg_10_0.loader = AutoLoader.New()

	arg_10_0:BindEvent()

	arg_10_0.baseView = Dorm3dBaseView.New(nil, arg_10_0.event, arg_10_0.contextData)

	arg_10_0.baseView:SetExtra(arg_10_0._tf)
	arg_10_0.baseView:Load()
	arg_10_0.baseView:BindEvent()
	arg_10_0.baseView:SetApartment(arg_10_0.apartment)
	arg_10_0.baseView:initNodeCanvas(arg_10_0.rtMainAI)
	arg_10_0.baseView:SetLadyTransform(arg_10_0.lady)
end

function var_0_0.BindEvent(arg_11_0)
	arg_11_0:bind(Dorm3dScene.PLAY_SINGLE_ACTION, function(arg_12_0, arg_12_1, arg_12_2)
		arg_11_0:PlaySingleAction(arg_12_1, arg_12_2)
	end)
	arg_11_0:bind(Dorm3dScene.SWITCH_ACTION, function(arg_13_0, arg_13_1, arg_13_2)
		arg_11_0:SwitchAnim(arg_13_1, arg_13_2)
	end)
	arg_11_0:bind(Dorm3dScene.PLAY_TIMELINE, function(arg_14_0, arg_14_1, arg_14_2)
		arg_11_0:PlayTimeline(arg_14_1, arg_14_2)
	end)
	arg_11_0:bind(Dorm3dScene.MOVE_PLAYER_TO_FURNITURE, function(arg_15_0, arg_15_1, arg_15_2)
		arg_11_0:PlayerMove(arg_15_1, arg_15_2)
	end)
	arg_11_0:bind(Dorm3dScene.ACTIVE_CAMERA, function(arg_16_0, arg_16_1)
		local var_16_0 = arg_11_0.cameras[arg_16_1]

		arg_11_0:ActiveCamera(var_16_0)
	end)
	arg_11_0:bind(Dorm3dScene.SHOW_BLOCK, function()
		arg_11_0.retainCount = arg_11_0.retainCount + 1

		setActive(arg_11_0.blockLayer, true)
	end)
	arg_11_0:bind(Dorm3dScene.HIDE_BLOCK, function()
		arg_11_0.retainCount = math.max(arg_11_0.retainCount - 1, 0)

		if arg_11_0.retainCount > 0 then
			return
		end

		setActive(arg_11_0.blockLayer, false)
	end)
	arg_11_0:bind(Dorm3dScene.ENTER_FREELOOK_MODE, function(arg_19_0, arg_19_1, arg_19_2)
		arg_11_0:EnterFreelookMode(arg_19_1, arg_19_2)
	end)
	arg_11_0:bind(Dorm3dScene.EXIT_FREELOOK_MODE, function(arg_20_0, arg_20_1, arg_20_2)
		arg_11_0:ExitFreelookMode(arg_20_1, arg_20_2)
	end)
	arg_11_0:bind(Dorm3dScene.ENTER_WATCH_MODE, function(arg_21_0)
		arg_11_0:EnterWatchMode()
	end)
	arg_11_0:bind(Dorm3dScene.EXIT_WATCH_MODE, function(arg_22_0)
		arg_11_0:ExitWatchMode()
	end)
	arg_11_0:bind(Dorm3dScene.WATCH_MODE_INTERACTIVE, function(arg_23_0)
		arg_11_0:WatchModeInteractive()
	end)
	arg_11_0:bind(Dorm3dScene.ENTER_GIFT_MODE, function(arg_24_0)
		arg_11_0:EnterGiftMode()
	end)
	arg_11_0:bind(Dorm3dScene.EXIT_GIFT_MODE, function(arg_25_0)
		arg_11_0:ExitGiftMode()
	end)
	arg_11_0:bind(Dorm3dScene.ON_DIALOGUE_BEGIN, function(arg_26_0, arg_26_1)
		arg_26_1()
	end)
	arg_11_0:bind(Dorm3dScene.ON_DIALOGUE_END, function(arg_27_0, arg_27_1)
		arg_27_1()
	end)
	arg_11_0:bind(Dorm3dScene.ON_UPDATE_CONTACT_STSTE, function(arg_28_0, arg_28_1)
		warning("test")
		arg_11_0:ActiveContact(arg_28_1)
	end)
	arg_11_0:bind(Dorm3dScene.ON_UPDATE_CONTACT_POSITION, function(arg_29_0, arg_29_1)
		arg_11_0:UpdateContactPosition(arg_29_1)
	end)
	arg_11_0:bind(Dorm3dScene.ON_STICK_MOVE, function(arg_30_0, arg_30_1)
		arg_11_0:OnStickMove(arg_30_1)
	end)
end

function var_0_0.SetApartment(arg_31_0, arg_31_1)
	arg_31_0.apartment = arg_31_1

	if arg_31_0.baseView then
		arg_31_0.baseView:SetApartment(arg_31_1)
	end
end

function var_0_0.GetApartment(arg_32_0)
	return arg_32_0.apartment
end

function var_0_0.initScene(arg_33_0)
	arg_33_0.mainCameraTF = GameObject.Find("BackYardMainCamera").transform
	arg_33_0.camBrain = arg_33_0.mainCameraTF:GetComponent(typeof(Cinemachine.CinemachineBrain))
	arg_33_0.camBrainEvenetHandler = arg_33_0.mainCameraTF:GetComponent(typeof(CameraBrainEventsHandler))
	arg_33_0.player = GameObject.Find("Player").transform
	arg_33_0.furnitures = GameObject.Find("Furnitures").transform
	arg_33_0.attachedPoints = {}

	eachChild(arg_33_0.furnitures, function(arg_34_0)
		table.insert(arg_33_0.attachedPoints, 1, arg_34_0)
		setActive(arg_34_0:Find("FreeLook Camera"), false)
		setActive(arg_34_0:Find("RoleWatch Camera"), false)
	end)

	arg_33_0.dollyParent = GameObject.Find("Dollys").transform
	arg_33_0.inFurniture = arg_33_0.furnitures:Find(arg_33_0.contextData.inFurnitureName)

	local var_33_0 = GetComponent(arg_33_0.inFurniture, typeof(UnityEngine.Collider))

	if var_33_0 then
		var_33_0.enabled = false
	end

	arg_33_0.modelRoot = GameObject.Find("fbx").transform
	arg_33_0.slotRoot = GameObject.Find("FurnitureSlots").transform

	setActive(arg_33_0.slotRoot, true)
	arg_33_0:InitSlots()

	arg_33_0.contactRoot = GameObject.Find("ContactColliders").transform

	setActive(arg_33_0.contactRoot, true)
	arg_33_0:InitContact()

	local var_33_1 = GameObject.Find("CM Cameras").transform

	arg_33_0.cameraAim = var_33_1:Find("Aim Camera"):GetComponent(typeof(Cinemachine.CinemachineVirtualCamera))
	arg_33_0.cameraAim2 = var_33_1:Find("Aim2 Camera"):GetComponent(typeof(Cinemachine.CinemachineVirtualCamera))
	arg_33_0.cameraFree = nil
	arg_33_0.cameraFurnitureWatch = nil
	arg_33_0.cameraRole = var_33_1:Find("Role Camera"):GetComponent(typeof(Cinemachine.CinemachineVirtualCamera))
	arg_33_0.cameraRole2 = var_33_1:Find("Role2 Camera"):GetComponent(typeof(Cinemachine.CinemachineVirtualCamera))
	arg_33_0.cameraTalk = var_33_1:Find("Talk Camera"):GetComponent(typeof(Cinemachine.CinemachineVirtualCamera))
	arg_33_0.cameraGift = var_33_1:Find("Gift Camera"):GetComponent(typeof(Cinemachine.CinemachineVirtualCamera))
	arg_33_0.cameraRoleWatch = nil
	arg_33_0.cameraPhoto = var_33_1:Find("Photo Camera"):GetComponent(typeof(Cinemachine.CinemachineFreeLook))
	arg_33_0.cameras = {
		arg_33_0.cameraAim,
		arg_33_0.cameraAim2,
		arg_33_0.cameraRole,
		arg_33_0.cameraTalk,
		arg_33_0.cameraRoleWatch,
		[var_0_0.CAMERA.GIFT] = arg_33_0.cameraGift,
		[var_0_0.CAMERA.ROLE2] = arg_33_0.cameraRole2,
		[var_0_0.CAMERA.PHOTO] = arg_33_0.cameraPhoto
	}
	arg_33_0.compDolly = arg_33_0.cameraAim:GetCinemachineComponent(Cinemachine.CinemachineCore.Stage.Body)
	arg_33_0.compPov = nil
	arg_33_0.ladyInterest = GameObject.Find("InterestProxy").transform
	arg_33_0.rtMainAI = GameObject.Find("MainAI").transform
	arg_33_0.mainCameraTF:Find("CameraForRaycast"):GetComponent(typeof(Camera)).fieldOfView = arg_33_0.mainCameraTF:GetComponent(typeof(Camera)).fieldOfView

	arg_33_0:InitTimeline()

	arg_33_0.globalVolume = GameObject.Find("GlobalVolume")

	arg_33_0:RegisterGlobalVolume()

	arg_33_0.characterLight = GameObject.Find("CharacterLight")

	arg_33_0:RecordCharacterLight()

	local var_33_2 = GameObject.Find("[Lighting]").transform

	table.IpairsCArray(var_33_2:GetComponentsInChildren(typeof(Light)), function(arg_35_0, arg_35_1)
		arg_35_1.shadows = UnityEngine.LightShadows.None
	end)

	arg_33_0.daynightCtrlComp = GameObject.Find("[MainBlock]").transform:GetComponent(typeof(DayNightCtrl))
end

function var_0_0.InitSlots(arg_36_0)
	local var_36_0 = arg_36_0.apartment:GetSlots()
	local var_36_1 = arg_36_0.modelRoot:GetComponentsInChildren(typeof(Transform))

	arg_36_0.slotDict = {}

	_.each(var_36_0, function(arg_37_0)
		local var_37_0 = arg_37_0:GetFurnitureName()
		local var_37_1 = arg_37_0:GetConfigID()
		local var_37_2 = arg_36_0.slotRoot:Find(tostring(var_37_1))

		assert(var_37_2)

		local var_37_3 = {
			trans = var_37_2
		}
		local var_37_4 = var_37_2:Find("Selector")

		if var_37_4 then
			GetOrAddComponent(var_37_4, typeof(EventTriggerListener)):AddPointClickFunc(function(arg_38_0, arg_38_1)
				arg_36_0:emit(Dorm3dSceneMediator.ON_CLICK_FURNITURE_SLOT, var_37_1)
			end)
			setActive(var_37_4, false)
		end

		local var_37_5

		for iter_37_0 = 0, var_36_1.Length - 1 do
			local var_37_6 = var_36_1[iter_37_0]

			if var_37_6.name == var_37_0 then
				var_37_5 = var_37_6

				break
			end
		end

		if var_37_5 then
			var_37_3.model = var_37_5
		end

		arg_36_0.slotDict[var_37_1] = var_37_3
	end)
end

function var_0_0.InitContact(arg_39_0)
	eachChild(arg_39_0.contactRoot, function(arg_40_0)
		local var_40_0 = arg_40_0:Find("Selector")

		GetOrAddComponent(var_40_0, typeof(EventTriggerListener)):AddPointClickFunc(function(arg_41_0, arg_41_1)
			arg_39_0.baseView:SendNodeCanvasEvent("ClickContact", tf(arg_41_0).parent.name)
		end)
		setActive(arg_40_0, false)
	end)
end

function var_0_0.ActiveContact(arg_42_0, arg_42_1)
	warning("ActiveContact", PrintTable(arg_42_1))
	eachChild(arg_42_0.contactRoot, function(arg_43_0)
		local var_43_0 = arg_43_0.name

		warning(var_43_0)
		setActive(arg_43_0, tobool(arg_42_1[var_43_0]))

		if arg_42_0.baseView.rtFloatPage:Find(var_43_0) then
			setActive(arg_42_0.baseView.rtFloatPage:Find(var_43_0), tobool(arg_42_1[var_43_0]))
		elseif tobool(arg_42_1[var_43_0]) then
			cloneTplTo(arg_42_0.baseView.tplFloat, arg_42_0.baseView.rtFloatPage, var_43_0)
		end
	end)
end

function var_0_0.UpdateContactPosition(arg_44_0, arg_44_1)
	if not arg_44_1 then
		return
	end

	for iter_44_0, iter_44_1 in pairs(arg_44_1) do
		local var_44_0 = arg_44_0.baseView.rtFloatPage:Find(iter_44_0)

		if var_44_0 then
			local var_44_1 = arg_44_0:GetScreenPosition(arg_44_0.contactRoot:Find(iter_44_0)) or Vector2.New(-10000, -10000)

			setAnchoredPosition(var_44_0, var_44_1)
		else
			warning("without this contact colliders:" .. iter_44_0)
		end
	end
end

function var_0_0.InitTimeline(arg_45_0)
	return
end

function var_0_0.LoadCharacter(arg_46_0, arg_46_1)
	PoolMgr.GetInstance():GetPrefab("dorm3d/character/" .. arg_46_0.assetRootName .. "/prefabs/" .. arg_46_0.modelName, "", true, function(arg_47_0)
		arg_46_0.ladyGameobject = arg_47_0

		existCall(arg_46_1)
	end)
end

function var_0_0.InitCharacter(arg_48_0)
	arg_48_0.lady = arg_48_0.ladyGameobject.transform

	arg_48_0.lady:SetParent(arg_48_0.mainCameraTF)
	arg_48_0.lady:SetParent(nil)

	local var_48_0 = arg_48_0.furnitures:Find(arg_48_0.contextData.charFurnitureName or arg_48_0.contextData.inFurnitureName)

	arg_48_0.contextData.charFurnitureName = nil
	arg_48_0.lady.position = var_48_0:Find("StayPoint").position
	arg_48_0.lady.rotation = var_48_0:Find("StayPoint").rotation
	arg_48_0.ladyAgent = arg_48_0.lady:GetComponent(typeof(UnityEngine.AI.NavMeshAgent))
	arg_48_0.ladyAgent.autoRepath = true
	arg_48_0.ladyHeadIKComp = arg_48_0.lady:GetComponent(typeof(HeadAimIK))
	arg_48_0.ladyHeadIKComp.AimTarget = arg_48_0.mainCameraTF:Find("AimTarget")
	arg_48_0.ladyHeadIKData = {
		DampTime = arg_48_0.ladyHeadIKComp.DampTime,
		blinkSpeed = arg_48_0.ladyHeadIKComp.blinkSpeed
	}
	arg_48_0.ladyAnimator = arg_48_0.lady:GetComponent(typeof(Animator))

	local var_48_1 = arg_48_0.lady:GetComponentsInChildren(typeof(Transform))

	table.IpairsCArray(var_48_1, function(arg_49_0, arg_49_1)
		if arg_49_1.name == "BodyCollider" then
			arg_48_0.ladyCollider = arg_49_1
		elseif arg_49_1.name == "Interest" then
			arg_48_0.ladyInterestRoot = arg_49_1
		end
	end)

	arg_48_0.ladyColliders = {}
	arg_48_0.ladyTouchColliders = {}

	table.IpairsCArray(arg_48_0.lady:GetComponentsInChildren(typeof(UnityEngine.Collider)), function(arg_50_0, arg_50_1)
		arg_50_1 = tf(arg_50_1)

		local var_50_0 = arg_50_1.name
		local var_50_1 = var_50_0 and string.find(var_50_0, "Collider") or -1

		if var_50_1 <= 0 then
			errorMsg("Wrong Name to lady Collider : " .. var_50_0)

			return
		end

		local var_50_2 = string.sub(var_50_0, 1, var_50_1 - 1)

		arg_48_0.ladyColliders[var_50_2] = arg_50_1

		if var_50_2 ~= "Body" then
			table.insert(arg_48_0.ladyTouchColliders, arg_50_1)
			setActive(arg_50_1, false)
		end
	end)

	arg_48_0.cameraAim2.LookAt = arg_48_0.ladyInterestRoot
	arg_48_0.cameraTalk.Follow = arg_48_0.ladyInterestRoot
	arg_48_0.cameraTalk.LookAt = arg_48_0.ladyInterestRoot
	arg_48_0.cameraGift.Follow = arg_48_0.ladyInterestRoot
	arg_48_0.cameraGift.LookAt = arg_48_0.ladyInterestRoot
	arg_48_0.cameraRole2.LookAt = arg_48_0.ladyInterestRoot
	arg_48_0.cameraPhoto.Follow = arg_48_0.ladyInterestRoot
	arg_48_0.cameraPhoto.LookAt = arg_48_0.ladyInterestRoot
end

function var_0_0.RemoveCharacter(arg_51_0)
	PoolMgr.GetInstance():ReturnPrefab("dorm3d/character/" .. arg_51_0.assetRootName .. "/prefabs/" .. arg_51_0.modelName, "", arg_51_0.ladyGameobject, true)
end

function var_0_0.didEnter(arg_52_0)
	GetComponent(arg_52_0.lady, typeof(EventTriggerListener)):AddPointClickFunc(function(arg_53_0, arg_53_1)
		if arg_53_1.rawPointerPress.transform == arg_52_0.ladyCollider then
			arg_52_0.baseView:SendNodeCanvasEvent("ClickCharacter", arg_52_0.lady)
		else
			local var_53_0 = table.keyof(arg_52_0.ladyColliders, arg_53_1.rawPointerPress.transform)

			warning(arg_53_1.rawPointerPress.name, var_53_0)
			arg_52_0:emit(var_0_0.ON_TOUCH_CHARACTER, Dorm3dScene.BONE_TO_TOUCH[var_53_0] or arg_53_1.rawPointerPress.name)
		end
	end)
	eachChild(arg_52_0.furnitures, function(arg_54_0)
		local var_54_0 = GetComponent(arg_54_0, typeof(EventTriggerListener))

		if not var_54_0 then
			return
		end

		var_54_0:AddPointClickFunc(function(arg_55_0, arg_55_1)
			arg_52_0.baseView:SendNodeCanvasEvent("ClickFurniture", arg_55_0.transform)
		end)
	end)

	local var_52_0 = -21.6 / Screen.height

	arg_52_0.joystickDelta = Vector2.zero
	arg_52_0.joystickTimer = FrameTimer.New(function()
		local var_56_0 = arg_52_0.joystickDelta * var_52_0
		local var_56_1 = var_56_0.x
		local var_56_2 = var_56_0.y

		local function var_56_3(arg_57_0, arg_57_1, arg_57_2)
			local var_57_0 = arg_57_0[arg_57_1]

			var_57_0.m_InputAxisValue = arg_57_2
			arg_57_0[arg_57_1] = var_57_0
		end

		if arg_52_0.compPov and go(arg_52_0.compPov).activeInHierarchy then
			var_56_3(arg_52_0.compPov, "m_HorizontalAxis", var_56_1)
			var_56_3(arg_52_0.compPov, "m_VerticalAxis", var_56_2)

			if math.abs(var_56_1) < 0.01 and math.abs(var_56_2) < 0.01 then
				if not arg_52_0.recentTweenId and Time.time > arg_52_0.nextRecentTime then
					arg_52_0:DoRecenter()
				end
			else
				arg_52_0:ResetRecenterTimer()
			end
		else
			arg_52_0:ResetRecenterTimer()
		end

		if arg_52_0.surroudCamera and not arg_52_0.pinchMode then
			var_56_3(arg_52_0.surroudCamera, "m_XAxis", var_56_1)
			var_56_3(arg_52_0.surroudCamera, "m_YAxis", var_56_2)

			if arg_52_0.surroudCamera == arg_52_0.cameraRoleWatch then
				if var_56_1 ~= 0 then
					local var_56_4 = arg_52_0.cameraRoleWatch.m_XAxis

					if not var_56_4.m_Wrap then
						local var_56_5 = var_56_1 * (var_56_4.m_InvertInput and -1 or 1)

						if var_56_5 < 0 and var_56_4.Value - 0.01 < var_56_4.m_MinValue then
							arg_52_0:emit(var_0_0.ON_ROLEWATCH_CAMERA_MAX, var_0_0.CAMERA_MAX_OPERATION.RIGHT)
						elseif var_56_5 > 0 and var_56_4.Value + 0.01 > var_56_4.m_MaxValue then
							arg_52_0:emit(var_0_0.ON_ROLEWATCH_CAMERA_MAX, var_0_0.CAMERA_MAX_OPERATION.LEFT)
						end
					end
				end

				if var_56_2 ~= 0 then
					local var_56_6 = arg_52_0.cameraRoleWatch.m_YAxis

					if not var_56_6.m_Wrap then
						if var_56_2 < 0 and var_56_6.Value - 0.01 < var_56_6.m_MinValue then
							arg_52_0:emit(var_0_0.ON_ROLEWATCH_CAMERA_MAX, var_0_0.CAMERA_MAX_OPERATION.DOWN)
						elseif var_56_2 > 0 and var_56_6.Value + 0.01 > var_56_6.m_MaxValue then
							arg_52_0:emit(var_0_0.ON_ROLEWATCH_CAMERA_MAX, var_0_0.CAMERA_MAX_OPERATION.UP)
						end
					end
				end
			end
		end

		arg_52_0.joystickDelta = Vector2.zero
	end, 1, -1)

	arg_52_0.joystickTimer:Start()

	arg_52_0.pinchMode = false
	arg_52_0.pinchSize = 0
	arg_52_0.pinchValue = 1
	arg_52_0.pinchNodeOrder = 1

	local var_52_1 = 0.5
	local var_52_2 = 1

	GlobalClickEventMgr.Inst:AddBeginPinchFunc(function(arg_58_0, arg_58_1)
		if not arg_52_0.surroudCamera or not isActive(arg_52_0.surroudCamera) then
			return
		end

		arg_52_0.pinchMode = true
		arg_52_0.pinchSize = (arg_58_0 - arg_58_1):Magnitude()
		arg_52_0.pinchNodeOrder = arg_58_1.x < arg_58_0.x and -1 or 1
	end)

	local var_52_3 = 0.01

	if IsUnityEditor then
		var_52_3 = 0.1
	end

	local var_52_4 = var_52_3 * 1080 / Screen.height

	GlobalClickEventMgr.Inst:AddPinchFunc(function(arg_59_0, arg_59_1)
		if not arg_52_0.pinchMode then
			return
		end

		local var_59_0 = (arg_59_0 - arg_59_1):Magnitude()
		local var_59_1 = arg_52_0.pinchSize - var_59_0
		local var_59_2 = arg_52_0.pinchNodeOrder * (arg_59_1.x < arg_59_0.x and -1 or 1)
		local var_59_3 = var_59_1 * var_52_4 * var_59_2

		arg_52_0:SetPinchValue(math.clamp(arg_52_0.pinchValue + var_59_3, var_52_1, var_52_2))

		arg_52_0.pinchSize = var_59_0

		if arg_52_0.surroudCamera == arg_52_0.cameraRoleWatch then
			if var_59_3 > 0.01 and arg_52_0.pinchValue == var_52_2 then
				arg_52_0:emit(var_0_0.ON_ROLEWATCH_CAMERA_MAX, var_0_0.CAMERA_MAX_OPERATION.ZOOMOUT)
			elseif var_59_3 < -0.01 and arg_52_0.pinchValue == var_52_1 then
				arg_52_0:emit(var_0_0.ON_ROLEWATCH_CAMERA_MAX, var_0_0.CAMERA_MAX_OPERATION.ZOOMIN)
			end
		end
	end)
	GlobalClickEventMgr.Inst:AddEndPinchFunc(function()
		arg_52_0.pinchMode = false
		arg_52_0.pinchSize = 0
	end)
	arg_52_0.ladyAnimator:GetComponent("DftAniEvent"):SetCommonEvent(function(arg_61_0)
		if arg_52_0.nowState and arg_61_0.animatorStateInfo:IsName(arg_52_0.nowState) then
			existCall(arg_52_0.stateCallback)
		elseif arg_61_0.stringParameter ~= "" then
			arg_52_0:OnAnimationEnd(arg_61_0)
		end
	end)

	arg_52_0.animCallbacks = {}
	arg_52_0.cameraBlendCallbacks = {}

	function arg_52_0.camBrainEvenetHandler.OnBlendFinished(arg_62_0)
		arg_52_0:OnCameraBlendFinished(arg_62_0)
	end

	pg.UIMgr.GetInstance():OverlayPanel(arg_52_0.blockLayer, {
		weight = LayerWeightConst.SECOND_LAYER,
		groupName = LayerWeightConst.GROUP_DORM3D
	})
	arg_52_0:OnSwitchStaticPosition()

	arg_52_0.nextRecentTime = 0

	arg_52_0:RefreshSlots(arg_52_0.apartment)
	arg_52_0.baseView:TreeStart()
end

function var_0_0.OnStickMove(arg_63_0, arg_63_1)
	arg_63_0.joystickDelta = arg_63_1
end

function var_0_0.SetPinchValue(arg_64_0, arg_64_1)
	arg_64_0.pinchValue = arg_64_1

	arg_64_0:SetCameraObrits()
end

function var_0_0.ShowBaseView(arg_65_0)
	setActive(arg_65_0.contactRoot, false)
	arg_65_0.baseView:TempHideUI(false)
end

function var_0_0.HideBaseView(arg_66_0)
	setActive(arg_66_0.contactRoot, true)
	arg_66_0.baseView:TempHideUI(true)
end

function var_0_0.RefreshSlots(arg_67_0, arg_67_1)
	local var_67_0 = arg_67_1:GetSlots()
	local var_67_1 = arg_67_1:GetFurnitures()

	arg_67_0:emit(Dorm3dScene.SHOW_BLOCK)
	table.ParallelIpairsAsync(var_67_0, function(arg_68_0, arg_68_1, arg_68_2)
		local var_68_0 = arg_68_1:GetConfigID()
		local var_68_1 = _.detect(var_67_1, function(arg_69_0)
			return arg_69_0:GetSlotID() == var_68_0
		end)
		local var_68_2 = var_68_1 and var_68_1:GetModel() or ""

		if arg_67_0.slotDict[var_68_0].displayModelName == var_68_2 then
			arg_68_2()

			return
		end

		local var_68_3 = arg_67_0.slotDict[var_68_0].model

		arg_67_0.slotDict[var_68_0].displayModelName = var_68_2

		if not var_68_2 or var_68_2 == "" then
			arg_67_0.loader:ClearRequest("slot_" .. var_68_0)

			if var_68_3 then
				setActive(var_68_3, true)
			end

			arg_68_2()

			return
		end

		local var_68_4 = arg_67_0.slotDict[var_68_0].trans

		arg_67_0.loader:GetPrefab("dorm3d/furniture/prefabs/" .. var_68_2, "", function(arg_70_0)
			arg_68_2()
			assert(arg_70_0)
			setParent(arg_70_0, var_68_4)

			if var_68_3 then
				local var_70_0 = arg_70_0:GetComponentsInChildren(typeof(Renderer))

				table.IpairsCArray(var_70_0, function(arg_71_0, arg_71_1)
					LuaHelper.CopyLightMap(arg_71_1.gameObject, arg_70_0)
				end)
				setActive(var_68_3, false)
			end
		end, "slot_" .. var_68_0)
	end, function()
		arg_67_0:emit(Dorm3dScene.HIDE_BLOCK)
	end)
end

function var_0_0.SyncInterestTransform(arg_73_0)
	arg_73_0.ladyInterest.position = arg_73_0.ladyInterestRoot.position
	arg_73_0.ladyInterest.rotation = arg_73_0.ladyInterestRoot.rotation
end

function var_0_0.OnSwitchStaticPosition(arg_74_0, arg_74_1)
	arg_74_0.baseView:SetInFurniture(arg_74_0.inFurniture)

	local var_74_0 = GetComponent(arg_74_0.inFurniture, typeof(UnityEngine.Collider))

	if var_74_0 then
		var_74_0.enabled = false
	end

	local var_74_1 = arg_74_0.inFurniture
	local var_74_2 = var_74_1:Find("FreeLook Camera")

	arg_74_0:SyncInterestTransform()

	local var_74_3 = var_74_2.transform.position

	var_74_3.y = 0
	arg_74_0.player.position = var_74_3

	if arg_74_0.cameraFree then
		setActive(arg_74_0.cameraFree, false)

		arg_74_0.cameras[var_0_0.CAMERA.FURNITURE_FREELOOK] = nil
	end

	arg_74_0.cameraFree = var_74_1:Find("FreeLook Camera"):GetComponent(typeof(Cinemachine.CinemachineVirtualCamera))
	arg_74_0.compPov = arg_74_0.cameraFree:GetCinemachineComponent(Cinemachine.CinemachineCore.Stage.Aim)
	arg_74_0.cameras[var_0_0.CAMERA.FURNITURE_FREELOOK] = arg_74_0.cameraFree

	if arg_74_0.cameraRoleWatch then
		arg_74_0:RevertCameraOrbit()
	end

	arg_74_0.cameraRoleWatch = var_74_1:Find("RoleWatch Camera"):GetComponent(typeof(Cinemachine.CinemachineFreeLook))
	arg_74_0.cameras[var_0_0.CAMERA.ROLE_WATCH] = arg_74_0.cameraRoleWatch

	arg_74_0:RegisterOrbits(arg_74_0.cameraRoleWatch)

	local var_74_4 = arg_74_0.ladyInterest.position - var_74_2.transform.position
	local var_74_5 = Quaternion.LookRotation(var_74_4).eulerAngles
	local var_74_6 = var_74_5.y
	local var_74_7 = var_74_5.x
	local var_74_8 = arg_74_0.compPov.m_HorizontalAxis

	var_74_8.Value = arg_74_0:GetNearestAngle(var_74_6, var_74_8.m_MinValue, var_74_8.m_MaxValue)
	arg_74_0.compPov.m_HorizontalAxis = var_74_8

	local var_74_9 = arg_74_0.compPov.m_VerticalAxis

	var_74_9.Value = var_74_7
	arg_74_0.compPov.m_VerticalAxis = var_74_9

	arg_74_0:ResetRecenterTimer()
	arg_74_0:RegisterCameraBlendFinished(arg_74_0.cameraFree, arg_74_1)
	arg_74_0:ActiveCamera(arg_74_0.cameraFree)
end

function var_0_0.GetAttachedFurnitureName(arg_75_0)
	return arg_75_0.inFurniture.name
end

function var_0_0.GetFurnitureByName(arg_76_0, arg_76_1)
	return underscore.detect(arg_76_0.attachedPoints, function(arg_77_0)
		return arg_77_0.name == arg_76_1
	end)
end

function var_0_0.GetSlotByID(arg_78_0, arg_78_1)
	return arg_78_0.displaySlots[arg_78_1] and arg_78_0.displaySlots[arg_78_1].trans
end

function var_0_0.GetScreenPosition(arg_79_0, arg_79_1)
	local var_79_0 = arg_79_0.mainCameraTF:Find("CameraForRaycast"):GetComponent(typeof(Camera)):WorldToScreenPoint(arg_79_1.position)

	if var_79_0.z < 0 then
		return false
	end

	local var_79_1 = pg.UIMgr.GetInstance().uiCamera:Find("Canvas").rect

	return (Vector2.New(var_79_0.x / Screen.width * var_79_1.width, var_79_0.y / Screen.height * var_79_1.height))
end

function var_0_0.GetModelRoot(arg_80_0)
	return arg_80_0.modelRoot
end

function var_0_0.PlayerMove(arg_81_0, arg_81_1, arg_81_2)
	local var_81_0 = arg_81_0:GetFurnitureByName(arg_81_1)

	if not var_81_0 then
		errorMsg(arg_81_1 .. " Not Find")
		existCall(arg_81_2)

		return
	end

	if var_81_0 == arg_81_0.inFurniture then
		existCall(arg_81_2)

		return
	end

	local var_81_1 = arg_81_0.inFurniture
	local var_81_2 = var_81_1:Find("FreeLook Camera")
	local var_81_3 = _.detect(arg_81_0.apartment:GetZones(), function(arg_82_0)
		return arg_82_0:GetWatchCameraName() == var_81_1.name
	end)
	local var_81_4 = _.detect(arg_81_0.apartment:GetZones(), function(arg_83_0)
		return arg_83_0:GetWatchCameraName() == arg_81_1
	end)
	local var_81_5 = table.indexof(arg_81_0.attachedPoints, arg_81_0.inFurniture)
	local var_81_6 = table.indexof(arg_81_0.attachedPoints, var_81_0)
	local var_81_7 = false

	if var_81_6 < var_81_5 then
		var_81_7 = true
		var_81_5, var_81_6 = var_81_6, var_81_5
	end

	local var_81_8 = "Dolly" .. var_81_5 .. "_" .. var_81_6
	local var_81_9 = arg_81_0.dollyParent:Find(var_81_8):GetComponent(typeof(Cinemachine.CinemachineSmoothPath))

	arg_81_0.compDolly.m_Path = var_81_9

	local var_81_10 = GetComponent(arg_81_0.inFurniture, typeof(UnityEngine.Collider))

	if var_81_10 then
		var_81_10.enabled = true
	end

	local var_81_11 = var_81_0:Find("Interest")
	local var_81_12 = var_81_0:Find("StayPoint")

	seriesAsync({
		function(arg_84_0)
			arg_81_0:emit(Dorm3dScene.SHOW_BLOCK)

			arg_81_0.cameraAim.transform.position = var_81_2.transform.position
			arg_81_0.cameraAim2.transform.position = var_81_2.transform.position

			arg_81_0:ActiveCamera(arg_81_0.cameraAim2)
			arg_84_0()
		end,
		function(arg_85_0)
			local var_85_0 = arg_81_0.ladyAgent

			var_85_0.enabled = true
			var_85_0.destination = var_81_12.position
			var_85_0.speed = 0
			arg_81_0.moveTimer = waitUntil(function()
				arg_81_0:WalkByRootMotionLoop(var_85_0, arg_81_0.ladyAnimator)

				return var_85_0.remainingDistance < 0.1
			end, function()
				var_85_0.enabled = false

				arg_85_0()
			end)
		end,
		function(arg_88_0)
			local var_88_0 = arg_81_0.lady.rotation
			local var_88_1 = var_81_12.rotation:ToEulerAngles().y - var_88_0:ToEulerAngles().y

			if var_88_1 < -180 then
				var_88_1 = var_88_1 + 360
			elseif var_88_1 > 180 then
				var_88_1 = var_88_1 - 360
			end

			arg_81_0.ladyAnimator:SetFloat("Speed", 0)
			arg_81_0.ladyAnimator:SetBool("Turn", true)
			arg_81_0.ladyAnimator:SetFloat("TurnAngle", var_88_1)
			arg_81_0:RegisterCallback("TurnEnd", function()
				arg_81_0.ladyAnimator:SetFloat("TurnAngle", 0)
				arg_81_0.ladyAnimator:SetBool("Turn", false)
				arg_88_0()
			end)
		end,
		function(arg_90_0)
			arg_81_0:ActiveCamera(arg_81_0.cameraAim)

			arg_81_0.cameraAim.LookAt = var_81_11

			local var_90_0 = 1
			local var_90_1 = arg_81_0.compDolly.m_Path.PathLength
			local var_90_2 = var_90_1 / var_90_0

			arg_81_0:managedTween(LeanTween.value, arg_90_0, go(arg_81_0.cameraAim), 0, 1, var_90_2):setOnUpdate(System.Action_float(function(arg_91_0)
				local var_91_0 = var_81_7 and 1 - arg_91_0 or arg_91_0

				arg_81_0.compDolly.m_PathPosition = var_90_1 * var_91_0
			end))
		end,
		function(arg_92_0)
			arg_81_0.inFurniture = var_81_0
			arg_81_0.contextData.inFurnitureName = var_81_0.name

			arg_81_0:OnSwitchStaticPosition(arg_92_0)
		end,
		function(arg_93_0)
			arg_81_0:emit(Dorm3dScene.HIDE_BLOCK)
			arg_93_0()
		end
	}, arg_81_2)
end

function var_0_0.WalkByRootMotionLoop(arg_94_0, arg_94_1, arg_94_2)
	if arg_94_1.pathPending then
		arg_94_2:SetFloat("Speed", 0)

		return
	end

	arg_94_2:SetFloat("Speed", 1)

	local var_94_0 = arg_94_1.path.corners

	if var_94_0.Length > 1 then
		local var_94_1 = var_94_0[1] - arg_94_1.transform.position

		var_94_1.y = 0

		local var_94_2 = Quaternion.LookRotation(var_94_1)
		local var_94_3 = arg_94_1.transform.rotation
		local var_94_4 = 1
		local var_94_5 = Damp(1, var_94_4, Time.deltaTime)

		arg_94_1.transform.rotation = Quaternion.Lerp(var_94_3, var_94_2, var_94_5)
	end
end

function var_0_0.ActiveCamera(arg_95_0, arg_95_1)
	table.Foreach(arg_95_0.cameras, function(arg_96_0, arg_96_1)
		setActive(arg_96_1, arg_96_1 == arg_95_1)
	end)
end

function var_0_0.ShowBlackScreen(arg_97_0, arg_97_1, arg_97_2)
	local var_97_0 = 0.3

	seriesAsync({
		function(arg_98_0)
			setActive(arg_97_0.blackLayer, true)
			arg_97_0:managedTween(LeanTween.alpha, arg_98_0, arg_97_0.blackLayer, 1, var_97_0)
		end,
		function(arg_99_0)
			arg_97_1(arg_99_0)
		end,
		function(arg_100_0)
			arg_97_0:managedTween(LeanTween.alpha, arg_100_0, arg_97_0.blackLayer, 0, var_97_0)
		end,
		function()
			setActive(arg_97_0.blackLayer, false)
			existCall(arg_97_2)
		end
	})
end

function var_0_0.RegisterOrbits(arg_102_0, arg_102_1)
	arg_102_0.orbits = {
		original = arg_102_1.m_Orbits
	}
	arg_102_0.orbits.current = _.range(3):map(function(arg_103_0)
		local var_103_0 = arg_102_0.orbits.original[arg_103_0 - 1]

		return Cinemachine.CinemachineFreeLook.Orbit.New(var_103_0.m_Height, var_103_0.m_Radius)
	end)
	arg_102_0.surroudCamera = arg_102_1
end

function var_0_0.SetCameraObrits(arg_104_0)
	local var_104_0 = arg_104_0.surroudCamera

	if not var_104_0 then
		return
	end

	local var_104_1 = arg_104_0.orbits.original[1]

	for iter_104_0 = 0, #arg_104_0.orbits.current - 1 do
		local var_104_2 = arg_104_0.orbits.current[iter_104_0 + 1]
		local var_104_3 = arg_104_0.orbits.original[iter_104_0]

		var_104_2.m_Height = math.lerp(var_104_1.m_Height, var_104_3.m_Height, arg_104_0.pinchValue)
		var_104_2.m_Radius = var_104_3.m_Radius * arg_104_0.pinchValue
	end

	var_104_0.m_Orbits = arg_104_0.orbits.current
end

function var_0_0.RevertCameraOrbit(arg_105_0)
	local var_105_0 = arg_105_0.surroudCamera

	if not var_105_0 then
		return
	end

	for iter_105_0 = 0, #arg_105_0.orbits.current - 1 do
		local var_105_1 = arg_105_0.orbits.current[iter_105_0 + 1]
		local var_105_2 = arg_105_0.orbits.original[iter_105_0]

		var_105_1.m_Height = var_105_2.m_Height
		var_105_1.m_Radius = var_105_2.m_Radius
	end

	var_105_0.m_Orbits = arg_105_0.orbits.current
	arg_105_0.surroudCamera = nil
end

function var_0_0.EnterWatchMode(arg_106_0)
	arg_106_0:emit(Dorm3dScene.SHOW_BLOCK)
	arg_106_0.baseView:EnableJoystick(false)
	arg_106_0:ResetRecenterTimer()
	arg_106_0:DoRecenterQuick(function()
		seriesAsync({
			function(arg_108_0)
				arg_106_0:RegisterCameraBlendFinished(arg_106_0.cameraRole, arg_108_0)
				arg_106_0:ActiveCamera(arg_106_0.cameraRole)
			end
		}, function()
			arg_106_0.baseView:EnterWatchMode()
			arg_106_0:emit(Dorm3dScene.HIDE_BLOCK)
		end)
	end)
end

function var_0_0.ExitWatchMode(arg_110_0)
	arg_110_0:emit(Dorm3dScene.SHOW_BLOCK)
	arg_110_0.baseView:ExitWatchMode()
	seriesAsync({
		function(arg_111_0)
			arg_110_0:ResetRecenterTimer()
			arg_110_0:RegisterCameraBlendFinished(arg_110_0.cameraFree, arg_111_0)
			arg_110_0:ActiveCamera(arg_110_0.cameraFree)
		end
	}, function()
		arg_110_0:emit(Dorm3dScene.HIDE_BLOCK)
		arg_110_0.baseView:EnableJoystick(true)
	end)
end

function var_0_0.WatchModeInteractive(arg_113_0)
	if arg_113_0.inFurniture.name ~= "Bed" then
		arg_113_0:PlaySingleAction("Bow")
	end
end

function var_0_0.EnterFreelookMode(arg_114_0, arg_114_1, arg_114_2)
	arg_114_0:emit(Dorm3dScene.SHOW_BLOCK)
	seriesAsync({
		function(arg_115_0)
			if arg_114_2.standby_action and arg_114_2.standby_action ~= "" then
				parallelAsync({
					function(arg_116_0)
						arg_114_0:emit(Dorm3dScene.PLAY_SINGLE_ACTION, arg_114_2.standby_action, arg_116_0)
					end,
					function(arg_117_0)
						arg_114_0.cameras[var_0_0.CAMERA.ROLE2].transform.position = arg_114_0.cameraRole.transform.position

						arg_114_0:ResetRecenterTimer()
						arg_114_0:RegisterCameraBlendFinished(arg_114_0.cameras[var_0_0.CAMERA.ROLE2], arg_117_0)
						arg_114_0:ActiveCamera(arg_114_0.cameras[var_0_0.CAMERA.ROLE2])
					end
				}, arg_115_0)

				return
			end

			arg_115_0()
		end,
		function(arg_118_0)
			arg_114_0:ResetRecenterTimer()

			arg_114_0.pinchValue = 1

			arg_114_0:SetCameraObrits()

			local var_118_0 = arg_114_0.cameraRoleWatch.m_XAxis

			var_118_0.Value = 180
			arg_114_0.cameraRoleWatch.m_XAxis = var_118_0

			local var_118_1 = arg_114_0.cameraRoleWatch.m_YAxis

			var_118_1.Value = 0.7
			arg_114_0.cameraRoleWatch.m_YAxis = var_118_1

			arg_114_0:SyncInterestTransform()
			arg_114_0:RegisterCameraBlendFinished(arg_114_0.cameraRoleWatch, arg_118_0)
			arg_114_0:ActiveCamera(arg_114_0.cameraRoleWatch)
		end,
		function(arg_119_0)
			setActive(arg_114_0.ladyCollider, false)
			_.each(arg_114_0.ladyTouchColliders, function(arg_120_0)
				setActive(arg_120_0, true)
			end)
			arg_119_0()
		end
	}, function()
		arg_114_0:emit(Dorm3dScene.HIDE_BLOCK)
		arg_114_1()
	end)
end

function var_0_0.ExitFreelookMode(arg_122_0, arg_122_1, arg_122_2)
	arg_122_0:emit(Dorm3dScene.SHOW_BLOCK)
	seriesAsync({
		function(arg_123_0)
			setActive(arg_122_0.ladyCollider, true)
			_.each(arg_122_0.ladyTouchColliders, function(arg_124_0)
				setActive(arg_124_0, false)
			end)
			arg_123_0()
		end,
		function(arg_125_0)
			if arg_122_2.finish_action and arg_122_2.finish_action ~= "" then
				parallelAsync({
					function(arg_126_0)
						arg_122_0:emit(Dorm3dScene.PLAY_SINGLE_ACTION, arg_122_2.finish_action, arg_126_0)
					end,
					function(arg_127_0)
						arg_122_0:ResetRecenterTimer()
						arg_122_0:RegisterCameraBlendFinished(arg_122_0.cameras[var_0_0.CAMERA.ROLE2], arg_127_0)
						arg_122_0:ActiveCamera(arg_122_0.cameras[var_0_0.CAMERA.ROLE2])
					end
				}, arg_125_0)

				return
			end

			arg_125_0()
		end,
		function(arg_128_0)
			arg_122_0:SyncInterestTransform()
			arg_122_0:RegisterCameraBlendFinished(arg_122_0.cameraRole, arg_128_0)
			arg_122_0:ActiveCamera(arg_122_0.cameraRole)
		end
	}, function()
		arg_122_0:emit(Dorm3dScene.HIDE_BLOCK)
		arg_122_1()
	end)
end

function var_0_0.EnableHeadIK(arg_130_0, arg_130_1)
	arg_130_0.ladyHeadIKComp.enableIk = arg_130_1
end

function var_0_0.HideCharacter(arg_131_0)
	arg_131_0.lastCharacterPosition = arg_131_0.lady.position

	setLocalPosition(arg_131_0.lady, Vector3(0, -10000, 0))
end

function var_0_0.RevertCharacter(arg_132_0)
	setLocalPosition(arg_132_0.lady, arg_132_0.lastCharacterPosition or Vector3.zero)
end

function var_0_0.EnterFurnitureWatchMode(arg_133_0)
	arg_133_0:HideCharacter()

	arg_133_0.lastCamera = table.Find(arg_133_0.cameras, function(arg_134_0, arg_134_1)
		return isActive(arg_134_1)
	end)

	eachChild(arg_133_0.furnitures, function(arg_135_0)
		local var_135_0 = arg_135_0:GetComponent(typeof(UnityEngine.Collider))

		if not var_135_0 then
			return
		end

		var_135_0.enabled = false
	end)
end

function var_0_0.ExitFurnitureWatchMode(arg_136_0)
	arg_136_0:HideFurnitureSlots()
	arg_136_0:emit(Dorm3dScene.SHOW_BLOCK)
	arg_136_0:ShowBlackScreen(function(arg_137_0)
		arg_136_0:RegisterCameraBlendFinished(arg_136_0.lastCamera, arg_137_0)
		arg_136_0:ActiveCamera(arg_136_0.lastCamera)
	end, function()
		arg_136_0.lastCamera = nil

		arg_136_0:emit(Dorm3dScene.HIDE_BLOCK)
	end)
	eachChild(arg_136_0.furnitures, function(arg_139_0)
		local var_139_0 = arg_139_0:GetComponent(typeof(UnityEngine.Collider))

		if not var_139_0 then
			return
		end

		var_139_0.enabled = true
	end)
	arg_136_0:RefreshSlots(arg_136_0.apartment)
end

function var_0_0.EnterGiftMode(arg_140_0)
	arg_140_0:emit(Dorm3dScene.SHOW_BLOCK)
	arg_140_0:RegisterCameraBlendFinished(arg_140_0.cameras[var_0_0.CAMERA.GIFT], function()
		arg_140_0:emit(Dorm3dScene.HIDE_BLOCK)
	end)
	arg_140_0:ActiveCamera(arg_140_0.cameras[var_0_0.CAMERA.GIFT])
end

function var_0_0.ExitGiftMode(arg_142_0)
	arg_142_0:emit(Dorm3dScene.SHOW_BLOCK)
	arg_142_0:RegisterCameraBlendFinished(arg_142_0.cameras[var_0_0.CAMERA.ROLE], function()
		arg_142_0:emit(Dorm3dScene.HIDE_BLOCK)
	end)
	arg_142_0:ActiveCamera(arg_142_0.cameras[var_0_0.CAMERA.ROLE])
end

function var_0_0.SwitchZone(arg_144_0, arg_144_1, arg_144_2)
	local var_144_0 = arg_144_0:GetFurnitureByName(arg_144_1:GetWatchCameraName()):Find("FurnitureWatch Camera"):GetComponent(typeof(Cinemachine.CinemachineVirtualCamera))

	if arg_144_0.cameraFurnitureWatch and arg_144_0.cameraFurnitureWatch ~= var_144_0 then
		arg_144_0:UnRegisterCameraBlendFinished(arg_144_0.cameraFurnitureWatch)
		setActive(arg_144_0.cameraFurnitureWatch, false)
	end

	arg_144_0.cameraFurnitureWatch = var_144_0
	arg_144_0.cameras[var_0_0.CAMERA.FURNITURE_WATCH] = arg_144_0.cameraFurnitureWatch

	arg_144_0:RegisterCameraBlendFinished(arg_144_0.cameraFurnitureWatch, function()
		arg_144_0:emit(Dorm3dScene.HIDE_BLOCK)
		existCall(arg_144_2)
	end)
	arg_144_0:emit(Dorm3dScene.SHOW_BLOCK)
	arg_144_0:ActiveCamera(arg_144_0.cameraFurnitureWatch)
end

function var_0_0.HideFurnitureSlots(arg_146_0)
	if arg_146_0.displaySlots then
		arg_146_0:UpdateDisplaySlots({})
		table.Foreach(arg_146_0.displaySlots, function(arg_147_0, arg_147_1)
			local var_147_0 = arg_147_1.trans

			if IsNil(var_147_0:Find("Selector")) then
				return
			end

			setActive(var_147_0:Find("Selector"), false)
		end)

		arg_146_0.displaySlots = nil
	end
end

function var_0_0.DisplayFurnitureSlots(arg_148_0, arg_148_1)
	arg_148_0:HideFurnitureSlots()

	arg_148_0.displaySlots = {}

	_.each(arg_148_1, function(arg_149_0)
		arg_148_0.displaySlots[arg_149_0] = arg_148_0.slotDict[arg_149_0]

		if not arg_148_0.displaySlots[arg_149_0] then
			errorMsg("Slot " .. arg_149_0 .. " Not Binding Scene Object")

			return
		end

		local var_149_0 = arg_148_0.displaySlots[arg_149_0].trans

		if var_149_0:Find("Selector") then
			setActive(var_149_0:Find("Selector"), true)
		end
	end)
end

function var_0_0.UpdateDisplaySlots(arg_150_0, arg_150_1)
	table.Foreach(arg_150_0.displaySlots, function(arg_151_0, arg_151_1)
		local var_151_0 = arg_151_1.trans

		if not IsNil(var_151_0:Find("Selector")) then
			setActive(var_151_0:Find("Selector/Normal"), arg_150_1[arg_151_0] == 0)
			setActive(var_151_0:Find("Selector/Active"), arg_150_1[arg_151_0] == 1)
			setActive(var_151_0:Find("Selector/Ban"), arg_150_1[arg_151_0] == 2)
		end

		local var_151_1 = arg_150_0.slotDict[arg_151_0].model
		local var_151_2 = arg_150_0.slotDict[arg_151_0].displayModelName

		if var_151_2 and var_151_2 ~= "" then
			var_151_1 = var_151_0:GetChild(var_151_0.childCount - 1)
		end

		local function var_151_3(arg_152_0, arg_152_1)
			local var_152_0 = arg_152_0:GetComponentsInChildren(typeof(Renderer))

			table.IpairsCArray(var_152_0, function(arg_153_0, arg_153_1)
				local var_153_0 = arg_153_1.material

				if var_153_0 and var_153_0:HasProperty("_FinalTint") then
					var_153_0:SetColor("_FinalTint", arg_152_1)
				end
			end)
		end

		if var_151_1 then
			if arg_150_1[arg_151_0] == 1 then
				var_151_3(var_151_1, Color.NewHex("3F83AE73"))
			else
				var_151_3(var_151_1, Color.New(0, 0, 0, 0))
			end
		end
	end)
end

function var_0_0.EnterPhotoMode(arg_154_0, arg_154_1)
	arg_154_0.lastCamera = table.Find(arg_154_0.cameras, function(arg_155_0, arg_155_1)
		return isActive(arg_155_1)
	end)

	arg_154_0:ShowBlackScreen(function(arg_156_0)
		arg_154_0:SwitchAnim(var_0_0.ANIM.IDLE)
		onNextTick(function()
			arg_154_0:ResetCharPosByZone(arg_154_1)
			arg_154_0:SyncInterestTransform()
		end)

		local var_156_0 = arg_154_0.cameraPhoto
		local var_156_1 = var_156_0.m_XAxis

		var_156_1.Value = 180
		var_156_0.m_XAxis = var_156_1

		local var_156_2 = var_156_0.m_YAxis

		var_156_2.Value = 0.7
		var_156_0.m_YAxis = var_156_2

		arg_154_0:RegisterOrbits(arg_154_0.cameraPhoto)

		arg_154_0.pinchValue = 1

		arg_154_0:SetCameraObrits()
		arg_154_0:RegisterCameraBlendFinished(var_156_0, arg_156_0)
		arg_154_0:ActiveCamera(var_156_0)
	end)
end

function var_0_0.ExitPhotoMode(arg_158_0)
	arg_158_0:emit(Dorm3dScene.SHOW_BLOCK)
	arg_158_0:ShowBlackScreen(function(arg_159_0)
		arg_158_0:RevertCameraOrbit()
		arg_158_0:SwitchAnim(var_0_0.ANIM.IDLE)
		onNextTick(function()
			local var_160_0 = arg_158_0.inFurniture:Find("StayPoint")

			arg_158_0.lady.position = var_160_0.position
			arg_158_0.lady.rotation = var_160_0.rotation

			arg_158_0:SyncInterestTransform()
		end)
		arg_158_0:RegisterCameraBlendFinished(arg_158_0.lastCamera, arg_159_0)
		arg_158_0:ActiveCamera(arg_158_0.lastCamera)
	end, function()
		arg_158_0.lastCamera = nil

		arg_158_0:RefreshSlots(arg_158_0.apartment)
		arg_158_0:emit(Dorm3dScene.HIDE_BLOCK)
	end)
end

function var_0_0.SwitchCameraZone(arg_162_0, arg_162_1, arg_162_2)
	arg_162_0:emit(var_0_0.SHOW_BLOCK)
	arg_162_0:ShowBlackScreen(function(arg_163_0)
		arg_162_0:SwitchAnim(var_0_0.ANIM.IDLE)
		onNextTick(function()
			arg_162_0:ResetCharPosByZone(arg_162_1)
			arg_162_0:SyncInterestTransform()
			arg_163_0()
		end)
	end, function()
		arg_162_0:emit(var_0_0.HIDE_BLOCK)
		existCall(arg_162_2)
	end)
end

function var_0_0.ResetCharPosByZone(arg_166_0, arg_166_1)
	local var_166_0 = arg_166_0:GetFurnitureByName(arg_166_1:GetWatchCameraName()):Find("StayPoint")

	arg_166_0.lady.position = var_166_0.position
	arg_166_0.lady.rotation = var_166_0.rotation
end

function var_0_0.GetNearestAngle(arg_167_0, arg_167_1, arg_167_2, arg_167_3)
	if arg_167_3 < arg_167_2 then
		arg_167_3 = arg_167_3 + 360
	end

	if arg_167_2 <= arg_167_1 and arg_167_1 <= arg_167_3 then
		return arg_167_1
	end

	local var_167_0 = (arg_167_2 + arg_167_3) / 2

	arg_167_1 = var_167_0 - Mathf.DeltaAngle(arg_167_1, var_167_0)
	arg_167_1 = math.clamp(arg_167_1, arg_167_2, arg_167_3)

	return arg_167_1
end

function var_0_0.PlayTimeline(arg_168_0, arg_168_1, arg_168_2)
	local var_168_0 = {}
	local var_168_1 = arg_168_1.name

	seriesAsync({
		function(arg_169_0)
			pg.UIMgr.GetInstance():LoadingOn(false)
			arg_169_0()
		end,
		function(arg_170_0)
			arg_168_0:LoadSceneAsync(string.lower("dorm3d/character/" .. arg_168_0.assetRootName .. "/timeline/" .. var_168_1 .. "/" .. var_168_1 .. "_scene"), var_168_1, function(arg_171_0, arg_171_1)
				onNextTick(arg_170_0)
			end)
		end,
		function(arg_172_0)
			if not arg_168_1.scene then
				return arg_172_0()
			end

			seriesAsync({
				function(arg_173_0)
					local var_173_0 = arg_168_1.scene
					local var_173_1 = arg_168_1.sceneRoot

					arg_168_0:LoadSceneAsync(string.lower("dorm3d/scenesres/scenes/" .. var_173_1 .. "/" .. var_173_0 .. "_scene"), var_173_0, function(arg_174_0, arg_174_1)
						local var_174_0 = _.detect(arg_168_0.sceneDataList, function(arg_175_0)
							return arg_175_0.name == var_173_0
						end)

						SceneOpMgr.Inst:SetActiveSceneByIndex(var_174_0.index)
						onNextTick(arg_173_0)
					end)
				end,
				function(arg_176_0)
					arg_168_0:UnloadSceneAsync(string.lower("dorm3d/scenesres/scenes/" .. arg_168_0.sceneRootName .. "/" .. arg_168_0.sceneName .. "_scene"), arg_168_0.sceneName)
					arg_176_0()
				end
			}, arg_172_0)
		end,
		function(arg_177_0)
			pg.UIMgr.GetInstance():LoadingOff()

			arg_168_0.timelineCallback = arg_168_2

			local var_177_0 = GameObject.Find("[sequence]").transform
			local var_177_1 = var_177_0:GetComponent(typeof(UnityEngine.Playables.PlayableDirector))
			local var_177_2 = GameObject.Find("[actor]").transform:GetComponentsInChildren(typeof(Animator))

			table.IpairsCArray(var_177_2, function(arg_178_0, arg_178_1)
				GetOrAddComponent(arg_178_1.transform, typeof(DftAniEvent))
			end)

			if arg_168_1.time then
				var_177_1.time = math.clamp(arg_168_1.time, 0, var_177_1.duration)
			end

			var_177_1:Stop()

			local var_177_3 = {}

			GetOrAddComponent(var_177_0, "DftCommonSignalReceiver"):SetCommonEvent(function(arg_179_0)
				local function var_179_0()
					return
				end

				switch(arg_179_0.stringParameter, {
					TimelinePause = function()
						arg_168_0.timelineSpeed = 0

						setDirectorSpeed(var_177_1, arg_168_0.timelineSpeed)
					end,
					TimelineResume = function()
						arg_168_0.timelineSpeed = 0

						setDirectorSpeed(var_177_1, arg_168_0.timelineSpeed)
					end,
					TimelinePlayOnTime = function()
						if arg_179_0.intParameter == 0 or arg_179_0.intParameter == var_177_3.optionIndex then
							var_177_1.time = arg_179_0.floatParameter
						end
					end,
					TimelineSelectStart = function()
						var_177_3.selectIndex = nil

						if arg_168_1.options then
							arg_168_0.baseView:DoTimelineOption(arg_168_1.options, function(arg_185_0)
								var_177_3.selectIndex = arg_185_0
								var_177_3.optionIndex = arg_168_1.options[arg_185_0].flag
							end)
						end
					end,
					TimelineTouchStart = function()
						var_177_3.selectIndex = nil

						if arg_168_1.touchs then
							arg_168_0.baseView:DoTimelineTouch(arg_168_1.touchs, function(arg_187_0)
								var_177_3.selectIndex = arg_187_0
								var_177_3.optionIndex = arg_168_1.touchs[arg_187_0].flag
							end)
						end
					end,
					TimelineSelectLoop = function()
						if not var_177_3.selectIndex then
							var_177_1.time = arg_179_0.floatParameter
						end
					end,
					TimelineEnd = function()
						var_177_3.finish = true

						var_177_1:Pause()
					end
				}, function()
					warning("other event trigger:" .. arg_179_0.stringParameter)
				end)

				if var_177_3.finish then
					seriesAsync({
						function(arg_191_0)
							if not arg_168_1.scene then
								return arg_191_0()
							end

							arg_168_0:LoadSceneAsync(string.lower("dorm3d/scenesres/scenes/" .. arg_168_0.sceneRootName .. "/" .. arg_168_0.sceneName .. "_scene"), arg_168_0.sceneName, function(arg_192_0, arg_192_1)
								local var_192_0 = _.detect(arg_168_0.sceneDataList, function(arg_193_0)
									return arg_193_0.name == arg_168_0.sceneName
								end)

								SceneOpMgr.Inst:SetActiveSceneByIndex(var_192_0.index)

								local var_192_1 = arg_168_1.scene
								local var_192_2 = arg_168_1.sceneRoot

								arg_168_0:UnloadSceneAsync(string.lower("dorm3d/scenesres/scenes/" .. var_192_2 .. "/" .. var_192_1 .. "_scene"), var_192_1)
								arg_191_0()
							end)
						end,
						function(arg_194_0)
							arg_168_0:RevertCharacter()
							setActive(arg_168_0.mainCameraTF, true)
							arg_168_0:UnloadSceneAsync(string.lower("dorm3d/character/scenes/" .. arg_168_0.assetRootName .. "/timeline/" .. var_168_1 .. "/" .. var_168_1 .. "_scene"), var_168_1)
							warning(arg_179_0.stringParameter, arg_168_0.timelineCallback)

							local var_194_0 = arg_168_0.timelineCallback

							arg_168_0.timelineCallback = nil

							existCall(var_194_0, var_177_3)
						end
					})
				end
			end)

			if defaultValue(arg_168_0.timelineSpeed, 1) ~= 1 then
				arg_168_0.timelineSpeed = 1

				setDirectorSpeed(var_177_1, arg_168_0.timelineSpeed)
			end

			arg_168_0:HideCharacter()
			setActive(arg_168_0.mainCameraTF, false)
			var_177_1:Play()
		end
	})
end

function var_0_0.PlaySingleAction(arg_195_0, arg_195_1, arg_195_2)
	local var_195_0 = {}

	warning("Play", arg_195_1)

	if not arg_195_0.ladyAnimator:GetCurrentAnimatorStateInfo(0):IsName(arg_195_1) then
		table.insert(var_195_0, function(arg_196_0)
			arg_195_0.nowState = arg_195_1
			arg_195_0.stateCallback = arg_196_0

			arg_195_0.ladyAnimator:CrossFade(arg_195_1, 0.05)
		end)
		table.insert(var_195_0, function(arg_197_0)
			arg_195_0.nowState = nil
			arg_195_0.stateCallback = nil

			arg_197_0()
		end)
	end

	seriesAsync(var_195_0, arg_195_2)
end

function var_0_0.SwitchAnim(arg_198_0, arg_198_1, arg_198_2)
	local var_198_0 = {}

	warning("Switch", arg_198_1)
	table.insert(var_198_0, function(arg_199_0)
		arg_198_0.nowState = arg_198_1
		arg_198_0.stateCallback = arg_199_0

		arg_198_0.ladyAnimator:Play(arg_198_1, 0, 0)
	end)
	table.insert(var_198_0, function(arg_200_0)
		arg_198_0.nowState = nil
		arg_198_0.stateCallback = nil

		arg_200_0()
	end)
	seriesAsync(var_198_0, arg_198_2)
end

function var_0_0.GetCurrentAnimatorStateInfo(arg_201_0)
	return (arg_201_0.ladyAnimator:GetCurrentAnimatorStateInfo(0))
end

function var_0_0.SetCharacterAnimSpeed(arg_202_0, arg_202_1)
	arg_202_0.ladyAnimator.speed = arg_202_1
	arg_202_0.ladyHeadIKComp.blinkSpeed = arg_202_0.ladyHeadIKData.blinkSpeed * arg_202_1

	if arg_202_1 > 0 then
		arg_202_0.ladyHeadIKComp.DampTime = arg_202_0.ladyHeadIKData.DampTime / arg_202_1
	else
		arg_202_0.ladyHeadIKComp.DampTime = arg_202_0.ladyHeadIKData.DampTime * math.huge
	end
end

function var_0_0.OnAnimationEnd(arg_203_0, arg_203_1)
	if arg_203_1.animatorClipInfo.weight < 0.5 then
		return
	end

	local var_203_0 = arg_203_1.stringParameter
	local var_203_1 = table.removebykey(arg_203_0.animCallbacks, var_203_0)

	existCall(var_203_1)
end

function var_0_0.RegisterCallback(arg_204_0, arg_204_1, arg_204_2)
	arg_204_0.animCallbacks[arg_204_1] = arg_204_2
end

function var_0_0.RegisterCameraBlendFinished(arg_205_0, arg_205_1, arg_205_2)
	arg_205_0.cameraBlendCallbacks[arg_205_1] = arg_205_2
end

function var_0_0.UnRegisterCameraBlendFinished(arg_206_0, arg_206_1)
	arg_206_0.cameraBlendCallbacks[arg_206_1] = nil
end

function var_0_0.OnCameraBlendFinished(arg_207_0, arg_207_1)
	if not arg_207_1 then
		return
	end

	local var_207_0 = table.removebykey(arg_207_0.cameraBlendCallbacks, arg_207_1)

	existCall(var_207_0)
end

function var_0_0.RegisterGlobalVolume(arg_208_0)
	local var_208_0 = arg_208_0.globalVolume
	local var_208_1 = BLHX.PostEffect.Overrides.DepthOfField
	local var_208_2 = LuaHelper.GetOrAddVolumeComponent(var_208_0, typeof(BLHX.PostEffect.Overrides.DepthOfField))
	local var_208_3 = LuaHelper.GetOrAddVolumeComponent(var_208_0, typeof(BLHX.PostEffect.Overrides.ColorGrading))

	arg_208_0.originalCameraSettings = {
		depthOfField = {
			enabeld = var_208_2.enabled.value,
			focusDistance = {
				length = 2,
				min = var_208_2.gaussianStart.min,
				value = var_208_2.gaussianStart.value
			},
			blurRadius = {
				min = var_208_2.blurRadius.min,
				max = var_208_2.blurRadius.max,
				value = var_208_2.blurRadius.value
			}
		},
		postExposure = {
			value = var_208_3.postExposure.value
		},
		contrast = {
			min = var_208_3.contrast.min,
			max = var_208_3.contrast.max,
			value = var_208_3.contrast.value
		},
		saturate = {
			min = var_208_3.saturation.min,
			max = var_208_3.saturation.max,
			value = var_208_3.saturation.value
		}
	}
	arg_208_0.originalCameraSettings.depthOfField.enabeld = true

	local var_208_4 = var_208_0:GetComponent(typeof(BLHX.Volume.Volume))

	arg_208_0.originalVolume = {
		profile = var_208_4.sharedProfile,
		weight = var_208_4.weight
	}
end

function var_0_0.SettingCamera(arg_209_0, arg_209_1)
	arg_209_0.activeCameraSettings = arg_209_1

	local var_209_0 = arg_209_0.globalVolume
	local var_209_1 = LuaHelper.GetOrAddVolumeComponent(var_209_0, typeof(BLHX.PostEffect.Overrides.DepthOfField))
	local var_209_2 = LuaHelper.GetOrAddVolumeComponent(var_209_0, typeof(BLHX.PostEffect.Overrides.ColorGrading))

	var_209_1.enabled:Override(arg_209_1.depthOfField.enabeld)
	var_209_1.gaussianStart:Override(arg_209_1.depthOfField.focusDistance.value)
	var_209_1.gaussianEnd:Override(arg_209_1.depthOfField.focusDistance.value + arg_209_1.depthOfField.focusDistance.length)
	var_209_1.blurRadius:Override(arg_209_1.depthOfField.blurRadius.value)
	var_209_2.postExposure:Override(arg_209_1.postExposure.value)
	var_209_2.contrast:Override(arg_209_1.contrast.value)
	var_209_2.saturation:Override(arg_209_1.saturate.value)
end

function var_0_0.GetCameraSettings(arg_210_0)
	return arg_210_0.originalCameraSettings
end

function var_0_0.RevertCameraSettings(arg_211_0)
	arg_211_0:SettingCamera(arg_211_0.originalCameraSettings)

	arg_211_0.activeCameraSettings = nil
end

function var_0_0.SetVolumeProfile(arg_212_0, arg_212_1, arg_212_2)
	warning(arg_212_1, arg_212_2)

	local var_212_0 = arg_212_0.globalVolume:GetComponent(typeof(BLHX.Volume.Volume))

	arg_212_0.activeProfileWeight = arg_212_2

	if arg_212_0.activeProfileName ~= arg_212_1 then
		arg_212_0.activeProfileName = arg_212_1

		arg_212_0.loader:LoadReference("dorm3d/scenesres/res/common", arg_212_1, nil, function(arg_213_0)
			warning(arg_213_0 and arg_213_0.name or "NIL")

			var_212_0.profile = arg_213_0
			var_212_0.weight = arg_212_0.activeProfileWeight

			if arg_212_0.activeCameraSettings then
				arg_212_0:SettingCamera(arg_212_0.activeCameraSettings)
			end
		end, "VolumeProfile")
	else
		var_212_0.weight = arg_212_0.activeProfileWeight
	end
end

function var_0_0.RevertVolumeProfile(arg_214_0)
	local var_214_0 = arg_214_0.globalVolume:GetComponent(typeof(BLHX.Volume.Volume))

	var_214_0.profile = arg_214_0.originalVolume.profile
	var_214_0.weight = arg_214_0.originalVolume.weight

	if arg_214_0.activeCameraSettings then
		arg_214_0:SettingCamera(arg_214_0.activeCameraSettings)
	end

	arg_214_0.activeProfileName = nil
end

function var_0_0.RecordCharacterLight(arg_215_0)
	local var_215_0 = arg_215_0.characterLight:GetComponent(typeof(Light))

	arg_215_0.originalCharacterColor = {
		color = var_215_0.color,
		intensity = var_215_0.intensity
	}
end

function var_0_0.SetCharacterLight(arg_216_0, arg_216_1, arg_216_2, arg_216_3)
	local var_216_0 = arg_216_0.characterLight:GetComponent(typeof(Light))

	var_216_0.color = Color.Lerp(arg_216_0.originalCharacterColor.color, arg_216_1, arg_216_3)
	var_216_0.intensity = math.lerp(arg_216_0.originalCharacterColor.intensity, arg_216_2, arg_216_3)
end

function var_0_0.RevertCharacterLight(arg_217_0)
	arg_217_0:SetCharacterLight(arg_217_0.originalCharacterColor.color, arg_217_0.originalCharacterColor.intensity, 1)
end

function var_0_0.LoadSceneAsync(arg_218_0, arg_218_1, arg_218_2, arg_218_3)
	table.insert(arg_218_0.sceneDataList, {
		index = 0,
		status = "Loading",
		path = arg_218_1,
		name = arg_218_2
	})
	SceneOpMgr.Inst:LoadSceneAsync(arg_218_1, arg_218_2, LoadSceneMode.Additive, function(arg_219_0, arg_219_1)
		local var_219_0 = _.detect(arg_218_0.sceneDataList, function(arg_220_0)
			return arg_220_0.name == arg_218_2
		end)

		var_219_0.status = "Loaded"
		arg_218_0.sceneCounter = arg_218_0.sceneCounter + 1
		var_219_0.index = arg_218_0.sceneCounter

		existCall(arg_218_3, arg_219_0, arg_219_1)
	end)
end

function var_0_0.UnloadSceneAsync(arg_221_0, arg_221_1, arg_221_2)
	SceneOpMgr.Inst:UnloadSceneAsync(arg_221_1, arg_221_2)

	local var_221_0 = _.detect(arg_221_0.sceneDataList, function(arg_222_0)
		return arg_222_0.name == arg_221_2
	end)
	local var_221_1 = var_221_0.index

	var_221_0.status = "Unloaded"
	arg_221_0.sceneCounter = arg_221_0.sceneCounter - 1
	var_221_0.index = 0

	table.removebyvalue(arg_221_0.sceneDataList, var_221_0)
	_.each(arg_221_0.sceneDataList, function(arg_223_0)
		if arg_223_0.index <= var_221_1 then
			return
		end

		arg_223_0.index = arg_223_0.index - 1
	end)
end

function var_0_0.SwitchLadyInterestInPhotoMode(arg_224_0, arg_224_1)
	if not arg_224_1 then
		arg_224_0:SyncInterestTransform()

		arg_224_0.cameraPhoto.Follow = arg_224_0.ladyInterest
		arg_224_0.cameraPhoto.LookAt = arg_224_0.ladyInterest
	else
		arg_224_0.cameraPhoto.Follow = arg_224_0.ladyInterestRoot
		arg_224_0.cameraPhoto.LookAt = arg_224_0.ladyInterestRoot
	end
end

function var_0_0.SwitchDayNight(arg_225_0, arg_225_1)
	if not arg_225_0.daynightCtrlComp then
		return
	end

	arg_225_0.daynightCtrlComp:SwitcherToIndex(arg_225_1)
end

local var_0_1 = 5
local var_0_2 = 2

function var_0_0.DoRecenter(arg_226_0)
	if arg_226_0.recentTweenId then
		return
	end

	arg_226_0.nextRecentTime = Time.time

	local var_226_0 = arg_226_0.ladyInterest.position - arg_226_0.cameraFree.transform.position
	local var_226_1 = Quaternion.LookRotation(var_226_0).eulerAngles
	local var_226_2 = var_226_1.y
	local var_226_3 = var_226_1.x
	local var_226_4 = arg_226_0.compPov.m_HorizontalAxis.Value
	local var_226_5 = arg_226_0.compPov.m_VerticalAxis.Value
	local var_226_6 = arg_226_0:GetNearestAngle(var_226_2, arg_226_0.compPov.m_HorizontalAxis.m_MinValue, arg_226_0.compPov.m_HorizontalAxis.m_MaxValue)

	arg_226_0.recentTweenId = arg_226_0:managedTween(LeanTween.value, nil, go(arg_226_0.cameraFree), 0, 1, var_0_2):setOnUpdate(System.Action_float(function(arg_227_0)
		local var_227_0 = math.lerp(var_226_4, var_226_6, arg_227_0)
		local var_227_1 = math.lerp(var_226_5, var_226_3, arg_227_0)
		local var_227_2 = arg_226_0.compPov.m_HorizontalAxis

		var_227_2.Value = var_227_0
		arg_226_0.compPov.m_HorizontalAxis = var_227_2

		local var_227_3 = arg_226_0.compPov.m_VerticalAxis

		var_227_3.Value = var_227_1
		arg_226_0.compPov.m_VerticalAxis = var_227_3
	end)):setEase(LeanTweenType.easeOutSine).uniqueId
end

function var_0_0.ResetRecenterTimer(arg_228_0)
	arg_228_0.nextRecentTime = Time.time + var_0_1

	if not arg_228_0.recentTweenId then
		return
	end

	LeanTween.cancel(arg_228_0.recentTweenId)

	arg_228_0.recentTweenId = nil
end

local var_0_3 = 30

function var_0_0.DoRecenterQuick(arg_229_0, arg_229_1)
	if arg_229_0.recentTweenId then
		return
	end

	arg_229_0.nextRecentTime = Time.time

	local var_229_0 = arg_229_0.ladyInterest.position - arg_229_0.cameraFree.transform.position
	local var_229_1 = Quaternion.LookRotation(var_229_0).eulerAngles
	local var_229_2 = var_229_1.y
	local var_229_3 = var_229_1.x
	local var_229_4 = arg_229_0.compPov.m_HorizontalAxis.Value
	local var_229_5 = arg_229_0.compPov.m_VerticalAxis.Value
	local var_229_6 = arg_229_0:GetNearestAngle(var_229_2, arg_229_0.compPov.m_HorizontalAxis.m_MinValue, arg_229_0.compPov.m_HorizontalAxis.m_MaxValue)
	local var_229_7 = math.abs(var_229_6 - var_229_4) / var_0_3

	if var_229_7 < 0.5 then
		return existCall(arg_229_1)
	end

	arg_229_0.recentTweenId = arg_229_0:managedTween(LeanTween.value, arg_229_1, go(arg_229_0.cameraFree), 0, 1, var_229_7):setOnUpdate(System.Action_float(function(arg_230_0)
		local var_230_0 = math.lerp(var_229_4, var_229_6, arg_230_0)
		local var_230_1 = math.lerp(var_229_5, var_229_3, arg_230_0)
		local var_230_2 = arg_229_0.compPov.m_HorizontalAxis

		var_230_2.Value = var_230_0
		arg_229_0.compPov.m_HorizontalAxis = var_230_2

		local var_230_3 = arg_229_0.compPov.m_VerticalAxis

		var_230_3.Value = var_230_1
		arg_229_0.compPov.m_VerticalAxis = var_230_3
	end)):setEase(LeanTweenType.easeOutSine).uniqueId
end

function var_0_0.onBackPressed(arg_231_0)
	if not arg_231_0.baseView or arg_231_0.retainCount > 0 then
		return
	end

	if not arg_231_0.baseView:onBackPressed() then
		arg_231_0:closeView()
	end
end

function var_0_0.willExit(arg_232_0)
	while arg_232_0.baseView:onBackPressed() do
		-- block empty
	end

	arg_232_0.baseView:Destroy()
	arg_232_0.joystickTimer:Stop()
	arg_232_0:ResetRecenterTimer()

	if arg_232_0.moveTimer then
		arg_232_0.moveTimer:Stop()
	end

	GlobalClickEventMgr.Inst:RemoveBeginPinchFunc()
	GlobalClickEventMgr.Inst:RemovePinchFunc()
	GlobalClickEventMgr.Inst:RemoveEndPinchFunc()
	eachChild(arg_232_0.furnitures, function(arg_233_0)
		local var_233_0 = GetComponent(arg_233_0, typeof(EventTriggerListener))

		if not var_233_0 then
			return
		end

		var_233_0:ClearEvents()
	end)
	GetComponent(arg_232_0.lady, typeof(EventTriggerListener)):ClearEvents()

	arg_232_0.camBrainEvenetHandler.OnBlendFinished = nil

	pg.UIMgr.GetInstance():UnOverlayPanel(arg_232_0.blockLayer, arg_232_0._tf)
	arg_232_0:RemoveCharacter()
	arg_232_0.loader:Clear()
	arg_232_0:UnloadSceneAsync(string.lower("dorm3d/scenesres/scenes/" .. arg_232_0.sceneRootName .. "/" .. arg_232_0.baseSceneName .. "_scene"), arg_232_0.baseSceneName)
	arg_232_0:UnloadSceneAsync(string.lower("dorm3d/scenesres/scenes/" .. arg_232_0.sceneRootName .. "/" .. arg_232_0.sceneName .. "_scene"), arg_232_0.sceneName)
end

return var_0_0
