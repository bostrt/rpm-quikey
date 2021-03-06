%global debug_package %{nil}

Name:		quikey
Version:	0.1.5
Release:	1
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
Requires:       python3-filelock

%description
A keyboard macro tool.

%prep
%setup -q -n quikey-%{version}
rm -rf test/

%build
%py3_build

%install
%py3_install

%files
%doc README.md
%license LICENSE
%{python3_sitelib}/quikey
%{python3_sitelib}/quikey-%{version}-py?.?.egg-info
%{_bindir}/qk
%{_bindir}/quikey-daemon

%changelog
* Sun Nov 29 2020 Robert Bost <rbost@redhat.com> 0.1.5-1
- Bug fixes 

* Sun Nov 22 2020 Robert Bost <rbost@redhat.com> 0.1.4-1
- Release of 0.1.4

* Sun Nov 22 2020 Robert Bost <rbost@redhat.com> 0.1.3-1
- Release of 0.1.3

* Wed Oct 16 2019 Robert Bost <bostrt@gmail.com> 0.1.1-0
- Marking release of quikey 0.1.1

* Wed Oct 16 2019 Robert Bost <bostrt@gmail.com> 0.1.0-3
- xdg->pyxdg (bostrt@gmail.com)

* Tue Oct 15 2019 Robert Bost <bostrt@gmail.com> 0.1.0-2
- Move from pyxdg -> xdg dependency (bostrt@gmail.com)

* Tue Oct 15 2019 Robert Bost <bostrt@gmail.com> 0.1.0-1
- Add executables to files listing (bostrt@gmail.com)


