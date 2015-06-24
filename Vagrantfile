# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "Censio/dev-env"

  # Network Setup
  config.vm.network :private_network, ip: "192.168.33.27"
  config.vm.hostname = "dev-vm"

  # SSH Configure
  config.ssh.forward_agent = true
  config.ssh.username = "ubuntu"

  # NFS configuration
  config.vm.synced_folder "sample-project", "/home/ubuntu/sample-project", type: "nfs"
  config.vm.synced_folder ".", "/vagrant", disabled: true

  #Modify VM (Memory)
  config.vm.provider :virtualbox do |vb|
    # Use VBoxManage to customize the VM. For example to change memory:
    vb.customize ["modifyvm", :id, "--natnet1", "192.168.42/24"]
    vb.memory = 3048
    vb.cpus = 2
  end

end
