#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Sat Dec 14 11:39:53 2013
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import gr_controller
import gr_sbhs
import gras
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
		self.sbhs_controller_0 = gr_controller.sbhs_controller()
		self.sbhs_controller_0.set_parameters(2, 1, 2, 0.1, 25, 1)
		    
		self.grex_subtract_0 = gras.make('/grex/subtract_v_f32_f32', 1)
		self.grex_subtract_0.set_preload((1, ))
		self.gr_vector_source_x_0_0 = gr.vector_source_f((30, ), True, 1)
		self.gr_sbhs_0 = gr_sbhs.gr_sbhs()
		self.gr_sbhs_0.set_parameters(1)
		    
		self.const_source_x_0 = gr.sig_source_f(0, gr.GR_CONST_WAVE, 0, 0, 40)

		##################################################
		# Connections
		##################################################
		self.connect((self.sbhs_controller_0, 0), (self.gr_sbhs_0, 0))
		self.connect((self.gr_vector_source_x_0_0, 0), (self.gr_sbhs_0, 1))
		self.connect((self.grex_subtract_0, 0), (self.sbhs_controller_0, 0))
		self.connect((self.gr_sbhs_0, 0), (self.grex_subtract_0, 1))
		self.connect((self.const_source_x_0, 0), (self.grex_subtract_0, 0))


	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

