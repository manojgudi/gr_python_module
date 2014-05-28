#!/usr/bin/python
import gras
import numpy
import serial

import pika
import cPickle as pickle

from rbf_def import train_rbf, calc_val

class worker(gras.Block):

    def __init__(self):
            gras.Block.__init__(self,
                    name="worker",
                    in_sig=[numpy.float32],
                    out_sig=[numpy.float32],
                    n=1)
        # window
        self.n = n

    def create_connection( self, hostname='localhost', queue_name):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(hostname))
        self.channel = connection.channel()
        self.channel.queue_declare(queue=queue_name)

    def work(self, input_items, output_items):

        ## Internal Functions
        def callback(self, ch, method, properties, body):
            self.body = pickle.loads(body)
            print "Got body"

            # Create Ack
            ch_basic_ack(delivery_tag = method.delivery_tag)
            
            self.trained_rbf = train_rbf(

        self.channel.basic_consume(callback, queue=queue_name, no_ack=False)

        print "Waiting for training_data"
        self.channel.start_consuming()

        self.n = input_items[0][0]
        out = output_items[0][:self.n]
        # Input is size of output_items to be returned


        self.produce(0,len(out)) # Produce from port 0 output_items
        self.consume(0,1) # Consume from port 0 input_items

