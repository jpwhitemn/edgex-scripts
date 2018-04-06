#!/bin/bash
localPATH=`pwd`                                         # path of current directory
sep='---------------'                                   
for d in */; do
  echo $sep"Processing" $d$sep
  d=`echo $d | sed s#/##`                               # remove trailing forward slash
  remoteRepo="https://github.com/edgexfoundry/$d.git"    # location of remote repo
  git -C $localPATH/$d pull            # pull from remote into solution
  echo -e "\n"
done