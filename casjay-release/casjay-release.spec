
Summary: Casjays repos release file
Name: casjay-release
Version: 1.0
Release: 3%{?dist}
License: GPLv2
Group: System Environment/Base
URL: http://casjaysdev.pro/

%if 0%{?rhel}
Source0: casjay.rh.repo
Source1: https://rpm-devel.sourceforge.io/ZREPO/RHEL/$releasever/keys/RPM-GPG-KEY-casjay
%endif
%if 0%{?fedora}
Source0: casjay.fc.repo
Source1: https://rpm-devel.sourceforge.io/ZREPO/Fedora/fc$releasever/keys/RPM-GPG-KEY-casjay
%endif

%description
This package contains yum configuration for the casjaysdev.pro Linux Repository, as well as the public GPG keys used to sign packages.

%prep
%setup -c -T
%{__cp} -a %{SOURCE1} .

# %build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dpm 0644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/casjay.repo
%{__install} -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-casjay

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%pubkey RPM-GPG-KEY-casjay
%dir %{_sysconfdir}/yum.repos.d/
%config %{_sysconfdir}/yum.repos.d/casjay.repo
%dir %{_sysconfdir}/pki/rpm-gpg/
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-casjay

%changelog
* Sat Jun 01 2019 CasjaysDev <rpm-admin@rpm-devel.casjaysdev.pro> - 0.3
- Fixes for fedora

* Thu Feb 22 2018 CasjaysDev <rpm-admin@rpm-devel.casjaysdev.pro> - 0.2
- Fixes for OS Specific rpm repos

* Thu Feb 22 2018 CasjaysDev <rpm-admin@rpm-devel.casjaysdev.pro> - 0.1
- initial release

