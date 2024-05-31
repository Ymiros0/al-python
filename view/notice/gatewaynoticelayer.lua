﻿local var_0_0 = class("GatewayNoticeLayer", import("..base.BaseUI"))

function var_0_0.getUIName(arg_1_0)
	return "GatewayNoticeUI"
end

function var_0_0.init(arg_2_0)
	arg_2_0.trFrame = arg_2_0:findTF("frame")
	arg_2_0.txtTitle = arg_2_0:findTF("frame/title"):GetComponent("Text")
	arg_2_0.txtContent = arg_2_0:findTF("frame/content"):GetComponent("RichText")
	arg_2_0.btnBack = arg_2_0:findTF("frame/title_pop/btnBack")
end

function var_0_0.didEnter(arg_3_0)
	onButton(arg_3_0, arg_3_0.btnBack, function()
		arg_3_0:showNext()
	end)
	pg.UIMgr.GetInstance():BlurPanel(arg_3_0._tf, false)
end

function var_0_0.updateNotices(arg_5_0, arg_5_1)
	arg_5_0.notices = arg_5_1

	arg_5_0:showNext()
end

function var_0_0.showNext(arg_6_0)
	if arg_6_0.notice then
		arg_6_0.notice:markAsRead()
	end

	if #arg_6_0.notices > 0 then
		arg_6_0.notice = table.remove(arg_6_0.notices, 1)
		arg_6_0.txtTitle.text = arg_6_0.notice.title
		arg_6_0.txtContent.text = arg_6_0.notice.content

		local var_6_0 = arg_6_0.trFrame:GetComponent("CanvasGroup")

		LeanTween.cancel(go(arg_6_0.trFrame))
		LeanTween.value(go(arg_6_0.trFrame), 0, 1, 0.3):setEase(LeanTweenType.easeOutBack):setOnUpdate(System.Action_float(function(arg_7_0)
			var_6_0.alpha = arg_7_0
			arg_6_0.trFrame.localScale = Vector3(0.8, 0.8, 1) + Vector3(0.2, 0.2, 0) * arg_7_0
		end))
		pg.CriMgr.GetInstance():PlaySoundEffect_V3(SFX_PANEL)
	else
		arg_6_0:emit(BaseUI.ON_CLOSE)
		pg.CriMgr.GetInstance():PlaySoundEffect_V3(SFX_CANCEL)
	end
end

function var_0_0.willExit(arg_8_0)
	LeanTween.cancel(go(arg_8_0.trFrame))
	pg.UIMgr.GetInstance():UnblurPanel(arg_8_0._tf)
end

return var_0_0
