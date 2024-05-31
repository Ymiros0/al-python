local var_0_0 = class("ChatBubblePublic")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.tf = tf(arg_1_1)
	arg_1_0.richText = findTF(arg_1_0.tf, "text").GetComponent("RichText")

	local var_1_0 = findTF(arg_1_0.tf, "channel")

	if not IsNil(var_1_0):
		arg_1_0.channel = var_1_0.GetComponent("Image")

def var_0_0.update(arg_2_0, arg_2_1):
	if arg_2_0.data == arg_2_1:
		return

	arg_2_0.data = arg_2_1
	arg_2_0.richText.supportRichText = True

	ChatProxy.InjectPublic(arg_2_0.richText, arg_2_1)
	arg_2_0.richText.AddListener(function(arg_3_0, arg_3_1)
		arg_2_0.clickItem(arg_3_0, arg_3_1))

	if arg_2_0.channel:
		arg_2_0.channel.sprite = GetSpriteFromAtlas("channel", ChatConst.GetChannelSprite(arg_2_1.type) .. "_1920")

		arg_2_0.channel.SetNativeSize()

def var_0_0.clickItem(arg_4_0, arg_4_1, arg_4_2):
	if arg_4_1 == "clickPlayer":
		print("click player . ")
	elif arg_4_1 == "clickShip":
		print("click ship . ")

def var_0_0.dispose(arg_5_0):
	arg_5_0.richText.RemoveAllListeners()

return var_0_0
