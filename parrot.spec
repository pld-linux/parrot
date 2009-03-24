# TODO:	finish %files (especially docs to man conversion)
#	html docs
# 	builds here (and here) but i didnt tested it yet..
# 	some work around packages splitting could be done too
#	"*** [PGE.pbc] Segmentation fault" on carme-i686 but on carme (x86_64, th) builds fine
#	builds fine on privete th i686 and x86_64 builder machines
#	consider BR: OpenGL-glut-devel (freeglut-devel or glut-devel) but this will add some libX11 deps
#	make tests with Rakudo (perl6) - looks ok (on the parrot builder machine)
#	somwhere there is a build path hardcoded in the parrot configuration!!!
#	check BR
#	clean pir/pbc stuff
#	raw pod docs
#
Summary:	A virtual machine designed to execute bytecode for interpreted languages
Summary(pl.UTF-8):Maszyna wirtualna przeznaczona do wykonywania bytecodu dla języków interpretowanych
Name:		parrot
Version:	1.0.0
Release:	0.2
License:	GPL v2/Artistic
Group:		Libraries
Source0:	ftp://ftp.parrot.org/pub/parrot/releases/stable/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	649ce1fb7c0edaf89dc1cd52ff267b1a
URL:		http://www.parrot.org/
BuildRequires:	perl-Storable
BuildRequires:	perl-devel
#Test::More
BuildRequires:	perl-Test-Simple
#Test::Harness
BuildRequires:	perl-Test-Harness
#MIME::Base64
BuildRequires:	perl-MIME-Base64
#URI
BuildRequires:	perl-URI
#Scalar::Util 1.07
BuildRequires:	perl-Scalar-List-Utils >= 1.07
#MKDoc::XML 0.72
BuildRequires:	perl-MKDoc-XML >= 0.72
#Digest::MD5
BuildRequires:	perl-Digest-MD5
#Petal
BuildRequires:	perl-Petal
#Date::Format 0.01
BuildRequires:	perl-TimeDate >= 0.01
#Petal::Utils
BuildRequires:	perl-Petal-Utils
#Method::Alias
#TODO
#Test::TAP::Model
#TODO
#Test::TAP::HTMLMatrix
#TODO
#IO::Uncompress::Base
#IO::Compress::Base
#IO::Compress::Base::Common
BuildRequires:	perl-IO-Compress-Base
#Compress::Raw::Zlib
#IO::Uncompress::Gunzip
#IO::Compress::Gzip
#IO::Compress::Gzip::Constants
BuildRequires:	perl-IO-Compress-Zlib
#Compress::Zlib
BuildRequires:	perl-Compress-Zlib
#HTML::Tagset 3
BuildRequires:	perl-HTML-Tagset >= 3
#HTML::Parser
BuildRequires:	perl-HTML-Parser
#LWP
BuildRequires:	perl-libwww
# ICU - Unicode stuff
BuildRequires:	libicu-devel
# OpenGL bindings
BuildRequires:	OpenGL-glut-devel
# lex and yacc - not sure do we need them
BuildRequires:	byacc
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parrot is a virtual machine designed to execute bytecode for
interpreted languages efficiently. Parrot will be the target for the
Perl 6 compiler. There is already a partial Perl 6 compiler as well as
compilers in various stages of completion for a wide range of other
languages.

%description -l pl.UTF-8
Parrot to maszyna wirtualna zaprojektowana do wydajnego wykonywania
bytecodu dla języków interpretowanych. Parrot będzie celem
kompilatora Perla 6. Istnieje już częściowy kompilator Perla 6, a
także kompilatory w różnych stopniach zaawansowania dla szerokiego
zakresu innych języków.

%package devel
Summary:	Header files for parrot
Summary(pl.UTF-8):Pliki nagłówkowe biblioteki parrot
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for parrot.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki parrot.

%package static
Summary:	Static parrot library
Summary(pl.UTF-8):Statyczna biblioteka parrot
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static parrot library.

%description static -l pl.UTF-8
Statyczna biblioteka parrot.

