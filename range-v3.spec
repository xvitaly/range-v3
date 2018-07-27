Name: range-v3
Summary: Experimental range library for C++11/14/17
Version: 0.3.6
Release: 2%{?dist}

License: Boost
URL: https://github.com/ericniebler/%{name}
Source0: %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: noarch

%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup

%build
# Nothing to build. Header-only library.

%install
# Installing headers...
mkdir -p "%{buildroot}%{_includedir}/%{name}"
cp -a include/* "%{buildroot}%{_includedir}/%{name}"

%files devel
%doc README.md CREDITS.md TODO.md
%license LICENSE.txt
%{_includedir}/%{name}

%changelog
* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.6-1
- Updated to version 0.3.6.

* Thu Mar 08 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.5-2
- Fixed bogus changelog entry.

* Thu Mar 08 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.5-1
- Updated to version 0.3.5.

* Fri Dec 01 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.0-1.20171112git0b0dd88
- Initial SPEC release.
