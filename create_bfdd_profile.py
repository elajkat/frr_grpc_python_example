import grpc

import frr_northbound_pb2
import frr_northbound_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = frr_northbound_pb2_grpc.NorthboundStub(channel)

        # Create a new candidate configuration change
        new_candidate = stub.CreateCandidate(
            frr_northbound_pb2.CreateCandidateRequest())
        config_d_tree = frr_northbound_pb2.DataTree(
               encoding='JSON',
               data=b'{"frr-bfdd:bfdd": {"bfd": {"profile": [{"name": '
                    b'"test-prof","detection-multiplier": 4,'
                    b'"required-receive-interval": 800000}]}}}')
        request = frr_northbound_pb2.LoadToCandidateRequest(
               candidate_id=new_candidate.candidate_id,
               type='MERGE',
               config=config_d_tree)

        # Load configuration to candidate.
        stub.LoadToCandidate(request)

        # Commit candidate
        commit_req = frr_northbound_pb2.CommitRequest(
               candidate_id=new_candidate.candidate_id,
               phase='ALL',
               comment='create test-prof')
        stub.Commit(commit_req)
