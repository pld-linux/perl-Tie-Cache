%include	/usr/lib/rpm/macros.perl
%define		pdir	Tie
%define		pnam	Cache
Summary:	Tie::Cache - LRU Cache in Memory
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
This module implements a least recently used (LRU) cache in memory through
a tie interface. Any time data is stored in the tied hash, that key/value
pair has an entry time associated with it, and as the cache fills up,
those members of the cache that are the oldest are removed to make room
for new entries.

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
