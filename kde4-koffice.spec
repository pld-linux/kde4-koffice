# TODO
# -- The following OPTIONAL packages could NOT be located on your system.
# -- Consider installing them to enable more features from this software.
# + OpenCTL, 0.9.2 or higher: OpenCTL is needed for some color spaces (High Dynamic Range Color Spaces, YCbCr and LMS) <http://www.openctl.org>
# + Spnav: Spnav is the library which is required by the space navigator device plugin <http://spacenav.sourceforge.net/>
# + pstoedit: The Karbon eps import filter will not be built. <http://www.pstoedit.net/>
#
# Conditional build:
%bcond_without	pdf		# build without PDF support

%define		_state		stable
%define		orgname		koffice
%define		kdever		4.4.3
%define		qtver		4.6.2

Summary:	KOffice - powerful office suite for KDE
Summary(pl.UTF-8):	KOffice - potężny pakiet biurowy dla KDE
Summary(pt_BR.UTF-8):	Suíte de aplicativos office para o KDE
Summary(ru.UTF-8):	Набор оффисных программ для KDE
Summary(uk.UTF-8):	Набір офісних програм для KDE
Summary(zh_CN.UTF-8):	KDE 的办公应用软件集。
Name:		kde4-koffice
Version:	2.2.0
Release:	2
License:	GPL/LGPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{orgname}-%{version}/%{orgname}-%{version}.tar.bz2
# Source0-md5:	204afae16ff90148a61752bccd86b278
URL:		http://www.koffice.org/
BuildRequires:	GraphicsMagick-devel
BuildRequires:	OpenEXR-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtScript-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	QtUiTools-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	boost-devel
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	eigen >= 1:2.0.12-3
BuildRequires:	exiv2-devel
BuildRequires:	glew-devel
BuildRequires:	gmm-devel
BuildRequires:	gsl-devel
BuildRequires:	kde4-kdegraphics-devel >= %{kdever}
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	kde4-kdepimlibs-devel >= %{kdever}
BuildRequires:	lcms-devel >= 1.18
BuildRequires:	libexif-devel >= 0.6.12
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libwpd-devel
BuildRequires:	libwpg-devel
BuildRequires:	libxml2-devel >= 0:2.4.8
BuildRequires:	libxslt-devel >= 1.0.7
BuildRequires:	mysql-devel
BuildRequires:	pkgconfig
%if %{with pdf}
BuildRequires:	poppler-Qt-devel >= 0.6
%endif
BuildRequires:	python-devel >= 2.2
BuildRequires:	qca-devel >= 2.0.0
BuildRequires:	qimageblitz-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sqlite3-devel >= 3.6.23
BuildRequires:	wv2-devel >= 0.4.1
BuildRequires:	xbase-devel
BuildRequires:	zlib-devel
Requires:	wv2 >= 0.4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KOffice is an integrated office suite for K Desktop Environment.
KOffice contains:
- KWord - word processor
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
- KSpread - arkusz kalkulacyjny
- KPresenter - tworzenie prezentacji
- Kivio - aplikacja wzorowana na Visio(R)
- KChart - generator wykresów
- Karbon - aplikacja do edycji grafiki wektorowej
- Krita - aplikacja do edycji grafiki bitmapowej

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
Requires:	kde4-kdebase-workspace >= %{kdever}

%description common
KOffice is an integrated office suite for K Desktop Environment.
KOffice contains:
- KWord - word processor
- KSpread - spreadsheet
- KPresenter - presentations
- Kivio - A Visio(R)-style flowcharting application
- KChart - diagram generator
- Karbon - A vector-based drawing application
- Krita - A pixel-based drawing application

Package contains common files and libraries needs by KOffice
applications.

%description common -l pl.UTF-8
KOffice jest zintegrowanym pakietem biurowym dla środowiska KDE.
Pakiet między innymi zawiera:
- KWord - procesor tekstu
- KSpread - arkusz kalkulacyjny
- KPresenter - tworzenie prezentacji
- Kivio - aplikacja wzorowana na Visio(R)
- KChart - generator wykresów
- Karbon - aplikacja do edycji grafiki wektorowej
- Krita - aplikacja do edycji grafiki bitmapowej

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
Summary:        KOffice - Kexi
Summary(pl.UTF-8):      KOffice - Kexi
Group:          X11/Applications
Requires:       %{name}-common = %{version}-%{release}

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
KFormula jest aplikacją służącą do tworzenia wzorów, równań itp.

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
przestrzenie barw, jak np. RGB, skala szarości, CMYK, Lab, YCBCR oraz
LMS - zarówno w trybie 8 jak i 16 bitowym na kanał.

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

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
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

