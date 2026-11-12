#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module	pydantic_settings
Summary:	Settings management using Pydantic
Summary(pl.UTF-8):	Zarządzanie ustawieniami z użyciem Pydantic
Name:		python3-pydantic-settings
Version:	2.16.2
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pydantic-settings/
Source0:	https://files.pythonhosted.org/packages/source/p/pydantic-settings/%{module}-%{version}.tar.gz
# Source0-md5:	67010dabd98141ee3ed3173baf9e2bf8
URL:		https://github.com/pydantic/pydantic-settings
BuildRequires:	python3-build
BuildRequires:	python3-hatchling
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.11
%if %{with tests}
BuildRequires:	python3-dotenv >= 1.2.2
BuildRequires:	python3-pydantic >= 2.7.0
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-examples
BuildRequires:	python3-pytest-mock
BuildRequires:	python3-typing_extensions >= 4.0.0
BuildRequires:	python3-typing_inspection >= 0.4.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.11
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Settings management using Pydantic, taking advantage of Pydantic data
validation.

%description -l pl.UTF-8
Zarządzanie ustawieniami z użyciem Pydantic, wykorzystujące walidację
danych Pydantic.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_mock.plugin \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/pydantic_settings
%{py3_sitescriptdir}/pydantic_settings-%{version}.dist-info
