local var_0_0 = class("MetaSkillUnlockPanel", import(".MsgboxSubPanel"))

def var_0_0.getUIName(arg_1_0):
	return "MetaSkillUnlockBox"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.findUI()
	arg_2_0.initData()
	arg_2_0.addListener()

def var_0_0.UpdateView(arg_3_0, arg_3_1):
	arg_3_0.PreRefresh(arg_3_1)
	arg_3_0.updateContent(arg_3_1)

	rtf(arg_3_0.viewParent._window).sizeDelta = Vector2.New(1000, 638)

	arg_3_0.PostRefresh(arg_3_1)

def var_0_0.findUI(arg_4_0):
	arg_4_0.tipText = arg_4_0.findTF("Tip")
	arg_4_0.materialTpl = arg_4_0.findTF("Material")
	arg_4_0.materialContainer = arg_4_0.findTF("MaterialContainer")
	arg_4_0.uiItemList = UIItemList.New(arg_4_0.materialContainer, arg_4_0.materialTpl)
	arg_4_0.cancelBtn = arg_4_0.findTF("Buttons/CancelBtn")
	arg_4_0.confirmBtn = arg_4_0.findTF("Buttons/ConfirmBtn")

	local var_4_0 = arg_4_0.findTF("Text", arg_4_0.cancelBtn)
	local var_4_1 = arg_4_0.findTF("Text", arg_4_0.confirmBtn)

	setText(var_4_0, i18n("word_cancel"))
	setText(var_4_1, i18n("word_ok"))

def var_0_0.initData(arg_5_0):
	arg_5_0.curMetaShipID = None
	arg_5_0.curUnlockSkillID = None
	arg_5_0.curUnlockMaterialID = None
	arg_5_0.curUnlockMaterialNeedCount = None

def var_0_0.addListener(arg_6_0):
	onButton(arg_6_0, arg_6_0.confirmBtn, function()
		if not arg_6_0.curUnlockMaterialID:
			pg.TipsMgr.GetInstance().ShowTips(i18n("meta_unlock_skill_select"))

			return
		elif getProxy(BagProxy).getItemCountById(arg_6_0.curUnlockMaterialID) < arg_6_0.curUnlockMaterialNeedCount:
			pg.TipsMgr.GetInstance().ShowTips(i18n("word_materal_no_enough"))
		else
			local var_7_0 = 0
			local var_7_1 = 0
			local var_7_2 = MetaCharacterConst.getMetaSkillTacticsConfig(arg_6_0.curUnlockSkillID, 1).skill_unlock

			for iter_7_0, iter_7_1 in ipairs(var_7_2):
				if arg_6_0.curUnlockMaterialID == iter_7_1[2]:
					var_7_0 = iter_7_0
					var_7_1 = iter_7_1[3]

					break

			pg.m02.sendNotification(GAME.TACTICS_META_UNLOCK_SKILL, {
				shipID = arg_6_0.curMetaShipID,
				skillID = arg_6_0.curUnlockSkillID,
				materialIndex = var_7_0,
				materialInfo = {
					id = arg_6_0.curUnlockMaterialID,
					count = var_7_1
				}
			})

		pg.MsgboxMgr.GetInstance().hide(), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.cancelBtn, function()
		pg.MsgboxMgr.GetInstance().hide(), SFX_CANCEL)

def var_0_0.updateContent(arg_9_0, arg_9_1):
	local var_9_0 = arg_9_1.metaShipVO
	local var_9_1 = var_9_0.getMetaCharacter()

	arg_9_0.curMetaShipID = var_9_0.id

	local var_9_2 = arg_9_1.skillID

	arg_9_0.curUnlockSkillID = var_9_2

	local var_9_3 = ShipGroup.getDefaultShipNameByGroupID(var_9_1.id)
	local var_9_4 = getSkillName(var_9_2)

	setText(arg_9_0.tipText, i18n("meta_unlock_skill_tip", var_9_3, var_9_4))

	local var_9_5 = MetaCharacterConst.getMetaSkillTacticsConfig(var_9_2, 1)
	local var_9_6 = var_9_5.skill_unlock
	local var_9_7 = {
		var_9_5.skill_unlock[1]
	}

	arg_9_0.uiItemList.make(function(arg_10_0, arg_10_1, arg_10_2)
		if arg_10_0 == UIItemList.EventUpdate:
			arg_10_1 = arg_10_1 + 1

			local var_10_0 = var_9_7[arg_10_1]
			local var_10_1 = arg_9_0.findTF("Item", arg_10_2)
			local var_10_2 = arg_9_0.findTF("SelectedTag", arg_10_2)
			local var_10_3 = arg_9_0.findTF("Count/Text", arg_10_2)
			local var_10_4 = {
				type = DROP_TYPE_ITEM,
				id = var_10_0[2],
				count = var_10_0[3]
			}

			updateDrop(var_10_1, var_10_4)
			setActive(var_10_2, False)

			local var_10_5 = var_10_0[2]
			local var_10_6 = var_10_0[3]
			local var_10_7 = getProxy(BagProxy).getItemCountById(var_10_5)
			local var_10_8 = var_10_7 < var_10_6 and setColorStr(var_10_7, COLOR_RED) or setColorStr(var_10_7, COLOR_GREEN)

			setText(var_10_3, var_10_8 .. "/" .. var_10_6)

			arg_9_0.curUnlockMaterialID = var_10_5
			arg_9_0.curUnlockMaterialNeedCount = var_10_6)
	arg_9_0.uiItemList.align(#var_9_7)

return var_0_0
