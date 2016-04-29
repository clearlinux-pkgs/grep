#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : grep
Version  : 2.25
Release  : 20
URL      : http://mirrors.kernel.org/gnu/grep/grep-2.25.tar.xz
Source0  : http://mirrors.kernel.org/gnu/grep/grep-2.25.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-3.0 GPL-3.0+
Requires: grep-bin
Requires: grep-doc
Requires: grep-locales
BuildRequires : pcre-dev

%description
This is GNU grep, the "fastest grep in the west" (we hope).  All
bugs reported in previous releases have been fixed.  Many exciting new
bugs have probably been introduced in this revision.

%package bin
Summary: bin components for the grep package.
Group: Binaries

%description bin
bin components for the grep package.


%package doc
Summary: doc components for the grep package.
Group: Documentation

%description doc
doc components for the grep package.


%package locales
Summary: locales components for the grep package.
Group: Default

%description locales
locales components for the grep package.


%prep
%setup -q -n grep-2.25

%build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -falign-functions=32 -fno-semantic-interposition -flto -O3 "
export FCFLAGS="$CFLAGS -falign-functions=32 -fno-semantic-interposition -flto -O3 "
export FFLAGS="$CFLAGS -falign-functions=32 -fno-semantic-interposition -flto -O3 "
export CXXFLAGS="$CXXFLAGS -falign-functions=32 -fno-semantic-interposition -flto -O3 "
%configure --disable-static --with-packager="Clear Linux"
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
rm -rf %{buildroot}
%make_install
%find_lang grep
## make_install_append content
chmod +x ./tests/kwset-abuse
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/egrep
/usr/bin/fgrep
/usr/bin/grep

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*

%files locales -f grep.lang 
%defattr(-,root,root,-)

