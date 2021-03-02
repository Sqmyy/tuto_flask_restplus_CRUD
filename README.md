# ANSIBLE

With Ansible we use a __playbook__ to manage distant nodes

The inventory describes the targeted nodes by Ansible, We can group them by domain or subdomain.

The playbook is the list of tasks to execute on distant nodes

Tasks are specific to ONE playbook, and the host executing the task have to be stated inside.
Generally tasks are used in short playbooks. The reason is it specifies a lot of details which will complicate the playbook and make it very long.

Roles let you group tasks and can be reused in more than 1 playbook.
They possess a file structure with at least 1 main in the following files:
- tasks/
- handlers/ 
- library/
- files/
- templates/
- vars/
- defaults/

Handlers are basically tasks but they are executed after tasks and roles. They are useful because they are executed only once no matter how many times they are called within other tasks

The order of execution in a playbook is as following:

1) Tasks executed in first
2) Roles in second
3) Lastly handlers are executed



# OPENSTACK 

OpenStack allows the creation of private and public clouds and is composed of several layers such as: 

- __NOVA :__ To create and manage virtual servers, this service depends on Glance, Neutron, Keystone and Placements services and is composed of:
    - An SQL database
    - The API communicates with other components via HTTP requests
    - Scheduler decides which host owns which instance
    - Compute communicates with the virtual machines
    - Conductor manages requests needing coordination
	- Placements keep a trace of provider's information such as what resource the provider needs, ... 
      

Also allows creating and/or managing security groups, useful for instance with NEUTRON to establish connection rules to a virtual network

- __GLANCE :__ https://docs.openstack.org/glance/latest/ \
  It is the Image Service. It allows discovering, register and upload of data assets, disk and server images.
  
- __KEYSTONE :__ https://docs.openstack.org/keystone/latest/ \
  Provides API client authentication, and their access rules, service discovery

- __NEUTRON :__ https://docs.openstack.org/neutron/latest/ \
  Neutron handles creation and management of a virtual networking infrastructure for a OpenStack Compute service(NOVA). Provides Network connectivity-as-a-service, allows network administration and providing IP address to other OpenStack services. Also allows Load balancing-as-a-Service and Firewall-as-a-Service. Needs several layers to work:

    - __Controller(MANDATORY)__
  Executes the Identity service, the Image service, Network agents. Incudes support services such as SQL database. Requires 2 network interfaces.
    - __Compute (MANDATORY)__
  Executes virtual machines, and a networking service agent connecting instances to a virtual network add providing a firewall. Requires 2 network interfaces
    - __Block Storage(OPTIONAL)__
  Storage space containing "hard drives", you can deploy more than 1. Requires 1 network interface
    - __Object Storage(OPTIONAL)__
  We split data in self-standing blocs and can be used by many systems. Requires 1 network interface

  Neutron is a standalone service that deploys processes across one or more nodes. Its main process is neutron-server. To communicate with other components neutron services use either SDN or Database connection. In short Neutron components are:

  - neutron-server: Services the Networking API and its extensions on the network node, enforces network model and IP addressing of each port. Requires an indirect access to a persistent database
  - plugin agent: Runs on each compute node, to manage virtual switch(vswitch) configuration. The agent running depends on the plugin you use
  - DHCP agent: Provides DHCP services to tenant network, requires message queue access
  - L3 agent: Provides L3/NAT forwarding for external access of virtual machines on tenant network, requires message queue access
  - SDN service:  Provides additional networking services to tenant network that can interact with neutron-server or plugin agents through communication channel like REST APIs

  Neutron also called OpenStack Networking service, provides an API that allows to set-up and define network connectivity.

  Neutron provides layers 2(Ethernet and switching) and 3(IP and routing) connectivity to instances and few routing services :

  - VPNaaS: Virtual-Private-Network-as-a-Service, introduces VPN feature set
  - FWaaS: Firewall-as-a-Service, allows adopters to test their networking implementations

  - LBaaS: Load-Balancer-as-a-Service, to provision and configure load balancers

  It includes support for Layers 2(networking and IP Address management) as well as an extension for a Layer 3 routing construct that enables routing between Layer 2 networks and gateways to external networks.

  OpenStack Networking also includes plug-ins, that enable interoperability with various commercials and open source network technologies(routers, switches, vswitches and SDN controllers)

  The OpenStack Networking plug-in and agents plugs and unplugs ports, create networks and subnets and provides IP addressing. Only one plug-in can be used at a time and it differs depending on the technologies used in the particular cloud.

  Lastly there is the Messaging queue. It accepts and routes RPC requests between agents to complete API operations

### Network infrastructure creation : 
- Create 2 networks and 2 subnetworks that you link to virtual machines and associates ports. DHCP are automatically created
- Using NOVA configure security rules for the groups that will use the infrastructure
- In order to allow our virtual machines to communicate with another network we need to create an external virtual router
- To set that router available on the internet set it as a Gateway
