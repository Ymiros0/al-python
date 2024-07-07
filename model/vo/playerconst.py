
from Framework.i18n import i18n
from const import *
from controller.const import game as GAME
from Framework import underscore
from lib import pg
from mod.experiment.world.model.World import World
from model.const import ActivityConst
from model.proxy.ActivityProxy import ActivityProxy
from model.proxy.BagProxy import BagProxy
from model.proxy.BayProxy import BayProxy
from model.proxy.CollectionProxy import CollectionProxy
from model.proxy.PlayerProxy import PlayerProxy
from packages.alsupport import tonumber
from packages.luatable import ipairs, pairs, setmetatable, table
from support.helpers.M02 import CompareFuncs, getProxy, nowWorld, switch
from drop import Drop
from Item import Item
from Player import id2res
from Ship import Ship


ResGold = 1
ResOil = 2
ResExploit = 3
ResDiamond = 4
ResOilField = 5
ResDormMoney = 6
ResGoldField = 7
ResGuildCoin = 8
ResBlueprintFragment = 9
ResClassField = 10
ResStoreGold = 16
ResStoreOil = 17
ResBattery = 101
ResPT = 102

var_0_1 = None

def var_0_2(arg_1_0):
	def _f1(arg_2_0):
			var_2_0 = getProxy(PlayerProxy)

			if var_2_0:
				var_2_0.UpdatePlayerRes(table(
					arg_2_0
				))
	def _f2(arg_3_0):
			var_3_0 = getProxy(BagProxy)

			if var_3_0:
				if arg_3_0.count > 0:
					var_3_0.addItemById(arg_3_0.id, arg_3_0.count)
				elif arg_3_0.count < 0:
					var_3_0.removeItemById(arg_3_0.id, -arg_3_0.count)
	def _f3(arg_4_0):
			var_4_0 = nowWorld()

			assert(var_4_0.type == World.TypeFull)

			var_4_1 = var_4_0.GetInventoryProxy()

			if var_4_1:
				if arg_4_0.count > 0:
					var_4_1.AddItem(arg_4_0.id, arg_4_0.count)
				elif arg_4_0.count < 0:
					var_4_1.RemoveItem(arg_4_0.id, -arg_4_0.count)
	var_0_1 = var_0_1 or table({
		DROP_TYPE_RESOURCE: _f1,
		DROP_TYPE_ITEM: _f2,
		DROP_TYPE_WORLD_ITEM: _f3
	})
	def _F():
		assert False
	switch(arg_1_0.type, var_0_1, _F, arg_1_0)

def addPlayerOwn(arg_6_0):
	arg_6_0.count = max(arg_6_0.count, 0)

	var_0_2(arg_6_0)

def reducePlayerOwn(arg_7_0):
	arg_7_0.count = -max(arg_7_0.count, 0)

	var_0_2(arg_7_0)

def addTranDrop(arg_8_0, arg_8_1):
	arg_8_0 = underscore.map(arg_8_0, lambda arg_9_0: Drop.New(table(
			type = arg_9_0.type,
			id = arg_9_0.id,
			count = arg_9_0.number
		)))

	var_8_0 = getProxy(BayProxy).getNewShip(False)
	var_8_1 = table()

	for iter_8_0, iter_8_1 in pairs(var_8_0):
		if iter_8_1.isMetaShip():
			table.insert(var_8_1, iter_8_1.configId)

	var_8_2 = table()

	for iter_8_2, iter_8_3 in ipairs(arg_8_0):
		var_8_3, var_8_4 = iter_8_3.DropTrans(var_8_1, arg_8_1)

		if var_8_3:
			table.insert(var_8_2, var_8_3)
			pg.m02.sendNotification(GAME.ADD_ITEM, var_8_3)

		if var_8_4:
			pg.m02.sendNotification(GAME.ADD_ITEM, var_8_4)

	if arg_8_1 and arg_8_1.taskId and pg.task_data_template[arg_8_1.taskId].auto_commit == 1:
		return table()
	else:
		return var_8_2

