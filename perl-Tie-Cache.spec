%define	pdir	Tie
%define	pnam	Cache
%include	/usr/lib/rpm/macros.perl
Summary:	Tie-Cache perl module
Summary(pl):	Modu³ perla Tie-Cache
Name:		perl-Tie-Cache
Version:	0.15
Release:	4

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie-Cache perl module.

%description -l pl
Modu³ perla Tie-Cache.

%prep
%setup -q -n Tie-Cache-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Tie/Cache.pm
%{_mandir}/man3/*
