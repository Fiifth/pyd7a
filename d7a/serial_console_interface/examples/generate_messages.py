
from d7a.d7anp.addressee import Addressee, IdType
from d7a.sp.qos import QoS, ResponseMode
from d7a.alp.command import *
from d7a.serial_console_interface.parser import *
from pprint import pprint
import binascii

from d7a.types.ct import CT


def output_serial_frame(description, command):
  print("\n=== {0} ===\n".format(description))

  serial_frame = Parser.build_serial_frame(command)
  print("command:")
  pprint(command.as_dict())
  print("serial frame:")
  print(binascii.hexlify(serial_frame).decode("ascii"))

output_serial_frame(
  "Return file data, with QoS, unicast",
  Command.create_with_return_file_data_action(
    file_id=0x40,
    data=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    interface_type=InterfaceType.D7ASP,
    interface_configuration=Configuration(
      qos=QoS(resp_mod=ResponseMode.RESP_MODE_ALL),
      addressee=Addressee(
        access_class=0,
        id_type=IdType.UID,
        id=2656824718681607041 # TODO hex string
      )
    )
  )
)

output_serial_frame(
  "Return file data, with QoS, broadcast",
  Command.create_with_return_file_data_action(
    file_id=0x40,
    data=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    interface_type=InterfaceType.D7ASP,
    interface_configuration=Configuration(
      qos=QoS(resp_mod=ResponseMode.RESP_MODE_ALL),
      addressee=Addressee(
        access_class=2,
        id_type=IdType.NOID
      )
    )
  )
)

output_serial_frame(
  "Return file data, without QoS, broadcast",
  Command.create_with_return_file_data_action(
    file_id=0x40,
    data=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    interface_type=InterfaceType.D7ASP,
    interface_configuration=Configuration(
      qos=QoS(resp_mod=ResponseMode.RESP_MODE_NO),
      addressee=Addressee(access_class=0x01, id_type=IdType.NOID)
    )
  )
)

output_serial_frame(
  "Return file data, with QoS, unicast",
  Command.create_with_return_file_data_action(
    file_id=0x40,
    data=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    interface_type=InterfaceType.D7ASP,
    interface_configuration=Configuration(
      qos=QoS(resp_mod=ResponseMode.RESP_MODE_ANY),
      addressee=Addressee(
        access_class=2,
        id_type=IdType.UID,
        id=0xDEADBEEFCAFEBABE
      )
    )
  )
)

output_serial_frame(
  "Read ID file, with QoS, broadcast",
  Command.create_with_read_file_action(
    file_id=0x00,
    offset=0,
    length=8,
    interface_type=InterfaceType.D7ASP,
    interface_configuration=Configuration(
      qos=QoS(resp_mod=ResponseMode.RESP_MODE_ANY),
      addressee=Addressee(
        id_type=IdType.NOID,
        access_class=0x01
      )
    )
  )
)

output_serial_frame(
  "Dormant session, write file",
    Command.create_with_write_file_action(
      file_id=0x40,
      offset=0,
      data=[0],
      interface_type=InterfaceType.D7ASP,
      interface_configuration=Configuration(
        qos=QoS(resp_mod=ResponseMode.RESP_MODE_ANY),
        addressee=Addressee(
          id_type=IdType.UID,
          id=0xE0022600017B388F,
          access_class=0x21
        ),
        dorm_to=CT.compress(60 * 5)
      )
    )
)