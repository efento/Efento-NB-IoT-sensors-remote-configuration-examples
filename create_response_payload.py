from protobuf import proto_config_pb2
from protobuf import proto_rule_pb2

rules = proto_rule_pb2.ProtoRule()
device_config = proto_config_pb2.ProtoConfig()

def get_device_info():
    device_config.request_device_info = True
    return device_config.SerializeToString()

def set_configuration_parameters():
    """
    To set calibration parameters, send to a sensor message with the values:

    calibration_request - requested channel number. bitmask bits[0:2].
    parameters - table of calibration parameters.
    channel_assignment - assignment of a channel. Code specific for each sensor driver used for validating the request [hex].

    General information about the rules configuration you find in https://jira.efento.io/browse/ES6-1016
    """
    # Set calibration parameters with protobuf fields.
    device_config.calibration_parameters_request.calibration_request = 0b001
    device_config.calibration_parameters_request.channel_assignment = 0x39
    device_config.calibration_parameters_request.parameters.extend([0, 5, 10])

    return device_config.SerializeToString()


def get_configuration_parameters():
    """
     To get calibration parameters,Set first three bits of the calibration_request with channel number of the sensor of interest. Set remaining bits to zero.
    """
    device_config.calibration_parameters_request.calibration_request = 0b001
    device_config.calibration_parameters_request.channel_assignment = 0x39
    return device_config.SerializeToString()

def create_new_rules():
    """
    To create or edit a rule, send to a sensor message with the values:

    channel mask - channels to which the rule is assigned bitmask on bits [0:5],
    condition - condition to be checked by the device,
    parameters - table of parameters for the condition to be checked by the device,
    action -  action to be triggered

    General information about the rules configuration you find in https://github.com/efento/Proto-files/blob/06.10.XX/proto_rule.proto.
    """

    # Set rules parameters  with protobuf fields from ProtoRule object .
    rules.channel_mask = 0b000001
    rules.condition = 2
    # Add the table of parameters values to the protobuf field "parameters".
    rules.parameters.extend([500, 0, 2, 3, 1])
    rules.action = 2
    # Add all parameters to the table of rules configuration with Protoconfig object.
    device_config.rules.extend([rules])

    #To set next rules add rules parameters to next position in the table of rules configuration.
    rules.channel_mask = 0b000010
    rules.condition = 2
    rules.ClearField("parameters")
    rules.parameters.extend([50, 0, 2, 3, 2])
    rules.action = 2
    device_config.rules.extend([rules])

    # To add logic operator set condition to 6 and assign rules in parameter number 2 (bitmask on bits[0:11]).
    rules.condition = 6
    rules.action = 2
    rules.ClearField("parameters")
    rules.parameters.extend([1, 0b00000000011, 0, 0, 0])
    device_config.rules.extend([rules])

    return device_config.SerializeToString()

def edit_rules():

    # If rule should not be edited, set all parameters to 0.
    rules.channel_mask = 0
    rules.condition = 0
    rules.action = 0
    rules.parameters.extend([0, 0, 0, 0, 0])
    device_config.rules.extend([rules])

    # To edit a rule, send new values, which will overwrite the old ones.
    rules.channel_mask = 0b000010
    rules.condition = 3
    rules.action = 2
    rules.ClearField("parameters")
    rules.parameters.extend([5, 0, 1, 3, 2])
    device_config.rules.extend([rules])

    rules.condition = 0
    rules.action = 0
    rules.ClearField("parameters")
    rules.parameters.extend([0, 0, 0, 0, 0])
    device_config.rules.extend([rules])

    return device_config.SerializeToString()

def detete_rules():
    # To disable a rule set "Condition" value to 1 (threshold disabled), and all the other parameters to 0
    rules.channel_mask = 0
    rules.condition = 1
    rules.action = 0
    rules.parameters.extend([0, 0, 0, 0, 0])
    device_config.rules.extend([rules])

    return device_config.SerializeToString()