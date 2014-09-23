#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface:
  def sendSMS(self, msg, phones):
    """
    Parameters:
     - msg
     - phones
    """
    pass

  def sendMail(self, mail):
    """
    Parameters:
     - mail
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def sendSMS(self, msg, phones):
    """
    Parameters:
     - msg
     - phones
    """
    self.send_sendSMS(msg, phones)
    return self.recv_sendSMS()

  def send_sendSMS(self, msg, phones):
    self._oprot.writeMessageBegin('sendSMS', TMessageType.CALL, self._seqid)
    args = sendSMS_args()
    args.msg = msg
    args.phones = phones
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_sendSMS(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = sendSMS_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.rpcException is not None:
      raise result.rpcException
    raise TApplicationException(TApplicationException.MISSING_RESULT, "sendSMS failed: unknown result");

  def sendMail(self, mail):
    """
    Parameters:
     - mail
    """
    self.send_sendMail(mail)
    return self.recv_sendMail()

  def send_sendMail(self, mail):
    self._oprot.writeMessageBegin('sendMail', TMessageType.CALL, self._seqid)
    args = sendMail_args()
    args.mail = mail
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_sendMail(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = sendMail_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.rpcException is not None:
      raise result.rpcException
    raise TApplicationException(TApplicationException.MISSING_RESULT, "sendMail failed: unknown result");


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["sendSMS"] = Processor.process_sendSMS
    self._processMap["sendMail"] = Processor.process_sendMail

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_sendSMS(self, seqid, iprot, oprot):
    args = sendSMS_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = sendSMS_result()
    try:
      result.success = self._handler.sendSMS(args.msg, args.phones)
    except NoticeRPCException, rpcException:
      result.rpcException = rpcException
    oprot.writeMessageBegin("sendSMS", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_sendMail(self, seqid, iprot, oprot):
    args = sendMail_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = sendMail_result()
    try:
      result.success = self._handler.sendMail(args.mail)
    except NoticeRPCException, rpcException:
      result.rpcException = rpcException
    oprot.writeMessageBegin("sendMail", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class sendSMS_args:
  """
  Attributes:
   - msg
   - phones
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'msg', (NoticeSMSMessage, NoticeSMSMessage.thrift_spec), None, ), # 1
    (2, TType.LIST, 'phones', (TType.STRING,None), None, ), # 2
  )

  def __init__(self, msg=None, phones=None,):
    self.msg = msg
    self.phones = phones

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.msg = NoticeSMSMessage()
          self.msg.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.phones = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readString();
            self.phones.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('sendSMS_args')
    if self.msg is not None:
      oprot.writeFieldBegin('msg', TType.STRUCT, 1)
      self.msg.write(oprot)
      oprot.writeFieldEnd()
    if self.phones is not None:
      oprot.writeFieldBegin('phones', TType.LIST, 2)
      oprot.writeListBegin(TType.STRING, len(self.phones))
      for iter6 in self.phones:
        oprot.writeString(iter6)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class sendSMS_result:
  """
  Attributes:
   - success
   - rpcException
  """

  thrift_spec = (
    (0, TType.STRING, 'success', None, None, ), # 0
    (1, TType.STRUCT, 'rpcException', (NoticeRPCException, NoticeRPCException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, rpcException=None,):
    self.success = success
    self.rpcException = rpcException

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRING:
          self.success = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.rpcException = NoticeRPCException()
          self.rpcException.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('sendSMS_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRING, 0)
      oprot.writeString(self.success)
      oprot.writeFieldEnd()
    if self.rpcException is not None:
      oprot.writeFieldBegin('rpcException', TType.STRUCT, 1)
      self.rpcException.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class sendMail_args:
  """
  Attributes:
   - mail
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'mail', (NoticeEmailMessage, NoticeEmailMessage.thrift_spec), None, ), # 1
  )

  def __init__(self, mail=None,):
    self.mail = mail

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.mail = NoticeEmailMessage()
          self.mail.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('sendMail_args')
    if self.mail is not None:
      oprot.writeFieldBegin('mail', TType.STRUCT, 1)
      self.mail.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class sendMail_result:
  """
  Attributes:
   - success
   - rpcException
  """

  thrift_spec = (
    (0, TType.STRING, 'success', None, None, ), # 0
    (1, TType.STRUCT, 'rpcException', (NoticeRPCException, NoticeRPCException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, rpcException=None,):
    self.success = success
    self.rpcException = rpcException

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRING:
          self.success = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.rpcException = NoticeRPCException()
          self.rpcException.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('sendMail_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRING, 0)
      oprot.writeString(self.success)
      oprot.writeFieldEnd()
    if self.rpcException is not None:
      oprot.writeFieldBegin('rpcException', TType.STRUCT, 1)
      self.rpcException.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
