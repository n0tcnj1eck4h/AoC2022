#!/bin/awk -f
{
  len=length($1)
  str1=substr($1, 1, len/2)
  str2=substr($1, len/2+1, len/2)
  for(i = 1; i<=len/2; i++) {
    symbol=substr(str1, i, 1)
    if(index(str2, symbol) != 0) {
      print symbol
      next
    }
  }
  print "No common symbols found on line", NR, str1, str2, $1
}
