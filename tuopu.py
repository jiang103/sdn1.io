from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
import time

class MyTopo(Topo):
    def build(self):
        # 添加交换机
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        
        # 添加主机
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        
        # 连接交换机和主机
        self.addLink(switch1, host1)
        self.addLink(switch2, host2)
        
# 创建网络
net = Mininet(topo=MyTopo())

# 设置控制器模式为"approve"
net.config['controller'] = 'approve'

# 启动网络并等待5秒以确保所有节点都已启动
net.start()
time.sleep(5)

# 执行CLI命令以查看网络状态和运行ping测试
CLI(net)
