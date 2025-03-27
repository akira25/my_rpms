Name:           ucode
Version:        0.0.20231102
Release:        %autorelease
Summary:        JavaScript-like language with optional templating

License:        ISC
URL:            https://ucode.mein.io/
Source:         https://github.com/jow-/ucode/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  json-c-devel
BuildRequires:  texinfo

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

%package    -n libucode
Summary:    Shared library files for ucode

%description -n libucode
This package contains the compiled shared libraries for ucode.

%package    -n libucode-devel
Summary:    Development files for ucode

%description -n libucode-devel
This package contains libraries and header files for developing applications
that use ucode.


%prep
%autosetup

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

%files  -n libucode
%{_prefix}/lib/libucode.so
%{_prefix}/lib/libucode.so.0
%{_prefix}/lib/ucode/debug.so
%{_prefix}/lib/ucode/fs.so
%{_prefix}/lib/ucode/log.so
%{_prefix}/lib/ucode/math.so
%{_prefix}/lib/ucode/resolv.so
%{_prefix}/lib/ucode/struct.so

%files  -n libucode-devel
%{_includedir}/ucode/chunk.h
%{_includedir}/ucode/compiler.h
%{_includedir}/ucode/lexer.h
%{_includedir}/ucode/lib.h
%{_includedir}/ucode/module.h
%{_includedir}/ucode/platform.h
%{_includedir}/ucode/program.h
%{_includedir}/ucode/source.h
%{_includedir}/ucode/types.h
%{_includedir}/ucode/util.h
%{_includedir}/ucode/vallist.h
%{_includedir}/ucode/vm.h
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
