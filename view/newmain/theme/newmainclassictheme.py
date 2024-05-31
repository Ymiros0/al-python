local var_0_0 = class("NewMainClassicTheme", import(".NewMainSceneBaseTheme"))

def var_0_0.getUIName(arg_1_0):
	return "NewMainClassicTheme"

def var_0_0.OnLoaded(arg_2_0):
	var_0_0.super.OnLoaded(arg_2_0)

	arg_2_0.adapterView = MainAdpterView.New(arg_2_0.findTF("top_bg"), arg_2_0.findTF("bottom_bg"), arg_2_0.findTF("bg/right"))

def var_0_0.PlayEnterAnimation(arg_3_0, arg_3_1, arg_3_2):
	arg_3_0.adapterView.Init()
	var_0_0.super.PlayEnterAnimation(arg_3_0, arg_3_1, arg_3_2)

def var_0_0._FoldPanels(arg_4_0, arg_4_1, arg_4_2):
	var_0_0.super._FoldPanels(arg_4_0, arg_4_1, arg_4_2)
	arg_4_0.adapterView.Fold(arg_4_1, arg_4_2)

def var_0_0.OnDestroy(arg_5_0):
	var_0_0.super.OnDestroy(arg_5_0)

	if arg_5_0.adapterView:
		arg_5_0.adapterView.Dispose()

		arg_5_0.adapterView = None

def var_0_0.GetCalibrationBG(arg_6_0):
	return "mainui_calibration"

def var_0_0.GetPbList(arg_7_0):
	return {
		arg_7_0.findTF("frame/chatPreview"),
		arg_7_0.findTF("frame/eventPanel")
	}

def var_0_0.GetPaintingOffset(arg_8_0, arg_8_1):
	return MainPaintingShift.New({
		-600,
		-10,
		170,
		0,
		170,
		0,
		1,
		1,
		1
	})

def var_0_0.GetWordView(arg_9_0):
	return MainWordView.New(arg_9_0.findTF("chat"), arg_9_0.event)

def var_0_0.GetTagView(arg_10_0):
	return MainTagsView.New(arg_10_0.findTF("frame/bottom/tags"), arg_10_0.event)

def var_0_0.GetTopPanel(arg_11_0):
	return MainTopPanel.New(arg_11_0.findTF("frame/top"), arg_11_0.event, arg_11_0.contextData)

def var_0_0.GetRightPanel(arg_12_0):
	return MainRightPanel.New(arg_12_0.findTF("frame/right"), arg_12_0.event, arg_12_0.contextData)

def var_0_0.GetLeftPanel(arg_13_0):
	return MainLeftPanel.New(arg_13_0.findTF("frame/left"), arg_13_0.event, arg_13_0.contextData)

def var_0_0.GetBottomPanel(arg_14_0):
	return MainBottomPanel.New(arg_14_0.findTF("frame/bottom"), arg_14_0.event, arg_14_0.contextData)

def var_0_0.GetIconView(arg_15_0):
	return MainIconView.New(arg_15_0.findTF("frame/char"))

def var_0_0.GetChatRoomView(arg_16_0):
	return MainChatRoomView.New(arg_16_0.findTF("frame/chatPreview"), arg_16_0.event)

def var_0_0.GetBannerView(arg_17_0):
	return MainBannerView.New(arg_17_0.findTF("frame/eventPanel"), arg_17_0.event)

def var_0_0.GetActBtnView(arg_18_0):
	return MainActivityBtnView.New(arg_18_0.findTF("frame/linkBtns"), arg_18_0.event)

def var_0_0.GetBuffView(arg_19_0):
	return MainBuffView.New(arg_19_0.findTF("frame/buffs"), arg_19_0.event)

def var_0_0.GetCalibrationView(arg_20_0):
	return MainCalibrationPage.New(arg_20_0._tf, arg_20_0.event)

def var_0_0.GetRedDots(arg_21_0):
	return {
		RedDotNode.New(arg_21_0._tf.Find("frame/bottom/taskButton/tip"), {
			pg.RedDotMgr.TYPES.TASK
		}),
		MailRedDotNode.New(arg_21_0._tf.Find("frame/right/mailButton")),
		RedDotNode.New(arg_21_0._tf.Find("frame/bottom/buildButton/tip"), {
			pg.RedDotMgr.TYPES.BUILD
		}),
		RedDotNode.New(arg_21_0._tf.Find("frame/bottom/guildButton/tip"), {
			pg.RedDotMgr.TYPES.GUILD
		}),
		RedDotNode.New(arg_21_0._tf.Find("frame/top/tip"), {
			pg.RedDotMgr.TYPES.ATTIRE
		}),
		RedDotNode.New(arg_21_0._tf.Find("frame/right/memoryButton/tip"), {
			pg.RedDotMgr.TYPES.MEMORY_REVIEW
		}),
		RedDotNode.New(arg_21_0._tf.Find("frame/right/collectionButton/tip"), {
			pg.RedDotMgr.TYPES.COLLECTION
		}),
		RedDotNode.New(arg_21_0._tf.Find("frame/right/friendButton/tip"), {
			pg.RedDotMgr.TYPES.FRIEND
		}),
		RedDotNode.New(arg_21_0._tf.Find("frame/left/commissionButton/tip"), {
			pg.RedDotMgr.TYPES.COMMISSION
		}),
		SettingsRedDotNode.New(arg_21_0._tf.Find("frame/right/settingButton/tip"), {
			pg.RedDotMgr.TYPES.SETTTING
		}),
		RedDotNode.New(arg_21_0._tf.Find("frame/right/noticeButton/tip"), {
			pg.RedDotMgr.TYPES.SERVER
		}),
		RedDotNode.New(arg_21_0._tf.Find("frame/bottom/technologyButton/tip"), {
			pg.RedDotMgr.TYPES.BLUEPRINT
		}),
		RedDotNode.New(arg_21_0._tf.Find("frame/right/combatBtn/tip"), {
			pg.RedDotMgr.TYPES.EVENT
		}),
		RedDotNode.New(arg_21_0._tf.Find("frame/bottom/liveButton/tip"), {
			pg.RedDotMgr.TYPES.COURTYARD,
			pg.RedDotMgr.TYPES.SCHOOL,
			pg.RedDotMgr.TYPES.COMMANDER
		})
	}

return var_0_0
