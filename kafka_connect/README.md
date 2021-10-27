Download local confluent

https://docs.confluent.io/platform/current/quickstart/cos-quickstart.html

Install Kafka Connect

confluent-hub install confluentinc/kafka-connect-mqtt:latest

Start Kafka Connect and dependencies (Kafka, Zookeeper, Schema Registry):

confluent local services start

Start MQTT Subscriber & Kafka Consumer

go run ./main.go

Create and deploy MQTT Connector Instance

```
curl -s -X POST -H 'Content-Type: application/json' http://localhost:8083/connectors -d '{
    "name" : "mqtt-source",
"config" : {
    "connector.class" : "io.confluent.connect.mqtt.MqttSourceConnector",
    "tasks.max" : "1",
    "mqtt.server.uri" : "tcp://127.0.0.1:1883",
    "mqtt.topics" : "temperature",
    "kafka.topic" : "mqtt.temperature",
    "confluent.topic.bootstrap.servers": "localhost:9092",
    "confluent.topic.replication.factor": "1",
    "confluent.license":""
    }
}'
```

Check connector is running:
curl -s "http://localhost:8083/connectors"
curl -s "http://localhost:8083/connectors/mqtt-source/status"

Create kafka topic:
kafka-topics --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic mqtt.temperature


Start sensor generator script

chmod 755 sensor-generator.sh
./sensor-generator.sh
