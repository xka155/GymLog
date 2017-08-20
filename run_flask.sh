#!/bin/sh
while getopts d option
do
 case "${option}"
 in
 d) DEBUG=${OPTARG};;
 esac
done

export FLASK_APP=run.py

if $DEBUG
then
    export FLASK_DEBUG=1
fi

flask run