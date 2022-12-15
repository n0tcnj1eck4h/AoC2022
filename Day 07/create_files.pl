#!/usr/bin/perl 

use Cwd "cwd";
my $root_dir = cwd . "/root/";

while(<STDIN>) {
  if(/^\$\scd\s(.+)/) {
    $dir = $1;
    $dir =~ s/^\//$root_dir/o;
    mkdir $dir;
    chdir $dir;
  }
  elsif(/^dir\s(.+)/) {
    mkdir $1;
  }
  elsif(/^(\d+)\s(.+)/) {
    open FILE, ">$2";
    print FILE $1;
    close FILE;
  }
}
