#!/bin/bash

ptn=$1
dir=$2
name=$3

if [ -z "$dir" ]; then
	dir='~'
fi

if [ -z "$name" ]; then
	name='*'
fi

find "$dir" -type f -name "$name" | xargs grep -nH "$pattern"
