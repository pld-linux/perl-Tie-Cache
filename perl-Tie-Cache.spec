%include	/usr/lib/rpm/macros.perl
%define		pdir	Tie
%define		pnam	Cache
Summary:	Tie::Cache - LRU Cache in Memory
Summary(pl):	Tie::Cache - cache typu LRU w pamiêci
Name:		perl-Tie-Cache
Version:	0.17
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a least recently used (LRU) cache in memory
through a tie interface. Any time data is stored in the tied hash,
that key/value pair has an entry time associated with it, and as the
cache fills up, those members of the cache that are the oldest are
removed to make room for new entries.

%description -l pl
Ten modu³ jest implementacj± cache typu LRU (ostatnio u¿ywane) w
pamiêci poprzez powi±zany interfejs. Wszytkie dane dotycz±ce czasu s±
zapisywane w powi±zanym haszu, którego para klucz/warto¶æ ma
przydzielony wpis dotycz±cy czasu. Kiedy cache siê zape³nia, te
najstarsze elementy s± usuwane, aby zrobiæ miejsce nowym.

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
