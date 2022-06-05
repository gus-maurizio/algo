#!/bin/bash
## Name: SSM Agent Installer Script
## Description: Installs SSM Agent on EMR cluster EC2 instances and update hosts file
##
sudo yum install -y amazon-ssm-agent
sudo service amazon-ssm-agent status >>/tmp/ssm-status.log
## Update hosts file
echo "########### localhost mapping check ###########" >> /tmp/localhost.log
v_ipaddr=$(hostname --ip-address)
echo "${v_ipaddr} localhost" >/tmp/etc.hosts
sudo /bin/bash -c 'cat /tmp/etc.hosts >>/etc/hosts'
sudo cat /etc/hosts >> /tmp/localhost.log
echo "########### Exit script ###########" >> /tmp/localhost.log
