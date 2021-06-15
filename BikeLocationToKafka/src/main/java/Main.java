import java.util.Properties;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.json.simple.JSONObject;
public class Main {
    public static void main(String[] args) {

        Properties properties = new Properties();
        properties.put("bootstrap.servers", "localhost:9092");
        properties.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        properties.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

        sendRecord(properties, "1", 3,4);
        sendRecord(properties, "1", 4,4);
        sendRecord(properties, "1", 3,4);
        sendRecord(properties, "1", 2,4);
        sendRecord(properties, "1", 2,3);
        sendRecord(properties, "1", 2,2);
        sendRecord(properties, "1", 2,1);
    }

    private static void sendRecord(Properties props, String bikeId, int X, int Y){

        JSONObject obj = new JSONObject();
        obj.put("bikeId", bikeId);
        obj.put("X", X);
        obj.put("Y", Y);

        ProducerRecord producerRecord = new ProducerRecord("bikes", "none", obj.toJSONString());

        KafkaProducer kafkaProducer = new KafkaProducer(props);

        kafkaProducer.send(producerRecord);
        kafkaProducer.close();
    }
}