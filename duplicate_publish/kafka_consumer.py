# kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 partitions 1 --topic temperature 3

# kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic temperature3 --from-beginning