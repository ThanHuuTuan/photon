%{!?python3_sitelib: %define python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}
%{!?python3_version: %define python3_version %(python3 -c "import sys; sys.stdout.write(sys.version[:3])")}

Summary:        Extensions to the standard Python datetime module
Name:           python3-dateutil
Version:        2.7.3
Release:        2%{?dist}
License:        Apache Software License, BSD License (Dual License)
Group:          Development/Languages/Python
Vendor:         VMware, Inc.
Distribution:   Photon
Url:            https://pypi.python.org/pypi/python-dateutil
Source0:        https://pypi.python.org/packages/54/bb/f1db86504f7a49e1d9b9301531181b00a1c7325dc85a29160ee3eaa73a54/python-dateutil-%{version}.tar.gz
%define         sha1 python-dateutil=b1aeb913996fc6660ea42a7b31b1331d41a8a13c
BuildRequires:  python3-devel
BuildRequires:  python3-libs
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-xml
Requires:       python3
Requires:       python3-libs
Requires:       python3-six
BuildArch:      noarch

%description
The dateutil module provides powerful extensions to the datetime module available in the Python standard library.


%prep
%setup -q -n python-dateutil-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
python3 setup.py test

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
*   Fri Jun 19 2020 Tapas Kundu <tkundu@vmware.com> 2.7.3-2
-   Mass removal python2
*   Fri Sep 14 2018 Tapas Kundu <tkundu@vmware.com> 2.7.3-1
-   Updated to release 2.7.3
*   Sun Jan 07 2018 Kumar Kaushik <kaushikk@vmware.com> 2.6.1-1
-   Initial packaging for photon.

