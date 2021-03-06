Summary:	The source repository for the TPM (Trusted Platform Module) 2 tools
Name:		tpm2-tools
Version:	3.1.3
Release:	2%{?dist}
License:	BSD 2-Clause
URL:		https://github.com/tpm2-software/tpm2-tools
Group:		System Environment/Security
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	%{name}-%{version}.tar.gz
%define sha1 tpm2=126f83d927a13aa5999769e33339136b2c7c5008
BuildRequires:	openssl-devel curl-devel tpm2-tss-devel
Requires:	openssl curl tpm2-tss
%if %{with_check}
BuildRequires:  ibmtpm
BuildRequires:  systemd
%endif
%description
The source repository for the TPM (Trusted Platform Module) 2 tools

%prep
%setup -q
%build
%configure \
    --disable-static

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%check
if [ ! -f /dev/tpm0 ];then
   systemctl start ibmtpm_server.service
   export TPM2TOOLS_TCTI=mssim:host=localhost,port=2321
   tpm2_startup -c
   tpm2_pcrlist
fi
make %{?_smp_mflags} check

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1

%changelog
*   Wed Jun 10 2020 Michelle Wang <michellew@vmware.com> 3.1.3-2
-   update make check with ibmtpm
*   Thu Feb 21 2019 Alexey Makhalov <amakhalov@vmware.com> 3.1.3-1
-   Initial build. First version
