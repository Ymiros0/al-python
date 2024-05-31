local var_0_0 = class("Dorm3dARScene", import("view.base.BaseUI"))
local var_0_1 = "dorm3d/scenesres/scenes/arscene/arscene_scene"

function var_0_0.getUIName(arg_1_0)
	return "Dorm3DARUI"
end

function var_0_0.preload(arg_2_0, arg_2_1)
	arg_2_0.sceneName = "ARScene"

	seriesAsync({
		function(arg_3_0)
			pg.UIMgr.GetInstance():LoadingOn(false)
			SceneOpMgr.Inst:LoadSceneAsync(string.lower(var_0_1), arg_2_0.sceneName, LoadSceneMode.Additive, function(arg_4_0, arg_4_1)
				arg_3_0()
			end)
		end,
		function(arg_5_0)
			pg.UIMgr.GetInstance():LoadingOff()
			arg_5_0()
		end,
		arg_2_1
	})
end

function var_0_0.init(arg_6_0)
	arg_6_0:findUI()
	arg_6_0:addListener()
end

function var_0_0.didEnter(arg_7_0)
	return
end

function var_0_0.willExit(arg_8_0)
	SceneOpMgr.Inst:UnloadSceneAsync(string.lower(var_0_1), arg_8_0.sceneName)
end

function var_0_0.findUI(arg_9_0)
	arg_9_0.backBtn = arg_9_0:findTF("BackBtn")

	local var_9_0 = arg_9_0:findTF("MenuList")

	arg_9_0.resetBtn = arg_9_0:findTF("ResetBtn", var_9_0)
	arg_9_0.showPlaneBtn = arg_9_0:findTF("ShowPlaneBtn", var_9_0)
	arg_9_0.hidePlaneBtn = arg_9_0:findTF("HidePlaneBtn", var_9_0)

	local var_9_1 = arg_9_0:findTF("TipText")

	arg_9_0.tipCheckPlane = arg_9_0:findTF("CheckPlaneText", var_9_1)
	arg_9_0.tipInsPrefab = arg_9_0:findTF("InsPrefabText", var_9_1)
	arg_9_0.tipDistance = arg_9_0:findTF("DistanceText", var_9_1)

	setText(arg_9_0.tipCheckPlane, "请检测一个平面")
	setText(arg_9_0.tipInsPrefab, "长按平面呼出角色")
	setText(arg_9_0.tipDistance, "距离太近隐藏角色")
	setActive(arg_9_0.tipCheckPlane, false)
	setActive(arg_9_0.tipInsPrefab, false)
	setActive(arg_9_0.tipDistance, false)

	local var_9_2 = GameObject.Find("ScriptHander")

	arg_9_0.aiHelperSC = GetComponent(var_9_2, "ARHelper")
end

function var_0_0.addListener(arg_10_0)
	onButton(arg_10_0, arg_10_0.backBtn, function()
		arg_10_0:closeView()
	end, SFX_PANEL)
	onButton(arg_10_0, arg_10_0.resetBtn, function()
		arg_10_0.aiHelperSC:ResetAll()
	end, SFX_PANEL)
	onButton(arg_10_0, arg_10_0.showPlaneBtn, function()
		arg_10_0.aiHelperSC:ShowAllPlane(true)
	end, SFX_PANEL)
	onButton(arg_10_0, arg_10_0.hidePlaneBtn, function()
		arg_10_0.aiHelperSC:ShowAllPlane(false)
	end, SFX_PANEL)

	function arg_10_0.aiHelperSC.planeCountCB(arg_15_0, arg_15_1)
		local var_15_0 = arg_15_0 > 0

		setActive(arg_10_0.tipCheckPlane, not var_15_0)
		setActive(arg_10_0.tipInsPrefab, var_15_0 and not arg_15_1)
	end

	function arg_10_0.aiHelperSC.distanceCB(arg_16_0)
		pg.TipsMgr.GetInstance():ShowTips("距离过近，以后会隐藏")
	end

	function arg_10_0.aiHelperSC.insPrefabFailCB()
		pg.TipsMgr.GetInstance():ShowTips("距离过近，呼出角色失败")
	end

	function arg_10_0.aiHelperSC.insPrefabSuccCB()
		pg.TipsMgr.GetInstance():ShowTips("呼出角色成功")
		arg_10_0.aiHelperSC:StopPlaneCheck()
	end
end

return var_0_0
