# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/portainer.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/portainer.proto',
  package='portainer',
  serialized_pb='\n\x15proto/portainer.proto\x12\tportainer\"\x91\x01\n\tBuildTask\x12%\n\x05image\x18\x01 \x02(\x0b\x32\x16.portainer.DockerImage\x12\x0f\n\x07\x63ontext\x18\x02 \x01(\t\x12\x12\n\ndockerfile\x18\x06 \x01(\t\x12\x0e\n\x06stream\x18\x05 \x01(\x08\x12\x13\n\x0b\x64ocker_host\x18\x03 \x01(\t\x12\x13\n\x0b\x64ocker_args\x18\x04 \x01(\t\"[\n\x0b\x44ockerImage\x12+\n\x08registry\x18\x02 \x01(\x0b\x32\x19.portainer.DockerRegistry\x12\x12\n\nrepository\x18\x01 \x02(\t\x12\x0b\n\x03tag\x18\x03 \x03(\t\"4\n\x0e\x44ockerRegistry\x12\x10\n\x08hostname\x18\x01 \x02(\t\x12\x10\n\x04port\x18\x02 \x01(\r:\x02\x38\x30')




_BUILDTASK = _descriptor.Descriptor(
  name='BuildTask',
  full_name='portainer.BuildTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='portainer.BuildTask.image', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='context', full_name='portainer.BuildTask.context', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dockerfile', full_name='portainer.BuildTask.dockerfile', index=2,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stream', full_name='portainer.BuildTask.stream', index=3,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='docker_host', full_name='portainer.BuildTask.docker_host', index=4,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='docker_args', full_name='portainer.BuildTask.docker_args', index=5,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=37,
  serialized_end=182,
)


_DOCKERIMAGE = _descriptor.Descriptor(
  name='DockerImage',
  full_name='portainer.DockerImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='registry', full_name='portainer.DockerImage.registry', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='repository', full_name='portainer.DockerImage.repository', index=1,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag', full_name='portainer.DockerImage.tag', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=184,
  serialized_end=275,
)


_DOCKERREGISTRY = _descriptor.Descriptor(
  name='DockerRegistry',
  full_name='portainer.DockerRegistry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hostname', full_name='portainer.DockerRegistry.hostname', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='portainer.DockerRegistry.port', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=80,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=277,
  serialized_end=329,
)

_BUILDTASK.fields_by_name['image'].message_type = _DOCKERIMAGE
_DOCKERIMAGE.fields_by_name['registry'].message_type = _DOCKERREGISTRY
DESCRIPTOR.message_types_by_name['BuildTask'] = _BUILDTASK
DESCRIPTOR.message_types_by_name['DockerImage'] = _DOCKERIMAGE
DESCRIPTOR.message_types_by_name['DockerRegistry'] = _DOCKERREGISTRY

class BuildTask(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BUILDTASK

  # @@protoc_insertion_point(class_scope:portainer.BuildTask)

class DockerImage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DOCKERIMAGE

  # @@protoc_insertion_point(class_scope:portainer.DockerImage)

class DockerRegistry(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DOCKERREGISTRY

  # @@protoc_insertion_point(class_scope:portainer.DockerRegistry)


# @@protoc_insertion_point(module_scope)
