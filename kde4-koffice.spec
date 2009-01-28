# TODO
# -- The following OPTIONAL packages could NOT be located on your system.
# -- Consider installing them to enable more features from this software.
# + Eigen2, 2.0 or higher: Eigen2 is needed by KSpread and Krita. They won't be built. <Module in kdesupport>
# + OpenCTL, 0.9.2 or higher: OpenCTL is needed for some color spaces (High Dynamic Range Color Spaces, YCbCr and LMS) <http://www.openctl.org>
# + Spnav: Spnav is the library which is required by the space navigator device plugin <http://spacenav.sourceforge.net/>
# + pstoedit: The Karbon eps import filter will not be built. <http://www.pstoedit.net/>


%define		_state		unstable
%define		origname	koffice
%define		kdever		4.2.0

Summary:	KOffice - powerful office suite for KDE
Summary(pl.UTF-8):	KOffice - potężny pakiet biurowy dla KDE
Summary(pt_BR.UTF-8):	Suíte de aplicativos office para o KDE
Summary(ru.UTF-8):	Набор оффисных программ для KDE
Summary(uk.UTF-8):	Набір офісних програм для KDE
Summary(zh_CN.UTF-8):	KDE 的办公应用软件集。
Name:		kde4-koffice
Version:	1.9.98.5
Release:	0.1
License:	GPL/LGPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{origname}-%{version}/src/%{origname}-%{version}.tar.bz2
# Source0-md5:	1525ca823dc39934a16cf1de0750ec11
Patch0:		%{name}-thumbnail.patch
URL:		http://www.koffice.org/
BuildRequires:	OpenEXR-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.6.2
BuildRequires:	exiv2-devel
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	kde4-kdepimlibs-devel >= %{kdever}
BuildRequires:	lcms-devel >= 1.15
BuildRequires:	libexif-devel >= 0.6.12
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libxml2-devel >= 0:2.4.8
BuildRequires:	libxslt-devel >= 1.0.7
BuildRequires:	mysql-devel
BuildRequires:	pkgconfig
BuildRequires:	poppler-qt-devel >= 0.5.1
BuildRequires:	python-devel >= 2.2
BuildRequires:	qca-devel >= 2.0.0
BuildRequires:	qimageblitz-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	zlib-devel
Requires:	wv2 >= 0.1.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KOffice is an integrated office suite for K Desktop Environment.
KOffice contains:
- KWord - word processor
- KFormula - formula editor
- KSpread - spreadsheet
- KPresenter - presentations
- Kivio - A Visio(R)-style flowcharting application
- KChart - diagram generator
- Karbon - A vector-based drawing application
- Krita - A pixel-based drawing application like The GIMP
- Kugar - A tool for generating business quality reports

%description -l pl.UTF-8
KOffice jest zintegrowanym pakietem biurowym dla środowiska KDE.
Pakiet między innymi zawiera:
- KWord - procesor tekstu
- KFormula - edytor równań
- KSpread - arkusz kalkulacyjny
- KPresenter - tworzenie prezentacji
- Kivio - aplikacja wzorowana na Visio(R)
- KChart - generator wykresów
- Karbon - aplikacja do edycji grafiki wektorowej
- Krita - aplikacja do edycji grafiki bitmapowej
- Kugar - narzędzie do generowania raportów jakości biznesowej

%description -l ru.UTF-8
Оффисные программы для K Desktop Environment 2.0. Содержит: KWord
(текстовый процессор), KSpread (электронная таблица), KPresenter
(презентации) и KChart (генератор диаграмм).

%description -l uk.UTF-8
Офісні програми для K Desktop Environment 2.0. Містить: KWord
(текстовий процесор), KSpread (електронна таблиця), KPresenter
(презентації) та KChart (генератор діаграм).

%package devel
Summary:	KOffice - header files
Summary(es.UTF-8):	Header files for compiling applications that use koffice libraries
Summary(pl.UTF-8):	KOffice - pliki nagłówkowe
Summary(pt_BR.UTF-8):	Arquivos de inclusão necessários à compilação de aplicações que usem as bibliotecas do koffice
Group:		X11/Development/Libraries
Requires:	%{name}-common = %{version}-%{release}

%description devel
This package includes the header files you will need to compile
applications that use koffice libraries.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne przy kompilowaniu
programów używających bibliotek KOffice.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão necessários à compilação de aplicações que usem
as bibliotecas do koffice.

%package common
Summary:	KOffice - common files and libraries
Summary(pl.UTF-8):	KOffice - wspólne pliki i biblioteki
Summary(pt_BR.UTF-8):	Arquivos requeridos por todos os softwares koffice
Group:		X11/Applications
Requires:	kdebase-core >= 9:3.2.0

