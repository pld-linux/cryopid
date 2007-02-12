Summary:	CryoPID - a process freezer for Linux
Summary(pl.UTF-8):   CryoPID - zamrażacz procesów dla Linuksa
Name:		cryopid
Version:	0.4
Release:	0.1
Epoch:		0
License:	GPL v2
Group:		Applications
Source0:	http://dagobah.ucc.asn.au/wacky/%{name}-%{version}.tar.gz
# Source0-md5:	ef3580a4e1ff8b90c9d1e2a51676e7bc
Patch0:		%{name}-build.patch
URL:		http://cryopid.berlios.de/
BuildRequires:	lzo-static
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CryoPID allows you to capture the state of a running process in Linux
and save it to a file. This file can then be used to resume the
process later on, either after a reboot or even on another machine.

%description -l pl.UTF-8
CryoPID umożliwia na zapamiętanie stanu działającego pod Linuksem
procesu i zapisanie go do pliku. Plik taki może zostać użyty do
wznowienia działania procesu, także po restarcie systemu bądź nawet
na innej maszynie.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install freeze $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO
%attr(755,root,root) %{_bindir}/*
