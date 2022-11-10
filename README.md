## Efento-NB-IoT-sensors-remote-configuration-examples

This quick demo will show you how to use a simple CoAP server to receive the data from Efento NB-IoT sensors and remotely change their configuration. 
> **Note**
> This is a demo implementation to explain how the response payload is generated and how to remotly reconfigure the sensors. <b>This should not be used as production code.</b>

Should you have any issues or questions, feel free to drop us a line at [help.efento.io](https://help.efento.io)

## How does it work?

This repository contains: 
 * coap_server - receives the data from Efento NB-IoT sensors and saves them in the PostgreSQL database. For more information visit getefento.com/library/efento-nb-iot-sensors-integration-with-a-python-coap-server/
* create_response_payload - library of functions used to serialize the response sent to the sensor. Responses are used to change the device's configuration.
* proto files

The server is constantly listening for data sent by Efento NB-IoT sensors. Once a new message arrives, the server parses the data, saves it in the PostgreSQL database and responds to the sensor with a configuration message created by 'create_response_payload'.

## How to use the application?
1. Setup PostgreSQL database 
2. Edit 'create_response_payload' script - set the new configuration values
3. Open 'coap_server' and choose what you want to include in the response payload by editing the line:

        response_payload = create_response_payload.METHOD_NAME_YOU_WANT_TO_USE
4. Run 'coap_server' script
5. Once a device sends a message with ACK, the server will respond with the new configuration

## Examples
To get device info from the device use:

    response_payload = create_response_payload.get_device_info()
    
To set rules on the device use:

    response_payload = create_response_payload.create_new_rules()
