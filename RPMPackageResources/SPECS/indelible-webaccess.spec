Name:	indelible-webaccess	
Version:	@REVISION@
Release:	@BUILD@
Summary:	Indelible Web Access
Group:		System Environment/Daemons
License:	Apache
URL:		http://www.indeliblefs.com
Source:		%{name}-%{version}.tar.gz

BuildRequires:	java-1.6.0-openjdk, ant >= 1.8, avahi-devel
Requires:	avahi, avahi-tools, avahi-libs, java-1.6.0-openjdk

%description
Indelible Web Access provides a browsable GUI interface to Indelible FS
%prep
%setup

%build
cd %{_builddir}/%{name}-%{version}/IndelibleWebAccess-Linux
ant buildDist

%install
echo %{buildroot}
cd %{_builddir}/%{name}-%{version}/IndelibleWebAccess-Linux
ant -DrpmInstallDir='%{buildroot}' install-rh

%files
/etc/init/
/usr/bin/
/usr/lib/igeek/indelible-webaccess/
/usr/share/igeek/indelible-webaccess/

%changelog

%clean
echo "Not cleaning"
