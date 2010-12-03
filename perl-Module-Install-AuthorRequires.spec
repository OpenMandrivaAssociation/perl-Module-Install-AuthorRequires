%define upstream_name    Module-Install-AuthorRequires
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Declare author-only dependencies
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Install)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


