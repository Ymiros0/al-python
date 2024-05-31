pg = pg or {}

local var_0_0 = pg

var_0_0.BgmMgr = singletonClass("BgmMgr")

local var_0_1 = var_0_0.BgmMgr

def var_0_1.Ctor(arg_1_0):
	return

def var_0_1.Init(arg_2_0, arg_2_1):
	print("initializing bgm manager...")
	arg_2_0.Clear()
	arg_2_1()

def var_0_1.Clear(arg_3_0):
	arg_3_0._stack = {}
	arg_3_0._dictionary = {}

def var_0_1.CheckPlay(arg_4_0):
	if #arg_4_0._stack == 0:
		return

	local var_4_0 = arg_4_0._dictionary[arg_4_0._stack[#arg_4_0._stack]]

	if arg_4_0.isDirty or arg_4_0._now != var_4_0:
		arg_4_0._now = var_4_0

		arg_4_0.ContinuePlay()

def var_0_1.Push(arg_5_0, arg_5_1, arg_5_2):
	if not arg_5_0._dictionary[arg_5_1]:
		table.insert(arg_5_0._stack, arg_5_1)

	arg_5_0._dictionary[arg_5_1] = arg_5_2

	arg_5_0.CheckPlay()

def var_0_1.Pop(arg_6_0, arg_6_1):
	if arg_6_0._dictionary[arg_6_1]:
		table.removebyvalue(arg_6_0._stack, arg_6_1)

		arg_6_0._dictionary[arg_6_1] = None

		arg_6_0.CheckPlay()

def var_0_1.ContinuePlay(arg_7_0):
	arg_7_0.isDirty = False

	var_0_0.CriMgr.GetInstance().PlayBGM(arg_7_0._now)

def var_0_1.TempPlay(arg_8_0, arg_8_1):
	arg_8_0.isDirty = True

	var_0_0.CriMgr.GetInstance().PlayBGM(arg_8_1)

def var_0_1.StopPlay(arg_9_0):
	arg_9_0.isDirty = True

	var_0_0.CriMgr.GetInstance().StopBGM()
