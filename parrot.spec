# TODO, finish %files (especially docs to man conversion)
# builds here but i didnt tested it yet..
# some work around packages splitting could be done too
Summary:	A virtual machine designed to execute bytecode for interpreted languages
Summary(pl):	Maszyna wirtualna przeznaczona do wykonywania bytecodu dla jêzyków interpretowanych
Name:		parrot
Version:	0.4.2
Release:	0.1
Epoch:		0
License:	GPL v2/Artistic
Group:		Libraries
Source0:	ftp://ftp.cpan.org/pub/CPAN/authors/id/L/LT/LTOETSCH/%{name}-%{version}.tar.gz
# Source0-md5:	f596a8eca0727887ce8e866950573dd7
BuildRequires:	perl-devel
URL:		http://www.parrotcode.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parrot is a virtual machine designed to execute bytecode for
interpreted languages efficiently. Parrot will be the target for the
Perl 6 compiler. There is already a partial Perl 6 compiler as well as
compilers in various stages of completion for a wide range of other
languages.

%description -l pl
Parrot to maszyna wirtualna zaprojektowana do wydajnego wykonywania
bytecodu dla jêzyków interpretowanych. Parrot bêdzie celem kompilatora
Perla 6. Istnieje ju¿ czê¶ciowy kompilator Perla 6, a tak¿e
kompilatory w ró¿nych stopniach zaawansowania dla szerokiego zakresu
innych jêzyków.

%package devel
Summary:	Header files for parrot
Summary(pl):	Pliki nag³ówkowe biblioteki parrot
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for parrot.

%description devel -l pl
Pliki nag³ówkowe biblioteki parrot.

%package static
Summary:	Static parrot library
Summary(pl):	Statyczna biblioteka parrot
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static parrot library.

%description static -l pl
Statyczna biblioteka parrot.

%package basic
Summary:	BASIC language
Summary(pl):	Jêzyk BASIC
Group:		Development/Languages

%description basic
BASIC language.

%description basic -l pl
Jêzyk BASIC.

%package befunge
Summary:	Befunge language
Summary(pl):	Jêzyk Befunge
Group:		Development/Languages

%description befunge
Befunge language.

%description befunge -l pl
Jêzyk Befunge

%package bf
Summary:	bf language
Summary(pl):	Jêzyk bf
Group:		Development/Languages

%description bf
bf language.

%description bf -l pl
Jêzyk bf.

%package cola
Summary:	cola language
Summary(pl):	Jêzyk cola
Group:		Development/Languages

%description cola
cola language.

%description cola -l pl
Jêzyk cola.

%package forth
Summary:	Forth language
Summary(pl):	Jêzyk Forth
Group:		Development/Languages

%description forth
Forth language.

%description forth -l pl
Jêzyk Forth.

%package jako
Summary:	jako language
Summary(pl):	Jêzyk jako
Group:		Development/Languages

%description jako
jako language.

%description jako -l pl
Jêzyk jako.

%package ook
Summary:	ook language
Summary(pl):	Jêzyk ook
Group:		Development/Languages

%description ook
ook language.

%description ook -l pl
Jêzyk ook.

%package perl6
Summary:	Perl 6 language
Summary(pl):	Jêzyk Perl 6
Group:		Development/Languages

%description perl6
Perl 6 language.

%description perl6 -l pl
Jêzyk Perl 6.

%package regex
Summary:	regex language
Summary(pl):	Jêzyk regex
Group:		Development/Languages

%description regex
regex language.

%description regex -l pl
Jêzyk regex.

%package ruby
Summary:	Ruby language
Summary(pl):	Jêzyk Ruby
Group:		Development/Languages

%description ruby
Ruby language.

%description ruby -l pl
Jêzyk Ruby.

%package scheme
Summary:	Scheme language
Summary(pl):	Jêzyk Scheme
Group:		Development/Languages

%description scheme
Scheme language.

%description scheme -l pl
Jêzyk Scheme.

%prep
%setup -q

%build
%{__perl} Configure.pl \
	--optimize
%{__make} parrot pdb pdump \
	CC="%{__cc}"