%package basic
Summary:	BASIC language
Summary(pl.UTF-8):Język BASIC
Group:		Development/Languages

%description basic
BASIC language.

%description basic -l pl.UTF-8
Język BASIC.

%package befunge
Summary:	Befunge language
Summary(pl.UTF-8):Język Befunge
Group:		Development/Languages

%description befunge
Befunge language.

%description befunge -l pl.UTF-8
Język Befunge

%package bf
Summary:	bf language
Summary(pl.UTF-8):Język bf
Group:		Development/Languages

%description bf
bf language.

%description bf -l pl.UTF-8
Język bf.

%package cola
Summary:	cola language
Summary(pl.UTF-8):Język cola
Group:		Development/Languages

%description cola
cola language.

%description cola -l pl.UTF-8
Język cola.

%package forth
Summary:	Forth language
Summary(pl.UTF-8):Język Forth
Group:		Development/Languages

%description forth
Forth language.

%description forth -l pl.UTF-8
Język Forth.

%package jako
Summary:	jako language
Summary(pl.UTF-8):Język jako
Group:		Development/Languages

%description jako
jako language.

%description jako -l pl.UTF-8
Język jako.

%package ook
Summary:	ook language
Summary(pl.UTF-8):Język ook
Group:		Development/Languages

%description ook
ook language.

%description ook -l pl.UTF-8
Język ook.

%package perl6
Summary:	Perl 6 language
Summary(pl.UTF-8):Język Perl 6
Group:		Development/Languages

%description perl6
Perl 6 language.

%description perl6 -l pl.UTF-8
Język Perl 6.

%package regex
Summary:	regex language
Summary(pl.UTF-8):Język regex
Group:		Development/Languages

%description regex
regex language.

%description regex -l pl.UTF-8
Język regex.

%package ruby
Summary:	Ruby language
Summary(pl.UTF-8):Język Ruby
Group:		Development/Languages

%description ruby
Ruby language.

%description ruby -l pl.UTF-8
Język Ruby.

%package scheme
Summary:	Scheme language
Summary(pl.UTF-8):Język Scheme
Group:		Development/Languages

%description scheme
Scheme language.

%description scheme -l pl.UTF-8
Język Scheme.

%prep
%setup -q

%build
%{__perl} Configure.pl --prefix=%{_libdir} \
	--optimize \
	--cc="%{__cc}"
%{__make} -j1
%{__make} -j1 -C docs html

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	PREFIX=%{_prefix} \
	EXEC_PREFIX=%{_exec_prefix} \
	BIN_DIR=%{_bindir} \
	LIB_DIR=%{_libdir} \
	INCLUDE_DIR=%{_includedir} \
	DOC_DIR=%{_datadir} \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -arl examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

install -d $RPM_BUILD_ROOT%{_docdir}/parrot

