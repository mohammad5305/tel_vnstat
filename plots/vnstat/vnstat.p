set macros
bg = 'background rgb "#1a1b26"'
fg = 'textcolor rgb "#a9b1d6"'
fg_lc = 'linecolor rgb "#a9b1d6"'
line_fg = 'linecolor rgb "#9ECE6A"'

set lmargin at screen 0.20
set rmargin at screen 0.85
set bmargin at screen 0.30
set tmargin at screen 0.85

#set tics font "Roboto:style=Medium,9"
set datafile separator " "
set title "Traffic" @fg
set ylabel "Total(MiB)" @fg
set xtics rotate by 45 right
#set style fill solid 1.00 
set autoscale
set border @fg_lc
set xdata time
set timefmt '%H:%M'
set format x '%H:%M'
set key bottom right @fg


set terminal png @bg size 720,600
set output "./vnstat.png"
plot "./vnstat.log" using 1:2 @line_fg w l title "eth0"
