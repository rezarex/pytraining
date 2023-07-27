#!/bin/bash

if [ ${1,,} = marvin ]; then
	echo "welcome baassman"
elif [ ${1,,} = help ]; then
	echo "just enter username"
else
	echo "you aint the one dummy!"
fi
