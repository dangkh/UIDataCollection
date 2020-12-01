import pika

class Pikachu:
    hostname = "192.168.1.190"
    port = 5672
    username = 'guest'
    password = 'guest'
    
    def __init__(self, hostname="192.168.1.190", port=5672, username="full_access", password="sc3r3t"):
        self.hostname   = hostname
        self.port       = port
        self.username   = username
        self.password   = password
        
    def send(self, queue, message):
        credentials = pika.PlainCredentials('hmi', 'cntt307e3')
        parameters = pika.ConnectionParameters(self.hostname, self.port, '/', credentials)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue)
        channel.basic_publish(exchange='', routing_key='hello', body=message)
        connection.close()

    def consume(self, queue, on_message_callback = exampleCallback, auto_ack=True):
        print("AAAAAAAAAAAAAAAA")
        credentials = pika.PlainCredentials('hmi', 'cntt307e3')
        parameters = pika.ConnectionParameters(self.hostname, self.port, '/', credentials)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue)
        channel.basic_consume(queue, on_message_callback, auto_ack)
        channel.start_consuming()
        
    def exampleCallback(ch, method, properties, body):
        print(" [x] Received %r" % body)
