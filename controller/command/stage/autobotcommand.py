
from luatable import table

from Framework.puremvc.patterns.command.SimpleCommand import SimpleCommand
from const import *
from support.helpers.UnitySupport import onDelayTick, GetComponent #!
from support.helpers.M02 import getProxy #!
from Framework.tolua.typeof import typeof #!
from Framework.tolua.tolua import Toggle, PlayerPrefs #!
from mgr import TipsMgr, MsgboxMgr #!
from mgr.const import LayerWeightConst
from Framework.i18n import i18n #!
import controller.const.game as GAME
from model.proxy.chapterproxy import ChapterProxy #!
from model.proxy.PlayerProxy import PlayerProxy #!
from model.proxy.SettingsProxy import SettingsProxy #!

class AutoBotCommand(SimpleCommand):
	def execute(self, arg_1_1):
		var_1_0 = arg_1_1.getBody()
		bot_active = var_1_0.isActiveBot
		toggle = var_1_0.toggle
		system = var_1_0.system
		auto_bot_mark = self.GetAutoBotMark(system)

		if self.autoBotSatisfied():
			if PlayerPrefs.GetInt("autoBotIsAcitve" + auto_bot_mark, 0) == (not bot_active):
				pass #-- block empty
			else:
				PlayerPrefs.SetInt("autoBotIsAcitve" + auto_bot_mark, not bot_active and 1 or 0)
				self.activeBotHelp(not bot_active)
		elif not bot_active:
			if toggle:
				def turn_off_toggle():
					GetComponent(toggle, typeof(Toggle)).isOn = False
				onDelayTick(turn_off_toggle, 0.1)

			TipsMgr.GetInstance().ShowTips(i18n("auto_battle_limit_tip"))

		if bot_active:
			self.sendNotification(GAME.AUTO_SUB, table(
				isActiveSub = True,
				system = system
			))

	@staticmethod
	def autoBotSatisfied():
		var_3_0 = getProxy(ChapterProxy)

		return var_3_0 and var_3_0.getChapterById(AUTO_ENABLE_CHAPTER).isClear()

	@staticmethod
	def activeBotHelp(arg_4_0):
		var_4_0 = getProxy(PlayerProxy)

		if not arg_4_0:
			if autoBotHelp:
				MsgboxMgr.GetInstance().hide()

			return

		if var_4_0.botHelp:
			return

		autoBotHelp = True

		if getProxy(SettingsProxy).isTipAutoBattle():
			def onCallback():
				if MsgboxMgr.GetInstance().stopRemindToggle.isOn:
					getProxy(SettingsProxy).setAutoBattleTip()
			def onClose():
				autoBotHelp = False

				if MsgboxMgr.GetInstance().stopRemindToggle.isOn:
					getProxy(SettingsProxy).setAutoBattleTip()
			MsgboxMgr.GetInstance().ShowMsgBox(table(
				showStopRemind = True,
				toggleStatus = True,
				type = MsgboxMgr.MSGBOX_TYPE_HELP,
				helps = i18n("help_battle_auto"),
				onCallback = onCallback,
				custom = table(
					table(
						text = "text_iknow",
						sound = SFX_CANCEL,
					)
				),
				onClose = onClose,
				weight = LayerWeightConst.TOP_LAYER
			))

		var_4_0.botHelp = True

	@staticmethod
	def GetAutoBotMark(system):
		if system == SYSTEM_WORLD or system == SYSTEM_WORLD_BOSS:
			return "_" + SYSTEM_WORLD
		elif system == SYSTEM_GUILD:
			return "_" + SYSTEM_GUILD
		else:
			return ""