#!/usr/bin/python2.4
# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2



_TAG = descriptor.Descriptor(
  name='Tag',
  full_name='tiledata.Tag',
  filename='tiledata.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='k', full_name='tiledata.Tag.k', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='v', full_name='tiledata.Tag.v', index=1,
      number=2, type=9, cpp_type=9, label=2,
      default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_NODE = descriptor.Descriptor(
  name='Node',
  full_name='tiledata.Node',
  filename='tiledata.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='tiledata.Node.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='lat', full_name='tiledata.Node.lat', index=1,
      number=2, type=2, cpp_type=6, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='lon', full_name='tiledata.Node.lon', index=2,
      number=3, type=2, cpp_type=6, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='x', full_name='tiledata.Node.x', index=3,
      number=4, type=5, cpp_type=1, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='y', full_name='tiledata.Node.y', index=4,
      number=5, type=5, cpp_type=1, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='tag', full_name='tiledata.Node.tag', index=5,
      number=6, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_WAY = descriptor.Descriptor(
  name='Way',
  full_name='tiledata.Way',
  filename='tiledata.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='tiledata.Way.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='node', full_name='tiledata.Way.node', index=1,
      number=2, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='tag', full_name='tiledata.Way.tag', index=2,
      number=3, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_OSM = descriptor.Descriptor(
  name='Osm',
  full_name='tiledata.Osm',
  filename='tiledata.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='poi', full_name='tiledata.Osm.poi', index=0,
      number=1, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='way', full_name='tiledata.Osm.way', index=1,
      number=2, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timestamp', full_name='tiledata.Osm.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_NODE.fields_by_name['tag'].message_type = _TAG
_WAY.fields_by_name['node'].message_type = _NODE
_WAY.fields_by_name['tag'].message_type = _TAG
_OSM.fields_by_name['poi'].message_type = _NODE
_OSM.fields_by_name['way'].message_type = _WAY

class Tag(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TAG

class Node(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NODE

class Way(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _WAY

class Osm(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OSM
