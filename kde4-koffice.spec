# TODO
# -- The following OPTIONAL packages could NOT be located on your system.
# -- Consider installing them to enable more features from this software.
# + Eigen2, 2.0 or higher: Eigen2 is needed by KSpread and Krita. They won't be built. <Module in kdesupport>
# + OpenCTL, 0.9.2 or higher: OpenCTL is needed for some color spaces (High Dynamic Range Color Spaces, YCbCr and LMS) <http://www.openctl.org>
# + Spnav: Spnav is the library which is required by the space navigator device plugin <http://spacenav.sourceforge.net/>
# + pstoedit: The Karbon eps import filter will not be built. <http://www.pstoedit.net/>
#
# And files:
#   /usr/lib64/kde4/artistictextshape.so
#   /usr/lib64/kde4/autocorrect.so
#   /usr/lib64/kde4/changecase.so
#   /usr/lib64/kde4/defaulttools.so
#   /usr/lib64/kde4/divineproportionshape.so
#   /usr/lib64/kde4/kopabackgroundtool.so
#   /usr/lib64/kde4/krossmodulekplato.so
#   /usr/lib64/kde4/krossmodulekword.so
#   /usr/lib64/kde4/libFilterkpr2odf.so
#   /usr/lib64/kde4/musicshape.so
#   /usr/lib64/kde4/pathshapes.so
#   /usr/lib64/kde4/pictureshape.so
#   /usr/lib64/kde4/spellcheck.so
#   /usr/lib64/kde4/textshape.so
#   /usr/lib64/kde4/textvariables.so
#   /usr/lib64/libflake.so.5
#   /usr/lib64/libflake.so.5.0.0
#   /usr/lib64/libkoguiutils.so.5
#   /usr/lib64/libkoguiutils.so.5.0.0
#   /usr/lib64/libkokross.so.5
#   /usr/lib64/libkokross.so.5.0.0
#   /usr/lib64/libkomain.so.5
#   /usr/lib64/libkomain.so.5.0.0
#   /usr/lib64/libkoodf.so.5
#   /usr/lib64/libkoodf.so.5.0.0
#   /usr/lib64/libkoresources.so.5
#   /usr/lib64/libkoresources.so.5.0.0
#   /usr/lib64/libkostore.so.5
#   /usr/lib64/libkostore.so.5.0.0
#   /usr/lib64/libpigmentcms.so.5
#   /usr/lib64/libpigmentcms.so.5.0.0
#   /usr/share/apps/musicshape/fonts/Emmentaler-14.ttf
#   /usr/share/color/icc/pigment/CMY.icm
#   /usr/share/color/icc/pigment/cmyk.icm
#   /usr/share/icons/hicolor/128x128/apps/kplato.png
#   /usr/share/icons/hicolor/128x128/mimetypes/application-x-vnd.kde.kplato.png
#   /usr/share/icons/hicolor/16x16/apps/kchart.png
#   /usr/share/icons/hicolor/16x16/apps/kplato.png
#   /usr/share/icons/hicolor/16x16/apps/kpresenter.png
#   /usr/share/icons/hicolor/16x16/mimetypes/application-x-vnd.kde.kplato.png
#   /usr/share/icons/hicolor/22x22/apps/kplato.png
#   /usr/share/icons/hicolor/22x22/apps/kpresenter.png
#   /usr/share/icons/hicolor/22x22/mimetypes/application-x-vnd.kde.kplato.png
#   /usr/share/icons/hicolor/32x32/apps/kchart.png
#   /usr/share/icons/hicolor/32x32/apps/kplato.png
#   /usr/share/icons/hicolor/32x32/apps/kpresenter.png
#   /usr/share/icons/hicolor/32x32/mimetypes/application-x-vnd.kde.kplato.png
#   /usr/share/icons/hicolor/48x48/apps/kchart.png
#   /usr/share/icons/hicolor/48x48/apps/kplato.png
#   /usr/share/icons/hicolor/48x48/apps/kpresenter.png
#   /usr/share/icons/hicolor/48x48/mimetypes/application-x-vnd.kde.kplato.png
#   /usr/share/icons/hicolor/64x64/apps/kplato.png
#   /usr/share/icons/hicolor/64x64/mimetypes/application-x-vnd.kde.kplato.png
#   /usr/share/icons/hicolor/scalable/apps/kplato.svgz
#   /usr/share/icons/hicolor/scalable/mimetypes/application-x-vnd.kde.kplato.svgz
#   /usr/share/icons/oxygen/scalable/actions/shape-choose.svgz
#   /usr/share/icons/oxygen/scalable/actions/table.svgz
#   /usr/share/kde4/services/Filterkpr2odf.desktop
#   /usr/share/kde4/services/artistictextshape.desktop
#   /usr/share/kde4/services/autocorrect.desktop
#   /usr/share/kde4/services/changecase.desktop
#   /usr/share/kde4/services/defaulttools.desktop
#   /usr/share/kde4/services/divineproportionshape.desktop
#   /usr/share/kde4/services/kopabackgroundtool.desktop
#   /usr/share/kde4/services/krossmodulekplato.desktop
#   /usr/share/kde4/services/krossmodulekword.desktop
#   /usr/share/kde4/services/musicshape.desktop
#   /usr/share/kde4/services/pathshapes.desktop
#   /usr/share/kde4/services/pictureshape.desktop
#   /usr/share/kde4/services/spellcheck.desktop
#   /usr/share/kde4/services/textshape.desktop
#   /usr/share/kde4/services/textvariables.desktop


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
Version:	1.9.98.6
Release:	0.1
License:	GPL/LGPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{origname}-%{version}/src/%{origname}-%{version}.tar.bz2
# Source0-md5:	00a4a0e9e0cfa60bf02a917e2267948c
Patch0:		%{name}-thumbnail.patch
URL:		http://www.koffice.org/
BuildRequires:	GraphicsMagick-devel
BuildRequires:	OpenEXR-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.6.2
BuildRequires:	eigen >= 2.0
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
Requires:	kdebase-core >= 9:3.2.0

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

