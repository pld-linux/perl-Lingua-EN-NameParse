#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Lingua
%define		pnam	EN-NameParse
Summary:	Lingua::EN::NameParse perl module
Summary(pl.UTF-8):	Moduł perla Lingua::EN::NameParse
Name:		perl-Lingua-EN-NameParse
Version:	1.30
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2fb117124b587063fd1ca5de7d92bef5
Patch0:		%{name}-paths.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Parse-RecDescent
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lingua::EN::NameParse - routines for manipulating a persons name.

%description -l pl.UTF-8
Lingua::EN::NameParse - umożliwia operacje na imionach osób.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%{__perl} -i -pe 's,\r,,g' examples/demo.pl
%patch0 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/%{pdir}/EN/*.pm
%{perl_vendorlib}/%{pdir}/EN/NameParse
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