%description common
KOffice is an integrated office suite for K Desktop Environment.
KOffice contains:
- KWord - word processor
- KFormula - formula editor
- KSpread - spreadsheet
- KPresenter - presentations
- Kivio - A Visio(R)-style flowcharting application
- KChart - diagram generator
- Karbon - A vector-based drawing application
- Krita - A pixel-based drawing application
- Kugar - A tool for generating business quality reports

Package contains common files and libraries needs by KOffice
applications.

%description common -l pl.UTF-8
KOffice jest zintegrowanym pakietem biurowym dla środowiska KDE.
Pakiet między innymi zawiera:
- KWord - procesor tekstu
- KFormula - edytor równań
- KSpread - arkusz kalkulacyjny
- KPresenter - tworzenie prezentacji
- Kivio - aplikacja wzorowana na Visio(R)
- KChart - generator wykresów
- Karbon - aplikacja do edycji grafiki wektorowej
- Krita - aplikacja do edycji grafiki bitmapowej
- Kugar - narzędzie do generowania raportów jakości biznesowej

Pakiet zawiera wspólne pliki i biblioteki wymagane przez aplikacje
KOffice.

%description common -l pt_BR.UTF-8
Arquivos requeridos por todos os softwares koffice.

%package karbon
Summary:	KOffice - Karbon
Summary(pl.UTF-8):	KOffice - Karbon
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description karbon
Karbon is a vector graphics application within koffice.

%description karbon -l pl.UTF-8
Karbon to aplikacja koffice służąca do rysowania grafiki wektorowej,

%package kchart
Summary:	KOffice - KChart
Summary(pl.UTF-8):	KOffice - KChart
Summary(pt_BR.UTF-8):	Gerador de diagramas do KOffice
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description kchart
KChart is KOffice part for generating diagrams from data, e.g. pie and
bar charts.

%description kchart -l pl.UTF-8
KChart jest aplikacją służącą do generowania wykresów.

%description kchart -l pt_BR.UTF-8
Gerador de diagramas do KOffice.

%package kexi
Summary:	KOffice - Kexi
Summary(pl.UTF-8):	KOffice - Kexi
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	kexi
Obsoletes:	kexi-backend-mysql
Obsoletes:	kexi-backend-pgsql

%description kexi
Kexi is KOffice part for using database system such as MySQL.

%description kexi -l pl.UTF-8
Kexi jest aplikacją służącą do korzystania z systemów baz danych
takich jak MySQL.

%package kformula
Summary:	KOffice - kformula
Summary(pl.UTF-8):	KOffice - kformula
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description kformula
KFormula is KOffice part for creating formulas, equations, etc...

%description kformula -l pl.UTF-8
KFormula jest aplikacją służącą do tworzenia wzorów, równań, itp.

%package kivio
Summary:	KOffice - kivio
Summary(pl.UTF-8):	KOffice - kivio
Summary(pt_BR.UTF-8):	Editor de fluxogramas do KOffice
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description kivio
Kivio on the surface is your everyday flowcharting program. Underneath
this skin, however, lies much more. Kivio will offer basic
flowcharting abilities, but with a twist. Objects are scriptable, and
a backend plugin system will offer the ability to make objects do just
about anything. Feed it a directory of C++ header files, or even Java
files, and let it generate a graphical class map for you. Give it a
network and let it explore and map out the network for you. All this
is possible through the scripting/plugin architecture Kivio will
possess.

%description kivio -l pl.UTF-8
Kivio jest programem typu flowcharting. Pod tym pojęciem jednak kryje
się znacznie więcej. Kivio dostarcza najpotrzebniejsze funkcje, ale
wszystkie obiekty można rozszerzać za pomocą języka skryptowego, a
system wtyczek backendowych oferuje możliwość tworzenia obiektów
dotyczących prawie wszystkiego. Kivio można nakarmić katalogiem plików
nagłówkowych C++ lub plików Javy i pozwolić wygenerować graficzną mapę
klas. Po podaniu sieci przejrzy ją i stworzy jej mapę. Wszystko to
jest możliwe poprzez architekturę skryptów i wtyczek Kivio.

%description kivio -l pt_BR.UTF-8
Editor de fluxogramas do KOffice.

%package kplato
Summary:	KOffice - KPlato
Summary(pl.UTF-8):	KOffice - KPlato
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description kplato
KPlato is a project management application.

%package kpresenter
Summary:	KOffice - KPresenter
Summary(pl.UTF-8):	KOffice - KPresenter
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description kpresenter
KPresenter is a presentation application of the KOffice, similar to MS
PowerPoint in the windows world. You can use it for doing screen
presentations or transparencies.

