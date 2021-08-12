#!/bin/bash
# usage : ./useradd.sh userlist
while read USERNAME
do
	useradd $USERNAME
	echo $USERNAME | passwd --stdin $USERNAME
done < $1
