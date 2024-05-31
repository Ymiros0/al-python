if System.Reflection == nil then
	System.Reflection = {}
end

local function var_0_0(...)
	local var_1_0 = {
		...
	}
	local var_1_1 = 0

	for iter_1_0 = 1, #var_1_0 do
		var_1_1 = var_1_1 + var_1_0[iter_1_0]
	end

	return var_1_1
end

local var_0_1 = {
	Default = 0,
	SetField = 2048,
	Static = 8,
	FlattenHierarchy = 64,
	ExactBinding = 65536,
	InvokeMethod = 256,
	NonPublic = 32,
	PutRefDispProperty = 32768,
	SuppressChangeType = 131072,
	IgnoreReturn = 16777216,
	CreateInstance = 512,
	GetField = 1024,
	OptionalParamBinding = 262144,
	Public = 16,
	Instance = 4,
	SetProperty = 8192,
	DeclaredOnly = 2,
	GetProperty = 4096,
	PutDispProperty = 16384,
	IgnoreCase = 1
}

System.Reflection.BindingFlags = var_0_1
System.Reflection.BindingFlags.GetMask = var_0_0

return var_0_1
