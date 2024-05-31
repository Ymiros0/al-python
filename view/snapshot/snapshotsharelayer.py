local var_0_0 = class("SnapshotShareLayer", import("..base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "snapshotshareui"

def var_0_0.init(arg_2_0):
	arg_2_0.photoImgTrans = arg_2_0.findTF("PhotoImg")
	arg_2_0.rawImage = arg_2_0.photoImgTrans.GetComponent("RawImage")
	arg_2_0.shareBtnTrans = arg_2_0.findTF("BtnPanel/ShareBtn")
	arg_2_0.confirmBtnTrans = arg_2_0.findTF("BtnPanel/ConfirmBtn")
	arg_2_0.cancelBtnTrans = arg_2_0.findTF("BtnPanel/CancelBtn")
	arg_2_0.userAgreenTF = arg_2_0.findTF("UserAgreement")
	arg_2_0.userAgreenMainTF = arg_2_0.findTF("window", arg_2_0.userAgreenTF)
	arg_2_0.closeUserAgreenTF = arg_2_0.findTF("close_btn", arg_2_0.userAgreenMainTF)
	arg_2_0.userRefuseConfirmTF = arg_2_0.findTF("refuse_btn", arg_2_0.userAgreenMainTF)
	arg_2_0.userAgreenConfirmTF = arg_2_0.findTF("accept_btn", arg_2_0.userAgreenMainTF)

	setActive(arg_2_0.userAgreenTF, False)

	arg_2_0.rawImage.texture = arg_2_0.contextData.photoTex
	arg_2_0.bytes = arg_2_0.contextData.photoData

def var_0_0.didEnter(arg_3_0):
	onButton(arg_3_0, arg_3_0.shareBtnTrans, function()
		local var_4_0 = PlayerPrefs.GetInt("snapshotAgress")

		if not var_4_0 or var_4_0 <= 0:
			arg_3_0.showUserAgreement(function()
				PlayerPrefs.SetInt("snapshotAgress", 1)
				pg.ShareMgr.GetInstance().Share(pg.ShareMgr.TypePhoto))
		else
			pg.ShareMgr.GetInstance().Share(pg.ShareMgr.TypePhoto), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.confirmBtnTrans, function()
		local var_6_0 = pg.TimeMgr.GetInstance().STimeDescS(pg.TimeMgr.GetInstance().GetServerTime(), "*t")
		local var_6_1 = "azur" .. var_6_0.year .. var_6_0.month .. var_6_0.day .. var_6_0.hour .. var_6_0.min .. var_6_0.sec .. ".jpg"
		local var_6_2 = Application.persistentDataPath .. "/" .. var_6_1

		MediaSaver.SaveImageWithBytes(var_6_2, arg_3_0.bytes)
		pg.TipsMgr.GetInstance().ShowTips(i18n("word_save_ok"))
		arg_3_0.closeView())
	onButton(arg_3_0, arg_3_0.cancelBtnTrans, function()
		arg_3_0.closeView())

def var_0_0.willExit(arg_8_0):
	return

def var_0_0.showUserAgreement(arg_9_0, arg_9_1):
	setButtonEnabled(arg_9_0.userAgreenConfirmTF, True)

	local var_9_0

	arg_9_0.userAgreenTitleTF = arg_9_0.findTF("UserAgreement/window/title")
	arg_9_0.userAgreenTitleTF.GetComponent("Text").text = i18n("word_snapshot_share_title")

	setActive(arg_9_0.userAgreenTF, True)
	setText(arg_9_0.userAgreenTF.Find("window/container/scrollrect/content/Text"), i18n("word_snapshot_share_agreement"))
	onButton(arg_9_0, arg_9_0.userRefuseConfirmTF, function()
		setActive(arg_9_0.userAgreenTF, False))
	onButton(arg_9_0, arg_9_0.userAgreenConfirmTF, function()
		setActive(arg_9_0.userAgreenTF, False)

		if arg_9_1:
			arg_9_1())
	onButton(arg_9_0, arg_9_0.closeUserAgreenTF, function()
		setActive(arg_9_0.userAgreenTF, False))

return var_0_0
