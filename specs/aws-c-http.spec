Name:           aws-c-http
Version:        0.6.8 
Release:        1%{?dist}
Summary:        C99 implementation of the HTTP/1.1 and HTTP/2 specifications
Epoch:          1

License:        ASL-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  aws-c-common-devel = 1:0.6.14
BuildRequires:  aws-c-compression-devel = 1:0.2.14
BuildRequires:  aws-c-io-devel = 1:0.10.12

Requires:       aws-c-common-libs = 1:0.6.14
Requires:       aws-c-compression-libs = 1:0.2.14
Requires:       aws-c-io-libs = 1:0.10.12

%description
C99 implementation of the HTTP/1.1 and HTTP/2 specifications


%package libs
Summary:        C99 implementation of the HTTP/1.1 and HTTP/2 specifications
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description libs
C99 implementation of the HTTP/1.1 and HTTP/2 specifications


%package devel
Summary:        C99 implementation of the HTTP/1.1 and HTTP/2 specifications
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
C99 implementation of the HTTP/1.1 and HTTP/2 specifications


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

%{_bindir}/elasticurl

%files libs
%{_libdir}/libaws-c-http.so
%{_libdir}/libaws-c-http.so.1.0.0

%files devel
%{_includedir}/aws/http/*.h

%{_libdir}/aws-c-http/cmake/aws-c-http-config.cmake
%{_libdir}/aws-c-http/cmake/shared/aws-c-http-targets-noconfig.cmake
%{_libdir}/aws-c-http/cmake/shared/aws-c-http-targets.cmake


%changelog
* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com>
- 