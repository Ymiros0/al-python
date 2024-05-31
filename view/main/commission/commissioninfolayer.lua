local var_0_0 = class("CommissionInfoLayer", import("...base.BaseUI"))

function var_0_0.getUIName(arg_1_0)
	if getProxy(SettingsProxy):IsMellowStyle() then
		return "CommissionInfoUI4Mellow"
	else
		return "CommissionInfoUI"
	end
end

function var_0_0.init(arg_2_0)
	arg_2_0.frame = arg_2_0:findTF("frame")
	arg_2_0.parentTr = arg_2_0._tf.parent
	arg_2_0.resourcesTF = arg_2_0:findTF("resources", arg_2_0.frame)
	arg_2_0.oilTF = arg_2_0:findTF("canteen/bubble/Text", arg_2_0.resourcesTF):GetComponent(typeof(Text))
	arg_2_0.goldTF = arg_2_0:findTF("merchant/bubble/Text", arg_2_0.resourcesTF):GetComponent(typeof(Text))
	arg_2_0.classTF = arg_2_0:findTF("class/bubble/Text", arg_2_0.resourcesTF):GetComponent(typeof(Text))
	arg_2_0.oilbubbleTF = arg_2_0:findTF("canteen/bubble", arg_2_0.resourcesTF)
	arg_2_0.goldbubbleTF = arg_2_0:findTF("merchant/bubble", arg_2_0.resourcesTF)
	arg_2_0.classbubbleTF = arg_2_0:findTF("class/bubble", arg_2_0.resourcesTF)
	arg_2_0.oilbubbleCG = GetOrAddComponent(arg_2_0.oilbubbleTF, typeof(CanvasGroup))
	arg_2_0.goldbubbleCG = GetOrAddComponent(arg_2_0.goldbubbleTF, typeof(CanvasGroup))
	arg_2_0.classbubbleCG = GetOrAddComponent(arg_2_0.classbubbleTF, typeof(CanvasGroup))

	local var_2_0 = getProxy(NavalAcademyProxy):GetClassVO():GetResourceType()
	local var_2_1 = Item.getConfigData(var_2_0).icon

	arg_2_0.classbubbleTF:Find("icon"):GetComponent(typeof(Image)).sprite = LoadSprite(var_2_1)
	arg_2_0.projectContainer = arg_2_0:findTF("main/content", arg_2_0.frame)
	arg_2_0.items = {
		CommissionInfoEventItem.New(arg_2_0:findTF("frame/main/content/event"), arg_2_0),
		CommissionInfoClassItem.New(arg_2_0:findTF("frame/main/content/class"), arg_2_0),
		CommissionInfoTechnologyItem.New(arg_2_0:findTF("frame/main/content/technology"), arg_2_0)
	}

	arg_2_0:BlurPanel()

	arg_2_0.linkBtnPanel = arg_2_0:findTF("frame/link_btns/btns")
	arg_2_0.activityInsBtn = arg_2_0:findTF("frame/link_btns/btns/ins")
	arg_2_0.activtyUrExchangeBtn = arg_2_0:findTF("frame/link_btns/btns/urEx")
	arg_2_0.activtyUrExchangeTxt = arg_2_0:findTF("frame/link_btns/btns/urEx/Text"):GetComponent(typeof(Text))
	arg_2_0.activtyUrExchangeCG = arg_2_0.activtyUrExchangeBtn:GetComponent(typeof(CanvasGroup))
	arg_2_0.activtyUrExchangeTip = arg_2_0:findTF("frame/link_btns/btns/urEx/tip")
	arg_2_0.activityCrusingBtn = arg_2_0:findTF("frame/link_btns/btns/crusing")
	arg_2_0.metaBossBtn = CommissionMetaBossBtn.New(arg_2_0:findTF("frame/link_btns/btns/meta_boss"), arg_2_0.event)
end

function var_0_0.BlurPanel(arg_3_0)
	pg.UIMgr.GetInstance():BlurPanel(arg_3_0._tf, false, {
		weight = LayerWeightConst.SECOND_LAYER
	})
end

