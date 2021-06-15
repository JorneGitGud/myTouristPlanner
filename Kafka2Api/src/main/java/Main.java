import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.http.HttpClient;
import java.time.Duration;
import java.util.Arrays;
import java.util.Properties;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


public class Main {


    public static void main(String[] args) throws IOException {

        //Setup kafka connect
        Logger logger= LoggerFactory.getLogger(Main.class.getName());
        String bootstrapServers="localhost:9092";
        String grp_id="KafkaConsumer";
        String topic="bikes";

        //setup api connect
        URL url = new URL ("http://localhost:5000/logs");
        HttpURLConnection con = (HttpURLConnection)url.openConnection();
        con.setRequestMethod("POST");
        con.setRequestProperty("Content-Type", "application/json; utf-8");
        con.setRequestProperty("Accept", "application/json");
        con.setDoOutput(true);


        //Creating consumer properties
        Properties properties=new Properties();
        properties.setProperty(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG,bootstrapServers);
        properties.setProperty(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG,   StringDeserializer.class.getName());
        properties.setProperty(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG,StringDeserializer.class.getName());
        properties.setProperty(ConsumerConfig.GROUP_ID_CONFIG,grp_id);
        properties.setProperty(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG,"earliest");

        //creating consumer
        KafkaConsumer<String,String> consumer= new KafkaConsumer<String,String>(properties);

        //Subscribing
        consumer.subscribe(Arrays.asList(topic));

        //get and send records
        while(true){
            ConsumerRecords<String,String> records=consumer.poll(Duration.ofMillis(100));
            for(ConsumerRecord<String,String> record: records){
                System.out.println( "this" + record.value());


            }
        }
    }
}
