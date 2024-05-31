local var_0_0 = class("TaskPtAwardWindow", import("..activity.Panels.PtAwardWindow"))

def var_0_0.UpdateList(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	assert(#arg_1_1 == #arg_1_2)
	arg_1_0.UIlist.make(function(arg_2_0, arg_2_1, arg_2_2)
		if arg_2_0 == UIItemList.EventUpdate:
			local var_2_0 = arg_1_1[arg_2_1 + 1]

			arg_1_0.UpdateDrop(arg_2_2.Find("award"), var_2_0[1])
			arg_1_0.UpdateDrop(arg_2_2.Find("award1"), var_2_0[2])

			local var_2_1 = arg_1_2[arg_2_1 + 1]

			setText(arg_2_2.Find("title/Text"), "PHASE " .. arg_2_1 + 1)
			setText(arg_2_2.Find("target/Text"), var_2_1)
			setText(arg_2_2.Find("target/title"), arg_1_0.resTitle)
			setActive(arg_2_2.Find("award/mask"), arg_2_1 + 1 <= arg_1_3)
			setActive(arg_2_2.Find("award1/mask"), arg_2_1 + 1 <= arg_1_3)

			if arg_2_2.Find("target/icon"):
				if arg_1_0.resIcon == "":
					arg_1_0.resIcon = None

				if arg_1_0.resIcon:
					LoadImageSpriteAsync(arg_1_0.resIcon, arg_2_2.Find("target/icon"), False)

				setActive(arg_2_2.Find("target/icon"), arg_1_0.resIcon)
				setActive(arg_2_2.Find("target/mark"), arg_1_0.resIcon))
	arg_1_0.UIlist.align(#arg_1_1)

def var_0_0.UpdateDrop(arg_3_0, arg_3_1, arg_3_2):
	if arg_3_2:
		setActive(arg_3_1, True)

		local var_3_0 = {
			type = arg_3_2[1],
			id = arg_3_2[2],
			count = arg_3_2[3]
		}

		updateDrop(arg_3_1, var_3_0, {
			hideName = True
		})
		onButton(arg_3_0.binder, arg_3_1, function()
			arg_3_0.binder.emit(BaseUI.ON_DROP, var_3_0), SFX_PANEL)
	else
		setActive(arg_3_1, False)

return var_0_0
