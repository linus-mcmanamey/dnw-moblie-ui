// File: .web/components/BleComponent.js
import React, { useEffect, useState } from 'react';
import { BleManager } from 'react-native-ble-plx';

const BleComponent = () => {
  const [bleManager] = useState(new BleManager());

  useEffect(() => {
    const subscription = bleManager.onStateChange((state) => {
      if (state === 'PoweredOn') {
        scanAndConnect();
      }
    }, true);

    return () => subscription.remove();
  }, [bleManager]);

  const scanAndConnect = () => {
    bleManager.startDeviceScan(null, null, (error, device) => {
      if (error) {
        console.error(error);
        return;
      }

      if (device.name === 'DesiredDeviceName') {
        bleManager.stopDeviceScan();

        device.connect()
          .then((device) => {
            return device.discoverAllServicesAndCharacteristics();
          })
          .then((device) => {
            // Do work on device with services and characteristics
          })
          .catch((error) => {
            console.error(error);
          });
      }
    });
  };

  return (
    <div>
      <h1>BLE Component</h1>
      <p>Scanning for BLE devices...</p>
    </div>
  );
};
console.log(BleComponent);
export default BleComponent;