#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Filter-IRCD
Summary:	POE::Filter::IRCD - a POE-based parser for the IRC protocol
Summary(pl.UTF-8):   POE::Filter::IRCD - oparty na POE analizator protokołu IRC
Name:		perl-POE-Filter-IRCD
Version:	2.1
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c14c685dc83a14c21666489df9be298d
URL:		http://search.cpan.org/dist/POE-Filter-IRCD/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-POE >= 1:0.3202
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl module POE::Filter::IRCD provides a convenient way of parsing and
creating IRC protocol lines.

%description -l pl.UTF-8
Moduł perla POE::Filter::IRCD udostępnia wygodny sposób analizy i
tworzenia linii protokołu IRC.

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
