pg = pg or {}
pg.RepairResMgr = singletonClass("RepairResMgr")

local var_0_0 = pg.RepairResMgr

var_0_0.TYPE_DEFAULT_RES = 2
var_0_0.TYPE_L2D = 4
var_0_0.TYPE_PAINTING = 8
var_0_0.TYPE_CIPHER = 16

def var_0_0.Init(arg_1_0, arg_1_1):
	PoolMgr.GetInstance().GetUI("RepairUI", True, function(arg_2_0)
		arg_1_0._go = arg_2_0
		arg_1_0._tf = arg_1_0._go.transform

		arg_1_0._go.SetActive(False)

		arg_1_0.contentTxt = arg_1_0._tf.Find("window/content/Text").GetComponent(typeof(Text))
		arg_1_0.parentTr = pg.UIMgr.GetInstance().OverlayToast

		arg_1_0._go.transform.SetParent(arg_1_0.parentTr, False)

		arg_1_0.closeBtn = arg_1_0._tf.Find("window/top/btnBack")
		arg_1_0.btns = {
			arg_1_0.InitDefaultResBtn(),
			arg_1_0.InitL2dBtn(),
			arg_1_0.InitPaintingBtn(),
			arg_1_0.InitCipherBtn()
		}
		arg_1_0.uiItemList = UIItemList.New(arg_1_0._tf.Find("window/buttons"), arg_1_0._tf.Find("window/buttons/custom_button_1"))

		setText(arg_1_0._tf.Find("window/top/title"), i18n("msgbox_repair_title"))
		arg_1_1())

def var_0_0.InitDefaultResBtn(arg_3_0):
	return {
		type = var_0_0.TYPE_DEFAULT_RES,
		text = i18n("msgbox_repair"),
		def onCallback:()
			if PathMgr.FileExists(Application.persistentDataPath .. "/hashes.csv"):
				BundleWizard.Inst.GetGroupMgr("DEFAULT_RES").StartVerifyForLua()
			else
				pg.TipsMgr.GetInstance().ShowTips(i18n("word_no_cache"))
	}

def var_0_0.InitL2dBtn(arg_5_0):
	return {
		type = var_0_0.TYPE_L2D,
		text = i18n("msgbox_repair_l2d"),
		def onCallback:()
			if PathMgr.FileExists(Application.persistentDataPath .. "/hashes-live2d.csv"):
				BundleWizard.Inst.GetGroupMgr("L2D").StartVerifyForLua()
			else
				pg.TipsMgr.GetInstance().ShowTips(i18n("word_no_cache"))
	}

def var_0_0.InitPaintingBtn(arg_7_0):
	return {
		type = var_0_0.TYPE_PAINTING,
		text = i18n("msgbox_repair_painting"),
		def onCallback:()
			if PathMgr.FileExists(Application.persistentDataPath .. "/hashes-painting.csv"):
				BundleWizard.Inst.GetGroupMgr("PAINTING").StartVerifyForLua()
			else
				pg.TipsMgr.GetInstance().ShowTips(i18n("word_no_cache"))
	}

def var_0_0.InitCipherBtn(arg_9_0):
	return {
		type = var_0_0.TYPE_CIPHER,
		text = i18n("msgbox_repair_cipher"),
		def onCallback:()
			if PathMgr.FileExists(Application.persistentDataPath .. "/hashes-cipher.csv"):
				BundleWizard.Inst.GetGroupMgr("CIPHER").StartVerifyForLua()
			else
				pg.TipsMgr.GetInstance().ShowTips(i18n("word_no_cache"))
	}

def var_0_0.Repair(arg_11_0, arg_11_1):
	local var_11_0 = arg_11_1 or bit.bor(var_0_0.TYPE_DEFAULT_RES, var_0_0.TYPE_L2D, var_0_0.TYPE_PAINTING, var_0_0.TYPE_CIPHER)
	local var_11_1 = {}

	for iter_11_0, iter_11_1 in ipairs(arg_11_0.btns):
		if bit.band(iter_11_1.type, var_11_0) > 0:
			table.insert(var_11_1, iter_11_1)

	arg_11_0.Show(var_11_1)

def var_0_0.Show(arg_12_0, arg_12_1):
	pg.DelegateInfo.New(arg_12_0)
	arg_12_0._go.SetActive(True)
	pg.UIMgr.GetInstance().BlurPanel(arg_12_0._tf)
	arg_12_0.uiItemList.make(function(arg_13_0, arg_13_1, arg_13_2)
		if arg_13_0 == UIItemList.EventUpdate:
			local var_13_0 = arg_12_1[arg_13_1 + 1]

			setText(arg_13_2.Find("Text"), var_13_0.text)
			onButton(arg_12_0, arg_13_2, function()
				if var_13_0.onCallback:
					var_13_0.onCallback()

				arg_12_0.Hide(), SFX_PANEL))
	arg_12_0.uiItemList.align(#arg_12_1)

	arg_12_0.contentTxt.text = i18n("resource_verify_warn")

	onButton(arg_12_0, arg_12_0._tf, function()
		arg_12_0.Hide(), SFX_PANEL)
	onButton(arg_12_0, arg_12_0.closeBtn, function()
		arg_12_0.Hide(), SFX_PANEL)

def var_0_0.Hide(arg_17_0):
	pg.DelegateInfo.Dispose(arg_17_0)
	arg_17_0._go.SetActive(False)
	pg.UIMgr.GetInstance().UnblurPanel(arg_17_0._tf, arg_17_0.parentTr)