%package kformula
Summary:        KOffice - kformula
Summary(pl.UTF-8):      KOffice - kformula
Group:          X11/Applications
Requires:       %{name}-common = %{version}-%{release}

%description kformula
KFormula is KOffice part for creating formulas, equations, etc...

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

%post	kplato -p /sbin/ldconfig
%postun	kplato -p /sbin/ldconfig

%post	kpresenter -p /sbin/ldconfig
%postun	kpresenter -p /sbin/ldconfig

%post   kword -p /sbin/ldconfig
%postun kword -p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%exclude %{_libdir}/libkdeinit4_*.so
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
%{_datadir}/apps/cmake/modules/FindKOfficeLibs.cmake

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
%attr(755,root,root) %{_libdir}/kde4/koffice_graya_u16_plugin.so
%attr(755,root,root) %{_libdir}/kde4/kofficedockers.so
%attr(755,root,root) %{_libdir}/kde4/kofficegrayau8plugin.so
%attr(755,root,root) %{_libdir}/kde4/kofficesimpletextedit.so
%{_datadir}/apps/koffice
%{_datadir}/kde4/services/clipartthumbnail.desktop
%{_datadir}/kde4/services/kodocinfopropspage.desktop
%{_datadir}/kde4/services/kofficethumbnail.desktop
%{_datadir}/kde4/services/koffice_graya_u16_plugin.desktop
%{_datadir}/kde4/services/kofficedockers.desktop
%{_datadir}/kde4/services/kofficegrayaplugin.desktop
%{_datadir}/kde4/services/kofficesimpletextedit.desktop
%{_datadir}/kde4/services/kounavail.desktop
%{_datadir}/kde4/services/xslt_*.desktop
%{_datadir}/kde4/services/generic_filter.desktop
%{_datadir}/kde4/servicetypes/*
%dir %{_datadir}/templates/.source
%{_desktopdir}/kde4/koffice.desktop
%{_iconsdir}/oxygen/*/actions/*.png
%{_kdedocdir}/en/koffice

%files karbon
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/karbon
%attr(755,root,root) %{_libdir}/libkarboncommon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkarboncommon.so.?
%attr(755,root,root) %{_libdir}/libkarbonui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkarbonui.so.?
%attr(755,root,root) %{_libdir}/libkdeinit4_karbon.so
%attr(755,root,root) %{_libdir}/kde4/*karbon*.so
%attr(755,root,root) %{_libdir}/kde4/*wmf*port.so
%{_datadir}/apps/karbon
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
#%{_iconsdir}/*/*x*/apps/kchart.png
%{_kdedocdir}/en/kchart

%files kformula
%defattr(644,root,root,755)
%{_datadir}/kde4/services/ServiceMenus/kformula_konqi.desktop
%{_kdedocdir}/en/kformula

%files kivio
%defattr(644,root,root,755)
%{_datadir}/kde4/services/ServiceMenus/kivio_konqi.desktop
#%{_iconsdir}/*/*/apps/kivio.png
%{_kdedocdir}/en/kivio

