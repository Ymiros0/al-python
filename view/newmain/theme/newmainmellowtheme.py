local var_0_0 = class("NewMainMellowTheme", import(".NewMainSceneBaseTheme"))

def var_0_0.getUIName(arg_1_0):
	return "NewMainMellowTheme"

def var_0_0.OnLoaded(arg_2_0):
	var_0_0.super.OnLoaded(arg_2_0)

	arg_2_0.switcherAnimationPlayer = arg_2_0._tf.Find("frame/right").GetComponent(typeof(Animation))
	arg_2_0.fxEffect = arg_2_0.findTF("frame/right/1/battle/root/FX")
	arg_2_0.animationPlayer = arg_2_0._tf.GetComponent(typeof(Animation))
	arg_2_0.dftAniEvent = arg_2_0._tf.GetComponent(typeof(DftAniEvent))
	arg_2_0.switcher = arg_2_0.findTF("frame/right/switch")

	onToggle(arg_2_0, arg_2_0.switcher, function(arg_3_0)
		local var_3_0 = arg_3_0 and "anim_newmain_switch_1to2" or "anim_newmain_switch_2to1"

		arg_2_0.switcherAnimationPlayer.Play(var_3_0)

		local var_3_1 = arg_2_0.GetRedDots()
		local var_3_2 = _.select(var_3_1, function(arg_4_0)
			return isa(arg_4_0, SwitcherRedDotNode))

		_.each(var_3_2, function(arg_5_0)
			arg_5_0.RefreshSelf()), SFX_PANEL)
	arg_2_0.Register()

def var_0_0.Register(arg_6_0):
	return

def var_0_0.PlayEnterAnimation(arg_7_0, arg_7_1, arg_7_2):
	arg_7_0.bannerView.Init()
	arg_7_0.actBtnView.Init()
	arg_7_0.dftAniEvent.SetStartEvent(None)
	arg_7_0.dftAniEvent.SetStartEvent(function()
		arg_7_0.dftAniEvent.SetStartEvent(None)

		arg_7_0.mainCG.alpha = 1)
	arg_7_0.animationPlayer.Play("anim_newmain_open")
	onDelayTick(arg_7_2, 0.51)

def var_0_0.Refresh(arg_9_0, arg_9_1):
	var_0_0.super.Refresh(arg_9_0, arg_9_1)
	UIUtil.SetLayerRecursively(arg_9_0.fxEffect.gameObject, LayerMask.NameToLayer("UI"))
	arg_9_0.animationPlayer.Play("anim_newmain_open")

def var_0_0.OnFoldPanels(arg_10_0, arg_10_1):
	if arg_10_1:
		arg_10_0.animationPlayer.Play("anim_newmain_hide")
	else
		arg_10_0.animationPlayer.Play("anim_newmain_show")

def var_0_0.Disable(arg_11_0):
	var_0_0.super.Disable(arg_11_0)
	arg_11_0.dftAniEvent.SetStartEvent(None)
	triggerToggle(arg_11_0.switcher, False)
	UIUtil.SetLayerRecursively(arg_11_0.fxEffect.gameObject, LayerMask.NameToLayer("UIHidden"))

def var_0_0.OnDestroy(arg_12_0):
	var_0_0.super.OnDestroy(arg_12_0)
	arg_12_0.dftAniEvent.SetStartEvent(None)

def var_0_0.ApplyDefaultResUI(arg_13_0):
	return False

def var_0_0.GetCalibrationBG(arg_14_0):
	return "mainui_calibration_mellow"

def var_0_0.GetPbList(arg_15_0):
	return {
		arg_15_0.findTF("frame/bottom/frame")
	}

def var_0_0.GetPaintingOffset(arg_16_0, arg_16_1):
	local var_16_0 = pg.ship_skin_newmainui_shift[arg_16_1.skinId]

	if var_16_0:
		local var_16_1 = arg_16_0.GetConfigShift(var_16_0)

		return MainPaintingShift.New(var_16_1, Vector3(-MainPaintingView.MESH_POSITION_X_OFFSET, -10, 0))
	else
		return MainPaintingShift.New({
			-MainPaintingView.MESH_POSITION_X_OFFSET,
			-10,
			MainPaintingView.MESH_POSITION_X_OFFSET,
			0,
			MainPaintingView.MESH_POSITION_X_OFFSET,
			0,
			1,
			1,
			1
		})

def var_0_0.GetConfigShift(arg_17_0, arg_17_1):
	local var_17_0 = arg_17_1.skin_shift
	local var_17_1 = arg_17_1.l2d_shift
	local var_17_2 = var_17_1[1] - var_17_0[1]
	local var_17_3 = var_17_1[2] - var_17_0[2]
	local var_17_4 = arg_17_1.spine_shift
	local var_17_5 = var_17_4[1] - var_17_0[1]
	local var_17_6 = var_17_4[2] - var_17_0[2]

	return {
		var_17_0[1],
		var_17_0[2],
		var_17_2,
		var_17_3,
		var_17_5,
		var_17_6,
		var_17_0[4],
		var_17_1[4],
		var_17_4[4]
	}

