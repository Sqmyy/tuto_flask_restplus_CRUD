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

Openstack allows the creation of private and public clouds and is composed of several layers such as: 

- __NOVA :__ To create and manage virtual servers, this service depends on Glance, Neutron, Keystone and Placements services and is composed of:
    - An SQL database
    - The API communicates with other components via HTTP requests
    - Scheduler decides which host owns which instance
    - Compute communicates with the virtual machines
    - Conductor manages requests needing coordination
	- Placements keep a trace of provider's information such as what ressource the provider needs, ... 
      
Also allows creating and/or managing security groups, useful for instance with NEUTRON to establish connection rules to a virtual network

- __GLANCE :__ https://docs.openstack.org/glance/latest/ \
  It is the Image Service. It allows discovering, register and upload of data assets, disk and server images.
  
- __KEYSTONE :__ https://docs.openstack.org/keystone/latest/ \
  Provides API client authentication, and their access rules, service discovery

- __NEUTRON :__ https://docs.openstack.org/neutron/latest/ \
  Provides Network connectivity-as-a-service, allows network administration and providing IP address to other Openstack services. Also allows Load balancing-as-a-Service and Firewall-as-a-Service. Needs several layers to work:

    - __Controller(MANDATORY)__
Executes the Identity service, the Image service, Network agents. Incudes support services such as SQL database. Requires 2 network interfaces.

    - __Compute (MANDATORY)__
Executes virtual machines, and a networking service agent connecting instances to a virtual network add providing a firewall. Requires 2 network interfaces

    - __Block Storage(OPTIONAL)__
Storage space containing "hard drives", you can deploy more than 1. Requires 1 network interface

    - __Object Storage(OPTIONAL)__
We split data in self-standing blocs and can be used by many systems. Requires 1 network interface

### Network infrastructure creation : 
- Create 2 networks and 2 subnetworks that you link to virtual machines and associates ports. DHCP are automatically created

- Using NOVA configure security rules for the groups that will use the infrastructure

- In order to allow our virtual machines to communicate with another network we need to create an external virtual router

- To set that router available on the internet set it as a Gateway
