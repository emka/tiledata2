#!/bin/sh

cd `dirname $0`
protoc -I=. --python_out=.. tiledata.proto
