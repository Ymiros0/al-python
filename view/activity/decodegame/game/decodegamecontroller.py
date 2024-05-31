local var_0_0 = class("DecodeGameController")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.model = DecodeGameModel.New(arg_1_0)
	arg_1_0.view = DecodeGameView.New(arg_1_0)

def var_0_0.SetCallback(arg_2_0, arg_2_1, arg_2_2, arg_2_3):
	arg_2_0.exitCallBack = arg_2_1
	arg_2_0.saveDataCallback = arg_2_2
	arg_2_0.successCallback = arg_2_3

def var_0_0.SetUp(arg_3_0, arg_3_1):
	seriesAsync({
		function(arg_4_0)
			arg_3_0.isIniting = True

			arg_3_0.model.SetData(arg_3_1)
			arg_3_0.UpdateProgress()
			arg_3_0.view.UpdateCanUseCnt(arg_3_0.model.canUseCnt)
			arg_3_0.SwitchMap(arg_3_0.model.map.id, arg_4_0()),
		function(arg_5_0)
			arg_3_0.PlayVoice(DecodeGameConst.OPEN_DOOR_VOICE)
			arg_3_0.view.DoEnterAnim(arg_5_0),
		function(arg_6_0)
			pg.NewStoryMgr.GetInstance().Play(DecodeGameConst.STORYID, arg_6_0),
		function(arg_7_0)
			arg_3_0.view.ShowHelper(1, arg_7_0),
		function(arg_8_0)
			arg_3_0.isIniting = None

			arg_3_0.ShowTip()
			arg_3_0.view.Inited(arg_3_0.model.isFinished)
	})

def var_0_0.ShowTip(arg_9_0):
	local var_9_0 = arg_9_0.model.GetUnlockMapCnt()
	local var_9_1

	if arg_9_0.model.isFinished:
		var_9_1 = 0
	elif var_9_0 < DecodeGameConst.MAX_MAP_COUNT and arg_9_0.model.canUseCnt <= 0:
		var_9_1 = 1
	elif var_9_0 < DecodeGameConst.MAX_MAP_COUNT and arg_9_0.model.canUseCnt > 0:
		var_9_1 = 2
	elif not arg_9_0.isInDecodeMap and not arg_9_0.isInComparison and var_9_0 == DecodeGameConst.MAX_MAP_COUNT:
		var_9_1 = 3
	elif arg_9_0.isInDecodeMap and not arg_9_0.isInComparison and var_9_0 == DecodeGameConst.MAX_MAP_COUNT:
		var_9_1 = 4
	elif arg_9_0.isInDecodeMap and arg_9_0.isInComparison and var_9_0 == DecodeGameConst.MAX_MAP_COUNT:
		var_9_1 = 5

	arg_9_0.view.ShowTip(var_9_1)

def var_0_0.UpdateProgress(arg_10_0, arg_10_1):
	local var_10_0 = arg_10_0.model.GetUnlockedCnt()
	local var_10_1 = arg_10_0.model.GetUnlockMapCnt()
	local var_10_2, var_10_3 = arg_10_0.model.GetPassWordProgress()

	arg_10_1 = arg_10_1 or function()
		return

	if var_10_3 > (arg_10_0.finishCnt or 0) and var_10_3 != #var_10_2:
		arg_10_0.finishCnt = var_10_3

		arg_10_0.PlayVoice(DecodeGameConst.INCREASE_PASSWORD_PROGRESS_VOICE)

	arg_10_0.view.UpdateProgress(var_10_0, var_10_1, var_10_2, arg_10_1)

