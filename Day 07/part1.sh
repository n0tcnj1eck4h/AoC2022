#!/bin/bash

result=0;

dirsize() {
  local sum=0;
  local lines=`ls`;
  while IFS= read -r line; do
    if [ -d $line ]; then
      cd $line
      size=`dirsize`
      sum=$(($sum+$size));
      cd ..
      if [ 100000 -gt $size ]; then
          result=$(($result+$size))
      fi
    else
      sum=$(($sum+`cat $line`));
    fi
  done <<< "$lines";
  echo $sum;
}

cd "root"
dirsize 
cd .. 
echo $result
