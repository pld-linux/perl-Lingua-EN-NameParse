%define	pdir	Lingua
%define	pnam	EN-NameParse
%include	/usr/lib/rpm/macros.perl
Summary:	Lingua-EN-NameParse perl module
Summary(pl):	Modu� perla Lingua-EN-NameParse
Name:		perl-Lingua-EN-NameParse
Version:	1.16
Release:	2

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Parse-RecDescent
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lingua-EN-NameParse - routines for manipulating a persons name.

%description -l pl
Lingua-EN-NameParse - umo�liwia operacje na imionach os�b.

%prep
%setup -q -n Lingua-EN-NameParse-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz demo.pl
%{perl_sitelib}/Lingua/EN/*.pm
%{_mandir}/man3/*
