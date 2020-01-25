#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Tie
%define		pnam	Cache
Summary:	Tie::Cache - LRU Cache in Memory
Summary(pl.UTF-8):	Tie::Cache - cache typu LRU w pamięci
Name:		perl-Tie-Cache
Version:	0.17
Release:	7
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	93f1bb8006815ade24fde309925cebe0
Patch0:		%{name}-paths.patch
URL:		http://search.cpan.org/dist/Tie-Cache/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a least recently used (LRU) cache in memory
through a tie interface. Any time data is stored in the tied hash,
that key/value pair has an entry time associated with it, and as the
cache fills up, those members of the cache that are the oldest are
removed to make room for new entries.

%description -l pl.UTF-8
Ten moduł jest implementacją cache typu LRU (ostatnio używane) w
pamięci poprzez powiązany interfejs. Wszystkie dane dotyczące czasu są
zapisywane w powiązanym haszu, którego para klucz/wartość ma
przydzielony wpis dotyczący czasu. Kiedy cache się zapełnia, te
najstarsze elementy są usuwane, aby zrobić miejsce nowym.

%package bench
Summary:	Berchmark comparing Tie::Cache and Tie::Cache::LRU Perl modules
Summary(pl.UTF-8):	Porównanie wydajności modułów Perla Tie::Cache i Tie::Cache::LRU
Group:		Development/Languages/Perl

%description bench
Berchmark comparing Tie::Cache and Tie::Cache::LRU Perl modules.

%description bench -l pl.UTF-8
Porównanie wydajności modułów Perla Tie::Cache i Tie::Cache::LRU.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

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
%doc CHANGES README
%{perl_vendorlib}/Tie/Cache.pm
%{_mandir}/man3/*

%files bench
%defattr(644,root,root,755)
%attr(755,root,root) %{perl_vendorlib}/Tie/bench.pl