def BonusItemMarker(arg_10_0):
	var_10_0 = table()

	for iter_10_0, iter_10_1 in ipairs(arg_10_0):
		if iter_10_1.type == DROP_TYPE_VITEM and iter_10_1.getConfig("virtual_type") == 20:
			iter_10_1.catchupActTag = var_10_0[iter_10_1.id]
			var_10_0[iter_10_1.id] = True

	return arg_10_0

var_0_3 = None
var_0_4 = None

def MergePassItemDrop(arg_11_0):
	if not var_0_3:
		var_0_4 = table({
			DROP_TYPE_SKIN: 1,
			DROP_TYPE_SHIP: 9
		})
		var_0_3 = table()

		for iter_11_0, iter_11_1 in pairs(table({
			DROP_TYPE_RESOURCE: table({
				1: 8,
				2: 8,
				14: 2
			}),
			DROP_TYPE_ITEM: table({
				20001: 3,
				21101: 12,
				16502: 6,
				50006: 10,
				16004: 7,
				16024: 7,
				17023: 16,
				17024: 11,
				30035: 13,
				15008: 15,
				42036: 4,
				30025: 13,
				21131: 12,
				21121: 12,
				17013: 16,
				42030: 5,
				20013: 14,
				17044: 11,
				17004: 11,
				17014: 11,
				30015: 13,
				16014: 7,
				17003: 16,
				21111: 12,
				17043: 16,
				17034: 11,
				54007: 5,
				30045: 13,
				15001: 17,
				17033: 16
			})
		})):
			for iter_11_2, iter_11_3 in pairs(iter_11_1):
				var_0_3["%d_%d" % (iter_11_0, iter_11_2)] = iter_11_3

		def _index(arg_12_0, arg_12_1):
				var_12_0, var_12_1 = underscore.map(arg_12_1.split("_"), lambda arg_13_0: tonumber(arg_13_0)).values()

				if var_0_4[var_12_0]:
					arg_12_0[arg_12_1] = var_0_4[var_12_0]
				elif var_12_0 == DROP_TYPE_ITEM and Item.getConfigData(var_12_1).type == 13:
					arg_12_0[arg_12_1] = 9
				else:
					arg_12_0[arg_12_1] = 100

				return arg_12_0[arg_12_1]

		PassItemOrder = setmetatable(var_0_3, table(
			__index = _index
		))

	var_11_0 = MergeSameDrops(arg_11_0)

	table.sort(var_11_0, CompareFuncs(table(
		lambda arg_14_0: PassItemOrder[f"{arg_14_0.type}_{arg_14_0.id}"],
		lambda arg_15_0: arg_15_0.id
	)))

	return var_11_0

def CheckResForShopping(arg_16_0, arg_16_1):
	var_16_0 = arg_16_0.count * arg_16_1
	var_16_1 = 0

	if arg_16_0.type == DROP_TYPE_RESOURCE:
		var_16_1 = getProxy(PlayerProxy).getRawData().getResource(arg_16_0.id)
	elif arg_16_0.type == DROP_TYPE_ITEM:
		var_16_1 = getProxy(BagProxy).getItemCountById(arg_16_0.id)
	else:
		assert(False)

	return var_16_0 <= var_16_1

def ConsumeResForShopping(arg_17_0, arg_17_1):
	var_17_0 = arg_17_0.count * arg_17_1

	if arg_17_0.type == DROP_TYPE_RESOURCE:
		var_17_1 = getProxy(PlayerProxy).getData()

		var_17_1.consume(table({
			id2res(arg_17_0.id): var_17_0
		}))
		getProxy(PlayerProxy).updatePlayer(var_17_1)
	elif arg_17_0.type == DROP_TYPE_ITEM:
		getProxy(BagProxy).removeItemById(arg_17_0.id, var_17_0)
	else:
		assert(False)

