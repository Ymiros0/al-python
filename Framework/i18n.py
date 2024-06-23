from Framework.lang import zh_cn as var_0_1
from lib import ALJsonAPI
api = ALJsonAPI()

def l10n(arg_1_0):
	return var_0_1[arg_1_0] or arg_1_0

def i18n(arg_2_0, *args):
	gametip = api.get_sharecfgmodule('gametip')
	var_2_0 = gametip[arg_2_0] #Use api

	if var_2_0:
		var_2_1 = var_2_0.tip

		for i, j in enumerate(args):
			var_2_1 = var_2_1.replace(f"${i+1}", j)

		return var_2_1
	else:
		return i18n_not_find(arg_2_0)

def i18n_not_find(arg_3_0):
	return f"UndefinedLanguage.{arg_3_0}"

def i18n1(arg_4_0, *args):
	return l10n(arg_4_0) % (args)

def i18n2(arg_5_0, *args):
	gameset_language_client = api.get_sharecfgmodule('gameset_language_client')
	var_5_0 = gameset_language_client[arg_5_0] #Use api

	if var_5_0:
		var_5_1 = var_5_0.value

		for i, j in enumerate(args):
			var_5_1 = var_5_1.replace(f"${i+1}", j)

		return var_5_1
	else:
		return arg_5_0
