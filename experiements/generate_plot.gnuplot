set terminal postscript enhanced color
set output '| ps2pdf - results-01.pdf'


set boxwidth 0.75 absolute
set style fill solid 1.00 border lt -1
set key outside right top vertical Left reverse noenhanced autotitles columnhead nobox
set key invert samplen 4 spacing 1 width 0 height 0 
set style histogram rowstacked title  offset character 0, 0, 0
set style data histograms

set title "Replication times for different data volumes \n from central iRODS server to osgGridFtpGroup sites" 
set yrange [ 0.00000 : 3000 ] noreverse nowriteback
set ylabel "Time (s)"
set xlabel "Data volume"

plot for [COL=2:10] 'results/results-01.dat' using COL:xticlabels(1) title columnheader
