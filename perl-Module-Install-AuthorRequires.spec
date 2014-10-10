%define upstream_name    Module-Install-AuthorRequires
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Declare author-only dependencies
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Module::Install)
BuildArch:	noarch

%description
Modules often have optional requirements, for example dependencies that are
useful for (optional) tests, but not required for the module to work
properly.

Usually you want all developers of a project to have these optional modules
installed. However, simply telling everyone or printing diagnostic messages
if optional dependencies are missing often isn't enough to make sure all
authors have all optional modules installed.

'Module::Install' already has a way of detecting an author environment, so
an easy way to achieve the above would be something like:

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
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 656938
- rebuild for updated spec-helper

* Fri Dec 03 2010 Shlomi Fish <shlomif@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 607070
- import perl-Module-Install-AuthorRequires

