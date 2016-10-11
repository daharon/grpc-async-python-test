package us.aharon.randomstream

import com.google.protobuf.Empty
import io.grpc.ManagedChannelBuilder

/**
 * Created by daharon on 10/11/16.
 */

fun main(args: Array<String>) {

    val channel = ManagedChannelBuilder
            .forAddress("localhost", 9000)
            .usePlaintext(true)
            .build()
    val blockingStub = RandomStreamGrpc.newBlockingStub(channel)

    val randomValues = blockingStub.read(Empty.getDefaultInstance())

    while (randomValues.hasNext()) {
        println("Read value: 0x%X".format(randomValues.next().value))
    }
}