%post	common	-p /sbin/ldconfig
%postun	common	-p /sbin/ldconfig

%post	karbon	-p /sbin/ldconfig
%postun	karbon	-p /sbin/ldconfig

%post	kchart	-p /sbin/ldconfig
%postun	kchart	-p /sbin/ldconfig

%post	kexi	-p /sbin/ldconfig
%postun	kexi	-p /sbin/ldconfig

%post	kformula	-p /sbin/ldconfig
%postun	kformula	-p /sbin/ldconfig

%post	kplato	-p /sbin/ldconfig
%postun	kplato	-p /sbin/ldconfig

%post	kpresenter	-p /sbin/ldconfig
%postun	kpresenter	-p /sbin/ldconfig

%post	krita	-p /sbin/ldconfig
%postun	krita	-p /sbin/ldconfig

%post	kspread	-p /sbin/ldconfig
%postun	kspread	-p /sbin/ldconfig

%post	kword	-p /sbin/ldconfig
%postun	kword	-p /sbin/ldconfig

%files common
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/koconverter
%attr(755,root,root) %{_libdir}/libkdchart.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdchart.so.?
%attr(755,root,root) %{_libdir}/libkochart.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkochart.so.?
#%attr(755,root,root) %{_libdir}/libkoffice_graya_u16.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkoffice_graya_u16.so.?
#%attr(755,root,root) %{_libdir}/libkofficegrayau8colorspace.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkofficegrayau8colorspace.so.?
%attr(755,root,root) %{_libdir}/libkopageapp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopageapp.so.?
%attr(755,root,root) %{_libdir}/libkotext.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkotext.so.?
%attr(755,root,root) %ghost %{_libdir}/libkoproperty.so.?
%attr(755,root,root) %{_libdir}/libkoproperty.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkoreport.so.?
%attr(755,root,root) %{_libdir}/libkoreport.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkowv2.so.?
%attr(755,root,root) %{_libdir}/libkowv2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmsooxml.so.?
%attr(755,root,root) %{_libdir}/libmsooxml.so.*.*.*
%attr(755,root,root) %{_libdir}/libkowmf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkowmf.so.?
%attr(755,root,root) %{_libdir}/libkwmf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkwmf.so.?
%attr(755,root,root) %{_libdir}/libkwordexportfilters.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkwordexportfilters.so.?
#%attr(755,root,root) %ghost %{_libdir}/libkoaction.so.?
#%attr(755,root,root) %{_libdir}/libkoaction.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkobase.so.?
#%attr(755,root,root) %{_libdir}/libkobase.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkocolorwidgets.so.?
#%attr(755,root,root) %{_libdir}/libkocolorwidgets.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkoplugin.so.?
%attr(755,root,root) %{_libdir}/libkoplugin.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkowidgets.so.?
%attr(755,root,root) %{_libdir}/libkowidgets.so.*.*.*
%attr(755,root,root) %{_libdir}/libkarbonui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkarbonui.so.?
%attr(755,root,root) %{_libdir}/libkpresenterprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkpresenterprivate.so.?
#%attr(755,root,root) %{_libdir}/kde4/clipartthumbnail.so
#%attr(755,root,root) %{_libdir}/kde4/kodocinfopropspage.so
%attr(755,root,root) %{_libdir}/kde4/kofficescan.so
%attr(755,root,root) %{_libdir}/kde4/kofficethumbnail.so
%attr(755,root,root) %{_libdir}/kde4/libgenerickofilter.so
%attr(755,root,root) %{_libdir}/kde4/libxslt*port*.so
%attr(755,root,root) %{_libdir}/kde4/libkounavailpart.so
#%attr(755,root,root) %{_libdir}/kde4/koffice_graya_u16_plugin.so
%attr(755,root,root) %{_libdir}/kde4/kofficedockers.so
#%attr(755,root,root) %{_libdir}/kde4/kofficegrayau8plugin.so
%attr(755,root,root) %{_libdir}/kde4/kolcmsengine.so
%attr(755,root,root) %{_libdir}/kde4/kprvariables.so
%attr(755,root,root) %{_libdir}/kde4/vectorshape.so
%attr(755,root,root) %{_libdir}/kde4/videoshape.so
%{_datadir}/apps/koffice
#%{_datadir}/kde4/services/clipartthumbnail.desktop
#%{_datadir}/kde4/services/kodocinfopropspage.desktop
%{_datadir}/kde4/services/kofficethumbnail.desktop
#%{_datadir}/kde4/services/koffice_graya_u16_plugin.desktop
%{_datadir}/kde4/services/kofficedockers.desktop
#%{_datadir}/kde4/services/kofficegrayaplugin.desktop
%{_datadir}/kde4/services/kounavail.desktop
%{_datadir}/kde4/services/xslt_*.desktop
%{_datadir}/kde4/services/generic_filter.desktop
%{_datadir}/kde4/services/kolcmsengine.desktop
%{_datadir}/kde4/services/kprvariables.desktop
%{_datadir}/kde4/services/vectorshape.desktop
%{_datadir}/kde4/services/videoshape.desktop
%{_datadir}/mime/packages/msooxml-all.xml
%{_datadir}/kde4/servicetypes/*
%dir %{_datadir}/templates/.source
%{_desktopdir}/kde4/koffice.desktop
%{_iconsdir}/oxygen/*/actions/*.png
%exclude %{_iconsdir}/oxygen/scalable
#%{_iconsdir}/oxygen/*/actions/*.svgz
%{_kdedocdir}/en/koffice
%dir %{_datadir}/color
%dir %{_datadir}/color/icc
%{_datadir}/color/icc/pigment
#
# Files i dunno what to do with
#
%attr(755,root,root) %{_libdir}/kde4/artistictextshape.so
%attr(755,root,root) %{_libdir}/kde4/autocorrect.so
%attr(755,root,root) %{_libdir}/kde4/changecase.so
%attr(755,root,root) %{_libdir}/kde4/defaulttools.so
%attr(755,root,root) %{_libdir}/kde4/divineproportionshape.so
%attr(755,root,root) %{_libdir}/kde4/kopabackgroundtool.so
%attr(755,root,root) %{_libdir}/kde4/krossmodulekplato.so
%attr(755,root,root) %{_libdir}/kde4/krossmodulekspread.so
%attr(755,root,root) %{_libdir}/kde4/krossmodulekword.so
%attr(755,root,root) %{_libdir}/kde4/libkspreadsolver.so
%attr(755,root,root) %{_libdir}/kde4/libFilterkpr2odf.so
%attr(755,root,root) %{_libdir}/kde4/libapplixspreadimport.so
%attr(755,root,root) %{_libdir}/kde4/libcsvexport.so
%attr(755,root,root) %{_libdir}/kde4/libcsvimport.so
%attr(755,root,root) %{_libdir}/kde4/libdbaseimport.so
%attr(755,root,root) %{_libdir}/kde4/libgnumericexport.so
%attr(755,root,root) %{_libdir}/kde4/libgnumericimport.so
%attr(755,root,root) %{_libdir}/kde4/libopencalcexport.so
%attr(755,root,root) %{_libdir}/kde4/libopencalcimport.so
%attr(755,root,root) %{_libdir}/kde4/libqproimport.so
%attr(755,root,root) %{_libdir}/kde4/libwpexport.so
%attr(755,root,root) %{_libdir}/kde4/libwpimport.so
%attr(755,root,root) %{_libdir}/kde4/libwpgimport.so
%attr(755,root,root) %{_libdir}/kde4/musicshape.so
%attr(755,root,root) %{_libdir}/kde4/pathshapes.so
%attr(755,root,root) %{_libdir}/kde4/pictureshape.so
%attr(755,root,root) %{_libdir}/kde4/spellcheck.so
%attr(755,root,root) %{_libdir}/kde4/spreadsheetshape.so
%attr(755,root,root) %{_libdir}/kde4/textshape.so
%attr(755,root,root) %{_libdir}/kde4/textvariables.so
%attr(755,root,root) %ghost %{_libdir}/libkokross.so.?
%attr(755,root,root) %{_libdir}/libkokross.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkoodf.so.?
%attr(755,root,root) %{_libdir}/libkoodf.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkostore.so.?
#%attr(755,root,root) %{_libdir}/libkostore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkomain.so.?
%attr(755,root,root) %{_libdir}/libkomain.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libflake.so.?
%attr(755,root,root) %{_libdir}/libflake.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkoresources.so.?
#%attr(755,root,root) %{_libdir}/libkoresources.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpigmentcms.so.?
%attr(755,root,root) %{_libdir}/libpigmentcms.so.*.*.*
%{_datadir}/kde4/services/Filterkpr2odf.desktop
%{_datadir}/kde4/services/artistictextshape.desktop
%{_datadir}/kde4/services/autocorrect.desktop
%{_datadir}/kde4/services/changecase.desktop
%{_datadir}/kde4/services/defaulttools.desktop
%{_datadir}/kde4/services/divineproportionshape.desktop
%{_datadir}/kde4/services/kopabackgroundtool.desktop
%{_datadir}/kde4/services/krossmodulekplato.desktop
%{_datadir}/kde4/services/krossmodulekspread.desktop
%{_datadir}/kde4/services/krossmodulekword.desktop
%{_datadir}/kde4/services/musicshape.desktop
%{_datadir}/kde4/services/pathshapes.desktop
%{_datadir}/kde4/services/pictureshape.desktop
%{_datadir}/kde4/services/spellcheck.desktop
%{_datadir}/kde4/services/textshape.desktop
%{_datadir}/kde4/services/textvariables.desktop
# these libs actually need to be here, to prevent LOOPS
%attr(755,root,root) %{_libdir}/libkarboncommon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkarboncommon.so.?
%attr(755,root,root) %ghost %{_libdir}/libkritaimage.so.?
%attr(755,root,root) %{_libdir}/libkritaimage.so.*.*.*
%attr(755,root,root) %{_libdir}/libkwordprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkwordprivate.so.?
%attr(755,root,root) %ghost %{_libdir}/libkritaui.so.?
%attr(755,root,root) %{_libdir}/libkritaui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkspreadcommon.so.?
%attr(755,root,root) %{_libdir}/libkspreadcommon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkplatokernel.so.?
%attr(755,root,root) %{_libdir}/libkplatokernel.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkplatomodels.so.?
%attr(755,root,root) %{_libdir}/libkplatomodels.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkplatoprivate.so.?
%attr(755,root,root) %{_libdir}/libkplatoprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkplatoui.so.?
%attr(755,root,root) %{_libdir}/libkplatoui.so.*.*.*

%files karbon
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/karbon
%attr(755,root,root) %{_libdir}/libkdeinit4_karbon.so
%attr(755,root,root) %{_libdir}/kde4/*karbon*.so
#%attr(755,root,root) %{_libdir}/kde4/*wmf*port.so
%{_datadir}/apps/karbon
%{_datadir}/config/karbonrc
%{_datadir}/kde4/services/karbon*
%{_datadir}/templates/.source/Illustration.karbon
%{_datadir}/templates/Illustration.desktop
%{_desktopdir}/kde4/karbon.desktop
%{_datadir}/kde4/services/ServiceMenus/karbon_konqi.desktop
#%{_iconsdir}/oxygen/*/apps/karbon.png
%{_kdedocdir}/en/karbon

