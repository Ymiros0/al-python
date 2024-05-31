﻿local var_0_0 = class("FileDownloadPanel", import(".MsgboxSubPanel"))

function var_0_0.getUIName(arg_1_0)
	return "FileDownloadBox"
end

function var_0_0.OnInit(arg_2_0)
	arg_2_0:findUI()
	arg_2_0:addListener()
end

function var_0_0.UpdateView(arg_3_0, arg_3_1)
	local var_3_0 = arg_3_1.onYes

	function arg_3_1.onYes()
		pg.FileDownloadMgr.GetInstance():SetRemind(arg_3_0.curStopValue)
		var_3_0()
	end

	arg_3_0:PreRefresh(arg_3_1)
	setText(arg_3_0.contextText, arg_3_1.content)

	rtf(arg_3_0.viewParent._window).sizeDelta = Vector2.New(1000, 638)

	arg_3_0:PostRefresh(arg_3_1)
end

function var_0_0.findUI(arg_5_0)
	arg_5_0.contextText = arg_5_0:findTF("Context")
	arg_5_0.toggleTF = arg_5_0:findTF("Toggle")
	arg_5_0.tickTF = arg_5_0:findTF("Tip/TickBG/Tick", arg_5_0.toggleTF)
end

function var_0_0.addListener(arg_6_0)
	arg_6_0.curStopValue = false

	onToggle(arg_6_0, arg_6_0.toggleTF, function(arg_7_0)
		arg_6_0.curStopValue = arg_7_0
	end, SFX_CONFIRM, SFX_CANCEL)
end

return var_0_0
