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
Version:	1.20
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1f42c836ce96b1916b4d1a3016d5ffef
Patch0:		%{name}-paths.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Parse-RecDescent
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lingua::EN::NameParse - routines for manipulating a persons name.

%description -l pl.UTF-8
Lingua::EN::NameParse - umożliwia operacje na imionach osób.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README demo.pl
%{perl_vendorlib}/%{pdir}/EN/*.pm
%{_mandir}/man3/*
