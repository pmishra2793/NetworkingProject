import paramiko
ssh_client =paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='hostname', username='mokgadi', password='mypassword')
ftp_client=ssh_client.open_sftp()
ftp_client.put('localfilepath', 'remotefilepath') 
ftp_client.close()
