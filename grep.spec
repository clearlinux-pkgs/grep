#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7FD9FCCB000BEEEE (meyering@fb.com)
#
Name     : grep
Version  : 3.6
Release  : 42
URL      : https://mirrors.kernel.org/gnu/grep/grep-3.6.tar.xz
Source0  : https://mirrors.kernel.org/gnu/grep/grep-3.6.tar.xz
Source1  : https://mirrors.kernel.org/gnu/grep/grep-3.6.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: grep-bin = %{version}-%{release}
Requires: grep-info = %{version}-%{release}
Requires: grep-license = %{version}-%{release}
Requires: grep-locales = %{version}-%{release}
Requires: grep-man = %{version}-%{release}
BuildRequires : glibc-locale
BuildRequires : pcre-dev

%description
This is GNU grep, the "fastest grep in the west" (we hope).  All
bugs reported in previous releases have been fixed.  Many exciting new
bugs have probably been introduced in this revision.

%package bin
Summary: bin components for the grep package.
Group: Binaries
Requires: grep-license = %{version}-%{release}

%description bin
bin components for the grep package.


%package info
Summary: info components for the grep package.
Group: Default

%description info
info components for the grep package.


%package license
Summary: license components for the grep package.
Group: Default

%description license
license components for the grep package.


%package locales
Summary: locales components for the grep package.
Group: Default

%description locales
locales components for the grep package.


%package man
Summary: man components for the grep package.
Group: Default

%description man
man components for the grep package.


%prep
%setup -q -n grep-3.6
cd %{_builddir}/grep-3.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604945770
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --with-packager="Clear Linux"
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1604945770
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/grep
cp %{_builddir}/grep-3.6/COPYING %{buildroot}/usr/share/package-licenses/grep/31a3d460bb3c7d98845187c716a30db81c44b615
%make_install
%find_lang grep
## install_append content
# Mark patched in test-suite executable
chmod +x ./tests/kwset-abuse
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/egrep
/usr/bin/fgrep
/usr/bin/grep

%files info
%defattr(0644,root,root,0755)
/usr/share/info/grep.info

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/grep/31a3d460bb3c7d98845187c716a30db81c44b615

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/egrep.1
/usr/share/man/man1/fgrep.1
/usr/share/man/man1/grep.1

%files locales -f grep.lang
%defattr(-,root,root,-)

