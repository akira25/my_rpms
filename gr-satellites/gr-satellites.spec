Name:           gr-satellites
Version:        5.9.0
Release:        %autorelease
Summary:        GNU Radio OOT module with a collection of decoders for Amateur satellites

License:        GPL-3.0-or-later
URL:            https://gr-satellites.readthedocs.io
Source:         https://github.com/daniestevez/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  bzip2
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  fmt-devel
BuildRequires:  gmp-devel
BuildRequires:  gnuradio-devel
BuildRequires:  liborc-devel
BuildRequires:  libsndfile-devel
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  spdlog-devel
# for the test suite
BuildRequires:  python3-construct
BuildRequires:  python3-requests
BuildRequires:  python3-websocket-client

Requires:       gnuradio%{?_isa}
Requires:       python3-construct
Requires:       python3-requests
Requires:       python3-websocket-client

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
Summary:        Development files for gr-satellites
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gnuradio-devel

%description devel
Header files and CMake configuration for building software against
gr-satellites.

%prep
%autosetup

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DENABLE_DOXYGEN=OFF
%cmake_build

%install
%cmake_install
# library modules are not meant to be executed directly
find %{buildroot}%{python3_sitearch}/satellites -name '*.py' ! -perm /111 \
    -exec sed -i '1{/^#!/d}' {} +

%check
# qa_mobitex_fec_block and qa_mobitex_deframer have timing issues and fail
# intermittently on COPR
%ctest -E '^(qa_mobitex_fec_block|qa_mobitex_deframer)$'

%files
%license LICENSE
%doc README.md
%{_bindir}/gr_satellites
%{_bindir}/gr_satellites_ssdv
%{_bindir}/smog_p_spectrum
%{_libdir}/libgnuradio-satellites.so.*
%{python3_sitearch}/satellites/
%{_datadir}/gnuradio/grc/blocks/satellites_*
%{_datadir}/gnuradio/grc/blocks/variable_time_format_parameters.block.yml
%{_mandir}/man1/gr_satellites.1*
%{_mandir}/man1/gr_satellites_ssdv.1*
%{_mandir}/man1/smog_p_spectrum.1*

%files devel
%{_includedir}/satellites/
%{_libdir}/libgnuradio-satellites.so
%{_libdir}/cmake/satellites/

%changelog
%autochangelog
