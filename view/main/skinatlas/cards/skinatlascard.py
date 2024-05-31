local var_0_0 = class("SkinAtlasCard")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0._go = arg_1_1
	arg_1_0._tf = arg_1_1.transform
	arg_1_0.usingTr = findTF(arg_1_0._tf, "using")
	arg_1_0.unavailableTr = findTF(arg_1_0._tf, "unavailable")
	arg_1_0.icon = findTF(arg_1_0._tf, "mask/icon").GetComponent(typeof(Image))
	arg_1_0.name = findTF(arg_1_0._tf, "name/Text").GetComponent(typeof(Text))
	arg_1_0.tags = {
		findTF(arg_1_0._tf, "tags/icon")
	}

def var_0_0.Update(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0.index = arg_2_2
	arg_2_0.skin = arg_2_1

	LoadSpriteAtlasAsync("shipYardIcon/" .. arg_2_1.getConfig("painting"), "", function(arg_3_0)
		if arg_2_0.exited:
			return

		arg_2_0.icon.sprite = arg_3_0)

	local var_2_0 = arg_2_1.getConfig("ship_group")
	local var_2_1 = getProxy(BayProxy).findShipsByGroup(var_2_0)
	local var_2_2 = _.any(var_2_1, function(arg_4_0)
		return arg_4_0.skinId == arg_2_1.id)

	setActive(arg_2_0.usingTr, #var_2_1 > 0 and var_2_2)

	local var_2_3 = getProxy(CollectionProxy).shipGroups[var_2_0] == None

	setActive(arg_2_0.unavailableTr, #var_2_1 == 0 or var_2_3)

	local var_2_4 = arg_2_1.getConfig("name")

	arg_2_0.name.text = shortenString(var_2_4, 7)

	arg_2_0.FlushTags(arg_2_1.getConfig("tag"))

def var_0_0.FlushTags(arg_5_0, arg_5_1):
	local var_5_0 = -10
	local var_5_1 = arg_5_0.tags[1]

	for iter_5_0 = #arg_5_0.tags + 1, #arg_5_1:
		local var_5_2 = Object.Instantiate(var_5_1, var_5_1.parent)

		arg_5_0.tags[iter_5_0] = var_5_2

	for iter_5_1 = 1, #arg_5_1:
		local var_5_3 = arg_5_0.tags[iter_5_1]

		setActive(var_5_3, True)
		LoadSpriteAtlasAsync("SkinIcon", "type_" .. ShipSkin.Tag2Name(arg_5_1[iter_5_1]), function(arg_6_0)
			if arg_5_0.exited:
				return

			var_5_3.GetComponent(typeof(Image)).sprite = arg_6_0)

		local var_5_4 = var_5_1.localPosition.y - (iter_5_1 - 1) * (var_5_1.sizeDelta.x + var_5_0)

		var_5_3.localPosition = Vector3(var_5_3.localPosition.x, var_5_4, 0)

	for iter_5_2 = #arg_5_1 + 1, #arg_5_0.tags:
		setActive(arg_5_0.tags[iter_5_2], False)

def var_0_0.Dispose(arg_7_0):
	arg_7_0.exited = True

return var_0_0
