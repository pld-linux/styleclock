Summary:	Replacement for KDE clock
Summary(pl.UTF-8):   Zamiennik zegara dla KDE
Name:		styleclock
Version:	0.5.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://fred.hexbox.de/styleclock/%{name}-%{version}.tar.gz
# Source0-md5:	8fa2a382239e61d6ad0c2d23a70ef1cd
URL:		http://fred.hexbox.de/styleclock/
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
StyleClock is a incomplete, but better-looking replacement for the
regular KDE clock. It is easily and flexibly themable.

%description -l pl.UTF-8
StyleClock jest niekompletnym, ale ładniej wyglądającym zamiennikiem
zegara KDE. Można do niego szybko i elastycznie stworzyć motyw.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* admin
%configure \
	--disable-rpath \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang fashionclock --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f fashionclock.lang
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/libstyleclock.so
%{_libdir}/libstyleclock.la
%{_datadir}/apps/styleclock
%{_datadir}/apps/kicker/applets/styleclock.desktop
