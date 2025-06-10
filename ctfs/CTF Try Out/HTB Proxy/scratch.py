'''
	if request.URL == string([]byte{47, 115, 101, 114, 118, 101, 114, 45, 115, 116, 97, 116, 117, 115}) {
		var serverInfo string = GetServerInfo()
		var responseText string = okResponse(serverInfo)
		frontendConn.Write([]byte(responseText))
		frontendConn.Close()
		return
	}
'''

translateme=[47, 115, 101, 114, 118, 101, 114, 45, 115, 116, 97, 116, 117, 115]

print(''.join([chr(x) for x in translateme]))
# /server-status