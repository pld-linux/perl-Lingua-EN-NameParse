%include	/usr/lib/rpm/macros.perl
%define	pdir	Lingua
%define	pnam	EN-NameParse
Summary:	Lingua::EN::NameParse perl module
Summary(pl):	Modu³ perla Lingua::EN::NameParse
Name:		perl-Lingua-EN-NameParse
Version:	1.19
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1dd30adcfc9a95ff041c962012eb8c41
Patch0:		%{name}-paths.patch
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Parse-RecDescent
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lingua::EN::NameParse - routines for manipulating a persons name.

%description -l pl
Lingua::EN::NameParse - umo¿liwia operacje na imionach osób.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README demo.pl
%{perl_vendorlib}/%{pdir}/EN/*.pm
%{_mandir}/man3/*
