Name:           itpp
Version:        4.3.1
Release:        %autorelease
Summary:        C++ library for math, signal/speech processing, and communications

License:        GPL-3.0-or-later
URL:            https://itpp.sourceforge.net/
Source0:        https://downloads.sourceforge.net/project/itpp/itpp/%{version}/itpp-%{version}.tar.bz2
# Fixes missing gtest-all.cc error
# source: https://build.opensuse.org/package/view_file/science/libitpp/gtest_support.patch
Patch0:         gtest_support.patch
# Fixes upstream bug in order to pass tests
# PATCH-FIX-UPSTREAM memmove.patch [deb#741814] cristeab@gmail.com -- Corrected multilateration algorithm
# source: https://build.opensuse.org/package/view_file/science/libitpp/itpp-4.3.1_memmove.patch
Patch1:         itpp-4.3.1_memmove.patch
# Fixes itpp CMakeLists.txt for destination of libraries in x86_64 arch
Patch2:         lib64_destination.patch

BuildRequires:  doxygen
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  ghostscript
BuildRequires:  texlive-latex
BuildRequires:  blas-devel
BuildRequires:  lapack-devel
BuildRequires:  fftw-devel
BuildRequires:  gtest-devel

%description
IT++ is a C++ library of mathematical, signal processing and communication
classes and functions. Its main use is in simulation of communication systems
and for performing research in the area of communications. The kernel of the
library consists of generic vector and matrix classes, and a set of
accompanying routines. Such a kernel makes IT++ similar to MATLAB, GNU Octave
or SciPy.

%package devel
Summary:        Header files for the IT++ library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fftw-devel
Requires:       blas-devel
Requires:       lapack-devel

%description devel
This package contains the header files for the IT++ library and a script that
easily provides installed IT++ library prefix and compiler flags.

%package doc
Summary:        HTML documentation for the IT++ library
BuildArch:      noarch

%description doc
This package contains the documentation for the IT++ library as HTML pages.

%prep
%autosetup -p1
# fix wrong permission in the source tarball for lapack.h
chmod 644 itpp/base/algebra/lapack.h

# TODO: Repair Gtest: C++-2017 onward, it++-type in language defined, thus ambiguity.
%build
%cmake \
    -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
    -DITPP_WITH_TESTS=OFF \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_CXX_FLAGS_RELEASE="%{optflags}"
%cmake_build

%install
%cmake_install
# move html docs to temp folder to prevent installation in main package
rm -rf __tmp_doc
mkdir __tmp_doc
mv -t __tmp_doc %{buildroot}%{_docdir}/%{name}/*
# fix wrong permission for itpp-config
chmod 755 %{buildroot}%{_bindir}/%{name}-config

%files
%{_libdir}/lib%{name}.so.*
%{_datadir}/%{name}
%doc AUTHORS ChangeLog NEWS README VERSION
%license COPYING

%files devel
%{_bindir}/%{name}-config
%{_mandir}/man1/%{name}-config*
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so

%files doc
%doc __tmp_doc/*
%license COPYING

%changelog
%autochangelog
