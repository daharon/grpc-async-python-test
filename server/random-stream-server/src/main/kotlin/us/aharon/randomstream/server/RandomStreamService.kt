package us.aharon.randomstream.server

import us.aharon.randomstream.RandomStreamGrpc
import us.aharon.randomstream.RandomValue

import com.google.protobuf.Empty
import io.grpc.stub.ServerCallStreamObserver
import io.grpc.stub.StreamObserver

import java.util.Vector

/**
 * Created by daharon on 10/11/16.
 */
class RandomStreamService(val clientList: Vector<ServerCallStreamObserver<RandomValue>>):
        RandomStreamGrpc.RandomStreamImplBase() {

    override fun read(request: Empty?, responseObserver: StreamObserver<RandomValue>?) {
        val scso = responseObserver as ServerCallStreamObserver<RandomValue>
        clientList.add(scso)
        scso.setOnCancelHandler {
            clientList.remove(scso)
        }
    }
}