%files kplato
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kplato
%attr(755,root,root) %{_libdir}/libkdeinit4_kplato.so
%attr(755,root,root) %ghost %{_libdir}/libkplatokernel.so.?
%attr(755,root,root) %{_libdir}/libkplatokernel.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkplatomodels.so.?
%attr(755,root,root) %{_libdir}/libkplatomodels.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkplatoprivate.so.?
%attr(755,root,root) %{_libdir}/libkplatoprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkplatoui.so.?
%attr(755,root,root) %{_libdir}/libkplatoui.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/libkplatopart.so
%{_datadir}/apps/kplato
%{_datadir}/kde4/services/kplatopart.desktop
%{_desktopdir}/kde4/kplato.desktop
%{_datadir}/config/kplatorc
#%{_iconsdir}/oxygen/*/apps/kplato.*
%{_kdedocdir}/en/kplato

%files kpresenter
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpresenter
%attr(755,root,root) %{_libdir}/libkpresenterprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkpresenterprivate.so.?
%attr(755,root,root) %{_libdir}/libkdeinit4_kpresenter.so
%attr(755,root,root) %{_libdir}/kde4/kpresenter*.so
%attr(755,root,root) %{_libdir}/kde4/libkpresenter*.so
%attr(755,root,root) %{_libdir}/kde4/libpowerpointimport.so
%attr(755,root,root) %{_libdir}/kde4/kpr_pageeffect_barwipe.so
%attr(755,root,root) %{_libdir}/kde4/kpr_pageeffect_clockwipe.so
%attr(755,root,root) %{_libdir}/kde4/kpr_pageeffect_edgewipe.so
%attr(755,root,root) %{_libdir}/kde4/kpr_pageeffect_iriswipe.so
%attr(755,root,root) %{_libdir}/kde4/kpr_pageeffect_matrixwipe.so
%attr(755,root,root) %{_libdir}/kde4/kpr_pageeffect_slidewipe.so
%attr(755,root,root) %{_libdir}/kde4/kpr_shapeanimation_example.so
%{_datadir}/apps/kpresenter
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
#%{_iconsdir}/*/*/apps/kpresenter*.png
%{_kdedocdir}/en/kpresenter

%files krita
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/krita_cmyk_u16_plugin.so
%attr(755,root,root) %{_libdir}/kde4/kritacmykplugin.so
%{_datadir}/kde4/services/ServiceMenus/krita_konqi.desktop
%{_datadir}/apps/krita
%{_datadir}/kde4/services/krita*.desktop
%{_datadir}/templates/Illustration.desktop
#%{_kdedocdir}/en/krita

#%files kross-python
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/krosspython.so
#%{_libdir}/kde4/krosspython.la
#%{_datadir}/apps/kross/python
#
#%files kross-ruby
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/krossruby.so
#%{_libdir}/kde4/krossruby.la

%files kspread
%defattr(644,root,root,755)
%{_datadir}/kde4/services/ServiceMenus/kspread_konqi.desktop
%{_datadir}/templates/.source/SpreadSheet.kst
%{_datadir}/templates/SpreadSheet.desktop

%files kword
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kthesaurus
%attr(755,root,root) %{_bindir}/kword
%attr(755,root,root) %{_libdir}/libkdeinit4_kword.so
%attr(755,root,root) %{_libdir}/libkwordprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkwordprivate.so.?
%attr(755,root,root) %{_libdir}/libkword*export*.so
%attr(755,root,root) %ghost %{_libdir}/libkwordexportfilters.so.?
%attr(755,root,root) %{_libdir}/libkdeinit4_kthesaurus.so
%attr(755,root,root) %{_libdir}/kde4/libabiword*port.so
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
%attr(755,root,root) %{_libdir}/kde4/libmswrite*port.so
%attr(755,root,root) %{_libdir}/kde4/libkword*.so
%attr(755,root,root) %{_libdir}/kde4/liboowriter*port.so
%{_datadir}/apps/kword
%dir %{_datadir}/apps/xsltfilter
%dir %{_datadir}/apps/xsltfilter/export
%dir %{_datadir}/apps/xsltfilter/export/kword
%dir %{_datadir}/apps/xsltfilter/export/kword/xslfo
%{_datadir}/apps/xsltfilter/export/kword/xslfo/*.xsl
%{_datadir}/kde4/services/ServiceMenus/kword_konqi.desktop
%{_datadir}/kde4/services/kword*.desktop
%{_datadir}/kde4/services/thesaurustool.desktop
# this is the mailmerge service info for qtsqldb and classic
%{_datadir}/templates/.source/TextDocument.kwt
%{_datadir}/templates/TextDocument.desktop
%{_desktopdir}/kde4/KThesaurus.desktop
%{_desktopdir}/kde4/kword.desktop
%{_iconsdir}/*/*/apps/kword.png
%{_kdedocdir}/en/kword
%{_kdedocdir}/en/thesaurus
