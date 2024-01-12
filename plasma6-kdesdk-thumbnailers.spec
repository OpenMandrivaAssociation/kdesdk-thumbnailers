Summary:	A preview image generator plugin for gettext translations and templates
Name:		plasma6-kdesdk-thumbnailers
Version:	24.01.90
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kdesdk-thumbnailers-%{version}.tar.xz
BuildRequires:	gettext-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	pkgconfig(Qt6Widgets)
Requires:	gettext

%description
A preview image generator plugin for gettext translations and templates.

%files -f pothumbnail.lang
%{_datadir}/config.kcfg/pocreatorsettings.kcfg
%{_libdir}/qt6/plugins/kf6/thumbcreator/pothumbnail.so

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n kdesdk-thumbnailers-%{?git:master}%{!?git:%{version}}
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang pothumbnail
