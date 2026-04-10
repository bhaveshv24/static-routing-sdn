from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink

def create_topology():
    net = Mininet(controller=RemoteController, link=TCLink)

    # Add controller
    c0 = net.addController('c0', ip='127.0.0.1', port=6633)

    # Add switches
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    # Add hosts
    h1 = net.addHost('h1', ip='10.0.0.1/24')
    h2 = net.addHost('h2', ip='10.0.0.2/24')
    h3 = net.addHost('h3', ip='10.0.0.3/24')

    # Add links
    net.addLink(h1, s1)
    net.addLink(h2, s2)
    net.addLink(h3, s2)
    net.addLink(s1, s2)

    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_topology()
