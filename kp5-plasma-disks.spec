#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.93.0
%define		qtver		5.15.2
%define		kpname		plasma-disks
%define		kf6ver		5.39.0

Summary:	plasma-disks
Name:		kp5-%{kpname}
Version:	5.93.0
Release:	0.1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/unstable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	2d4e463b22254852d47728127ce27bc3
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= 5.15.0
BuildRequires:	Qt6Gui-devel >= 5.15.0
BuildRequires:	cmake >= 3.16.0
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= 5.82
BuildRequires:	kf6-kauth-devel >= 5.82
BuildRequires:	kf6-kcoreaddons-devel >= 5.85.0
BuildRequires:	kf6-kdbusaddons-devel >= 5.82
BuildRequires:	kf6-kdeclarative-devel >= 5.82
BuildRequires:	kf6-ki18n-devel >= 5.82
BuildRequires:	kf6-kio-devel >= 5.82
BuildRequires:	kf6-knotifications-devel >= 5.82
BuildRequires:	kf6-kservice-devel >= 5.85.0
BuildRequires:	kf6-solid-devel >= 5.85.0
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
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/smart.so
%{_datadir}/dbus-1/system-services/org.kde.kded.smart.service
%{_datadir}/dbus-1/system.d/org.kde.kded.smart.conf
%{_datadir}/metainfo/org.kde.plasma.disks.metainfo.xml
%{_datadir}/polkit-1/actions/org.kde.kded.smart.policy
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/kinfocenter/kcm_disks.so
%attr(755,root,root) %{_prefix}/libexec/kf6/kauth/kded-smart-helper
%{_desktopdir}/kcm_disks.desktop
%{_datadir}/knotifications6/org.kde.kded.smart.notifyrc
