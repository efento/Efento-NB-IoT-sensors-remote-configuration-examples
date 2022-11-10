## Efento-NB-IoT-sensors-remote-configuration-examples

This quick tutorial will show you how to use a simple CoAP server for remote configuration of Efento NB-Iot sensors. Should you have any issues or questions, feel free to drop us a line at help.efento.io

## How does it work?

This application consists of: 
 * coap_server - receives data from Efento NB-IoT sensors and saves them in the PostgreSQL database. For more information visit getefento.com/library/efento-nb-iot-sensors-integration-with-a-python-coap-server/
* create_response_payload -includes methods for creating response for remote configuration.
* proto files

The server is constantly listening for data sent by Efento NB-IoT sensors. Once a new message arrives, the server parses the data, saves it in the PostgreSQL database and responds to the sensor with configuration message created by create_response_payload.
## How to use the application?
1. Setup PostgreSQL database 
2. Open the script create_response_payload and set your configuration.
3. Open the coap server and choose your configuration.
    response_payload = create_response_payload.get_device_info()
4. Run server.