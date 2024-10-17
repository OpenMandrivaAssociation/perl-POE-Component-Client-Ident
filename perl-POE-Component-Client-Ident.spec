%define upstream_name	 POE-Component-Client-Ident
%define upstream_version 1.16

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	A component that provides non-blocking ident lookups to your sessions
License:	GPL
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(POE)
BuildRequires:	perl(Test::POE::Server::TCP)
BuildArch:	noarch

%description
POE::Component::Client::Ident is a POE component that provides non-blocking
Ident lookup services to other components and sessions. The Ident protocol
is described in RFC 1413

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/POE
%{_mandir}/*/*


%changelog
* Tue Aug 04 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.160.0-2mdv2010.0
+ Revision: 408773
- force rebuild
- rebuild using %%perl_convert_version

* Thu May 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.16-1mdv2010.0
+ Revision: 378237
- update to new version 1.16

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.14-2mdv2009.0
+ Revision: 268700
- rebuild early 2009.0 package (before pixel changes)

* Tue Jun 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.14-1mdv2009.0
+ Revision: 214569
- new version

* Thu Mar 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.12-1mdv2008.1
+ Revision: 180603
- update to new version 1.12

* Sat Feb 02 2008 Funda Wang <fwang@mandriva.org> 1.10-1mdv2008.1
+ Revision: 161380
- update to new version 1.10

* Mon Jan 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-1mdv2008.1
+ Revision: 155673
- update to new version 1.08

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-1mdv2008.1
+ Revision: 105444
- new version
- update to new version 1.07

* Thu Aug 09 2007 Funda Wang <fwang@mandriva.org> 1.06-1mdv2008.0
+ Revision: 60697
- New version 1.06

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 1.05-1mdv2008.0
+ Revision: 20324
- 1.05


* Sat Dec 09 2006 Olivier Thauvin <nanardon@mandriva.org> 1.04-1mdv2007.0
+ Revision: 94357
- 1.04

* Tue Aug 08 2006 Olivier Thauvin <nanardon@mandriva.org> 1.01-1mdv2007.0
+ Revision: 54025
- Import perl-POE-Component-Client-Ident

* Tue May 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2007.0
- New release 1.01
- spec cleanup

* Mon May 01 2006 Olivier Thauvin <nanardon@mandriva.org> 1.00-1mdk
- 1.00

* Fri Mar 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.9-1mdk
- New release 0.9

* Fri Nov 04 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.8-1mdk
- 0.8

* Sat Oct 01 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.7-2mdk
- Buildrequires fix

* Thu Sep 08 2005 Olivier Thauvin <nanardon@mandriva.org> 0.7-1mdk
- First mandriva package

