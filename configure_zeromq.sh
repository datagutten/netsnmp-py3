#!/usr/bin/env bash
wget --no-check-certificate "https://github.com/zeromq/libzmq/releases/download/v4.3.4/zeromq-4.3.4.tar.gz" -O zeromq-4.3.4.tar.gz
tar xzf zeromq-4.3.4.tar.gz
( cd zeromq-4.3.4 && ./configure --without-{libsodium,pgm})
