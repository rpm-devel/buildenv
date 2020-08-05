Name:		sickchill
Version:	e094759
Release:	1%{?dist}
Summary:	Automatic Video Library Manager for TV Shows

Group:		Web
License:	GPLv3
URL:		https://github.com/SickChill/SickChill
Source0:	https://github.com/SickChill/SickChill
Source1:    sickchill.service
Source2:    sickchill-bt.service
Source3:    transmission-settings.json
BuildRequires:	transmission-daemon python3-virtualenv
Requires:

%description


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%doc



%changelog

