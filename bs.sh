#!/bin/bash

# collect both times in seconds-since-the-epoch
filename=~/.bs.update
docker_image=kostyay/circlestatus:latest

if [ ! -f $filename ] || [[ $(find "$filename" -mtime +1 -print) ]]; then
  echo "Checking for updates.."
  docker pull $docker_image
  touch $filename
fi

target_dir=`pwd`
if [ ! -z "$1" ]; then
	target_dir=$1
fi

echo docker run --env HOME=$HOME -v $HOME:$HOME -v `pwd`:`pwd` $docker_image $target_dir
docker run --env HOME=$HOME -v $HOME:$HOME -v `pwd`:`pwd` $docker_image $target_dir
