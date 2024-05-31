if pg and pg.ConnectionMgr:
	pg.ConnectionMgr.GetInstance().Disconnect()

if pg and pg.SimpleConnectionMgr:
	pg.SimpleConnectionMgr.GetInstance().Disconnect()
