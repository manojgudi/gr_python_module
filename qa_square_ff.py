#!/usr/bin/env python
# 
# Copyright 2013 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

from gnuradio import gr, gr_unittest
#import mymod_swig as mymod
from square3_ff import square3_ff

class qa_square_ff (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
    	src_data = (-2, 4, 5, 2, 1)
	expected_result = (4, 16, 25, 4, 1)

	src = gr.vector_source_f(src_data)
	sqr = square3_ff()
	dst = gr.vector_sink_f()
	
	self.tb.connect(src, sqr)
	self.tb.connect(sqr,dst)
	
	self.tb.run()

	result_data = dst.data()
	print str(result_data), "Result data"
	print str(expected_result), "expected "
	#self.assertFloatTupleAlmostEqual(expected_result, result_data, 6)


if __name__ == '__main__':
    gr_unittest.main()
    #gr_unittest.run(qa_square_ff, "qa_square_ff.xml")
