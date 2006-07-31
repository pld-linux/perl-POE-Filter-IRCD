#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Filter-IRCD
Summary:	perl(POE::Filter::IRCD) - A POE−based parser for the IRC protocol.
Name:		perl-POE-Filter-IRCD
Version:	1.8
Release:	0.1
# note if it is "same as perl"
License:	(enter GPL/LGPL/BSD/BSD-like/Artistic/other license name here)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b6343b3d9e0e917550a57035d1474f92
URL:		http://search.cpan.org/dist/POE-Filter-IRCD
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
#%if %{with autodeps} || %{with tests}
BuildRequires:	perl-POE
#%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl module POE::Filter::IRCD provides a convenient way of parsing and creating
IRC protocol lines.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/POE/Filter/IRCD.pm
%{_mandir}/man3/*
