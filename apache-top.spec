Summary:	Provides real-time display of the active processes from a remote Apache HTTP server
Name:		apache-top
Version:	0.1
# date when fetched from git
Release:	0.20140604.2
License:	GPL v2
Group:		Applications/System
Source0:	http://www.isartor.org/w/images/3/39/Apache-top.py
# Source0-md5:	4843daed2cbac7346c31d6cf0fcf6c1b
URL:		http://www.isartor.org/wiki/Monitor_you_Apache_processes
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
apache-top provides real-time display of the active processes from a
remote Apache HTTP server. It's like the top Linux command.

With apache-top you can get:
- The active Apache processes with their associated PID, the status,
  the seconds being active, the CPU usage, the asociated VirtualHost,
  the accessing ip and the request (POST or GET, the file being accessed
  and the used protocol)
- The server uptime and the last time it was restarted
- The CPU usage
- Requests by second, Kb by second and the average Kb by request
- Number of active and inactive processes
- A graph with the inactive and active processes and their status

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/%{name}
%{__sed} -i -e '1s,^#!.*python,#!%{__python},' $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/apache-top
