#!/bin/bash
while getopts m: option
do
 case "${option}"
 in
 m) MODE=${OPTARG};;
 esac
done

export FLASK_APP=start.py

if [ $MODE == "dev" ]; then
    export MODE="dev"
    export FLASK_DEBUG=1
else
    export FLASK_DEBUG=0
    export MODE="prod"
fi

flask run