#!/bin/bash
./find_common.awk input.txt | ./get_values.awk | ./sum.awk
./group.awk input.txt | ./find_badge.awk | ./get_values.awk | ./sum.awk 
