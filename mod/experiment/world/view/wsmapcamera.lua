﻿local var_0_0 = class("WSMapCamera", import("...BaseEntity"))

var_0_0.Fields = {
	map = "table",
	camera = "userdata",
	gid = "number"
}

function var_0_0.Setup(arg_1_0)
	arg_1_0:Init()
end

function var_0_0.Dispose(arg_2_0)
	arg_2_0.camera.enabled = false

	arg_2_0:Clear()
end

function var_0_0.UpdateMap(arg_3_0, arg_3_1)
	if arg_3_0.map ~= arg_3_1 or arg_3_0.gid ~= arg_3_1.gid then
		arg_3_0.map = arg_3_1
		arg_3_0.gid = arg_3_1.gid
		arg_3_0.camera.fieldOfView = arg_3_1.theme.fov
	end
end

function var_0_0.Init(arg_4_0)
	arg_4_0.camera.enabled = true
end

return var_0_0