def var_0_0.SwitchMap(arg_12_0, arg_12_1, arg_12_2):
	if arg_12_0.inSwitching:
		return

	if arg_12_0.mapId != arg_12_1:
		local function var_12_0(arg_13_0)
			parallelAsync({
				function(arg_14_0)
					if not arg_12_0.isInDecodeMap:
						arg_12_0.view.OnSwitchMap(arg_14_0)
					else
						arg_14_0(),
				function(arg_15_0)
					if not arg_12_0.mapId:
						arg_15_0()

						return

					arg_12_0.model.ExitMap()
					arg_12_0.view.OnExitMap(arg_12_0.mapId, arg_12_0.isInDecodeMap, arg_15_0),
				function(arg_16_0)
					arg_12_0.mapId = None

					arg_12_0.model.SwitchMap(arg_12_1)
					arg_12_0.view.UpdateMap(arg_12_0.model.map)
					arg_12_0.view.OnEnterMap(arg_12_1, arg_12_0.isInDecodeMap, arg_16_0)
			}, arg_13_0)

		seriesAsync({
			function(arg_17_0)
				if not arg_12_0.isIniting:
					arg_12_0.PlayVoice(DecodeGameConst.SWITCH_MAP_VOCIE)

				arg_12_0.inSwitching = True

				var_12_0(arg_17_0),
			function(arg_18_0)
				arg_12_0.mapId = arg_12_1

				if not arg_12_0.isInDecodeMap:
					arg_18_0()

					return

				arg_12_0.isInComparison = True

				arg_12_0.PlayVoice(DecodeGameConst.SCAN_MAP_VOICE)
				arg_12_0.view.OnDecodeMap(arg_12_0.model.map, arg_18_0),
			function(arg_19_0)
				arg_12_0.inSwitching = None

				if arg_12_0.isInDecodeMap:
					arg_12_0.ShowTip()
					arg_12_0.view.ShowHelper(3, arg_19_0)
				else
					arg_19_0()
		}, arg_12_2)

def var_0_0.Unlock(arg_20_0, arg_20_1):
	if arg_20_0.inSwitching:
		return

	if arg_20_0.isInDecodeMap:
		arg_20_0.EnterPassWord(arg_20_1)
	else
		arg_20_0.UnlockMapItem(arg_20_1)

def var_0_0.EnterPassWord(arg_21_0, arg_21_1):
	if not arg_21_0.model.IsMapKey(arg_21_1):
		return

	if arg_21_0.model.IsUsedMapKey(arg_21_1):
		return

	if arg_21_0.model.CheckIndex(arg_21_1):
		arg_21_0.model.InsertMapKey(arg_21_1)

		local var_21_0 = arg_21_0.model.GetCurrMapKeyIndex(arg_21_1)
		local var_21_1 = arg_21_0.model.GetMapKeyStr(arg_21_1)

		arg_21_0.view.OnRightCode(arg_21_1, var_21_1, var_21_0)

		if arg_21_0.model.IsSuccess():
			arg_21_0.model.Finish()
			arg_21_0.PlayVoice(DecodeGameConst.GET_AWARD_DONE_VOICE)
			arg_21_0.view.OnSuccess(function()
				pg.NewStoryMgr.GetInstance().Play(DecodeGameConst.LAST_STORYID)

				if arg_21_0.successCallback:
					arg_21_0.successCallback())
		else
			arg_21_0.PlayVoice(DecodeGameConst.PASSWORD_IS_RIGHT_VOICE)

		arg_21_0.UpdateProgress()
	else
		arg_21_0.PlayVoice(DecodeGameConst.PASSWORD_IS_FALSE_VOICE)
		arg_21_0.view.OnFalseCode(arg_21_1)

def var_0_0.UnlockMapItem(arg_23_0, arg_23_1):
	if arg_23_0.model.canUseCnt > 0 and not arg_23_0.model.IsUnlock(arg_23_1):
		seriesAsync({
			function(arg_24_0)
				arg_23_0.inSwitching = True

				arg_23_0.model.UnlockMapItem(arg_23_1)
				arg_23_0.view.UnlockMapItem(arg_23_1, arg_24_0),
			function(arg_25_0)
				arg_23_0.PlayStory(arg_25_0),
			function(arg_26_0)
				arg_23_0.view.UpdateCanUseCnt(arg_23_0.model.canUseCnt)

				if arg_23_0.model.IsUnlockMap(arg_23_0.model.map.id):
					arg_23_0.RepairMap()
				else
					arg_23_0.PlayVoice(DecodeGameConst.INCREASE_PROGRESS_VOICE)
					arg_23_0.UpdateProgress()

					if arg_23_0.saveDataCallback:
						arg_23_0.saveDataCallback()

					arg_23_0.inSwitching = None

				arg_23_0.ShowTip()
				arg_26_0()
		})

