#!/usr/bin/python
import gras
import numpy
import serial
import pika
import cPickle as pickle

class Params:
    def __init__(self):
        pass

class tasker(gras.Block):


    def __init__(self):
            gras.Block.__init__(self,
                    name="tasker",
                    in_sig=[numpy.float32],
                    out_sig=[numpy.float32],
                    n=1)
        # window
        self.n = n
        self.params = Params()

    def create_connection(self, hostname='localhost',  queue_name):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(hostname))
        self.channel = connection.channel()
        self.channel.queue_declare( queue=queue_name )

    def work(self, input_items, output_items, queue_name):

        in0 = input_items[0][:self.n]
        in1 = input_items[1]self:n]

        out = output_items[0][:self.n]

        # Get this from xml
        self.duration = 10
        self.delta_t = .1
        # Input is size of output_items to be returned
	    
        ## Untested Code
        # Send params to Kalman Filter worker 
        # Currently I am sending duration and delta_t
        self.params.duration = self.duration
        self.params.delta_t = self.delta_t

        self.dumps1 = pickle.dumps(self.params)

        self.channel.basic_publish( exchange='',
                                    routing_key=queue_name,
                                    body=self.dumps1)


        print "OUT", out[:self.n]

        self.produce(0,len(out)) # Produce from port 0 output_items
        self.consume(0,1) # Consume from port 0 input_items