%files kchart
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libkchartcommon.so.?
%attr(755,root,root) %{_libdir}/libkchartcommon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libchartshapelib.so.?
%attr(755,root,root) %{_libdir}/libchartshapelib.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/libkchart*.so
%attr(755,root,root) %{_libdir}/kde4/chartshape.so
%{_datadir}/apps/kchart
%{_datadir}/kde4/services/kchart*.desktop
%{_datadir}/kde4/services/chartshape.desktop
%{_datadir}/kde4/services/ServiceMenus/kchart_konqi.desktop
%{_iconsdir}/hicolor/*/apps/kchart.png
%{_kdedocdir}/en/kchart

%files kexi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kexi
%attr(755,root,root) %ghost %{_libdir}/libkexicore.so.?
%attr(755,root,root) %{_libdir}/libkexicore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkexidatatable.so.?
%attr(755,root,root) %{_libdir}/libkexidatatable.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkexidb.so.?
%attr(755,root,root) %{_libdir}/libkexidb.so.*.*.*
%attr(755,root,root) %{_libdir}/libkexiextendedwidgets.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkexiformutils.so.?
%attr(755,root,root) %{_libdir}/libkexiformutils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkexiguiutils.so.?
%attr(755,root,root) %{_libdir}/libkexiguiutils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkeximain.so.?
%attr(755,root,root) %{_libdir}/libkeximain.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkeximigrate.so.?
%attr(755,root,root) %{_libdir}/libkeximigrate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkexirelationsview.so.?
%attr(755,root,root) %{_libdir}/libkexirelationsview.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkexiutils.so.?
%attr(755,root,root) %{_libdir}/libkexiutils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkformdesigner.so.?
%attr(755,root,root) %{_libdir}/libkformdesigner.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/kexidb_mysqldriver.so
%attr(755,root,root) %{_libdir}/kde4/kexidb_sqlite3driver.so
%attr(755,root,root) %{_libdir}/kde4/kexidb_xbasedriver.so
%attr(755,root,root) %{_libdir}/kde4/kexihandler_csv_importexport.so
%attr(755,root,root) %{_libdir}/kde4/kexihandler_form.so
%attr(755,root,root) %{_libdir}/kde4/kexihandler_migration.so
%attr(755,root,root) %{_libdir}/kde4/kexihandler_query.so
%attr(755,root,root) %{_libdir}/kde4/kexihandler_report.so
%attr(755,root,root) %{_libdir}/kde4/kexihandler_script.so
%attr(755,root,root) %{_libdir}/kde4/kexihandler_table.so
%attr(755,root,root) %{_libdir}/kde4/keximigrate_kspread.so
%attr(755,root,root) %{_libdir}/kde4/keximigrate_mdb.so
%attr(755,root,root) %{_libdir}/kde4/keximigrate_mysql.so
%attr(755,root,root) %{_libdir}/kde4/keximigrate_txt.so
%attr(755,root,root) %{_libdir}/kde4/keximigrate_xbase.so
%attr(755,root,root) %{_libdir}/kde4/kexirelationdesignshape.so
%attr(755,root,root) %{_libdir}/kde4/kformdesigner_containers.so
%attr(755,root,root) %{_libdir}/kde4/kformdesigner_kexidbwidgets.so
%attr(755,root,root) %{_libdir}/kde4/kformdesigner_stdwidgets.so
%attr(755,root,root) %{_libdir}/kde4/krossmodulekexidb.so
%{_datadir}/applications/kde4/kexi.desktop
%{_datadir}/apps/kexi
%{_datadir}/config/kexirc
%dir %{_datadir}/kde4/services/kexi
%{_datadir}/kde4/services/kexi/kexicsv_importexporthandler.desktop
%{_datadir}/kde4/services/kexi/kexiformhandler.desktop
%{_datadir}/kde4/services/kexi/keximigrationhandler.desktop
%{_datadir}/kde4/services/kexi/kexiqueryhandler.desktop
%{_datadir}/kde4/services/kexi/kexireporthandler.desktop
%{_datadir}/kde4/services/kexi/kexiscripthandler.desktop
%{_datadir}/kde4/services/kexi/kexitablehandler.desktop
%{_datadir}/kde4/services/kexidb_mysqldriver.desktop
%{_datadir}/kde4/services/kexidb_sqlite3driver.desktop
%{_datadir}/kde4/services/kexidb_xbasedriver.desktop
%{_datadir}/kde4/services/keximigrate_kspread.desktop
%{_datadir}/kde4/services/keximigrate_mdb.desktop
%{_datadir}/kde4/services/keximigrate_mysql.desktop
%{_datadir}/kde4/services/keximigrate_txt.desktop
%{_datadir}/kde4/services/keximigrate_xbase.desktop
%{_datadir}/kde4/services/kexirelationdesignshape.desktop
%dir %{_datadir}/kde4/services/kformdesigner
%{_datadir}/kde4/services/kformdesigner/kformdesigner_containers.desktop
%{_datadir}/kde4/services/kformdesigner/kformdesigner_kexidbfactory.desktop
%{_datadir}/kde4/services/kformdesigner/kformdesigner_stdwidgets.desktop
%{_kdedocdir}/en/kexi

%files kformula
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kformula
#%attr(755,root,root) %{_libdir}/libkdeinit_kformula.so
%attr(755,root,root) %ghost %{_libdir}/libkformulalib.so.?
%attr(755,root,root) %{_libdir}/libkformulalib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkformulaprivate.so.?
%attr(755,root,root) %{_libdir}/libkformulaprivate.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/formulashape.so
%attr(755,root,root) %{_libdir}/kde4/libexcelimport.so
%attr(755,root,root) %{_libdir}/kde4/libkformulapart.so
%attr(755,root,root) %{_libdir}/kde4/libicalendarexport.so
%attr(755,root,root) %{_libdir}/kde4/libxlsximport.so
%attr(755,root,root) %{_libdir}/kde4/paragraphtool.so
%{_datadir}/kde4/services/ServiceMenus/kformula_konqi.desktop
%{_datadir}/kde4/services/formulashape.desktop
%{_datadir}/kde4/services/kformulapart.desktop
%{_datadir}/kde4/services/paragraphtool.desktop
%{_datadir}/apps/formulashape
%{_datadir}/apps/kformula
%{_desktopdir}/kde4/kformula.desktop
%{_kdedocdir}/en/kformula

%files kivio
%defattr(644,root,root,755)
%{_datadir}/kde4/services/ServiceMenus/kivio_konqi.desktop
#%{_iconsdir}/*/*/apps/kivio.png
#%{_kdedocdir}/en/kivio

