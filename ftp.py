import paramiko
import os,json
#读取当前路径
base_dir = os.getcwd()
#读取在远程主机执行的脚本
cmd_filepath = base_dir+r'/pu1.txt'
cmd_file = open(cmd_filepath,'r')
cmd = cmd_file.read()


class PcManage(object):
    def __init__(self,host,port,username,password,timeout):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.timeout = timeout

    def ssh(self,cmd):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=self.host,port=self.port,username=self.username,password=self.password,timeout=self.timeout)
        stdin, stdout, stderr = client.exec_command(cmd)
        cmd_info = stdout.read().decode('gbk')
        print(cmd_info)
        client.close()


    def get(self,c_path,s_path):
        transport = paramiko.Transport((self.host,self.port))
        transport.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.get(s_path, c_path)
        print('下载成功')
        transport.close()

    def put(self,c_path,s_path):
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(c_path, s_path)
        print('上传成功')
        transport.close()

p = PcManage('123.56.20.45',22,'root','562159@Wrx',20)
# p.ssh(cmd)
# p.get('/home/pu.txt','/Users/wrx/Desktop/test.txt')
p.put('/Users/wrx/Desktop/img_face/kcj.mp4','/home/mysite/jfdh2/media/kcj.mp4')