import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.json.simple.parser.JSONParser;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.Duration;
import java.util.Arrays;
import java.util.Properties;


public class Main {


    public static void main(String[] args) throws URISyntaxException, IOException, InterruptedException {

        //Setup kafka connect
        Logger logger= LoggerFactory.getLogger(Main.class.getName());
        String bootstrapServers="localhost:9092";
        String grp_id="KafkaConsumer";
        String topic="bikes";

        //setup api connect
        var logsUri = new URI("http://localhost:5000/logs/");
        var bikesUri = new URI("http://localhost:5000/bikes/");
        var client = HttpClient.newHttpClient();


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
            for(ConsumerRecord<String,String> record: records) {
                String bikeObject = record.value();
                //send to api
                System.out.println("value"+record.value());
                var request =  HttpRequest.newBuilder(logsUri).POST(HttpRequest.BodyPublishers.ofString(bikeObject)).header("content-type", "application/json").build();
                var response = client.send(request, HttpResponse.BodyHandlers.discarding());
                System.out.println( response.toString());

                request =  HttpRequest.newBuilder(bikesUri).POST(HttpRequest.BodyPublishers.ofString(bikeObject)).header("content-type", "application/json").build();
                response = client.send(request, HttpResponse.BodyHandlers.discarding());
                System.out.println( response.toString());
            }
        }
    }
}
