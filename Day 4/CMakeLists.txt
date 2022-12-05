cmake_minimum_required(VERSION 3.9)

if(NOT DEFINED input_file)
  set(input_file "input.txt")
endif()

file(STRINGS ${input_file} lines)

set(count 0)
foreach(line ${lines})
  string(REPLACE "-" "," pairs ${line})
  string(REPLACE "," ";" pairs ${pairs})
  list(POP_BACK pairs b a d c)
  message(STATUS "${a} - ${b} - ${c} - ${d}")
  if(a LESS_EQUAL d AND b LESS_EQUAL d AND a GREATER_EQUAL c AND b GREATER_EQUAL c)
    math(EXPR count "${count}+1")
  elseif(c LESS_EQUAL b AND d LESS_EQUAL b AND c GREATER_EQUAL a AND d GREATER_EQUAL a)
    math(EXPR count "${count}+1")
  endif()
endforeach()

message(STATUS ${count})





set(count 0)
foreach(line ${lines})
  string(REPLACE "-" "," pairs ${line})
  string(REPLACE "," ";" pairs ${pairs})
  list(POP_BACK pairs b a d c)
  if    (a LESS_EQUAL d AND a GREATER_EQUAL c)
    math(EXPR count "${count}+1")
  elseif(b LESS_EQUAL d AND b GREATER_EQUAL c)
    math(EXPR count "${count}+1")
  elseif(c LESS_EQUAL b AND c GREATER_EQUAL a)
    math(EXPR count "${count}+1")
  elseif(d LESS_EQUAL b AND d GREATER_EQUAL a)
    math(EXPR count "${count}+1")
  endif()
endforeach()

message(STATUS ${count})





#set(checked_sections "")
#set(count 0)
#foreach(line ${lines})
#  string(REPLACE "-" "," pairs ${line})
#  string(REPLACE "," ";" pairs ${pairs})
#  list(POP_BACK pairs b a d c)
#
#  if(a GREATER c)
#    set(max_of_min ${a})
#  else()
#    set(max_of_min ${c})
#  endif()
#
#  if(b LESS d)
#    set(min_of_max ${b})
#  else()
#    set(min_of_max ${d})
#  endif()
#
#  math(EXPR result "${min_of_max}-${max_of_min}")
#  if(result GREATER 0)
#    foreach(i RANGE ${max_of_min} ${min_of_max})
#      list(FIND checked_sections ${i} found)
#      if(found EQUAL -1)
#        list(APPEND checked_sections ${i})
#      endif()
#    endforeach() 
#  endif()
#endforeach()
#
#list(LENGTH checked_sections length)
#message(STATUS ${length})
