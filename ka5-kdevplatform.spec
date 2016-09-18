#
# TODO: Add 'Requires:' for grantlee version with which it is built
#

%define		_state		stable
%define		orgname		kdevplatform
%define		_kdevelopver	5.0.1
%define		qtver		5.5.1

Summary:	KDevelop Development Platform
Summary(pl.UTF-8):	KDevelop Development Platform
Name:		ka5-kdevplatform
Version:	5.0.1
Release:	0.1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://download.kde.org/stable/kdevelop/%{_kdevelopver}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	54b7f9dd20856edbd3dc91d84c07cd03
URL:		http://www.kdevelop.org/
BuildRequires:	Qt5WebKit-devel
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	kf5-extra-cmake-modules
BuildRequires:	kf5-karchive-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kguiaddons-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kitemmodels-devel
BuildRequires:	kf5-kitemviews-devel
BuildRequires:	kf5-kjobwidgets-devel
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-knotifyconfig-devel
BuildRequires:	kf5-kparts-devel
BuildRequires:	kf5-kservice-devel
BuildRequires:	kf5-sonnet-devel
BuildRequires:	kf5-ktexteditor-devel
BuildRequires:	kf5-threadweaver-devel
BuildRequires:	kf5-kdeclarative-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kpackage-devel
BuildRequires:	kf5-kauth-devel
BuildRequires:	kf5-kcodecs-devel
BuildRequires:	kf5-kbookmarks-devel
BuildRequires:	kf5-kcompletion-devel
BuildRequires:	kf5-solid-devel
BuildRequires:	kf5-attica-devel
BuildRequires:	kf5-ktextwidgets-devel
BuildRequires:	kf5-libkomparediff2-devel
BuildRequires:	kf5-kwindowsystem-devel



BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.8.9
BuildRequires:	gettext-tools
BuildRequires:	grantlee-qt5-devel
BuildRequires:	libstdc++-devel
#BuildRequires:	qjson-devel
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	subversion-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXdmcp-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	zlib-devel
Requires:	subversion-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kdevplatform

%description -l pl.UTF-8
kdevplatform

%package devel
Summary:	kdevplatform - header files and development documentation
Summary(pl.UTF-8):	kdevplatform - pliki nagłówkowe i dokumentacja
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains header files and development documentation for
kdevplatform.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących kdevplatform.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
        -DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdev_dbus_socket_transformer
%attr(755,root,root) %{_bindir}/kdev_format_source
%attr(755,root,root) %{_bindir}/kdevplatform_shell_environment.sh
%attr(755,root,root) %{_libdir}/libKDevPlatformDebugger.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libKDevPlatformDebugger.so.??
%attr(755,root,root) %{_libdir}/libKDevPlatformDocumentation.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libKDevPlatformDocumentation.so.??
%attr(755,root,root) %{_libdir}/libKDevPlatformInterfaces.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libKDevPlatformInterfaces.so.??
%attr(755,root,root) %{_libdir}/libKDevPlatformLanguage.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libKDevPlatformLanguage.so.??
%attr(755,root,root) %{_libdir}/libKDevPlatformOutputView.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libKDevPlatformOutputView.so.??
%attr(755,root,root) %{_libdir}/libKDevPlatformProject.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libKDevPlatformProject.so.??
%attr(755,root,root) %{_libdir}/libKDevPlatformSerialization.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libKDevPlatformSerialization.so.??
%attr(755,root,root) %{_libdir}/libKDevPlatformShell.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libKDevPlatformShell.so.??
%attr(755,root,root) %{_libdir}/libKDevPlatformSublime.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libKDevPlatformSublime.so.??
%attr(755,root,root) %{_libdir}/libKDevPlatformTests.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libKDevPlatformTests.so.??
%attr(755,root,root) %{_libdir}/libKDevPlatformUtil.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libKDevPlatformUtil.so.??
%attr(755,root,root) %{_libdir}/libKDevPlatformVcs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libKDevPlatformVcs.so.??
%dir %{_libdir}/qt5/plugins/grantlee
%dir %{_libdir}/qt5/plugins/grantlee/*
%attr(755,root,root) %{_libdir}/qt5/plugins/grantlee/*/kdev_filters.so
%dir %{_libdir}/qt5/plugins/kdevplatform
%dir %{_libdir}/qt5/plugins/kdevplatform/*
%attr(755,root,root) %{_libdir}/qt5/plugins/kdevplatform/*/kdev*.so
%dir %{_libdir}/qt5/qml/org/kde/kdevplatform
%{_libdir}/qt5/qml/org/kde/kdevplatform/qmldir
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/kdevplatform/libkdevelopdashboarddeclarativeplugin.so
%{_datadir}/kdevcodegen
%{_datadir}/kdevcodeutils
%{_datadir}/kservicetypes5/kdevelopplugin.desktop
%{_iconsdir}/hicolor/*/actions/*.png
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg

%files devel
%defattr(644,root,root,755)
%{_includedir}/kdevplatform
%{_libdir}/libKDevPlatformDebugger.so
%{_libdir}/libKDevPlatformDocumentation.so
%{_libdir}/libKDevPlatformInterfaces.so
%{_libdir}/libKDevPlatformLanguage.so
%{_libdir}/libKDevPlatformOutputView.so
%{_libdir}/libKDevPlatformProject.so
%{_libdir}/libKDevPlatformSerialization.so
%{_libdir}/libKDevPlatformShell.so
%{_libdir}/libKDevPlatformSublime.so
%{_libdir}/libKDevPlatformTests.so
%{_libdir}/libKDevPlatformUtil.so
%{_libdir}/libKDevPlatformVcs.so
%dir %{_libdir}/cmake/KDevPlatform
%{_libdir}/cmake/KDevPlatform/KDevPlatformConfig.cmake
%{_libdir}/cmake/KDevPlatform/KDevPlatformConfigVersion.cmake
%{_libdir}/cmake/KDevPlatform/KDevPlatformMacros.cmake
%{_libdir}/cmake/KDevPlatform/KDevPlatformTargets.cmake
%{_libdir}/cmake/KDevPlatform/KDevPlatformTargets-pld.cmake
