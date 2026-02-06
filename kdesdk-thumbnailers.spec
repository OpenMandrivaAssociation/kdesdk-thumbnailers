#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Summary:	A preview image generator plugin for gettext translations and templates
Name:		kdesdk-thumbnailers
Version:	25.12.2
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		https://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%if 0%{?git:1}
Source0:	https://invent.kde.org/sdk/kdesdk-thumbnailers/-/archive/%{gitbranch}/kdesdk-thumbnailers-%{gitbranchd}.tar.bz2#/kdesdk-thumbnailers-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kdesdk-thumbnailers-%{version}.tar.xz
%endif
BuildRequires:	gettext-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	pkgconfig(Qt6Widgets)
Requires:	gettext

%rename plasma6-kdesdk-thumbnailers

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildOption:	-DQT_MAJOR_VERSION=6

%description
A preview image generator plugin for gettext translations and templates.

%files
%{_libdir}/qt6/plugins/kf6/thumbcreator/pothumbnail.so
