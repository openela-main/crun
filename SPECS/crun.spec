Summary: OCI runtime written in C
Name: crun
Version: 1.8.4
Release: 2%{?dist}
Source0: https://github.com/containers/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0: 0001-criu-check-if-the-criu_join_ns_add-function-exists.patch
License: GPLv2+
URL: https://github.com/containers/crun
# https://fedoraproject.org/wiki/PackagingDrafts/Go#Go_Language_Architectures
ExclusiveArch: %{go_arches}
# We always run autogen.sh
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: python3
BuildRequires: git
BuildRequires: libcap-devel
BuildRequires: systemd-devel
BuildRequires: yajl-devel
BuildRequires: libseccomp-devel
BuildRequires: libselinux-devel
BuildRequires: criu-devel
BuildRequires: python3-libmount
BuildRequires: libtool
BuildRequires: /usr/bin/go-md2man
BuildRequires: libgcrypt-devel
Provides: oci-runtime
Recommends: criu >= 3.17.1
Recommends: criu-libs

%description
crun is a runtime for running OCI containers

%prep
%autosetup -Sgit -n %{name}-%{version}

%build
export CFLAGS="%{optflags} -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64"
./autogen.sh
%configure --disable-silent-rules

%make_build

%install
%make_install
rm -rf %{buildroot}%{_prefix}/lib*

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/*

%changelog
* Mon Apr 17 2023 Jindrich Novy <jnovy@redhat.com> - 1.8.4-2
- Apply additional criu fix
- Resolves: #2184221

* Fri Apr 14 2023 Jindrich Novy <jnovy@redhat.com> - 1.8.4-1
- update to https://github.com/containers/crun/releases/tag/1.8.4
- Resolves: #2184221

* Tue Apr 04 2023 Jindrich Novy <jnovy@redhat.com> - 1.8.1-3
- fix could not find symbol criu_set_lsm_mount_context in libcriu.so
- Resolves: #2184221

* Mon Mar 20 2023 Jindrich Novy <jnovy@redhat.com> - 1.8.1-2
- add BR: criu-devel
- Resolves: #2179195

* Tue Feb 28 2023 Jindrich Novy <jnovy@redhat.com> - 1.8.1-1
- update to https://github.com/containers/crun/releases/tag/1.8.1
- Related: #2123641

* Thu Feb 02 2023 Jindrich Novy <jnovy@redhat.com> - 1.8-1
- update to https://github.com/containers/crun/releases/tag/1.8
- Related: #2123641

* Thu Jan 05 2023 Jindrich Novy <jnovy@redhat.com> - 1.7.2-2
- require libgcrypt-devel and add criu weak dep
- Resolves: #2158084

* Wed Nov 30 2022 Jindrich Novy <jnovy@redhat.com> - 1.7.2-1
- update to https://github.com/containers/crun/releases/tag/1.7.2
- Related: #2123641

* Mon Nov 28 2022 Jindrich Novy <jnovy@redhat.com> - 1.7.1-1
- update to https://github.com/containers/crun/releases/tag/1.7.1
- Related: #2123641

* Tue Nov 08 2022 Jindrich Novy <jnovy@redhat.com> - 1.7-1
- update to https://github.com/containers/crun/releases/tag/1.7
- Related: #2123641

* Thu Sep 08 2022 Jindrich Novy <jnovy@redhat.com> - 1.6-1
- update to https://github.com/containers/crun/releases/tag/1.6
- Related: #2123641

* Tue Jul 26 2022 Jindrich Novy <jnovy@redhat.com> - 1.5-1
- update to https://github.com/containers/crun/releases/tag/1.5
- Related: #2061390

* Wed May 11 2022 Jindrich Novy <jnovy@redhat.com> - 1.4.5-2
- BuildRequires: /usr/bin/go-md2man
- Related: #2061390

* Wed Apr 27 2022 Jindrich Novy <jnovy@redhat.com> - 1.4.5-1
- update to https://github.com/containers/crun/releases/tag/1.4.5
- Related: #2061390

* Thu Mar 24 2022 Jindrich Novy <jnovy@redhat.com> - 1.4.4-1
- update to https://github.com/containers/crun/releases/tag/1.4.4
- Related: #2061390

* Mon Mar 07 2022 Jindrich Novy <jnovy@redhat.com> - 1.4.3-1
- update to https://github.com/containers/crun/releases/tag/1.4.3
- Related: #2061390

* Wed Jan 26 2022 Jindrich Novy <jnovy@redhat.com> - 1.4.2-1
- update to https://github.com/containers/crun/releases/tag/1.4.2
- Related: #2001445

* Fri Jan 14 2022 Jindrich Novy <jnovy@redhat.com> - 1.4.1-1
- update to https://github.com/containers/crun/releases/tag/1.4.1
- Related: #2001445

* Wed Dec 22 2021 Jindrich Novy <jnovy@redhat.com> - 1.4-1
- update to https://github.com/containers/crun/releases/tag/1.4
- Related: #2001445

* Mon Nov 08 2021 Jindrich Novy <jnovy@redhat.com> - 1.3-1
- update to https://github.com/containers/crun/releases/tag/1.3
- Related: #2001445

* Mon Oct 11 2021 Jindrich Novy <jnovy@redhat.com> - 1.2-1
- update to https://github.com/containers/crun/releases/tag/1.2
- Related: #2001445

* Mon Sep 27 2021 Jindrich Novy <jnovy@redhat.com> - 1.1-1
- update to https://github.com/containers/crun/releases/tag/1.1
- Related: #2001445

* Thu Aug 26 2021 Jindrich Novy <jnovy@redhat.com> - 1.0-1
- update to https://github.com/containers/crun/releases/tag/1.0
- Related: #1934415

* Fri Aug 06 2021 Jindrich Novy <jnovy@redhat.com> - 0.21-3
- remove BR: criu-devel and leave it just for RHEL9
- Related: #1934415

* Fri Aug 06 2021 Jindrich Novy <jnovy@redhat.com> - 0.21-2
- do not use versioned provide
- BR: criu-devel
- Related: #1934415

* Tue Jul 27 2021 Jindrich Novy <jnovy@redhat.com> - 0.21-1
- update to https://github.com/containers/crun/releases/tag/0.21
- Related: #1934415

* Thu Jun 10 2021 Jindrich Novy <jnovy@redhat.com> - 0.20.1-1
- update to https://github.com/containers/crun/releases/tag/0.20.1
- Related: #1934415

* Wed Jun 02 2021 Jindrich Novy <jnovy@redhat.com> - 0.20-1
- update to https://github.com/containers/crun/releases/tag/0.20
- Related: #1934415

* Mon Apr 26 2021 Jindrich Novy <jnovy@redhat.com> - 0.19.1-1
- update to https://github.com/containers/crun/releases/tag/0.19.1
- Related: #1934415

* Wed Apr 07 2021 Jindrich Novy <jnovy@redhat.com> - 0.19-2
- remove unused patch reference from spec
- Related: #1934415

* Tue Apr 06 2021 Jindrich Novy <jnovy@redhat.com> - 0.19-1
- update to https://github.com/containers/crun/releases/tag/0.19
- Related: #1934415

* Fri Feb 19 2021 Jindrich Novy <jnovy@redhat.com> - 0.18-1
- allow to build without glibc-static (thanks to Giuseppe Scrivano)
- Related: #1883490

* Fri Feb 19 2021 Jindrich Novy <jnovy@redhat.com> - 0.17-2
- reverting back to 0.17 as there's no glibc-static in RHEL
- Related: #1883490

* Fri Feb 19 2021 Jindrich Novy <jnovy@redhat.com> - 0.18-1
- update to https://github.com/containers/crun/releases/tag/0.18
- Related: #1883490

* Fri Jan 22 2021 Jindrich Novy <jnovy@redhat.com> - 0.17-1
- update to https://github.com/containers/crun/releases/tag/0.17
- Related: #1883490

* Thu Dec 03 2020 Jindrich Novy <jnovy@redhat.com> - 0.16-2
- exclude i686 because of build failures
- Related: #1883490

* Wed Nov 25 2020 Jindrich Novy <jnovy@redhat.com> - 0.16-1
- update to https://github.com/containers/crun/releases/tag/0.16
- Related: #1883490

* Wed Nov 04 2020 Jindrich Novy <jnovy@redhat.com> - 0.15.1-1
- update to https://github.com/containers/crun/releases/tag/0.15.1
- Related: #1883490

* Thu Oct 29 2020 Jindrich Novy <jnovy@redhat.com> - 0.15-2
- synchronize with stream-container-tools-rhel8
- Related: #1883490

* Wed Oct 21 2020 Jindrich Novy <jnovy@redhat.com> - 0.15-1
- synchronize with stream-container-tools-rhel8
- Related: #1883490

* Tue Aug 11 2020 Jindrich Novy <jnovy@redhat.com> - 0.14.1-2
- use proper CFLAGS
- Related: #1821193

* Wed Jul 08 2020 Jindrich Novy <jnovy@redhat.com> - 0.14.1-1
- update to https://github.com/containers/crun/releases/tag/v0.14.1
- Related: #1821193

* Thu Jul 02 2020 Jindrich Novy <jnovy@redhat.com> - 0.14-1
- update to https://github.com/containers/crun/releases/tag/v0.14
- Related: #1821193

* Tue Jun 16 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.13-1
- initial import
