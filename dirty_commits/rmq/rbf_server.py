#!/usr/bin/env python
import pika
import cPickle as pickle
from rbf_def import train_rbf, calc_val

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))

channel = connection.channel()
channel.queue_declare(queue='rpc_queue')

### Training Rbf
x,y = range(1,10), range(11,20)
trained_rbf = train_rbf(x,y)

def on_request(ch, method, props, body):
    n = pickle.loads(body)

    print " [.] RBF prediction of (%s)"  % (n,)
    
    # trained_rbf is global value
    response = calc_val(trained_rbf, n)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                     props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

print " [x] Awaiting RPC requests"
channel.start_consuming()
