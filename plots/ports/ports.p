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
set title "Connections" @fg
#set ylabel "" @fg
set xtics rotate by 45 right
#set style fill solid 1.00 
set autoscale
set border @fg_lc
set xdata time
set timefmt '%H:%M'
set format x '%H:%M'
set key top left @fg

set terminal png @bg size 720,600
set output "./ports.png"
plot "./ports.log" using 1:2 @line_fg w l title "8080",\
"./ports.log" using 1:3 w l title "80",\