def var_0_0.PlayStory(arg_27_0, arg_27_1):
	local var_27_0 = arg_27_0.model.GetUnlockedCnt()
	local var_27_1 = DecodeGameConst.UNLOCK_STORYID[var_27_0]

	if var_27_1:
		pg.NewStoryMgr.GetInstance().Play(var_27_1, arg_27_1)
	else
		arg_27_1()

def var_0_0.RepairMap(arg_28_0):
	seriesAsync({
		function(arg_29_0)
			arg_28_0.model.OnRepairMap()
			arg_28_0.view.OnMapRepairing(arg_29_0),
		function(arg_30_0)
			if arg_28_0.saveDataCallback:
				arg_28_0.saveDataCallback(arg_30_0)
			else
				arg_30_0(),
		function(arg_31_0)
			arg_28_0.PlayVoice(DecodeGameConst.INCREASE_PROGRESS_VOICE)
			arg_28_0.view.UpdateMap(arg_28_0.model.map)
			arg_28_0.UpdateProgress(arg_31_0),
		function(arg_32_0)
			if arg_28_0.model.GetUnlockMapCnt() == DecodeGameConst.MAX_MAP_COUNT:
				arg_28_0.view.ShowHelper(2, arg_32_0)

			arg_28_0.inSwitching = None
	})

def var_0_0.CanSwitch(arg_33_0):
	return not arg_33_0.inSwitching

def var_0_0.SwitchToDecodeMap(arg_34_0, arg_34_1):
	if arg_34_0.inSwitching:
		return

	if arg_34_1:
		arg_34_0.EnterDecodeMap()
	else
		arg_34_0.ExitDeCodeMap()

def var_0_0.ExitDeCodeMap(arg_35_0):
	arg_35_0.isFirstSwitch = False

	seriesAsync({
		function(arg_36_0)
			arg_35_0.PlayVoice(DecodeGameConst.PRESS_UP_PASSWORDBTN)

			arg_35_0.finishCnt = 0
			arg_35_0.isInComparison = None
			arg_35_0.inSwitching = True

			arg_35_0.view.OnEnterNormalMapBefore(arg_36_0),
		function(arg_37_0)
			parallelAsync({
				function(arg_38_0)
					arg_35_0.view.OnEnterNormalMap(arg_35_0.model.map, arg_38_0),
				function(arg_39_0)
					arg_35_0.mapId = arg_35_0.model.map.id

					arg_35_0.view.OnEnterMap(arg_35_0.mapId, False, arg_39_0)
			}, arg_37_0),
		function()
			arg_35_0.model.ClearMapKeys()
			arg_35_0.UpdateProgress()

			arg_35_0.isInDecodeMap = None
			arg_35_0.inSwitching = None

			arg_35_0.ShowTip()
	})

def var_0_0.EnterDecodeMap(arg_41_0):
	arg_41_0.isInDecodeMap = True
	arg_41_0.isFirstSwitch = True

	seriesAsync({
		function(arg_42_0)
			arg_41_0.PlayVoice(DecodeGameConst.PRESS_DOWN_PASSWORDBTN)

			arg_41_0.inSwitching = True

			parallelAsync({
				function(arg_43_0)
					arg_41_0.view.OnEnterDecodeMapBefore(arg_43_0),
				function(arg_44_0)
					arg_41_0.view.OnExitMap(arg_41_0.mapId, True, arg_44_0)
			}, arg_42_0),
		function(arg_45_0)
			arg_41_0.mapId = None

			local var_45_0 = arg_41_0.model.GetMapKeyStrs()

			arg_41_0.view.OnEnterDecodeMap(var_45_0, arg_45_0),
		function(arg_46_0)
			arg_41_0.ShowTip()

			arg_41_0.inSwitching = None
	})

def var_0_0.ExitGame(arg_47_0):
	if arg_47_0.inSwitching:
		return

	if arg_47_0.exitCallBack:
		arg_47_0.exitCallBack()

def var_0_0.PlayVoice(arg_48_0, arg_48_1):
	if arg_48_1 and arg_48_1 != "":
		arg_48_0.view.PlayVoice(arg_48_1)

def var_0_0.GetSaveData(arg_49_0):
	return arg_49_0.model.unlocks

def var_0_0.Dispose(arg_50_0):
	arg_50_0.model.Dispose()
	arg_50_0.view.Dispose()

return var_0_0
