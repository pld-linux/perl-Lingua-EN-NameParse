%include	/usr/lib/rpm/macros.perl
Summary:	Lingua-EN-NameParse perl module
Summary(pl):	Modu³ perla Lingua-EN-NameParse
Name:		perl-Lingua-EN-NameParse
Version:	1.00
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Lingua/Lingua-EN-NameParse-%{version}.tar.gz
Patch:		perl-Lingua-EN-NameParse-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Parse-RecDescent
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Lingua-EN-NameParse - routines for manipulating a persons name.

%description -l pl
Lingua-EN-NameParse - umo¿liwia operacje na imionach osób.

%prep
%setup -q -n Lingua-EN-NameParse-%{version}
%patch -p0

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Lingua/EN/NameParse
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz demo.pl

%{perl_sitelib}/Lingua/EN/NameParse.pm
%{perl_sitearch}/auto/Lingua/EN/NameParse

%{_mandir}/man3/*
