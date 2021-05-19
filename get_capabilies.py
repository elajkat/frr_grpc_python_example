import grpc

import frr_northbound_pb2
import frr_northbound_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = frr_northbound_pb2_grpc.NorthboundStub(channel)

        request = frr_northbound_pb2.GetCapabilitiesRequest()
        res = stub.GetCapabilities(request)
        print('Supported capabilities: %s ' % res)


if __name__ == '__main__':
    run()
