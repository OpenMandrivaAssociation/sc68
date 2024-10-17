%define major 2.2.1
%define libname %mklibname sc68_ %{major}
%define develname %mklibname -d %name

Summary:	Atari ST and Amiga music player
Name:		sc68
Version:	2.2.1
Release:	17
License:	GPLv2+
Group:		Sound
Url:		https://sc68.atari.org/
Source:		http://prdownloads.sourceforge.net/sc68/%{name}-%{version}.tar.bz2
Patch: sc68-2.2.1-format-string.patch

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


%package -n %{develname}
Summary: Development files of the sc68 sound emulator
Group: Development/C
Requires: %libname = %version
Provides: %name-devel = %version-%release
Provides: lib%name-devel = %version-%release
Provides: %{libname}-devel = %version-%release
Obsoletes: %{mklibname sc68_2.2.1 -d}

%description -n %{develname}
sc68 is an Atari ST and Amiga music player. It can play special files
(.sc68). This file encapsulates orgininal music files and possibly the
program to play it.  You can find a very large collection of this file
on sc68 official web site <http://sashipa.ben.free.fr/sc68>.

This package contains the C headers and libraries required for
building applications with sc68.

%prep
%setup -q
%patch -p1

%build
%define _disable_ld_no_undefined 1
%define _disable_ld_as_needed 1
%configure2_5x --enable-doc
%make
cd doc
make

%install
%makeinstall_std
rm -f %buildroot%_libdir/*a

%clean

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


%files -n %{develname}
%defattr(-, root, root)
%doc doc/html
%_bindir/sc68-config
%_includedir/sc68/
%_libdir/lib*.so
%_libdir/pkgconfig/*.pc


%changelog
* Wed Oct 26 2011 Matthew Dawkins <mattydaw@mandriva.org> 2.2.1-13
+ Revision: 707342
- rebuild
  dropped major from devel pkg

* Sat Sep 17 2011 GÃ¶tz Waschk <waschk@mandriva.org> 2.2.1-12
+ Revision: 700122
- rebuild

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 2.2.1-11mdv2011.0
+ Revision: 442816
- rebuild

* Wed Feb 25 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.2.1-10mdv2009.1
+ Revision: 344772
- fix format string

* Tue Jul 29 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.2.1-9mdv2009.0
+ Revision: 252458
- rebuild

* Mon Jul 28 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.2.1-8mdv2009.0
+ Revision: 250889
- update license
- fix build by disabling --as-needed and --no-undefined

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Jul 25 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.2.1-5mdv2008.0
+ Revision: 55243
- Import sc68



* Thu Jul 20 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.2.1-5mdk
- Rebuild

* Mon Jan 23 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.2.1-4mdk
- Rebuild
- use mkrel

* Fri Jan 21 2005 Götz Waschk <waschk@linux-mandrake.com> 2.2.1-3mdk
- rebuild for new readline

* Fri Dec  3 2004 Götz Waschk <waschk@linux-mandrake.com> 2.2.1-2mdk
- fix URL

* Wed Nov 26 2003 Götz Waschk <waschk@linux-mandrake.com> 2.2.1-1mdk
- new version

* Fri Sep 26 2003 Götz Waschk <waschk@linux-mandrake.com> 2.2.0-2mdk
- enable devel docs
- fix buildrequires
- fix devel requrires

* Fri Sep 26 2003 Götz Waschk <waschk@linux-mandrake.com> 2.2.0-1mdk
- add devel package
- drop patch
- remove xmms stuff
- new version

* Wed Mar 12 2003 Götz Waschk <waschk@linux-mandrake.com> 1.2.0-5mdk
- fix buildrequires

* Tue Mar 11 2003 Götz Waschk <waschk@linux-mandrake.com> 1.2.0-4mdk
- mklibname macro

* Fri Dec 27 2002 Götz Waschk <waschk@linux-mandrake.com> 1.2.0-3mdk
- clean unpackaged files
- fix build

* Sat Mar  2 2002 Götz Waschk <waschk@linux-mandrake.com> 1.2.0-2mdk
- really fix info dir entry

* Tue Feb  5 2002 Götz Waschk <waschk@linux-mandrake.com> 1.2.0-1mdk
- fixed info entry
- initial package
