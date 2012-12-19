set terminal pdf # transparent enhanced font "arial,10" fontscale 1.0 size 500, 350 
set output 'histograms.4.pdf'
set boxwidth 0.75 absolute
set style fill   solid 1.00 border lt -1
set key outside right top vertical Left reverse noenhanced autotitles columnhead nobox
set key invert samplen 4 spacing 1 width 0 height 0 
set style histogram rowstacked title  offset character 0, 0, 0
set datafile missing '-'
set style data histograms
set xtics border in scale 0,0 nomirror rotate by -45  offset character 0, 0, 0 autojustify
set xtics  norangelimit font ",8"
set xtics   ()
set title "US immigration from Europe by decade\nPlot as stacked histogram" 
set yrange [ 0.00000 : 7.00000e+06 ] noreverse nowriteback
i = 22
plot 'immigration.dat' using 2:xtic(1), for [i=3:22] '' using i

