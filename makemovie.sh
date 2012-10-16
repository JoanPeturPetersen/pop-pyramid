#!/bin/sh

#http://www-i6.informatik.rwth-aachen.de/~dreuw/videotools.html

#mencoder -ovc lavc -oac copy -mf fps=25 'mf://*.png' -of avi -lavcopts vcodec=mpeg2video:keyint=1:mbd=1:vqmin=2:vqmax=10:autoaspect -vf harddup -ofps 25 -noskip -o outputfile.avi
mencoder -ovc lavc -oac copy -mf w=640:h=480:fps=25 'mf://movie*.png' -of avi -lavcopts vcodec=mpeg2video:keyint=1:mbd=1:vqmin=2:vqmax=10:autoaspect -vf harddup,scale=640:480 -ofps 25 -noskip -o outputfile.avi
