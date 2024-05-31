local var_0_0 = class("Server", import(".BaseVO"))

var_0_0.STATUS = {
	REGISTER_FULL = 3,
	VINDICATE = 1,
	NORMAL = 0,
	FULL = 2
}

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1.id
	arg_1_0.status = arg_1_1.status or var_0_0.STATUS.NORMAL
	arg_1_0.name = arg_1_1.name

	local var_1_0 = arg_1_1.tag_state or 0

	arg_1_0.isHot = var_1_0 == 1
	arg_1_0.isNew = var_1_0 == 2
	arg_1_0.isLogined = False
	arg_1_0.sortIndex = arg_1_1.sort or arg_1_0.id
	arg_1_0.host = arg_1_1.host
	arg_1_0.port = arg_1_1.port
	arg_1_0.proxyHost = arg_1_1.proxy_host
	arg_1_0.proxyPort = arg_1_1.proxy_port

def var_0_0.getHost(arg_2_0):
	if VersionMgr.Inst.OnProxyUsing() and arg_2_0.proxyHost != None and arg_2_0.proxyHost != "":
		return arg_2_0.proxyHost

	return arg_2_0.host

def var_0_0.getPort(arg_3_0):
	if VersionMgr.Inst.OnProxyUsing() and arg_3_0.proxyPort != None and arg_3_0.proxyPort != 0:
		return arg_3_0.proxyPort

	return arg_3_0.port

return var_0_0
