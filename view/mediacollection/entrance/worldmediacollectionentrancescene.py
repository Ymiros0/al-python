local var_0_0 = class("WorldMediaCollectionEntranceScene", import("view.base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "WorldMediaCollectionEntranceUI"

def var_0_0.init(arg_2_0):
	arg_2_0.recallBtn = arg_2_0.findTF("Main/recall")
	arg_2_0.cryptolaliaBtn = arg_2_0.findTF("Main/cryptolalia")
	arg_2_0.archiveBtn = arg_2_0.findTF("Main/archive")
	arg_2_0.recordBtn = arg_2_0.findTF("Main/record")
	arg_2_0.optionBtn = arg_2_0.findTF("Top/blur_panel/adapt/top/option")
	arg_2_0.backBtn = arg_2_0.findTF("Top/blur_panel/adapt/top/back_btn")

	setText(arg_2_0.findTF("Main/empty/label"), i18n("cryptolalia_unopen"))
	setText(arg_2_0.findTF("Main/empty1/label"), i18n("cryptolalia_unopen"))

def var_0_0.didEnter(arg_3_0):
	onButton(arg_3_0, arg_3_0.optionBtn, function()
		arg_3_0.emit(var_0_0.ON_HOME), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.backBtn, function()
		arg_3_0.emit(var_0_0.ON_BACK), SFX_CANCEL)
	onButton(arg_3_0, arg_3_0.recallBtn, function()
		arg_3_0.emit(WorldMediaCollectionEntranceMediator.OPEN_RECALL), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.cryptolaliaBtn, function()
		if LOCK_CRYPTOLALIA:
			pg.TipsMgr.GetInstance().ShowTips(i18n("word_comingSoon"))
		else
			arg_3_0.emit(WorldMediaCollectionEntranceMediator.OPEN_CRYPTOLALIA), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.archiveBtn, function()
		arg_3_0.emit(WorldMediaCollectionEntranceMediator.OPEN_ARCHIVE), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.recordBtn, function()
		arg_3_0.emit(WorldMediaCollectionEntranceMediator.OPEN_RECORD), SFX_PANEL)

def var_0_0.willExit(arg_10_0):
	return

return var_0_0