%description kpresenter -l pl.UTF-8
KPresenter jest aplikacją KOffice do tworzenia prezentacji, podobną do
MS PowerPoint. Możesz użyć jej do tworzenia wizualnych prezentacji.

%package krita
Summary:	KOffice - Krita
Summary(pl.UTF-8):	KOffice - Krita
Summary(pt_BR.UTF-8):	Ferramenta de desenho vetorial do KOffice
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description krita
Krita is a painting and image editing application for KOffice. It
supports many color spaces like RGB, grayscale, CMYK, Lab, YCBCR and
LMS, in 8 and 16 bits per channel

%description krita -l pl.UTF-8
Krita jest aplikacją do edycji grafiki bitmapowej. Wspiera różne
przestrzenie barw, jak np. RGB, skala szarości, CMYK, Lab, YCBCR
oraz LMS - zarówno w trybie 8 jak i 16 bitowym na kanał.

%package kross-python
Summary:	KOffice - Kross Python
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description kross-python
Kross is a scripting bridge to embed scripting functionality into an
application. Kross provides an abstract API to access the scripting
functionality in a interpreter-independend way. This package provides
Python scripting backend.

%package kross-ruby
Summary:	KOffice - Kross Ruby
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description kross-ruby
Kross is a scripting bridge to embed scripting functionality into an
application. Kross provides an abstract API to access the scripting
functionality in a interpreter-independend way. This package provides
Ruby scripting backend.

%package kspread
Summary:	KOffice - KSpread
Summary(pl.UTF-8):	KOffice - KSpread
Summary(pt_BR.UTF-8):	Planilha eletrônica do KOffice
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description kspread
KSpread is the spread sheet of the KOffice, similar to MS Excel.

%description kspread -l pl.UTF-8
KSpread jest arkuszem kalkulacyjnym, podobnym do MS Excel.

%description kspread -l pt_BR.UTF-8
Planilha eletrônica do KOffice.

%package kugar
Summary:	KOffice - KUgar
Summary(pl.UTF-8):	KOffice - KUgar
Summary(pt_BR.UTF-8):	Gerador de relatórios do KOffice
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description kugar
Kugar is a KDE tool for generating business quality reports which can
be viewed and printed. It includes a standalone report application can
embed the report viewing functionality and that reports can be viewed
using the Konqueror browser.

%description kugar -l pl.UTF-8
Kugar jest narzędziem KDE do generowania raportów o jakości
biznesowej, które mogą być przeglądane oraz drukowane. Dodatkowo
dołączony jest program który może być dołączony do raportu
umożliwiając oglądanie raportu w przeglądarce Konqueror.

%description kugar -l pt_BR.UTF-8
Gerador de relatórios do KOffice.

%package kword
Summary:	KOffice - KWord
Summary(pl.UTF-8):	KOffice - KWord
Summary(pt_BR.UTF-8):	Processador de texto do KOffice
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description kword
KWord is a FrameMaker-like wordprocessor application for KOffice. So
it can be used for DTP, but also for "normal" wordprocessing (like
writing letters, reports, etc.).

%description kword -l pl.UTF-8
KWord jest ramkowym procesorem tekstu. Może być użyty do DTP, ale
również do zwykłej edycji tekstu (jak pisanie listów, raportów, itp.).

%description kword -l pt_BR.UTF-8
Processador de texto do KOffice.

%package apidocs
Summary:	Koffice API documentation
Summary(pl.UTF-8):	Dokumentacja API dla Koffice
Group:		Documentation
Requires:	%{name}-devel = %{version}-%{release}

%description apidocs
Annotated reference of KOffice libraries programming interface
including:
- class lists
- class members
- namespaces

%description apidocs -l pl.UTF-8
Dokumentacja interfejsu programowania bibliotek KOffice z przypisami.
Zawiera:
- listy klas i ich składników
- listę przestrzeni nazw (namespace)

%prep
%setup -q -n %{origname}-%{version}
%patch0 -p0

%build
install -d build
cd build
%cmake \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
        -DLIB_SUFFIX=64 \
%endif
        ../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	common -p /sbin/ldconfig
%postun common -p /sbin/ldconfig

%post   karbon -p /sbin/ldconfig
%postun karbon -p /sbin/ldconfig

%post   kchart -p /sbin/ldconfig
%postun kchart -p /sbin/ldconfig

%post	kexi -p /sbin/ldconfig
%postun	kexi -p /sbin/ldconfig

%post	kivio -p /sbin/ldconfig
%postun	kivio -p /sbin/ldconfig

%post	kplato -p /sbin/ldconfig
%postun	kplato -p /sbin/ldconfig

%post	kpresenter -p /sbin/ldconfig
%postun	kpresenter -p /sbin/ldconfig

%post	krita -p /sbin/ldconfig
%postun	krita -p /sbin/ldconfig

