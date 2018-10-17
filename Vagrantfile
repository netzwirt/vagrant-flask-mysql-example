# -*- mode: ruby -*-
# vi: set ft=ruby :
# this setup requires vagrant hostnames plugin
# @see https://github.com/smdahlen/vagrant-hostmanager
# vagrant plugin install vagrant-hostmanager


Vagrant.configure("2") do |config|

	config.vm.box = "ubuntu/bionic64"
	config.vm.network "private_network", ip: "12.20.54.21"
	config.vm.provider :virtualbox do |vb|
	    vb.customize ["modifyvm", :id, "--name", "flask", "--memory", "1024"]
	    vb.customize ["modifyvm", :id, "--uartmode1", "disconnected"]
	end
	
	config.vm.provision "shell",
 		inline: "test ! -f /home/flask/app/venv/ || (sudo apt update && sudo apt install python3-pip -y && mkdir -p /home/flask/base)"

	config.vm.synced_folder "./base", "/home/flask/base", type: "nfs"

	config.vm.provision "ansible" do |ansible|
    	ansible.playbook = "ansible/venv.yml"
    	ansible.extra_vars = { ansible_python_interpreter:"/usr/bin/python3" }
	end

	config.vm.provision "ansible" do |ansible|
    	ansible.playbook = "ansible/mysql-server.yml"
    	ansible.extra_vars = { ansible_python_interpreter:"/usr/bin/python3" }
	end

	config.vm.provision "ansible" do |ansible|
    	ansible.playbook = "ansible/flask.yml"
    	ansible.extra_vars = { ansible_python_interpreter:"/usr/bin/python3" }
	end
		
end


