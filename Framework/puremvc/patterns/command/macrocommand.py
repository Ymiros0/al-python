local var_0_0 = import("..observer.Notifier")
local var_0_1 = class("MacroCommand", var_0_0)

def var_0_1.Ctor(arg_1_0):
	var_0_1.super.Ctor(arg_1_0)

	arg_1_0.subCommands = {}

	arg_1_0.initializeMacroCommand()

def var_0_1.initializeMacroCommand(arg_2_0):
	return

def var_0_1.addSubCommand(arg_3_0, arg_3_1):
	table.insert(arg_3_0.subCommands, arg_3_1)

def var_0_1.execute(arg_4_0, arg_4_1):
	while #arg_4_0.subCommands > 0:
		local var_4_0 = table.remove(arg_4_0.subCommands, 1).New()

		var_4_0.initializeNotifier(arg_4_0.multitonKey)
		var_4_0.execute(arg_4_1)

return var_0_1