%files kplato
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kplato
%attr(755,root,root) %{_bindir}/kplatowork
%attr(755,root,root) %{_libdir}/libkdeinit4_kplatowork.so
%attr(755,root,root) %ghost %{_libdir}/libkplatoworkapp.so.?
%attr(755,root,root) %{_libdir}/libkplatoworkapp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkplatoworkfactory.so.?
%attr(755,root,root) %{_libdir}/libkplatoworkfactory.so.*.*.*
%attr(755,root,root) %{_libdir}/libkdeinit4_kplato.so
%attr(755,root,root) %{_libdir}/kde4/libkplatopart.so
%attr(755,root,root) %{_libdir}/kde4/libkplatoworkpart.so
%{_desktopdir}/kde4/kplatowork.desktop
%{_datadir}/apps/kplato
%{_datadir}/apps/kplatowork
%{_datadir}/kde4/services/kplatopart.desktop
%{_datadir}/kde4/services/kplato_icalendar_export.desktop
%{_datadir}/kde4/services/kplatoworkpart.desktop
%{_desktopdir}/kde4/kplato.desktop
%{_datadir}/config/kplatorc
%{_datadir}/config.kcfg/kplatosettings.kcfg
%{_datadir}/config/kplatoworkrc
%{_iconsdir}/hicolor/*/apps/kplato.png
#%{_iconsdir}/hicolor/*/apps/kplato.svgz
%{_iconsdir}/hicolor/*/mimetypes/application-x-vnd.kde.kplato.png
#%{_iconsdir}/hicolor/*/mimetypes/application-x-vnd.kde.kplato.svgz
#%{_kdedocdir}/en/kplato

