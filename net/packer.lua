﻿pg = pg or {}

local var_0_0 = pg

var_0_0.Packer = singletonClass("Packer")

local var_0_1 = var_0_0.Packer

var_0_1.ps = nil

function var_0_1.Ctor(arg_1_0)
	arg_1_0._protocols = {}
	var_0_1.ps = PackStream.New()
	arg_1_0.defaultBuffSize = 8192
end

function var_0_1.Pack(arg_2_0, arg_2_1, arg_2_2, arg_2_3)
	local var_2_0 = arg_2_3:SerializeToString()
	local var_2_1 = ""
	local var_2_2 = arg_2_0.ps

	if #var_2_0 > arg_2_0.defaultBuffSize - 7 then
		var_2_2 = PackStream.New(#var_2_0 + 7)
	end

	if var_2_2.Length ~= 0 then
		print("### pack string error !!!!!!!!!!!")
	end

	if #var_2_0 == 0 then
		var_2_2:WriteUint16(6)
	else
		var_2_2:WriteUint16(5 + #var_2_0)
	end

	var_2_2:WriteUint8(0)
	var_2_2:WriteUint16(arg_2_2)
	var_2_2:WriteUint16(arg_2_1)
	var_2_2:WriteBuffer(var_2_0)

	return var_2_2:ToArray()
end

function var_0_1.Unpack(arg_3_0, arg_3_1, arg_3_2)
	local var_3_0 = var_0_1.GetInstance():GetProtocolWithName("sc_" .. arg_3_1)

	if var_3_0 ~= nil then
		local var_3_1 = var_3_0._object[var_3_0._name]()

		var_3_1:ParseFromString(arg_3_2)

		return var_3_1
	end
end

function var_0_1.GetProtocolWithName(arg_4_0, arg_4_1)
	if arg_4_0._protocols[arg_4_1] ~= nil then
		return arg_4_0._protocols[arg_4_1]
	end

	local var_4_0 = string.sub(arg_4_1, 4, #arg_4_1)
	local var_4_1 = "Net/Protocol/"
	local var_4_2 = "p" .. string.sub(var_4_0, 1, 2) .. "_pb"
	local var_4_3

	pcall(function()
		var_4_3 = require(var_4_1 .. var_4_2)
	end)

	if var_4_3 then
		local var_4_4 = var_0_0.Protocol.New(var_4_0, arg_4_1, package.loaded[var_4_2])

		arg_4_0._protocols[arg_4_1] = var_4_4

		return var_4_4
	else
		return nil
	end
end
