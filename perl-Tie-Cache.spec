%include	/usr/lib/rpm/macros.perl
Summary:	Tie-Cache perl module
Summary(pl):	Modu� perla Tie-Cache
Name:		perl-Tie-Cache
Version:	0.08
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Tie/Tie-Cache-%{version}.tar.gz
Patch:		perl-Tie-Cache-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie-Cache perl module. 

%description -l pl
Modu� perla Tie-Cache.

%prep
%setup -q -n Tie-Cache-%{version}
%patch -p1

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Tie/Cache
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,README}.gz

%{perl_sitelib}/Tie/Cache.pm
%{perl_sitearch}/auto/Tie/Cache

%{_mandir}/man3/*
