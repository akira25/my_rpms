Name:           gr-satellites-next
Version:        5.8.0git
Release:        2
Summary:        GNU Radio OOT module with a collection of decoders for Amateur satellites; Main-branch

License:        GPL-3.0-or-later
URL:            https://gr-satellites.readthedocs.io
Source0:        https://github.com/daniestevez/gr-satellites/archive/refs/heads/main.tar.gz#/%{name}-%{version}.tar.gz


BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-g++
BuildRequires:  gmp-devel
BuildRequires:  gnupg2
BuildRequires:  gnuradio-devel
BuildRequires:  liborc-devel
BuildRequires:  libsndfile-devel
BuildRequires:  make
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  spdlog-devel
BuildRequires:  texinfo

Requires:  gnuradio
Requires:  python3-construct
Requires:  python3-requests
Requires:  python3-websocket-client

%description
gr-satellites is a GNU Radio out-of-tree module encompassing a collection
of telemetry decoders that supports many different Amateur satellites. This
open-source project started in 2015 with the goal of providing telemetry
decoders for all the satellites that transmit on the Amateur radio bands.

It supports most popular protocols, such as AX.25, the GOMspace NanoCom U482C
and AX100 modems, an important part of the CCSDS stack, the AO-40 protocol used
in the FUNcube satellites, and several ad-hoc protocols used in other
satellites.

This out-of-tree module can be used to decode frames transmitted from most
Amateur satellites in orbit, performing demodulation, forward error correction,
etc. Decoded frames can be saved to a file or displayed in hex format. For some
satellites the telemetry format definition is included in gr-satellites, so the
decoded telemetry frames can be printed out as human-readable values such as bus
voltages and currents. Additionally, some satellites transmit files such as JPEG
images. gr-satellites can be used to reassemble these files and even display the
images in real-time as they are being received.

gr-satellites can be used as a set of building blocks to implement decoders for
other satellites or other ground station solutions. Some of the low level blocks
in gr-satellites are also useful for other kinds of RF communications protocols.

%package devel
Summary: Development files for gr-satellites-next
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gnuradio-devel
Requires: python3-construct
Requires: python3-requests
Requires: python3-websocket-client

%description devel
Development files for gr-satellites-next

%prep
%setup -q -n gr-satellites-main

# Remove some GitHub-specific files
rm -rf .github || true
rm -rf parts/.github || true

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

# repair wrong line endings, merged upstream already. Will be obsolete with
# versions after 5.6.0
for file in %{buildroot}%{python3_sitearch}/satellites/telemetry/{cute_70cm,inspiresat_1}.py; do
    sed -i 's/\r$//' $file
done

# make python scripts executable
for file in %{buildroot}%{python3_sitearch}/satellites/*.py; do
    chmod a+x $file
done
for file in %{buildroot}%{python3_sitearch}/satellites/ccsds/*.py; do
   chmod a+x $file
done
for file in %{buildroot}%{python3_sitearch}/satellites/components/*.py; do
   chmod a+x $file
done
for file in %{buildroot}%{python3_sitearch}/satellites/components/{datasinks,datasources,deframers,demodulators,transports}/*.py; do
   chmod a+x $file
done
for file in %{buildroot}%{python3_sitearch}/satellites/core/*.py; do
   chmod a+x $file
done
chmod +x %{buildroot}%{python3_sitearch}/satellites/hier/__init__.py
for file in %{buildroot}%{python3_sitearch}/satellites/{filereceiver,satyaml,telemetry,usp,utils}/*.py; do
   chmod a+x $file
done

%check
make test

%files
%doc README.md
%license LICENSE
%{_bindir}/gr_satellites_ssdv
%{_bindir}/gr_satellites
%{_bindir}/smog_p_spectrum
%{_libdir}/cmake/satellites/*
%{_libdir}/libgnuradio-satellites.so*
%{python3_sitearch}/satellites/*
%{_datadir}/gnuradio/grc/blocks/*
%{_datadir}/man/man1/gr_satellites.1.gz
%{_datadir}/man/man1/smog_p_spectrum.1.gz
%{_datadir}/man/man1/gr_satellites_ssdv.1.gz

%files devel
%doc README.md
%license LICENSE
%{_includedir}/satellites/*
%{_libdir}/cmake/satellites/*
%{python3_sitearch}/satellites/*
%{_datadir}/gnuradio/grc/blocks/*

%changelog
%autochangelog
