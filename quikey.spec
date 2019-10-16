%global debug_package %{nil}

Name:		quikey
Version:	0.1.0
Release:	0%{?dist}
Summary:	A keyboard macro tool.


License:	MIT
URL:		https://github.com/bostrt/quikey
Source0:	https://github.com/bostrt/quikey/archive/%{version}.tar.gz

BuildRequires:	python3-devel
Requires:       python3-click
Requires:       python3-daemon
Requires:       python3-inotify_simple
Requires:       python3-tinydb
Requires:       python3-terminaltables
Requires:       python3-humanize
Requires:       python3-pyxdg
Requires:       python3-pynput
Requires:       python3-colored

%description
A keyboard macro tool.

%prep
%setup -q -n quikey-%{version}

%build
%py3_build

%install
%py3_install

%files
%doc README.md
%license LICENSE
%{python3_sitelib}/quikey
%{python3_sitelib}/quikey-%{version}-py?.?.egg-info

%changelog

