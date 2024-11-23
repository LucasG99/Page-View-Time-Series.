from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

# Generate and save the line plot
line_plot = draw_line_plot()
line_plot.savefig("line_plot.png")

# Generate and save the bar plot
bar_plot = draw_bar_plot()
bar_plot.savefig("bar_plot.png")

# Generate and save the box plot
box_plot = draw_box_plot()
box_plot.savefig("box_plot.png")