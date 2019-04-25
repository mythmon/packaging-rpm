Name: entr
Version: 4.2
Release: 1%{?dist}
Summary: Run arbitrary commands when files change
License: ISC
URL: https://bitbucket.org/eradman/%{name}

Source: %{url}/get/%{name}-%{version}.tar.bz2

BuildRequires: gcc

%global debug_package %{nil}

%description
Run arbitrary commands when files change

%prep
%autosetup -n eradman-entr-6cd0927b54a6

%build
./configure
CPPFLAGS="-g" make

%install
install -D -s -m755 entr -t %{buildroot}%{_bindir}
install -D -m644 entr.1 -t %{buildroot}%{_mandir}/man1/

%check
make test

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
* Wed Apr 24 2019 Michael Cooper <mythmon@gmail.com - 4.2-1
- First entr package
