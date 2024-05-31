local var_0_0 = class("ServerNotice", import(".Notice"))

function var_0_0.Ctor(arg_1_0, arg_1_1)
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.version = arg_1_1.version
	arg_1_0.btnTitle = arg_1_1.btn_title
	arg_1_0.titleImage = arg_1_1.title_image
	arg_1_0.timeDes = arg_1_1.time_desc
	arg_1_0.type = arg_1_1.tag_type
	arg_1_0.icon = arg_1_1.icon
	arg_1_0.track = arg_1_1.track

	local var_1_0 = string.split(arg_1_0.title, "&")

	if #var_1_0 > 1 then
		arg_1_0.title = var_1_0[1]
		arg_1_0.pageTitle = var_1_0[2]
	else
		arg_1_0.title = var_1_0[1]
		arg_1_0.pageTitle = var_1_0[1]
	end
end

function var_0_0.prefKey(arg_2_0)
	return "ServerNotice" .. arg_2_0.id
end

return var_0_0