function var_0_0.UnBlurPanel(arg_4_0)
	pg.UIMgr.GetInstance():UnblurPanel(arg_4_0._tf, arg_4_0.parentTr)
end

function var_0_0.UpdateUrItemEntrance(arg_5_0)
	if not LOCK_UR_SHIP then
		local var_5_0 = pg.gameset.urpt_chapter_max.description
		local var_5_1 = var_5_0[1]
		local var_5_2 = var_5_0[2]
		local var_5_3 = getProxy(BagProxy):GetLimitCntById(var_5_1)

		arg_5_0.activtyUrExchangeTxt.text = var_5_3 .. "/" .. var_5_2

		local var_5_4 = var_5_3 == var_5_2

		arg_5_0.activtyUrExchangeCG.alpha = var_5_4 and 0.6 or 1

		setActive(arg_5_0.activtyUrExchangeTip, NotifyTipHelper.ShouldShowUrTip())
		onButton(arg_5_0, arg_5_0.activtyUrExchangeBtn, function()
			arg_5_0:emit(CommissionInfoMediator.ON_UR_ACTIVITY)
		end, SFX_PANEL)
	else
		setActive(arg_5_0.activtyUrExchangeBtn, false)
	end
end

function var_0_0.updateCrusingEntrance(arg_7_0)
	local var_7_0 = getProxy(ActivityProxy):getAliveActivityByType(ActivityConst.ACTIVITY_TYPE_PT_CRUSING)

	if var_7_0 and not var_7_0:isEnd() then
		setActive(arg_7_0.activityCrusingBtn, true)

		local var_7_1 = var_7_0:GetCrusingInfo()

		setText(arg_7_0.activityCrusingBtn:Find("Text"), var_7_1.phase .. "/" .. #var_7_1.awardList)
		setActive(arg_7_0.activityCrusingBtn:Find("tip"), #var_7_0:GetCrusingUnreceiveAward() > 0)
	else
		setActive(arg_7_0.activityCrusingBtn, false)
	end

	onButton(arg_7_0, arg_7_0.activityCrusingBtn, function()
		arg_7_0:emit(CommissionInfoMediator.ON_CRUSING)
	end, SFX_PANEL)
end

function var_0_0.NotifyIns(arg_9_0, arg_9_1, arg_9_2)
	local var_9_0 = arg_9_1:ExistMsg() and (not arg_9_2 or arg_9_2:isEnd())

	setActive(arg_9_0.activityInsBtn, var_9_0)

	if var_9_0 then
		onButton(arg_9_0, arg_9_0.activityInsBtn, function()
			arg_9_0:emit(CommissionInfoMediator.ON_INS)
		end, SFX_PANEL)
	end
end

function var_0_0.UpdateLinkPanel(arg_11_0)
	local var_11_0 = false

	for iter_11_0 = 1, arg_11_0.linkBtnPanel.childCount do
		if isActive(arg_11_0.linkBtnPanel:GetChild(iter_11_0 - 1)) then
			var_11_0 = true

			break
		end
	end

	setActive(arg_11_0.linkBtnPanel.parent, var_11_0)
end

function var_0_0.didEnter(arg_12_0)
	onButton(arg_12_0, arg_12_0.oilbubbleTF, function()
		if arg_12_0.isPaying then
			return
		end

		if not getProxy(PlayerProxy):getRawData():CanGetResource(PlayerConst.ResOil) then
			pg.TipsMgr.GetInstance():ShowTips(i18n("player_harvestResource_error_fullBag"))

			return
		end

		arg_12_0:PlayGetResAnimation(arg_12_0.oilbubbleTF, function()
			arg_12_0:emit(CommissionInfoMediator.GET_OIL_RES)
		end)
	end, SFX_PANEL)
	onButton(arg_12_0, arg_12_0.goldbubbleTF, function()
		if arg_12_0.isPaying then
			return
		end

		if not getProxy(PlayerProxy):getRawData():CanGetResource(PlayerConst.ResGold) then
			pg.TipsMgr.GetInstance():ShowTips(i18n("player_harvestResource_error_fullBag"))

			return
		end

		arg_12_0:PlayGetResAnimation(arg_12_0.goldbubbleTF, function()
			arg_12_0:emit(CommissionInfoMediator.GET_GOLD_RES)
		end)
	end, SFX_PANEL)
	onButton(arg_12_0, arg_12_0.classbubbleTF, function()
		if arg_12_0.isPaying then
			return
		end

		if not getProxy(NavalAcademyProxy):GetClassVO():CanGetRes() then
			pg.TipsMgr.GetInstance():ShowTips(i18n("player_harvestResource_error_fullBag"))

			return
		end

		arg_12_0:PlayGetResAnimation(arg_12_0.classbubbleTF, function()
			arg_12_0:emit(CommissionInfoMediator.GET_CLASS_RES)
		end)
	end, SFX_PANEL)
	onButton(arg_12_0, arg_12_0._tf, function()
		if arg_12_0.contextData.inFinished then
			return
		end

		arg_12_0.isPaying = true

		arg_12_0:PlayExitAnimation(function()
			arg_12_0:emit(var_0_0.ON_CLOSE)

			arg_12_0.isPaying = false
		end)
	end, SOUND_BACK)
	arg_12_0:InitItems()
	arg_12_0:UpdateUrItemEntrance()
	arg_12_0:updateCrusingEntrance()
	arg_12_0.metaBossBtn:Flush()
end

function var_0_0.PlayGetResAnimation(arg_21_0, arg_21_1, arg_21_2)
	arg_21_0.isPaying = true

	local var_21_0 = arg_21_1:GetComponent(typeof(Animation))
	local var_21_1 = arg_21_1:GetComponent(typeof(DftAniEvent))

	var_21_1:SetEndEvent(nil)
	var_21_1:SetEndEvent(function()
		var_21_1:SetEndEvent(nil)
		arg_21_2()

		arg_21_0.isPaying = false
	end)
	var_21_0:Play("anim_commission_bubble_get")
end

function var_0_0.InitItems(arg_23_0)
	for iter_23_0, iter_23_1 in ipairs(arg_23_0.items) do
		iter_23_1:Init()
	end
end

function var_0_0.OnUpdateEventInfo(arg_24_0)
	arg_24_0.items[1]:Update()
end

function var_0_0.OnUpdateClass(arg_25_0)
	arg_25_0.items[2]:Update()
end

function var_0_0.OnUpdateTechnology(arg_26_0)
	arg_26_0.items[3]:Update()
end

function var_0_0.setPlayer(arg_27_0, arg_27_1)
	arg_27_0.playerVO = arg_27_1

	arg_27_0:updateResource(arg_27_1)
end

function var_0_0.updateResource(arg_28_0, arg_28_1)
	local var_28_0 = getProxy(NavalAcademyProxy):GetClassVO():GetGenResCnt()

	arg_28_0.oilbubbleCG.alpha = 1
	arg_28_0.goldbubbleCG.alpha = 1
	arg_28_0.classbubbleCG.alpha = 1
	arg_28_0.oilbubbleTF.localScale = Vector3.one
	arg_28_0.goldbubbleTF.localScale = Vector3.one
	arg_28_0.classbubbleTF.localScale = Vector3.one

	setActive(arg_28_0.oilbubbleTF, arg_28_1.oilField ~= 0)
	setActive(arg_28_0.goldbubbleTF, arg_28_1.goldField ~= 0)
	setActive(arg_28_0.classbubbleTF, var_28_0 > 0)

	arg_28_0.oilTF.text = arg_28_1.oilField
	arg_28_0.goldTF.text = arg_28_1.goldField
	arg_28_0.classTF.text = var_28_0
end

function var_0_0.onBackPressed(arg_29_0)
	pg.CriMgr.GetInstance():PlaySoundEffect_V3(SFX_CANCEL)
	triggerButton(arg_29_0._tf)
end

function var_0_0.willExit(arg_30_0)
	arg_30_0:UnBlurPanel()

	for iter_30_0, iter_30_1 in ipairs(arg_30_0.items) do
		iter_30_1:Dispose()
	end

	arg_30_0.items = nil

	arg_30_0.metaBossBtn:Dispose()

	arg_30_0.metaBossBtn = nil
end

return var_0_0
