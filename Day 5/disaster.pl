#!/usr/bin/perl

use warnings;
#use strict;

open(INPUT, "<input.txt") or die "Couldn't open input.txt\n";

my @stack = ();
my @instructions = ();
my $stack_count = 0;
my $stack_height = 0;

while(<INPUT>) {
  if(/^(\s*\[.\])+/) {
    $stack_height++;
    push @stack_raw, split(/\[(.)\]/, $_);
  }
  elsif(/^(\s\d\s\s?)+$/) {
    $stack_count = $1;
  }
  elsif(/^move (\d+) from (\d+) to (\d+)$/) {
    push @instructions, ($1, $2, $3);
  }
}

#print "@instructions";
print "@stack_raw";
#print "$stack_count";
close(INPUT);

# SCREW THIS 
