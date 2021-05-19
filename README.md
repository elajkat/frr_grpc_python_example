FRRrouting Northbound example with python
=========================================

FRR has an experimental gRPC northbound interface, see:
[FRR Northbound gRPC](https://docs.frrouting.org/en/latest/grpc.html)

gRPC itself has several language bindings, for details see:
[gRPC Supported languages](https://grpc.io/docs/languages/)

FRR documentation has gRPC example for Ruby:
[Northbound gRPC Programming Language Bindings](http://docs.frrouting.org/projects/dev-guide/en/latest/grpc.html)

Here You can find a similar example for python.

Install FRR with gRPC support
-----------------------------

As a starting point:
[Ubuntu20.04 innstall from source](http://docs.frrouting.org/projects/dev-guide/en/latest/building-frr-for-ubuntu2004.html)

To build frr with gRPC enabled when executing configure
add the following ``--enable-grpc``:

    $ ./configure \
        --prefix=/usr \
        --includedir=\${prefix}/include \
        --enable-exampledir=\${prefix}/share/doc/frr/examples \
        --bindir=\${prefix}/bin \
        --sbindir=\${prefix}/lib/frr \
        --libdir=\${prefix}/lib/frr \
        --libexecdir=\${prefix}/lib/frr \
        --localstatedir=/var/run/frr \
        --sysconfdir=/etc/frr \
        --with-moduledir=\${prefix}/lib/frr/modules \
        --with-libyang-pluginsdir=\${prefix}/lib/frr/libyang_plugins \
        --enable-configfile-mask=0640 \
        --enable-logfile-mask=0640 \
        --enable-snmp=agentx \
        --enable-multipath=64 \
        --enable-user=frr \
        --enable-group=frr \
        --enable-vty-group=frrvty \
        --with-pkg-git-version \
        --with-pkg-extra-version=-MyOwnFRRVersion
        --enable-grpc
        --enable-systemd=yes

When you have all systemd file and config in place, 
enable bfd in daemons file (/etc/frr/daemons):
https://docs.frrouting.org/en/latest/grpc.html#daemon-grpc-configuration

    ...
    bfdd=yes
    ...
    bfdd_options="   --daemon -A 127.0.0.1 -M grpc" 
    ...

    $ sudo systemctl restart frr.service

Install python env for gRPC
---------------------------

From [gRPC python Quick Start](https://grpc.io/docs/languages/python/quickstart/):

    $ mkdir frr_example; cd frr_example
    $ virtualenv frrgrpcvenv
    $ source frrgrpcvenv/bin/activate
    (frrgrpcvenv) $ pip install grpcio
    (frrgrpcvenv) $ pip install grpcio-tools

Next the proto file must be converted as next step.
The proto file is in the frr repo under grpc folder:
https://github.com/FRRouting/frr/blob/master/grpc/frr-northbound.proto
 
    (frrgrpcvenv) $ python -m grpc_tools.protoc -I~/frr/grpc --python_out=. --grpc_python_out=. ~/frr/grpc/frr-northbound.proto

After this the following 2 files should have in your folder:
* frr_northbound_pb2.py
* frr_northbound_pb2_grpc.py
