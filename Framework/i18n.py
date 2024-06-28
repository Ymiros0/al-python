from Framework.lang import zh_cn as var_0_1
from lib import pg


def l10n(arg_1_0):
	return var_0_1[arg_1_0] or arg_1_0

def i18n(arg_2_0, *args):
	var_2_0 = pg.gametip[arg_2_0]

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
	var_5_0 = pg.gameset_language_client[arg_5_0]

	if var_5_0:
		var_5_1 = var_5_0.value

		for i, j in enumerate(args):
			var_5_1 = var_5_1.replace(f"${i+1}", j)

		return var_5_1
	else:
		return arg_5_0
