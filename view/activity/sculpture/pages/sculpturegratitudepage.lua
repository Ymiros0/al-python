﻿local var_0_0 = class("SculptureGratitudePage", import("view.base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "SculptureGratitudeUI"
end

function var_0_0.OnLoaded(arg_2_0)
	arg_2_0.backBtn = arg_2_0:findTF("back")
	arg_2_0.roleImg = arg_2_0:findTF("char/Image")
	arg_2_0.container = arg_2_0:findTF("frame/gift")
	arg_2_0.awards = arg_2_0:findTF("frame/awards")
	arg_2_0.giftBg = arg_2_0:findTF("frame/Image")
	arg_2_0.wordTxtScr = arg_2_0:findTF("frame/scrollrect")
	arg_2_0.wordTxt = arg_2_0:findTF("frame/scrollrect/content/Text"):GetComponent(typeof(Text))
	arg_2_0.typer = arg_2_0:findTF("frame/scrollrect/content/Text"):GetComponent(typeof(Typewriter))
	arg_2_0.uilist = UIItemList.New(arg_2_0:findTF("frame/awards"), arg_2_0:findTF("frame/awards/tpl"))
	arg_2_0.arrLeft = arg_2_0:findTF("frame/arr")
	arg_2_0.arrRight = arg_2_0:findTF("frame/arr (1)")
end

function var_0_0.OnInit(arg_3_0)
	return
end

function var_0_0.Show(arg_4_0, arg_4_1, arg_4_2, arg_4_3)
	arg_4_0:Clear()
	setText(arg_4_0:findTF("tip"), i18n("sculpture_gratitude_tip"))
	var_0_0.super.Show(arg_4_0)
	setActive(arg_4_0.giftBg, true)
	setAnchoredPosition(arg_4_0.arrLeft, {
		x = 338
	})
	setAnchoredPosition(arg_4_0.arrRight, {
		x = 675
	})

	if arg_4_3 then
		arg_4_3()
	end

	arg_4_0.id = arg_4_1
	arg_4_0.activity = arg_4_2

	arg_4_0:SetScrollTxt(arg_4_2:getDataConfig(arg_4_0.id, "words"))
	seriesAsync({
		function(arg_5_0)
			arg_4_0:LoadChar(arg_5_0)
		end,
		function(arg_6_0)
			arg_4_0:LoadSculpture(arg_6_0)
		end
	}, function()
		arg_4_0:RegisterEvent()
	end)
	pg.BgmMgr.GetInstance():Push(arg_4_0.__cname, "story-richang-8")
end

function var_0_0.Flush(arg_8_0, arg_8_1)
	arg_8_0.activity = arg_8_1

	local var_8_0 = arg_8_0.activity:GetSculptureState(arg_8_0.id)

	if var_8_0 == SculptureActivity.STATE_FINSIH then
		arg_8_0:Clear()

		local var_8_1, var_8_2, var_8_3 = arg_8_0:State2CharNameAndActionName(var_8_0)

		arg_8_0:UpdateRole(var_8_1, var_8_2, var_8_3)
		setActive(arg_8_0.container, false)
		setActive(arg_8_0.awards, true)
		arg_8_0:InitAwards()
		arg_8_0:SetScrollTxt(arg_8_1:getDataConfig(arg_8_0.id, "thankwords"))
		setText(arg_8_0:findTF("tip"), "")
		setActive(arg_8_0.giftBg, false)
		setAnchoredPosition(arg_8_0.arrLeft, {
			x = 260
		})
		setAnchoredPosition(arg_8_0.arrRight, {
			x = 745
		})
	end
end

function var_0_0.SetScrollTxt(arg_9_0, arg_9_1)
	arg_9_0.typer:setSpeed(99999)

	arg_9_0.wordTxt.text = HXSet.hxLan(arg_9_1)

	arg_9_0.typer:setSpeed(0.06)

	function arg_9_0.typer.endFunc()
		arg_9_0:RemoveTimer()
	end

	arg_9_0.typer:Play()
	arg_9_0:RemoveTimer()

	arg_9_0.timer = Timer.New(function()
		scrollToBottom(arg_9_0.wordTxtScr)
	end, 0.1, -1)

	arg_9_0.timer:Start()
end

function var_0_0.RemoveTimer(arg_12_0)
	if arg_12_0.timer then
		arg_12_0.timer:Stop()

		arg_12_0.timer = nil
	end
end

function var_0_0.InitAwards(arg_13_0)
	local var_13_0 = arg_13_0.activity:getDataConfig(arg_13_0.id, "reward_display")

	arg_13_0.uilist:make(function(arg_14_0, arg_14_1, arg_14_2)
		if arg_14_0 == UIItemList.EventUpdate then
			local var_14_0 = var_13_0[arg_14_1 + 1]
			local var_14_1 = {
				type = var_14_0[1],
				id = var_14_0[2],
				count = var_14_0[3]
			}

			updateDrop(arg_14_2, var_14_1)
			onButton(arg_13_0, arg_14_2, function()
				arg_13_0:emit(BaseUI.ON_DROP, var_14_1)
			end, SFX_PANEL)
		end
	end)
	arg_13_0.uilist:align(#var_13_0)
end

function var_0_0.LoadChar(arg_16_0, arg_16_1)
	local var_16_0 = arg_16_0.activity:GetSculptureState(arg_16_0.id)
	local var_16_1, var_16_2, var_16_3 = arg_16_0:State2CharNameAndActionName(var_16_0)

	arg_16_0:UpdateRole(var_16_1, var_16_2, var_16_3, arg_16_1)
end

function var_0_0.State2CharNameAndActionName(arg_17_0, arg_17_1)
	local var_17_0 = arg_17_0.activity:GetResorceName(arg_17_0.id)

	if arg_17_1 == SculptureActivity.STATE_FINSIH then
		return var_17_0, "gift_get_", "take_wait_"
	else
		return var_17_0, "gift_wait_"
	end
end

function var_0_0.LoadSculpture(arg_18_0, arg_18_1)
	local var_18_0 = arg_18_0.activity:GetResorceName(arg_18_0.id)

	ResourceMgr.Inst:getAssetAsync("ui/" .. var_18_0 .. "_puzzle_whole", "", UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_19_0)
		local var_19_0 = Object.Instantiate(arg_19_0, arg_18_0.container)

		var_19_0.transform.localScale = arg_18_0.activity:GetScale(arg_18_0.id)

		arg_18_0:InitSculpture(var_19_0.transform)

		arg_18_0.puzzle = var_19_0

		arg_18_1()
	end), true, true)
end

function var_0_0.InitSculpture(arg_20_0, arg_20_1)
	local var_20_0 = GetOrAddComponent(arg_20_1, typeof(EventTriggerListener))
	local var_20_1

	var_20_0:AddBeginDragFunc(function()
		arg_20_1:SetAsLastSibling()

		var_20_1 = arg_20_1.localPosition
	end)
	var_20_0:AddDragFunc(function(arg_22_0, arg_22_1)
		local var_22_0 = Screen2Local(arg_20_1.parent, arg_22_1.position)

		arg_20_1.localPosition = var_22_0
	end)
	var_20_0:AddDragEndFunc(function(arg_23_0, arg_23_1)
		local var_23_0 = arg_20_0.roleImg.gameObject.transform
		local var_23_1 = getBounds(var_23_0)
		local var_23_2 = getBounds(arg_20_1)

		if var_23_1:Intersects(var_23_2) then
			arg_20_1.localPosition = TrPosition2LocalPos(var_23_0.parent, arg_20_1.parent, var_23_0.localPosition)

			arg_20_0:emit(SculptureMediator.ON_FINSIH_SCULPTURE, arg_20_0.id)
		else
			arg_20_1.localPosition = var_20_1
		end
	end)
end

function var_0_0.UpdateRole(arg_24_0, arg_24_1, arg_24_2, arg_24_3, arg_24_4)
	if arg_24_0.charName == arg_24_1 then
		return
	end

	arg_24_0:ClearChar()
	PoolMgr.GetInstance():GetSpineChar("takegift_" .. arg_24_1, true, function(arg_25_0)
		arg_25_0.transform:SetParent(arg_24_0.roleImg.gameObject.transform.parent)

		arg_25_0.transform.localScale = Vector3(1, 1, 0)
		arg_25_0.transform.localPosition = Vector3(0, 0, 0)

		local var_25_0 = arg_25_0:GetComponent(typeof(SpineAnimUI))

		var_25_0:SetAction(arg_24_2 .. arg_24_1, 0)

		if arg_24_3 then
			var_25_0:SetActionCallBack(function(arg_26_0)
				if arg_26_0 == "finish" then
					var_25_0:SetActionCallBack(nil)
					var_25_0:SetAction(arg_24_3 .. arg_24_1, 0)
				end
			end)
		end

		arg_24_0.spineAnimUI = var_25_0
		arg_24_0.charGo = arg_25_0

		if arg_24_4 then
			arg_24_4()
		end
	end)

	arg_24_0.charName = arg_24_1
end

function var_0_0.ClearChar(arg_27_0)
	if arg_27_0.charName and arg_27_0.charGo then
		if arg_27_0.spineAnimUI then
			arg_27_0.spineAnimUI:SetActionCallBack(nil)

			arg_27_0.spineAnimUI = nil
		end

		PoolMgr.GetInstance():ReturnSpineChar(arg_27_0.charName, arg_27_0.charGo)

		arg_27_0.charName = nil
		arg_27_0.charGo = nil
	end
end

function var_0_0.RegisterEvent(arg_28_0)
	onButton(arg_28_0, arg_28_0.backBtn, function()
		arg_28_0:Hide()
	end, SFX_PANEL)
end

function var_0_0.Clear(arg_30_0)
	if arg_30_0.puzzle then
		local var_30_0 = arg_30_0.puzzle:GetComponent(typeof(EventTriggerListener))

		ClearEventTrigger(var_30_0)
		Object.Destroy(arg_30_0.puzzle.gameObject)

		arg_30_0.puzzle = nil
	end

	arg_30_0:ClearChar()
	setActive(arg_30_0.container, true)
	setActive(arg_30_0.awards, false)
end

function var_0_0.Hide(arg_31_0)
	var_0_0.super.Hide(arg_31_0)
	pg.BgmMgr.GetInstance():Pop(arg_31_0.__cname)
	arg_31_0:RemoveTimer()
end

function var_0_0.OnDestroy(arg_32_0)
	arg_32_0:Clear()
end

return var_0_0
