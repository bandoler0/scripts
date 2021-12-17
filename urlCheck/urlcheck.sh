#!/bin/bash

for site in $(cat sitelist.txt)
do
status=$(curl -s -H "User-Agent: Teste" -o /dev/null -w "%{http_code}" $site)
echo "$status : $site"
done