def GetTranAwards(arg_18_0, arg_18_1):
	var_18_0 = table()
	var_18_1 = addTranDrop(arg_18_1.award_list)

	for iter_18_0, iter_18_1 in ipairs(var_18_0):
		if iter_18_1.type == DROP_TYPE_SHIP:
			var_18_2 = pg.ship_data_template[iter_18_1.id]

			if not getProxy(CollectionProxy).getShipGroup(var_18_2.group_type) and Ship.inUnlockTip(iter_18_1.id):
				pg.TipsMgr.GetInstance().ShowTips(i18n("collection_award_ship", var_18_2.name))

	if arg_18_0.isAwardMerge:
		var_18_1 = MergeSameDrops(var_18_1)

	return var_18_1

def MergeTechnologyAward(arg_19_0):
	var_19_0 = arg_19_0.items

	for iter_19_0, iter_19_1 in ipairs(arg_19_0.commons):
		iter_19_1.riraty = True

		table.insert(var_19_0, iter_19_1)

	for iter_19_2, iter_19_3 in ipairs(arg_19_0.catchupItems):
		iter_19_3.catchupTag = True

		table.insert(var_19_0, iter_19_3)

	for iter_19_4, iter_19_5 in ipairs(arg_19_0.catchupActItems):
		iter_19_5.catchupActTag = True

		table.insert(var_19_0, iter_19_5)

	return var_19_0

def CanDropItem(arg_20_0):
	var_20_0 = getProxy(ActivityProxy)
	var_20_1 = var_20_0.getActivityById(ActivityConst.UTAWARERU_ACTIVITY_PT_ID)

	if var_20_1 and not var_20_1.isEnd():
		var_20_2 = var_20_1.getConfig("config_client").pt_id
		var_20_3 = underscore.detect(var_20_0.getActivitiesByType(ActivityConst.ACTIVITY_TYPE_PT_RANK), lambda arg_21_0: arg_21_0.getConfig("config_id") == var_20_2).getData1()

		if var_20_3 >= 1500:
			var_20_4 = var_20_3 - 1500
			var_20_5 = underscore.detect(arg_20_0, lambda arg_22_0: arg_22_0.type == DROP_TYPE_RESOURCE and arg_22_0.id == var_20_2)

			arg_20_0 = underscore.filter(arg_20_0, lambda arg_23_0: arg_23_0.type != DROP_TYPE_RESOURCE or arg_23_0.id != var_20_2)

			if var_20_5 and var_20_4 < var_20_5.count:
				var_20_5.count = var_20_5.count - var_20_4

				table.insert(arg_20_0, var_20_5)

	arg_20_0 = BonusItemMarker(arg_20_0)

	return table.getCount(arg_20_0) > 0

var_0_5 = None

def var_0_6(arg_24_0):
	var_0_5 = var_0_5 or table({
		DROP_TYPE_SHIP: True,
		DROP_TYPE_OPERATION: True,
		DROP_TYPE_LOVE_LETTER: True
	})

	if var_0_5[arg_24_0.type]:
		return True
	elif arg_24_0.type == DROP_TYPE_ITEM and bool(arg_24_0.extra):
		return True
	else:
		return False

def MergeSameDrops(arg_25_0):
	var_25_0 = table()
	var_25_1 = table()

	for iter_25_0, iter_25_1 in ipairs(arg_25_0):
		var_25_2 = f"{iter_25_1.type}_{iter_25_1.id}"

		if not var_25_1[var_25_2]:
			if var_0_6(iter_25_1):
				pass#-- block empty
			else:
				var_25_1[var_25_2] = iter_25_1

			table.insert(var_25_0, iter_25_1)
		else:
			var_25_1[var_25_2].count = var_25_1[var_25_2].count + iter_25_1.count

	return var_25_0
