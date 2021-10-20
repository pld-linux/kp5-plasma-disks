%define		kdeplasmaver	5.23.1
%define		qtver		5.9.0
%define		kpname		plasma-disks
%define		kf5ver		5.39.0

Summary:	plasma-disks
Name:		kp5-%{kpname}
Version:	5.23.1
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	42ac4a668869c8729372a8c4bc6eae23
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= 5.15.0
BuildRequires:	Qt5Gui-devel >= 5.15.0
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.82
BuildRequires:	kf5-kauth-devel >= 5.82
BuildRequires:	kf5-kcoreaddons-devel >= 5.85.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.82
BuildRequires:	kf5-kdeclarative-devel >= 5.82
BuildRequires:	kf5-ki18n-devel >= 5.82
BuildRequires:	kf5-kio-devel >= 5.82
BuildRequires:	kf5-knotifications-devel >= 5.82
BuildRequires:	kf5-kservice-devel >= 5.85.0
BuildRequires:	kf5-solid-devel >= 5.85.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
Requires:	python3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
plasma-disks.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%{_libdir}/qt5/plugins/kcms/smart.so
%{_libdir}/qt5/plugins/kf5/kded/smart.so
%attr(755,root,root) %{_prefix}/libexec/kauth/kded-smart-helper
%{_datadir}/dbus-1/system-services/org.kde.kded.smart.service
%{_datadir}/dbus-1/system.d/org.kde.kded.smart.conf
%{_datadir}/knotifications5/org.kde.kded.smart.notifyrc
%{_datadir}/kpackage/kcms/plasma_disks
%{_datadir}/kservices5/smart.desktop
%{_datadir}/metainfo/org.kde.plasma.disks.metainfo.xml
%{_datadir}/polkit-1/actions/org.kde.kded.smart.policy
