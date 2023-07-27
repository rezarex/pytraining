#!/bin/bash


case ${1,,} in
	marvin | administrator)
		echo "Hello baaasman"
		;;
	help)
		echo "GIve me your name"
		;;
	*)
		echo "You shall not pass!"
esac
