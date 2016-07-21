%global srcname keystone-voms

Name:           python-%{srcname}
Version:        8.0.3
Release:        1%{?dist}
Summary:        Keystone VOMS module for Keystone

#Group:
License:        ASL 2.0
URL:            http://ifca.github.io/keystone-voms
Source:         python-%{srcname}_%{version}.orig.tar.gz

BuildArch:      noarch
BuildRequires:  python2
BuildRequires:  python2-rpm-macros
BuildRequires:  python-rpm-macros
BuildRequires:  python-pbr
BuildRequires:  python-setuptools

Requires:       openstack-keystone >= 8.0.0
Requires:       pyOpenSSL >= 0.15
Requires:       python-cffi
Requires:       python-oslo-config >= 2.3.0
Requires:       python-oslo-log >= 1.8.0
Requires:       python-oslo-serialization >= 1.4.0

%description
Keystone-VOMS implements VOMS-based authentication for the
OpenStack identity service (Keystone) for V2 API.

This package contains the VOMS external authentication module.

%prep
%autosetup -n python-%{srcname}-%{version}

%build
%py2_build

%install
%py2_install

%files
%license LICENSE
%doc README.md
%{python2_sitelib}/*

%changelog
* Fri Jul 22 2016 Alvaro Lopez <aloga@ifca.unican.es> 8.0.3
- Update to Keystone-VOMS 8.0.3
* Thu Mar 10 2016 Alvaro Lopez <aloga@ifca.unican.es> 8.0.2
- Update to Keystone-VOMS 8.0.2
* Tue Mar 08 2016 Enol Fernandez <enol.fernandez@egi.eu> 8.0.0
- Initial RPM version