%files kpresenter
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpresenter
%attr(755,root,root) %{_libdir}/libkdeinit4_kpresenter.so
%attr(755,root,root) %{_libdir}/kde4/kpresenter*.so
%attr(755,root,root) %{_libdir}/kde4/libkpresenter*.so
%attr(755,root,root) %{_libdir}/kde4/libpptximport.so
%attr(755,root,root) %{_libdir}/kde4/libpowerpointimport.so
%attr(755,root,root) %{_libdir}/kde4/kpr_pageeffect_barwipe.so
%attr(755,root,root) %{_libdir}/kde4/kpr_pageeffect_clockwipe.so
%attr(755,root,root) %{_libdir}/kde4/kpr_pageeffect_edgewipe.so
%attr(755,root,root) %{_libdir}/kde4/kpr_pageeffect_iriswipe.so
%attr(755,root,root) %{_libdir}/kde4/kpr_pageeffect_matrixwipe.so
%attr(755,root,root) %{_libdir}/kde4/kpr_pageeffect_slidewipe.so
%attr(755,root,root) %{_libdir}/kde4/kpr_shapeanimation_example.so
%{_datadir}/apps/kpresenter
%{_datadir}/config/kpresenterrc
%{_datadir}/kde4/services/ServiceMenus/kpresenter_konqi.desktop
%{_datadir}/templates/.source/Presentation.kpt
%{_datadir}/templates/Presentation.desktop
%{_datadir}/kde4/services/kpresenter*.desktop
%{_datadir}/kde4/services/kpr_pageeffect_barwipe.desktop
%{_datadir}/kde4/services/kpr_pageeffect_clockwipe.desktop
%{_datadir}/kde4/services/kpr_pageeffect_edgewipe.desktop
%{_datadir}/kde4/services/kpr_pageeffect_iriswipe.desktop
%{_datadir}/kde4/services/kpr_pageeffect_matrixwipe.desktop
%{_datadir}/kde4/services/kpr_pageeffect_slidewipe.desktop
%{_datadir}/kde4/services/kpr_shapeanimation_example.desktop
%{_desktopdir}/kde4/kpresenter.desktop
%{_iconsdir}/hicolor/*/apps/kpresenter.png
%{_kdedocdir}/en/kpresenter

%files krita
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/krita
%attr(755,root,root) %{_libdir}/libkdeinit4_krita.so
#%attr(755,root,root) %ghost %{_libdir}/libKritaRulerAssistantCommon.so.?
#%attr(755,root,root) %{_libdir}/libKritaRulerAssistantCommon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkritalibbrush.so.?
%attr(755,root,root) %{_libdir}/libkritalibbrush.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkrita_xyz_u16.so.?
#%attr(755,root,root) %{_libdir}/libkrita_xyz_u16.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkritagrayscale.so.?
#%attr(755,root,root) %{_libdir}/libkritagrayscale.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkritalibpaintop.so.?
%attr(755,root,root) %{_libdir}/libkritalibpaintop.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkrossmodulekrita.so.?
%attr(755,root,root) %{_libdir}/libkrossmodulekrita.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkritabasicdynamiccoloringprogram.so.?
#%attr(755,root,root) %{_libdir}/libkritabasicdynamiccoloringprogram.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkritabasicdynamicshapeprogram.so.?
#%attr(755,root,root) %{_libdir}/libkritabasicdynamicshapeprogram.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkritadynamicbrush.so.?
#%attr(755,root,root) %{_libdir}/libkritadynamicbrush.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/krita*.so
%attr(755,root,root) %{_libdir}/kde4/libkritabmpexport.so
#%attr(755,root,root) %{_libdir}/kde4/libkritagmagickexport.so
#%attr(755,root,root) %{_libdir}/kde4/libkritagmagickimport.so
%attr(755,root,root) %{_libdir}/kde4/libkritajpegexport.so
%attr(755,root,root) %{_libdir}/kde4/libkritajpegimport.so
%attr(755,root,root) %{_libdir}/kde4/libkritaoraexport.so
%attr(755,root,root) %{_libdir}/kde4/libkritaoraimport.so
%attr(755,root,root) %{_libdir}/kde4/libkritapart.so
%attr(755,root,root) %{_libdir}/kde4/libkritapngexport.so
%attr(755,root,root) %{_libdir}/kde4/libkritapngimport.so
%attr(755,root,root) %{_libdir}/kde4/libkritatiffexport.so
%attr(755,root,root) %{_libdir}/kde4/libkritatiffimport.so
%attr(755,root,root) %{_libdir}/kde4/libkrita_raw_import.so
%attr(755,root,root) %{_libdir}/kde4/libkritabmpimport.so
%attr(755,root,root) %{_libdir}/kde4/libkritagifimport.so
%attr(755,root,root) %{_libdir}/kde4/libkritappmexport.so
%attr(755,root,root) %{_libdir}/kde4/libkritappmimport.so
%attr(755,root,root) %{_libdir}/kde4/libkritapsdimport.so
%attr(755,root,root) %{_libdir}/kde4/libkritaxcfimport.so
%if %{with pdf}
%attr(755,root,root) %{_libdir}/kde4/libkritapdfimport.so
%{_desktopdir}/kde4/krita_pdf.desktop
%endif
%{_desktopdir}/kde4/krita_raw.desktop
%{_datadir}/kde4/services/ServiceMenus/krita_konqi.desktop
%{_datadir}/apps/krita
%{_datadir}/apps/kritaplugins
%{_datadir}/applications/kde4/krita_gif.desktop
%{_datadir}/applications/kde4/krita_ppm.desktop
%{_datadir}/applications/kde4/krita_xcf.desktop
%{_desktopdir}/kde4/krita.desktop
%{_desktopdir}/kde4/krita_bmp.desktop
%{_desktopdir}/kde4/krita_jpeg.desktop
#%{_desktopdir}/kde4/krita_magick.desktop
%{_desktopdir}/kde4/krita_ora.desktop
%{_desktopdir}/kde4/krita_png.desktop
%{_desktopdir}/kde4/krita_tiff.desktop
%{_datadir}/config/kritarc
%{_datadir}/color/icc/krita
%{_datadir}/kde4/services/krita*.desktop
%{_datadir}/templates/Illustration.desktop
%{_datadir}/mime/packages/krita_ora.xml
%{_iconsdir}/hicolor/*/apps/krita.png
#%{_kdedocdir}/en/krita

