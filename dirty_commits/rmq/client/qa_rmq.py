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
from gr_tasker import tasker
#import mymod_swig as mymod


class qa_tasker (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):

        # Source Data
        src_data = range(10)

        src0 = gr.vector_source_f(src_data)
        new_task = tasker()

        #Preload
        dst = gr.vector_sink_f()

        self.tb.connect(src0, (new_task,0)) # src0(vector_source) -> sqr_input_0
        #self.tb.connect((sqr,0), (sqr,1)) # sqr_output_0 -> sqr_input_1
        self.tb.connect(new_task,dst) # sqr_output_0 -> dst (vector_source)

        self.tb.run()

        result_data = dst.data()
        #print str(result_data), "Result data"
        #print str(expected_result), "expected "


   	#self.assertFloatTuplesAlmostEqual(expected_result, result_data, 6)


if __name__ == '__main__':
    gr_unittest.main()
   #gr_unittest.run(qa_dsim, "qa_dsim.xml")
