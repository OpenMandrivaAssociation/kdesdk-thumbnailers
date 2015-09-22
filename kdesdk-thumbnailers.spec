Summary:	A preview image generator plugin for gettext translations and templates
Name:		kdesdk-thumbnailers
Version:	15.08.1
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	gettext-devel
BuildRequires:	kdelibs4-devel
Requires:	gettext
Conflicts:	kde-thumbnailer-po < 1:4.11.0
Obsoletes:	kde-thumbnailer-po < 1:4.11.0

%description
A preview image generator plugin for gettext translations and templates.

%files
%{_libdir}/kde4/pothumbnail.so
%{_datadir}/config.kcfg/pocreatorsettings.kcfg
%{_kde_services}/pothumbnail.desktop

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

