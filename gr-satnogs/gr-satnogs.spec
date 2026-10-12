Name:           gr-satnogs
Version:        3.1.0.1
Release:        %autorelease
Summary:        GNU Radio OOT module for decoding signals of scientific and academic satellites

License:        GPL-3.0-or-later
URL:            https://gitlab.com/librespacefoundation/satnogs/gr-satnogs
Source:         %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  cmake
# CRCpp is a git submodule upstream, use the Fedora package instead
BuildRequires:  crcpp-devel
BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  fmt-devel
BuildRequires:  gmp-devel
BuildRequires:  gnuradio-devel
BuildRequires:  gsl-devel
BuildRequires:  hamlib-c++-devel
BuildRequires:  hamlib-devel
BuildRequires:  itpp-devel
BuildRequires:  json-devel
BuildRequires:  libogg-devel
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  png++-devel
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  spdlog-devel
BuildRequires:  volk-devel

Requires:       gnuradio%{?_isa}
Requires:       python3-hamlib
Requires:       python3-numpy

%description
gr-satnogs is an out-of-tree GNU Radio module that provides all the necessary
tools for decoding signals from various scientific and academic satellites. It
also provides blocks for debugging and experimenting with known satellite
telecommunication schemes. It is the signal processing core of the SatNOGS
ground station network.

%package devel
Summary:        Development files for gr-satnogs
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gnuradio-devel
Requires:       crcpp-devel

%description devel
Header files and CMake configuration for building software against gr-satnogs.

%prep
%autosetup -n %{name}-v%{version}
# CRC.h comes from crcpp-devel, don't install the (missing) submodule copy
sed -i '/CRCpp\/inc\/CRC.h/d' include/gnuradio/satnogs/CMakeLists.txt

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DENABLE_DOXYGEN=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libgnuradio-satnogs*.so.*
%{python3_sitearch}/gnuradio/satnogs/
%{_datadir}/gnuradio/grc/blocks/satnogs*

%files devel
%{_includedir}/gnuradio/satnogs/
%{_libdir}/libgnuradio-satnogs*.so
%{_libdir}/cmake/gnuradio-satnogs/

%changelog
%autochangelog
