import pika
import time

class Pikachu:
    hostname = "192.168.1.190"
    port = 5672
    username = 'guest'
    password = 'guest'
    exchange = ''
    exchange_type = ''
    routing_key = 'hello'
    connectionSend = pika.BlockingConnection()
    connectionReceieve = pika.BlockingConnection()
    
    def __init__(self, hostname="192.168.1.190", port=5672, username="hmi", password="cntt307e3"):
        self.hostname   = hostname
        self.port       = port
        self.username   = username
        self.password   = password
        
    def send(self, message, queue='hello'):
        credentials = pika.PlainCredentials('hmi', 'cntt307e3')
        parameters = pika.ConnectionParameters(self.hostname, self.port, '/', credentials)
        self.connectionSend = pika.BlockingConnection(parameters)
        channel = self.connectionSend.channel()
        channel.queue_declare(queue)
        channel.exchange_declare(exchange=self.exchange, exchange_type=self.exchange_type)
        channel.queue_bind(exchange=self.exchange, queue=queue, routing_key=self.routing_key)
        channel.basic_publish(exchange=self.exchange, routing_key=self.routing_key, body=message)
        self.connectionSend.close()
        # print(" [x] Send %r" % message)

    def consume(self, queue, callback, autoAck=True):
        credentials = pika.PlainCredentials('hmi', 'cntt307e3')
        parameters = pika.ConnectionParameters(self.hostname, self.port, '/', credentials)
        self.connectionReceieve = pika.BlockingConnection(parameters)
        channel = self.connectionReceieve.channel()
        channel.queue_declare(queue)
        channel.basic_consume(queue, on_message_callback=callback, auto_ack=autoAck)
        channel.start_consuming()
    
    def StopConsume(self):
        self.connectionReceieve.close()
    
    def exampleCallback(ch, method, properties, body):
        print(" [x] Received %r" % body)
