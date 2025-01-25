import reflex as rx
from reflex.components.component import NoSSRComponent
from loguru import logger
import simplepyble
from typing import List, Dict



class BleComponent(rx.Component):
    # Use an absolute path starting with /public
    library = "/assets/BleComponent"

class BleManager(rx.Component):
    # Use an absolute path starting with /public
    library = "/assets/BleManager"
    tag = "manager"


class ReactNativeBlePlx(NoSSRComponent):
    library = "react-native-ble-plx"






class BleState(rx.State):
    adapters: List[Dict] = []
#     selected_adapter_index: int = 0
#     peripherals: list = []
#     selected_peripheral_index: int = 0
#     connected: bool = False
#     services: list = []
#     scanning: bool = False
#     scan_results: str = ""
#     connection_status: str = ""

    @rx.event
    def set_adapters(self):
        return_list = []
        local_adapters = simplepyble.Adapter.get_adapters()
        if len(local_adapters) == 0:
            logger.info("No adapters found")
        for adapter in local_adapters:
            logger.info(f"Adapter: {adapter.identifier()} [{adapter.address()}]")
            return_list.append({'identifier': adapter.identifier(), 'address': adapter.address()})
        self.adapters = return_list
    

#     def start_scan(self):
#         """Start BLE scan."""
#         self.scanning = True
#         self.adapters = simplepyble.Adapter.get_adapters()
        
#         if len(self.adapters) == 0:
#             self.scan_results = "No adapters found"
#             self.scanning = False
#             return
            
#         adapter = self.adapters[self.selected_adapter_index]
#         adapter.set_callback_on_scan_start(lambda: self.set_scan_results("Scan started."))
#         adapter.set_callback_on_scan_stop(lambda: self.set_scan_results("Scan complete."))
#         adapter.set_callback_on_scan_found(
#             lambda peripheral: self.set_scan_results(
#                 f"Found {peripheral.identifier()} [{peripheral.address()}]"
#             )
#         )
        
#         adapter.scan_for(5000)
#         self.peripherals = adapter.scan_get_results()
#         self.scanning = False
    
#     def connect_peripheral(self):
#         """Connect to selected peripheral."""
#         if not self.peripherals:
#             self.connection_status = "No peripherals available"
#             return
            
#         peripheral = self.peripherals[self.selected_peripheral_index]
#         self.connection_status = f"Connecting to: {peripheral.identifier()} [{peripheral.address()}]"
        
#         try:
#             peripheral.connect()
#             self.connected = True
#             self.services = peripheral.services()
#             services_info = []
#             for service in self.services:
#                 service_info = f"Service: {service.uuid()}\n"
#                 for characteristic in service.characteristics():
#                     capabilities = " ".join(characteristic.capabilities())
#                     service_info += f"    Characteristic: {characteristic.uuid()}\n"
#                     service_info += f"    Capabilities: {capabilities}\n"
#                 services_info.append(service_info)
#             self.connection_status = "\n".join(services_info)
#         except Exception as e:
#             self.connection_status = f"Connection failed: {str(e)}"
#             self.connected = False
    
#     def disconnect_peripheral(self):
#         """Disconnect from peripheral."""
#         if self.connected and self.peripherals:
#             peripheral = self.peripherals[self.selected_peripheral_index]
#             peripheral.disconnect()
#             self.connected = False
#             self.connection_status = "Disconnected"



    # if len(adapters) == 0:
    #     print("No adapters found")

    # for adapter in adapters:
    #     print(f"Adapter: {adapter.identifier()} [{adapter.address()}]")

def colored_box(identifier: str, address: str):
    return rx.box(rx.text(f"{identifier}--{address}"), bg='red')

def index():
    return rx.center(
        rx.vstack(
            rx.center(rx.heading("BLE Scanner", font_size="1.5em")),
                rx.button("Connect", on_click=BleState.set_adapters())
            , rx.cond(BleState.adapters,
                    rx.foreach(BleState.adapters, lambda i: rx.center(colored_box(i.identifier, i.address))),
            rx.text("No adapters found")
        )))
    # """The main page."""
    # return rx.center(
    #     rx.vstack(
    #         rx.heading("BLE Scanner", font_size="1.5em"),
            
    #         # Adapter selection
    #         rx.foreach(BleState.adapters, lambda i: colored_box(i.identifier(), i.address())),
    #         #rx.select(options=rx.foreach(range(State.adapters), lambda i: {"label": f"{i}: {i.identifier()} [{i.address()}]", "value": str(i)}),
    #         #rx.select(options=rx.foreach(range(State.adapters), lambda adapter, i: {"label": f"{i}: {adapter.identifier()} [{adapter.address()}]", "value": str(i)}),
    #             placeholder="Select adapter...",
    #             #on_change=set_selected_adapter_index,
    #             width="25em",
    #         )),
            
            # Scan button
            # rx.button(
            #     "Scan for Devices",
            #     on_click=BleState.start_scan,
            #     width="25em",
            #     is_loading=BleState.scanning,
            # ),
            
            # # Scan results
            # rx.text(BleState.scan_results),
            
            ## Peripheral selection
            # rx.cond(
            #     State.peripherals,
            #     rx.vstack(
            #         rx.select(
            #             options=rx.foreach(
            #                 State.peripherals,
            #                 lambda p, i: {"label": f"{i}: {p.identifier()} [{p.address()}]", "value": str(i)}
            #             ),
            #             placeholder="Select device...",
            #             on_change=State.set_selected_peripheral_index,
            #             width="25em",
            #         ),
            #         rx.hstack(
            #             rx.button(
            #                 "Connect",
            #                 on_click=State.connect_peripheral,
            #                 is_disabled=State.connected,
            #             ),
            #             rx.button(
            #                 "Disconnect",
            #                 on_click=State.disconnect_peripheral,
            #                 is_disabled=~State.connected,
            #             ),
            #         ),
            #     ),
            # ),
            
        #     # Connection status and services
        #     rx.text_area(
        #         rx.cond(State.connection_status,
        #         is_read_only=True,
        #         width="25em",
        #         height="15em",
        #         visibility="visible" if State.connection_status else "hidden",
        #     )),
            
        #     align="center",
        #     spacing="1em",
        # ),

# Add state and page to the app.
app = rx.App()
app.add_page(index)
