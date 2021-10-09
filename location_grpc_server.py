import time
from concurrent import futures

import grpc
import LocationEvent_pb2
import LocationEvent_pb2_grpc


class LocationEventServicer(LocationEvent_pb2_grpc.ItemServiceServicer):

   
        def Create(self, request, context):

            request_value = {
                 "personId": request.personId,
                 "latitude": request.latitude,
                 "longitude": request.longitude,
              }
            print(request_value)

            return LocationEvent_pb2.LocationEventMessage(**request_value)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
LocationEvent_pb2_grpc.add_ItemServiceServicer_to_server(LocationEventServicer(), server)
print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