%post   kspread -p /sbin/ldconfig
%postun kspread -p /sbin/ldconfig

%post   kugar -p /sbin/ldconfig
%postun kugar -p /sbin/ldconfig

%post   kword -p /sbin/ldconfig
%postun kword -p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%exclude %{_libdir}/libkdeinit4_*.so
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h

%files common
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/koconverter
%attr(755,root,root) %{_libdir}/libkdchart.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdchart.so.?
%attr(755,root,root) %{_libdir}/libkochart.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkochart.so.?
%attr(755,root,root) %{_libdir}/libkoffice_graya_u16.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkoffice_graya_u16.so.?
%attr(755,root,root) %{_libdir}/libkofficegrayau8colorspace.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkofficegrayau8colorspace.so.?
%attr(755,root,root) %{_libdir}/libkopageapp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopageapp.so.?
%attr(755,root,root) %{_libdir}/libkotext.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkotext.so.?
%attr(755,root,root) %{_libdir}/libkowmf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkowmf.so.?
%attr(755,root,root) %{_libdir}/libkwmf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkwmf.so.?
%attr(755,root,root) %{_libdir}/libkwordexportfilters.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkwordexportfilters.so.?
%attr(755,root,root) %{_libdir}/kde4/clipartthumbnail.so
%attr(755,root,root) %{_libdir}/kde4/kodocinfopropspage.so
%attr(755,root,root) %{_libdir}/kde4/kofficescan.so
%attr(755,root,root) %{_libdir}/kde4/kofficethumbnail.so
%attr(755,root,root) %{_libdir}/kde4/libgenerickofilter.so
%attr(755,root,root) %{_libdir}/kde4/libxslt*port*.so
%attr(755,root,root) %{_libdir}/kde4/libkounavailpart.so
%{_datadir}/apps/koffice
%{_datadir}/kde4/services/clipartthumbnail.desktop
%{_datadir}/kde4/services/kodocinfopropspage.desktop
%{_datadir}/kde4/services/kofficethumbnail.desktop
%{_datadir}/kde4/services/kounavail.desktop
%{_datadir}/kde4/services/xslt_*.desktop
%{_datadir}/kde4/services/generic_filter.desktop
%{_datadir}/kde4/servicetypes/*
%dir %{_datadir}/templates/.source
%{_desktopdir}/kde4/koffice.desktop

#%files karbon
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/karbon
#%{_libdir}/libkarbon*.la
#%attr(755,root,root) %{_libdir}/libkarbon*.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkarboncommon.so.0
#%attr(755,root,root) %{_libdir}/libkdeinit4_karbon.so
#%{_libdir}/kde3/liboodrawimport.la
#%attr(755,root,root) %{_libdir}/kde3/liboodrawimport.so
#%{_libdir}/kde3/*karbon*.la
#%attr(755,root,root) %{_libdir}/kde3/*karbon*.so
#%{_libdir}/kde3/*wmf*port.la
#%attr(755,root,root) %{_libdir}/kde3/*wmf*port.so
#%{_datadir}/apps/karbon
#%{_datadir}/apps/konqueror/servicemenus/karbon_konqi.desktop
#%{_datadir}/services/karbon*
#%{_datadir}/templates/.source/Illustration.karbon
#%{_datadir}/templates/Illustration.desktop
#%{_desktopdir}/kde/karbon.desktop
#%{_iconsdir}/*/*/apps/karbon.png
#%{_iconsdir}/hicolor/scalable/apps/karbon.svgz
#
#%files kchart
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kchart
#%{_libdir}/libkchartcommon.la
#%attr(755,root,root) %{_libdir}/libkchartcommon.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkchartcommon.so.2
#%{_libdir}/libkchartimageexport.la
#%attr(755,root,root) %{_libdir}/libkchartimageexport.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkchartimageexport.so.4
#%attr(755,root,root) %{_libdir}/libkdeinit4_kchart.so
#%{_libdir}/kde3/kchart.la
#%attr(755,root,root) %{_libdir}/kde3/kchart.so
#%{_libdir}/kde3/libkchart*.la
#%attr(755,root,root) %{_libdir}/kde3/libkchart*.so
#%{_datadir}/apps/kchart
#%{_datadir}/apps/konqueror/servicemenus/kchart_konqi.desktop
#%{_datadir}/services/kchart*.desktop
#%{_desktopdir}/kde/kchart.desktop
#%{_iconsdir}/*/*x*/apps/kchart.png
#
#%files kexi
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kexi*
#%attr(755,root,root) %{_bindir}/ksqlite
#%attr(755,root,root) %{_bindir}/ksqlite2
#%attr(755,root,root) %{_bindir}/ksqlite2to3
#%attr(755,root,root) %{_libdir}/libkdeinit4_kexi.so
#%{_libdir}/libkformdesigner.la
#%attr(755,root,root) %{_libdir}/libkformdesigner.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkformdesigner.so.2
#%{_libdir}/libkexi*.la
#%attr(755,root,root) %{_libdir}/libkexi*.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkexicore.so.2
#%attr(755,root,root) %ghost %{_libdir}/libkexidatatable.so.2
#%attr(755,root,root) %ghost %{_libdir}/libkexidb.so.2
#%attr(755,root,root) %ghost %{_libdir}/libkexidbparser.so.2
#%attr(755,root,root) %ghost %{_libdir}/libkexiextendedwidgets.so.2
#%attr(755,root,root) %ghost %{_libdir}/libkexiformutils.so.2
#%attr(755,root,root) %ghost %{_libdir}/libkexiguiutils.so.2
#%attr(755,root,root) %ghost %{_libdir}/libkeximain.so.2
#%attr(755,root,root) %ghost %{_libdir}/libkeximigrate.so.2
#%attr(755,root,root) %ghost %{_libdir}/libkexirelationsview.so.2
#%attr(755,root,root) %ghost %{_libdir}/libkexisql2.so.2
#%attr(755,root,root) %ghost %{_libdir}/libkexisql3.so.3
#%attr(755,root,root) %ghost %{_libdir}/libkexiutils.so.2
#%{_libdir}/kde3/*kexi*.la
#%attr(755,root,root) %{_libdir}/kde3/*kexi*.so
#%{_libdir}/kde3/kformdesigner_containers.la
#%attr(755,root,root) %{_libdir}/kde3/kformdesigner_containers.so
#%{_libdir}/kde3/kformdesigner_stdwidgets.la
#%attr(755,root,root) %{_libdir}/kde3/kformdesigner_stdwidgets.so
#%{_datadir}/apps/kexi
#%{_datadir}/apps/konqueror/servicemenus/kexi_konqi.desktop
#%{_datadir}/config/kexirc
#%{_datadir}/config/magic/kexi.magic
#%{_datadir}/mimelnk/application/x-kexiproject-shortcut.desktop
#%{_datadir}/mimelnk/application/x-kexiproject-sqlite**.desktop
#%{_datadir}/mimelnk/application/x-kexi-connectiondata.desktop
#%{_datadir}/services/kexi*
#%{_datadir}/services/kformdesigner
#%{_desktopdir}/kde/kexi.desktop
#%{_iconsdir}/hicolor/*/apps/kexi.*
#%{_iconsdir}/crystalsvg/*/mimetypes/kexiproject_*.png
#%{_mandir}/man1/*
#
#%files kformula
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kformula
#%attr(755,root,root) %{_libdir}/libkdeinit4_kformula*.so
#%{_libdir}/kde3/libkfo*.la
#%attr(755,root,root) %{_libdir}/kde3/libkfo*.so
#%{_libdir}/kde3/kformula.la
#%attr(755,root,root) %{_libdir}/kde3/kformula.so
#%{_datadir}/apps/kformula
#%{_datadir}/services/kformula*
#%{_datadir}/apps/konqueror/servicemenus/kformula_konqi.desktop
#%{_desktopdir}/kde/kformula.desktop
#%{_iconsdir}/*/*/actions/abs.png
#%{_iconsdir}/*/*/actions/brac*.png
#%{_iconsdir}/*/*/actions/frac.png
#%{_iconsdir}/*/*/actions/ins*.png
#%{_iconsdir}/*/*/actions/rem*.png
#%{_iconsdir}/*/*/actions/int.png
#%{_iconsdir}/*/*/actions/[lr]su[bp].png
#%{_iconsdir}/*/*/actions/matrix.png
#%{_iconsdir}/*/*/actions/paren.png
#%{_iconsdir}/*/*/actions/prod.png
#%{_iconsdir}/*/*/actions/sqrt.png
#%{_iconsdir}/*/*/actions/sum.png
#%{_iconsdir}/*/*/actions/onetwomatrix.png
#%{_iconsdir}/*/*/actions/multiline.png
#%{_iconsdir}/*/*/actions/over.png
#%{_iconsdir}/*/*/actions/under.png
#%{_iconsdir}/*/*/apps/kformula.png
#
#%files kivio
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kivio
#%{_libdir}/libkiviocommon.la
#%attr(755,root,root) %{_libdir}/libkiviocommon.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkiviocommon.so.0
#%attr(755,root,root) %{_libdir}/libkdeinit4_kivio.so
#%{_libdir}/kde3/*kivio*.la
#%attr(755,root,root) %{_libdir}/kde3/*kivio*.so
#%{_libdir}/kde3/straight_connector.la
#%attr(755,root,root) %{_libdir}/kde3/straight_connector.so
#%{_datadir}/apps/kivio
#%{_datadir}/apps/konqueror/servicemenus/kivio_konqi.desktop
#%{_datadir}/config.kcfg/kivio.kcfg
#%{_datadir}/services/kivio*.desktop
#%{_desktopdir}/kde/kivio.desktop
#%{_iconsdir}/*/*/apps/kivio.png
#
#%files kplato
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kplato
#%attr(755,root,root) %{_libdir}/libkdeinit4_kplato.so
#%{_libdir}/kde3/kplato.la
#%attr(755,root,root) %{_libdir}/kde3/kplato.so
#%{_libdir}/kde3/libkplatopart.la
#%attr(755,root,root) %{_libdir}/kde3/libkplatopart.so
#%{_datadir}/apps/kplato
#%{_datadir}/services/kplatopart.desktop
#%{_desktopdir}/kde/kplato.desktop
#%{_iconsdir}/crystalsvg/*/apps/kplato.*
#
#%files kpresenter
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kpresenter
#%attr(755,root,root) %{_bindir}/kprconverter.pl
#%{_libdir}/libkpresenterimageexport.la
#%attr(755,root,root) %{_libdir}/libkpresenterimageexport.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkpresenterimageexport.so.4
#%{_libdir}/libkpresenterprivate.la
#%attr(755,root,root) %{_libdir}/libkpresenterprivate.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkpresenterprivate.so.4
#%attr(755,root,root) %{_libdir}/libkdeinit4_kpresenter.so
#%{_libdir}/kde3/kpresenter.la
#%attr(755,root,root) %{_libdir}/kde3/kpresenter.so
#%{_libdir}/kde3/libkpresenter*.la
#%attr(755,root,root) %{_libdir}/kde3/libkpresenter*.so
#%{_libdir}/kde3/libkprkword.la
#%attr(755,root,root) %{_libdir}/kde3/libkprkword.so
#%{_libdir}/kde3/libooimpress*port.la
#%attr(755,root,root) %{_libdir}/kde3/libooimpress*port.so
#%{_libdir}/kde3/libpowerpointimport.la
#%attr(755,root,root) %{_libdir}/kde3/libpowerpointimport.so
#%{_datadir}/apps/kpresenter
#%{_datadir}/apps/konqueror/servicemenus/kpresenter_konqi.desktop
#%{_datadir}/templates/.source/Presentation.kpt
#%{_datadir}/templates/Presentation.desktop
#%{_datadir}/services/kprkword.desktop
#%{_datadir}/services/kpresenter*.desktop
#%{_desktopdir}/kde/kpresenter.desktop
#%{_iconsdir}/*/*/apps/kpresenter*.png
#
#%files krita
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/krita
#%{_libdir}/libkrita*.la
#%attr(755,root,root) %{_libdir}/libkrita*.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkrita_cmyk_u16.so.0
#%attr(755,root,root) %ghost %{_libdir}/libkrita_gray_u16.so.0
#%attr(755,root,root) %ghost %{_libdir}/libkrita_lms_f32.so.0
#%attr(755,root,root) %ghost %{_libdir}/libkrita_rgb_f16half.so.0
#%attr(755,root,root) %ghost %{_libdir}/libkrita_rgb_f32.so.0
#%attr(755,root,root) %ghost %{_libdir}/libkrita_rgb_u16.so.0
#%attr(755,root,root) %ghost %{_libdir}/libkrita_ycbcr_u16.so.0
#%attr(755,root,root) %ghost %{_libdir}/libkrita_ycbcr_u8.so.0
#%attr(755,root,root) %ghost %{_libdir}/libkritacolor.so.1
#%attr(755,root,root) %ghost %{_libdir}/libkritacommon.so.1
#%attr(755,root,root) %ghost %{_libdir}/libkritagrayscale.so.0
#%attr(755,root,root) %ghost %{_libdir}/libkritaimage.so.1
#%attr(755,root,root) %ghost %{_libdir}/libkritargb.so.0
#%attr(755,root,root) %ghost %{_libdir}/libkritascripting.so.0
#%attr(755,root,root) %ghost %{_libdir}/libkritaui.so.1
#%attr(755,root,root) %{_libdir}/libkdeinit4_krita.so
#%{_libdir}/kde3/*krita*.la
#%attr(755,root,root) %{_libdir}/kde3/*krita*.so
#%{_datadir}/apps/konqueror/servicemenus/krita_konqi.desktop
#%{_datadir}/apps/krita
#%{_datadir}/apps/kritaplugins
#%{_datadir}/services/krita*.desktop
#%{_datadir}/templates/Illustration.desktop
#%{_datadir}/applnk/.hidden/krita_*.desktop
#%{_desktopdir}/kde/krita.desktop
#%{_iconsdir}/hicolor/*/apps/krita.png
#
#%files kross-python
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde3/krosspython.so
#%{_libdir}/kde3/krosspython.la
#%{_datadir}/apps/kross/python
#
#%files kross-ruby
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde3/krossruby.so
#%{_libdir}/kde3/krossruby.la
#
#%files kspread
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kspread
#%{_libdir}/libkdeinit_kspread.la
#%attr(755,root,root) %{_libdir}/libkdeinit_kspread.so
#%{_libdir}/kde3/kspread.la
#%attr(755,root,root) %{_libdir}/kde3/kspread.so
#%{_libdir}/kde3/krosskspreadcore.la
#%attr(755,root,root) %{_libdir}/kde3/krosskspreadcore.so
#%{_libdir}/kde3/kspreadscripting.la
#%attr(755,root,root) %{_libdir}/kde3/kspreadscripting.so
#%{_libdir}/kde3/libkspread*.la
#%attr(755,root,root) %{_libdir}/kde3/libkspread*.so
#%{_libdir}/kde3/libcsv*.la
#%attr(755,root,root) %{_libdir}/kde3/libcsv*.so
#%{_libdir}/kde3/libapplixspreadimport.la
#%attr(755,root,root) %{_libdir}/kde3/libapplixspreadimport.so
#%{_libdir}/kde3/libexcelimport.la
#%attr(755,root,root) %{_libdir}/kde3/libexcelimport.so
#%{_libdir}/kde3/kfile_gnumeric.la
#%attr(755,root,root) %{_libdir}/kde3/kfile_gnumeric.so
#%{_libdir}/kde3/libgnumeric*port.la
#%attr(755,root,root) %{_libdir}/kde3/libgnumeric*port.so
#%{_libdir}/kde3/libdbase*port.la
#%attr(755,root,root) %{_libdir}/kde3/libdbase*port.so
#%{_libdir}/kde3/libqproimport.la
#%attr(755,root,root) %{_libdir}/kde3/libqproimport.so
#%{_libdir}/kde3/libopencalc*port.la
#%attr(755,root,root) %{_libdir}/kde3/libopencalc*port.so
#%{_libdir}/kde3/kwmailmerge_kspread.la
#%attr(755,root,root) %{_libdir}/kde3/kwmailmerge_kspread.so
#%{_datadir}/apps/kspread
#%{_datadir}/apps/konqueror/servicemenus/kspread_konqi.desktop
#%{_datadir}/services/kfile_gnumeric.desktop
#%{_datadir}/services/kspread*.desktop
#%{_datadir}/services/kwmailmerge_kspread.desktop
#%{_datadir}/templates/.source/SpreadSheet.kst
#%{_datadir}/templates/SpreadSheet.desktop
#%{_desktopdir}/kde/kspread.desktop
#%{_iconsdir}/[!l]*/*/apps/kspread*.png
#
#%files kugar
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kudesigner
#%attr(755,root,root) %{_bindir}/kugar
#%{_libdir}/libkdeinit_kudesigner.la
#%attr(755,root,root) %{_libdir}/libkdeinit_kudesigner.so
#%{_libdir}/libkugarlib.la
#%attr(755,root,root) %{_libdir}/libkugarlib.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkugarlib.so.1
#%{_libdir}/libkdeinit_kugar.la
#%attr(755,root,root) %{_libdir}/libkdeinit_kugar.so
#%{_libdir}/libkudesignercore.la
#%attr(755,root,root) %{_libdir}/libkudesignercore.so
#%{_libdir}/kde3/*kugar*.la
#%attr(755,root,root) %{_libdir}/kde3/*kugar*.so
#%{_libdir}/kde3/*kudesigner*.la
#%attr(755,root,root) %{_libdir}/kde3/*kudesigner*.so
#%{_desktopdir}/kde/kudesigner.desktop
#%{_desktopdir}/kde/kugar.desktop
#%{_datadir}/apps/kudesigner
#%{_datadir}/apps/kugar
#%{_datadir}/services/kugar_kugar_import.desktop
#%{_datadir}/services/kugarpart.desktop
#%{_iconsdir}/*/*/*/kudesigner.png
#%{_iconsdir}/*/*/*/kugar.png
#%{_iconsdir}/*/*/mimetypes/kugardata.png
#
#%files kword
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kthesaurus
#%attr(755,root,root) %{_bindir}/kword
#%{_libdir}/libkdeinit_kword.la
#%attr(755,root,root) %{_libdir}/libkdeinit_kword.so
#%{_libdir}/libkwordprivate.la
#%attr(755,root,root) %{_libdir}/libkwordprivate.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkwordprivate.so.4
#%{_libdir}/libkword*export*.la
#%attr(755,root,root) %{_libdir}/libkword*export*.so
#%attr(755,root,root) %ghost %{_libdir}/libkwordexportfilters.so.1
#%{_libdir}/libkdeinit_kthesaurus.la
#%attr(755,root,root) %{_libdir}/libkdeinit_kthesaurus.so
#%{_libdir}/kde3/kthesaurus.la
#%attr(755,root,root) %{_libdir}/kde3/kthesaurus.so
#%{_libdir}/kde3/kword.la
#%attr(755,root,root) %{_libdir}/kde3/kword.so
#%{_libdir}/kde3/kfile_abiword.la
#%attr(755,root,root) %{_libdir}/kde3/kfile_abiword.so
#%{_libdir}/kde3/libabiword*port.la
#%attr(755,root,root) %{_libdir}/kde3/libabiword*port.so
#%{_libdir}/kde3/libhancomwordimport.la
#%attr(755,root,root) %{_libdir}/kde3/libhancomwordimport.so
#%{_libdir}/kde3/libmswordimport.la
#%attr(755,root,root) %{_libdir}/kde3/libmswordimport.so
#%{_libdir}/kde3/libapplixwordimport.la
#%attr(755,root,root) %{_libdir}/kde3/libapplixwordimport.so
#%{_libdir}/kde3/libascii*port.la
#%attr(755,root,root) %{_libdir}/kde3/libascii*port.so
#%{_libdir}/kde3/libdocbookexport.la
#%attr(755,root,root) %{_libdir}/kde3/libdocbookexport.so
#%{_libdir}/kde3/libhtml*port.la
#%attr(755,root,root) %{_libdir}/kde3/libhtml*port.so
#%{_libdir}/kde3/libpalmdoc*port.la
#%attr(755,root,root) %{_libdir}/kde3/libpalmdoc*port.so
#%{_libdir}/kde3/libamipro*port.la
#%attr(755,root,root) %{_libdir}/kde3/libamipro*port.so
#%{_libdir}/kde3/libpdfimport.la
#%attr(755,root,root) %{_libdir}/kde3/libpdfimport.so
#%{_libdir}/kde3/libwml*port.la
#%attr(755,root,root) %{_libdir}/kde3/libwml*port.so
#%{_libdir}/kde3/librtf*port.la
#%attr(755,root,root) %{_libdir}/kde3/librtf*port.so
#%{_libdir}/kde3/libthesaurustool.la
#%attr(755,root,root) %{_libdir}/kde3/libthesaurustool.so
#%{_libdir}/kde3/libwp*port.la
#%attr(755,root,root) %{_libdir}/kde3/libwp*port.so
#%{_libdir}/kde3/libmswrite*port.la
#%attr(755,root,root) %{_libdir}/kde3/libmswrite*port.so
#%{_libdir}/kde3/libkword*.la
#%attr(755,root,root) %{_libdir}/kde3/libkword*.so
#%{_libdir}/kde3/liboowriter*port.la
#%attr(755,root,root) %{_libdir}/kde3/liboowriter*port.so
#%{_libdir}/kde3/kwmailmerge_classic.la
#%attr(755,root,root) %{_libdir}/kde3/kwmailmerge_classic.so
#%{_libdir}/kde3/kwmailmerge_kabc.la
#%attr(755,root,root) %{_libdir}/kde3/kwmailmerge_kabc.so
#%{_libdir}/kde3/kwmailmerge_qtsqldb*.la
#%attr(755,root,root) %{_libdir}/kde3/kwmailmerge_qtsqldb*.so
#%{_datadir}/apps/kword
#%{_datadir}/apps/thesaurus
#%dir %{_datadir}/apps/xsltfilter
#%dir %{_datadir}/apps/xsltfilter/export
#%dir %{_datadir}/apps/xsltfilter/export/kword
#%dir %{_datadir}/apps/xsltfilter/export/kword/xslfo
#%{_datadir}/apps/xsltfilter/export/kword/xslfo/*.xsl
#%{_datadir}/apps/konqueror/servicemenus/kword_konqi.desktop
#%{_datadir}/services/kfile_abiword.desktop
#%{_datadir}/services/kword*.desktop
#%{_datadir}/services/thesaurustool.desktop
#%{_datadir}/services/kwmailmerge_kabc.desktop
## this is the mailmerge service info for qtsqldb and classic
#%{_datadir}/services/kwserialletter*
#%{_datadir}/templates/.source/TextDocument.kwt
#%{_datadir}/templates/TextDocument.desktop
#%{_desktopdir}/kde/KThesaurus.desktop
#%{_desktopdir}/kde/kword.desktop
#%{_iconsdir}/*/*/apps/kword.png
