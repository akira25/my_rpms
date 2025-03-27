Name:           ucode-next
Version:        0.0.2025git
Release:        %autorelease
Summary:        JavaScript-like language with optional templating; Main-branch

License:        ISC
URL:            https://ucode.mein.io/
Source0:        https://github.com/jow-/ucode/archive/refs/heads/master.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  json-c-devel
BuildRequires:  texinfo
BuildRequires:  zlib-devel

%description
The ucode language is a small, general-purpose scripting language that
resembles ECMAScript syntax. It can be used as a standalone interpreter or
embedded into host applications. Ucode supports template mode with control flow
and expression logic statements embedded in Jinja-like markup blocks.

Initially intended as a template processor, ucode evolved into a versatile
scripting language for various system scripting tasks. Its design goals include
easy integration with C applications, efficient handling of JSON data and
complex data structures, support for OpenWrt's ubus message bus system, and a
comprehensive set of built-in functions inspired by Perl 5.

%package    -n libucode-next
Summary:    Shared library files for ucode-next

%description -n libucode-next
This package contains the compiled shared libraries for ucode-next.

%package    -n libucode-next-devel
Summary:    Development files for ucode-next

%description -n libucode-next-devel
This package contains libraries and header files for developing applications
that use ucode-next.


%prep
%setup -q -n ucode-master

%build
%cmake -DUBUS_SUPPORT=OFF \
    -DUCI_SUPPORT=OFF \
    -DULOOP_SUPPORT=OFF \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files
%{_bindir}/ucc
%{_bindir}/ucode
%{_bindir}/utpl
# doc docs/README.md README.md
%doc README.md
%license LICENSE

%files  -n libucode-next
%{_prefix}/lib/libucode.so*
%{_prefix}/lib/ucode/*

%files  -n libucode-next-devel
%{_includedir}/ucode/*
#% {_prefix}/lib/debug/usr/bin/ucode-0.0.20231102-1.fc40.x86_64.debug
#% {_prefix}/lib/debug/usr/lib/libucode.so.0-0.0.20231102-1.fc40.x86_64.debug
#% {_prefix}/lib/debug/usr/lib/ucode/debug.so-0.0.20231102-1.fc40.x86_64.debug
#% {_prefix}/lib/debug/usr/lib/ucode/fs.so-0.0.20231102-1.fc40.x86_64.debug
#% {_prefix}/lib/debug/usr/lib/ucode/log.so-0.0.20231102-1.fc40.x86_64.debug
#% {_prefix}/lib/debug/usr/lib/ucode/math.so-0.0.20231102-1.fc40.x86_64.debug
#% {_prefix}/lib/debug/usr/lib/ucode/resolv.so-0.0.20231102-1.fc40.x86_64.debug
#% {_prefix}/lib/debug/usr/lib/ucode/struct.so-0.0.20231102-1.fc40.x86_64.debug

%changelog
%autochangelog