%files kspread
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kspread
%attr(755,root,root) %{_libdir}/libkdeinit4_kspread.so
%attr(755,root,root) %{_libdir}/kde4/kspread_plugin_tool_calendar.so
%attr(755,root,root) %{_libdir}/kde4/kspreadbitopsmodule.so
%attr(755,root,root) %{_libdir}/kde4/kspreadconversionmodule.so
%attr(755,root,root) %{_libdir}/kde4/kspreaddatabasemodule.so
%attr(755,root,root) %{_libdir}/kde4/kspreaddatetimemodule.so
%attr(755,root,root) %{_libdir}/kde4/kspreadengineeringmodule.so
%attr(755,root,root) %{_libdir}/kde4/kspreadfinancialmodule.so
%attr(755,root,root) %{_libdir}/kde4/kspreadinformationmodule.so
%attr(755,root,root) %{_libdir}/kde4/kspreadlogicmodule.so
%attr(755,root,root) %{_libdir}/kde4/kspreadmathmodule.so
%attr(755,root,root) %{_libdir}/kde4/kspreadreferencemodule.so
%attr(755,root,root) %{_libdir}/kde4/kspreadstatisticalmodule.so
%attr(755,root,root) %{_libdir}/kde4/kspreadtextmodule.so
%attr(755,root,root) %{_libdir}/kde4/kspreadtrigonometrymodule.so
%attr(755,root,root) %{_libdir}/kde4/libkspreadhtmlexport.so
%attr(755,root,root) %{_libdir}/kde4/libkspreadhtmlimport.so
%attr(755,root,root) %{_libdir}/kde4/libkspreadlatexexport.so
%attr(755,root,root) %{_libdir}/kde4/libkspreadpart.so
%attr(755,root,root) %{_libdir}/kde4/spreadsheetshape.so
%{_datadir}/apps/kspread
%{_desktopdir}/kde4/kspread.desktop
%{_datadir}/kde4/services/ServiceMenus/kspread_konqi.desktop
%{_datadir}/templates/.source/SpreadSheet.kst
%{_datadir}/templates/SpreadSheet.desktop
%{_datadir}/kde4/services/kspread*.desktop
%{_datadir}/kde4/services/spreadsheetshape.desktop
%{_datadir}/config/kspreadrc
%{_datadir}/config.kcfg/kspread.kcfg
%{_iconsdir}/hicolor/*/apps/kspread.png
%{_kdedocdir}/en/kspread

%files kword
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kthesaurus
%attr(755,root,root) %{_bindir}/kword
%attr(755,root,root) %{_libdir}/libkdeinit4_kword.so
%attr(755,root,root) %{_libdir}/libkword*export*.so
%attr(755,root,root) %ghost %{_libdir}/libkwordexportfilters.so.?
%attr(755,root,root) %{_libdir}/libkdeinit4_kthesaurus.so
%attr(755,root,root) %{_libdir}/kde4/libabiword*port.so
%attr(755,root,root) %{_libdir}/kde4/libdocximport.so
%attr(755,root,root) %{_libdir}/kde4/libhancomwordimport.so
%attr(755,root,root) %{_libdir}/kde4/libapplixwordimport.so
%attr(755,root,root) %{_libdir}/kde4/libascii*port.so
%attr(755,root,root) %{_libdir}/kde4/libdocbookexport.so
%attr(755,root,root) %{_libdir}/kde4/libhtml*port.so
%attr(755,root,root) %{_libdir}/kde4/libpalmdoc*port.so
%attr(755,root,root) %{_libdir}/kde4/libamipro*port.so
%attr(755,root,root) %{_libdir}/kde4/libwm*port.so
%attr(755,root,root) %{_libdir}/kde4/librtf*port.so
%attr(755,root,root) %{_libdir}/kde4/thesaurustool.so
#%attr(755,root,root) %{_libdir}/kde4/libmswrite*port.so
%attr(755,root,root) %{_libdir}/kde4/libmswordodf_import.so
%attr(755,root,root) %{_libdir}/kde4/libkword*.so
%attr(755,root,root) %{_libdir}/kde4/liboowriter*port.so
%{_datadir}/apps/kword
%dir %{_datadir}/apps/xsltfilter
%dir %{_datadir}/apps/xsltfilter/export
%dir %{_datadir}/apps/xsltfilter/export/kword
%dir %{_datadir}/apps/xsltfilter/export/kword/xslfo
%{_datadir}/apps/xsltfilter/export/kword/xslfo/*.xsl
%{_datadir}/config/kwordrc
%{_datadir}/kde4/services/ServiceMenus/kword_konqi.desktop
%{_datadir}/kde4/services/kword*.desktop
%{_datadir}/kde4/services/thesaurustool.desktop
# this is the mailmerge service info for qtsqldb and classic
%{_datadir}/templates/.source/TextDocument.kwt
%{_datadir}/templates/TextDocument.desktop
%{_desktopdir}/kde4/KThesaurus.desktop
%{_desktopdir}/kde4/kword.desktop
%{_iconsdir}/hicolor/*/apps/kword.png
#%{_kdedocdir}/en/kword
%{_kdedocdir}/en/thesaurus

%files devel
%defattr(644,root,root,755)
%exclude %{_libdir}/libkdeinit4_*.so
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
%{_includedir}/changetracker
%{_includedir}/kexi
%{_includedir}/styles
%{_datadir}/apps/cmake/modules/FindKOfficeLibs.cmake
