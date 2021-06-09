Summary:	A preview image generator plugin for gettext translations and templates
Name:		kdesdk-thumbnailers
Version:	21.04.2
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	gettext-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	pkgconfig(Qt5Widgets)
Requires:	gettext
Conflicts:	kde-thumbnailer-po < 1:4.11.0
Obsoletes:	kde-thumbnailer-po < 1:4.11.0

%description
A preview image generator plugin for gettext translations and templates.

%files -f pothumbnail.lang
%{_libdir}/qt5/plugins/pothumbnail.so
%{_datadir}/config.kcfg/pocreatorsettings.kcfg
%{_datadir}/kservices5/pothumbnail.desktop

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang pothumbnail
