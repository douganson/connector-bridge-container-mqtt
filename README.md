mbed Device Connector integration bridge image importer for generic MQTT brokers

Original Date: August 12, 2016

5/3/2017: Updated with the latest bridge.

4/26/2017: Updated with the latest bridge (patches for R1.2 GA)

1/26/2017: Updated with the latest bridge. 

1/17/2017: Updated with the latest bridge. Happy New Year!

Container Bridge source (Apache 2.0 licensed - Enjoy!): https://github.com/ARMmbed/connector-bridge.git
 

Container Bridge Instance Installation:

1). Clone this repo into a Linux instance that supports docker

2). cd into the cloned repo and run: ./run-reload-bridge.sh

3). Next go to https://connector.mbed.com and create your mbed Connector Account

4). Once your Connector account is created, you need to "Access Keys" to create an API Key/Token

Now that you have your:

    - MQTT Broker IP Address 

    - Connector API Key/Token generated

Go to:  https://[[your containers public IP address]]:8234

    - username: "admin" (no quotes)

    - password: "admin" (no quotes)

Enter your MQTT Broker IP address and Connector API Token

    - Please press "SAVE" after *each* is entered... 

    - After all are entered and saved, press "RESTART"

Your Generic MQTT bridge should now be configured and operational. 

For your mbed endpoint, you can clone and build (via yotta) this: https://github.com/ARMmbed/mbed-ethernet-sample-withdm

    - This sample assumes you are using the NXP K64F + mbed Application Shield

NOTE: for the test scripts, I've had issues with paho-mqtt v1.2. Try v1.1... seems to work better.

Enjoy!

Copyright 2015. ARM Ltd. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License. 
