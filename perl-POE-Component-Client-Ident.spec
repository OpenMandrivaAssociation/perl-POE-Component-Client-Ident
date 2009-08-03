%define upstream_name	 POE-Component-Client-Ident
%define upstream_version 1.16

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	A component that provides non-blocking ident lookups to your sessions
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl(POE)
BuildRequires:  perl(Test::POE::Server::TCP)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
POE::Component::Client::Ident is a POE component that provides non-blocking
Ident lookup services to other components and sessions. The Ident protocol
is described in RFC 1413

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
