#!/bin/awk -f

{
  delete seen
  for(j=1;j<=3;j++) {
    delete seen_local
    for(i=1;i<=length($j);i++) {
      s=substr($j,i,1)
      seen_local[s]++
    }
    for(i in seen_local) seen[i]++
  }

  for(i in seen)
    if(seen[i] == 3)
      print i
}
