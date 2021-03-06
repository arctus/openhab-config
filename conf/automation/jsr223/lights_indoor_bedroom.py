from marvin.helper import rule, sendCommand
from core.triggers import ItemStateChangeTrigger


@rule("lights_indoor_bedroom_control.py")
class LightsIndoorBedroomControlRule:
    def __init__(self):
        self.triggers = [
            ItemStateChangeTrigger("Light_SF_Bedroom_Left_Long_Pressed", state="ON"),
            ItemStateChangeTrigger("Light_SF_Bedroom_Right_Long_Pressed", state="ON")
        ]

    def execute(self, module, input):
        sendCommand("Scene4", ON)
