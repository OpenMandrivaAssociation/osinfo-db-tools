# Please keep this package in sync with FC

# -*- rpm-spec -*-

Group: System/Base
Summary: Tools for managing the osinfo database
Name: osinfo-db-tools
Version: 1.8.0
Release: 2
License: GPLv2+
Source0: https://releases.pagure.org/libosinfo/%{name}-%{version}.tar.xz
URL: http://libosinfo.org/

### Patches ###

BuildRequires: gettext-devel
BuildRequires: git
BuildRequires: meson
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libxml-2.0) >= 2.6.0
BuildRequires: pkgconfig(libxslt) >= 1.0.0
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: json-glib-devel
BuildRequires: perl
BuildRequires: python
BuildRequires: python-requests
Conflicts: libosinfo-common <= 0.3.0-3.mga6

%description
This package provides tools for managing the osinfo database of
information about operating systems for use with virtualization

%prep
%autosetup -S git

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%doc NEWS README
%license COPYING
%{_bindir}/osinfo-db-export
%{_bindir}/osinfo-db-import
%{_bindir}/osinfo-db-path
%{_bindir}/osinfo-db-validate
%{_mandir}/man1/osinfo-db-export.1*
%{_mandir}/man1/osinfo-db-import.1*
%{_mandir}/man1/osinfo-db-path.1*
%{_mandir}/man1/osinfo-db-validate.1*
