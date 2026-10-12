Name:           png++
Version:        0.2.9
Release:        %autorelease
Summary:        Simple yet powerful C++ interface to libpng
License:        BSD-3-Clause
URL:            https://www.nongnu.org/pngpp/
Source0:        https://download.savannah.nongnu.org/releases/pngpp/png++-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  doxygen
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel

%description
PNG++ aims to provide a simple yet powerful C++ interface to libpng, the PNG
reference implementation library. It makes reading and writing PNG images in
C++ easy and intuitive, avoiding the complexity of directly using libpng.

%package devel
Summary:        Development files for PNG++, a header-only C++ wrapper for libpng
Requires:       libpng-devel

%description devel
This package provides the C++ header files for PNG++, which wraps libpng to
offer a high-level interface for handling PNG files in C++. Being header-only,
it does not require linking against a separate library.

%package doc
Summary:        Documentation for the PNG++ library

%description doc
This package contains API documentation for the PNG++ library, generated using Doxygen.

%prep
%autosetup

%build
%make_build
make docs

%install
make install PREFIX=%{buildroot}%{_prefix}

%files devel
%license COPYING
%doc README
%{_includedir}/%{name}/

%files doc
%license COPYING
%doc %{_docdir}/%{name}-%{version}/
%{_docdir}/png++

%changelog
%autochangelog
