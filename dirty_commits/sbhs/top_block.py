#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Fri Dec 13 22:33:20 2013
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import gr_sbhs
import wx

class top_block(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Top Block")

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 32000

		##################################################
		# Blocks
		##################################################
		self.gr_vector_source_x_0_0 = gr.vector_source_f((40,50,60), False, 1)
		self.gr_vector_source_x_0 = gr.vector_source_f((4,5,6), False, 1)
		self.gr_vector_sink_x_0 = gr.vector_sink_f(1)
		self.gr_sbhs_0 = gr_sbhs.gr_sbhs()
		self.gr_sbhs_0.set_parameters(1)
		    
		self.gr_file_sink_0 = gr.file_sink(gr.sizeof_float*1, "ne2.txt")
		self.gr_file_sink_0.set_unbuffered(True)

		##################################################
		# Connections
		##################################################
		self.connect((self.gr_vector_source_x_0, 0), (self.gr_sbhs_0, 0))
		self.connect((self.gr_vector_source_x_0_0, 0), (self.gr_sbhs_0, 1))
		self.connect((self.gr_sbhs_0, 0), (self.gr_vector_sink_x_0, 0))
		self.connect((self.gr_sbhs_0, 0), (self.gr_file_sink_0, 0))


	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

