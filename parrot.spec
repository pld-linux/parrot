Summary:	A virtual machine designed to execute bytecode for interpreted languages
Name:		parrot
Version:	0.1.1
Release:	1
Epoch:		0
License:	BSD
Group:		Libraries
Source0:	ftp://ftp.cpan.org/pub/CPAN/authors/id/L/LT/LTOETSCH/%{name}-%{version}.tar.gz
# Source0-md5:	39991aee98df7b1249e44cced43403e3
BuildRequires:	perl-devel
URL:		http://www.parrotcode.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parrot is a virtual machine designed to execute bytecode for
interpreted languages efficiently. Parrot will be the target for the
Perl 6 compiler. There is already a partial Perl 6 compiler as well as
compilers in various stages of completion for a wide range of other
languages.

%package devel
Summary:	Header files and develpment documentation for parrot
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files and develpment documentation for parrot.

%package static
Summary:	Static parrot library
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static parrot library.

%package basic
Summary:	BASIC language
Group:		Development/Languages

%description basic
BASIC language

%package befunge
Summary:	befunge
Group:		Development/Languages

%description befunge
befunge

%package bf
Summary:	bf
Group:		Development/Languages

%description bf
bf

%package cola
Summary:	cola
Group:		Development/Languages

%description cola
cola

%package forth
Summary:	forth
Group:		Development/Languages

%description forth
forth

%package jako
Summary:	jako
Group:		Development/Languages

%description jako
jako

%package ook
Summary:	ook
Group:		Development/Languages

%description ook
ook

%package perl6
Summary:	perl6
Group:		Development/Languages

%description perl6
perl6

%package regex
Summary:	regex
Group:		Development/Languages

%description regex
regex

%package ruby
Summary:	ruby
Group:		Development/Languages

%description ruby
ruby

%package scheme
Summary:	scheme
Group:		Development/Languages

%description scheme
scheme

%prep
%setup -q

%build
%{__perl} \
	Configure.pl --optimize
%{__make} parrot pdb pdump \
	CC="%{__cc}" parrot pdb pdump
%{__make} -C imcc
%{__perl} \
	tools/dev/mk_manifests.pl \
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
%doc CHANGES CREDITS LICENSE README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
%{_mandir}/man?/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
