﻿local var_0_0 = class("MainActInsBtn", import(".MainBaseSpcailActBtn"))

function var_0_0.GetContainer(arg_1_0)
	return arg_1_0.root
end

function var_0_0.InShowTime(arg_2_0)
	local var_2_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_INSTAGRAM)

	return var_2_0 and not var_2_0:isEnd()
end

function var_0_0.GetUIName(arg_3_0)
	return "MainUIInsBtn"
end

function var_0_0.OnClick(arg_4_0)
	arg_4_0.event:emit(NewMainMediator.SKIP_INS)
end

function var_0_0.OnInit(arg_5_0)
	arg_5_0.animator = arg_5_0._tf:Find("icon"):GetComponent(typeof(Animator))

	local var_5_0 = getProxy(InstagramProxy):ShouldShowTip()

	arg_5_0.animator.enabled = var_5_0

	setActive(arg_5_0._tf:Find("Tip"), var_5_0)

	arg_5_0._tf.localScale = arg_5_0.isScale and Vector3(0.85, 0.85, 1) or Vector3(1, 1, 1)

	setAnchoredPosition(arg_5_0._tf, {
		y = arg_5_0.isScale and -950 or -752.5
	})
end

return var_0_0
