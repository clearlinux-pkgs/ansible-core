#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v16
# autospec commit: b858a2a
#
Name     : ansible-core
Version  : 2.17.2
Release  : 55
URL      : https://github.com/ansible/ansible/archive/v2.17.2/ansible-2.17.2.tar.gz
Source0  : https://github.com/ansible/ansible/archive/v2.17.2/ansible-2.17.2.tar.gz
Summary  : Radically simple IT automation
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause GPL-3.0 MIT Python-2.0
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![PyPI version](https://img.shields.io/pypi/v/ansible-core.svg)](https://pypi.org/project/ansible-core)
[![Docs badge](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://docs.ansible.com/ansible/latest/)
[![Chat badge](https://img.shields.io/badge/chat-IRC-brightgreen.svg)](https://docs.ansible.com/ansible/latest/community/communication.html)
[![Build Status](https://dev.azure.com/ansible/ansible/_apis/build/status/CI?branchName=devel)](https://dev.azure.com/ansible/ansible/_build/latest?definitionId=20&branchName=devel)
[![Ansible Code of Conduct](https://img.shields.io/badge/code%20of%20conduct-Ansible-silver.svg)](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)
[![Ansible mailing lists](https://img.shields.io/badge/mailing%20lists-Ansible-orange.svg)](https://docs.ansible.com/ansible/latest/community/communication.html#mailing-list-information)
[![Repository License](https://img.shields.io/badge/license-GPL%20v3.0-brightgreen.svg)](COPYING)
[![Ansible CII Best Practices certification](https://bestpractices.coreinfrastructure.org/projects/2372/badge)](https://bestpractices.coreinfrastructure.org/projects/2372)

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
%setup -q -n ansible-2.17.2
cd %{_builddir}/ansible-2.17.2
pushd ..
cp -a ansible-2.17.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1721139003
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . resolvelib
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
pypi-dep-fix.py . resolvelib
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ansible-core
cp %{_builddir}/ansible-%{version}/COPYING %{buildroot}/usr/share/package-licenses/ansible-core/31a3d460bb3c7d98845187c716a30db81c44b615 || :
cp %{_builddir}/ansible-%{version}/licenses/Apache-License.txt %{buildroot}/usr/share/package-licenses/ansible-core/c700a8b9312d24bdc57570f7d6a131cf63d89016 || :
cp %{_builddir}/ansible-%{version}/licenses/Apache-License.txt %{buildroot}/usr/share/package-licenses/ansible-core/c700a8b9312d24bdc57570f7d6a131cf63d89016 || :
cp %{_builddir}/ansible-%{version}/licenses/MIT-license.txt %{buildroot}/usr/share/package-licenses/ansible-core/df180fcf964224ba9180a646ca107bfe65595f23 || :
cp %{_builddir}/ansible-%{version}/licenses/MIT-license.txt %{buildroot}/usr/share/package-licenses/ansible-core/df180fcf964224ba9180a646ca107bfe65595f23 || :
cp %{_builddir}/ansible-%{version}/licenses/PSF-license.txt %{buildroot}/usr/share/package-licenses/ansible-core/e9665a5e46702a4080c47049e29edf05eb70bfd6 || :
cp %{_builddir}/ansible-%{version}/licenses/PSF-license.txt %{buildroot}/usr/share/package-licenses/ansible-core/e9665a5e46702a4080c47049e29edf05eb70bfd6 || :
cp %{_builddir}/ansible-%{version}/licenses/simplified_bsd.txt %{buildroot}/usr/share/package-licenses/ansible-core/964a86ea34677b9cf55c3c92f65bf279efbb12c6 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
pypi-dep-fix.py %{buildroot} resolvelib
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
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
/usr/share/package-licenses/ansible-core/31a3d460bb3c7d98845187c716a30db81c44b615
/usr/share/package-licenses/ansible-core/964a86ea34677b9cf55c3c92f65bf279efbb12c6
/usr/share/package-licenses/ansible-core/c700a8b9312d24bdc57570f7d6a131cf63d89016
/usr/share/package-licenses/ansible-core/df180fcf964224ba9180a646ca107bfe65595f23
/usr/share/package-licenses/ansible-core/e9665a5e46702a4080c47049e29edf05eb70bfd6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