def var_0_0.GetWordView(arg_18_0):
	return MainWordView4Mellow.New(arg_18_0.findTF("chat"), arg_18_0.event)

def var_0_0.GetTagView(arg_19_0):
	return MainTagsView.New(arg_19_0.findTF("frame/bottom/tags"), arg_19_0.event)

def var_0_0.GetTopPanel(arg_20_0):
	return MainTopPanel4Mellow.New(arg_20_0.findTF("frame/top"), arg_20_0.event, arg_20_0.contextData)

def var_0_0.GetRightPanel(arg_21_0):
	return MainRightPanel4Mellow.New(arg_21_0.findTF("frame/right"), arg_21_0.event, arg_21_0.contextData)

def var_0_0.GetLeftPanel(arg_22_0):
	return MainLeftPanel4Mellow.New(arg_22_0.findTF("frame/left"), arg_22_0.event, arg_22_0.contextData)

def var_0_0.GetBottomPanel(arg_23_0):
	return MainBottomPanel4Mellow.New(arg_23_0.findTF("frame/bottom"), arg_23_0.event, arg_23_0.contextData)

def var_0_0.GetIconView(arg_24_0):
	return MainIconView4Mellow.New(arg_24_0.findTF("frame/top/icon"), arg_24_0.event)

def var_0_0.GetChatRoomView(arg_25_0):
	return MainChatRoomView4Mellow.New(arg_25_0.findTF("frame/right/chat_room"), arg_25_0.event)

def var_0_0.GetBannerView(arg_26_0):
	return MainBannerView4Mellow.New(arg_26_0.findTF("frame/left/banner"), arg_26_0.event)

def var_0_0.GetActBtnView(arg_27_0):
	return MainActivityBtnView4Mellow.New(arg_27_0.findTF("frame"), arg_27_0.event)

def var_0_0.GetBuffView(arg_28_0):
	return MainBuffView4Mellow.New(arg_28_0.findTF("frame/top/buff_list"), arg_28_0.event)

def var_0_0.GetRedDots(arg_29_0):
	return {
		RedDotNode.New(arg_29_0._tf.Find("frame/bottom/frame/task/tip"), {
			pg.RedDotMgr.TYPES.TASK
		}),
		MailRedDotNode4Mellow.New(arg_29_0._tf.Find("frame/top/btns/mail")),
		RedDotNode.New(arg_29_0._tf.Find("frame/bottom/frame/build/tip"), {
			pg.RedDotMgr.TYPES.BUILD
		}),
		RedDotNode.New(arg_29_0._tf.Find("frame/bottom/frame/guild/tip"), {
			pg.RedDotMgr.TYPES.GUILD
		}),
		RedDotNode.New(arg_29_0._tf.Find("frame/top/icon_front/tip"), {
			pg.RedDotMgr.TYPES.ATTIRE
		}),
		RedDotNode.New(arg_29_0._tf.Find("frame/right/2/menor/root/tip"), {
			pg.RedDotMgr.TYPES.MEMORY_REVIEW
		}),
		RedDotNode.New(arg_29_0._tf.Find("frame/right/2/collection/root/tip"), {
			pg.RedDotMgr.TYPES.COLLECTION
		}),
		RedDotNode.New(arg_29_0._tf.Find("frame/right/2/friend/root/tip"), {
			pg.RedDotMgr.TYPES.FRIEND
		}),
		RedDotNode.New(arg_29_0._tf.Find("frame/left/extend/tip"), {
			pg.RedDotMgr.TYPES.COMMISSION
		}),
		SettingsRedDotNode.New(arg_29_0._tf.Find("frame/top/btns/settings/tip"), {
			pg.RedDotMgr.TYPES.SETTTING
		}),
		RedDotNode.New(arg_29_0._tf.Find("frame/top/btns/noti/tip"), {
			pg.RedDotMgr.TYPES.SERVER
		}),
		RedDotNode.New(arg_29_0._tf.Find("frame/bottom/frame/tech/tip"), {
			pg.RedDotMgr.TYPES.BLUEPRINT
		}),
		RedDotNode.New(arg_29_0._tf.Find("frame/right/1/battle/root/tip"), {
			pg.RedDotMgr.TYPES.EVENT
		}),
		RedDotNode.New(arg_29_0._tf.Find("frame/bottom/frame/live/tip"), {
			pg.RedDotMgr.TYPES.COURTYARD,
			pg.RedDotMgr.TYPES.SCHOOL,
			pg.RedDotMgr.TYPES.COMMANDER
		}),
		SwitcherRedDotNode.New(arg_29_0._tf.Find("frame/right/switch"), {
			pg.RedDotMgr.TYPES.COLLECTION,
			pg.RedDotMgr.TYPES.FRIEND,
			pg.RedDotMgr.TYPES.MEMORY_REVIEW
		}, True),
		SwitcherRedDotNode.New(arg_29_0._tf.Find("frame/right/switch"), {
			pg.RedDotMgr.TYPES.EVENT
		}, False)
	}

return var_0_0
