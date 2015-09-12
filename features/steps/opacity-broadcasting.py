from __future__ import division

from behave import *

import numpy
import toyplot.testing

@given(u'a set of per-series opacity values')
def step_impl(context):
    context.series_opacities = numpy.linspace(1, 0.1, context.series.shape[1])

@given(u'a set of per-datum opacity values')
def step_impl(context):
    numpy.random.seed(1234)
    context.datum_opacities = numpy.random.uniform(0, 1, size=context.series.shape)

@then(u'bars can be rendered with one explicit opacity')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", opacity=0.2)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "opacity-broadcast-bars-one-opacity")

@then(u'bars can be rendered with per-series opacities')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", opacity=numpy.linspace(0.2, 0.8, 4))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "opacity-broadcast-bars-per-series-opacities")

@then(u'bars can be rendered with per-datum opacities')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", opacity=context.datum_opacities)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "opacity-broadcast-bars-per-datum-opacities")

@then(u'fills can be rendered with one explicit opacity')
def step_impl(context):
    context.axes.fill(context.series, opacity=0.2)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "opacity-broadcast-fills-one-opacity")

@then(u'fills can be rendered with per-series opacities')
def step_impl(context):
    context.axes.fill(context.series, opacity=numpy.linspace(0.2, 0.8, 3))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "opacity-broadcast-fills-per-series-opacities")

@then(u'hlines can be rendered with one explicit opacity')
def step_impl(context):
    context.axes.hlines(context.series[:,0], opacity=0.1)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "opacity-broadcast-hlines-one-opacity")

@then(u'hlines can be rendered with per-datum opacities')
def step_impl(context):
    context.axes.hlines(context.series[:,0], opacity=context.datum_opacities[:,0])
    toyplot.testing.assert_canvas_equal(
        context.canvas, "opacity-broadcast-hlines-per-datum-opacities")

@then(u'plots can be rendered with one explicit opacity')
def step_impl(context):
    context.axes.plot(context.series, opacity=0.2)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "opacity-broadcast-plots-one-opacity")

@then(u'plots can be rendered with per-series opacities')
def step_impl(context):
    context.axes.plot(context.series, opacity=context.series_opacities)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "opacity-broadcast-plots-per-series-opacities")

@then(u'rects can be rendered with one explicit opacity')
def step_impl(context):
    context.axes.rects(context.series[:-1,0], context.series[1:,0], context.series[:-1,1], context.series[1:,1], opacity=0.2)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "opacity-broadcast-rects-one-opacity")

@then(u'rects can be rendered with per-datum opacities')
def step_impl(context):
    context.axes.rects(context.series[:-1,0], context.series[1:,0], context.series[:-1,1], context.series[1:,1], opacity=context.datum_opacities[:-1,0])
    toyplot.testing.assert_canvas_equal(
        context.canvas, "opacity-broadcast-rects-per-datum-opacities")

@then(u'scatterplots can be rendered with one explicit opacity')
def step_impl(context):
    context.axes.scatterplot(context.series, opacity=0.2)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "opacity-broadcast-scatterplots-one-opacity")

@then(u'scatterplots can be rendered with per-series opacities')
def step_impl(context):
    context.axes.scatterplot(context.series, opacity=context.series_opacities)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "opacity-broadcast-scatterplots-per-series-opacities")

@then(u'scatterplots can be rendered with per-datum opacities')
def step_impl(context):
    context.axes.scatterplot(context.series, opacity=context.datum_opacities)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "opacity-broadcast-scatterplots-per-datum-opacities")

@then(u'text can be rendered with one explicit opacity')
def step_impl(context):
    text = ["#"] * len(context.series)
    context.axes.text(context.x, context.series[:,0], text, opacity=0.2)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "opacity-broadcast-text-one-opacity")

@then(u'text can be rendered with per-datum opacities')
def step_impl(context):
    text = ["#"] * len(context.series)
    context.axes.text(context.x, context.series[:,0], text, opacity=context.datum_opacities[:,0])
    toyplot.testing.assert_canvas_equal(
        context.canvas, "opacity-broadcast-text-per-datum-opacities")

@then(u'vlines can be rendered with one explicit opacity')
def step_impl(context):
    context.axes.vlines(context.series[:,0], opacity=0.1)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "opacity-broadcast-vlines-one-opacity")

@then(u'vlines can be rendered with per-datum opacities')
def step_impl(context):
    context.axes.vlines(context.series[:,0], opacity=context.datum_opacities[:,0])
    toyplot.testing.assert_canvas_equal(
        context.canvas, "opacity-broadcast-vlines-per-datum-opacities")

