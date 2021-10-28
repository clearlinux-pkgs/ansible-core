#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ansible-core
Version  : 2.11.6
Release  : 7
URL      : https://github.com/ansible/ansible/archive/v2.11.6/ansible-2.11.6.tar.gz
Source0  : https://github.com/ansible/ansible/archive/v2.11.6/ansible-2.11.6.tar.gz
Summary  : Radically simple IT automation
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0 GPL-3.0 MIT Python-2.0
Requires: ansible-core-bin = %{version}-%{release}
Requires: ansible-core-license = %{version}-%{release}
Requires: ansible-core-python = %{version}-%{release}
Requires: ansible-core-python3 = %{version}-%{release}
Requires: Jinja2
Requires: PyYAML
Requires: cryptography
Requires: packaging
Requires: resolvelib
BuildRequires : Jinja2
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-golang
BuildRequires : cryptography
BuildRequires : packaging
BuildRequires : resolvelib

%description
|PyPI version| |Docs badge| |Chat badge| |Build Status| |Code Of Conduct| |Mailing Lists| |License| |CII Best Practices|

%package bin
Summary: bin components for the ansible-core package.
Group: Binaries
Requires: ansible-core-license = %{version}-%{release}

%description bin
bin components for the ansible-core package.


%package license
Summary: license components for the ansible-core package.
Group: Default

%description license
license components for the ansible-core package.


%package python
Summary: python components for the ansible-core package.
Group: Default
Requires: ansible-core-python3 = %{version}-%{release}

%description python
python components for the ansible-core package.


%package python3
Summary: python3 components for the ansible-core package.
Group: Default
Requires: python3-core
Provides: pypi(ansible_core)
Requires: pypi(cryptography)
Requires: pypi(jinja2)
Requires: pypi(packaging)
Requires: pypi(pyyaml)
Requires: pypi(resolvelib)

%description python3
python3 components for the ansible-core package.


%prep
%setup -q -n ansible-2.11.6
cd %{_builddir}/ansible-2.11.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634075149
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ansible-core
cp %{_builddir}/ansible-2.11.6/COPYING %{buildroot}/usr/share/package-licenses/ansible-core/338650eb7a42dd9bc1f1c6961420f2633b24932d
cp %{_builddir}/ansible-2.11.6/licenses/Apache-License.txt %{buildroot}/usr/share/package-licenses/ansible-core/c700a8b9312d24bdc57570f7d6a131cf63d89016
cp %{_builddir}/ansible-2.11.6/licenses/MIT-license.txt %{buildroot}/usr/share/package-licenses/ansible-core/df180fcf964224ba9180a646ca107bfe65595f23
cp %{_builddir}/ansible-2.11.6/licenses/PSF-license.txt %{buildroot}/usr/share/package-licenses/ansible-core/7b14725671bae6dc04be2b87de58131f0614dfad
cp %{_builddir}/ansible-2.11.6/packaging/debian/copyright %{buildroot}/usr/share/package-licenses/ansible-core/b7f3dc6d692392795202ab560c7583e986d8352b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ansible
/usr/bin/ansible-config
/usr/bin/ansible-connection
/usr/bin/ansible-console
/usr/bin/ansible-doc
/usr/bin/ansible-galaxy
/usr/bin/ansible-inventory
/usr/bin/ansible-playbook
/usr/bin/ansible-pull
/usr/bin/ansible-test
/usr/bin/ansible-vault

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ansible-core/338650eb7a42dd9bc1f1c6961420f2633b24932d
/usr/share/package-licenses/ansible-core/7b14725671bae6dc04be2b87de58131f0614dfad
/usr/share/package-licenses/ansible-core/b7f3dc6d692392795202ab560c7583e986d8352b
/usr/share/package-licenses/ansible-core/c700a8b9312d24bdc57570f7d6a131cf63d89016
/usr/share/package-licenses/ansible-core/df180fcf964224ba9180a646ca107bfe65595f23

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
