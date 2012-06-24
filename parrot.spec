Summary:	A virtual machine designed to execute bytecode for interpreted languages
Summary(pl):	Maszyna wirtualna przeznaczona do wykonywania bytecodu dla j�zyk�w interpretowanych
Name:		parrot
Version:	0.2.0
Release:	1
Epoch:		0
License:	GPL v2/Artistic
Group:		Libraries
Source0:	ftp://ftp.cpan.org/pub/CPAN/authors/id/L/LT/LTOETSCH/%{name}-%{version}.tar.gz
# Source0-md5:	ece59a572b67bea73ed8aa7230c253c2
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
bytecodu dla j�zyk�w interpretowanych. Parrot b�dzie celem kompilatora
Perla 6. Istnieje ju� cz�ciowy kompilator Perla 6, a tak�e
kompilatory w r�nych stopniach zaawansowania dla szerokiego zakresu
innych j�zyk�w.

%package devel
Summary:	Header files for parrot
Summary(pl):	Pliki nag��wkowe biblioteki parrot
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for parrot.

%description devel -l pl
Pliki nag��wkowe biblioteki parrot.

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
Summary(pl):	J�zyk BASIC
Group:		Development/Languages

%description basic
BASIC language.

%description basic -l pl
J�zyk BASIC.

%package befunge
Summary:	Befunge language
Summary(pl):	J�zyk Befunge
Group:		Development/Languages

%description befunge
Befunge language.

%description befunge -l pl
J�zyk Befunge

%package bf
Summary:	bf language
Summary(pl):	J�zyk bf
Group:		Development/Languages

%description bf
bf language.

%description bf -l pl
J�zyk bf.

%package cola
Summary:	cola language
Summary(pl):	J�zyk cola
Group:		Development/Languages

%description cola
cola language.

%description cola -l pl
J�zyk cola.

%package forth
Summary:	Forth language
Summary(pl):	J�zyk Forth
Group:		Development/Languages

%description forth
Forth language.

%description forth -l pl
J�zyk Forth.

%package jako
Summary:	jako language
Summary(pl):	J�zyk jako
Group:		Development/Languages

%description jako
jako language.

%description jako -l pl
J�zyk jako.

%package ook
Summary:	ook language
Summary(pl):	J�zyk ook
Group:		Development/Languages

%description ook
ook language.

%description ook -l pl
J�zyk ook.

%package perl6
Summary:	Perl 6 language
Summary(pl):	J�zyk Perl 6
Group:		Development/Languages

%description perl6
Perl 6 language.

%description perl6 -l pl
J�zyk Perl 6.

%package regex
Summary:	regex language
Summary(pl):	J�zyk regex
Group:		Development/Languages

%description regex
regex language.

%description regex -l pl
J�zyk regex.

%package ruby
Summary:	Ruby language
Summary(pl):	J�zyk Ruby
Group:		Development/Languages

%description ruby
Ruby language.

%description ruby -l pl
J�zyk Ruby.

%package scheme
Summary:	Scheme language
Summary(pl):	J�zyk Scheme
Group:		Development/Languages

%description scheme
Scheme language.

%description scheme -l pl
J�zyk Scheme.

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

%{__make} install \
	BUILDPREFIX=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	EXEC_PREFIX=%{_exec_prefix} \
	BINDIR=%{_bindir} \
	LIBDIR=%{_libdir} \
	INCLUDEDIR=%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ABI_CHANGES CREDITS ChangeLog README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
%{_mandir}/man?/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