cp -arl docs/book $RPM_BUILD_ROOT%{_docdir}/parrot
cp -arl compilers $RPM_BUILD_ROOT%{_libdir}/parrot/%{version}
cp -arl tools $RPM_BUILD_ROOT%{_libdir}/parrot/%{version}
# PCT.pbc not installed ???
cp -arl runtime/parrot/library/PCT.pbc $RPM_BUILD_ROOT%{_libdir}/parrot/%{version}/library

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog NEWS README docs/html
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/parrot/%{version}/dynext/*.so
%dir %{_libdir}/parrot
%dir %{_libdir}/parrot/%{version}
%dir %{_libdir}/parrot/%{version}/compilers
%dir %{_libdir}/parrot/%{version}/compilers/imcc
%dir %{_libdir}/parrot/%{version}/compilers/json
%dir %{_libdir}/parrot/%{version}/compilers/ncigen
%dir %{_libdir}/parrot/%{version}/compilers/nqp
%dir %{_libdir}/parrot/%{version}/compilers/pct
%dir %{_libdir}/parrot/%{version}/compilers/pge
%dir %{_libdir}/parrot/%{version}/compilers/pge/PGE/
%dir %{_libdir}/parrot/%{version}/compilers/pirc
%dir %{_libdir}/parrot/%{version}/compilers/tge
%dir %{_libdir}/parrot/%{version}/dynext
%dir %{_libdir}/parrot/%{version}/languages
%dir %{_libdir}/parrot/%{version}/languages/pge
%dir %{_libdir}/parrot/%{version}/languages/pge/PGE
%dir %{_libdir}/parrot/%{version}/library
%dir %{_libdir}/parrot/%{version}/library/CGI
%dir %{_libdir}/parrot/%{version}/library/Config
%dir %{_libdir}/parrot/%{version}/library/Data
%dir %{_libdir}/parrot/%{version}/library/Data/Dumper
%dir %{_libdir}/parrot/%{version}/library/Digest
%dir %{_libdir}/parrot/%{version}/library/Getopt
%dir %{_libdir}/parrot/%{version}/library/HTTP
%dir %{_libdir}/parrot/%{version}/library/Math
%dir %{_libdir}/parrot/%{version}/library/Math/Random
%dir %{_libdir}/parrot/%{version}/library/MIME
%dir %{_libdir}/parrot/%{version}/library/NCI
%dir %{_libdir}/parrot/%{version}/library/Parrot
%dir %{_libdir}/parrot/%{version}/library/PGE
%dir %{_libdir}/parrot/%{version}/library/SDL
%dir %{_libdir}/parrot/%{version}/library/Stream
%dir %{_libdir}/parrot/%{version}/library/String
%dir %{_libdir}/parrot/%{version}/library/Tcl
%dir %{_libdir}/parrot/%{version}/library/Test
%dir %{_libdir}/parrot/%{version}/library/Test/Builder
%dir %{_libdir}/parrot/%{version}/library/YAML
%dir %{_libdir}/parrot/%{version}/library/YAML/Dumper
%dir %{_libdir}/parrot/%{version}/library/YAML/Parser
%dir %{_libdir}/parrot/%{version}/tools
%dir %{_libdir}/parrot/%{version}/tools/build
%dir %{_libdir}/parrot/%{version}/tools/dev
%dir %{_datadir}/parrot
%dir %{_datadir}/parrot/%{version}
%dir %{_datadir}/parrot/%{version}/pod
%dir %{_datadir}/parrot/%{version}/pod/ops
%dir %{_datadir}/parrot/%{version}/pod/pmc
%dir %{_datadir}/parrot/%{version}/pod/user
%dir %{_datadir}/parrot/%{version}/pod/user/pir
%dir %{_docdir}/parrot

%{_libdir}/parrot/%{version}/compilers/json/*.pir
%{_libdir}/parrot/%{version}/compilers/json/*.pbc
%{_libdir}/parrot/%{version}/compilers/json/JSON/*.pir
%{_libdir}/parrot/%{version}/compilers/json/JSON/*.pbc
%{_libdir}/parrot/%{version}/compilers/nqp/*.pir
%{_libdir}/parrot/%{version}/compilers/nqp/*.pbc
%{_libdir}/parrot/%{version}/compilers/pge/*.pir
%{_libdir}/parrot/%{version}/compilers/pge/*.pbc
%{_libdir}/parrot/%{version}/compilers/pge/PGE/*.pir
#%{_libdir}/parrot/%{version}/compilers/pge/PGE/*.pbc
%{_libdir}/parrot/%{version}/languages/pge/P6Rule.grammar
%{_libdir}/parrot/%{version}/languages/pge/STATUS
%{_libdir}/parrot/%{version}/languages/pge/*.pir
%{_libdir}/parrot/%{version}/languages/pge/PGE/*.pir
%{_libdir}/parrot/%{version}/languages/pge/PGE/builtins.pg
%{_libdir}/parrot/%{version}/library/*.pir
%{_libdir}/parrot/%{version}/library/*.pbc
%{_libdir}/parrot/%{version}/library/*.pasm
%{_libdir}/parrot/%{version}/library/*.declarations
%{_libdir}/parrot/%{version}/library/CGI/*.pir
%{_libdir}/parrot/%{version}/library/CGI/*.pbc
%{_libdir}/parrot/%{version}/library/Config/*.pir
%{_libdir}/parrot/%{version}/library/Data/*.pir
%{_libdir}/parrot/%{version}/library/Data/*.pbc
%{_libdir}/parrot/%{version}/library/Data/Dumper/*.pir
%{_libdir}/parrot/%{version}/library/Data/Dumper/*.pbc
%{_libdir}/parrot/%{version}/library/Digest/*.pir
%{_libdir}/parrot/%{version}/library/Getopt/*.pir
%{_libdir}/parrot/%{version}/library/Getopt/*.pbc
%{_libdir}/parrot/%{version}/library/HTTP/*.pir
%{_libdir}/parrot/%{version}/library/Math/*.pir
%{_libdir}/parrot/%{version}/library/Math/*.pbc
%{_libdir}/parrot/%{version}/library/Math/Random/*.pir
%{_libdir}/parrot/%{version}/library/Math/Random/*.pbc
%{_libdir}/parrot/%{version}/library/MIME/*.pir
%{_libdir}/parrot/%{version}/library/MIME/*.pbc
%{_libdir}/parrot/%{version}/library/NCI/*.pir
%{_libdir}/parrot/%{version}/library/NCI/*.pbc
%{_libdir}/parrot/%{version}/library/Parrot/*.pir
%{_libdir}/parrot/%{version}/library/Parrot/*.pbc
%{_libdir}/parrot/%{version}/library/PGE/*.pir
%{_libdir}/parrot/%{version}/library/PGE/*.pbc
%{_libdir}/parrot/%{version}/library/SDL/*.pir
%{_libdir}/parrot/%{version}/library/SDL/*.png
%{_libdir}/parrot/%{version}/library/Stream/*.pir
%{_libdir}/parrot/%{version}/library/Stream/*.pbc
%{_libdir}/parrot/%{version}/library/String/*.pir
%{_libdir}/parrot/%{version}/library/Tcl/*.pir
%{_libdir}/parrot/%{version}/library/Test/*.pir
%{_libdir}/parrot/%{version}/library/Test/Builder/*.pir
%{_libdir}/parrot/%{version}/library/YAML/*.pir
%{_libdir}/parrot/%{version}/library/YAML/Dumper/*.pir
%{_libdir}/parrot/%{version}/library/YAML/Parser/*.pir
%{_libdir}/parrot/%{version}/tools/build/*
%{_libdir}/parrot/%{version}/tools/dev/*
%{_datadir}/parrot/%{version}/LICENSE
%{_datadir}/parrot/%{version}/NEWS
%{_datadir}/parrot/%{version}/PBC_COMPAT
%{_datadir}/parrot/%{version}/RESPONSIBLE_PARTIES
%{_datadir}/parrot/%{version}/pod/*.pod
%{_datadir}/parrot/%{version}/pod/ops/*.pod
%{_datadir}/parrot/%{version}/pod/pmc/*.pod
%{_datadir}/parrot/%{version}/pod/user/pir/*.pod
%{_docdir}/parrot/book/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%dir %{_includedir}/%{name}
%dir %{_includedir}/%{name}/%{version}
%dir %{_includedir}/%{name}/%{version}/%{name}
%dir %{_includedir}/%{name}/%{version}/%{name}/atomic
%dir %{_includedir}/%{name}/%{version}/%{name}/oplib
%dir %{_libdir}/parrot/%{version}/include
%dir %{_pkgconfigdir}/%{name}
%dir %{_pkgconfigdir}/%{name}/%{version}
%{_libdir}/parrot/%{version}/include/*
%{_includedir}/%{name}/%{version}/%{name}/*.h
%{_includedir}/%{name}/%{version}/%{name}/atomic/*.h
%{_includedir}/%{name}/%{version}/%{name}/oplib/*.h
#%{_mandir}/man?/*
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*
%{_pkgconfigdir}/%{name}/%{version}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
