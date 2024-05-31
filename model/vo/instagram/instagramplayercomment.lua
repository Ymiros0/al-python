﻿local var_0_0 = class("InstagramPlayerComment", import(".InstagramComment"))

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4)
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4)

	if arg_1_1.npc_reply ~= 0 then
		local var_1_0 = arg_1_0.level + 1
		local var_1_1 = InstagramNpcComment.New(arg_1_0.allReply[arg_1_1.npc_reply], arg_1_2, var_1_0, arg_1_0)

		table.insert(arg_1_0.replyList, var_1_1)
	end
end

function var_0_0.GetName(arg_2_0)
	return getProxy(PlayerProxy):getData().name
end

function var_0_0.GetPainting(arg_3_0)
	return "ui/InstagramUI_atlas", "txdi_3"
end

function var_0_0.GetType(arg_4_0)
	return Instagram.TYPE_PLAYER_COMMENT
end

return var_0_0
