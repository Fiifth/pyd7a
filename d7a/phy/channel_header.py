from enum import Enum

from d7a.support.schema import Validatable, Types


class ChannelCoding(Enum):
  PN9 = 0x00
  FEC_PN9 = 0x02


class ChannelClass(Enum):
  LO_RATE = 0x00
  NORMAL_RATE = 0x02
  HI_RATE = 0x03

class ChannelBand(Enum):
  BAND_433 = 0x02
  BAND_868 = 0x03
  BAND_915 = 0x04

class ChannelHeader(Validatable):
  # TODO
  SCHEMA = [{
    "channel_coding": Types.ENUM(ChannelCoding),
    "channel_class": Types.ENUM(ChannelClass),
    "channel_band": Types.ENUM(ChannelBand)
  }]

  def __init__(self, channel_coding, channel_class, channel_band):
    self.channel_coding = channel_coding
    self.channel_class = channel_class
    self.channel_band = channel_band
    super(ChannelHeader, self).__init__()

  # TODO byte generation