%include	/usr/lib/rpm/macros.perl
%define		pdir	Tie
%define		pnam	Cache
Summary:	Tie::Cache Perl module
Summary(cs):	Modul Tie::Cache pro Perl
Summary(da):	Perlmodul Tie::Cache
Summary(de):	Tie::Cache Perl Modul
Summary(es):	Módulo de Perl Tie::Cache
Summary(fr):	Module Perl Tie::Cache
Summary(it):	Modulo di Perl Tie::Cache
Summary(ja):	Tie::Cache Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Tie::Cache ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Tie::Cache
Summary(pl):	Modu³ perla Tie::Cache
Summary(pt_BR):	Módulo Perl Tie::Cache
Summary(pt):	Módulo de Perl Tie::Cache
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Tie::Cache
Summary(sv):	Tie::Cache Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Tie::Cache
Summary(zh_CN):	Tie::Cache Perl Ä£¿é
Name:		perl-Tie-Cache
Version:	0.17
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie::Cache perl module.

%description -l cs
Modul Tie::Cache pro Perl.

%description -l da
Perlmodul Tie::Cache.

%description -l de
Tie::Cache Perl Modul.

%description -l es
Módulo de Perl Tie::Cache.

%description -l fr
Module Perl Tie::Cache.

%description -l it
Modulo di Perl Tie::Cache.

%description -l ja
Tie::Cache Perl ¥â¥¸¥å¡¼¥ë

%description -l ko
Tie::Cache ÆÞ ¸ðÁÙ.

%description -l no
Perlmodul Tie::Cache.

%description -l pl
Modu³ perla Tie::Cache.

%description -l pt
Módulo de Perl Tie::Cache.

%description -l pt_BR
Módulo Perl Tie::Cache.

%description -l ru
íÏÄÕÌØ ÄÌÑ Perl Tie::Cache.

%description -l sv
Tie::Cache Perlmodul.

%description -l uk
íÏÄÕÌØ ÄÌÑ Perl Tie::Cache.

%description -l zh_CN
Tie::Cache Perl Ä£¿é

%package bench
Summary:	Berchmark comparing Tie::Cache and Tie::Cache::LRU Perl modules
Summary(pl):	Porównanie wydajno¶ci modu³ów Perla Tie::Cache i Tie::Cache::LRU
Group:		Development/Languages/Perl

%description bench
Berchmark comparing Tie::Cache and Tie::Cache::LRU Perl modules.

%description bench -l pl
Porównanie wydajno¶ci modu³ów Perla Tie::Cache i Tie::Cache::LRU.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_sitelib}/Tie/Cache.pm
%{_mandir}/man3/*

%files bench
%defattr(644,root,root,755)
%attr(755,root,root) %{perl_sitelib}/Tie/bench.pl
