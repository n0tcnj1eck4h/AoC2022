#!/bin/awk -f

BEGIN{for(n=0;n<256;n++)ord[sprintf("%c",n)]=n}

{
  val=ord[$1]
  if(val <= ord["Z"])
    val = val - ord["A"] + 27
  else
    val = val - ord["a"] + 1

  print val
}
