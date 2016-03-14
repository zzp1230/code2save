#!/bin/bash

if (( $# == 1 ))
then
	inputfile=$1
else
	echo "Usage: sh viterbi.sh filename"
	exit 1
fi

dir=$(pwd)
cd $dir
file_han="han.key"
file_pin="pin.key"
words2seq_pl="words2seq.pl"
pianyi_hmm="py.hmm"
ints2words_pl="ints2words.pl"
testvit="testvit"

if [ ! -f $file_han ] || [ ! -f $file_pin ] || [ ! -f $words2seq_pl ] || [ ! -f $pianyi_hmm ] || [ ! -f $ints2words_pl ] || [ ! -f $testvit ]
then
	echo "File $file_han $file_pin  $words2seq_pl $pianyi_hmm $ints2words_pl $testvit does not exist."
	exit 1
fi

perl $words2seq_pl $file_han < $inputfile > $inputfile.seq

./$testvit $pianyi_hmm $inputfile.seq > $inputfile.seq.temp

awk '{if(NR == 5 || NR == 6)print $0}' $inputfile.seq.temp > $inputfile.seq.out
rm $inputfile.seq.temp

outfile=$inputfile.seq.out
perl $ints2words_pl $file_pin < $outfile > $inputfile.pin

cat $inputfile
cat $inputfile.seq
cat $inputfile.seq.out
cat $inputfile.pin
