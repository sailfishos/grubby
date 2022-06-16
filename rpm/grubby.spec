# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       grubby

# >> macros
# << macros

Summary:    Command line tool for updating bootloader configs
Version:    0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://git.fedorahosted.org/git/grubby.git
Source0:    %{name}-%{version}.tar.bz2
Source100:  grubby.yaml
Patch0:     change-to-moblin-release.patch
Patch1:     more-support-code-for-syslinux.patch
Patch2:     set-default-kernel.patch
Patch3:     symbolic-link-to-kernel.patch
Patch4:     grubby_add_kboot.patch
Patch5:     support_linux_keyword.patch
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(popt)

%description
grubby  is  a command line tool for updating and displaying information about 
the configuration files for the grub, lilo, elilo (ia64),  yaboot (powerpc)  
and zipl (s390) boot loaders. It is primarily designed to be used from scripts
which install new kernels and need to find information about the current boot 
environment.



%prep
%setup -q -n %{name}-%{version}/%{name}

# change-to-moblin-release.patch
%patch0 -p1
# more-support-code-for-syslinux.patch
%patch1 -p1
# set-default-kernel.patch
%patch2 -p1
# symbolic-link-to-kernel.patch
%patch3 -p1
# grubby_add_kboot.patch
%patch4 -p1
# support_linux_keyword.patch
%patch5 -p1
# >> setup
# << setup

%build
# >> build pre
# << build pre


make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post


%files
%defattr(-,root,root,-)
# >> files
%license COPYING
%{_sbindir}/installkernel
%{_sbindir}/new-kernel-pkg
%{_sbindir}/grubby
%doc %{_mandir}/man8/grubby.8*
# << files
