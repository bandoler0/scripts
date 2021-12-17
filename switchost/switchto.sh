#!/bin/bash

resultado=$(ls /etc | egrep "hosts.dev|hosts.prod")

if [ $resultado = "hosts.dev" ]; then
	sudo mv /etc/hosts /etc/hosts.prod
	sudo mv /etc/hosts.dev /etc/hosts
	echo "Você está em ambiente DESENVOLVEDOR"
else
	sudo mv /etc/hosts /etc/hosts.dev
	sudo mv /etc/hosts.prod /etc/hosts
	echo "Você está em ambiente PRODUÇÃO"
fi
