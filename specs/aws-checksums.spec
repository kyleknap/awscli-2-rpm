Name:           aws-checksums
Version:        0.1.12 
Release:        1%{?dist}
Summary:        Checksum package for AWS SDK for C
Epoch:          1

License:        ASL-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  aws-c-common-devel = 1:0.6.14

Requires:       aws-c-common-libs = 1:0.6.14

%description
Checksum package for AWS SDK for C. Contains
Cross-Platform HW accelerated CRC32c and CRC32 with
fallback to efficient SW implementations.


%package libs
Summary:        Checksum package for AWS SDK for C
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
	
%description libs
Checksum package for AWS SDK for C. Contains
Cross-Platform HW accelerated CRC32c and CRC32 with
fallback to efficient SW implementations.


%package devel
Summary:        Checksum package for AWS SDK for C
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
Checksum package for AWS SDK for C. Contains
Cross-Platform HW accelerated CRC32c and CRC32 with
fallback to efficient SW implementations.


%prep
%autosetup


%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install


%files
%license LICENSE
%doc README.md

%files libs
%{_libdir}/libaws-checksums.so
%{_libdir}/libaws-checksums.so.1.0.0

%files devel
%{_includedir}/aws/checksums/*.h

%{_libdir}/aws-checksums/cmake/aws-checksums-config.cmake
%{_libdir}/aws-checksums/cmake/shared/aws-checksums-targets-noconfig.cmake
%{_libdir}/aws-checksums/cmake/shared/aws-checksums-targets.cmake


%changelog
* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com>
- 