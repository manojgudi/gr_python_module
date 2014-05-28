#!/usr/bin/python
import gras
import numpy
import serial
import pika
import cPickle as pickle
import uuid

class tasker(gras.Block):


    def __init__(self):
        gras.Block.__init__(self,
                    name="tasker",
                    in_sig=[numpy.float32],
                    out_sig=[numpy.float32],
                    n=1)

    class FibonacciRpcClient(object):
        def __init__(self):
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                    host='localhost'))

            self.channel = self.connection.channel()

            result = self.channel.queue_declare(exclusive=True)
            self.callback_queue = result.method.queue

            self.channel.basic_consume(self.on_response, no_ack=True,
                                    queue=self.callback_queue)

        def on_response(self, ch, method, props, body):
            if self.corr_id == props.correlation_id:
                self.response = body

        def call(self, n):
            self.response = None
            self.corr_id = str(uuid.uuid4())
            self.channel.basic_publish(exchange='',
                                    routing_key='rpc_queue',
                                    properties=pika.BasicProperties(
                                            reply_to = self.callback_queue,
                                            correlation_id = self.corr_id,
                                            ),
                                    body=n)
            while self.response is None:
                self.connection.process_data_events()
            return int(self.response)

        self.fibonnaci_rpc = FibonacciRpcClient()
        # window
        self.n = n

    def work(self, input_items, output_items, queue_name):

        in0 = input_items[0][:self.n]
        in1 = input_items[1]self:n]

        out = output_items[0][:self.n]

        # Input is size of output_items to be returned

        # Send this in0 to worker
        ## TODO CHECK THIS
        self.dumps0 = pickle.dumps(in0[0])
        self.dumps1 = pickle.dumps(in1)

        # self.dumps0 has to be an integer
        out[0] = self.finbonnaci_rpc.call(30)


        print "OUT", out[:self.n]

        self.produce(0,len(out)) # Produce from port 0 output_items
        self.consume(0,1) # Consume from port 0 input_items

