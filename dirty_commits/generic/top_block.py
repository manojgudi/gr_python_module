#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Fri Sep 20 15:34:14 2013
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import scimod
import wx

class top_block(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Top Block")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 32000

		##################################################
		# Blocks
		##################################################
		self.scimod_generic_0 = scimod.generic()
		self.scimod_generic_0.set_parameters("fft", 6)
		    
		self.gr_vector_source_x_0 = gr.vector_source_f((1,2,3,4,1.578, 12), True, 1)
		self.gr_vector_sink_x_0 = gr.vector_sink_f(1)

		##################################################
		# Connections
		##################################################
		self.connect((self.scimod_generic_0, 0), (self.gr_vector_sink_x_0, 0))
		self.connect((self.gr_vector_source_x_0, 0), (self.scimod_generic_0, 0))


	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

