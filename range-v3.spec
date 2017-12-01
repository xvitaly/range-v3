# Set Git revision of library...
%global commit0 0b0dd886bd05d389649a043bb1d0bcd27c2bf25d
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20171112

Name: range-v3
Summary: Experimental range library for C++11/14/17
Version: 0.3.0
Release: 1.%{date}git%{shortcommit0}%{?dist}

License: Boost
URL: https://github.com/ericniebler/%{name}
Source0: %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
BuildArch: noarch

%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n %{name}-%{commit0} -p1

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
* Fri Dec 01 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.20171112git0b0dd88
- Initial SPEC release. 
