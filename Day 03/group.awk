#!/bin/awk -f

BEGIN{i=1}

{
  if(acc==3) {
    acc=0
    i++
  }
  arr[i] = ($1 OFS arr[i])
  acc++
}

END{
  for(i in arr) print arr[i]

}
