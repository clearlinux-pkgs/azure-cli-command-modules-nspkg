#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-cli-command-modules-nspkg
Version  : 2.0.3
Release  : 11
URL      : https://files.pythonhosted.org/packages/f9/e4/88d5ac135701d4debaad95f4e421392621152ef2491d3e2cd67ec98353d5/azure-cli-command-modules-nspkg-2.0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/f9/e4/88d5ac135701d4debaad95f4e421392621152ef2491d3e2cd67ec98353d5/azure-cli-command-modules-nspkg-2.0.3.tar.gz
Summary  : Microsoft Azure CLI Command Modules Namespace Package
Group    : Development/Tools
License  : MIT
Requires: azure-cli-command-modules-nspkg-python = %{version}-%{release}
Requires: azure-cli-command-modules-nspkg-python3 = %{version}-%{release}
Requires: azure-cli-nspkg
BuildRequires : azure-cli-nspkg
BuildRequires : buildreq-distutils3

%description
=====================================================
        
        This is the Microsoft Azure CLI command module namespace package.
        
        This package is not intended to be installed directly by the end user.
        
        It provides the necessary files for other packages to extend the azure cli command module namespaces.

%package python
Summary: python components for the azure-cli-command-modules-nspkg package.
Group: Default
Requires: azure-cli-command-modules-nspkg-python3 = %{version}-%{release}

%description python
python components for the azure-cli-command-modules-nspkg package.


%package python3
Summary: python3 components for the azure-cli-command-modules-nspkg package.
Group: Default
Requires: python3-core
Provides: pypi(azure_cli_command_modules_nspkg)
Requires: pypi(azure_cli_nspkg)

%description python3
python3 components for the azure-cli-command-modules-nspkg package.


%prep
%setup -q -n azure-cli-command-modules-nspkg-2.0.3
cd %{_builddir}/azure-cli-command-modules-nspkg-2.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1607992835
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/lib/python3.8/site-packages/azure/cli/command_modules/__init__.py
rm -f %{buildroot}/usr/lib/python3.8/site-packages/azure/cli/command_modules/__pycache__/__init__.cpython-38.pyc

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
