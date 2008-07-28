%define	name	sc68
%define	version	2.2.1
%define release %mkrel 8
%define major 2.2.1
%define libname %mklibname sc68_ %{major}

Summary:	SC68 - Atari ST and Amiga music player
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Sound
Url:		http://sc68.atari.org/
Source:		http://prdownloads.sourceforge.net/sc68/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	readline-devel
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
BuildRequires:	doxygen
BuildRequires:	pkgconfig

%description
sc68 is an Atari ST and Amiga music player. It can play special files
(.sc68). This file encapsulates orgininal music files and possibly the
program to play it.  You can find a very large collection of this file
on sc68 official web site <http://sashipa.ben.free.fr/sc68>.

This package contains a command line player.

%package -n %libname
Summary: Libraries of the sc68 sound emulator
Group: System/Libraries
Requires: %name >= %version

%description -n %libname
sc68 is an Atari ST and Amiga music player. It can play special files
(.sc68). This file encapsulates orgininal music files and possibly the
program to play it.  You can find a very large collection of this file
on sc68 official web site <http://sashipa.ben.free.fr/sc68>.

This package contains the shared libraries required by sc68.


%package -n %libname-devel
Summary: Development files of the sc68 sound emulator
Group: Development/C
Requires: %libname = %version
Provides: %name-devel = %version-%release
Provides: lib%name-devel = %version-%release

%description -n %libname-devel
sc68 is an Atari ST and Amiga music player. It can play special files
(.sc68). This file encapsulates orgininal music files and possibly the
program to play it.  You can find a very large collection of this file
on sc68 official web site <http://sashipa.ben.free.fr/sc68>.

This package contains the C headers and libraries required for
building applications with sc68.

%prep
%setup -q

%build
%define _disable_ld_no_undefined 1
%define _disable_ld_as_needed 1
%configure2_5x --enable-doc
%make
cd doc
make

%install
rm -rf %buildroot
%makeinstall_std
rm -f %buildroot%_libdir/*a

%clean
rm -rf %buildroot

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%post
%_install_info sc68.info

%postun
%_remove_install_info sc68.info

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%_bindir/*68
%_mandir/man1/*
%_infodir/sc68.info*
%_datadir/sc68

%files -n %libname
%defattr(-, root, root)
%doc COPYING README
%_libdir/lib*.so.*


%files -n %libname-devel
%defattr(-, root, root)
%doc doc/html
%_bindir/sc68-config
%_includedir/sc68/
%_libdir/lib*.so
%_libdir/pkgconfig/*.pc
