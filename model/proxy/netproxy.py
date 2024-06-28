from luatable import table, ipairs, Clone

from Framework.puremvc.patterns.proxy.Proxy import Proxy
from mgr.ConnectionMgr import ConnectionMgr
class NetProxy(Proxy):
	def onRegister(arg_1_0):
		arg_1_0.event = {}

		arg_1_0.register()

	def register(arg_2_0):
		return

	def on(arg_3_0, arg_3_1, arg_3_2):
		ConnectionMgr.GetInstance().On(arg_3_1, lambda arg_4_0: arg_3_2(arg_4_0))
		table.insert(arg_3_0.event, arg_3_1)

	def onRemove(arg_5_0):
		arg_5_0.remove()

		for iter_5_0, iter_5_1 in ipairs(arg_5_0.event):
			ConnectionMgr.GetInstance().Off(iter_5_1)

	def remove(arg_6_0):
		return

	def getRawData(arg_7_0):
		return arg_7_0.data

	def getData(arg_8_0):
		return Clone(arg_8_0.data)

