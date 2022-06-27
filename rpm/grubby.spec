Name:       grubby
Summary:    Command line tool for updating bootloader configs
Version:    0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://git.fedorahosted.org/git/grubby.git
Source0:    %{name}-%{version}.tar.bz2
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
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%make_build

%install
%make_install

%files
%defattr(-,root,root,-)
%license COPYING
/sbin/installkernel
/sbin/new-kernel-pkg
/sbin/grubby
%doc %{_mandir}/man8/grubby.8*
