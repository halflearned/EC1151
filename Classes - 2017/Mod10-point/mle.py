#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 11:33:28 2017

@author: vitorhadad
"""
import numpy as np

from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput
from bokeh.plotting import figure

# Set up data
N = 200
x = np.linspace(0, 1, N)
f = lambda p: p**3 * (1-p)**2
y = f(x)
source = ColumnDataSource(data=dict(x=x, y=y))


# Set up plot
plot = figure(plot_height=400, plot_width=400, title="Likelihood of p",
              tools="crosshair,pan,reset,save,wheel_zoom",
              x_range=[0, 1], y_range=[-.1, .1])

plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

line = plot.segment(source = ColumnDataSource(data= dict(x0=[0.5], y0=[0], 
             x1=[0.5], y1=[f(0.5)])), 
             color="#F4A582", line_width=3)


# Set up widgets
text = TextInput(title="title", value='my sine wave')
p = Slider(title="p", value=0.5, start=0, end=1)


def update_data(attrname, old, new):

    # Get the current slider values
    new_p = p.value
    new_source = ColumnDataSource(data= dict(x0=[new_p], y0=[0], 
                                             x1=[new_p], y1=[f(new_p)]))

    # Generate the new curve
    x = np.linspace(0, 1, N)
    y = f(x)

    line.data_source = new_source

p.on_change('value', update_data)


# Set up layouts and add to document
inputs = widgetbox(text, p)

curdoc().add_root(row(inputs, plot, width=800))
curdoc().title = "Maximum likelihood"