Summary:	Replacement for KDE clock
Summary(pl):	Zamiennik zegara dla KDE
Name:		styleclock
Version:	0.3.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://fred.hexbox.de/styleclock/%{name}-%{version}.tar.gz
# Source0-md5:	8459613854cefdb3cf962b88cd716f53
URL:		http://fred.hexbox.de/styleclock/
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
StyleClock is a incomplete, but better-looking replacement for the
regular KDE clock. It is easily and flexibly themable.

%description -l pl
StyleClock jest niekompletnym, ale ³adniej wygl±daj±cym zamiennikiem
zegara KDE. Mo¿na do niego szybko i elastycznie stworzyæ motyw.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%{_datadir}/*
%attr(755,root,root) %{_libdir}/libstyleclock.la
%attr(755,root,root) %{_libdir}/libstyleclock.so