%{__perl} tools/dev/mk_manifests.pl \
	--prefix=%{_prefix} \
	--exec-prefix=%{_exec_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--includedir=%{_includedir} \
	MANIFEST

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

	#BINDIR=%{_bindir} \
	#LIBDIR=%{_libdir} \
	#INCLUDEDIR=%{_includedir} \

%{__make} install \
	PREFIX=%{_prefix} \
	EXEC_PREFIX=%{_exec_prefix} \
	BIN_DIR=%{_bindir} \
	LIB_DIR=%{_libdir} \
	INCLUDE_DIR=%{_includedir} \
	DOC_DIR=%{_datadir} \
	DESTDIR=$RPM_BUILD_ROOT 

install -d $RPM_BUILD_ROOT%{_examplesdir}
mv $RPM_BUILD_ROOT%{_datadir}/examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

#mv $RPM_BUILD_ROOT%{_datadir}/docs $RPM_BUILD_ROOT/tmp-doc-dir
#install -d $RPM_BUILD_ROOT%{_docdir}
#mv $RPM_BUILD_ROOT/tmp-doc-dir $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
#mv -v $RPM_BUILD_ROOT%{_datadir}/LICENSES/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/
#rmdir -v $RPM_BUILD_ROOT%{_datadir}/LICENSES
#mv -v $RPM_BUILD_ROOT%{_datadir}/RESPONSIBLE_PARTIES $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/
#mv -v $RPM_BUILD_ROOT%{_datadir}/TODO $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/


%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ABI_CHANGES CREDITS ChangeLog README 
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/parrot
%dir %{_libdir}/parrot/dynext
%attr(755,root,root) %{_libdir}/parrot/dynext/*.so
%{_libdir}/parrot/library/*.pir
%{_libdir}/parrot/library/*.pbc
%{_libdir}/parrot/library/*.pasm
%{_libdir}/parrot/library/*.declarations
%dir %{_libdir}/parrot/library
%dir %{_libdir}/parrot/library/Data
%dir %{_libdir}/parrot/library/Data/Dumper
%dir %{_libdir}/parrot/library/Digest
%dir %{_libdir}/parrot/library/File
%dir %{_libdir}/parrot/library/File/Spec
%dir %{_libdir}/parrot/library/Getopt
%dir %{_libdir}/parrot/library/JSON
%dir %{_libdir}/parrot/library/PGE
%dir %{_libdir}/parrot/library/SDL
%dir %{_libdir}/parrot/library/Stream
%dir %{_libdir}/parrot/library/Test
%dir %{_libdir}/parrot/library/Test/Builder
%dir %{_libdir}/parrot/library/YAML
%dir %{_libdir}/parrot/library/YAML/Parser

%{_libdir}/parrot/library/Data/*.pir
%{_libdir}/parrot/library/Data/*.pbc
%{_libdir}/parrot/library/Data/Dumper/*.pir
%{_libdir}/parrot/library/Data/Dumper/*.pbc
%{_libdir}/parrot/library/Digest/MD5.pir
%{_libdir}/parrot/library/File/Spec.pir
%{_libdir}/parrot/library/File/Spec/*.pir
%{_libdir}/parrot/library/Getopt/*.pir
%{_libdir}/parrot/library/Getopt/*.pbc
%{_libdir}/parrot/library/JSON/*.pir
%{_libdir}/parrot/library/PGE/*.pir
%{_libdir}/parrot/library/SDL/*.pir
%{_libdir}/parrot/library/SDL/*.png
%{_libdir}/parrot/library/Stream/*.pir
%{_libdir}/parrot/library/Stream/*.pbc
%{_libdir}/parrot/library/Test/*.pir
%{_libdir}/parrot/library/Test/Builder/*.pir
%{_libdir}/parrot/library/YAML/Parser/*.pir

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%dir %{_includedir}/%{name}
%dir %{_includedir}/%{name}/oplib
%dir %{_libdir}/parrot/include
%{_libdir}/parrot/include/*
%{_includedir}/%{name}/*.h
%{_includedir}/%{name}/oplib/*.h
#%{_mandir}/man?/*
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
