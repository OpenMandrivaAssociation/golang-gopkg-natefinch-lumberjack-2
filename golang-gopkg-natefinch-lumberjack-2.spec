# Run tests in check section
%bcond_without check

%global goipath         gopkg.in/natefinch/lumberjack.v2
%global forgeurl        https://github.com/natefinch/lumberjack
Version:                2.1

%global common_description %{expand:
Lumberjack is a Go package for writing logs to rolling files.

Lumberjack is intended to be one part of a logging infrastructure. It is not 
an all-in-one solution, but instead is a pluggable component at the bottom of 
the logging stack that simply controls the files to which logs are written.

Lumberjack plays well with any logging package that can write to an io.Writer, 
including the standard library's log package.

Lumberjack assumes that only one process is writing to the output files. Using 
the same lumberjack configuration from multiple processes on the same machine 
will result in improper behavior.}

%gometa

Name:           %{goname}
Release:        2%{?dist}
Summary:        Rolling logger for Go
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
BuildRequires: golang(github.com/BurntSushi/toml)
BuildRequires: golang(gopkg.in/yaml.v2)
%endif

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 13 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.1-1
- First package for Fedora

