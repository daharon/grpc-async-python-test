package us.aharon.randomstream

import com.google.protobuf.Timestamp
import io.grpc.ServerBuilder
import io.grpc.stub.StreamObserver

import java.util.logging.Logger
import java.util.*

import kotlin.concurrent.fixedRateTimer
import kotlin.concurrent.thread

import us.aharon.randomstream.server.RandomStreamService

/**
 * Created by daharon on 10/11/16.
 */

fun main(args: Array<String>) {
    val port = 9000
    val log = Logger.getLogger("RandomStream Server")
    val randomStreamClientList = Vector<StreamObserver<RandomValue>>()
    val randomValueGenerator = fixedRateTimer(null, true, 100, 500) {
        val randomValue = Random().nextLong()
        log.info("Generated random value: " + randomValue)
        val millis = System.currentTimeMillis()
        val timestamp = Timestamp.newBuilder()
                .setSeconds(millis / 1000)
                .setNanos(((millis % 1000) * 1000000).toInt())
                .build()
        val randomValueMsg = RandomValue.newBuilder()
                .setTimestamp(timestamp)
                .setValue(randomValue)
                .build()

        log.info("Client list size: " + randomStreamClientList.size)
        randomStreamClientList.forEach {
            log.info("Writing to client: " + it)
            it.onNext(randomValueMsg)
        }
    }

    val server = ServerBuilder.forPort(port)
            .addService(RandomStreamService(randomStreamClientList))
            .build()
    server.start()
    log.info("Server started, listening on port " + port)

    /*
    Runtime.getRuntime().addShutdownHook(thread {
        log.info("Shutting down gRPC server")
        server?.shutdown()
        log.info("gRPC server shut down")
    })
    */

    server.awaitTermination()
}
