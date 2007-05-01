%define module	POE-Component-Client-Ident
%define name	perl-%{module}
%define version	1.05
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A component that provides non-blocking ident lookups to your sessions
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/POE/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl(POE)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
POE::Component::Client::Ident is a POE component that provides non-blocking
Ident lookup services to other components and sessions. The Ident protocol
is described in RFC 1413

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/POE
%_mandir/*/*



