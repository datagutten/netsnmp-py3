#!/usr/bin/env bash
wget --no-check-certificate "https://github.com/zeromq/czmq/releases/download/v4.2.1/czmq-4.2.1.tar.gz" -O czmq-4.2.1.tar.gz
tar xzf czmq-4.2.1.tar.gz
( cd czmq-4.2.1 && ./configure)