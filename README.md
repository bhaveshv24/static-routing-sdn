# Static Routing using SDN Controller
**Student:** Bhavesh Velluru | **SRN:** PES1UG24CS115  
**Course:** Computer Networks - UE24CS252B

## Problem Statement
Implement static routing paths using controller-installed flow rules.

## Topology
- 3 Hosts: h1 (10.0.0.1), h2 (10.0.0.2), h3 (10.0.0.3)
- 2 Switches: s1, s2
- Ryu SDN Controller (OpenFlow 1.3)

## Setup & Execution

### 1. Install dependencies
```bash
sudo apt install mininet openvswitch-switch iperf -y
python3.8 -m venv ~/ryu-env
source ~/ryu-env/bin/activate
pip install wheel ryu eventlet==0.30.2
```

### 2. Start Ryu Controller (Terminal 1)
```bash
source ~/ryu-env/bin/activate
ryu-manager static_router.py
```

### 3. Start Mininet (Terminal 2)
```bash
sudo python3 topology.py
```

## Test Scenarios

### Scenario 1 - Normal Routing
```bash
mininet> pingall
# Expected: 0% dropped (6/6 received)
```

### Scenario 2 - Regression Test
```bash
# Delete flow rules
mininet> sh ovs-ofctl del-flows s1
mininet> sh ovs-ofctl del-flows s2
mininet> pingall
# Expected: 100% dropped

# Restart and verify rules restored
# Expected: 0% dropped (6/6 received)
```

## Expected Output
- pingall: 0% packet loss
- iperf h1->h2: ~100 Gbits/sec
- Flow tables show static rules per switch

## Outputs 

[PES1UG24CS115_SDN_MININET.pdf](https://github.com/user-attachments/files/26865276/PES1UG24CS115_SDN_MININET.pdf)


## References
- [Ryu SDN Framework](https://ryu-sdn.org/)
- [Mininet](https://mininet.org/)
- [OpenFlow Spec](https://opennetworking.org/sdn-resources/openflow/)
