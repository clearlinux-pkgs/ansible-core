#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ansible-core
Version  : 2.13.5
Release  : 30
URL      : https://github.com/ansible/ansible/archive/v2.13.5/ansible-2.13.5.tar.gz
Source0  : https://github.com/ansible/ansible/archive/v2.13.5/ansible-2.13.5.tar.gz
Summary  : Radically simple IT automation
Group    : Development/Tools
License  : Apache-2.0 GPL-3.0 MIT Python-2.0
Requires: ansible-core-bin = %{version}-%{release}
Requires: ansible-core-license = %{version}-%{release}
Requires: ansible-core-python = %{version}-%{release}
Requires: ansible-core-python3 = %{version}-%{release}
Requires: sshpass
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cryptography)
BuildRequires : pypi(jinja2)
BuildRequires : pypi(packaging)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(resolvelib)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

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
%setup -q -n ansible-2.13.5
cd %{_builddir}/ansible-2.13.5
pushd ..
cp -a ansible-2.13.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1665518032
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . resolvelib
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . resolvelib
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ansible-core
cp %{_builddir}/ansible-%{version}/COPYING %{buildroot}/usr/share/package-licenses/ansible-core/338650eb7a42dd9bc1f1c6961420f2633b24932d || :
cp %{_builddir}/ansible-%{version}/licenses/Apache-License.txt %{buildroot}/usr/share/package-licenses/ansible-core/c700a8b9312d24bdc57570f7d6a131cf63d89016 || :
cp %{_builddir}/ansible-%{version}/licenses/MIT-license.txt %{buildroot}/usr/share/package-licenses/ansible-core/df180fcf964224ba9180a646ca107bfe65595f23 || :
cp %{_builddir}/ansible-%{version}/licenses/PSF-license.txt %{buildroot}/usr/share/package-licenses/ansible-core/e9665a5e46702a4080c47049e29edf05eb70bfd6 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} resolvelib
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/share/package-licenses/ansible-core/c700a8b9312d24bdc57570f7d6a131cf63d89016
/usr/share/package-licenses/ansible-core/df180fcf964224ba9180a646ca107bfe65595f23
/usr/share/package-licenses/ansible-core/e9665a5e46702a4080c47049e29edf05eb70bfd6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
