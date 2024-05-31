local var_0_0 = class("MailRedDotNode4Mellow", import(".RedDotNode"))
local var_0_1 = 99

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0._attachmentHint = findTF(arg_1_1, "tip")
	arg_1_0._attachmentCountText = findTF(arg_1_1, "Text"):GetComponent(typeof(Text))

	var_0_0.super.Ctor(arg_1_0, arg_1_1, {
		pg.RedDotMgr.TYPES.MAIL
	})
end

function var_0_0.GetName(arg_2_0)
	return arg_2_0.gameObject.name
end

function var_0_0.Init(arg_3_0)
	var_0_0.super.Init(arg_3_0)

	local var_3_0 = getProxy(MailProxy)

	if var_3_0.total >= MAIL_COUNT_LIMIT then
		pg.TipsMgr.GetInstance():ShowTips(i18n("warning_mail_max_2"))
	elseif var_3_0.total > MAIL_COUNT_LIMIT * 0.9 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("warning_mail_max_1", var_3_0.total, MAIL_COUNT_LIMIT))
	end
end

function var_0_0.SetData(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_1

	if var_4_0 > 0 then
		SetActive(arg_4_0._attachmentHint, true)

		if var_4_0 > var_0_1 then
			arg_4_0._attachmentCountText.text = var_0_1 .. "+"
		else
			arg_4_0._attachmentCountText.text = var_4_0
		end
	else
		SetActive(arg_4_0._attachmentHint, false)

		arg_4_0._attachmentCountText.text = ""
	end
end

return var_0_0
