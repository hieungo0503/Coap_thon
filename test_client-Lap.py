import schedule
import time
from coapthon.client.helperclient import HelperClient

def coap_client_job():
    host = "115.78.92.253"
    port = 9999
    path = "message/coap/data"
    payload ="0"

    try:
        client = HelperClient(server=(host, port))
        response = client.post(path, payload,None,1000,1)
        print("Response from server:", response)
    finally:
        client.stop()

# Schedule the job to run every day at 19:00
schedule.every().day.at("11:23").do(coap_client_job)

# Run the scheduler in an infinite loop
while True:
    schedule.run_pending()
    time.sleep(1)  # Sleep for 1 second to avoid high CPU usage
